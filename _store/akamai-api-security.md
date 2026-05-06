---
aid: akamai-api-security
name: Akamai API Security
description: Akamai API Security (formerly Noname Security) provides comprehensive API discovery, posture management, and threat protection for organizations across cloud, on-premises, and hybrid environments. The platform continuously discovers and monitors all APIs, identifies vulnerabilities and misconfigurations, detects and responds to API threats in real time, and provides pre-production security testing integrated into CI/CD pipelines.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Discovery
  - API Security
  - Cloud Security
  - Posture Management
  - Runtime Protection
  - Threat Protection
url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: akamai-api-security:api-security
    name: Akamai API Security
    description: Akamai API Security provides end-to-end API protection including discovery, posture management, runtime protection, and active testing. It discovers all APIs including shadow and zombie APIs, identifies vulnerabilities and misconfigurations, and detects and blocks API-based attacks in real time.
    humanURL: https://www.akamai.com/products/api-security
    tags:
      - API Discovery
      - API Security
      - Runtime Protection
      - Threat Protection
    properties:
      - type: Documentation
        url: https://techdocs.akamai.com/api-security/docs/welcome
      - type: GettingStarted
        url: https://techdocs.akamai.com/api-security/docs/get-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/openapi/akamai-api-security-openapi.json
  - aid: akamai-api-security:akamai-apis
    name: Akamai APIs
    description: Akamai provides a comprehensive set of REST APIs for managing and configuring their platform services, including API security, CDN, edge computing, and security products. The APIs use the Akamai EdgeGrid authentication mechanism.
    humanURL: https://techdocs.akamai.com/home/page/products-tools-a-z
    tags:
      - Configuration
      - EdgeGrid
      - Platform API
      - REST API
    properties:
      - type: Documentation
        url: https://techdocs.akamai.com/home/page/products-tools-a-z
      - type: Authentication
        url: https://techdocs.akamai.com/developer/docs/authenticate-with-edgegrid
      - type: GettingStarted
        url: https://techdocs.akamai.com/developer/docs/get-started
common:
  - type: Website
    url: https://www.akamai.com/products/api-security
  - type: Documentation
    url: https://techdocs.akamai.com
  - type: Blog
    url: https://www.akamai.com/blog
  - type: Pricing
    url: https://www.akamai.com/products/api-security#pricing
  - type: Support
    url: https://www.akamai.com/support
  - type: Login
    url: https://control.akamai.com
  - type: SignUp
    url: https://www.akamai.com/free-trials
  - type: GitHubOrganization
    url: https://github.com/akamai
  - type: StatusPage
    url: https://www.akamaistatus.com
  - type: LinkedIn
    url: https://www.linkedin.com/company/akamai-technologies
  - type: X
    url: https://twitter.com/Akamai
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/rules/akamai-api-security-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/vocabulary/akamai-api-security-vocabulary.yaml
  - type: Features
    data:
      - name: API Discovery
        description: Automatically discovers all APIs including shadow, zombie, GenAI, LLM, and MCP server APIs across cloud, on-premises, and hybrid environments.
      - name: Posture Management
        description: Audits APIs for vulnerabilities and misconfigurations including the full OWASP API Top 10, generating posture findings from runtime incidents.
      - name: Runtime Protection
        description: Uses contextual insights to detect and block API threats including business logic abuse, credential attacks, data scraping, and malicious bots in real time.
      - name: CI/CD Security Testing
        description: Runs 200+ dynamic security tests simulating OWASP API Top 10 attacks integrated into CI/CD pipelines without sacrificing development speed.
      - name: GitHub Integration
        description: Automatically scans GitHub repositories for OpenAPI specs and adds them to the API library for security analysis and posture assessment.
      - name: App and API Protector Integration
        description: Direct integration with Akamai App and API Protector for blocking API threats detected at runtime.
  - type: UseCases
    data:
      - name: Shadow API Discovery
        description: Security teams automatically discover undocumented and shadow APIs across their environment to eliminate blind spots.
      - name: API Vulnerability Assessment
        description: Security engineers assess API posture against OWASP API Top 10 and compliance frameworks to prioritize remediation.
      - name: Real-Time Threat Detection
        description: SOC analysts detect and respond to API attacks, data leakage, and suspicious behavior in real time.
      - name: Pre-Production API Testing
        description: Development teams integrate API security testing into CI/CD pipelines to find and fix vulnerabilities before production.
      - name: Compliance Reporting
        description: Compliance teams assess API security posture against industry frameworks and generate audit-ready reports.
  - type: Integrations
    data:
      - name: Akamai App and API Protector
        description: Direct integration for blocking API threats detected by API Security
      - name: GitHub
        description: Automatic OpenAPI spec discovery from GitHub repositories
      - name: CI/CD Pipelines
        description: Integration with development pipelines for pre-production security testing
      - name: SIEM
        description: Export security events to SIEM platforms for centralized monitoring
      - name: AWS Marketplace
        description: Available on AWS Marketplace for cloud-native deployments
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
