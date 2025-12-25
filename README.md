# GC-MLM-RCSA

## Multimodal Radiopathomics for Postoperative Metachronous Liver Metastasis Prediction in Gastric Cancer

This repository contains the reference implementation of **GC-MLM-RCSA**, a multimodal deep learning framework for predicting **postoperative metachronous liver metastasis (MLM)** in patients with gastric cancer by integrating **radiological computed tomography (CT)** and **histopathological whole-slide images (WSIs)**.

The framework is designed for research purposes and aims to explore the complementary value of radiological and pathological information for individualized postoperative risk assessment.

---

## Introduction

Despite curative gastrectomy, a substantial proportion of gastric cancer patients develop metachronous liver metastasis, which severely affects long-term survival. Accurate postoperative risk stratification remains challenging due to the heterogeneous biological behavior of tumors.

Radiological images provide macroscopic information about tumor morphology and surrounding tissues, while histopathological whole-slide images capture microscopic tumor characteristics. However, models based on a single modality are often insufficient to comprehensively characterize tumor heterogeneity.

To address this issue, we propose a **multimodal radiopathomics framework** that jointly models radiological and pathological data to predict postoperative MLM risk.

---

## Framework Overview

The proposed GC-MLM-RCSA framework consists of three main components:

1. **Radiology Branch**
   - Automatic segmentation of gastric regions on CT images
   - Extraction of deep radiological features from segmented regions

2. **Pathology Branch**
   - Patch-level feature extraction from WSIs
   - Slide-level representation learning using multiple instance learning

3. **Multimodal Prediction Module**
   - Patient-level feature alignment
   - Feature fusion and dimensionality reduction
   - Final classification for MLM risk prediction

---

## Workflow
