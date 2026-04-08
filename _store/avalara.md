---
aid: avalara
url: https://raw.githubusercontent.com/api-evangelist/avalara/refs/heads/main/apis.yml
apis:
- aid: avalara:avalara
  name: Avalara
  tags:
  - Taxes
  humanURL: ' https://developer.avalara.com/'
  properties:
  - url: ' https://developer.avalara.com/'
    type: Documentation
  description: Automate compliance with Avalara MCP servers for AI-driven tax workflows and APIs. Have your agent call our agent.
- aid: avalara:avatax-apis
  name: AvaTax APIs
  tags:
  - Sales Tax
  - Taxes
  - VAT
  humanURL: https://developer.avalara.com/api-reference/avatax/rest/v2/
  description: The AvaTax API is a set of application programming interfaces provided by Avalara that allows businesses to integrate automated, real-time sales and use tax, VAT, and GST calculations directly into their own software applications. This allows for seamless and accurate tax compliance for every transaction, regardless of jurisdiction or product type.
  properties:
  - url: https://developer.avalara.com/api-reference/avatax/rest/v2/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-avatax-rest-openapi.yml
- aid: avalara:avatax-soap-api
  name: AvaTax SOAP API
  tags:
  - SOAP
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/avatax/soap/
  description: The AvaTax SOAP API exposes the most commonly used features for interacting with the AvaTax service, allowing calculation of tax, modification of documents, and validation of addresses.
  properties:
  - url: https://developer.avalara.com/api-reference/avatax/soap/
    type: Documentation
- aid: avalara:communications-api
  name: Communications Tax API
  tags:
  - Communications
  - Taxes
  - Telecom
  humanURL: https://developer.avalara.com/api-reference/communications/v2/
  description: The Avalara Communications Tax API (SaasPro) provides communications tax calculations using information provided by jurisdiction codes, enabling tax calculations on invoices and line items, jurisdiction determination via geocoding, and profile customization.
  properties:
  - url: https://developer.avalara.com/api-reference/communications/v2/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-communications-openapi.yml
- aid: avalara:excise-tax-api
  name: Excise Platform API
  tags:
  - Excise
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/excise/v1/
  description: The Excise Platform API provides an external programmatic interface for the Avalara Excise application, enabling excise tax calculation and management, business entity imports, location management, and other tax compliance operations through REST API endpoints.
  properties:
  - url: https://developer.avalara.com/api-reference/excise/v1/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-excise-openapi.yml
- aid: avalara:item-classification-api
  name: Item Classification API
  tags:
  - Classification
  - HS Codes
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/item-classification/v2/
  description: The Avalara Item Classification API allows users subscribed to the Item Classification service to submit products for classification and retrieve the corresponding HS Codes, with support for storage and non-storage subscription models.
  properties:
  - url: https://developer.avalara.com/api-reference/item-classification/v2/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-item-classification-openapi.yml
- aid: avalara:tax-content-for-retail-api
  name: Avalara Tax Content for Retail Configuration API
  tags:
  - Point of Sale
  - Retail
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/cgpos/cfg/
  description: The Avalara Tax Content for Retail Configuration API automates tax content delivery for brick-and-mortar businesses, enabling management of configurations, communications, jobs, onboarding, and user roles for point-of-sale tax content.
  properties:
  - url: https://developer.avalara.com/api-reference/cgpos/cfg/
    type: Documentation
- aid: avalara:avatax-brazil-api
  name: AvaTax Brazil API
  tags:
  - Brazil
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/avatax-brazil/v1/
  description: The AvaTax Brazil API exposes the most commonly used services for interacting with AvaTax-Brazil, allowing calculation of taxes, issuing electronic invoice documents, and modifying existing transactions when allowed by tax authorities for businesses with a physical presence in Brazil.
  properties:
  - url: https://developer.avalara.com/api-reference/avatax-brazil/v1/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-avatax-brazil-openapi.yml
