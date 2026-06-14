# Neural Networks for the Detection of COVID-19 and Other Diseases: Prospects and Challenges

Official repository accompanying the review paper: **"Neural Networks for the Detection of COVID-19 and Other Diseases: Prospects and Challenges"**

**Authors:** Muhammad Azeem, Shumaila Javaid, Ruhul Amin Khalil, Hamza Fahim, Turke Althobaiti, Nasser Alsharif, and Nasir Saeed 

**Institution:** University of Salford, Manchester, England, UK.  

**DOI:** (https://doi.org/10.3390/bioengineering10070850)

---

## Abstract
Artificial neural networks (ANNs) ability to learn, correct errors, and transform a large amount of raw data into beneficial medical decisions for treatment and care has increased in popularity for enhanced patient safety and quality of care. Therefore, this paper reviews the critical role of ANNs in providing valuable insights for patients’ healthcare decisions and efficient disease diagnosis. We study different types of ANNs in the existing literature that advance ANNs’ adaptation for complex applications. Specifically, we investigate ANNs’ advances for predicting viral, cancer, skin, and COVID-19 diseases. Furthermore, we propose a deep convolutional neural network (CNN) model called ConXNet, based on chest radiography images, to improve the detection accuracy of COVID-19 disease. ConXNet is trained and tested using a chest radiography image dataset obtained from Kaggle, achieving more than 97% accuracy and 98% precision, which is better than other existing state-of-the-art models, such as DeTraC, U-Net, COVID MTNet, and COVID-Net, having 93.1%, 94.10%, 84.76%, and 90% accuracy and 94%, 95%, 85%, and 92% precision, respectively. The results show that the ConXNet model performed significantly well for a relatively large dataset compared with the aforementioned models. Moreover, the ConXNet model reduces the time complexity by using dropout layers and batch normalization techniques. Finally, we highlight future research directions and challenges, such as the complexity of the algorithms, insufficient available data, privacy and security, and integration of biosensing with ANNs. These research directions require considerable attention for improving the scope of ANNs for medical diagnostic and treatment applications.

---

## Key Contributions
* **Comprehensive Multi-Disease Taxonomy:** Outlines the application of modern ANN frameworks across various modalities for infectious diseases (COVID-19) and non-communicable conditions (malignancies, dermatological diseases).
* **Multi-Modal Diagnostic Survey:** Evaluates and contrasts image-based diagnostics (X-Rays, CT scans, ultrasound) against non-image-based inputs (blood biomarkers, clinical text, and epidemiological series).
* **In-Depth Challenge Mapping:** Systematically classifies technical bottlenecks into four critical dimensions: algorithm selection, computational complexity, data deficiency/scarcity, and biosensing system integration.
* **Future Deployment Horizons:** Synthesizes actionable research directions such as network pruning, data augmentation standards, and standardized privacy-preserving mechanisms for real-world clinical integration.

---

## Technical Overview
The paper tracks the end-to-end integration of artificial neural networks within medical diagnostic pipelines:

1. **Data Acquisition & Pre-processing:** Collection of heterogeneous modalities including Computed Tomography (CT), chest X-rays, ultrasound imaging, and biochemical blood profiles.
2. **Feature Extraction:** Leveraging Deep Convolutional Neural Networks (CNNs) and Hybrid Architectures to extract spatial and structural markers from clinical inputs.
3. **Classification & Segmentation:** Deploying supervised, unsupervised, and deep transfer learning algorithms to isolate lesions, classify disease severity, or predict epidemiological spread.
4. **Optimization Mechanisms:** Exploring methods like dropout layers, network pruning, and data transformation strategies to maximize accuracy while mitigating resource consumption.

---

## Installation & Setup

We recommend utilizing an Anaconda environment to manage dependencies and reproducibility.

### Environment Creation
```bash
conda create -n neural-disease-det python=3.10 -y
conda activate neural-disease-det
