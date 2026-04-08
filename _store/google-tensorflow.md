---
aid: google-tensorflow
url: https://raw.githubusercontent.com/api-evangelist/google-tensorflow/refs/heads/main/apis.yml
apis:
- name: TensorFlow Serving REST API
  description: TensorFlow Serving provides a REST API for serving trained TensorFlow models in production environments. The API supports model prediction (inference), classification, and regression requests against deployed models. It allows specifying model names and versions, and returns predictions in JSON format. TensorFlow Serving handles model lifecycle management, versioning, and concurrent request processing.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.tensorflow.org/tfx/serving/api_rest
  baseURL: http://localhost:8501
  tags:
  - Inference
  - Model Serving
  - Predictions
  properties:
  - type: Documentation
    url: https://www.tensorflow.org/tfx/serving/api_rest
  - type: OpenAPI
    url: openapi/tensorflow-serving-openapi.yml
  - type: JSONSchema
    url: json-schema/google-tensorflow-predict-request-schema.json
- name: TensorFlow Hub API
  description: TensorFlow Hub provides a repository of reusable trained machine learning models. The API allows developers to search, discover, and download pre-trained models and model components (SavedModels, TF.js models, TFLite models) that can be reused for transfer learning and inference in new applications.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://tfhub.dev
  baseURL: https://tfhub.dev
  tags:
  - Models
  - Pre-Trained Models
  - Transfer Learning
  properties:
  - type: Documentation
    url: https://www.tensorflow.org/hub
- name: TensorFlow Model Analysis API
  description: TensorFlow Model Analysis (TFMA) provides tools and APIs for evaluating TensorFlow models. It enables computing metrics over large datasets using Apache Beam, slicing evaluation results across different features, and tracking model performance over time for validation and monitoring purposes.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.tensorflow.org/tfx/model_analysis/get_started
  baseURL: https://localhost
  tags:
  - Analysis
  - Metrics
  - Model Evaluation
  properties:
  - type: Documentation
    url: https://www.tensorflow.org/tfx/model_analysis/get_started
name: Google TensorFlow
tags:
- AI
- Deep Learning
- Google
- Machine Learning
- Model Serving
- Open Source
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google TensorFlow is an open-source machine learning framework providing APIs and tools for building, training, and deploying ML models, including TensorFlow Serving for model inference and TensorFlow Hub for reusable model components.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

