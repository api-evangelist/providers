---
aid: lf-ai-and-data
name: LF AI and Data
description: The LF AI & Data Foundation is a Linux Foundation umbrella that advances open source artificial intelligence, machine learning, and data projects. It hosts 80+ projects spanning graduated, incubation, and sandbox stages, including ONNX, Milvus, Horovod, Flyte, Kedro, Pyro, Egeria, OpenLineage, Marquez, and the Adversarial Robustness Toolbox, fostering scalable, trustworthy, and interoperable AI and data solutions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Machine Learning
  - Data
  - Linux Foundation
  - Open Source
  - MLOps
  - Vector Database
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/lf-ai-and-data/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lf-ai-and-data:onnx
    name: ONNX
    description: Open Neural Network Exchange (ONNX) is an open format for representing deep learning models, enabling interoperability between AI frameworks.
    humanURL: https://onnx.ai/
    tags:
      - AI
      - Machine Learning
      - Model Format
      - Interoperability
    properties:
      - type: Documentation
        url: https://onnx.ai/
      - type: GitHubRepo
        url: https://github.com/onnx/onnx
  - aid: lf-ai-and-data:milvus
    name: Milvus
    description: Milvus is an open source vector database built for scalable similarity search, supporting embedding-based AI applications.
    humanURL: https://milvus.io/
    tags:
      - Vector Database
      - AI
      - Search
    properties:
      - type: Documentation
        url: https://milvus.io/docs
      - type: GitHubRepo
        url: https://github.com/milvus-io/milvus
  - aid: lf-ai-and-data:horovod
    name: Horovod
    description: Horovod is a distributed deep learning training framework for TensorFlow, Keras, PyTorch, and Apache MXNet.
    humanURL: https://horovod.ai/
    tags:
      - Deep Learning
      - Distributed Training
      - GPU
    properties:
      - type: Documentation
        url: https://horovod.readthedocs.io/
      - type: GitHubRepo
        url: https://github.com/horovod/horovod
  - aid: lf-ai-and-data:flyte
    name: Flyte
    description: Flyte is a production-grade, cloud-native workflow orchestration platform for data and machine learning processes.
    humanURL: https://flyte.org/
    tags:
      - Workflow Orchestration
      - MLOps
      - Cloud Native
    properties:
      - type: Documentation
        url: https://docs.flyte.org/
      - type: GitHubRepo
        url: https://github.com/flyteorg/flyte
  - aid: lf-ai-and-data:kedro
    name: Kedro
    description: Kedro is a Python framework for creating reproducible, maintainable, and modular data science code.
    humanURL: https://kedro.org/
    tags:
      - Data Science
      - Python
      - Pipelines
    properties:
      - type: Documentation
        url: https://docs.kedro.org/
      - type: GitHubRepo
        url: https://github.com/kedro-org/kedro
  - aid: lf-ai-and-data:openlineage
    name: OpenLineage
    description: OpenLineage is an open standard and API for collecting lineage metadata across data pipelines.
    humanURL: https://openlineage.io/
    tags:
      - Data Lineage
      - Metadata
      - Standards
    properties:
      - type: Documentation
        url: https://openlineage.io/docs/
      - type: GitHubRepo
        url: https://github.com/OpenLineage/OpenLineage
  - aid: lf-ai-and-data:marquez
    name: Marquez
    description: Marquez is an open source metadata service for the collection, aggregation, and visualization of a data ecosystem's metadata.
    humanURL: https://marquezproject.ai/
    tags:
      - Metadata
      - Data Ecosystem
      - Lineage
    properties:
      - type: Documentation
        url: https://marquezproject.ai/docs/
      - type: GitHubRepo
        url: https://github.com/MarquezProject/marquez
  - aid: lf-ai-and-data:egeria
    name: Egeria
    description: Egeria is the world's first open source metadata standard for enterprise data management, enabling unified governance and discovery.
    humanURL: https://egeria-project.org/
    tags:
      - Metadata
      - Data Governance
      - Enterprise
    properties:
      - type: Documentation
        url: https://egeria-project.org/
      - type: GitHubRepo
        url: https://github.com/odpi/egeria
  - aid: lf-ai-and-data:adversarial-robustness-toolbox
    name: Adversarial Robustness Toolbox
    description: ART (Adversarial Robustness Toolbox) provides tools for evaluating and defending machine learning models against adversarial threats.
    humanURL: https://adversarial-robustness-toolbox.readthedocs.io/
    tags:
      - AI Security
      - Machine Learning
      - Adversarial
    properties:
      - type: Documentation
        url: https://adversarial-robustness-toolbox.readthedocs.io/
      - type: GitHubRepo
        url: https://github.com/Trusted-AI/adversarial-robustness-toolbox
  - aid: lf-ai-and-data:delta-lake
    name: Delta Lake
    description: Delta Lake is an open source storage layer that brings ACID transactions and reliability to data lakes.
    humanURL: https://delta.io/
    tags:
      - Data Lake
      - ACID
      - Storage
    properties:
      - type: Documentation
        url: https://docs.delta.io/
      - type: GitHubRepo
        url: https://github.com/delta-io/delta
  - aid: lf-ai-and-data:feast
    name: Feast
    description: Feast is an open source feature store for machine learning, providing consistent feature serving across training and inference.
    humanURL: https://feast.dev/
    tags:
      - Feature Store
      - Machine Learning
      - MLOps
    properties:
      - type: Documentation
        url: https://docs.feast.dev/
      - type: GitHubRepo
        url: https://github.com/feast-dev/feast
common:
  - type: Documentation
    name: LF AI and Data Documentation
    description: Official documentation for LF AI and Data.
    url: https://lfaidata.foundation/projects/
  - type: GitHubOrg
    name: LF AI and Data GitHub
    description: Source code and repositories for LF AI and Data.
    url: https://github.com/lfai
  - type: Website
    name: LF AI and Data Website
    description: Main LF AI and Data Foundation website.
    url: https://lfaidata.foundation/
  - type: ProjectsList
    name: LF AI and Data Projects List
    description: Comprehensive list of all LF AI and Data hosted projects.
    url: https://lfaidata.foundation/projects/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