- aid: avalara:vat-reporting-api
  name: VAT Reporting API
  tags:
  - Reporting
  - Taxes
  - VAT
  humanURL: https://developer.avalara.com/api-reference/vat-reporting/v1/
  description: The Avalara VAT Reporting API orchestrates end-to-end VAT compliance workflows including onboarding, file ingress, error handling, filing of VAT Returns, EC Listings, Intrastat, and transaction reporting across multiple jurisdictions.
  properties:
  - url: https://developer.avalara.com/api-reference/vat-reporting/v1/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-vat-reporting-openapi.yml
- aid: avalara:mylodgetax-api
  name: MyLodgeTax API
  tags:
  - Lodging
  - Short-Term Rental
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/myLodgeAPI/tax/
  description: The MyLodgeTax API provides sales and lodging tax compliance for short-term property rentals, offering partners access to summarized tax responsibilities for property owners by marketplace including direct listings and marketplace bookings.
  properties:
  - url: https://developer.avalara.com/api-reference/myLodgeAPI/tax/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-mylodgetax-openapi.yml
- aid: avalara:certcapture-api
  name: CertCapture API
  tags:
  - Certificates
  - Exemptions
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/CertCapture/v2/
  description: The Avalara CertCapture RESTful API provides document management for tax-exempt sales, including managing certificates, attributes, custom fields, customers, authentication tokens, and eCommerce token generation for CertCapture 6.X and beyond.
  properties:
  - url: https://developer.avalara.com/api-reference/CertCapture/v2/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-certcapture-openapi.yml
- aid: avalara:e-invoicing-api
  name: E-Invoicing REST API
  tags:
  - Compliance
  - E-Invoicing
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/e-invoicing/v1.0
  description: The Avalara E-Invoicing REST API supports sending data within the Alpha scope for e-Invoicing compliance use cases, enabling technology partners to integrate e-invoicing workflows for cross-border and domestic compliance.
  properties:
  - url: https://developer.avalara.com/api-reference/e-invoicing/v1.0
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-e-invoicing-openapi.yml
- aid: avalara:activation-service-api
  name: Activation Service API
  tags:
  - Registration
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/activationService/activationService/
  description: The Avalara Activation Service API allows technology partners to retrieve the status of their registrations within the Avalara Compliance Cloud platform, providing endpoints for listing all registrations and retrieving individual registration details.
  properties:
  - url: https://developer.avalara.com/api-reference/activationService/activationService/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-activation-service-openapi.yml
- aid: avalara:business-api
  name: Avalara Business API
  tags:
  - Business
  - Orders
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/business/v1/
  description: The Avalara Business API provides public APIs for doing business with Avalara, including registering customer accounts and creating sales orders for Avalara services through partner integrations.
  properties:
  - url: https://developer.avalara.com/api-reference/business/v1/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-business-openapi.yml
- aid: avalara:portal-oauth-api
  name: Portal OAuth API
  tags:
  - Authentication
  - OAuth
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/oauth/oauth/
  description: The Avalara Portal OAuth API provides OAuth token generation and session management endpoints for implementing authentication in Avalara platform integrations, supporting credential-based authentication and SAML assertions.
  properties:
  - url: https://developer.avalara.com/api-reference/oauth/oauth/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-portal-oauth-openapi.yml
- aid: avalara:shared-company-service-api
  name: Shared Company Service API
  tags:
  - Company Management
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/sharedservice/sharedCompanyService/
  description: The Avalara Shared Company Service API provides scalable APIs for managing canonical company and contact information across Avalara products, enabling creation, retrieval, update, and deletion of company records.
  properties:
  - url: https://developer.avalara.com/api-reference/sharedservice/sharedCompanyService/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-shared-company-service-openapi.yml
- aid: avalara:hs-code-classification-api
  name: Automated Tariff Code Classification API
  tags:
  - Classification
  - HS Codes
  - Tariff
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/hscodeclassification/hscodeclassification/
  description: The Avalara HSCode and AvataxCode Classification API classifies products into Harmonized System Codes (HS Codes) and Avalara Tax Codes, providing tariff code predictions based on product information and destination country with confidence levels.
  properties:
  - url: https://developer.avalara.com/api-reference/hscodeclassification/hscodeclassification/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-hs-code-classification-openapi.yml
