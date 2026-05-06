---
aid: tensorflow
name: TensorFlow
description: TensorFlow is an end-to-end open source machine learning platform developed by Google. It provides a comprehensive ecosystem of tools, libraries, and community resources for building and deploying ML-powered applications, including model training, serving, mobile/edge deployment, and a hub of pre-trained models. TensorFlow Serving exposes REST and gRPC APIs for production model inference.
type: Index
image: https://www.tensorflow.org/images/tf_logo_social.png
tags:
  - AI
  - Deep Learning
  - JavaScript
  - Machine Learning
  - Model Serving
  - Neural Networks
  - Open Source
  - Python
url: https://raw.githubusercontent.com/api-evangelist/tensorflow/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tensorflow:tensorflow-serving-rest
    name: TensorFlow Serving REST API
    description: A flexible, high-performance serving system for machine learning models designed for production environments. Provides REST endpoints for model status, metadata, classification, regression, and prediction inference.
    humanURL: https://www.tensorflow.org/tfx/serving/api_rest
    baseURL: http://host:8501
    tags:
      - Inference
      - Model Serving
      - Production
      - REST API
    properties:
      - type: Documentation
        url: https://www.tensorflow.org/tfx/serving/api_rest
      - type: GitHub
        url: https://github.com/tensorflow/serving
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tensorflow/refs/heads/main/openapi/tensorflow-serving-openapi.yml
  - aid: tensorflow:tensorflow-core
    name: TensorFlow Core API
    description: The foundational Python and C++ API for building and training machine learning models using TensorFlow.
    humanURL: https://www.tensorflow.org/api_docs/python/tf
    baseURL: https://www.tensorflow.org/api_docs
    tags:
      - Core API
      - Machine Learning
      - Python
    properties:
      - type: Documentation
        url: https://www.tensorflow.org/api_docs/python/tf
      - type: Tutorial
        url: https://www.tensorflow.org/tutorials
      - type: GitHub
        url: https://github.com/tensorflow/tensorflow
      - type: Guide
        url: https://www.tensorflow.org/guide
  - aid: tensorflow:tensorflow-js
    name: TensorFlow.js API
    description: A JavaScript library for training and deploying ML models in the browser and on Node.js.
    humanURL: https://js.tensorflow.org/
    baseURL: https://cdn.jsdelivr.net/npm/@tensorflow/tfjs
    tags:
      - Browser
      - JavaScript
      - Node.js
    properties:
      - type: Documentation
        url: https://js.tensorflow.org/api/latest/
      - type: Tutorial
        url: https://js.tensorflow.org/tutorials/
      - type: GitHub
        url: https://github.com/tensorflow/tfjs
      - type: NPM
        url: https://www.npmjs.com/package/@tensorflow/tfjs
  - aid: tensorflow:tensorflow-lite
    name: TensorFlow Lite API
    description: Lightweight solution for ML inference on mobile and embedded devices, optimized for on-device model execution.
    humanURL: https://www.tensorflow.org/lite
    baseURL: https://www.tensorflow.org/lite/api_docs
    tags:
      - Edge Computing
      - Embedded
      - Mobile
      - On-Device AI
    properties:
      - type: Documentation
        url: https://www.tensorflow.org/lite/api_docs
      - type: Guide
        url: https://www.tensorflow.org/lite/guide
      - type: Examples
        url: https://www.tensorflow.org/lite/examples
      - type: GitHub
        url: https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite
  - aid: tensorflow:tensorflow-hub
    name: TensorFlow Hub API
    description: A library and repository of reusable pre-trained machine learning modules, enabling transfer learning across text, image, video, and audio domains.
    humanURL: https://tfhub.dev/
    baseURL: https://tfhub.dev/
    tags:
      - Model Repository
      - Pre-Trained Models
      - Transfer Learning
    properties:
      - type: Documentation
        url: https://www.tensorflow.org/hub/api_docs/python/hub
      - type: Models
        url: https://tfhub.dev/
      - type: GitHub
        url: https://github.com/tensorflow/hub
  - aid: tensorflow:tensorboard
    name: TensorBoard API
    description: TensorFlow's visualization toolkit for experiment tracking, model debugging, and performance profiling via an embedded web server with REST endpoints.
    humanURL: https://www.tensorflow.org/tensorboard
    tags:
      - Model Debugging
      - Monitoring
      - Visualization
    properties:
      - type: Documentation
        url: https://www.tensorflow.org/tensorboard/get_started
      - type: GitHub
        url: https://github.com/tensorflow/tensorboard
maintainers:
  - FN: Google Brain Team
    email: tensorflow@googlegroups.com
    url: https://www.tensorflow.org/
include:
  - name: TensorFlow Community
    url: https://www.tensorflow.org/community
common:
  - type: Blog
    url: https://blog.tensorflow.org/
  - type: GitHub Org
    url: https://github.com/tensorflow
  - type: Twitter
    url: https://twitter.com/tensorflow
  - type: YouTube
    url: https://www.youtube.com/tensorflow
  - type: License
    url: https://github.com/tensorflow/tensorflow/blob/master/LICENSE
  - type: Forum
    url: https://discuss.tensorflow.org/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/tensorflow
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/tensorflow/refs/heads/main/openapi/tensorflow-serving-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tensorflow/refs/heads/main/vocabulary/tensorflow-vocabulary.yml
---
