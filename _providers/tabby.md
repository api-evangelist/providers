---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tabby Agentic Access
  operation_count: 19
  slug: tabby-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.tabby.ai
  baseurl_source: declared
  description: Checkout is a whole process of customer data collection and payment authorization.
  name: Tabby Checkout API
  slug: tabby-checkout-api
- baseURL: https://api.tabby.ai
  baseurl_source: declared
  description: The Disputes API is designed to simplify the process of handling disputes and help merchants resolve issues with customer orders more efficiently. Merchants can use this API to retrieve a list of disp
  name: Tabby Disputes API
  slug: tabby-disputes-api
- baseURL: https://api.tabby.ai
  baseurl_source: declared
  description: The core of tabby is a payments flow enabling you to handle payments at your webstore.
  name: Tabby Payments API
  slug: tabby-payments-api
- baseURL: https://api.tabby.ai
  baseurl_source: declared
  description: Manage webhook endpoints.
  name: Tabby Webhooks API
  slug: tabby-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Tabby Webhooks
  slug: tabby-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tabby API Reference
  slug: open-tabby-api
- collection_type: open
  name: Tabby API Reference Checkout API
  slug: open-tabby-checkout-api
- collection_type: open
  name: Tabby API Reference Checkout Disputes API
  slug: open-tabby-disputes-api
- collection_type: open
  name: Tabby API Reference Checkout Payments API
  slug: open-tabby-payments-api
- collection_type: open
  name: Tabby API Reference Checkout Webhooks API
  slug: open-tabby-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tabby-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tabby-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tabby-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tabby.ai
- group: company
  title: ''
  type: Website
  url: https://tabby.ai/en-AE/business
- group: start
  title: ''
  type: Portal
  url: https://docs.tabby.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tabby.ai/introduction/quick-start
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.tabby.ai/openapi.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/testing-guidelines/testing-credentials
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/pay-in-4-custom-integration/full-testing-checklist
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/pay-in-4-custom-integration/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/pay-in-4-custom-integration/payment-statuses
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tabby-ai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tabby-ai/tabby-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tabby-ai/tabby-android-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tabby-ai/tabby_flutter_inapp_sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tabby-ai/react-native-example
- group: build
  title: ''
  type: Plugin
  url: https://github.com/tabby-ai/m2-checkout
- group: build
  title: ''
  type: Plugin
  url: https://github.com/tabby-ai/m2-payments
- group: build
  title: ''
  type: Plugin
  url: https://github.com/tabby-ai/m2-feed
- group: build
  title: ''
  type: Plugin
  url: https://github.com/tabby-ai/m2-sub
- group: build
  title: ''
  type: Plugin
  url: https://github.com/tabby-ai/odoo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tabby-ai/hijri-converter
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/shopify/shopify-plugin-installation
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/woocommerce
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/salla
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/zid
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/opencart/opencart-plugin-installation
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/expandcart
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/matjrah
- group: build
  title: ''
  type: Plugin
  url: https://docs.tabby.ai/e-commerce-platforms/salesforce
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/offline-payment-methods/pos-integration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/offline-payment-methods/custom-payment-links
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/pay-in-4-custom-integration/mobile-apps/sdk-all
- group: other
  title: ''
  type: Logos
  url: https://docs.tabby.ai/marketing/brand-assets
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tabbypay
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/paywithtabby
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/tabby.uae
- group: company
  title: ''
  type: Blog
  url: https://tabby.ai/en-AE/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://tabby.ai/en-AE/help-business/about-tabby/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/tabby-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tabby-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tabby-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/tabby-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tabby-vocabulary.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tabby.ai/api-reference/overview
- group: operate
  title: ''
  type: Support
  url: https://support.tabby.ai/l/en
- group: start
  title: ''
  type: SignUp
  url: https://merchant.tabby.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tabby.ai/en-AE/legal/merchant-terms-and-conditions-b2b/latest
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tabby.ai/en-AE/legal/privacy-policy/latest
- group: build
  title: ''
  type: Postman
  url: https://docs.tabby.ai/custom-api.json
- group: operate
  title: ''
  type: StatusPage
  url: https://www.tabby-status.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabby.ai/introduction/ai-tools
- group: build
  title: ''
  type: Packages
  url: packages/tabby-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tabby-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tabby-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tabby-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tabby-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/tabby-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tabby-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tabby-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tabby-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tabby-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tabby-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tabby-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/tabby-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tabby-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/tabby-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tabby-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tabby-webhooks.yml
