\# HyperspectralForge Pro (v1.0.0)  
\#\#\# CCSDS 123.0-B-2 & ISO 18381 Spacecraft Multispectral & Hyperspectral Image Compression Studio

HyperspectralForge Pro is an aerospace-grade developer studio, adaptive 3D spectral predictor, near-lossless error quantizer, sample-adaptive Golomb-power-of-two entropy coder, Spectral Angle Mapper (SAM) analyzer, and 10-point normative compliance auditor designed for Earth observation satellites, airborne hyperspectral cameras, and planetary exploration imaging instruments.

\---

\#\# 🌟 Key Capabilities  
\- \*\*Adaptive Inter-Band Spectral Predictor\*\*: Implements neighbor spatial local sum and adaptive Sign-LMS weight vectors across spectral channels to exploit high inter-band correlation.  
\- \*\*Bounded Near-Lossless Quantization\*\*: User-configurable maximum absolute error limit \$m\_z\$ per spectral band (\$m\_z \= 0\$ for exact lossless reconstruction, \$m\_z \> 0\$ for maximum bounded error \$\\pm m\_z\$).  
\- \*\*Sample-Adaptive Entropy Coding\*\*: Low-complexity variable-length Golomb-power-of-two code symbol generation designed for high throughput on radiation-hardened flight processors.  
\- \*\*Spectral Angle Mapper (SAM) Quality Verification\*\*: Evaluates full 3D spectral vector fidelity (\$	heta \< 2.0^\\circ\$), PSNR in dB, RMSE, and compression ratios.  
\- \*\*CCSDS 123.0-B-2 Essential Header Packing\*\*: Serializes 16-bit sync word \`0x5A73\`, spatial dimensions, spectral band counts (\$1 \\le N\_z \\le 65536\$), and dynamic range (2 to 16 bits).  
\- \*\*10-Point Normative Auditor\*\*: Automated verification engine enforcing rules \`HYP-001\` through \`HYP-010\` per official CCSDS Blue Book standards.

\---

\#\# 📂 Project Structure  
\`\`\`text  
hyperspectral-forge-pro/  
├── source-code/  
│   ├── hyperspectral-engine.js  \# Core 3D adaptive predictor, quantizer & SAM engine  
│   ├── hyperspectral-auditor.js \# 10-point normative compliance auditor  
│   ├── hyperspectral\_cli.py     \# Python 3 CLI executable  
│   ├── hyperspectral-cli.py     \# Python 3 CLI alias  
│   ├── test\_runner.py           \# 10-suite unit test runner  
│   └── index.html               \# Interactive Mission Control operations console  
├── build/  
│   └── hyperspectral-forge-pro-v1.0.0.zip \# Standalone production bundle  
├── documentation/  
│   ├── CCSDS\_HYPERSPECTRAL\_SPECIFICATION.md \# Normative protocol specification  
│   └── HYPERSPECTRAL\_COMPLIANCE\_MATRIX.md   \# 10-point requirement traceability  
└── screenshots/  
    ├── architecture-diagram.svg             \# System architecture diagram  
    └── hyperspectral-studio-preview.svg     \# Operations studio interface preview  
\`\`\`

\---

\#\# 🚀 Quick Start

\#\#\# Running Automated Tests  
\`\`\`bash  
python3 source-code/test\_runner.py \-v  
\`\`\`

\#\#\# Command Line Interface  
\`\`\`bash  
\# Compress synthesized hyperspectral cube in exact lossless mode (m\_z \= 0\)  
python3 source-code/hyperspectral\_cli.py \--mode compress \--width 16 \--height 16 \--bands 8 \--error 0

\# Compress in near-lossless mode with bounded absolute error (m\_z \= 3\)  
python3 source-code/hyperspectral\_cli.py \--mode compress \--width 16 \--height 16 \--bands 8 \--error 3

\# Run 10-Point Normative Compliance Audit  
python3 source-code/hyperspectral\_cli.py \--mode audit  
\`\`\`

\#\#\# Launching the Web Operations Console  
Open \`source-code/index.html\` in any modern web browser to access live 3D spectral slice visualization, band profile browsing, and real-time compliance auditing.  
