---
aid: intel
url: https://raw.githubusercontent.com/api-evangelist/intel/refs/heads/main/apis.yml
apis:
  - aid: intel:trust-authority-api
    name: Intel Trust Authority API
    tags:
      - Attestation
      - Confidential Computing
      - Security
      - Trust
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trustauthority.intel.com
    humanURL: https://docs.trustauthority.intel.com/main/articles/restapi-intro.html
    properties:
      - url: https://docs.trustauthority.intel.com/main/articles/restapi-intro.html
        type: Documentation
      - url: openapi/intel-trust-authority-api-openapi.yml
        type: OpenAPI
    description: Intel Trust Authority REST API enables developers to build secure applications with confidence using attestation services. It provides Faithful Verification for unmatched transparency in the attestation process, allowing auditing of attestation tokens issued by Intel Trust Authority.
  - aid: intel:oneapi
    name: Intel oneAPI
    tags:
      - Accelerators
      - AI
      - Compute
      - GPU
      - Heterogeneous Computing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api-portal.intel.com
    humanURL: https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html
    properties:
      - url: https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html
        type: Documentation
      - url: openapi/intel-oneapi-openapi.yml
        type: OpenAPI
    description: Intel oneAPI is an open standard unified programming model for heterogeneous computing across CPUs, GPUs, AI accelerators, and FPGAs. It provides a cross-architecture programming interface that simplifies development across diverse computing accelerator architectures.
description: Discover Intel® Trust Authority, the independent attestation service for securing your confidential computing workloads.
---
