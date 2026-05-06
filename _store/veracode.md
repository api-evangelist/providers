---
aid: veracode
name: Veracode
description: Veracode is an application security testing (AST) platform offering static analysis (SAST), dynamic analysis (DAST), software composition analysis (SCA), manual penetration testing, and developer security training. The Veracode Platform provides a comprehensive suite of REST APIs enabling organizations to automate security testing, access findings, manage policies, generate reports, and administer users and teams. All REST APIs use HMAC authentication with API ID/key credentials and return JSON responses following OpenAPI standards.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Security
  - SAST
  - DAST
  - SCA
  - Security Testing
  - DevSecOps
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/veracode/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: veracode:veracode-applications-api
    name: Veracode Applications REST API
    description: The Applications REST API provides access to all applications in a Veracode portfolio, including application profiles, policy evaluations, sandboxes, and compliance status. Enables programmatic creation, update, deletion, and querying of application profiles with filtering by name, tag, business unit, scan type, policy compliance, and modified date.
    humanURL: https://docs.veracode.com/r/c_apps_intro
    baseURL: https://api.veracode.com
    tags:
      - Applications
      - Portfolio
      - Policy
      - Sandboxes
    properties:
      - type: Documentation
        url: https://docs.veracode.com/r/c_apps_intro
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/veracode/refs/heads/main/openapi/veracode-applications-openapi.yml
  - aid: veracode:veracode-findings-api
    name: Veracode Findings REST API
    description: The Findings REST API retrieves security findings from static, dynamic, manual penetration testing, and SCA scans for applications. Supports filtering by CWE, severity, scan type, CVSS score, policy compliance, and annotation status. Also provides access to flaw info and MPT scan results.
    humanURL: https://docs.veracode.com/r/c_findings_v2_intro
    baseURL: https://api.veracode.com
    tags:
      - Findings
      - Vulnerabilities
      - SAST
      - DAST
      - SCA
    properties:
      - type: Documentation
        url: https://docs.veracode.com/r/c_findings_v2_intro
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/veracode/refs/heads/main/openapi/veracode-findings-openapi.yml
  - aid: veracode:veracode-identity-api
    name: Veracode Identity REST API
    description: The Identity REST API manages users, teams, business units, roles, and API credentials for a Veracode organization. Provides CRUD operations for user accounts, API service accounts, team management, and role-based access control configuration.
    humanURL: https://docs.veracode.com/r/c_identity_intro
    baseURL: https://api.veracode.com
    tags:
      - Identity
      - Users
      - Teams
      - Access Control
    properties:
      - type: Documentation
        url: https://docs.veracode.com/r/c_identity_intro
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/veracode/refs/heads/main/openapi/veracode-identity-openapi.yml
  - aid: veracode:veracode-reporting-api
    name: Veracode Reporting REST API
    description: The Reporting REST API generates asynchronous security reports for findings, scans, deleted scans, and audit events across the Veracode portfolio. Supports filtering by application, scan type, severity, status, date range, and policy compliance.
    humanURL: https://docs.veracode.com/r/Reporting_REST_API
    baseURL: https://api.veracode.com
    tags:
      - Reporting
      - Analytics
      - Findings
      - Compliance
    properties:
      - type: Documentation
        url: https://docs.veracode.com/r/Reporting_REST_API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/veracode/refs/heads/main/openapi/veracode-reporting-openapi.yml
common:
  - type: Website
    url: https://www.veracode.com/
  - type: Documentation
    url: https://docs.veracode.com/
  - type: GettingStarted
    url: https://docs.veracode.com/r/REST_APIs_Quickstart
  - type: Authentication
    url: https://docs.veracode.com/r/c_enabling_hmac
  - type: GitHubOrganization
    url: https://github.com/veracode
  - type: OpenSourceSite
    url: https://veracode.github.io/
  - type: Blog
    url: https://www.veracode.com/blog
  - type: Support
    url: https://community.veracode.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
