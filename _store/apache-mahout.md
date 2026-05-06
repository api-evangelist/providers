---
aid: apache-mahout
name: Apache Mahout
description: Apache Mahout is an open-source framework for building scalable machine learning applications. The project has evolved to include Qumat, a unified Python API for building quantum circuits that runs across multiple quantum backends including Qiskit, Cirq, and Amazon Braket, along with QDP for GPU-accelerated classical-to-quantum data encoding.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Computing
  - Machine Learning
  - Python
  - Quantum Computing
  - Scala
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-mahout/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-mahout:qumat
    name: Qumat
    description: Qumat is a unified Python API for building and executing quantum circuits across multiple quantum computing backends including Qiskit, Cirq, and Amazon Braket. It provides a hardware-agnostic interface for quantum gate operations, parameterized circuits, measurement, and state vector retrieval.
    humanURL: https://mahout.apache.org/docs/qumat
    tags:
      - Python
      - Quantum Computing
      - Quantum Circuits
    properties:
      - type: Documentation
        url: https://mahout.apache.org/docs/qumat
      - type: APIReference
        url: https://mahout.apache.org/docs/qumat/api
      - type: GettingStarted
        url: https://mahout.apache.org/docs/qumat/getting-started
      - type: SDK
        url: https://pypi.org/project/qumat/
        title: Python SDK (PyPI)
      - type: GitHubRepository
        url: https://github.com/apache/mahout
  - aid: apache-mahout:apache-mahout-samsara
    name: Apache Mahout Samsara
    description: Mahout Samsara is a distributed linear algebra DSL in Scala for building machine learning algorithms on Apache Spark. It provides matrix decompositions, collaborative filtering, clustering, and other algorithms as a mathematically expressive API.
    humanURL: https://mahout.apache.org/docs/latest/
    tags:
      - Distributed Computing
      - Linear Algebra
      - Machine Learning
      - Scala
      - Spark
    properties:
      - type: Documentation
        url: https://mahout.apache.org/docs/latest/
      - type: GitHubRepository
        url: https://github.com/apache/mahout
common:
  - type: Portal
    url: https://mahout.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/mahout
  - type: IssueTracker
    url: https://issues.apache.org/jira/browse/MAHOUT
  - type: MailingList
    url: https://mahout.apache.org/docs/community/mailing-lists
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Hardware-Agnostic Quantum API
        description: Qumat provides a unified API that runs the same quantum circuit code on Qiskit, Cirq, and Amazon Braket backends without modification.
      - name: Quantum Gate Operations
        description: Complete library of single-qubit gates (H, X, Y, Z, T, Rx, Ry, Rz, U) and multi-qubit gates (CNOT, Toffoli, SWAP, CSWAP).
      - name: Parameterized Quantum Circuits
        description: Support for symbolic parameters in rotation gates for variational quantum algorithms and quantum machine learning.
      - name: GPU-Accelerated Data Encoding
        description: QDP provides zero-copy tensor transfer for encoding classical data into quantum states with GPU acceleration.
      - name: Distributed Linear Algebra
        description: Samsara DSL enables large-scale matrix operations distributed across Apache Spark clusters.
      - name: Collaborative Filtering
        description: Distributed recommendation algorithms including ALS-based collaborative filtering for large-scale datasets.
      - name: Clustering
        description: Distributed K-Means, fuzzy K-Means, and spectral clustering algorithms running on Spark.
      - name: Dimensionality Reduction
        description: Distributed SVD, PCA, and random projection methods for large-scale feature reduction.
  - type: UseCases
    data:
      - name: Quantum Machine Learning
        description: Build variational quantum algorithms and quantum neural networks using parameterized circuits via the Qumat API.
      - name: Quantum Algorithm Research
        description: Prototype and test quantum algorithms across different hardware backends without rewriting circuit code.
      - name: Large-Scale Recommendation
        description: Build distributed recommendation systems processing billions of user-item interactions using Mahout on Spark.
      - name: Distributed Clustering
        description: Cluster large datasets using distributed K-Means and other algorithms running on Apache Spark.
  - type: Integrations
    data:
      - name: Qiskit
        description: IBM Qiskit quantum computing framework as a Qumat execution backend for IBM quantum hardware and simulators.
      - name: Cirq
        description: Google Cirq quantum computing framework as a Qumat execution backend for Google quantum hardware.
      - name: Amazon Braket
        description: AWS Braket quantum computing service as a Qumat execution backend for cloud quantum hardware.
      - name: Apache Spark
        description: Primary distributed computing backend for Mahout Samsara linear algebra and machine learning algorithms.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
