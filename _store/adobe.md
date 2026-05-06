---
aid: adobe
url: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/apis.yml
name: Adobe
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Creative Cloud
  - Digital Asset Management
  - Document Services
  - E-Commerce
  - E-Signatures
  - Experience Cloud
  - Generative AI
  - Marketing
  - PDF
  - Work Management
description: Adobe provides APIs and developer resources for its creative, document, and experience cloud platforms. Developers can integrate with PDF services, Creative Cloud, generative AI (Firefly), analytics, e-commerce, e-signatures, and many other Adobe products and services.
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: adobe:adobe-pdf-services-api
    name: Adobe PDF Services API
    tags:
      - Conversion
      - Documents
      - PDF
    humanURL: https://developer.adobe.com/document-services/apis/pdf-services/
    baseURL: https://pdf-services.adobe.io
    properties:
      - type: Documentation
        url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/
      - type: GettingStarted
        url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/gettingstarted/
      - type: ChangeLog
        url: https://developer.adobe.com/document-services/docs/overview/releasenotes/
      - type: OpenAPI
        url: openapi/adobe-pdf-services-api-openapi.yml
      - type: JSONSchema
        url: json-schema/adobe-pdf-services-asset-upload-request-schema.json
      - type: JSONLD
        url: json-ld/adobe-pdf-services-context.jsonld
    description: Create, manipulate, and export PDF documents programmatically.
  - aid: adobe:adobe-pdf-extract-api
    name: Adobe PDF Extract API
    tags:
      - AI
      - Extraction
      - PDF
    humanURL: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/
    baseURL: https://pdf-services.adobe.io
    properties:
      - type: Documentation
        url: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/
      - type: GettingStarted
        url: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/gettingstarted/
    description: Extract text, images, tables, and more from native and scanned PDFs into structured JSON using AI technology.
  - aid: adobe:adobe-acrobat-sign-api
    name: Adobe Acrobat Sign API
    tags:
      - Documents
      - E-Signatures
    humanURL: https://developer.adobe.com/document-services/apis/sign-api/
    baseURL: https://api.adobesign.com
    properties:
      - type: Documentation
        url: https://opensource.adobe.com/acrobat-sign/developer_guide/index.html
      - type: APIReference
        url: https://opensource.adobe.com/acrobat-sign/developer_guide/apiusage.html
      - type: GettingStarted
        url: https://opensource.adobe.com/acrobat-sign/developer_guide/gstarted.html
      - type: SDK
        url: https://developer.adobe.com/acrobat-sign/docs/overview/sdks/rest
      - type: ChangeLog
        url: https://opensource.adobe.com/acrobat-sign/releasenotes/acrobatsignreleasenotes.html
    description: Embed e-signature workflows and manage signing agreements programmatically.
  - aid: adobe:adobe-analytics-api
    name: Adobe Analytics API
    tags:
      - Analytics
      - Metrics
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/
    baseURL: https://analytics.adobe.io
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/2.0/
      - type: Authentication
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
      - type: GettingStarted
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
    description: Access and analyze digital marketing data and metrics.
  - aid: adobe:adobe-firefly-api
    name: Adobe Firefly API
    tags:
      - Generative AI
      - Image Generation
    humanURL: https://developer.adobe.com/firefly-services/docs/firefly-api/
    baseURL: https://firefly-api.adobe.io
    properties:
      - type: Documentation
        url: https://developer.adobe.com/firefly-services/docs/firefly-api/
      - type: APIReference
        url: https://developer.adobe.com/firefly-services/docs/firefly-api/api/
      - type: GettingStarted
        url: https://developer.adobe.com/firefly-services/docs/firefly-api/guides/
      - type: SDK
        url: https://developer.adobe.com/firefly-services/docs/guides/sdks/
      - type: ChangeLog
        url: https://developer.adobe.com/firefly-services/docs/firefly-api/guides/changelog/
    description: Generate and edit images using generative AI models through a RESTful API.
  - aid: adobe:adobe-experience-platform-api
    name: Adobe Experience Platform API
    tags:
      - Customer Data
      - Experience Platform
    humanURL: https://developer.adobe.com/experience-platform-apis/
    baseURL: https://platform.adobe.io
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/docs/experience-platform/landing/platform-apis/api-guide.html
      - type: APIReference
        url: https://developer.adobe.com/experience-platform-apis/references/
      - type: GettingStarted
        url: https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-guide
    description: Build and manage customer experience applications on Adobe Experience Platform.
  - aid: adobe:adobe-stock-api
    name: Adobe Stock API
    tags:
      - Assets
      - Stock
    humanURL: https://developer.adobe.com/stock/
    baseURL: https://stock.adobe.io
    properties:
      - type: Documentation
        url: https://developer.adobe.com/stock/docs/getting-started/
      - type: APIReference
        url: https://developer.adobe.com/stock/docs/api/
      - type: GettingStarted
        url: https://developer.adobe.com/stock/docs/getting-started/
      - type: SDK
        url: https://github.com/adobe/stock-api-sdk
    description: Search, license, and manage Adobe Stock assets including photos, vectors, videos, and templates.
  - aid: adobe:adobe-commerce-api
    name: Adobe Commerce API
    tags:
      - E-Commerce
      - REST
    humanURL: https://developer.adobe.com/commerce/webapi/
    properties:
      - type: Documentation
        url: https://developer.adobe.com/commerce/docs/
      - type: APIReference
        url: https://developer.adobe.com/commerce/webapi/rest/reference/
      - type: GettingStarted
        url: https://developer.adobe.com/commerce/webapi/get-started/
      - type: Authentication
        url: https://developer.adobe.com/commerce/webapi/get-started/authentication/
    description: Build and integrate e-commerce applications with REST, GraphQL, and SOAP web APIs.
  - aid: adobe:adobe-marketo-engage-api
    name: Adobe Marketo Engage API
    tags:
      - Leads
      - Marketing Automation
    humanURL: https://developer.adobe.com/marketo-apis/
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api
      - type: APIReference
        url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/endpoint-reference
      - type: Authentication
        url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/authentication
      - type: GettingStarted
        url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api
    description: Automate marketing processes and manage leads, campaigns, and assets via REST APIs.
  - aid: adobe:adobe-workfront-api
    name: Adobe Workfront API
    tags:
      - Projects
      - Work Management
    humanURL: https://developer.adobe.com/workfront-apis/
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/workfront-api
      - type: APIReference
        url: https://developer.adobe.com/workfront/api-explorer/
      - type: GettingStarted
        url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-general-information/api-basics
    description: Manage work, projects, tasks, and resources programmatically with a REST API.
  - aid: adobe:adobe-user-management-api
    name: Adobe User Management API
    tags:
      - Identity
      - User Management
    humanURL: https://developer.adobe.com/umapi/
    baseURL: https://usermanagement.adobe.io
    properties:
      - type: Documentation
        url: https://adobe-apiplatform.github.io/umapi-documentation/
      - type: APIReference
        url: https://adobe-apiplatform.github.io/umapi-documentation/en/RefOverview.html
      - type: GettingStarted
        url: https://adobe-apiplatform.github.io/umapi-documentation/en/getstarted.html
    description: Programmatically manage users, groups, and product entitlements for Adobe enterprise organizations.
  - aid: adobe:adobe-io-events-api
    name: Adobe I/O Events API
    tags:
      - Events
      - Webhooks
    humanURL: https://developer.adobe.com/events/
    baseURL: https://platform.adobe.io
    properties:
      - type: Documentation
        url: https://developer.adobe.com/events/docs/
      - type: APIReference
        url: https://developer.adobe.com/events/docs/guides/api/
      - type: GettingStarted
        url: https://developer.adobe.com/events/docs/
    description: Subscribe to and receive near real-time events from Adobe services for event-driven integrations.
  - aid: adobe:adobe-experience-manager-api
    name: Adobe Experience Manager API
    tags:
      - Content Management
      - Digital Asset Management
    humanURL: https://developer.adobe.com/experience-cloud/experience-manager-apis
    baseURL: https://platform.adobe.io
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service
      - type: APIReference
        url: https://developer.adobe.com/experience-cloud/experience-manager-apis
      - type: GettingStarted
        url: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/reference-materials
    description: Create, read, update, and delete content, assets, and forms in Adobe Experience Manager as a Cloud Service.
