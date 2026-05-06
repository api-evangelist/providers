---
name: SAP
description: Collection of SAP's enterprise APIs for business applications and cloud services.
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
url: https://api.sap.com
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.18'
apis:
  - name: SAP Business One Service Layer API
    description: RESTful API for accessing SAP Business One data and business logic.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/SAP_BUSINESS_ONE_SERVICE_LAYER
    baseUrl: https://{server}:50000/b1s/v1
    tags:
      - Business Management
      - Enterprise
      - ERP
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_BUSINESS_ONE_SERVICE_LAYER
      - type: OpenAPI
        url: openapi/sap-business-one-service-layer-openapi.yml
      - type: Authentication
        url: https://help.sap.com/docs/SAP_BUSINESS_ONE_SERVICE_LAYER/0a7d48c2c45a4732914129e920b0a8c1/Authentication.html
      - type: GettingStarted
        url: https://help.sap.com/docs/SAP_BUSINESS_ONE_SERVICE_LAYER/0a7d48c2c45a4732914129e920b0a8c1/Getting_Started.html
  - name: SAP S/4HANA Cloud API
    description: APIs for SAP S/4HANA Cloud enabling integration with intelligent ERP.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/package/SAPS4HANACloud
    baseUrl: https://sandbox.api.sap.com/s4hanacloud
    tags:
      - Cloud
      - Enterprise Resource Planning
      - ERP
      - S/4HANA
    properties:
      - type: OpenAPI
        url: openapi/sap-s4hana-cloud-business-partner-openapi.yml
      - type: Documentation
        url: https://api.sap.com/package/SAPS4HANACloud
      - type: Hub
        url: https://api.sap.com/package/SAPS4HANACloud/rest
      - type: Sandbox
        url: https://api.sap.com/api/API_BUSINESS_PARTNER/tryout
      - type: GettingStarted
        url: https://help.sap.com/docs/SAP_S4HANA_CLOUD
  - name: SAP SuccessFactors API
    description: Human Capital Management APIs for employee central, recruiting, and talent management.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/package/SAPSuccessFactors
    baseUrl: https://api.successfactors.com/odata/v2
    tags:
      - HCM
      - HR
      - Human Resources
      - Talent Management
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/
      - type: APIReference
        url: https://api.sap.com/package/SAPSuccessFactors/odata
      - type: APIReference
        url: https://help.sap.com/doc/74597e67f54d4f448252bad4c2b601c9/
      - type: Hub
        url: https://api.sap.com/package/SAPSuccessFactors
  - name: SAP Ariba APIs
    description: Procurement and supply chain APIs for sourcing, contracts, and supplier management.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://developer.ariba.com
    baseUrl: https://openapi.ariba.com
    tags:
      - Procurement
      - Sourcing
      - Supplier Management
      - Supply Chain
    properties:
      - type: Documentation
        url: https://developer.ariba.com/api
      - type: DeveloperPortal
        url: https://developer.ariba.com
      - type: APIReference
        url: https://developer.ariba.com/api/guides
  - name: SAP Cloud Platform Integration Suite
    description: Integration APIs for connecting applications, data, and processes.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/package/CloudPlatformIntegration
    baseUrl: https://{tenant}.it-cpi{xx}.cfapps.{region}.hana.ondemand.com
    tags:
      - Cloud Platform
      - Integration
      - iPaaS
      - Middleware
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/CLOUD_INTEGRATION
      - type: Hub
        url: https://api.sap.com/package/CloudPlatformIntegration
      - type: Training
        url: https://help.sap.com/learning-journeys/integrate-applications-and-services
      - type: GettingStarted
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management-capability
  - name: SAP Commerce Cloud API
    description: E-commerce APIs for product catalog, cart, checkout, and order management.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/SAP_COMMERCE_CLOUD
    baseUrl: https://{baseSiteId}.{environment}/rest/v2
    tags:
      - Commerce
      - E-Commerce
      - OCC
      - Retail
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/0996ba68e5794b8ab51db8d25d4c9f4a/
      - type: APIReference
        url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/9d346683b0084da2938be8a285c0c27a/
      - type: APIReference
        url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD/9d346683b0084da2938be8a285c0c27a/swagger.html
  - name: SAP Analytics Cloud API
    description: APIs for business intelligence, planning, and predictive analytics.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD
    baseUrl: https://{tenant}.{region}.sapanalytics.cloud/api/v1
    tags:
      - Analytics
      - BI
      - Business Intelligence
      - Planning
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/
      - type: APIReference
        url: https://help.sap.com/doc/14cac91febef464dbb1efce20e3f1613/release/en-US/index.html
      - type: APIReference
        url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/c7c2d8a03f524126af618f2cdac43595/
  - name: SAP Concur API
    description: APIs for travel and expense management including expense reporting, travel booking, and invoice processing.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://developer.concur.com
    baseUrl: https://us.api.concursolutions.com
    tags:
      - Concur
      - Expense Management
      - Invoice
      - Travel
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/
      - type: DeveloperPortal
        url: https://developer.concur.com
      - type: Authentication
        url: https://developer.concur.com/api-reference/authentication/getting-started.html
      - type: Hub
        url: https://api.sap.com/products/SAPConcur/apis/REST
      - type: ChangeLog
        url: https://developer.concur.com/tools-support/release-notes/
  - name: SAP Fieldglass API
    description: Vendor management system APIs for managing external workers, contractors, and service providers.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/products/SAPFieldglass/apis/packages
    baseUrl: https://www.fieldglass.net/api
    tags:
      - Contingent Workforce
      - External Workers
      - Vendor Management
      - VMS
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION
      - type: Hub
        url: https://api.sap.com/package/FieldglassAPI
      - type: APIReference
        url: https://api.sap.com/package/FieldglassAPI/odata
      - type: APIReference
        url: https://api.sap.com/products/SAPFieldglass/apis/all
  - name: SAP BTP Core Services API
    description: Core platform APIs for managing accounts, entitlements, and services on SAP Business Technology Platform.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/package/SAPCloudPlatformCoreServices/overview
    baseUrl: https://accounts-service.cfapps.{region}.hana.ondemand.com
    tags:
      - BTP
      - Cloud Management
      - Cloud Platform
      - Platform Services
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/BTP
      - type: APIReference
        url: https://api.sap.com/package/SAPCloudPlatformCoreServices/rest
      - type: Hub
        url: https://api.sap.com/package/SAPCloudPlatformCoreServices/overview
      - type: GettingStarted
        url: https://help.sap.com/docs/btp/btp-developers-guide/apis
  - name: SAP Datasphere API
    description: APIs for data warehousing, catalog access, and consumption of analytical and relational models.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/package/sapdatasphere/overview
    baseUrl: https://{tenant}.{region}.hcs.cloud.sap
    tags:
      - Analytics
      - Data Integration
      - Data Warehousing
      - Datasphere
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_DATASPHERE
      - type: APIReference
        url: https://api.sap.com/package/sapdatasphere/odatav4
      - type: Hub
        url: https://api.sap.com/package/sapdatasphere/overview
      - type: APIReference
        url: https://api.sap.com/api/DatasphereCatalog/resource/
  - name: SAP Event Mesh API
    description: Messaging APIs for event-driven architecture supporting AMQP, MQTT, and REST protocols.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/event-mesh
    baseUrl: https://enterprise-messaging-pubsub.cfapps.{region}.hana.ondemand.com
    tags:
      - AMQP
      - Event-Driven
      - Messaging
      - MQTT
    properties:
      - type: AsyncAPI
        url: asyncapi/sap-event-mesh-asyncapi.yml
      - type: Documentation
        url: https://help.sap.com/docs/event-mesh
      - type: APIReference
        url: https://help.sap.com/docs/event-mesh/event-mesh/rest-apis-for-messaging
      - type: Hub
        url: https://api.sap.com/package/SAPEventMeshDefaultPlan/rest
      - type: GettingStarted
        url: https://help.sap.com/docs/event-mesh/event-mesh/what-is-sap-event-mesh
  - name: SAP Master Data Integration API
    description: APIs for centralizing and harmonizing master data across SAP and third-party applications.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://api.sap.com/package/sap-mdi-masterDataIntegration/overview
    baseUrl: https://{tenant}.integrationsuite.{region}.hana.ondemand.com
    tags:
      - Data Integration
      - Data Quality
      - Master Data
      - MDI
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION
      - type: APIReference
        url: https://api.sap.com/package/sap-mdi-masterDataIntegration
      - type: Hub
        url: https://api.sap.com/package/sap-mdi-masterDataIntegration/overview
      - type: APIReference
        url: https://api.sap.com/api/masterdata/resource
  - name: SAP Signavio Process Manager API
    description: APIs for process modeling, BPMN diagram management, and process governance automation.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/signavio-process-manager/sap-signavio-process-manager-api/sap-signavio-process-manager-api-guide
    baseUrl: https://editor.signavio.com/p
    tags:
      - BPM
      - BPMN
      - Process Management
      - Process Mining
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/signavio-process-manager/sap-signavio-process-manager-api/sap-signavio-process-manager-api-guide
      - type: APIReference
        url: https://help.sap.com/docs/signavio-process-insights/api-reference/getting-started-with-apis
      - type: APIReference
        url: https://help.sap.com/docs/signavio-process-governance/developer-guide/public-api
  - name: SAP Document Management Service API
    description: CMIS-based APIs for document management including versioning, access control, and content storage on BTP.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/document-management-service
    baseUrl: https://{tenant}.document-center.cfapps.{region}.hana.ondemand.com
    tags:
      - BTP
      - CMIS
      - Content Management
      - Document Management
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/document-management-service
      - type: Hub
        url: https://api.sap.com/package/SAPDocumentManagementServiceIntegrationOptionCMISAPI/rest
      - type: GettingStarted
        url: https://help.sap.com/docs/document-management-service/sap-document-management-service/access-document-management-service-application-option-repository-using-api
  - name: SAP Integration Suite API Management
    description: APIs for building, managing, publishing, and monitoring API proxies within SAP Integration Suite.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/sap-api-management
    baseUrl: https://{tenant}.{region}.apimanagement.hana.ondemand.com
    tags:
      - API Gateway
      - API Management
      - API Proxy
      - Integration Suite
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-documentation
      - type: Hub
        url: https://api.sap.com/package/APIMgmt/overview
      - type: GettingStarted
        url: https://developers.sap.com/group.cp-apim-code-1.html
      - type: DeveloperPortal
        url: https://api.sap.com/api/APIPortal_Developer_CF/overview
  - name: SAP AI Core API
    description: APIs for deploying, managing, and consuming AI models and workflows on SAP Business Technology Platform. Provides endpoints for scenario management, execution orchestration, and model serving.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/about-ai-api
    baseUrl: https://api.ai.{region}.cfapps.{landscape}.hana.ondemand.com/v2
    tags:
      - AI Core
      - Artificial Intelligence
      - BTP
      - Machine Learning
    properties:
      - type: OpenAPI
        url: openapi/sap-ai-core-openapi.yml
      - type: Documentation
        url: https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/about-ai-api
      - type: APIReference
        url: https://api.sap.com/api/AI_CORE_API/resource
      - type: Hub
        url: https://api.sap.com/api/AI_CORE_API/overview
      - type: SDK
        url: https://sap.github.io/ai-sdk/docs/js/ai-core/ai-api
  - name: SAP Emarsys Customer Engagement API
    description: REST APIs for marketing automation, customer engagement, and personalized campaign management across email, web, SMS, and mobile channels.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://dev.emarsys.com/
    baseUrl: https://api.emarsys.net/api/v2
    tags:
      - CRM
      - Customer Engagement
      - Email Marketing
      - Marketing Automation
    properties:
      - type: Documentation
        url: https://dev.emarsys.com/
      - type: APIReference
        url: https://help.sap.com/docs/SAP_EMARSYS_CUSTOMER_ENGAGEMENT/f8e2fafeea804018a954a8857d9dfff3/fdf6023c74c11014b724bbfdb6028c98.html
      - type: Hub
        url: https://api.sap.com/package/SAPEmarsysCustomerEngagement/overview
  - name: SAP Build Work Zone API
    description: APIs for managing digital workplace experiences, integrating business applications into unified workpages, and administering work zone sites and content.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanUrl: https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition/api-documentation
    baseUrl: https://{tenant}.dt.workzone.cfapps.{region}.hana.ondemand.com
    tags:
      - BTP
      - Digital Workplace
      - Portal
      - Work Zone
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition/api-documentation
include:
  - name: SAP API Business Hub
    url: https://api.sap.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AI
  - BTP
  - Business Applications
  - Cloud
  - Data Management
  - Enterprise
  - ERP
  - Integration
