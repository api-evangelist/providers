---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Amazon Agentic Access
  operation_count: 42
  slug: amazon-agentic-access
  summary_line: 42 operations · 20 acting
api_count: 18
apis:
- description: The Amazon Creators API provides programmatic access to Amazon product data for publishers, influencers, and affiliate partners. It is the recommended replacement for the Product Advertising API and r
  name: Amazon Creators API
  slug: creators-api
- description: The Alexa Skills Kit (ASK) REST APIs enable developers to create, manage, test, and deploy custom voice skills for Alexa-enabled devices including skill manifest management, interaction model building
  name: Amazon Alexa Skills Kit API
  slug: alexa-skills-kit-api
- description: The Amazon Appstore Developer APIs provide tools for managing app submissions, testing, and monetization through in-app purchases on the Amazon Appstore for Android and Fire OS applications.
  name: Amazon Appstore API
  slug: appstore-api
- description: Ad group management operations
  name: Amazon Ad Groups API
  slug: amazon-ad-groups-api
- description: Campaign management operations
  name: Amazon Campaigns API
  slug: amazon-campaigns-api
- description: Search and retrieve catalog item information
  name: Amazon Catalog API
  slug: amazon-catalog-api
- description: Manage buyer charge authorizations
  name: Amazon Charge Permissions API
  slug: amazon-charge-permissions-api
- description: Create and manage payment charges
  name: Amazon Charges API
  slug: amazon-charges-api
- description: Manage buyer checkout sessions
  name: Amazon Checkout Sessions API
  slug: amazon-checkout-sessions-api
- description: Retrieve financial transaction data
  name: Amazon Finances API
  slug: amazon-finances-api
- description: Manage FBA inventory
  name: Amazon Inventory API
  slug: amazon-inventory-api
- description: Keyword management operations
  name: Amazon Keywords API
  slug: amazon-keywords-api
- description: Create, update, and manage product listings
  name: Amazon Listings API
  slug: amazon-listings-api
- description: Manage and retrieve order information
  name: Amazon Orders API
  slug: amazon-orders-api
- description: Account profile management
  name: Amazon Profiles API
  slug: amazon-profiles-api
- description: Process refunds on captured charges
  name: Amazon Refunds API
  slug: amazon-refunds-api
- description: Reporting and analytics
  name: Amazon Reports API
  slug: amazon-reports-api
- description: Product targeting operations
  name: Amazon Targets API
  slug: amazon-targets-api
artifact_total: 250
collections:
- collection_type: postman
  name: Amazon Advertising Ad Groups API
  slug: postman-amazon-ad-groups-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Campaigns API
  slug: postman-amazon-campaigns-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Catalog API
  slug: postman-amazon-catalog-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Charge Permissions API
  slug: postman-amazon-charge-permissions-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Charges API
  slug: postman-amazon-charges-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Checkout Sessions API
  slug: postman-amazon-checkout-sessions-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Finances API
  slug: postman-amazon-finances-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Inventory API
  slug: postman-amazon-inventory-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Keywords API
  slug: postman-amazon-keywords-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Listings API
  slug: postman-amazon-listings-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Orders API
  slug: postman-amazon-orders-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Profiles API
  slug: postman-amazon-profiles-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Refunds API
  slug: postman-amazon-refunds-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Reports API
  slug: postman-amazon-reports-api
- collection_type: postman
  name: Amazon Advertising Ad Groups Targets API
  slug: postman-amazon-targets-api
- collection_type: open
  name: Amazon Advertising API
  slug: open-amazon-advertising-api
- collection_type: open
  name: Amazon Pay API
  slug: open-amazon-pay-api
- collection_type: open
  name: Amazon Selling Partner API
  slug: open-amazon-selling-partner-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amazon
- group: start
  title: ''
  type: Portal
  url: https://developer.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://www.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.amazon.com/docs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/support/legal/da
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amazon.com/gp/help/customer/display.html?nodeId=468496
- group: operate
  title: ''
  type: Support
  url: https://developer.amazon.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amzn
- group: start
  title: ''
  type: Console
  url: https://developer.amazon.com/dashboard
- group: start
  title: ''
  type: Signup
  url: https://www.amazon.com/ap/register?openid.assoc_handle=aws
