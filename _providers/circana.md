---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Circana Agentic Access
  operation_count: 14
  slug: circana-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 20
apis:
- description: Unify+ is Circana's business intelligence platform that provides access to data visualization, analytics, and reporting capabilities with conversational AI for automated analysis and insights.
  name: Circana Unify+ API
  slug: unify-plus-api
- description: Liquid Data Go is a turnkey insights solution delivering affordable, actionable market, retailer, and consumer intelligence for emerging and mid-market CPG and general merchandise brands with 15% more
  name: Circana Liquid Data Go API
  slug: liquid-data-go-api
- description: Intelligence Suite helps integrate, harmonize, and automate data workflows with hundreds of pre-built connectors for Azure, Snowflake, AWS, Google BigQuery, and Databricks, enabling real-time automati
  name: Circana Intelligence Suite API
  slug: intelligence-suite-api
- description: Complete Market provides robust POS measurement for in-store and online sales with fulfillment type breaks and UPC details across CPG categories.
  name: Circana Complete Market API
  slug: complete-market-api
- description: Complete Consumer combines verified purchase data, survey insights, and advanced shopper panels to provide a 360-degree view of how, where, and why consumers shop across channels.
  name: Circana Complete Consumer API
  slug: complete-consumer-api
- description: Complete Beauty offers a holistic view of the beauty industry combining mass and prestige POS data for manufacturers and retailers to track emerging shifts in consumer preferences and category perform
  name: Circana Complete Beauty API
  slug: complete-beauty-api
- description: Complete Food and Beverage unites retail, CPG, foodservice, and consumption data to deliver a complete understanding of U.S. food and beverage consumption patterns.
  name: Circana Complete Food and Beverage API
  slug: complete-food-beverage-api
- description: Liquid Data Collaborate provides AI-powered retail data analysis capabilities for brands, manufacturers, and retailers enabling collaborative insights and data-driven decision making.
  name: Circana Liquid Data Collaborate API
  slug: liquid-data-collaborate-api
- description: Liquid Data Engage propels retailers into a new era of decision-making with precise, customer-centric data for developing retail strategies.
  name: Circana Liquid Data Engage API
  slug: liquid-data-engage-api
- description: Liquid Activation enables marketers to build and activate purchase-based audiences in minutes using deterministic data, integrating with publishers, media platforms, and marketing technologies.
  name: Circana Liquid Activation API
  slug: liquid-activation-api
- description: Price and Promotion solutions combine AI models and granular store-level data to optimize pricing strategies, quantify elasticity, and improve promotional efficiency delivering 5% average sales growth
  name: Circana Price and Promotion API
  slug: price-promotion-api
- description: Retail Media connects shopper analytics to activation, linking marketing to retail sales for longitudinal insights and improved ROAS with AI-driven media channel performance assessment.
  name: Circana Retail Media API
  slug: retail-media-api
- description: Complete Why delivers fast AI-powered insights so teams know what is working, what is not, and where to act next before opportunities disappear.
  name: Circana Complete Why Analytics API
  slug: complete-why-api
- description: Brand performance and analytics
  name: Circana Brands API
  slug: circana-brands-api
- description: Product category hierarchy and management
  name: Circana Categories API
  slug: circana-categories-api
- description: Consumer panel data and shopper insights
  name: Circana Consumer Panel API
  slug: circana-consumer-panel-api
- description: Data export and download operations
  name: Circana Exports API
  slug: circana-exports-api
- description: Access point-of-sale and market measurement data
  name: Circana Market Data API
  slug: circana-market-data-api
- description: Report generation and management
  name: Circana Reports API
  slug: circana-reports-api
- description: Retailer data and channel analytics
  name: Circana Retailers API
  slug: circana-retailers-api
artifact_total: 140
collections:
- collection_type: postman
  name: Circana Liquid Data Brands API
  slug: postman-circana-brands-api
- collection_type: postman
  name: Circana Liquid Data Brands Categories API
  slug: postman-circana-categories-api
- collection_type: postman
  name: Circana Liquid Data Brands Consumer Panel API
  slug: postman-circana-consumer-panel-api
- collection_type: postman
  name: Circana Liquid Data Brands Exports API
  slug: postman-circana-exports-api
- collection_type: postman
  name: Circana Liquid Data Brands Market Data API
  slug: postman-circana-market-data-api
- collection_type: postman
  name: Circana Liquid Data Brands Reports API
  slug: postman-circana-reports-api
- collection_type: postman
  name: Circana Liquid Data Brands Retailers API
  slug: postman-circana-retailers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Circana Liquid Data Brands API
  slug: open-circana-brands-api
