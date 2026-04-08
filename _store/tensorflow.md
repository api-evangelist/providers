---
aid: tensorflow
url: https://raw.githubusercontent.com/api-evangelist/tensorflow/refs/heads/main/apis.yml
apis:
- name: TensorFlow Core API
  description: The foundational API for building and training machine learning models using TensorFlow.
  image: https://www.tensorflow.org/images/tf_logo_social.png
  humanURL: https://www.tensorflow.org/api_docs/python/tf
  baseURL: https://www.tensorflow.org/api_docs
  tags:
  - Core API
  - Machine Learning
  - Python
  properties:
  - type: X-documentation
    url: https://www.tensorflow.org/api_docs/python/tf
  - type: X-tutorial
    url: https://www.tensorflow.org/tutorials
  - type: X-github
    url: https://github.com/tensorflow/tensorflow
  - type: X-guide
    url: https://www.tensorflow.org/guide
- name: TensorFlow.js API
  description: A JavaScript library for training and deploying ML models in the browser and on Node.js.
  image: https://www.tensorflow.org/images/tf_logo_social.png
  humanURL: https://js.tensorflow.org/
  baseURL: https://cdn.jsdelivr.net/npm/@tensorflow/tfjs
  tags:
  - Browser
  - JavaScript
  - Node.js
  properties:
  - type: X-documentation
    url: https://js.tensorflow.org/api/latest/
  - type: X-tutorial
    url: https://js.tensorflow.org/tutorials/
  - type: X-github
    url: https://github.com/tensorflow/tfjs
  - type: X-npm
    url: https://www.npmjs.com/package/@tensorflow/tfjs
- name: TensorFlow Lite API
  description: Lightweight solution for mobile and embedded devices.
  image: https://www.tensorflow.org/images/tf_logo_social.png
  humanURL: https://www.tensorflow.org/lite
  baseURL: https://www.tensorflow.org/lite/api_docs
  tags:
  - Edge Computing
  - Embedded
  - Mobile
  properties:
  - type: X-documentation
    url: https://www.tensorflow.org/lite/api_docs
  - type: X-guide
    url: https://www.tensorflow.org/lite/guide
  - type: X-examples
    url: https://www.tensorflow.org/lite/examples
  - type: X-github
    url: https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite
- name: TensorFlow Serving API
  description: A flexible, high-performance serving system for machine learning models, designed for production environments.
  image: https://www.tensorflow.org/images/tf_logo_social.png
  humanURL: https://www.tensorflow.org/tfx/guide/serving
  baseURL: https://www.tensorflow.org/tfx/serving
  tags:
  - gRPC
  - Model Serving
  - Production
  - REST API
  properties:
  - type: X-documentation
    url: https://www.tensorflow.org/tfx/serving/api_docs/cc/
  - type: X-rest-api
    url: https://www.tensorflow.org/tfx/serving/api_rest
  - type: X-grpc-api
    url: https://www.tensorflow.org/tfx/serving/api_grpc
  - type: X-github
    url: https://github.com/tensorflow/serving
- name: TensorFlow Hub API
  description: A library for reusable machine learning modules.
  image: https://www.tensorflow.org/images/tf_logo_social.png
  humanURL: https://tfhub.dev/
  baseURL: https://tfhub.dev/
  tags:
  - Model Repository
  - Pre-Trained Models
  - Transfer Learning
  properties:
  - type: X-documentation
    url: https://www.tensorflow.org/hub/api_docs/python/hub
  - type: X-models
    url: https://tfhub.dev/
  - type: X-github
    url: https://github.com/tensorflow/hub
name: TensorFlow
tags:
- AI
- Deep Learning
- JavaScript
- Machine Learning
- Neural Networks
- Open Source
- Python
type: Contract
image: https://www.tensorflow.org/images/tf_logo_social.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: An end-to-end open source machine learning platform for everyone. TensorFlow provides a comprehensive ecosystem of tools, libraries, and community resources for building and deploying ML-powered applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

