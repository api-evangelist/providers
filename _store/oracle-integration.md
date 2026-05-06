---
aid: oracle-integration
name: Oracle Integration
description: Oracle Integration provides native connectivity to Oracle and non-Oracle Software as a Service (SaaS) and on-premises applications, such as Oracle ERP Cloud, Oracle Service Cloud, HCM Cloud, Salesforce, Workday, EBS, SAP, NetSuite and others. It combines application integration, process automation, visual application building, and integration analytics into a single unified cloud service.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/apis.yml
tags:
  - API Management
  - Automation
  - B2B Integration
  - Cloud Integration
  - Enterprise Integration
  - Integration
  - iPaaS
  - Process Automation
apis:
  - name: Oracle Integration Developer API
    description: Developer API for Oracle Integration 3 providing day-to-day management of integrations, connections, packages, libraries, lookups, certificates, scheduled integrations, monitoring, B2B trading partner operations, and rapid adapter building.
    image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
    humanURL: https://docs.oracle.com/en/cloud/paas/application-integration/rest-api/index.html
    baseURL: https://{instance}.integration.ocp.oraclecloud.com/ic/api/integration/v1
    tags:
      - B2B
      - Connections
      - Integration Management
      - Monitoring
      - Orchestration
      - Packages
      - REST API
      - Scheduled Integrations
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/application-integration/rest-api/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/paas/application-integration/rest-api/rest-endpoints.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/paas/application-integration/rest-api/Authentication.html
      - type: OpenAPI
        url: openapi/oracle-integration-developer-api.yaml
      - type: JSONSchema
        url: json-schema/developer-api-connection-schema.json
        title: Connection Schema
      - type: JSONSchema
        url: json-schema/developer-api-integration-schema.json
        title: Integration Schema
      - type: JSONSchema
        url: json-schema/developer-api-monitoring-instance-schema.json
        title: Monitoring Instance Schema
      - type: JSONSchema
        url: json-schema/developer-api-trading-partner-schema.json
        title: Trading Partner Schema
      - type: JSONLD
        url: json-ld/oracle-integration-developer-api-context.jsonld
    contact:
      - FN: Oracle Integration Support
        email: oracle-integration-support@oracle.com
  - name: Oracle Integration Process Automation API
    description: REST API for Oracle Cloud Infrastructure Process Automation enabling management of process definitions, process instances, tasks, decision models, dynamic processes, identities, spaces, analytics, and QuickStart applications.
    image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
    humanURL: https://docs.oracle.com/en/cloud/paas/process-automation/rest-api-proca/index.html
    baseURL: https://{instance}.integration.ocp.oraclecloud.com/ic/api/process/v1
    tags:
      - BPM
      - Decision Models
      - Process Automation
      - Tasks
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/process-automation/rest-api-proca/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/paas/process-automation/rest-api-proca/rest-endpoints.html
      - type: OpenAPI
        url: openapi/oracle-integration-process-automation-api.yaml
      - type: JSONSchema
        url: json-schema/process-automation-api-process-instance-schema.json
        title: Process Instance Schema
      - type: JSONSchema
        url: json-schema/process-automation-api-task-schema.json
        title: Task Schema
      - type: JSONLD
        url: json-ld/oracle-integration-process-automation-api-context.jsonld
    contact:
      - FN: Oracle Integration Support
        email: oracle-integration-support@oracle.com
  - name: Oracle Integration File Server API
    description: REST API for configuring and administering the Oracle Integration File Server, an SFTP-compliant file repository for managing file-based integrations.
    image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
    humanURL: https://docs.oracle.com/en/cloud/paas/application-integration/rest-api-fs/index.html
    baseURL: https://{instance}.integration.ocp.oraclecloud.com/ic/api/fileserver/v1
    tags:
      - File Management
      - File Server
      - SFTP
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/application-integration/rest-api-fs/index.html
    contact:
      - FN: Oracle Integration Support
        email: oracle-integration-support@oracle.com
  - name: Oracle Integration Administrative API
    description: OCI control plane API for provisioning and managing Oracle Integration instances, custom endpoints, and data retention configuration.
    image: https://www.oracle.com/assets/ocom-logo-og-1200x628-1-5046771.jpg
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/integration/20190131/
    baseURL: https://integration.{region}.oci.oraclecloud.com
    tags:
      - Administration
      - Lifecycle Management
      - Provisioning
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/api/#/en/integration/20190131/
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/#/en/integration/20190131/
    contact:
      - FN: Oracle Integration Support
        email: oracle-integration-support@oracle.com
