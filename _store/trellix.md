---
name: Trellix
description: Trellix is a cybersecurity company that delivers comprehensive, open, and native extended detection and response (XDR) platform. The company provides threat detection, investigation, and response capabilities across endpoints, networks, data, and cloud environments.
image: https://www.trellix.com/favicon.ico
url: https://www.trellix.com
created: '2024'
modified: '2026-05-03'
tags:
  - Cloud Security
  - Cybersecurity
  - Endpoint Security
  - Threat Detection
  - Threat Intelligence
  - XDR
apis:
  - name: Trellix ePO API
    description: McAfee ePolicy Orchestrator (ePO) REST API for centralized security management, policy enforcement, and reporting across the enterprise.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/epolicy-orchestrator
    baseURL: https://your-epo-server:8443/remote
    tags:
      - Endpoint Management
      - Enterprise Security
      - Policy Orchestration
      - Security Management
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/epolicy-orchestrator
      - type: Authentication
        url: https://developer.manage.trellix.com/mvision/docs/umam
      - type: GettingStarted
        url: https://developer.manage.trellix.com/mvision/docs/uma
      - type: APIReference
        url: https://developer.manage.trellix.com/mvision/apis/v2-devices
    contact:
      - FN: Trellix Support
        url: https://www.trellix.com/support/
  - name: Trellix ePO SaaS API
    description: The Trellix ePO SaaS API provides cloud-based access to ePolicy Orchestrator management capabilities. It enables programmatic control of devices, events, tags, queries, and response actions through the Trellix cloud management platform.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/epolicy-orchestrator-saas-product-guide
    baseURL: https://api.manage.trellix.com
    tags:
      - Cloud Management
      - Endpoint Management
      - SaaS
      - Security Management
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/epolicy-orchestrator-saas-product-guide
      - type: Authentication
        url: https://developer.manage.trellix.com/mvision/docs/umam
      - type: GettingStarted
        url: https://developer.manage.trellix.com/mvision/docs/uma
  - name: Trellix Insights API
    description: API for accessing threat intelligence, security analytics, and insights from the Trellix threat research platform. Provides investigation of indicators of compromise, campaign tracking, and prioritized threat intelligence for security operations.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/trellix-insights-product-guide
    baseURL: https://api.manage.trellix.com
    tags:
      - Analytics
      - Security Insights
      - Threat Intelligence
      - Threat Research
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/trellix-insights-product-guide
      - type: APIReference
        url: https://docs.trellix.com/bundle/trellix-insights-product-guide/page/UUID-e5e4730b-ac74-d923-f691-168ea880e3cd.html
  - name: Trellix EDR API
    description: Endpoint Detection and Response API for advanced threat hunting, investigation, and automated response capabilities. The EDR API supports querying threat data, searching devices, retrieving action history, and executing real-time search and response actions across managed endpoints.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/mvision-endpoint-detection-and-response-product-guide
    baseURL: https://api.manage.trellix.com
    tags:
      - Endpoint Detection
      - Forensics
      - Incident Response
      - Threat Hunting
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/mvision-endpoint-detection-and-response-product-guide
      - type: APIReference
        url: https://docs.trellix.com/bundle/mvision-endpoint-detection-and-response-product-guide/page/UUID-d4602e2b-5adc-bdb4-c8cf-163997d5cd6e.html
      - type: Authentication
        url: https://developer.manage.trellix.com/mvision/docs/umam
      - type: GitHubRepository
        url: https://github.com/trellix-enterprise/EDR-Integration-Scripts
  - name: Trellix Data Exchange Layer (DXL) API
    description: Messaging fabric API that enables real-time communication between security tools and data sharing across the security ecosystem. OpenDXL provides client libraries in Python, JavaScript, and Java for integrating applications with the DXL message bus, enabling automated threat response and security tool orchestration.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://opendxl.github.io/
    baseURL: https://dxl.trellix.com
    tags:
      - Automation
      - Data Exchange
      - Integration
      - Messaging
    properties:
      - type: Documentation
        url: https://opendxl.github.io/
      - type: GitHubOrganization
        url: https://github.com/opendxl
      - type: SDKs
        url: https://opendxl.github.io/opendxl-client-python/
  - name: Trellix Endpoint Security (HX) API
    description: REST API for the Trellix Endpoint Security (HX) platform, formerly FireEye HX. Provides programmatic access to endpoint information, acquisitions, alerts, indicators, conditions, and containment operations. Uses role-based access control with api_admin and api_analyst user roles.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/hx_api_2020-2/page/UUID-973bb2b7-aeba-2ea1-afb9-7d20b136d3f6.html
    baseURL: https://{hx-appliance}/hx/api/v3
    tags:
      - Containment
      - Endpoint Security
      - Incident Response
      - Threat Detection
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/hx_api_2020-2/page/UUID-973bb2b7-aeba-2ea1-afb9-7d20b136d3f6.html
      - type: APIReference
        url: https://docs.trellix.com/bundle/hx_api_2020-2/page/UUID-33b4d7e3-a428-5137-d583-d40753483fbe.html
      - type: GettingStarted
        url: https://docs.trellix.com/bundle/api_1-0-0_ug/page/api-documentation-module-home-page/using-the-endpoint-security-apis.html
  - name: Trellix Data Loss Prevention (DLP) API
    description: REST API for Trellix Data Loss Prevention Endpoint that enables programmatic management of DLP policies, retrieval and analysis of data loss incidents, and integration with cloud gateways. Supports applying DLP policies, querying incident IDs for data-in-use and data-in-motion events, and retrieving incident details.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/data-loss-prevention-landing-page/page/UUID-d99a9913-80b8-d1b9-e030-9186ad9648ff.html
    baseURL: https://{epo-server}:8443
    tags:
      - Compliance
      - Data Loss Prevention
      - Data Protection
      - Incident Management
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/data-loss-prevention-landing-page/page/UUID-d99a9913-80b8-d1b9-e030-9186ad9648ff.html
      - type: APIReference
        url: https://docs.trellix.com/bundle/data-loss-prevention-11.11.x-product-guide/page/UUID-fde8c193-c95f-0f3c-2ccf-926691ea31d8.html
  - name: Trellix Email Security Cloud API
    description: RESTful API for Trellix Email Security Cloud (formerly FireEye ETP) providing custom integration capabilities for advanced threat detection in email. Supports APIs for querying advanced threats, email trace, and quarantine management operations.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/fe-email-cloud-landing/page/UUID-aa9b8905-c585-0327-7f24-f66ea402d3b6.html
    baseURL: https://etp.us.fireeye.com/api/v1
    tags:
      - Cloud Security
      - Email Security
      - Quarantine
      - Threat Detection
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/fe-email-cloud-landing/page/UUID-aa9b8905-c585-0327-7f24-f66ea402d3b6.html
      - type: APIReference
        url: https://docs.trellix.com/bundle/etp_api/page/UUID-30726aa3-e420-6f62-6b84-6ad0bdace483.html
  - name: Trellix Helix API
    description: API for the Trellix Helix security operations platform that integrates security controls from Trellix and over 500 third-party sources to create multi-vector threat detections and AI-guided responses. The Helix API supports querying alerts, managing cases, searching events, and automating security operations workflows.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://www.trellix.com/products/helix/
    baseURL: https://apps.fireeye.com/helix/api/v3
    tags:
      - Security Operations
      - SIEM
      - SOAR
      - Threat Detection
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/helix_pg/page/UUID-889d9be0-0cc8-3ab3-cdb3-9aab24208509.html
      - type: APIReference
        url: https://docs.trellix.com/bundle/helix_pg/page/UUID-1fa29a61-f2d5-601e-dd27-e72f93627e59.html
  - name: Trellix Intelligent Sandbox API
    description: REST API for Trellix Intelligent Sandbox (formerly Advanced Threat Defense) that enables automated submission and analysis of files and URLs in a sandboxed environment. Supports file submission, analysis status queries, and report retrieval for malware detection and threat analysis.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/trellix-intelligent-sandbox-5.0.x-api-reference-guide/page/GUID-F600CDC5-827A-4435-BD37-E0DF91810AB1.html
    baseURL: https://{sandbox-server}/php
    tags:
      - File Analysis
      - Malware Analysis
      - Sandbox
      - Threat Detection
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/trellix-intelligent-sandbox-5.0.x-api-reference-guide/page/GUID-F600CDC5-827A-4435-BD37-E0DF91810AB1.html
      - type: GitHubRepository
        url: https://github.com/trellix-opensource/intelligent-sandbox-api
  - name: Trellix Threat Intelligence Exchange (TIE) API
    description: API for Trellix Threat Intelligence Exchange which acts as a reputation broker enabling real-time sharing of threat intelligence from global and local sources across the security ecosystem via the Data Exchange Layer. The TIE API allows querying file and certificate reputations, setting local reputations, and receiving reputation change notifications.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/threat-intelligence-exchange-3.0.x-product-guide
    baseURL: https://dxl.trellix.com
    tags:
      - Data Exchange
      - Malware Detection
      - Reputation
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/threat-intelligence-exchange-3.0.x-product-guide
      - type: SDKs
        url: https://github.com/opendxl/opendxl-tie-client-javascript
  - name: Trellix IOC (Indicators of Compromise) API
    description: REST API interface for managing indicators of compromise within the Trellix security platform. Enables uploading, querying, and managing IOCs including file hashes, IP addresses, domains, and email addresses for threat detection and investigation.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://docs.trellix.com/bundle/iocs_1-2-144_ug/page/UUID-d981cbd0-d535-dd8f-7cf8-a287bf077392.html
    baseURL: https://{hx-appliance}/hx/api/v3
    tags:
      - Indicators of Compromise
      - Security Operations
      - Threat Detection
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/iocs_1-2-144_ug/page/UUID-d981cbd0-d535-dd8f-7cf8-a287bf077392.html
      - type: APIReference
        url: https://docs.trellix.com/bundle/iocs_1-2-144_ug/page/UUID-11acd4c1-f095-333a-c394-5bfbf0a69823.html
  - name: Trellix Detection as a Service API
    description: API-driven malware detection service that leverages the Trellix Multi-Vector Virtual Execution (MVX) engine and multiple dynamic machine learning, AI, and correlation engines to analyze submitted files. Designed for integration into security operations workflows, SIEM systems, and custom web applications.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://www.trellix.com/products/detection-as-a-service/
    baseURL: https://feapi.marketplace.apps.fireeye.com
    tags:
      - Cloud Security
      - File Analysis
      - Malware Detection
      - Threat Detection
    properties:
      - type: Documentation
        url: https://developer.manage.trellix.com/mvision/docs/uma
  - name: Trellix API Explorer
    description: Interactive API documentation and testing tool for Trellix security products formerly under the FireEye brand. Provides a web-based interface for exploring and testing API endpoints across multiple Trellix product lines with regional endpoint support for US, EU, and AP data centers.
    image: https://www.trellix.com/favicon.ico
    humanURL: https://api-docs.us.fireeye.com/
    baseURL: https://api-docs.us.fireeye.com
    tags:
      - API Explorer
      - Developer Tools
      - Documentation
      - Testing
    properties:
      - type: Documentation
        url: https://api-docs.us.fireeye.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://www.trellix.com/
  - type: Developer Portal
    url: https://developer.manage.trellix.com/
  - type: Documentation
    url: https://docs.trellix.com/
  - type: Authentication
    url: https://developer.manage.trellix.com/mvision/docs/umam
  - type: GettingStarted
    url: https://developer.manage.trellix.com/mvision/docs/uma
  - type: Support
    url: https://www.trellix.com/support/
  - type: Login
    url: https://sso.trellix.com/
  - type: Sign Up
    url: https://developer.manage.trellix.com/
  - type: Community
    url: https://communitym.trellix.com/
  - type: Status
    url: https://status.trellix.com/
  - type: Blog
    url: https://www.trellix.com/blogs/
  - type: Privacy Policy
    url: https://www.trellix.com/en-us/about/legal/privacy.html
  - type: Terms of Service
    url: https://www.trellix.com/en-us/about/legal/terms-of-use.html
  - type: GitHubOrganization
    url: https://github.com/trellix-enterprise
  - type: GitHubOrganization
    url: https://github.com/opendxl
  - type: GitHubOrganization
    url: https://github.com/trellix-opensource
  - type: GitHubOrganization
    url: https://github.com/advanced-threat-research
  - type: Website
    url: https://www.trellix.com/
  - type: Knowledge Base
    url: https://kcm.trellix.com/
  - type: PostmanCollection
    url: https://www.postman.com/bmarandel/trellix-api-gateway/documentation/d3e3gan/trellix-api-gateway
  - type: ReleaseNotes
    url: https://docs.trellix.com/bundle/trellix-developer-portal-and-marketplace-release-notes
  - type: OpenAPI
    url: openapi/trellix-edr-openapi.yml
  - type: OpenAPI
    url: openapi/trellix-epo-saas-openapi.yml
  - type: JSONSchema
    url: json-schema/trellix-threat-schema.json
  - type: JSONSchema
    url: json-schema/trellix-device-schema.json
  - type: JSONStructure
    url: json-structure/trellix-threat-structure.json
  - type: JSON-LD
    url: json-ld/trellix-context.jsonld
  - type: SpectralRules
    url: rules/trellix-spectral-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/endpoint-security-operations.yaml
  - type: Vocabulary
    url: vocabulary/trellix-vocabulary.yml
---
