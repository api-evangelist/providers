---
aid: splunk
url: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/apis.yml
apis:
- aid: splunk:splunk
  name: Splunk
  tags: []
  humanURL: https://www.splunk.com/en_us/blog/learn/api-monitoring.html
  properties:
  - url: https://www.splunk.com/en_us/blog/learn/api-monitoring.html
    type: Documentation
  description: API monitoring checks to see if API-connected resources are available, working properly and responding to calls.
- aid: splunk:splunk-enterprise-rest-api
  name: Splunk Enterprise REST API
  tags:
  - Data
  - Enterprise
  - Management
  - REST
  - Search
  humanURL: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog
  properties:
  - url: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog
    type: Documentation
  - url: https://docs.splunk.com/Documentation/Splunk/latest/RESTUM/RESTusing
    type: Getting Started
  - url: https://dev.splunk.com/enterprise/reference
    type: API Reference
  - url: https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-reference/10.2/introduction/endpoints-reference-list
    type: API Reference
  - url: https://docs.splunk.com/Documentation/Splunk/latest/RESTUM/RESTusing
    type: Authentication
  - url: https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTsearch
    type: Documentation
  - url: openapi/splunk-enterprise-rest-api.yml
    type: OpenAPI
  - url: json-schema/splunk-search-job-schema.json
    type: JSONSchema
  - url: json-schema/splunk-event-schema.json
    type: JSONSchema
  - url: json-ld/splunk-context.jsonld
    type: JSON-LD Context
  description: The Splunk Enterprise REST API provides programmatic access to the same information and functionality available to core system software and Splunk Web. It supports GET, POST, and DELETE operations over HTTPS on the splunkd management port 8089.
- aid: splunk:splunk-cloud-platform-rest-api
  name: Splunk Cloud Platform REST API
  tags:
  - Cloud
  - Data
  - Management
  - REST
  - Search
  humanURL: https://help.splunk.com/en/splunk-cloud-platform/rest-api-reference
  properties:
  - url: https://help.splunk.com/en/splunk-cloud-platform/rest-api-reference
    type: Documentation
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/RESTTUT/RESTandCloud
    type: Getting Started
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/RESTREF/RESTprolog
    type: API Reference
  description: The Splunk Cloud Platform REST API provides a subset of the Splunk Enterprise REST API endpoints for managing and interacting with your Splunk Cloud Platform deployment. Access requires port 8089 to be opened by Splunk Support.
- aid: splunk:splunk-cloud-admin-config-service-api
  name: Splunk Cloud Admin Config Service (ACS) API
  tags:
  - Administration
  - Cloud
  - Configuration
  - Management
  humanURL: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSIntro
  properties:
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSIntro
    type: Documentation
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSusage
    type: Getting Started
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Config/ACSREF
    type: API Reference
  description: The Admin Config Service (ACS) is a cloud-native API that provides programmatic self-service administration capabilities for Splunk Cloud Platform. Administrators can use the ACS API to manage indexes, IP allow lists, HEC tokens, users, and roles without assistance from Splunk Support. ACS provides an OpenAPI 3.0 specification.
- aid: splunk:splunk-cloud-admin-config-service-openapi
  name: Splunk Cloud ACS OpenAPI Specification
  tags:
  - Administration
  - Cloud
  - OpenAPI
  humanURL: https://admin.splunk.com/service/info/specs/v2/openapi.json
  properties:
  - url: https://admin.splunk.com/service/info/specs/v2/openapi.json
    type: OpenAPI
  description: The OpenAPI 3.0 specification for the Splunk Cloud Admin Config Service (ACS) API. It includes all parameters, response codes, and other metadata needed to send requests to the ACS API endpoint.
