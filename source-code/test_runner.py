#!/usr/bin/env python3
"""
Automated Test Runner for HyperspectralForge Pro
Verifies 3D cube generation, exact lossless inter-band prediction, near-lossless quantization, SAM metrics, and 10-point normative auditor.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hyperspectral_cli import generate_cube, compress_cube, audit

class TestHyperspectralForge(unittest.TestCase):

    def setUp(self):
        self.w = 16
        self.h = 16
        self.b = 8
        self.cube = generate_cube(self.w, self.h, self.b)

    def test_01_cube_geometry(self):
        self.assertEqual(len(self.cube), self.b)
        self.assertEqual(len(self.cube[0]), self.w * self.h)

    def test_02_lossless_exact_reconstruction(self):
        res = compress_cube(self.cube, self.w, self.h, self.b, max_error=0)
        self.assertEqual(res["rmse"], 0.0)
        self.assertIn("Lossless", res["psnr"])
        self.assertEqual(res["max_error"], 0)

    def test_03_near_lossless_bounded_error(self):
        max_err = 3
        res = compress_cube(self.cube, self.w, self.h, self.b, max_error=max_err)
        self.assertLessEqual(res["rmse"], max_err * 1.5)
        self.assertGreater(float(res["achieved_bpp"]), 0.0)

    def test_04_spectral_angle_mapper_calculation(self):
        res = compress_cube(self.cube, self.w, self.h, self.b, max_error=0)
        self.assertTrue("°" in res["spectral_angle_mapper"])
        self.assertAlmostEqual(float(res["spectral_angle_mapper"].replace("°", "")), 0.0, places=2)

    def test_05_header_sync_word(self):
        res = compress_cube(self.cube, self.w, self.h, self.b)
        self.assertTrue(res["header_hex"].startswith("5A 73"))

    def test_06_compression_ratio_positive(self):
        res = compress_cube(self.cube, self.w, self.h, self.b)
        self.assertLess(res["compressed_bytes"], res["original_bytes"])
        self.assertTrue(":1" in res["compression_ratio"])

    def test_07_dynamic_range_bounds(self):
        for band in self.cube:
            for val in band:
                self.assertTrue(0 <= val <= 4095)

    def test_08_normative_auditor_compliance(self):
        report = audit()
        self.assertEqual(report["status"], "PASSED")
        self.assertEqual(report["score"], "10/10 Normative Rules Compliant")
        self.assertEqual(len(report["rules"]), 10)

    def test_09_single_band_edge_case(self):
        single_cube = generate_cube(self.w, self.h, 1)
        res = compress_cube(single_cube, self.w, self.h, 1)
        self.assertEqual(res["bands"], 1)

    def test_10_large_error_near_lossless_decay(self):
        res_lossless = compress_cube(self.cube, self.w, self.h, self.b, max_error=0)
        res_lossy = compress_cube(self.cube, self.w, self.h, self.b, max_error=10)
        self.assertLess(res_lossy["compressed_bytes"], res_lossless["compressed_bytes"])

if __name__ == "__main__":
    unittest.main()
