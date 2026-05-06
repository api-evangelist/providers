---
aid: apptainer
name: Apptainer
description: Apptainer, formerly Singularity, is a Linux Foundation project providing a high-performance container runtime optimized for high-performance computing and scientific workloads. It enables reproducible, portable scientific computing with support for existing Docker/OCI containers and integration with HPC schedulers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - HPC
  - Scientific Computing
  - Open Source
  - Linux Foundation
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apptainer/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apptainer:apptainer-api
    name: Apptainer API
    tags:
      - Containers
      - HPC
      - Scientific Computing
      - SIF
    humanURL: https://apptainer.org/docs/
    properties:
      - url: https://apptainer.org/docs/
        type: Documentation
      - url: https://github.com/apptainer/apptainer
        type: GitHubRepository
      - url: openapi/apptainer-openapi.yaml
        type: OpenAPI
      - url: json-schema/container-image-schema.json
        type: JSONSchema
      - url: json-structure/container-image-structure.json
        type: JSONStructure
      - url: examples/container-image-example.json
        type: Example
      - url: json-ld/apptainer-context.jsonld
        type: JSONLD
      - url: rules/apptainer-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/apptainer-api.yaml
        type: NaftikoCapability
      - url: capabilities/hpc-container-management.yaml
        type: NaftikoCapability
      - url: vocabulary/apptainer-vocabulary.yaml
        type: Vocabulary
    description: API for the Apptainer container runtime, providing programmatic management of HPC container images and instances optimized for scientific computing workloads.
common:
  - type: Documentation
    name: Apptainer Documentation
    description: Official documentation for Apptainer.
    url: https://apptainer.org/docs/
  - type: GitHubOrg
    name: Apptainer GitHub
    description: Source code and repositories for Apptainer.
    url: https://github.com/apptainer
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