common:
  - type: DeveloperPortal
    url: https://developers.sap.com/
  - type: Hub
    url: https://api.sap.com
  - type: Blog
    url: https://community.sap.com/t5/all-sap-community-blogs/ct-p/all-blogs
  - type: Support
    url: https://community.sap.com/
  - type: GitHubOrganization
    url: https://github.com/SAP
  - type: StatusPage
    url: https://www.sap.com/about/trust-center/cloud-service-status.html
  - type: Support
    url: https://support.sap.com/
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: TermsOfService
    url: https://www.sap.com/about/legal/terms-of-use.html
  - type: GettingStarted
    url: https://developers.sap.com/tutorial-navigator.html
  - type: Training
    url: https://learning.sap.com/
  - type: Portal
    url: https://www.sap.com
  - type: SignUp
    url: https://developers.sap.com/tutorials/hcp-create-trial-account.html
  - type: Login
    url: https://accounts.sap.com
  - type: SDK
    url: https://developers.sap.com/topics/cloud-sdk.html
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/sap
  - type: YouTube
    url: https://www.youtube.com/@SAPTechnology
  - type: ChangeLog
    url: https://help.sap.com/whats-new/
  - type: Features
    data:
      - ERP and business suite APIs for finance, HR, procurement, and supply chain
      - AI/ML model deployment and serving via AI Core on BTP
      - Master data management and integration across SAP and third-party systems
      - Event-driven architecture with AMQP, MQTT, and REST messaging
      - OData-compatible endpoints for business object CRUD operations
  - type: UseCases
    data:
      - Automating order-to-cash and procure-to-pay business processes
      - Deploying and serving AI models for intelligent enterprise workflows
      - Integrating SAP ERP with third-party CRM, e-commerce, and analytics platforms
      - Managing business partner master data across multi-system landscapes
      - Building digital workplace experiences with unified work zone portals
  - type: Integrations
    data:
      - SAP S/4HANA Cloud with CRM and e-commerce platforms
      - SAP AI Core with machine learning frameworks and model registries
      - SAP Integration Suite with middleware and iPaaS connectors
      - SAP SuccessFactors with HR and talent management systems
      - SAP Event Mesh with event-driven microservices architectures
  - type: JSONLD
    url: json-ld/sap-context.jsonld
  - type: JSONSchema
    url: json-schema/sap-business-partner-schema.json
  - type: JSONSchema
    url: json-schema/sap-sales-order-schema.json
  - type: Rules
    url: rules/sap-spectral-rules.yml
  - type: Capabilities
    url: capabilities/shared/ai-core.yaml
  - type: Capabilities
    url: capabilities/shared/business-one.yaml
  - type: Capabilities
    url: capabilities/shared/s4hana-business-partner.yaml
  - type: Capabilities
    url: capabilities/enterprise-business-operations.yaml
---
