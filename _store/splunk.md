---
aid: splunk
name: Splunk
description: Splunk is a platform for searching, monitoring, and analyzing machine-generated big data via a web-style interface.
image: https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico
url: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Analytics
  - Data Analysis
  - Logging
  - Machine Data
  - Monitoring
  - Observability
  - Platform
  - Security
  - SIEM
apis:
  - aid: splunk:splunk
    name: Splunk
    description: API monitoring checks to see if API-connected resources are available, working properly and responding to calls.
    humanURL: https://www.splunk.com/en_us/blog/learn/api-monitoring.html
    tags: []
    properties:
      - type: Documentation
        url: https://www.splunk.com/en_us/blog/learn/api-monitoring.html
  - aid: splunk:splunk-enterprise-rest-api
    name: Splunk Enterprise REST API
    description: The Splunk Enterprise REST API provides programmatic access to the same information and functionality available to core system software and Splunk Web. It supports GET, POST, and DELETE operations over HTTPS on the splunkd management port 8089.
    humanURL: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog
    tags:
      - Data
      - Enterprise
      - Management
      - REST
      - Search
    properties:
      - type: Documentation
        url: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog
      - type: GettingStarted
        url: https://docs.splunk.com/Documentation/Splunk/latest/RESTUM/RESTusing
      - type: APIReference
        url: https://dev.splunk.com/enterprise/reference
      - type: APIReference
        url: https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-reference/10.2/introduction/endpoints-reference-list
        title: Endpoints Reference List
      - type: Authentication
        url: https://docs.splunk.com/Documentation/Splunk/latest/RESTUM/RESTusing
      - type: Documentation
        url: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTsearch
        title: Search REST Reference
      - type: OpenAPI
        url: openapi/splunk-enterprise-rest-api.yml
      - type: JSONSchema
        url: json-schema/splunk-search-job-schema.json
      - type: JSONSchema
        url: json-schema/splunk-event-schema.json
      - type: JSONLD
        url: json-ld/splunk-context.jsonld
  - aid: splunk:splunk-cloud-platform-rest-api
    name: Splunk Cloud Platform REST API
    description: The Splunk Cloud Platform REST API provides a subset of the Splunk Enterprise REST API endpoints for managing and interacting with your Splunk Cloud Platform deployment. Access requires port 8089 to be opened by Splunk Support.
    humanURL: https://help.splunk.com/en/splunk-cloud-platform/rest-api-reference
    tags:
      - Cloud
      - Data
      - Management
      - REST
      - Search
    properties:
      - type: Documentation
        url: https://help.splunk.com/en/splunk-cloud-platform/rest-api-reference
      - type: GettingStarted
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/RESTTUT/RESTandCloud
      - type: APIReference
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/RESTREF/RESTprolog
  - aid: splunk:splunk-cloud-admin-config-service-api
    name: Splunk Cloud Admin Config Service (ACS) API
    description: The Admin Config Service (ACS) is a cloud-native API that provides programmatic self-service administration capabilities for Splunk Cloud Platform. Administrators can use the ACS API to manage indexes, IP allow lists, HEC tokens, users, and roles without assistance from Splunk Support. ACS provides an OpenAPI 3.0 specification.
    humanURL: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSIntro
    tags:
      - Administration
      - Cloud
      - Configuration
      - Management
    properties:
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSIntro
      - type: GettingStarted
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSusage
      - type: APIReference
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSREF
  - aid: splunk:splunk-cloud-admin-config-service-openapi
    name: Splunk Cloud ACS OpenAPI Specification
    description: The OpenAPI 3.0 specification for the Splunk Cloud Admin Config Service (ACS) API. It includes all parameters, response codes, and other metadata needed to send requests to the ACS API endpoint.
    humanURL: https://admin.splunk.com/service/info/specs/v2/openapi.json
    tags:
      - Administration
      - Cloud
      - OpenAPI
    properties:
      - type: OpenAPI
        url: https://admin.splunk.com/service/info/specs/v2/openapi.json
  - aid: splunk:splunk-observability-cloud-api
    name: Splunk Observability Cloud API
    description: The Splunk Observability Cloud API provides REST endpoints for sending and managing metrics, traces, and events. It supports infrastructure monitoring, application performance monitoring (APM), real user monitoring, and synthetic monitoring use cases.
    humanURL: https://dev.splunk.com/observability/
    tags:
      - APM
      - Metrics
      - Monitoring
      - Observability
      - Traces
    properties:
      - type: Documentation
        url: https://dev.splunk.com/observability/docs
      - type: APIReference
        url: https://dev.splunk.com/observability/reference
      - type: APIReference
        url: https://dev.splunk.com/observability/docs/apibasics/api_list/
        title: API List
      - type: Authentication
        url: https://dev.splunk.com/observability/docs/apibasics/authentication_basics/
      - type: Documentation
        url: https://dev.splunk.com/observability/docs/datamodel/ingest/
        title: Data Ingest
      - type: APIReference
        url: https://dev.splunk.com/observability/reference/api/ingest_data/latest
        title: Ingest Data Reference
      - type: Documentation
        url: https://dev.splunk.com/observability/docs/administration/authtokens
        title: Auth Tokens
  - aid: splunk:splunk-soar-rest-api
    name: Splunk SOAR REST API
    description: The Splunk SOAR REST API enables programmatic creation, updating, and management of security automation objects including containers, assets, playbooks, indicators, lists, and audit records. REST API requests must be performed over HTTPS with token-based or basic authentication.
    humanURL: https://docs.splunk.com/Documentation/SOAR/current/PlatformAPI/Using
    tags:
      - Automation
      - Orchestration
      - Playbooks
      - Security
      - SOAR
    properties:
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SOAR/current/PlatformAPI/Using
      - type: Documentation
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/using-the-splunk-soar-rest-api/using-the-rest-api-reference-for-splunk-soar-cloud
        title: SOAR Cloud REST API Reference
      - type: APIReference
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/container-endpoints/rest-containers
        title: Container Endpoints
      - type: APIReference
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/artifact-endpoints/rest-artifact
        title: Artifact Endpoints
      - type: Documentation
        url: https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/7.1.0/using-the-splunk-soar-rest-api/using-the-rest-api-reference-for-splunk-soar-on-premises
        title: SOAR On-Premises REST API Reference
  - aid: splunk:splunk-enterprise-security-api
    name: Splunk Enterprise Security API
    description: The Splunk Enterprise Security API provides REST endpoints for accessing and modifying findings, investigations, risk scores, assets, and identities in Splunk Enterprise Security. It includes an OpenAPI specification for download.
    humanURL: https://help.splunk.com/en/splunk-enterprise-security-8/api-reference
    tags:
      - Enterprise Security
      - Findings
      - Investigations
      - Security
      - SIEM
    properties:
      - type: Documentation
        url: https://help.splunk.com/en/splunk-enterprise-security-8/api-reference
      - type: APIReference
        url: https://help.splunk.com/en/splunk-enterprise-security-8/rest-api-reference
      - type: GettingStarted
        url: https://dev.splunk.com/enterprise/docs/devtools/enterprisesecurity
      - type: APIReference
        url: https://help.splunk.com/en/splunk-enterprise-security-8/rest-api-reference/8.0/threat-intelligence-endpoints/threat-intelligence-api-reference
        title: Threat Intelligence API
      - type: Documentation
        url: https://dev.splunk.com/enterprise/docs/devtools/enterprisesecurity/threatintelligenceframework/
        title: Threat Intelligence Framework
  - aid: splunk:splunk-itsi-rest-api
    name: Splunk IT Service Intelligence (ITSI) REST API
    description: The Splunk IT Service Intelligence (ITSI) REST API allows bulk creation and updating of ITOA interface objects such as entities, services, and KPI base searches. ITSI is a monitoring and analytics solution powered by artificial intelligence for IT Operations (AIOps).
    humanURL: https://help.splunk.com/en/splunk-it-service-intelligence/splunk-it-service-intelligence/leverage-rest-apis/4.19/itsi-rest-api-schema/itsi-rest-api-schema
    tags:
      - AIOps
      - IT Service Intelligence
      - ITSI
      - Monitoring
    properties:
      - type: Documentation
        url: https://help.splunk.com/en/splunk-it-service-intelligence/splunk-it-service-intelligence/leverage-rest-apis/4.19/itsi-rest-api-schema/itsi-rest-api-schema
      - type: APIReference
        url: https://help.splunk.com/en/splunk-it-service-intelligence/splunk-it-service-intelligence/leverage-rest-apis/4.18/itsi-rest-api-reference/itsi-rest-api-reference
  - aid: splunk:splunk-http-event-collector-api
    name: Splunk HTTP Event Collector (HEC) API
    description: The Splunk HTTP Event Collector (HEC) is a high-performance REST API data input that accepts JSON or raw text data sent over HTTP or HTTPS. It uses token-based authentication and provides endpoints for sending events (/services/collector/event), raw data (/services/collector/raw), and checking indexing status (/services/collector/ack).
    humanURL: https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector
    tags:
      - Data Ingestion
      - Events
      - HEC
      - Logging
      - REST
    properties:
      - type: Documentation
        url: https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector
      - type: APIReference
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/HECRESTendpoints
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/FormateventsforHTTPEventCollector
        title: Event Format
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/HECExamples
        title: HEC Examples
      - type: GettingStarted
        url: https://dev.splunk.com/view/event-collector/SP-CAAAE6M
  - aid: splunk:splunk-intelligence-management-api
    name: Splunk Intelligence Management API
    description: The Splunk Intelligence Management (formerly ThreatStream) API provides REST v2.0 endpoints for managing threat intelligence data including indicators, observables, and intelligence sources. It supports STIX and TAXII formats for sharing cyber threat intelligence over HTTPS.
    humanURL: https://docs.splunk.com/Documentation/SIM/current/Develop/RESTv20
    tags:
      - Indicators
      - Security
      - STIX
      - TAXII
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SIM/current/Develop/RESTv20
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SIM/current/User/Threatintelsources
        title: Threat Intel Sources
      - type: Documentation
        url: https://docs.splunk.com/Documentation/SIM/current/Intro/UsagePolicy
        title: Usage Policy
  - aid: splunk:splunk-soar-playbook-automation-api
    name: Splunk SOAR Playbook Automation API
    description: The Splunk SOAR Playbook Automation API provides Python APIs for developing playbooks and automation within Splunk SOAR. It includes container, playbook, data access, vault, network, and session automation APIs for building detailed security orchestration workflows.
    humanURL: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/overview/about-splunk-soar-cloud-playbook-automation-apis
    tags:
      - Automation
      - Orchestration
      - Playbooks
      - Security
      - SOAR
    properties:
      - type: Documentation
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/overview/about-splunk-soar-cloud-playbook-automation-apis
      - type: APIReference
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/container-automation-api
        title: Container Automation
      - type: APIReference
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/playbook-automation-api
        title: Playbook Automation
      - type: APIReference
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/data-access-automation-api
        title: Data Access Automation
      - type: APIReference
        url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/vault-automation-api
        title: Vault Automation
  - aid: splunk:splunk-appinspect-api
    name: Splunk AppInspect API
    description: The Splunk AppInspect API validates Splunk apps and add-ons against Splunk best practices and requirements for publishing to Splunkbase or installing on Splunk Cloud Platform. It provides automated app vetting through a REST API.
    humanURL: https://dev.splunk.com/enterprise/docs/relnotes/relnotes-appinspectapi/whatsnew
    tags:
      - Apps
      - Cloud
      - Splunkbase
      - Validation
    properties:
      - type: ChangeLog
        url: https://dev.splunk.com/enterprise/docs/relnotes/relnotes-appinspectapi/whatsnew
      - type: APIReference
        url: https://dev.splunk.com/enterprise/reference
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Splunk Inc.
    email: devinfo@splunk.com
    url: https://www.splunk.com