- aid: avalara:self-serve-tariff-classification-api
  name: Self-Serve Tariff Classification API
  tags:
  - Cross-Border
  - Tariff
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/selfservicetarrifclassification/selfservicetarrifclassification/
  description: The Avalara Cross Border Tariff Content API classifies products based on provided product information for the specified country of destination, supporting interactive classification dialogues, trade data access, certificate generation, and data downloads.
  properties:
  - url: https://developer.avalara.com/api-reference/selfservicetarrifclassification/selfservicetarrifclassification/
    type: Documentation
- aid: avalara:1099-w9-api
  name: 1099 & W-9 API
  tags:
  - Tax Forms
  - Taxes
  - W-9
  humanURL: https://developer.avalara.com/api-reference/avalara1099/avalara1099/
  description: The Avalara 1099 and W-9 API automates collection, validation, and e-filing of IRS forms including 1099 variants, 1095 forms, W-2, and 1042-S, providing endpoints for creating, updating, and managing various IRS forms for US and foreign companies.
  properties:
  - url: https://developer.avalara.com/api-reference/avalara1099/avalara1099/
    type: Documentation
  - type: OpenAPI
    url: openapi/avalara-1099-w9-openapi.yml
- aid: avalara:license-guidance-order-api
  name: License Guidance Order API
  tags:
  - Licensing
  - Registration
  - Taxes
  humanURL: https://developer.avalara.com/api-reference/registration-and-licensing/license-guidance-order/license-guidance-order/
  description: The Avalara License Guidance Order API enables placing Avalara License Guidance orders and populating questionnaire responses with known business information, returning order confirmation details including unique order URLs and numbers.
  properties:
  - url: https://developer.avalara.com/api-reference/registration-and-licensing/license-guidance-order/license-guidance-order/
    type: Documentation
name: Avalara
tags:
- Taxes
type: Index
image: https://www.avalara.com/us/en/about/newsroom/media-kit/_jcr_content/root/responsivegrid/responsivegrid/columncontrol/par2/image.coreimg.svg/1614712826993/avalara-logo.svg
access: 3rd-Party
common:
- url: https://developer.avalara.com/sdk/
  name: AvaTax Software Development Kit | Avalara Developer
  type: SDKs
  description: The Avalara unified SDK provides a set of SDKs that cover multiple Avalara APIs. A unified SDK allows partners & customer developers to download one SDK and easily add on additional Avalara features and services.
- url: https://developer.avalara.com/developer-community/
  name: Avalara Developer Communities | Avalara Developer
  type: Community
  description: Become a part of the growing developer community building on the Avalara developer platform where you can get help, provide feedback, brainstorm ideas, make connections, and get inspired.
- url: https://developer.avalara.com/blogs/
  name: Developer Blog | Avalara Developer
  type: Blog
  description: 'null'
- url: https://developer.avalara.com/resources/support/
  name: AvaTax API Support | Avalara Developer
  type: Support
  description: 'null'
- url: https://knowledge.avalara.com/bundle/xti1670300535545/page/contact_avalara_support.html
  name: Contact Avalara Support
  type: Contact
  description: 'null'
- url: https://developercommunity.avalara.com/s/
  name: Avalara Developer Community
  type: AskQuestions
  description: 'null'
- url: https://developer.avalara.com/certification/avatax/
  name: Avalara Certification | Avalara Developer
  type: Certifications
  description: 'null'
- url: https://www.avalara.com/us/en/learn/webinars.html#developerwebinars
  name: Sales & Use Tax Compliance Webinars - Avalara
  type: Webinars
  description: 'null'
- url: https://training.avalara.com/pages/product-training
  name: Avalara University
  type: Learning
  description: 'null'
- url: https://developer.avalara.com/elr-usecases/
  name: E-Invoicing Mandate Definitions | Avalara Developer
  type: Schema
  description: 'null'
- url: https://developer.avalara.com/
  name: Avalara Developer
  type: Portal
  description: 'null'