- aid: splunk:splunk-observability-cloud-api
  name: Splunk Observability Cloud API
  tags:
  - APM
  - Metrics
  - Monitoring
  - Observability
  - Traces
  humanURL: https://dev.splunk.com/observability/
  properties:
  - url: https://dev.splunk.com/observability/docs
    type: Documentation
  - url: https://dev.splunk.com/observability/reference
    type: API Reference
  - url: https://dev.splunk.com/observability/docs/apibasics/api_list/
    type: API Reference
  - url: https://dev.splunk.com/observability/docs/apibasics/authentication_basics/
    type: Authentication
  - url: https://dev.splunk.com/observability/docs/datamodel/ingest/
    type: Documentation
  - url: https://dev.splunk.com/observability/reference/api/ingest_data/latest
    type: API Reference
  - url: https://dev.splunk.com/observability/docs/administration/authtokens
    type: Documentation
  description: The Splunk Observability Cloud API provides REST endpoints for sending and managing metrics, traces, and events. It supports infrastructure monitoring, application performance monitoring (APM), real user monitoring, and synthetic monitoring use cases.
- aid: splunk:splunk-soar-rest-api
  name: Splunk SOAR REST API
  tags:
  - Automation
  - Orchestration
  - Playbooks
  - Security
  - SOAR
  humanURL: https://docs.splunk.com/Documentation/SOAR/current/PlatformAPI/Using
  properties:
  - url: https://docs.splunk.com/Documentation/SOAR/current/PlatformAPI/Using
    type: Documentation
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/using-the-splunk-soar-rest-api/using-the-rest-api-reference-for-splunk-soar-cloud
    type: Documentation
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/container-endpoints/rest-containers
    type: API Reference
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/rest-api-reference/artifact-endpoints/rest-artifact
    type: API Reference
  - url: https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/7.1.0/using-the-splunk-soar-rest-api/using-the-rest-api-reference-for-splunk-soar-on-premises
    type: Documentation
  description: The Splunk SOAR REST API enables programmatic creation, updating, and management of security automation objects including containers, assets, playbooks, indicators, lists, and audit records. REST API requests must be performed over HTTPS with token-based or basic authentication.
- aid: splunk:splunk-enterprise-security-api
  name: Splunk Enterprise Security API
  tags:
  - Enterprise Security
  - Findings
  - Investigations
  - Security
  - SIEM
  humanURL: https://help.splunk.com/en/splunk-enterprise-security-8/api-reference
  properties:
  - url: https://help.splunk.com/en/splunk-enterprise-security-8/api-reference
    type: Documentation
  - url: https://help.splunk.com/en/splunk-enterprise-security-8/rest-api-reference
    type: API Reference
  - url: https://dev.splunk.com/enterprise/docs/devtools/enterprisesecurity
    type: Getting Started
  - url: https://help.splunk.com/en/splunk-enterprise-security-8/rest-api-reference/8.0/threat-intelligence-endpoints/threat-intelligence-api-reference
    type: API Reference
  - url: https://dev.splunk.com/enterprise/docs/devtools/enterprisesecurity/threatintelligenceframework/
    type: Documentation
  description: The Splunk Enterprise Security API provides REST endpoints for accessing and modifying findings, investigations, risk scores, assets, and identities in Splunk Enterprise Security. It includes an OpenAPI specification for download.
- aid: splunk:splunk-itsi-rest-api
  name: Splunk IT Service Intelligence (ITSI) REST API
  tags:
  - AIOps
  - IT Service Intelligence
  - ITSI
  - Monitoring
  humanURL: https://help.splunk.com/en/splunk-it-service-intelligence/splunk-it-service-intelligence/leverage-rest-apis/4.19/itsi-rest-api-schema/itsi-rest-api-schema
  properties:
  - url: https://help.splunk.com/en/splunk-it-service-intelligence/splunk-it-service-intelligence/leverage-rest-apis/4.19/itsi-rest-api-schema/itsi-rest-api-schema
    type: Documentation
  - url: https://help.splunk.com/en/splunk-it-service-intelligence/splunk-it-service-intelligence/leverage-rest-apis/4.18/itsi-rest-api-reference/itsi-rest-api-reference
    type: API Reference
  description: The Splunk IT Service Intelligence (ITSI) REST API allows bulk creation and updating of ITOA interface objects such as entities, services, and KPI base searches. ITSI is a monitoring and analytics solution powered by artificial intelligence for IT Operations (AIOps).
