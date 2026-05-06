---
aid: uipath
name: UiPath
description: UiPath is an enterprise automation platform offering robotic process automation (RPA), AI-powered automation, and agentic automation capabilities. The platform includes Orchestrator for managing robots and automation jobs, Studio for developing automation workflows, Document Understanding for intelligent document processing, Data Service for structured data storage, Automation Hub for pipeline management and governance, Test Manager for automated testing, and Platform Management for organization and tenant administration. UiPath provides Python SDKs, REST APIs, and a rich integration ecosystem supporting enterprise automation at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Robotic Process Automation
  - RPA
  - Artificial Intelligence
  - Document Processing
  - Enterprise Automation
  - Orchestration
  - Testing
url: https://raw.githubusercontent.com/api-evangelist/uipath/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: uipath:uipath-orchestrator-api
    name: UiPath Orchestrator API
    description: The UiPath Orchestrator API provides programmatic access to the core automation management platform, enabling developers to manage robots, jobs, processes, queues, assets, schedules, and more. Built on the OData protocol, the API supports RESTful operations with filtering, sorting, and pagination across all resources. Authentication uses OAuth 2.0 tokens from the UiPath Identity Server.
    humanURL: https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/read-me
    baseURL: https://cloud.uipath.com/{organizationName}/{tenantName}/orchestrator_
    tags:
      - Orchestrator
      - Robots
      - Jobs
      - Queues
      - Automation
    properties:
      - type: Documentation
        url: https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/read-me
      - type: OpenAPI
        url: openapi/uipath-orchestrator-openapi.yml
      - type: AsyncAPI
        url: asyncapi/uipath-orchestrator-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/uipath-orchestrator-schema.json
      - type: JSONSchema
        url: json-schema/orchestrator-job-schema.json
      - type: JSONSchema
        url: json-schema/orchestrator-robot-schema.json
      - type: JSONSchema
        url: json-schema/orchestrator-queue-definition-schema.json
      - type: JSONSchema
        url: json-schema/orchestrator-queue-item-schema.json
      - type: JSONSchema
        url: json-schema/orchestrator-asset-schema.json
      - type: JSONStructure
        url: json-structure/orchestrator-job-structure.json
      - type: JSON-LD
        url: json-ld/uipath-orchestrator-context.jsonld
  - aid: uipath:uipath-automation-hub-api
    name: UiPath Automation Hub API
    description: The UiPath Automation Hub API provides access to the automation pipeline and idea management platform, allowing developers to programmatically create, retrieve, and manage automation ideas, projects, and pipeline data. Designed for organizations building Center of Excellence workflows and integrating Automation Hub with external tools.
    humanURL: https://docs.uipath.com/automation-hub/automation-cloud/latest/api-guide/introduction-to-automation-hub-api-1
    baseURL: https://cloud.uipath.com/{orgName}/{tenantName}/automationhub_/api/v1
    tags:
      - Automation Hub
      - Pipeline Management
      - Center of Excellence
      - Ideas
    properties:
      - type: Documentation
        url: https://docs.uipath.com/automation-hub/automation-cloud/latest/api-guide/introduction-to-automation-hub-api-1
      - type: OpenAPI
        url: openapi/uipath-automation-hub-openapi.yml
      - type: JSONSchema
        url: json-schema/automation-hub-automation-schema.json
      - type: JSONStructure
        url: json-structure/automation-hub-automation-structure.json
      - type: JSON-LD
        url: json-ld/uipath-automation-hub-context.jsonld
  - aid: uipath:uipath-document-understanding-api
    name: UiPath Document Understanding API
    description: The UiPath Document Understanding API enables intelligent document processing using machine learning and AI models. Developers can submit documents for digitization, classification, and data extraction, as well as manage custom ML models and training datasets.
    humanURL: https://docs.uipath.com/document-understanding/automation-cloud/latest/api-guide/api-overview
    baseURL: https://cloud.uipath.com/{organizationName}/{tenantName}/du_
    tags:
      - Document Understanding
      - Machine Learning
      - OCR
      - Data Extraction
      - Intelligent Document Processing
    properties:
      - type: Documentation
        url: https://docs.uipath.com/document-understanding/automation-cloud/latest/api-guide/api-overview
      - type: OpenAPI
        url: openapi/uipath-document-understanding-openapi.yml
      - type: JSONSchema
        url: json-schema/uipath-document-understanding-schema.json
      - type: JSONStructure
        url: json-structure/document-understanding-digitization-result-structure.json
      - type: JSON-LD
        url: json-ld/uipath-document-understanding-context.jsonld
  - aid: uipath:uipath-data-service-api
    name: UiPath Data Service API
    description: The UiPath Data Service API provides programmatic access to structured data storage within the UiPath Platform. Developers can create, read, update, and delete records in custom data entities, enabling automation workflows to read from and write to persistent cloud-based data stores.
    humanURL: https://docs.uipath.com/data-service/automation-cloud/latest/api-guide/about-the-data-service-api
    baseURL: https://cloud.uipath.com/{organizationName}/{tenantName}/dataservice_
    tags:
      - Data Service
      - Data Storage
      - Records
      - Entities
    properties:
      - type: Documentation
        url: https://docs.uipath.com/data-service/automation-cloud/latest/api-guide/about-the-data-service-api
      - type: OpenAPI
        url: openapi/uipath-data-service-openapi.yml
      - type: JSONSchema
        url: json-schema/data-service-entity-record-schema.json
      - type: JSONStructure
        url: json-structure/data-service-entity-record-structure.json
      - type: JSON-LD
        url: json-ld/uipath-data-service-context.jsonld
  - aid: uipath:uipath-platform-management-api
    name: UiPath Platform Management API
    description: The UiPath Platform Management API provides administrative access to organization and tenant management capabilities, including user management, license management, and account configuration. Used by platform administrators to manage UiPath Automation Cloud organizations programmatically.
    humanURL: https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/accessing-uipath-resources-using-external-apps
    baseURL: https://cloud.uipath.com
    tags:
      - Platform Management
      - Administration
      - Organizations
      - Tenants
      - Licensing
    properties:
      - type: Documentation
        url: https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/accessing-uipath-resources-using-external-apps
      - type: OpenAPI
        url: openapi/uipath-platform-management-openapi.yml
      - type: JSONStructure
        url: json-structure/platform-management-user-structure.json
      - type: JSON-LD
        url: json-ld/uipath-platform-management-context.jsonld
  - aid: uipath:uipath-test-manager-api
    name: UiPath Test Manager API
    description: The UiPath Test Manager API enables programmatic interaction with the automated testing platform, allowing CI/CD pipelines and external tools to create test sets, execute tests, and retrieve test results. Supports enterprise-grade test management and reporting workflows.
    humanURL: https://docs.uipath.com/test-manager/automation-cloud/latest/api-guide/test-manager-api
    baseURL: https://cloud.uipath.com/{organizationName}/{tenantName}/testmanager_
    tags:
      - Testing
      - Quality Assurance
      - CI/CD
      - Test Automation
    properties:
      - type: Documentation
        url: https://docs.uipath.com/test-manager/automation-cloud/latest/api-guide/test-manager-api
      - type: OpenAPI
        url: openapi/uipath-test-manager-openapi.yml
      - type: JSONSchema
        url: json-schema/test-manager-test-case-schema.json
      - type: JSONStructure
        url: json-structure/test-manager-test-case-structure.json
      - type: JSON-LD
        url: json-ld/uipath-test-manager-context.jsonld
