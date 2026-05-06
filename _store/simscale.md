---
name: SimScale
description: SimScale is a cloud-based computer-aided engineering (CAE) platform offering computational fluid dynamics (CFD), finite element analysis (FEA), and thermal simulation capabilities. The SimScale REST API enables programmatic project management, geometry upload, mesh generation, simulation setup and execution, and results extraction for engineering automation workflows.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/simscale/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - CAE
  - CFD
  - FEA
  - Simulation
  - Engineering
apis:
  - name: SimScale REST API
    description: The SimScale REST API provides programmatic access to the SimScale cloud simulation platform. Developers can manage projects, upload CAD geometry, configure meshing operations, set up and run CFD/FEA simulations, and retrieve results. Available on Enterprise plans. SDKs available for Python and C#.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.simscale.com/docs/platform/api-and-sdk-documentation/
    baseURL: https://api.simscale.com
    tags:
      - CFD
      - FEA
      - Simulation
      - Geometry
      - Meshing
      - Projects
    properties:
      - type: Documentation
        url: https://www.simscale.com/docs/platform/api-and-sdk-documentation/
      - type: SwaggerUI
        url: https://api.simscale.com/apidoc/swagger/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/simscale/refs/heads/main/openapi/simscale-openapi.yml
      - type: PythonSDK
        url: https://github.com/SimScaleGmbH/simscale-python-sdk
      - type: GitHubOrganization
        url: https://github.com/SimScaleGmbH
      - type: Authentication
        url: https://www.simscale.com/docs/platform/api-and-sdk-documentation/
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/simscale/refs/heads/main/rules/simscale-rules.yml
    contact:
      - FN: SimScale Support
        url: https://www.simscale.com/support/
common:
  - type: GitHubOrganization
    url: https://github.com/SimScaleGmbH
  - type: DeveloperPortal
    url: https://www.simscale.com/product/api/
  - type: Documentation
    url: https://www.simscale.com/docs/
  - type: PythonSDK
    url: https://github.com/SimScaleGmbH/simscale-python-sdk
  - type: Pricing
    url: https://www.simscale.com/pricing/
  - type: TermsOfService
    url: https://www.simscale.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.simscale.com/privacy-policy/
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
---
