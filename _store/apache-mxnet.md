---
aid: apache-mxnet
name: Apache MXNet
description: Apache MXNet is a retired deep learning framework (now in the Apache Attic) designed for both efficiency and flexibility. It provided a multi-language API for building and training deep neural networks with support for distributed training, the Gluon high-level API, and deployment on edge devices. MXNet supported Python, Scala, Java, C++, R, Julia, and Perl.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Deep Learning
  - Machine Learning
  - Neural Networks
  - Python
  - Retired
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-mxnet/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-mxnet:apache-mxnet
    name: Apache MXNet
    description: MXNet provides APIs in Python, Scala, Java, C++, R, Julia, and Perl for deep learning model development, with the Gluon high-level API for imperative model building, Symbol/NDArray low-level APIs for efficient computation graphs, and distributed training via Parameter Server and Horovod. Final version is 1.9.1.
    humanURL: https://mxnet.apache.org/versions/1.9.1/api
    tags:
      - Deep Learning
      - Distributed Training
      - Gluon
      - Python
    properties:
      - type: Documentation
        url: https://mxnet.apache.org/versions/1.9.1/api
      - type: GettingStarted
        url: https://mxnet.apache.org/versions/1.9.1/get_started
      - type: SDK
        url: https://pypi.org/project/mxnet/
        title: Python SDK (PyPI)
      - type: SDK
        url: https://central.sonatype.com/artifact/org.apache.mxnet/mxnet-full_2.12
        title: Scala/Java SDK (Maven)
      - type: GitHubRepository
        url: https://github.com/apache/mxnet
common:
  - type: Portal
    url: https://mxnet.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/mxnet
  - type: Wiki
    url: https://cwiki.apache.org/confluence/display/MXNET/Apache+MXNet+Home
  - type: IssueTracker
    url: https://issues.apache.org/jira/projects/MXNET/issues
  - type: MailingList
    url: mailto:dev@mxnet.apache.org
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Hybrid Front-End
        description: Seamlessly transitions between Gluon eager imperative mode and symbolic execution for research flexibility and production efficiency.
      - name: Distributed Training
        description: Supports Parameter Server and Horovod for scalable distributed training across multiple GPUs and nodes.
      - name: Multi-Language Bindings
        description: Native APIs in Python, Scala, Java, C++, R, Julia, Clojure, and Perl for broad developer accessibility.
      - name: Gluon High-Level API
        description: Intuitive Gluon API for imperative model building with automatic differentiation and dynamic computation graphs.
      - name: NDArray API
        description: NumPy-like array operations for GPU-accelerated numerical computing as the foundation of MXNet computations.
      - name: Symbol API
        description: Symbolic computation graph API for efficient inference and production deployment.
      - name: Model Zoo
        description: Pre-trained models for computer vision, NLP, and other tasks accessible via the Gluon model zoo.
      - name: Edge Deployment
        description: Lightweight deployment support for edge devices and mobile platforms via TVM and ONNX export.
  - type: UseCases
    data:
      - name: Computer Vision
        description: Build and train image classification, object detection, and segmentation models using GluonCV toolkit.
      - name: Natural Language Processing
        description: Develop NLP models for text classification, sentiment analysis, and language modeling using GluonNLP.
      - name: Time Series Forecasting
        description: Build time series forecasting models using the GluonTS toolkit for probabilistic forecasting.
      - name: Distributed Deep Learning
        description: Train large neural networks across multiple GPUs and nodes using Parameter Server or Horovod.
      - name: Research Prototyping
        description: Rapid prototyping of novel deep learning architectures using the Gluon imperative API.
  - type: Integrations
    data:
      - name: GluonCV
        description: Computer vision toolkit built on MXNet providing pre-trained models and training utilities for vision tasks.
      - name: GluonNLP
        description: NLP toolkit built on MXNet with pre-trained language models and text processing utilities.
      - name: GluonTS
        description: Time series modeling toolkit built on MXNet for probabilistic forecasting.
      - name: ONNX
        description: ONNX model format support for importing and exporting models to/from other frameworks.
      - name: TVM
        description: Apache TVM deep learning compiler for optimizing MXNet model deployment on diverse hardware targets.
      - name: Horovod
        description: Horovod distributed training framework integration for efficient multi-GPU and multi-node training.
      - name: D2L.ai
        description: Dive into Deep Learning interactive textbook using MXNet for teaching deep learning concepts.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