- collection_type: open
  name: Circana Liquid Data Brands Categories API
  slug: open-circana-categories-api
- collection_type: open
  name: Circana Liquid Data Brands Consumer Panel API
  slug: open-circana-consumer-panel-api
- collection_type: open
  name: Circana Liquid Data Brands Exports API
  slug: open-circana-exports-api
- collection_type: open
  name: Circana Liquid Data Brands Market Data API
  slug: open-circana-market-data-api
- collection_type: open
  name: Circana Liquid Data Brands Reports API
  slug: open-circana-reports-api
- collection_type: open
  name: Circana Liquid Data Brands Retailers API
  slug: open-circana-retailers-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/circana/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/circana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circana-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.circana.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.circana.com/solutions
- group: company
  title: ''
  type: Blog
  url: https://www.circana.com/intelligence/press-releases
- group: other
  title: ''
  type: Customers
  url: https://www.circana.com/case-studies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.circana.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circana.com/the-circana-group-global-privacy-policy-and-notice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wearecircana
- group: operate
  title: ''
  type: Contact
  url: https://www.circana.com/contact
- group: other
  title: ''
  type: Resources
  url: https://www.circana.com/intelligence
- group: company
  title: ''
  type: Partners
  url: https://www.circana.com/company/partners
- group: learn
  title: ''
  type: Training
  url: https://www.circana.com/industry-experts
- group: commercial
  title: ''
  type: Pricing
  url: https://www.circana.com/solutions
- group: design
  title: ''
  type: SpectralRules
  url: rules/circana-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/circana-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://circana.com/llms.txt
created: '2024-01-01'
description: Circana (formerly IRI and The NPD Group) is the leading advisor on the complexity of consumer behavior, providing data-driven insights, analytics, and technology solutions that help almost 7,000 brands and retailers understand and predict consumer purchasing patterns across retail, CPG, beauty, foodservice, healthcare, and technology sectors covering $4T+ in global consumer spending across 26 industries.
examples:
- key_count: 6
  name: Circana Createexport Example
  slug: circana-createexport-example
- key_count: 6
  name: Circana Createreport Example
  slug: circana-createreport-example
- key_count: 6
  name: Circana Getbrand Example
  slug: circana-getbrand-example
- key_count: 6
  name: Circana Getcategory Example
  slug: circana-getcategory-example
- key_count: 6
  name: Circana Getconsumerpurchases Example
  slug: circana-getconsumerpurchases-example
- key_count: 6
  name: Circana Getconsumersegments Example
  slug: circana-getconsumersegments-example
- key_count: 6
  name: Circana Getexport Example
  slug: circana-getexport-example
- key_count: 6
  name: Circana Getmarketshare Example
  slug: circana-getmarketshare-example
- key_count: 6
  name: Circana Getpointofsaledata Example
  slug: circana-getpointofsaledata-example
- key_count: 6
  name: Circana Getreport Example
  slug: circana-getreport-example
- key_count: 6
  name: Circana Listbrands Example
  slug: circana-listbrands-example
- key_count: 6
  name: Circana Listcategories Example
  slug: circana-listcategories-example
- key_count: 6
  name: Circana Listreports Example
  slug: circana-listreports-example
- key_count: 6
  name: Circana Listretailers Example
  slug: circana-listretailers-example
- key_count: 6
  name: Liquid Data Brand Detail Example
  slug: liquid-data-brand-detail-example
- key_count: 8
  name: Liquid Data Category Detail Example
  slug: liquid-data-category-detail-example
- key_count: 7
  name: Liquid Data Consumer Purchase Record Example
  slug: liquid-data-consumer-purchase-record-example
- key_count: 6
  name: Liquid Data Consumer Segment Example
  slug: liquid-data-consumer-segment-example
- key_count: 7
  name: Liquid Data Export Detail Example
  slug: liquid-data-export-detail-example
- key_count: 5
  name: Liquid Data Market Share Record Example
  slug: liquid-data-market-share-record-example
- key_count: 9
  name: Liquid Data Pos Record Example
  slug: liquid-data-pos-record-example
- key_count: 9
  name: Liquid Data Report Detail Example
  slug: liquid-data-report-detail-example
- key_count: 5
  name: Liquid Data Retailer Summary Example
  slug: liquid-data-retailer-summary-example
features:
- description: Cross-industry data and advanced analytics platform deployable across Azure, AWS, Google Cloud, and Oracle Cloud environments.
  name: Liquid Data Platform
