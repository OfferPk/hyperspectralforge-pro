\# CCSDS 123.0-B-2 Multispectral & Hyperspectral Image Compression Specification

\#\# 1\. Scope & Spacecraft Applications  
The \*\*Consultative Committee for Space Data Systems (CCSDS)\*\* Recommendation \*\*CCSDS 123.0-B-2\*\* (and international standard \*\*ISO 18381\*\*) defines a low-complexity lossless and near-lossless compression algorithm for 3D multispectral and hyperspectral image data cubes.

Hyperspectral sensors onboard satellites and spacecraft (such as NASA EMIT, PACE, ESA Copernicus Sentinel-2 / CHIME, and commercial constellations like Pixxel) capture hundreds of narrow, contiguous spectral bands across visible, near-infrared (VNIR), shortwave infrared (SWIR), and thermal infrared (TIR) regions. CCSDS 123.0-B-2 exploits the extreme cross-band correlation to achieve high compression ratios with zero or tightly bounded radiometric distortion.

\---

\#\# 2\. Core Functional Pipeline  
The compression architecture comprises three sequential processing stages:  
1\. \*\*Adaptive Spatial & Spectral Prediction\*\*:  
   \- Calculates a spatial local sum \$\\sigma\_{z,y,x}\$ from neighboring samples.  
   \- Combines spatial difference components and past spectral band differences into a directional prediction vector \$U\_{z,y,x}\$.  
   \- Computes predicted sample value \$\\hat{s}\_{z,y,x}\$ using an adaptive weight vector updated via Sign-LMS gradient rules.  
2\. \*\*Near-Lossless Quantization\*\*:  
   \- Applies user-defined maximum error limit \$m\_z \\ge 0\$.  
   \- When \$m\_z \= 0\$, compression is mathematically exact lossless.  
   \- When \$m\_z \> 0\$, absolute distortion is strictly bounded: \$\|s'\_{z,y,x} \- s\_{z,y,x}\| \\le m\_z\$.  
3\. \*\*Sample-Adaptive Entropy Coding\*\*:  
   \- Converts prediction residuals into non-negative integers via adaptive Rice / Golomb-power-of-two coding.

\---

\#\# 3\. Essential Header Bitstream Structure  
\- \*\*Sync Marker\*\*: 16-bit word (\`0x5A73\`).  
\- \*\*Image Geometry\*\*: Spectral Bands \$N\_z\$ (16 bits), Width \$N\_x\$ (16 bits), Height \$N\_y\$ (16 bits).  
\- \*\*Sample Bit Depth\*\*: Dynamic range \$D\$ (2 to 16 bits).  
\- \*\*Error Limits\*\*: Maximum error bound \$m\_z\$.  
\- \*\*Predictor Configuration\*\*: Full vs reduced prediction mode, neighbor vs column local sum.  