- group: docs
  title: ''
  type: Documentation
  url: errors/tabby-decline-codes.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tabby-checkout-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tabby-payments-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tabby-webhooks-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tabby-disputes-api-overlay.yaml
created: '2026-05-24'
description: Tabby is the MENA region's largest buy-now-pay-later (BNPL) provider, founded in 2019 by Hosam Arab (ex-Namshi) and Daniil Barkalov, originally in Dubai and now headquartered in Riyadh ahead of a planned IPO. Tabby reached a $3.3B valuation in a February 2025 Series E ($160M co-led by Blue Pool Capital and Hassana Investment Company), making it the most valuable fintech in the Middle East, and reports 15M+ users, 40,000+ merchants, and $10B+ in annualized transaction volume across KSA, UAE, and Kuwait. The Tabby API powers split-purchase checkouts (Pay-in-4 interest-free, monthly plans up to 12 months), payment lifecycle management, webhooks, and dispute resolution, complemented by Tabby Card (Visa-enabled), Tabby Shop discovery, Tabby Care purchase protection, and the Tabby Plus loyalty programme. Public developer surface includes a versioned REST API across two regional hosts (api.tabby.ai for UAE/Kuwait, api.tabby.sa for KSA), an OpenAPI 3.1 specification, iOS / Android /
  Flutter / React Native SDKs, and certified Magento 2, Shopify, WooCommerce, Salla, Zid, OpenCart, ExpandCart, Matjrah, Salesforce, and Odoo plugins.
examples:
- key_count: 2
  name: Tabby Capture Payment Example
  slug: tabby-capture-payment-example
- key_count: 2
  name: Tabby Create Checkout Session Example
  slug: tabby-create-checkout-session-example
- key_count: 2
  name: Tabby Refund Payment Example
  slug: tabby-refund-payment-example
- key_count: 2
  name: Tabby Register Webhook Example
  slug: tabby-register-webhook-example
- key_count: 3
  name: Tabby Webhook Event Example
  slug: tabby-webhook-event-example
finops:
- name: Tabby Finops
  service_category: Financial Services
  slug: tabby-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tabby.png
json_schemas:
- name: TabbyCapture
  property_count: 8
  slug: tabby-capture
- name: TabbyCheckoutSession
  property_count: 6
  slug: tabby-checkout-session
- name: TabbyDispute
  property_count: 11
  slug: tabby-dispute
- name: TabbyOrderItem
  property_count: 19
  slug: tabby-order-item
- name: TabbyPayment
  property_count: 14
  slug: tabby-payment
- name: TabbyRefund
  property_count: 6
  slug: tabby-refund
- name: TabbyWebhookEvent
  property_count: 10
  slug: tabby-webhook-event
jsonld:
- class_count: 29
  name: Tabby Context
  property_count: 5
  slug: tabby-context
layout: provider
mcp_servers:
- description: ''
  name: Tabby Docs MCP Server
  slug: tabby-docs-mcp-server
modified: '2026-08-26'
name: Tabby
nav: Providers
network: true
overview: 'Tabby publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Checkout API, Disputes API, Payments API, and 1 more. Tagged areas include BNPL, Buy Now Pay Later, Consumer Finance, E-Commerce, and Fintech.


  The Tabby catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Tabby''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, pricing, API reference, and 70 more developer resources.'
plans:
- name: Tabby Plans Pricing
  plan_count: 3
  slug: tabby-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Tabby Rate Limits
  slug: tabby-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tabby API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tabby-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Tabby API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: tabby-rules
score:
  band: exemplar
  composite: 81.3
  coverage:
    artifact_dirs: 30
    catalog_gap: 23.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 47.0
    contract_quality: 78.7
    developer_ergonomics: 92.9
    discoverability: 75.9
    governance: 47.0
    operational_transparency: 60.5
  previous_composite: 81.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tabby/refs/heads/main/screenshots/tabby-2026-06-20T194846.png
security:
- kind: authentication
  name: Tabby Authentication
  slug: tabby-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tabby Domain Security
  slug: tabby-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tabby
tags:
- BNPL
- Buy Now Pay Later
- Consumer Finance
- E-Commerce
- Fintech
- Installments
- MENA
- Payments
- Saudi Arabia
- UAE
website: https://tabby.ai
---