- group: start
  title: ''
  type: Login
  url: https://developer.amazon.com/login
- group: company
  title: ''
  type: Blog
  url: https://developer.amazon.com/blogs/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/AmazonDeveloper
- group: operate
  title: ''
  type: Contact
  url: https://www.amazon.com/gp/help/customer/contact-us
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.amazon.com/llms.txt
created: '2024-01-15'
description: Amazon is a global technology and e-commerce company offering a wide range of consumer and developer APIs including the Selling Partner API for marketplace sellers, Advertising API for campaign management, Amazon Pay for payments, Alexa Skills Kit for voice experiences, Amazon Appstore for mobile applications, and the Creators API for affiliate publishers. These APIs power Amazon's ecosystem of sellers, developers, advertisers, and content creators.
examples:
- key_count: 5
  name: Advertising Ad Group Example
  slug: advertising-ad-group-example
- key_count: 3
  name: Advertising Ad Group Response Example
  slug: advertising-ad-group-response-example
- key_count: 8
  name: Advertising Campaign Example
  slug: advertising-campaign-example
- key_count: 3
  name: Advertising Campaign Response Example
  slug: advertising-campaign-response-example
- key_count: 4
  name: Advertising Create Ad Group Request Example
  slug: advertising-create-ad-group-request-example
- key_count: 6
  name: Advertising Create Campaign Request Example
  slug: advertising-create-campaign-request-example
- key_count: 6
  name: Advertising Create Keyword Request Example
  slug: advertising-create-keyword-request-example
- key_count: 6
  name: Advertising Create Target Request Example
  slug: advertising-create-target-request-example
- key_count: 7
  name: Advertising Keyword Example
  slug: advertising-keyword-example
- key_count: 3
  name: Advertising Keyword Response Example
  slug: advertising-keyword-response-example
- key_count: 4
  name: Advertising Profile Example
  slug: advertising-profile-example
- key_count: 3
  name: Advertising Report Request Example
  slug: advertising-report-request-example
- key_count: 2
  name: Advertising Report Request Response Example
  slug: advertising-report-request-response-example
- key_count: 4
  name: Advertising Report Status Example
  slug: advertising-report-status-example
- key_count: 7
  name: Advertising Target Example
  slug: advertising-target-example
- key_count: 3
  name: Advertising Target Response Example
  slug: advertising-target-response-example
- key_count: 4
  name: Advertising Update Campaign Request Example
  slug: advertising-update-campaign-request-example
- key_count: 9
  name: Pay Address Example
  slug: pay-address-example
- key_count: 3
  name: Pay Buyer Example
  slug: pay-buyer-example
- key_count: 9
  name: Pay Charge Example
  slug: pay-charge-example
- key_count: 9
  name: Pay Charge Permission Example
  slug: pay-charge-permission-example
- key_count: 11
  name: Pay Checkout Session Example
  slug: pay-checkout-session-example
- key_count: 5
  name: Pay Create Charge Request Example
  slug: pay-create-charge-request-example
- key_count: 5
  name: Pay Create Checkout Session Request Example
  slug: pay-create-checkout-session-request-example
- key_count: 3
  name: Pay Create Refund Request Example
  slug: pay-create-refund-request-example
- key_count: 3
  name: Pay Merchant Metadata Example
  slug: pay-merchant-metadata-example
- key_count: 2
  name: Pay Price Example
  slug: pay-price-example
- key_count: 6
  name: Pay Refund Example
  slug: pay-refund-example
- key_count: 3
  name: Pay Status Details Example
  slug: pay-status-details-example
- key_count: 3
  name: Pay Update Checkout Session Request Example
  slug: pay-update-checkout-session-request-example
- key_count: 4
  name: Selling Partner Catalog Item Example
  slug: selling-partner-catalog-item-example
- key_count: 3
  name: Selling Partner Catalog Item List Example
  slug: selling-partner-catalog-item-list-example
- key_count: 1
  name: Selling Partner Create Report Response Example
  slug: selling-partner-create-report-response-example
- key_count: 4
  name: Selling Partner Create Report Specification Example
  slug: selling-partner-create-report-specification-example
