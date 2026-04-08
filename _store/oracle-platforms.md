---
aid: oracle-platforms
url: https://raw.githubusercontent.com/api-evangelist/oracle-platforms/refs/heads/main/apis.yml
apis:
- name: Oracle Cloud Infrastructure (OCI) REST API
  description: Comprehensive REST API for managing Oracle Cloud Infrastructure resources including compute, storage, networking, and databases.
  image: https://www.oracle.com/cloud/img/social-og-oracle-cloud.jpg
  humanURL: https://docs.oracle.com/en-us/iaas/api/
  baseURL: https://iaas.{region}.oraclecloud.com
  tags:
  - Cloud
  - Compute
  - IaaS
  - Infrastructure
  - Storage
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/api/
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/
  - type: X-authentication
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
  - type: X-rate-limits
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apithrottling.htm
  - type: X-sdk
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
- name: Oracle Autonomous Database API
  description: API for managing Oracle Autonomous Database instances with self-driving, self-securing, and self-repairing capabilities.
  humanURL: https://docs.oracle.com/en/cloud/paas/autonomous-database/
  baseURL: https://database.{region}.oraclecloud.com
  tags:
  - Autonomous
  - Database
  - DBaaS
  - SQL
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/database/latest/
  - type: X-pricing
    url: https://www.oracle.com/cloud/price-list.html
- name: Oracle Integration Cloud API
  description: REST API for Oracle Integration Cloud enabling application integration, process automation, and API management.
  humanURL: https://docs.oracle.com/en/cloud/paas/integration-cloud/
  baseURL: https://integration.ocp.oraclecloud.com
  tags:
  - API Management
  - Automation
  - Integration
  - iPaaS
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/
  - type: X-openapi
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/api-integration-cloud.html
- name: Oracle Content Management API
  description: RESTful API for Oracle Content Management providing digital asset management and content collaboration.
  humanURL: https://docs.oracle.com/en/cloud/paas/content-cloud/
  baseURL: https://www.oraclecloud.com/content/api
  tags:
  - CMS
  - Collaboration
  - Content Management
  - Digital Assets
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en/cloud/paas/content-cloud/rest-api-documents/
  - type: X-sdk
    url: https://github.com/oracle/content-management-sdk
- name: Oracle Fusion Cloud ERP API
  description: REST API for Oracle Fusion Cloud ERP providing access to financial management, procurement, and project management capabilities.
  humanURL: https://docs.oracle.com/en/cloud/saas/financials/
  baseURL: https://servername.fa.us2.oraclecloud.com
  tags:
  - Cloud Applications
  - ERP
  - Finance
  - Procurement
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en/cloud/saas/financials/farsw/
  - type: X-wadl
    url: https://docs.oracle.com/en/cloud/saas/financials/farsw/rest-endpoints.html
- name: Oracle Analytics Cloud API
  description: RESTful API for Oracle Analytics Cloud enabling data visualization, analytics, and business intelligence operations.
  humanURL: https://docs.oracle.com/en/cloud/paas/analytics-cloud/
  baseURL: https://{instanceName}.analytics.ocp.oraclecloud.com
  tags:
  - Analytics
  - Business Intelligence
  - Data Visualization
  - Reporting
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acapi/
  - type: X-openapi
    url: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acapi/api-rest.html
- name: Oracle Cloud Infrastructure Data Science API
  description: API for managing machine learning models, notebook sessions, and data science projects.
  humanURL: https://docs.oracle.com/en-us/iaas/data-science/
  baseURL: https://datascience.{region}.oraclecloud.com
  tags:
  - AI
  - Data Science
  - Machine Learning
  - MLOps
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en-us/iaas/api/#/en/data-science/latest/
  - type: X-openapi
    url: https://docs.oracle.com/en-us/iaas/api/#/en/data-science/latest/
- name: Oracle APEX REST APIs
  description: RESTful services for Oracle Application Express enabling low-code application development.
  humanURL: https://apex.oracle.com/api
  baseURL: https://{instance}.adb.{region}.oraclecloudapps.com
  tags:
  - APEX
  - Application Development
  - Low-Code
  - REST Services
  properties:
  - type: X-documentation
    url: https://docs.oracle.com/en/database/oracle/apex/latest/
  - type: X-tutorials
    url: https://apex.oracle.com/en/learn/tutorials/
name: Oracle Platforms
tags:
- Analytics
- Cloud Computing
- Database
- Enterprise Software
- Infrastructure as a Service
- Integration
- Machine Learning
- Platform as a Service
- SaaS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs and services provided by Oracle's cloud and enterprise platforms.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

