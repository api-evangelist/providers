---
aid: solarwinds
name: SolarWinds
description: A collection of APIs provided by SolarWinds for IT infrastructure management, monitoring, and observability.
image: https://www.solarwinds.com/sites/all/themes/solarwinds_theme/logo.png
url: https://www.solarwinds.com/apis.json
tags:
  - Application Monitoring
  - Database Monitoring
  - Infrastructure
  - IP Address Management
  - IT Management
  - ITSM
  - Log Management
  - Network Monitoring
  - Observability
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Index
apis:
  - aid: solarwinds:solarwinds-orion-api
    name: SolarWinds Orion API
    description: RESTful API for managing and monitoring network devices, servers, and applications through the Orion Platform. Provides access to the SolarWinds Information Service (SWIS) using SWQL queries via REST endpoints.
    image: https://www.solarwinds.com/sites/default/files/orion-platform-icon.png
    humanURL: https://www.solarwinds.com/orion-platform
    baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
    tags:
      - Infrastructure Management
      - Network Monitoring
      - Orion
      - SWIS
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/orionplatform/content/core-swis-api.htm
      - type: OpenAPI
        url: openapi/solarwinds-orion-openapi.yml
      - type: Authentication
        url: https://documentation.solarwinds.com/en/success_center/orionplatform/content/core-swis-api-authentication.htm
      - type: SDK
        url: https://github.com/solarwinds/OrionSDK
      - type: APIReference
        url: https://github.com/solarwinds/OrionSDK/wiki/REST
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-service-desk-api
    name: SolarWinds Service Desk API
    description: API for IT service management, ticketing, and help desk operations. Provides CRUD access to incidents, service requests, changes, problems, releases, and asset management resources.
    humanURL: https://www.solarwinds.com/service-desk
    baseURL: https://{instance}.samanage.com/api
    tags:
      - Help Desk
      - ITSM
      - Service Desk
      - Ticketing
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/swsd/content/swsd_documentation.htm
      - type: APIReference
        url: https://apidoc.samanage.com/
      - type: Authentication
        url: https://help.samanage.com/s/article/API-Authentication
      - type: GettingStarted
        url: https://documentation.solarwinds.com/en/success_center/swsd/content/swsd_getting_started_guide.htm
      - type: OpenAPI
        url: openapi/solarwinds-service-desk-openapi.yml
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-observability-api
    name: SolarWinds Observability API
    description: Cloud-native observability API for logs, metrics, and distributed tracing.
    humanURL: https://www.solarwinds.com/solarwinds-observability
    baseURL: https://api.na-01.cloud.solarwinds.com
    tags:
      - APM
      - Cloud
      - Logs
      - Metrics
      - Monitoring
      - Observability
      - Tracing
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/observability/default.htm#cshid=api-overview
      - type: OpenAPI
        url: https://api.na-01.cloud.solarwinds.com/v1/openapi.json
      - type: APIReference
        url: https://documentation.solarwinds.com/en/success_center/observability/content/api/api-swagger.htm
      - type: Authentication
        url: https://documentation.solarwinds.com/en/success_center/observability/content/system/api-tokens.htm
      - type: SDK
        url: https://github.com/solarwinds
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-dpa-api
    name: SolarWinds Database Performance Analyzer API
    description: API for database monitoring and performance analysis.
    humanURL: https://www.solarwinds.com/database-performance-analyzer
    baseURL: https://{dpa-server}:8124/iwc/api
    tags:
      - Database
      - Monitoring
      - Performance
      - SQL
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/dpa/content/dpa-integrate-api.htm
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/dpa/default.htm
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-npm-rest-api
    name: SolarWinds NPM REST API
    description: Network Performance Monitor REST API for network device monitoring.
    humanURL: https://www.solarwinds.com/network-performance-monitor
    baseURL: https://{npm-server}:17778/SolarWinds/InformationService/v3
    tags:
      - Monitoring
      - Network
      - Performance
      - SNMP
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/npm/content/core-npm-rest-api.htm
      - type: SDK
        url: https://github.com/solarwinds/OrionSDK
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-whd-api
    name: SolarWinds Web Help Desk API
    description: REST API for creating, reading, updating, and deleting data in Web Help Desk including tickets, clients, assets, and locations.
    humanURL: https://www.solarwinds.com/web-help-desk
    baseURL: https://{whd-server}/helpdesk/WebObjects/Helpdesk.woa/ra
    tags:
      - Asset Management
      - Help Desk
      - IT Support
      - Ticketing
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/whd/content/helpdeskprogrammingrestapi.htm
      - type: Documentation
        url: https://documentation.solarwinds.com/archive/pdf/whd/whdapiguide.pdf
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-pingdom-api
    name: SolarWinds Pingdom API
    description: API for website uptime monitoring, performance monitoring, and transaction checks enabling automated management of checks, contacts, and reporting. Uses Bearer Token authentication for secure API access.
    humanURL: https://www.solarwinds.com/pingdom
    baseURL: https://api.pingdom.com/api/3.1
    tags:
      - Performance
      - Synthetic Monitoring
      - Uptime Monitoring
      - Website Monitoring
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/pingdom/content/topics/the-pingdom-api.htm
      - type: APIReference
        url: https://docs.pingdom.com/api/
      - type: Authentication
        url: https://documentation.solarwinds.com/en/success_center/pingdom/content/shared/sw-unified-login.htm
      - type: OpenAPI
        url: openapi/solarwinds-pingdom-openapi.yml
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-loggly-api
    name: SolarWinds Loggly API
    description: RESTful API for cloud-based log management including event submission, event retrieval, search, and account management. Supports sending events over HTTP/S and retrieving log data via paginating event retrieval endpoints.
    humanURL: https://www.solarwinds.com/loggly
    baseURL: https://{subdomain}.loggly.com/apiv2
    tags:
      - Cloud
      - Log Management
      - Logging
      - Search
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/api-overview.htm
      - type: APIReference
        url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/api-retrieving-data.htm
      - type: Authentication
        url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/token-based-api-authentication.htm
      - type: GettingStarted
        url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/api-sending-data.htm
      - type: OpenAPI
        url: openapi/solarwinds-loggly-openapi.yml
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-papertrail-api
    name: SolarWinds Papertrail API
    description: HTTP API for cloud-based log management including searching logs, managing systems, groups, saved searches, and user accounts. Provides endpoints for log search, settings management, and system configuration via token-based authentication.
    humanURL: https://www.solarwinds.com/papertrail
    baseURL: https://papertrailapp.com/api/v1
    tags:
      - Cloud
      - Log Management
      - Logging
      - Search
    properties:
      - type: Documentation
        url: https://www.papertrail.com/help/http-api/
      - type: APIReference
        url: https://www.papertrail.com/help/settings-api/
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/papertrail/content/kb/how-it-works/search-api.htm
      - type: OpenAPI
        url: openapi/solarwinds-papertrail-openapi.yml
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-ipam-api
    name: SolarWinds IPAM API
    description: API for IP address management providing CRUD operations for subnets, IP addresses, and DNS entries through the SolarWinds Information Service.
    humanURL: https://www.solarwinds.com/ip-address-manager
    baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
    tags:
      - DHCP
      - DNS
      - IP Address Management
      - IPAM
      - Network
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/ipam/content/ipam_documentation.htm
      - type: SDK
        url: https://github.com/solarwinds/OrionSDK
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-ncm-api
    name: SolarWinds NCM API
    description: API for network configuration management providing automation of configuration backups, change management, and compliance through the SolarWinds Information Service.
    humanURL: https://www.solarwinds.com/network-configuration-manager
    baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
    tags:
      - Automation
      - Compliance
      - Configuration Management
      - Network Configuration
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/ncm/content/ncm_documentation.htm
      - type: SDK
        url: https://github.com/solarwinds/OrionSDK
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-sam-api
    name: SolarWinds SAM API
    description: Server and Application Monitor API for monitoring application health and performance using the API Poller feature and SolarWinds Information Service.
    humanURL: https://www.solarwinds.com/server-application-monitor
    baseURL: https://{orion-server}:17778/SolarWinds/InformationService/v3
    tags:
      - APM
      - Application Monitoring
      - Performance
      - Server Monitoring
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/sam/content/sam_documentation.htm
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/sam/content/sam-api-poller-methods.htm
      - type: SDK
        url: https://github.com/solarwinds/OrionSDK
    contact:
      - type: Support
        url: https://support.solarwinds.com
  - aid: solarwinds:solarwinds-appoptics-api
    name: SolarWinds AppOptics API
    description: 'REST API for application performance monitoring providing CRUD access to metrics, dashboards, alerts, and traces. Supports custom metrics submission and distributed tracing for cloud-native applications. Note: AppOptics reached End of Service Life on November 30, 2025.'
    humanURL: https://documentation.solarwinds.com/en/success_center/appoptics/content/kb/custom_metrics/api.htm
    baseURL: https://api.appoptics.com/v1
    tags:
      - APM
      - Deprecated
      - Metrics
      - Monitoring
      - Tracing
    properties:
      - type: Documentation
        url: https://documentation.solarwinds.com/en/success_center/appoptics/content/kb/custom_metrics/api.htm
    contact:
      - type: Support
        url: https://support.solarwinds.com
