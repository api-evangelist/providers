---
aid: oracle-integration
url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/apis.yml
apis:
- name: Oracle Integration REST API
  description: REST API for managing integrations, connections, adapters, and monitoring integration instances.
  image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
  humanURL: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/
  baseURL: https://<instance-name>.integration.ocp.oraclecloud.com/ic/api/integration/v1
  tags:
  - Integration Management
  - Orchestration
  - REST API
  properties:
  - type: x-documentation
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/
  - type: x-openapi
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/openapi.json
  - type: x-authentication
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/Authentication.html
  - type: x-rate-limits
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/integration-cloud-service-limits.html
  - type: x-pricing
    url: https://www.oracle.com/cloud/integration/pricing.html
  contact:
  - FN: Oracle Integration Support
    email: oracle-integration-support@oracle.com
    x-twitter: Oracle
- name: Oracle Integration Monitoring API
  description: API for monitoring integration flows, tracking messages, and viewing activity streams.
  image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
  humanURL: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/op-ic-api-integration-v1-monitoring-integrations-get.html
  baseURL: https://<instance-name>.integration.ocp.oraclecloud.com/ic/api/integration/v1/monitoring
  tags:
  - Analytics
  - Logging
  - Monitoring
  properties:
  - type: x-documentation
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/integration-monitoring.html
  - type: x-openapi
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/openapi-monitoring.json
- name: Oracle Integration Connections API
  description: API for creating and managing connections to various applications and services.
  image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
  humanURL: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/Connections.html
  baseURL: https://<instance-name>.integration.ocp.oraclecloud.com/ic/api/integration/v1/connections
  tags:
  - Adapters
  - Configuration
  - Connections
  properties:
  - type: x-documentation
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/Connections.html
- name: Oracle Integration Process Automation API
  description: API for Oracle Process Automation workflows and approvals.
  image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
  humanURL: https://docs.oracle.com/en/cloud/paas/process-automation/
  baseURL: https://<instance-name>.integration.ocp.oraclecloud.com/ic/api/process/v1
  tags:
  - BPM
  - Process Automation
  - Workflows
  properties:
  - type: x-documentation
    url: https://docs.oracle.com/en/cloud/paas/process-automation/user-process-automation/
name: Oracle Integration
tags:
- API Management
- Automation
- Cloud Integration
- Integration
- iPaaS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Integration provides native connectivity to Oracle and non-Oracle Software as a Service (SaaS) and On-premises applications, such as Oracle ERP Cloud, Oracle Service Cloud, HCM Cloud, Salesforce, Workday, EBS, SAP, NetSuite and others.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

