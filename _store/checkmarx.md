---
name: Checkmarx
description: Checkmarx is a leading application security testing solution provider, offering static application security testing (SAST), software composition analysis (SCA), and other security tools to help organizations identify and remediate vulnerabilities in their code.
image: https://www.checkmarx.com/wp-content/uploads/2022/03/checkmarx-logo.svg
tags:
  - Application Security
  - Code Analysis
  - DevSecOps
  - SAST
  - Security Testing
  - Vulnerability Scanning
created: '2024'
modified: '2026-04-23'
url: https://www.checkmarx.com
specificationVersion: '0.20'
apis:
  - name: Checkmarx SAST API
    description: API for Checkmarx Static Application Security Testing (SAST) to scan source code for security vulnerabilities.
    image: https://www.checkmarx.com/wp-content/uploads/2022/03/checkmarx-logo.svg
    humanURL: https://checkmarx.com/resource/documents/en/34965-8158-rest-api.html
    baseURL: https://your-checkmarx-instance.com/cxrestapi
    tags:
      - SAST
      - Security Scanning
      - Static Analysis
      - Vulnerability Detection
    properties:
      - type: Documentation
        url: https://checkmarx.com/resource/documents/en/34965-8158-rest-api.html
      - type: OpenAPI
        url: https://checkmarx.com/resource/documents/en/34965-8158-rest-api.html
      - type: Authentication
        url: https://checkmarx.com/resource/documents/en/34965-8158-authentication.html
      - type: OpenAPI
        url: openapi/checkmarx-sast-openapi.yml
  - name: Checkmarx SCA API
    description: API for Software Composition Analysis to identify open source vulnerabilities and license compliance issues.
    image: https://www.checkmarx.com/wp-content/uploads/2022/03/checkmarx-logo.svg
    humanURL: https://checkmarx.com/resource/documents/en/34965-68617-api.html
    baseURL: https://api-sca.checkmarx.net
    tags:
      - Dependency Scanning
      - License Compliance
      - Open Source Security
      - SCA
    properties:
      - type: Documentation
        url: https://checkmarx.com/resource/documents/en/34965-68617-api.html
      - type: Authentication
        url: https://checkmarx.com/resource/documents/en/34965-68617-authentication.html
      - type: OpenAPI
        url: openapi/checkmarx-sca-openapi.yml
  - name: Checkmarx One API
    description: Unified API for Checkmarx One cloud-native application security platform.
    image: https://www.checkmarx.com/wp-content/uploads/2022/03/checkmarx-logo.svg
    humanURL: https://checkmarx.com/resource/documents/en/34965-128036-checkmarx-one-api.html
    baseURL: https://ast.checkmarx.net/api
    tags:
      - Application Security
      - Cloud Security
      - DevSecOps
      - Unified Platform
    properties:
      - type: Documentation
        url: https://checkmarx.com/resource/documents/en/34965-128036-checkmarx-one-api.html
      - type: API Reference
        url: https://checkmarx.com/resource/documents/en/34965-128036-api-reference.html
      - type: OpenAPI
        url: openapi/checkmarx-one-openapi.yml
common:
  - type: Website
    url: https://www.checkmarx.com
  - type: Documentation
    url: https://checkmarx.com/resource/documents/
  - type: Support
    url: https://support.checkmarx.com/
  - type: Login
    url: https://checkmarx.com/login/
  - type: Blog
    url: https://checkmarx.com/blog/
  - type: News
    url: https://checkmarx.com/news/
  - type: GitHub
    url: https://github.com/checkmarx
  - type: Status
    url: https://status.checkmarx.com/
  - type: Privacy Policy
    url: https://checkmarx.com/privacy-policy/
  - type: Terms of Service
    url: https://checkmarx.com/terms-of-use/
  - type: JSON-LD
    url: json-ld/checkmarx-context.jsonld
  - type: JSONSchema
    url: json-schema/checkmarx-scan-result-schema.json
  - type: JSONSchema
    url: json-schema/checkmarx-vulnerability-schema.json
  - type: Spectral
    url: spectral/checkmarx-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/checkmarx-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