common:
  - type: DeveloperPortal
    url: https://dev.splunk.com/
  - type: Blog
    url: https://www.splunk.com/en_us/blog
  - type: Support
    url: https://www.splunk.com/en_us/support-and-services.html
  - type: StatusPage
    url: https://www.splunk.com/en_us/customer-success/splunk-services-status.html
  - type: Documentation
    url: https://community.splunk.com/
    title: Community
  - type: GitHubOrganization
    url: https://github.com/splunk
  - type: Documentation
    url: https://docs.splunk.com/Documentation
  - type: Documentation
    url: https://help.splunk.com/en
    title: Help Center
  - type: GettingStarted
    url: https://dev.splunk.com/enterprise/docs
  - type: Documentation
    url: https://dev.splunk.com/enterprise/docs/devtools/
    title: Developer Tools
  - type: Documentation
    url: https://dev.splunk.com/enterprise/downloads
    title: Downloads
  - type: Marketplace
    url: https://splunkbase.splunk.com/
  - type: Pricing
    url: https://www.splunk.com/en_us/products/pricing.html
  - type: SignUp
    url: https://www.splunk.com/en_us/download/splunk-cloud.html
  - type: SignUp
    url: https://dev.splunk.com/enterprise/dev_license/
    title: Developer License
  - type: TermsOfService
    url: https://www.splunk.com/en_us/legal/terms/terms-of-use.html
  - type: TermsOfService
    url: https://www.splunk.com/en_us/legal/splunk-general-terms.html
    title: General Terms
  - type: ChangeLog
    url: https://help.splunk.com/en/splunk-enterprise/release-notes-and-updates
  - type: Authentication
    url: https://docs.splunk.com/Documentation/Splunk/latest/RESTUM/RESTusing
  - type: SDK
    url: https://github.com/splunk/splunk-sdk-python
    title: Python SDK
  - type: SDK
    url: https://github.com/splunk/splunk-sdk-java
    title: Java SDK
  - type: SDK
    url: https://github.com/splunk/splunk-sdk-javascript
    title: JavaScript SDK
  - type: SDK
    url: https://github.com/splunk/splunk-sdk-csharp-pcl
    title: C# SDK
  - type: SDK
    url: https://dev.splunk.com/enterprise/docs/devtools/csharp
    title: C# SDK Documentation
  - type: ChangeLog
    url: https://dev.splunk.com/enterprise/docs/whatsnew/
    title: What's New
  - type: ChangeLog
    url: https://dev.splunk.com/enterprise/docs/relnotes
    title: Release Notes
  - type: Documentation
    url: https://dev.splunk.com/enterprise/docs/devtools/customrestendpoints
    title: Custom REST Endpoints
  - type: Authentication
    url: https://docs.splunk.com/Documentation/Splunk/latest/Security/UseAuthTokens
    title: Auth Tokens
  - type: PrivacyPolicy
    url: https://www.splunk.com/en_us/legal/privacy-policy.html
  - type: Security
    url: https://www.splunk.com/en_us/about-splunk/splunk-data-security-and-privacy.html
  - type: GitHubRepository
    url: https://github.com/signalfx/splunk-otel-collector
    title: OpenTelemetry Collector
  - type: LinkedIn
    url: https://www.linkedin.com/company/splunk
  - type: X
    url: https://twitter.com/splunk
  - type: SpectralRules
    url: rules/splunk-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/enterprise-rest.yaml
    title: Splunk Enterprise REST API Shared Definition
  - type: NaftikoCapability
    url: capabilities/search-and-analytics.yaml
    title: Search and Analytics Workflow
  - type: Features
    url: https://www.splunk.com/en_us/products.html
    data:
      - 'Splunk (now Cisco): hundreds of services across Observability + SIEM'
      - 'Detailed pricing: see https://www.splunk.com/en_us/products/pricing.html'
      - 'Service: Splunk Enterprise / Cloud (data ingest)'
      - 'Service: Splunk Observability Cloud (APM, Logs, RUM, Synthetics)'
      - 'Service: Splunk SOAR'
      - 'Service: Splunk Enterprise Security (SIEM)'
      - 'Service: Splunk ITSI'
      - 'Service: Splunk SOC Platform'
    sources:
      - https://www.splunk.com/en_us/products/pricing.html
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    url: https://www.splunk.com/en_us/solutions.html
    data:
      - name: Security Information and Event Management
        description: Centralize security event data for real-time threat detection, investigation, and compliance reporting.
      - name: IT Operations Monitoring
        description: Monitor infrastructure health, application performance, and service availability across hybrid environments.
      - name: Log Management
        description: Collect, index, and analyze log data from servers, applications, and network devices for troubleshooting.
      - name: Incident Response Automation
        description: Automate security incident triage, enrichment, and response using SOAR playbooks and integrations.
      - name: Application Performance Monitoring
        description: Trace application requests end-to-end to identify bottlenecks and optimize performance.
      - name: Compliance and Audit
        description: Generate compliance reports and audit trails from indexed data to meet regulatory requirements.
  - type: Integrations
    url: https://splunkbase.splunk.com/
    data:
      - name: AWS
        description: Ingest and analyze AWS CloudTrail, CloudWatch, VPC Flow Logs, and other AWS service data.
      - name: Azure
        description: Collect and analyze Azure activity logs, metrics, and diagnostic data.
      - name: Google Cloud
        description: Ingest Google Cloud audit logs, metrics, and Pub/Sub messages for cloud monitoring.
      - name: Kubernetes
        description: Monitor Kubernetes clusters with metrics, logs, and events from containers and orchestration.
      - name: ServiceNow
        description: Integrate Splunk alerts and incidents with ServiceNow ITSM for ticketing and workflow automation.
      - name: PagerDuty
        description: Trigger PagerDuty incidents from Splunk alerts for on-call notification and escalation.
      - name: Cisco
        description: Collect and analyze Cisco network device logs, firewall events, and security telemetry.
      - name: CrowdStrike
        description: Ingest CrowdStrike Falcon endpoint detection data for correlated threat analysis.
---
