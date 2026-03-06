## Workshop 5

## Workshop Name: Regulatory Text Analysis with LLMs

## Description 

Use a large language model (LLM) to analyze regulatory text and evaluate performance differences between full-precision and quantized models.

## Targeted Courses 

Regulatory Compliance, Natural Language Processing, AI in Law

## Activities 

### Pre-lab Content Dissemination 

In this pre-lab activity, we will understand how LLMs can be used to analyze regulatory texts for compliance, risk identification, or information extraction. We will focus on using the **Mistral 7B** model.

Quantization is a technique to reduce the memory footprint of LLMs by using fewer bits to represent model weights (e.g., 4-bit instead of FP16). This can improve runtime efficiency but may affect precision and recall.

### In-class Hands-on Experience 

- Install the necessary Python packages for running Mistral 7B (e.g., `transformers`, `torch`, `accelerate`)  
- Load Mistral 7B in FP16 precision  
- Run the model on a regulatory text dataset and record:
  - **Precision (FP16)**
  - **Recall (FP16)**  

### Post Lab Experience 
- Quantize the model to 4-bit precision
- Load the 4-bit model using bitsandbytes quantization
  
**Reference:**
https://huggingface.co/docs/transformers/quantization/bitsandbytes

- Run the model again on the same dataset and record:
  - **Precision (4-bit)**
  - **Recall (4-bit)**  
- Compare the runtime of FP16 vs 4-bit runs
- Summarize your observations in a report:  
  - Compare precision and recall between FP16 and 4-bit quantized models  
  - Note any differences in runtime and memory usage  
  - Discuss potential trade-offs when using quantized models in regulatory text analysis  
- Upload the report on Assignment 5 @ CANVAS  
- Due: Mar 16, 2026









