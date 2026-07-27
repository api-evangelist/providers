---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Parcellab Agentic Access
  operation_count: 17
  slug: parcellab-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 8
apis:
- description: Hosted Model Context Protocol server exposing the parcelLab order tracking and returns registration workflow to MCP-compatible agents, authenticated via OAuth 2.1 bearer tokens with scopes such as `tr
  name: parcelLab MCP Server
  slug: parcellab-mcp
- description: Evaluate campaign targeting and redirect analytics events.
  name: parcelLab Campaigns API
  slug: parcellab-campaigns-api
- description: Send custom shop or warehouse events into the tracking timeline.
  name: parcelLab Events API
  slug: parcellab-events-api
- description: Create, update, and inspect orders and their trackings.
  name: parcelLab Orders API
  slug: parcellab-orders-api
- description: Look up nearby pickup and drop-off (PUDO) locations.
  name: parcelLab Place Info API
  slug: parcellab-place-info-api
- description: Pre-checkout delivery date predictions.
  name: parcelLab Promise API
  slug: parcellab-promise-api
- description: Return registrations, configurations, and document templates.
  name: parcelLab Returns API
  slug: parcellab-returns-api
- description: Retrieve survey definitions and submit responses.
  name: parcelLab Surveys API
  slug: parcellab-surveys-api
arazzos:
- description: Create a return registration and immediately read it back by external id.
  name: parcelLab Create and Fetch Return
  slug: parcellab-create-and-fetch-return-workflow
- description: Evaluate campaign targeting for a tracking, then record a redirect analytics event.
  name: parcelLab Evaluate Campaign and Log Redirect
  slug: parcellab-evaluate-campaign-and-redirect-workflow
- description: List return registrations for an account, then fetch the first one in detail.
  name: parcelLab List and Get Return
  slug: parcellab-list-and-get-return-workflow
- description: Get a pre-checkout delivery prediction, then create the order it describes.
  name: parcelLab Predict Delivery and Create Order
  slug: parcellab-predict-then-create-order-workflow
- description: Find a nearby drop-off point, then open a return registration for the order.
  name: parcelLab PUDO Lookup and Register Return
  slug: parcellab-pudo-lookup-and-register-return-workflow
- description: Create a return registration, then submit a survey response tied to it.
  name: parcelLab Register Return and Collect Survey
  slug: parcellab-register-return-and-survey-workflow
- description: Resolve a return configuration for an account, then register a return with it.
  name: parcelLab Resolve Config and Register Return
  slug: parcellab-resolve-config-and-register-return-workflow
- description: Push a warehouse or shop event into the timeline, then refresh the order status.
  name: parcelLab Send Event and Refresh Status
  slug: parcellab-send-event-and-refresh-workflow
- description: Load a survey, fetch its prefilled answers for a reference, then submit a response.
  name: parcelLab Survey Fetch and Submit
  slug: parcellab-survey-fetch-and-submit-workflow
- description: Read an order's tracking status, then evaluate a campaign for that tracking.
  name: parcelLab Track and Target Campaign
  slug: parcellab-track-and-target-campaign-workflow
- description: Create or update an order, then retrieve its latest tracking and checkpoints.
  name: parcelLab Create Order and Track
  slug: parcellab-upsert-order-and-track-workflow
artifact_total: 77
collections:
- collection_type: postman
  name: parcelLab API
  slug: postman-parcellab
- collection_type: open
  name: parcelLab API
  slug: open-parcellab
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parcellab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parcellab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parcellab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parcellab-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/parcellab/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-create-and-fetch-return-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-evaluate-campaign-and-redirect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-list-and-get-return-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-predict-then-create-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-pudo-lookup-and-register-return-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-register-return-and-survey-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-resolve-config-and-register-return-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-send-event-and-refresh-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-survey-fetch-and-submit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-track-and-target-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/parcellab-upsert-order-and-track-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://parcellab.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.parcellab.com/docs/developers/readme
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parcellab.com/docs/readme
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.parcellab.com/docs/onboarding
- group: auth
  title: ''
  type: Authentication
  url: https://docs.parcellab.com/docs/developers/getting-started/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parcellab.com/docs/developers/getting-started/api-reference
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.parcellab.com/docs/developers/getting-started/error-codes
- group: start
  title: ''
  type: Signup
  url: https://app.parcellab.com/signin
- group: start
  title: ''
  type: Console
  url: https://app.parcellab.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parcellab.com
- group: commercial
  title: ''
  type: Pricing
  url: https://parcellab.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://parcellab.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parcellab.com/legal/terms-of-service/
- group: company
  title: ''
  type: Careers
  url: https://parcellab.com/careers
- group: operate
  title: ''
  type: Support
  url: https://parcellab.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parcelLab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parcellab
- group: auth
  title: ''
  type: SecurityCompliance
  url: https://docs.parcellab.com/docs/platform/security-compliance
- group: other
  title: ''
  type: SingleSignOn
  url: https://docs.parcellab.com/docs/platform/security-compliance/single-sign-on
- group: other
  title: ''
  type: DataRetentionPolicy
  url: https://docs.parcellab.com/docs/platform/security-compliance/data-retention-policy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/parcelLab/parcelLab-js-plugin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/parcelLab/js-plugin-utils
- group: build
  title: ''
  type: SDKs
  url: https://github.com/parcelLab/regionIdentifier
- group: build
  title: ''
  type: SDKs
  url: https://github.com/parcelLab/parcellab-embedded-ui-snippets
- group: build
  title: ''
  type: SDKs
  url: https://github.com/parcelLab/charts
- group: build
  title: ''
  type: AgentSDK
  url: https://github.com/parcelLab/parcellab-mcp-server
- group: commercial
  title: ''
  type: Plans
  url: plans/parcellab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parcellab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/parcellab-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/parcellab-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/parcellab-vocabulary.yml
- group: other
  title: ''
  type: Offices
  url: ''
created: '2026-05-25'
description: parcelLab is a Munich-headquartered post-purchase experience platform (parcelLab GmbH) used by retailers including IKEA, Hugo Boss, Dyson, Puma, and John Lewis to turn delivery and returns into a branded, revenue-generating part of the customer journey. The platform spans four modules — Convert (pre-checkout delivery promise), Engage (multichannel post-purchase communications), Retain (Returns Portal and returns experience), and Insights (analytics, benchmarking, control tower) — layered with AI agents (WISMO/R, Insights, Fraud & Abuse) and exposed via the parcelLab API v4 Enhanced. Global, EU, and US regional endpoints are available; the same data backs a Model Context Protocol server at agents.parcellab.com/mcp/ for agentic clients.
examples:
- key_count: 2
  name: Parcellab Create Return Registration Example
  slug: parcellab-create-return-registration-example
- key_count: 2
  name: Parcellab Get Order Info Example
  slug: parcellab-get-order-info-example
- key_count: 2
  name: Parcellab Predict Delivery Example
  slug: parcellab-predict-delivery-example
- key_count: 2
  name: Parcellab Pudo Lookup Example
  slug: parcellab-pudo-lookup-example
- key_count: 2
  name: Parcellab Upsert Order Example
  slug: parcellab-upsert-order-example
features:
- description: Pre-checkout delivery date prediction (Promise API) to drive cart conversion.
  name: Delivery Promise
- description: Idempotent v4 Orders API with mutations to add/cancel trackings or amend line items.
  name: Order & Tracking Ingestion
- description: Integrations with 450+ carriers worldwide via direct carrier interfaces.
  name: Carrier Network
- description: Branded self-service returns portal with refund options, exchanges, retention offers, split returns, and claims.
  name: Returns Portal
- description: Email, SMS, Push, Webhook, and Order Status Page delivery of branded post-purchase messages.
  name: Multichannel Communications
- description: Native Apple Wallet passes for order tracking.
  name: Apple Wallet Tracking
- description: WISMO/R Agent, Insights Agent, and Fraud & Abuse Insights powered by ML over post-purchase data.
  name: AI Agents
- description: Trackings Insights, Communication Insights, Control Tower, Logistics Analysis, and Benchmarking dashboards.
  name: Insights & Benchmarking
- description: Embedded surveys and NPS feedback tied to deliveries or return registrations.
  name: Surveys & NPS
- description: Hosted Model Context Protocol server (agents.parcellab.com/mcp/) for agentic order tracking and return registration workflows.
  name: MCP Server
finops:
- name: Parcellab Finops
  service_category: Post-Purchase Experience SaaS
  slug: parcellab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parcellab.png
integrations:
- description: Native Shopify integration for tracking, communications, and returns.
  name: Shopify
- description: Webhook extension for Magento 2 storefronts.
  name: Magento 2
- description: Embedded Order Status Page for Shopware shops.
  name: Shopware
- description: Route post-purchase email through Klaviyo journeys.
  name: Klaviyo
- description: Route post-purchase SMS through Postscript.
  name: Postscript
- description: Customer service ticket sidebar with parcelLab tracking data.
  name: Zendesk
- description: Helpdesk widget displaying order and tracking data.
  name: Gorgias
- description: Helpdesk app for parcelLab delivery context.
  name: Kustomer
- description: Customer Service Integration surfacing parcelLab data in SFSC.
  name: Salesforce Service Cloud
- description: Unified cross-border returns experience.
  name: Global-e
- description: Native order tracking passes in Apple Wallet.
  name: Apple Wallet
- description: List non-returnable items directly from the Returns Portal onto Poshmark.
  name: Poshmark
json_schemas:
- name: parcelLab Address
  property_count: 9
  slug: parcellab-address
- name: parcelLab Line Item
  property_count: 7
  slug: parcellab-line-item
- name: parcelLab Order
  property_count: 11
  slug: parcellab-order
- name: parcelLab Promise Prediction
  property_count: 3
  slug: parcellab-promise-prediction
- name: parcelLab Return Registration
  property_count: 22
  slug: parcellab-return-registration
- name: parcelLab Tracking
  property_count: 6
  slug: parcellab-tracking
json_structures:
- name: Parcellab Order Structure
  property_count: 10
  slug: parcellab-order-structure
- name: Parcellab Return Registration Structure
  property_count: 12
  slug: parcellab-return-registration-structure
jsonld:
- class_count: 25
  name: Parcellab Context
  property_count: 0
  slug: parcellab-context
layout: provider
modified: '2026-05-25'
name: parcelLab
nav: Providers
network: true
overview: 'parcelLab publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Events API, Orders API, and 4 more. Tagged areas include Post-Purchase, E-Commerce, Tracking, Returns, and Shipping.


  The parcelLab catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  parcelLab''s developer surface includes authentication, documentation, getting-started guide, API reference, signup flow, developer console, pricing, and 40 more developer resources.'
plans:
- name: Parcellab Plans Pricing
  plan_count: 4
  slug: parcellab-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 2
  name: Parcellab Rate Limits
  slug: parcellab-rate-limits
rules:
- name: parcelLab API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: parcellab-jsonschema-spectral-rules
- name: parcelLab API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: parcellab-rules
score:
  band: exemplar
  composite: 72.1
  delta: 5.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 74.0
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 42.1
  previous_composite: 66.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/parcellab/refs/heads/main/screenshots/parcellab-2026-06-20T191411.png
security:
- kind: authentication
  name: Parcellab Authentication
  slug: parcellab-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parcellab Domain Security
  slug: parcellab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Parcellab Vulnerability Disclosure
  slug: parcellab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: parcellab
solutions:
- description: Pre-checkout delivery promise module.
  name: Convert
- description: Multichannel post-purchase communication module.
  name: Engage
- description: Returns Portal and returns experience module.
  name: Retain
- description: Analytics, benchmarking, and control tower module.
  name: Insights
- description: Add-on autonomous agents for WISMO/R, insights, and fraud.
  name: AI Agents
tags:
- Post-Purchase
- E-Commerce
- Tracking
- Returns
- Shipping
- Delivery
- Customer Experience
- Logistics
- Communications
- Germany
use_cases:
- description: Cut "Where Is My Order" support contacts by proactively communicating tracking updates.
  name: WISMO Reduction
- description: Convert returns into exchanges, store credit, or retention offers to keep revenue.
  name: Returns as Retention
- description: Display a delivery promise at checkout to reduce abandonment.
  name: Cart Conversion
- description: Provide customs handling and Global-e integration for unified cross-border returns.
  name: Cross-Border Returns
- description: Compare lead-times, exceptions, and on-time rates across the carrier portfolio.
  name: Carrier Performance Benchmarking
- description: Embed branded campaigns and product recommendations in delivery communications.
  name: Marketing in the Delivery Window
website: https://parcellab.com
---
