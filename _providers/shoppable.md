---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Shoppable Agentic Access
  operation_count: 8
  slug: shoppable-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://cloud.shoppable.com
  baseurl_source: declared
  description: The Catalog API from Shoppable — 1 operation(s) for catalog.
  name: Shoppable Catalog API
  slug: shoppable-catalog-api
- baseURL: https://cloud.shoppable.com
  baseurl_source: declared
  description: The Checkout API from Shoppable — 1 operation(s) for checkout.
  name: Shoppable Checkout API
  slug: shoppable-checkout-api
- baseURL: https://cloud.shoppable.com
  baseurl_source: declared
  description: The Merchants API from Shoppable — 2 operation(s) for merchants.
  name: Shoppable Merchants API
  slug: shoppable-merchants-api
- baseURL: https://cloud.shoppable.com
  baseurl_source: declared
  description: The OrderData API from Shoppable — 1 operation(s) for orderdata.
  name: Shoppable OrderData API
  slug: shoppable-orderdata-api
- baseURL: https://cloud.shoppable.com
  baseurl_source: declared
  description: The Orders API from Shoppable — 2 operation(s) for orders.
  name: Shoppable Orders API
  slug: shoppable-orders-api
- baseURL: https://cloud.shoppable.com
  baseurl_source: declared
  description: The Products API from Shoppable — 1 operation(s) for products.
  name: Shoppable Products API
  slug: shoppable-products-api
artifact_total: 22
collections:
- collection_type: open
  name: Shoppable Commerce API Suite Catalog API
  slug: open-shoppable-catalog-api
- collection_type: open
  name: Shoppable Commerce API Suite Catalog Checkout API
  slug: open-shoppable-checkout-api
- collection_type: open
  name: Shoppable Commerce API Suite Catalog Merchants API
  slug: open-shoppable-merchants-api
- collection_type: open
  name: Shoppable Commerce API Suite Catalog OrderData API
  slug: open-shoppable-orderdata-api
- collection_type: open
  name: Shoppable Commerce API Suite Catalog Orders API
  slug: open-shoppable-orders-api
- collection_type: open
  name: Shoppable Commerce API Suite Catalog Products API
  slug: open-shoppable-products-api
common:
- group: commercial
  href: https://artifacts.apis.io/shoppable/plans/shoppable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shoppable-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://about.shoppable.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/shoppable/overlays/shoppable-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shoppable-cloud-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/shoppable/security/shoppable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shoppable-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/shoppable/agentic-access/shoppable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shoppable-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/shoppable/authentication/shoppable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shoppable-authentication.yml
- group: agent
  href: https://artifacts.apis.io/shoppable/mcp/shoppable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shoppable-mcp.yml
- group: design
  href: https://artifacts.apis.io/shoppable/conventions/shoppable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shoppable-conventions.yml
- group: design
  href: https://artifacts.apis.io/shoppable/conformance/shoppable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shoppable-conformance.yml
- group: design
  href: https://artifacts.apis.io/shoppable/lifecycle/shoppable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shoppable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shoppable.com
- group: operate
  href: https://artifacts.apis.io/shoppable/changelog/shoppable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shoppable-changelog.yml
- group: agent
  href: https://artifacts.apis.io/shoppable/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/shoppable/llms/shoppable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shoppable-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://about.shoppable.com/help/setup-developer-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://ask.shoppable.com
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis-docs/shoppable-dca/shoppable-cloud_api/1.0.2
- group: start
  title: ''
  type: GettingStarted
  url: https://about.shoppable.com/help/setup-developer-documentation
- group: operate
  title: ''
  type: Support
  url: https://ask.shoppable.com
- group: company
  title: ''
  type: Blog
  url: https://about.shoppable.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://about.shoppable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.shoppable.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.shoppable.com/terms#terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.shoppable.com/terms#privacy-policy
- group: company
  title: ''
  type: Website
  url: https://shoppable.com
created: '2026-07-17'
description: Shoppable is embeddable commerce infrastructure that lets shoppers buy any product from any retailer in a single universal cart without leaving the content they are in. Founded in 2011 by Heather Udo, the company powers off-site commerce across editorial content, social media, ads, connected TV, email, and emerging AI/agentic channels through a single integration. Its Shoppable Commerce API Suite (OpenAPI 3.0) exposes product lookup, catalog search, merchant data, order data, and a universal v6 checkout backed by Stripe tokenization, plus a hosted Model Context Protocol (MCP) server for agentic commerce. Shoppable holds four U.S. patents for universal checkout and is backed by 500 Global, MI Ventures, and Bodley Group.
finops:
- has_sources: true
  method: derived
  name: Shoppable Finops
  primary_unit: month, billed annually
  service_category: ''
  slug: shoppable-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shoppable.png
layout: provider
mcp_servers:
- description: 'Official hosted Model Context Protocol server for Shoppable''s universal commerce platform. Exposes conversational product discovery, cart building, and order lookup to AI assistants (Claude, ChatGPT, '
  name: Shoppable MCP Server
  slug: shoppable-mcp-server
modified: '2026-10-06'
name: Shoppable
nav: Providers
network: true
overview: 'Shoppable publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Checkout API, Merchants API, and 3 more. Tagged areas include Company, Commerce, E-Commerce, Checkout, and Catalog.


  The Shoppable catalog on APIs.io includes 1 Spectral governance ruleset.


  Shoppable''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
plans:
- name: Shoppable Plans Pricing
  plan_count: 4
  slug: shoppable-plans-pricing
- name: Shoppable Price Estimates
  plan_count: 0
  slug: shoppable-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Shoppable API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: shoppable-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 62.5
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shoppable/shoppable-2026-08-17T081841.png
security:
- kind: authentication
  name: Shoppable Authentication
  slug: shoppable-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shoppable Domain Security
  slug: shoppable-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Look up order status
  slug: shoppable-order-lookup
- name: Search the catalog and complete a checkout
  slug: shoppable-search-and-checkout
slug: shoppable
tags:
- Company
- Commerce
- E-Commerce
- Checkout
- Catalog
- Payments
- Agentic Commerce
- MCP
- Embeddable Commerce
- Retail
website: https://shoppable.com
---
