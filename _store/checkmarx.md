---
aid: checkmarx
url: https://raw.githubusercontent.com/api-evangelist/checkmarx/refs/heads/main/apis.yml
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
name: Checkmarx
tags:
- Application Security
- Code Analysis
- DevSecOps
- SAST
- Security Testing
- Vulnerability Scanning
type: Contract
image: https://www.checkmarx.com/wp-content/uploads/2022/03/checkmarx-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Checkmarx is a leading application security testing solution provider, offering static application security testing (SAST), software composition analysis (SCA), and other security tools to help organizations identify and remediate vulnerabilities in their code.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

