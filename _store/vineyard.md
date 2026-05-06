---
aid: vineyard
name: Vineyard
description: Vineyard (v6d) is an in-memory immutable data manager developed under CNCF TAG-Storage. It provides efficient zero-copy data sharing across distributed systems for big data analytics, machine learning, and data-intensive workflows. Vineyard enables seamless object sharing between computation engines through a metadata-payload separation architecture, supporting Python, C++, Rust, and Go clients. The Vineyard Operator provides Kubernetes-native deployment with CRDs for managing clusters, sidecars, backups, and data operations.
type: Index
url: https://v6d.io/
tags:
  - Big Data
  - CNCF
  - Cloud Native
  - Data Engineering
  - Distributed Systems
  - In-Memory Storage
  - Kubernetes
  - Machine Learning
  - Metadata Management
  - Python
  - Zero-Copy
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vineyard:vineyard-python-client
    name: Vineyard Python Client API
    description: The Vineyard Python client API provides programmatic access to the Vineyard in-memory data manager. It supports IPC (UNIX domain socket) and RPC (TCP) connections for storing, retrieving, and managing distributed in-memory objects. Key operations include put, get, delete, persist, and metadata inspection.
    humanURL: https://v6d.io/notes/references/python-api.html
    tags:
      - Python
      - Client
      - In-Memory Storage
      - Distributed Systems
    properties:
      - type: OpenAPI
        url: openapi/vineyard-python-client-openapi.yml
      - type: Documentation
        url: https://v6d.io/notes/references/python-api.html
      - type: GettingStarted
        url: https://v6d.io/notes/getting-started.html
  - aid: vineyard:vineyard-kubernetes-operator
    name: Vineyard Kubernetes Operator
    description: The Vineyard Kubernetes Operator manages vineyard cluster lifecycle and orchestrates shared objects on Kubernetes. It defines CRDs including Vineyardd, Sidecar, GlobalObject, LocalObject, Backup, Recover, Operation, and CSIDriver for deploying and managing Vineyard in cloud-native environments.
    humanURL: https://v6d.io/notes/cloud-native/vineyard-operator.html
    tags:
      - Kubernetes
      - Operator
      - Cloud Native
      - CNCF
    properties:
      - type: Documentation
        url: https://v6d.io/notes/cloud-native/vineyard-operator.html
      - type: Documentation
        url: https://v6d.io/notes/references/crds.html
      - type: KubernetesCRD
        url: crd/vineyardd-crd.yaml
      - type: KubernetesCRD
        url: crd/localobject-crd.yaml
      - type: KubernetesCRD
        url: crd/globalobject-crd.yaml
      - type: KubernetesCRD
        url: crd/sidecar-crd.yaml
      - type: KubernetesCRD
        url: crd/operation-crd.yaml
      - type: KubernetesCRD
        url: crd/backup-crd.yaml
      - type: KubernetesCRD
        url: crd/recover-crd.yaml
common:
  - type: Website
    url: https://v6d.io/
  - type: Documentation
    url: https://v6d.io/docs.html
  - type: GitHubOrg
    url: https://github.com/v6d-io
  - type: GitHub
    url: https://github.com/v6d-io/v6d
  - type: GettingStarted
    url: https://v6d.io/notes/getting-started.html
  - type: JSONSchema
    url: json-schema/vineyard-object-schema.json
  - type: JSONSchema
    url: json-schema/vineyard-metadata-schema.json
  - type: JSON-LD
    url: json-ld/vineyard-context.jsonld
  - type: Vocabulary
    url: vocabulary/vineyard-vocabulary.yml
  - type: SpectralRules
    url: rules/vineyard-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
