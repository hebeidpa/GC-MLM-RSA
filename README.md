# GC-MLM-RCSA

# Multimodal Radiopathomics Model Predicts Postoperative Metachronous Liver Metastasis in Gastric Cancer

## Overview
This project mainly covers two core functionalities:
- GastricNN-UNet: A nnU-Net-based CT segmentation model for gastric medical imaging.
- Pathomic Framework: Extracting features from whole slide images (WSIs)  using CLAM(https://github.com/mahmoodlab/CLAM).

## Directory Structure
```plaintext
train.py
test.py
feature_extractor.py
```Overview
1. GastricNN-UNet
A customized implementation of the nnU-Net framework for 3D CT image segmentation focusing on gastric structures. Key features:

Preprocessing pipelines optimized for abdominal CT scans

Configuration files for gastric organ/tumor segmentation

Trained model weights (optional, contact for access)

2. Pathomic Framework
A computational pathology toolkit for feature extraction from histopathology images, including:

Handcrafted feature calculation (e.g., texture, morphology)

Deep feature extraction via pretrained encoders

Feature fusion and dimensionality reduction

Installation
Requirements
Python 3.8+

PyTorch 1.9+

MONAI 0.8+

SimpleITK