- key_count: 1
  name: Selling Partner Error List Example
  slug: selling-partner-error-list-example
- key_count: 2
  name: Selling Partner Inventory Summaries Example
  slug: selling-partner-inventory-summaries-example
- key_count: 5
  name: Selling Partner Listings Item Example
  slug: selling-partner-listings-item-example
- key_count: 2
  name: Selling Partner Listings Item Patch Request Example
  slug: selling-partner-listings-item-patch-request-example
- key_count: 2
  name: Selling Partner Listings Item Put Request Example
  slug: selling-partner-listings-item-put-request-example
- key_count: 4
  name: Selling Partner Listings Item Submission Response Example
  slug: selling-partner-listings-item-submission-response-example
- key_count: 2
  name: Selling Partner Money Example
  slug: selling-partner-money-example
- key_count: 10
  name: Selling Partner Order Example
  slug: selling-partner-order-example
- key_count: 7
  name: Selling Partner Order Item Example
  slug: selling-partner-order-item-example
- key_count: 1
  name: Selling Partner Order Item List Example
  slug: selling-partner-order-item-list-example
- key_count: 1
  name: Selling Partner Order List Example
  slug: selling-partner-order-list-example
- key_count: 2
  name: Selling Partner Pagination Example
  slug: selling-partner-pagination-example
- key_count: 2
  name: Selling Partner Report Document Example
  slug: selling-partner-report-document-example
- key_count: 5
  name: Selling Partner Report Example
  slug: selling-partner-report-example
- key_count: 2
  name: Selling Partner Report List Example
  slug: selling-partner-report-list-example
- key_count: 2
  name: Selling Partner Transaction List Example
  slug: selling-partner-transaction-list-example
features:
- 'Amazon (Web Services + Marketplace + Ads): hundreds of services across Cloud + Commerce'
- 'Detailed pricing: see https://aws.amazon.com/pricing/'
- 'Service: EC2 (compute)'
- 'Service: S3 (object storage)'
- 'Service: EBS (block storage)'
- 'Service: RDS (managed SQL)'
- 'Service: DynamoDB (NoSQL)'
- 'Service: Lambda (serverless)'
- 'Service: API Gateway'
- 'Service: CloudFront (CDN)'
- 'Service: Route 53 (DNS)'
- 'Service: VPC (networking)'
- 'Service: IAM (identity)'
- 'Service: KMS (encryption)'
- 'Service: Secrets Manager'
- 'Service: CloudWatch (monitoring)'
- 'Service: EKS (Kubernetes)'
- 'Service: ECS (containers)'
- 'Service: ECR (container registry)'
- 'Service: SQS (queue)'
- 'Service: SNS (pub-sub)'
- 'Service: SES (email)'
- 'Service: Bedrock (AI/ML)'
- 'Service: SageMaker (ML)'
- 'Service: Comprehend (NLP)'
- 'Service: Rekognition (vision)'
- 'Service: Polly (TTS)'
- 'Service: Transcribe (STT)'
- 'Service: Translate'
- 'Service: Athena (SQL on S3)'
- 'Service: Redshift (data warehouse)'
- 'Service: Glue (ETL)'
- 'Service: EMR (Hadoop)'
- 'Service: Kinesis (streaming)'
- 'Service: MSK (managed Kafka)'
- 'Service: OpenSearch'
- 'Service: QuickSight (BI)'
- 'Service: Amazon Advertising API'
- 'Service: Amazon Marketplace API'
- 'Service: Amazon SP API'
- 'Service: Amazon Pay'
- 'Service: Amazon Music API'
- 'Service: Amazon Drive (deprecated)'
finops:
- name: Amazon Finops
  service_category: Cloud + Commerce
  slug: amazon-finops
graphqls:
- description: This conceptual GraphQL schema models the Amazon Selling Partner API (SP-API) surface.
  name: Amazon Selling Partner API - GraphQL Schema
  slug: amazon-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon.png
integrations:
- description: SP-API is the modern replacement for the deprecated Amazon Marketplace Web Service (MWS) for all seller operations.
  name: Amazon MWS Legacy Migration
- description: Integrate smart home devices and services with Alexa voice control using the Smart Home Skill API.
  name: Alexa Smart Home
