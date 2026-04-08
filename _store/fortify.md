---
aid: fortify
url: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/apis.yml
apis:
- name: Fortify on Demand API
  description: REST API for Fortify on Demand (FoD), the cloud-based application security testing service from OpenText. Provides programmatic access to manage applications, initiate scans, and retrieve vulnerability results.
  image: https://www.microfocus.com/brand/fortify-logo.png
  baseURL: https://api.ams.fortify.com
  humanURL: https://www.opentext.com/products/fortify-on-demand
  tags:
  - Application Security
  - DAST
  - SAST
  - Security Testing
  - Vulnerability Management
  properties:
  - type: Documentation
    url: https://www.microfocus.com/documentation/fortify-on-demand/
  - type: OpenAPI
    url: https://api.ams.fortify.com/swagger/docs/v3
  - type: OpenAPI
    url: openapi/fortify-on-demand-openapi.yml
  - type: API Reference
    url: https://api.ams.fortify.com/swagger/ui/index
  - type: Authentication
    url: https://api.ams.fortify.com/oauth/token
  - type: Getting Started
    url: https://www.microfocus.com/documentation/fortify-on-demand/251/Fortify_on_Demand_Guide_25.1_EN.pdf
  contact:
  - type: Support
    url: https://www.opentext.com/support
  - type: Email
    url: fortify-support@microfocus.com
- name: Fortify Software Security Center API
  description: REST API for the on-premise Fortify Software Security Center (SSC), which provides centralized management and reporting of security assessment data across an organization's application portfolio.
  image: https://www.microfocus.com/brand/fortify-logo.png
  baseURL: https://your-ssc-server/ssc/api/v1
  humanURL: https://www.microfocus.com/documentation/fortify-software-security-center/
  tags:
  - Application Security
  - Compliance
  - On-Premise
  - Security Analytics
  - Vulnerability Management
  properties:
  - type: Documentation
    url: https://www.microfocus.com/documentation/fortify-software-security-center/2520/
  - type: OpenAPI
    url: openapi/fortify-software-security-center-openapi.yml
  - type: API Reference
    url: https://your-ssc-server/ssc/html/docs/api-reference/
  - type: Authentication
    url: https://your-ssc-server/ssc/api/v1/auth
  - type: Getting Started
    url: https://www.microfocus.com/documentation/fortify-software-security-center/
  - type: SDKs
    url: https://github.com/fortify/ssc-restapi-client
- name: Fortify ScanCentral DAST API
  description: REST API for Fortify ScanCentral DAST, which provides centralized dynamic application security testing management. Enables orchestration of DAST scans across distributed sensors and integration with CI/CD pipelines.
  image: https://www.microfocus.com/brand/fortify-logo.png
  baseURL: https://your-scancentral-dast-server/api/
  humanURL: https://www.microfocus.com/documentation/fortify-ScanCentral-DAST/
  tags:
  - CI/CD
  - DAST
  - Dynamic Analysis
  - Security Testing
  - Web Application Security
  properties:
  - type: Documentation
    url: https://www.microfocus.com/documentation/fortify-ScanCentral-DAST/2520/
  - type: OpenAPI
    url: openapi/fortify-scancentral-dast-openapi.yml
  - type: Getting Started
    url: https://www.microfocus.com/documentation/fortify-ScanCentral-DAST/2520/sc-dast-ugd-25.2.0.pdf
name: Fortify
tags:
- Application Security
- DAST
- DevSecOps
- SAST
- SCA
- Security Testing
- Vulnerability Scanning
type: Contract
image: https://www.microfocus.com/brand/fortify-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Fortify is a comprehensive application security platform from OpenText that provides static application security testing (SAST), dynamic application security testing (DAST), and software composition analysis (SCA) capabilities. It helps organizations identify and remediate vulnerabilities across the software development lifecycle.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