common:
  - type: Portal
    url: https://cloud.oracle.com/integration
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/paas/application-integration/oracle-integration-oci/explore-oracle-integration-apis.html
  - type: Tutorials
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/tutorials.html
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/paas/application-integration/index.html
  - type: Blog
    url: https://blogs.oracle.com/integration/
  - type: ChangeLog
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/whats-new/
  - type: Support
    url: https://www.oracle.com/support/
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: StatusPage
    url: https://ocistatus.oraclecloud.com/
  - type: Pricing
    url: https://www.oracle.com/integration/pricing/
  - type: Console
    url: https://cloud.oracle.com/integration
  - type: SDK
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
    title: OCI SDKs
  - type: CLI
    url: https://github.com/oracle/oci-cli
    title: OCI CLI
  - type: GitHubOrganization
    url: https://github.com/oracle
  - type: GitHubRepository
    url: https://github.com/oracle/oci-cli
    title: OCI CLI Repository
  - type: GitHubRepository
    url: https://github.com/oracle/oci-python-sdk
    title: Python SDK Repository
  - type: GitHubRepository
    url: https://github.com/oracle/oci-go-sdk
    title: Go SDK Repository
  - type: Training
    url: https://education.oracle.com/
  - type: Marketplace
    url: https://cloudmarketplace.oracle.com/marketplace/en_US/homeLinkPage
  - type: SpectralRules
    url: rules/oracle-integration-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/integration-management.yaml
    title: Integration Management Workflow
  - type: NaftikoCapability
    url: capabilities/shared/developer-api.yaml
    title: Developer API Shared Definition
  - type: NaftikoCapability
    url: capabilities/shared/process-automation-api.yaml
    title: Process Automation API Shared Definition
  - type: Vocabulary
    url: vocabulary/oracle-integration-vocabulary.yaml
  - type: Features
    data:
      - name: Prebuilt Integrations
        description: Library of prebuilt integration recipes and adapters for rapid deployment of common integration patterns.
      - name: Application Adapters
        description: Native connectivity to Oracle SaaS, on-premises applications, and third-party services including Salesforce, SAP, Workday, and ServiceNow.
      - name: Visual Integration Designer
        description: Low-code drag-and-drop integration designer for building integration flows without extensive coding.
      - name: B2B Document Exchange
        description: EDI and B2B document processing with support for trading partner management, document standards, and agreement lifecycle.
      - name: Process Automation
        description: Business process management with structured and unstructured workflows, case management, and task management.
      - name: Decision Modeling
        description: DMN-based decision model management for business rules execution and deployment.
      - name: Scheduled Integrations
        description: Time-based scheduling of integration flows with pause, resume, start, and stop controls.
      - name: Integration Monitoring
        description: Real-time monitoring of integration instances, error tracking, activity streams, and audit records.
      - name: File Server
        description: SFTP-compliant embedded file server for file-based integration scenarios.
      - name: Rapid Adapter Builder
        description: Custom adapter development framework for building reusable connectivity to proprietary or niche systems.
      - name: AI Agents
        description: AI agent capabilities within integration projects for intelligent automation patterns and prompt templates.
      - name: Machine Learning Recommendations
        description: ML-based guidance and recommendations for building and optimizing integrations.
      - name: Integration Analytics
        description: Built-in analytics and process analytics with custom query builders and data visualization.
      - name: FHIR Support
        description: Native Fast Healthcare Interoperability Resources support for healthcare integration workflows.
  - type: UseCases
    data:
      - name: SaaS Application Integration
        description: Connect Oracle SaaS applications like ERP Cloud, HCM Cloud, and CX Cloud with third-party SaaS platforms.
      - name: ERP Integration
        description: Integrate Oracle ERP Cloud or on-premises EBS with procurement, supply chain, and financial systems.
      - name: HCM Integration
        description: Synchronize human capital management data across Oracle HCM Cloud, Workday, and other HR systems.
      - name: B2B Trading Partner Onboarding
        description: Automate EDI-based trading partner setup, agreement management, and document exchange.
      - name: Process Automation
        description: Automate business processes with approval workflows, case management, and task orchestration.
      - name: Healthcare Data Exchange
        description: Build FHIR-compliant healthcare integration workflows for patient data exchange and interoperability.
      - name: Hybrid Cloud Integration
        description: Connect on-premises applications to Oracle Cloud and third-party cloud services via connectivity agents.
      - name: File-Based Integration
        description: Automate file transfers and processing with the embedded SFTP-compliant file server.
      - name: CI/CD For Integrations
        description: Manage integration lifecycle with export, import, and deployment APIs for DevOps automation.
      - name: Real-Time Event Processing
        description: Process events and messages in real time using event-driven integration patterns and stream analytics.
  - type: Integrations
    data:
      - name: Oracle ERP Cloud
        description: Native adapter for Oracle Enterprise Resource Planning Cloud including financials, procurement, and supply chain.
      - name: Oracle HCM Cloud
        description: Native adapter for Oracle Human Capital Management Cloud for HR, payroll, and talent management.
      - name: Oracle CX Cloud
        description: Native adapter for Oracle Customer Experience Cloud including sales, service, and marketing.
      - name: Oracle NetSuite
        description: Native adapter for Oracle NetSuite ERP and CRM cloud services.
      - name: Salesforce
        description: Prebuilt adapter for Salesforce CRM integration with Oracle cloud and on-premises applications.
      - name: SAP
        description: Adapter for SAP ERP and S/4HANA integration via IDoc, BAPI, and RFC protocols.
      - name: Workday
        description: Prebuilt adapter for Workday HCM and financial management integration.
      - name: ServiceNow
        description: Adapter for ServiceNow ITSM and ITOM integration with Oracle applications.
      - name: Shopify
        description: Adapter for Shopify e-commerce platform integration with order management and inventory systems.
      - name: Snowflake
        description: Adapter for Snowflake data warehouse integration for analytics and data pipelines.
      - name: Microsoft Azure
        description: Connectivity to Microsoft Azure services and applications for multi-cloud integration.
      - name: AWS
        description: Connectivity to Amazon Web Services for multi-cloud integration scenarios.
      - name: Slack
        description: Adapter for Slack messaging integration with workflow notifications and approvals.
      - name: JIRA
        description: Adapter for Atlassian JIRA project management and issue tracking integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