- aid: splunk:splunk-http-event-collector-api
  name: Splunk HTTP Event Collector (HEC) API
  tags:
  - Data Ingestion
  - Events
  - HEC
  - Logging
  - REST
  humanURL: https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector
  properties:
  - url: https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector
    type: Documentation
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/HECRESTendpoints
    type: API Reference
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/FormateventsforHTTPEventCollector
    type: Documentation
  - url: https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/HECExamples
    type: Documentation
  - url: https://dev.splunk.com/view/event-collector/SP-CAAAE6M
    type: Getting Started
  description: The Splunk HTTP Event Collector (HEC) is a high-performance REST API data input that accepts JSON or raw text data sent over HTTP or HTTPS. It uses token-based authentication and provides endpoints for sending events (/services/collector/event), raw data (/services/collector/raw), and checking indexing status (/services/collector/ack).
- aid: splunk:splunk-intelligence-management-api
  name: Splunk Intelligence Management API
  tags:
  - Indicators
  - Security
  - STIX
  - TAXII
  - Threat Intelligence
  humanURL: https://docs.splunk.com/Documentation/SIM/current/Develop/RESTv20
  properties:
  - url: https://docs.splunk.com/Documentation/SIM/current/Develop/RESTv20
    type: Documentation
  - url: https://docs.splunk.com/Documentation/SIM/current/User/Threatintelsources
    type: Documentation
  - url: https://docs.splunk.com/Documentation/SIM/current/Intro/UsagePolicy
    type: Documentation
  description: The Splunk Intelligence Management (formerly ThreatStream) API provides REST v2.0 endpoints for managing threat intelligence data including indicators, observables, and intelligence sources. It supports STIX and TAXII formats for sharing cyber threat intelligence over HTTPS.
- aid: splunk:splunk-soar-playbook-automation-api
  name: Splunk SOAR Playbook Automation API
  tags:
  - Automation
  - Orchestration
  - Playbooks
  - Security
  - SOAR
  humanURL: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/overview/about-splunk-soar-cloud-playbook-automation-apis
  properties:
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/overview/about-splunk-soar-cloud-playbook-automation-apis
    type: Documentation
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/container-automation-api
    type: API Reference
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/playbook-automation-api
    type: API Reference
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/data-access-automation-api
    type: API Reference
  - url: https://help.splunk.com/en/splunk-soar/soar-cloud/develop-apps/python-playbook-api-reference/automation-api/vault-automation-api
    type: API Reference
  description: The Splunk SOAR Playbook Automation API provides Python APIs for developing playbooks and automation within Splunk SOAR. It includes container, playbook, data access, vault, network, and session automation APIs for building detailed security orchestration workflows.
- aid: splunk:splunk-appinspect-api
  name: Splunk AppInspect API
  tags:
  - Apps
  - Cloud
  - Splunkbase
  - Validation
  humanURL: https://dev.splunk.com/enterprise/docs/relnotes/relnotes-appinspectapi/whatsnew
  properties:
  - url: https://dev.splunk.com/enterprise/docs/relnotes/relnotes-appinspectapi/whatsnew
    type: Change Log
  - url: https://dev.splunk.com/enterprise/reference
    type: API Reference
  description: The Splunk AppInspect API validates Splunk apps and add-ons against Splunk best practices and requirements for publishing to Splunkbase or installing on Splunk Cloud Platform. It provides automated app vetting through a REST API.
name: Splunk
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
type: Index
image: https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Splunk is a platform for searching, monitoring, and analyzing machine-generated big data via a web-style interface.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