common:
  - type: Website
    url: https://www.uipath.com
  - type: Documentation
    url: https://docs.uipath.com
  - type: Portal
    url: https://cloud.uipath.com
  - type: Blog
    url: https://www.uipath.com/blog
  - type: Pricing
    url: https://www.uipath.com/pricing
  - type: TermsOfService
    url: https://www.uipath.com/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.uipath.com/legal/privacy-policy
  - type: Support
    url: https://support.uipath.com
  - type: StatusPage
    url: https://status.uipath.com
  - type: Academy
    url: https://academy.uipath.com
  - type: Forum
    url: https://forum.uipath.com
  - type: GitHubOrganization
    url: https://github.com/UiPath
  - type: SDK
    url: https://pypi.org/project/uipath/
    title: Python SDK
  - type: SDK
    url: https://github.com/UiPath/uipath-python
    title: Python SDK GitHub
  - type: SDK
    url: https://github.com/UiPath/uipath-langchain-python
    title: LangChain Python SDK
  - type: SDK
    url: https://github.com/UiPath/uipath-typescript
    title: TypeScript SDK
  - type: SDK
    url: https://github.com/UiPath/uipath-integrations-python
    title: Python Integrations SDK
  - type: Tools
    url: https://github.com/UiPath/uipath-mcp-python
    title: MCP Server
  - type: CLI
    url: https://github.com/UiPath/uipathcli
    title: UiPath CLI
  - type: CLI
    url: https://docs.uipath.com/automation-cloud/docs/uipath-cli
  - type: Signup
    url: https://cloud.uipath.com/portal_/cloudrpa
  - type: GettingStarted
    url: https://docs.uipath.com/automation-cloud/docs/introduction
  - type: Authentication
    url: https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/accessing-uipath-resources-using-external-apps
  - type: SpectralRules
    url: rules/uipath-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/automation-operations.yaml
    title: Automation Operations
  - type: NaftikoCapability
    url: capabilities/intelligent-document-processing.yaml
    title: Intelligent Document Processing
  - type: NaftikoCapability
    url: capabilities/automation-governance.yaml
    title: Automation Governance
  - type: Vocabulary
    url: vocabulary/uipath-vocabulary.yaml
  - type: Features
    data:
      - name: Robotic Process Automation
        description: Automate repetitive tasks across any application using software robots with no-code, low-code, and coded automation options.
      - name: AI-Powered Automation
        description: Integrate AI capabilities including document understanding, computer vision, and natural language processing into automation workflows.
      - name: Agentic Automation
        description: Build and deploy intelligent agents using Python, LangGraph, or LlamaIndex frameworks on the UiPath Agent Cloud.
      - name: Document Understanding
        description: Extract structured data from unstructured documents using ML models for OCR, classification, and field extraction.
      - name: Orchestration
        description: Centrally manage and monitor automation robots, jobs, queues, schedules, and assets across the enterprise.
      - name: Process Mining
        description: Discover and analyze business processes to identify automation opportunities and measure impact.
      - name: Test Automation
        description: Create, manage, and execute automated tests for RPA and application testing with enterprise CI/CD integration.
      - name: Integration Service
        description: Connect to 1,000+ applications and services through pre-built connectors for enterprise integration.
  - type: UseCases
    data:
      - name: Finance and Accounting Automation
        description: Automate invoice processing, accounts payable/receivable, financial reporting, and compliance workflows.
      - name: HR Onboarding Automation
        description: Streamline employee onboarding, offboarding, payroll processing, and HR data management across systems.
      - name: Customer Service Automation
        description: Automate customer inquiry routing, case management, data lookup, and response generation.
      - name: IT Process Automation
        description: Automate IT service desk tickets, provisioning, monitoring alerts, and infrastructure management tasks.
      - name: Healthcare Administration
        description: Automate patient data management, claims processing, prior authorization, and regulatory reporting.
      - name: Supply Chain Automation
        description: Automate procurement, order management, inventory tracking, and logistics workflows.
  - type: Integrations
    data:
      - name: Salesforce
        description: Automate CRM operations, data sync, and customer workflows with native Salesforce integration.
      - name: SAP
        description: Connect with SAP ERP and S/4HANA for automated finance, HR, and supply chain processes.
      - name: Microsoft 365
        description: Automate Office applications, SharePoint, Teams, and Azure services through Microsoft 365 integration.
      - name: ServiceNow
        description: Integrate with ServiceNow for ITSM automation, ticket management, and service catalog workflows.
      - name: Workday
        description: Connect with Workday HCM for HR automation, payroll processing, and workforce management.
      - name: LangChain and LangGraph
        description: Build and deploy AI agents using LangChain and LangGraph frameworks on the UiPath platform.
  - type: Solutions
    data:
      - name: Automation Cloud Basic
        description: Entry-level cloud automation for individuals and small teams with basic RPA and limited scale.
      - name: Automation Cloud Standard
        description: Professional automation platform for businesses with unlimited users, robots, and enterprise data extraction.
      - name: Automation Cloud Enterprise
        description: Strategic enterprise automation with full infrastructure control, BYOK, multi-region deployment, and advanced AI capabilities.
      - name: Automation Cloud Public Sector
        description: FedRAMP Moderate authorized automation solution for U.S. government and public sector organizations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