- url: https://developer.avalara.com/api-reference/
  name: Avalara APIs | Avalara Developer
  type: Explorer
  description: 'null'
- url: https://developer.avalara.com/mcp-servers/
  name: MCP Servers | Avalara Developer
  type: MCPServers
  description: Avalara Model Context Protocol (MCP) servers connect AI applications with Avalaras tax compliance systems in a standardized way. MCP servers allow partners and developers to integrate AI-driven tax workflows, automate cross-border compliance, and access Avalaras regularly updated tax content.
- url: https://developer.avalara.com/freeTrial/
  name: Start Your 90-Day AvaTax Free Trial | Avalara Developer
  type: Trial
  description: 'null'
- url: https://developer.avalara.com/documentation/
  name: Tax API Integration Guide | Avalara Developer
  type: Guide
  description: 'null'
- url: https://www.avalara.com/us/en/products/integrations-browse-all.html
  name: Search or Browse all Avalara Partner Integrations
  type: Integrations
  description: 'null'
- url: https://legal.avalara.com/#siteterms
  name: Avalara Legal Center
  type: TermsOfService
  description: 'null'
- url: https://legal.avalara.com/dpa#privacynotice
  name: Avalara Legal Center
  type: PrivacyPolicy
  description: 'null'
- url: https://www.avalara.com/us/en/about/customer-stories.html
  name: Customer Stories & Testimonials - Avalara
  type: Customers
  description: 'null'
- url: https://careers.avalara.com/north-america
  name: Avalara North America
  type: Careers
  description: 'null'
- url: https://www.avalara.com/us/en/partners/partner-programs.html
  name: Partners
  type: Partners
  description: 'null'
- url: https://newsroom.avalara.com/
  name: Avalara - Newsroom
  type: Newsroom
  description: Newsroom
- url: https://www.avalara.com/us/en/learn/whitepapers.html
  name: Sales & Use Tax Whitepapers - Avalara
  type: WhitePapers
  description: 'null'
- url: https://www.avalara.com/us/en/learn/events.html
  name: Learning and Training Events - Avalara
  type: Events
  description: 'null'
- url: https://training.avalara.com/pages/product-training
  name: Avalara University
  type: Training
  description: 'null'
- url: https://www.avalara.com/us/en/signin.html
  name: Avalara Login - Product Login for Free & Paid Services
  type: Login
  description: 'null'
- url: https://developer.avalara.com/api-reference/
  name: Avalara APIs | Avalara Developer
  type: Documentation
  description: 'null'
- url: https://developer.avalara.com/patch-notes/
  name: Patch Notes | Avalara Developer
  type: ChangeLog
  description: 'null'
- url: https://developer.avalara.com/api-versioning/
  name: Avalara API Versioning | Avalara Developer
  type: Versioning
  description: 'null'
- url: https://buy.avalara.com/
  name: Buy | Avalara
  type: SignUp
  description: 'null'
- url: https://legal.avalara.com/compliance?_gl=1*1hevp4p*_gcl_au*MTM1NDY3OTg2MC4xNzYzNjY2Njc5LjEzNjM2NTU5NjEuMTc2MzY2ODQ1OC4xNzYzNjY4NzA3
  name: Avalara Legal Center
  type: Compliance
  description: 'null'
- url: https://www.linkedin.com/company/avalara/
  name: LinkedIn
  type: LinkedIn
- url: https://www.youtube.com/c/Avalara
  name: YouTube
  type: YouTube
- url: https://www.postman.com/api-evangelist/avalara/overview
  name: Postman Workspace
  type: PostmanWorkspace
- url: https://github.com/Avalara
  name: GitHub Organization
  type: GitHubOrganization
- url: https://github.com/Avalara/Swagger
  name: Swagger
  type: Swagger
created: '2025-11-19'
modified: '2026-04-07'
position: Consumer
description: Avalara helps businesses of all sizes get tax compliance right. We deliver cloud-based solutions that work with existing business applications to calculate tax accurately and file returns automatically.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