- description: OAuth 2.0 authentication for all Amazon developer APIs including SP-API, Advertising API, and ASK via Login with Amazon (LWA).
  name: Login with Amazon
- description: Affiliate program integration for the Creators API and Product Advertising API for commission-based product promotion.
  name: Amazon Associates Program
- description: Amazon Appstore SDK for Fire OS and Android apps with in-app purchasing and device targeting capabilities.
  name: Fire OS and Android
json_schemas:
- name: AdGroupResponse
  property_count: 3
  slug: advertising-ad-group-response
- name: AdGroup
  property_count: 5
  slug: advertising-ad-group
- name: CampaignResponse
  property_count: 3
  slug: advertising-campaign-response
- name: Campaign
  property_count: 8
  slug: advertising-campaign
- name: CreateAdGroupRequest
  property_count: 4
  slug: advertising-create-ad-group-request
- name: CreateCampaignRequest
  property_count: 6
  slug: advertising-create-campaign-request
- name: CreateKeywordRequest
  property_count: 6
  slug: advertising-create-keyword-request
- name: CreateTargetRequest
  property_count: 6
  slug: advertising-create-target-request
- name: KeywordResponse
  property_count: 3
  slug: advertising-keyword-response
- name: Keyword
  property_count: 7
  slug: advertising-keyword
- name: Profile
  property_count: 4
  slug: advertising-profile
- name: ReportRequestResponse
  property_count: 2
  slug: advertising-report-request-response
- name: ReportRequest
  property_count: 3
  slug: advertising-report-request
- name: ReportStatus
  property_count: 4
  slug: advertising-report-status
- name: TargetResponse
  property_count: 3
  slug: advertising-target-response
- name: Target
  property_count: 7
  slug: advertising-target
- name: UpdateCampaignRequest
  property_count: 4
  slug: advertising-update-campaign-request
- name: Address
  property_count: 9
  slug: pay-address
- name: Buyer
  property_count: 3
  slug: pay-buyer
- name: ChargePermission
  property_count: 9
  slug: pay-charge-permission
- name: Charge
  property_count: 9
  slug: pay-charge
- name: CheckoutSession
  property_count: 11
  slug: pay-checkout-session
- name: CreateChargeRequest
  property_count: 5
  slug: pay-create-charge-request
- name: CreateCheckoutSessionRequest
  property_count: 5
  slug: pay-create-checkout-session-request
- name: CreateRefundRequest
  property_count: 3
  slug: pay-create-refund-request
- name: MerchantMetadata
  property_count: 3
  slug: pay-merchant-metadata
- name: Price
  property_count: 2
  slug: pay-price
- name: Refund
  property_count: 6
  slug: pay-refund
- name: StatusDetails
  property_count: 3
  slug: pay-status-details
- name: UpdateCheckoutSessionRequest
  property_count: 3
  slug: pay-update-checkout-session-request
- name: CatalogItemList
  property_count: 3
  slug: selling-partner-catalog-item-list
- name: CatalogItem
  property_count: 4
  slug: selling-partner-catalog-item
- name: CreateReportResponse
  property_count: 1
  slug: selling-partner-create-report-response
- name: CreateReportSpecification
  property_count: 4
  slug: selling-partner-create-report-specification
- name: ErrorList
  property_count: 1
  slug: selling-partner-error-list
- name: InventorySummaries
  property_count: 2
  slug: selling-partner-inventory-summaries
- name: ListingsItemPatchRequest
  property_count: 2
  slug: selling-partner-listings-item-patch-request
- name: ListingsItemPutRequest
  property_count: 2
  slug: selling-partner-listings-item-put-request
- name: ListingsItem
  property_count: 5
  slug: selling-partner-listings-item
- name: ListingsItemSubmissionResponse
  property_count: 4
  slug: selling-partner-listings-item-submission-response
- name: Money
  property_count: 2
  slug: selling-partner-money
- name: OrderItemList
  property_count: 1
  slug: selling-partner-order-item-list
- name: OrderItem
  property_count: 7
  slug: selling-partner-order-item
- name: OrderList
  property_count: 1
  slug: selling-partner-order-list
- name: Order
  property_count: 10
  slug: selling-partner-order