- description: Next-generation intelligence platform leveraging generative AI to accelerate decision-making and shift focus from hindsight to foresight.
  name: Liquid AI
- description: AI embedded into Unify+ allowing teams to automate routine analysis and reduce time to insight.
  name: Conversational AI
- description: Robust POS measurement for in-store and online sales with fulfillment type breaks and UPC details.
  name: Complete Market Measurement
- description: 360-degree view of U.S. buyers tracking purchases across channels with POS-aligned panel insights.
  name: Consumer Panel Data
- description: Hundreds of pre-built connectors for Azure, Snowflake, AWS, Google BigQuery, and Databricks integration.
  name: Intelligence Suite Connectors
- description: Build and activate audiences using deterministic purchase data for precision marketing.
  name: Purchase-Based Audiences
- description: AI models with granular store-level data to quantify price elasticity and promotional efficiency.
  name: Price Elasticity Modeling
- description: Coverage of $4T+ in global consumer spending across 26 industries in 23 countries.
  name: Cross-Industry Coverage
- description: Industry-only predictive market structure based on actual shopper behavior for new product forecasts within 10% accuracy.
  name: Predictive Market Structure
finops:
- name: Circana Finops
  service_category: Market Intelligence / Consumer Data
  slug: circana-finops
image: /assets/icons/circana.png
integrations:
- description: Access Circana POS and panel data directly within Snowflake Data Cloud for seamless data sharing and collaboration.
  name: Snowflake
- description: Deploy Liquid Data platform on Azure for cloud-native data integration and analytics workflows.
  name: Microsoft Azure
- description: Deploy Liquid Data platform on AWS for scalable cloud analytics and data processing.
  name: Amazon Web Services
- description: Connect Circana data to Google BigQuery for large-scale analytics and machine learning workloads.
  name: Google BigQuery
- description: Integrate Circana data with Databricks for advanced analytics, data engineering, and AI model training.
  name: Databricks
- description: Collaborate on RampIDs with Circana purchase data in Snowflake for privacy-safe audience targeting.
  name: LiveRamp
- description: Deploy Liquid Data platform on Oracle Cloud for enterprise-grade data processing and analytics.
  name: Oracle Cloud
- description: Deploy Liquid Data platform on GCP for cloud-based analytics and data integration.
  name: Google Cloud Platform
json_schemas:
- name: BrandDetail
  property_count: 6
  slug: circana-branddetail
- name: BrandListResponse
  property_count: 2
  slug: circana-brandlistresponse
- name: BrandSummary
  property_count: 5
  slug: circana-brandsummary
- name: CategoryDetail
  property_count: 8
  slug: circana-categorydetail
- name: CategoryListResponse
  property_count: 2
  slug: circana-categorylistresponse
- name: CategorySummary
  property_count: 6
  slug: circana-categorysummary
- name: ConsumerPurchaseRecord
  property_count: 7
  slug: circana-consumerpurchaserecord
- name: ConsumerPurchaseResponse
  property_count: 2
  slug: circana-consumerpurchaseresponse
- name: ConsumerSegment
  property_count: 6
  slug: circana-consumersegment
- name: ConsumerSegmentResponse
  property_count: 2
  slug: circana-consumersegmentresponse
- name: CreateExportRequest
  property_count: 4
  slug: circana-createexportrequest
- name: CreateReportRequest
  property_count: 7
  slug: circana-createreportrequest
- name: DataCoverage
  property_count: 4
  slug: circana-datacoverage
- name: ErrorResponse
  property_count: 4
  slug: circana-errorresponse
- name: ExportDetail
  property_count: 7
  slug: circana-exportdetail
- name: MarketPresence
  property_count: 3
  slug: circana-marketpresence
- name: MarketShareRecord
  property_count: 5
  slug: circana-marketsharerecord
- name: MarketShareResponse
  property_count: 2
  slug: circana-marketshareresponse
- name: Pagination
  property_count: 3
  slug: circana-pagination
- name: POSDataResponse
  property_count: 2
  slug: circana-posdataresponse
- name: POSRecord
  property_count: 9
  slug: circana-posrecord
- name: ReportDetail
  property_count: 9
  slug: circana-reportdetail
- name: ReportListResponse
  property_count: 2
  slug: circana-reportlistresponse
- name: ReportSummary
  property_count: 6
  slug: circana-reportsummary
- name: RetailerListResponse
  property_count: 2
  slug: circana-retailerlistresponse
- name: RetailerSummary
  property_count: 5
  slug: circana-retailersummary