common:
  - type: Portal
    url: https://developer.adobe.com/
  - type: Console
    url: https://developer.adobe.com/console/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
  - type: Support
    url: https://developer.adobe.com/developer-support/
  - type: StatusPage
    url: https://status.adobe.com/
  - type: Blog
    url: https://blog.developer.adobe.com/
  - type: TermsOfService
    url: https://www.adobe.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.adobe.com/privacy/policy.html
  - type: GettingStarted
    url: https://developer.adobe.com/developer-console/docs/guides/getting-started
  - type: GitHubOrganization
    url: https://github.com/AdobeDocs/
  - type: SDK
    url: https://developer.adobe.com/apis
  - type: SignUp
    url: https://developer.adobe.com/console/
  - type: Login
    url: https://developer.adobe.com/console/
  - type: OpenAPI
    url: openapi/adobe-pdf-services-api-openapi.yml
  - type: JSONSchema
    url: json-schema/adobe-pdf-services-asset-upload-request-schema.json
  - type: JSONLD
    url: json-ld/adobe-context.jsonld
  - type: SpectralRules
    url: rules/adobe-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/adobe-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/document-processing.yaml
  - type: Features
    data:
      - PDF creation, conversion, and manipulation via REST API
      - AI-powered PDF content extraction into structured JSON
      - Generative AI image creation and editing with Firefly
      - E-signature workflows with Acrobat Sign
      - Digital analytics and marketing insights
      - Customer data platform with Experience Platform
      - Content management with Experience Manager
      - Marketing automation with Marketo Engage
      - E-commerce platform with Adobe Commerce
      - Work management and project tracking with Workfront
      - Event-driven integrations with I/O Events
      - Stock asset search and licensing
  - type: UseCases
    data:
      - Automating document workflows with PDF Services API
      - Extracting data from invoices and forms with PDF Extract
      - Generating creative assets at scale with Firefly API
      - Embedding e-signature capabilities into business applications
      - Building personalized customer experiences with Experience Platform
      - Automating marketing campaigns and lead management
      - Managing digital content and assets across channels
      - Building and managing e-commerce storefronts
  - type: Integrations
    data:
      - Microsoft 365 and Teams integration
      - Salesforce CRM integration
      - Adobe Creative Cloud libraries
      - Workfront and Jira project management
      - SAP and Oracle ERP systems
      - Shopify and Magento marketplaces
      - Google Analytics and Tag Manager
      - Slack and Microsoft Teams notifications
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