- name: Pagination
  property_count: 2
  slug: selling-partner-pagination
- name: ReportDocument
  property_count: 2
  slug: selling-partner-report-document
- name: ReportList
  property_count: 2
  slug: selling-partner-report-list
- name: Report
  property_count: 5
  slug: selling-partner-report
- name: TransactionList
  property_count: 2
  slug: selling-partner-transaction-list
json_structures:
- name: Advertising Ad Group Response Structure
  property_count: 3
  slug: advertising-ad-group-response-structure
- name: Advertising Ad Group Structure
  property_count: 5
  slug: advertising-ad-group-structure
- name: Advertising Campaign Response Structure
  property_count: 3
  slug: advertising-campaign-response-structure
- name: Advertising Campaign Structure
  property_count: 8
  slug: advertising-campaign-structure
- name: Advertising Create Ad Group Request Structure
  property_count: 4
  slug: advertising-create-ad-group-request-structure
- name: Advertising Create Campaign Request Structure
  property_count: 6
  slug: advertising-create-campaign-request-structure
- name: Advertising Create Keyword Request Structure
  property_count: 6
  slug: advertising-create-keyword-request-structure
- name: Advertising Create Target Request Structure
  property_count: 6
  slug: advertising-create-target-request-structure
- name: Advertising Keyword Response Structure
  property_count: 3
  slug: advertising-keyword-response-structure
- name: Advertising Keyword Structure
  property_count: 7
  slug: advertising-keyword-structure
- name: Advertising Profile Structure
  property_count: 4
  slug: advertising-profile-structure
- name: Advertising Report Request Response Structure
  property_count: 2
  slug: advertising-report-request-response-structure
- name: Advertising Report Request Structure
  property_count: 3
  slug: advertising-report-request-structure
- name: Advertising Report Status Structure
  property_count: 4
  slug: advertising-report-status-structure
- name: Advertising Target Response Structure
  property_count: 3
  slug: advertising-target-response-structure
- name: Advertising Target Structure
  property_count: 7
  slug: advertising-target-structure
- name: Advertising Update Campaign Request Structure
  property_count: 4
  slug: advertising-update-campaign-request-structure
- name: Pay Address Structure
  property_count: 9
  slug: pay-address-structure
- name: Pay Buyer Structure
  property_count: 3
  slug: pay-buyer-structure
- name: Pay Charge Permission Structure
  property_count: 9
  slug: pay-charge-permission-structure
- name: Pay Charge Structure
  property_count: 9
  slug: pay-charge-structure
- name: Pay Checkout Session Structure
  property_count: 11
  slug: pay-checkout-session-structure
- name: Pay Create Charge Request Structure
  property_count: 5
  slug: pay-create-charge-request-structure
- name: Pay Create Checkout Session Request Structure
  property_count: 5
  slug: pay-create-checkout-session-request-structure
- name: Pay Create Refund Request Structure
  property_count: 3
  slug: pay-create-refund-request-structure
- name: Pay Merchant Metadata Structure
  property_count: 3
  slug: pay-merchant-metadata-structure
- name: Pay Price Structure
  property_count: 2
  slug: pay-price-structure
- name: Pay Refund Structure
  property_count: 6
  slug: pay-refund-structure
- name: Pay Status Details Structure
  property_count: 3
  slug: pay-status-details-structure
- name: Pay Update Checkout Session Request Structure
  property_count: 3
  slug: pay-update-checkout-session-request-structure
- name: Selling Partner Catalog Item List Structure
  property_count: 3
  slug: selling-partner-catalog-item-list-structure
- name: Selling Partner Catalog Item Structure
  property_count: 4
  slug: selling-partner-catalog-item-structure
- name: Selling Partner Create Report Response Structure
  property_count: 1
  slug: selling-partner-create-report-response-structure
- name: Selling Partner Create Report Specification Structure
  property_count: 4
  slug: selling-partner-create-report-specification-structure
- name: Selling Partner Error List Structure
  property_count: 1
  slug: selling-partner-error-list-structure
- name: Selling Partner Inventory Summaries Structure
  property_count: 2
  slug: selling-partner-inventory-summaries-structure