common:
  - type: Portal
    url: https://www.solarwinds.com
  - type: Documentation
    url: https://documentation.solarwinds.com
  - type: Support
    url: https://support.solarwinds.com
  - type: Blog
    url: https://www.solarwinds.com/blog
  - type: GitHubOrganization
    url: https://github.com/solarwinds
  - type: StatusPage
    url: https://status.solarwinds.com
  - type: PrivacyPolicy
    url: https://www.solarwinds.com/legal/privacy
  - type: TermsOfService
    url: https://www.solarwinds.com/legal/terms
  - type: Login
    url: https://customerportal.solarwinds.com
  - type: Security
    url: https://www.solarwinds.com/information-security
  - type: X
    url: https://twitter.com/solarwinds
  - type: LinkedIn
    url: https://www.linkedin.com/company/solarwinds
  - type: SDK
    url: https://github.com/solarwinds/OrionSDK
  - type: CLI
    url: https://github.com/solarwinds/OrionSDK/tree/master/Samples/PowerShell
  - type: JSONLD
    url: json-ld/solarwinds-context.jsonld
  - type: JSONSchema
    url: json-schema/solarwinds-node-schema.json
  - type: JSONSchema
    url: json-schema/solarwinds-alert-schema.json
  - type: Features
    url: https://www.solarwinds.com
    data:
      - Network Device Monitoring via SWIS/SWQL
      - IT Service Management and Ticketing
      - Cloud-Native Observability (Logs, Metrics, Traces)
      - Website Uptime and Synthetic Monitoring
      - Cloud-Based Log Aggregation and Search
      - Database Performance Analysis
      - IP Address Management
      - Network Configuration Compliance
  - type: UseCases
    url: https://www.solarwinds.com
    data:
      - Network Infrastructure Monitoring and Alerting
      - IT Incident Management and Ticketing Workflows
      - Cloud Application Performance Monitoring
      - Centralized Log Management and Search
      - Website and API Uptime Monitoring
      - Database Query Performance Tuning
  - type: Integrations
    url: https://www.solarwinds.com
    data:
      - Slack
      - PagerDuty
      - Microsoft Teams
      - ServiceNow
      - Jira
      - AWS CloudWatch
      - Azure Monitor
      - Splunk
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