- name: BrandDetail
  property_count: 6
  slug: liquid-data-brand-detail
- name: CategoryDetail
  property_count: 8
  slug: liquid-data-category-detail
- name: ConsumerPurchaseRecord
  property_count: 7
  slug: liquid-data-consumer-purchase-record
- name: ConsumerSegment
  property_count: 6
  slug: liquid-data-consumer-segment
- name: ExportDetail
  property_count: 7
  slug: liquid-data-export-detail
- name: MarketShareRecord
  property_count: 5
  slug: liquid-data-market-share-record
- name: POSRecord
  property_count: 9
  slug: liquid-data-pos-record
- name: ReportDetail
  property_count: 9
  slug: liquid-data-report-detail
- name: RetailerSummary
  property_count: 5
  slug: liquid-data-retailer-summary
json_structures:
- name: Circana Structure
  property_count: 0
  slug: circana-structure
- name: Liquid Data Brand Detail Structure
  property_count: 6
  slug: liquid-data-brand-detail-structure
- name: Liquid Data Category Detail Structure
  property_count: 8
  slug: liquid-data-category-detail-structure
- name: Liquid Data Consumer Purchase Record Structure
  property_count: 7
  slug: liquid-data-consumer-purchase-record-structure
- name: Liquid Data Consumer Segment Structure
  property_count: 6
  slug: liquid-data-consumer-segment-structure
- name: Liquid Data Export Detail Structure
  property_count: 7
  slug: liquid-data-export-detail-structure
- name: Liquid Data Market Share Record Structure
  property_count: 5
  slug: liquid-data-market-share-record-structure
- name: Liquid Data Pos Record Structure
  property_count: 9
  slug: liquid-data-pos-record-structure
- name: Liquid Data Report Detail Structure
  property_count: 9
  slug: liquid-data-report-detail-structure
- name: Liquid Data Retailer Summary Structure
  property_count: 5
  slug: liquid-data-retailer-summary-structure
jsonld:
- class_count: 16
  name: Circana Liquid Data Context
  property_count: 51
  slug: circana-liquid-data-context
layout: provider
modified: '2026-05-19'
name: Circana
nav: Providers
network: true
overview: 'Circana publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Categories API, Consumer Panel API, and 4 more. Tagged areas include Analytics, Consumer Data, Market Research, Retail, and CPG.


  The Circana catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Circana''s developer surface includes authentication, developer portal, documentation, engineering blog, training material, pricing, and 13 more developer resources.'
plans:
- name: Circana Plans Pricing
  plan_count: 1
  slug: circana-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Circana Rate Limits
  slug: circana-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Circana API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: circana-jsonschema-spectral-rules
- effective_rule_count: 86
  extends:
  - spectral:oas
  name: Circana API Rules
  rule_count: 45
  severity_counts:
    error: 19
    hint: 0
    info: 6
    warn: 20
  slug: circana-spectral-rules
score:
  band: thin
  composite: 34.5
  delta: -5.5
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 25.0
    contract_quality: 30.1
    developer_ergonomics: 35.7
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/screenshots/circana-2026-06-20T174349.png
security:
- kind: authentication
  name: Circana Authentication
  slug: circana-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Circana Domain Security
  slug: circana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circana
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
use_cases:
- description: Track brand and category performance across retail channels with POS and panel data to understand competitive positioning.
  name: Market Share Tracking
- description: Validate new product concepts with custom simulations and predictive market structure analysis to prioritize winning ideas.
  name: New Product Innovation
- description: Optimize pricing strategies using AI-driven elasticity models and store-level data to maximize revenue and margin.
  name: Pricing Optimization
- description: Plan and evaluate trade promotions with quantified ROI metrics and scenario modeling for smarter promotional spending.
  name: Promotional Planning
- description: Segment consumers by behavior, demographics, and purchase patterns to tailor marketing and product strategies.
  name: Consumer Segmentation
- description: Measure retail media campaign performance linking advertising spend to actual sales outcomes for improved ROAS.
  name: Retail Media Measurement
- description: Optimize product mix by category, store, and geography to improve shelf efficiency and drive sales growth.
  name: Assortment Optimization
- description: Monitor near-real-time cross-retailer inventory and distribution data to spot risks and gaps early.
  name: Supply Chain Visibility
- description: Build purchase-based audience segments and activate them across publishers and media platforms in minutes.
  name: Audience Activation
- description: Unite retail, CPG, foodservice, and consumption data for a complete picture of food and beverage market dynamics.
  name: Foodservice Intelligence
website: https://www.circana.com
---
