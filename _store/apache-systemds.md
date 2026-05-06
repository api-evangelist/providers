---
aid: apache-systemds
name: Apache SystemDS
description: Apache SystemDS is an open-source ML system for the end-to-end data science lifecycle from data integration, cleaning, and feature engineering to model training, debugging, and deployment. It provides a declarative machine learning language (DML), automatic optimization for different execution backends (local, distributed Spark), and a Python API (SystemDS Python). SystemDS is an Apache Software Foundation top-level project designed for scalable ML workflows.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AutoML
  - Data Science
  - Distributed Computing
  - Machine Learning
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-systemds/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-systemds:apache-systemds-python-api
    name: Apache SystemDS Python API
    description: The SystemDS Python API (systemds) provides a Python interface for building end-to-end ML pipelines. It includes Matrix and Frame types for distributed data manipulation, built-in algorithms for preprocessing, feature engineering, classification, regression, and clustering, and federated learning capabilities. The Python API communicates with a SystemDS runtime backend via gRPC for distributed execution on Apache Spark.
    humanURL: https://apache.github.io/systemds/api/python/
    tags:
      - Python
      - Machine Learning
      - Data Science
      - Distributed Computing
    properties:
      - type: Documentation
        url: https://apache.github.io/systemds/api/python/
      - type: SDK
        url: https://pypi.org/project/systemds/
        title: Python Package (PyPI)
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.systemds
        title: Java/Scala Maven Package
common:
  - type: GitHubRepository
    url: https://github.com/apache/systemds
  - type: Documentation
    url: https://apache.github.io/systemds/
  - type: Portal
    url: https://systemds.apache.org/
  - type: GettingStarted
    url: https://apache.github.io/systemds/get-started
  - type: ReleaseNotes
    url: https://github.com/apache/systemds/releases
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Declarative ML Language (DML)
        description: High-level R-like language for specifying ML algorithms with automatic optimization.
      - name: Automatic Optimization
        description: Query optimization, memory management, and execution plan selection for ML workloads.
      - name: Federated Learning
        description: Privacy-preserving federated ML across distributed data silos without data sharing.
      - name: Built-In Algorithms
        description: 50+ built-in ML algorithms including linear models, neural networks, clustering, and ensemble methods.
      - name: Python API
        description: Pythonic API for ML pipeline development with lazy evaluation and distributed execution.
      - name: Data Cleaning Pipelines
        description: Automated data cleaning, imputation, encoding, and normalization pipelines.
  - type: UseCases
    data:
      - name: Distributed ML Training
        description: Train large-scale ML models distributed across Apache Spark clusters.
      - name: Federated Machine Learning
        description: Cross-silo federated learning for privacy-sensitive healthcare and finance data.
      - name: End-to-End ML Pipelines
        description: Integrated data preparation, feature engineering, training, and serving pipelines.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Native Spark backend for distributed matrix operations and ML training.
      - name: Python
        description: Python API with NumPy-compatible Matrix type for local and distributed computation.
      - name: Kubernetes
        description: Kubernetes deployment support for SystemDS runtime via Helm charts.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