- name: Selling Partner Listings Item Patch Request Structure
  property_count: 2
  slug: selling-partner-listings-item-patch-request-structure
- name: Selling Partner Listings Item Put Request Structure
  property_count: 2
  slug: selling-partner-listings-item-put-request-structure
- name: Selling Partner Listings Item Structure
  property_count: 5
  slug: selling-partner-listings-item-structure
- name: Selling Partner Listings Item Submission Response Structure
  property_count: 4
  slug: selling-partner-listings-item-submission-response-structure
- name: Selling Partner Money Structure
  property_count: 2
  slug: selling-partner-money-structure
- name: Selling Partner Order Item List Structure
  property_count: 1
  slug: selling-partner-order-item-list-structure
- name: Selling Partner Order Item Structure
  property_count: 7
  slug: selling-partner-order-item-structure
- name: Selling Partner Order List Structure
  property_count: 1
  slug: selling-partner-order-list-structure
- name: Selling Partner Order Structure
  property_count: 10
  slug: selling-partner-order-structure
- name: Selling Partner Pagination Structure
  property_count: 2
  slug: selling-partner-pagination-structure
- name: Selling Partner Report Document Structure
  property_count: 2
  slug: selling-partner-report-document-structure
- name: Selling Partner Report List Structure
  property_count: 2
  slug: selling-partner-report-list-structure
- name: Selling Partner Report Structure
  property_count: 5
  slug: selling-partner-report-structure
- name: Selling Partner Transaction List Structure
  property_count: 2
  slug: selling-partner-transaction-list-structure
jsonld:
- class_count: 53
  name: Amazon Context
  property_count: 113
  slug: amazon-context
layout: provider
modified: '2026-05-19'
name: Amazon
nav: Providers
network: true
overview: 'Amazon publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Ad Groups API, Campaigns API, Catalog API, and 12 more. Tagged areas include Amazon, Advertising, Alexa, E-Commerce, and Marketplace.


  The Amazon catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, engineering blog, and 16 more developer resources.'
plans:
- name: Amazon Plans Pricing
  plan_count: 3
  slug: amazon-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial Intelligence
  url: https://aws.amazon.com/blogs/machine-learning/
- date: '2026-05-25'
  title: Announcements | Artificial Intelligence
  url: https://aws.amazon.com/blogs/machine-learning/category/post-types/announcements/
- date: '2026-05-25'
  title: AI Technology - Artificial Intelligence
  url: https://aws.amazon.com/ai/
- date: '2026-05-25'
  title: Latest news about AI at Amazon
  url: https://www.aboutamazon.com/artificial-intelligence-ai-news
- date: '2026-05-25'
  title: Press Center - US Press Center - Amazon's Press Releases
  url: https://press.aboutamazon.com/press-release-archive
random_paper: 66
rate_limits:
- limit_count: 2
  name: Amazon Rate Limits
  slug: amazon-rate-limits
rules:
- name: Amazon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-jsonschema-spectral-rules
- name: Amazon API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 11
  slug: amazon-spectral-rules
score:
  band: strong
  composite: 59.6
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 78.2
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon/refs/heads/main/screenshots/amazon-2026-06-20T171600.png
security:
- kind: authentication
  name: Amazon Authentication
  slug: amazon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Amazon Domain Security
  slug: amazon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Vulnerability Disclosure
  slug: amazon-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon
tags:
- Amazon
- Advertising
- Alexa
- E-Commerce
- Marketplace
- Payments
- Voice
- Fortune 100
use_cases:
- description: Automate product listing creation, price updates, inventory management, and order fulfillment for Amazon marketplace sellers.
  name: Marketplace Seller Automation
- description: Build automated bid management and campaign optimization tools using the Amazon Advertising API and performance reporting.
  name: Advertising Campaign Optimization
- description: Add Amazon Pay as a payment option for external e-commerce sites to reduce checkout friction and increase conversion rates.
  name: E-Commerce Payment Integration
- description: Create Alexa skills for voice-driven shopping, home automation, and customer service interactions.
  name: Voice Commerce and Smart Home
- description: Build product recommendation engines and affiliate content sites using the Creators API for real-time Amazon product data.
  name: Affiliate Content Monetization
website: https://www.amazon.com/
---
