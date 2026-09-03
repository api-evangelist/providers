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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Narvar Agentic Access
  operation_count: 3
  slug: narvar-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Submit and update shipment records with carrier, tracking number, and destination data to enable real-time order tracking and delivery notifications.
  name: Narvar Shipment API
  slug: narvar-shipment-api
- description: Initiate and manage returns and exchanges, generate return labels, and receive webhook notifications for return status updates.
  name: Narvar Returns API
  slug: narvar-returns-api
- baseURL: https://api.narvar.com
  baseurl_source: declared
  description: The Orders API from Narvar — 3 operation(s) for orders.
  name: Narvar Orders API
  slug: narvar-orders-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Narvar Orders API
  slug: open-narvar-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/narvar-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/narvar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/narvar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/narvar-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://corp.narvar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.narvar.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/narvar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/narvar
- group: other
  title: ''
  type: X
  url: https://twitter.com/narvarinc
- group: company
  title: ''
  type: Blog
  url: https://corp.narvar.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.narvar.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/narvar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/narvar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/narvar-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/narvar-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/narvar-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://corp.narvar.com/blog/rss.xml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-12'
description: Narvar is a post-purchase commerce platform serving 1,500+ global retail brands with intelligent personalization and automation across delivery, returns, and customer engagement. The platform provides APIs for order creation and updates, shipment tracking, returns and exchange management, and proactive multi-channel customer notifications. Narvar's IRIS AI engine is trained on 74 billion+ annual interactions to deliver predictive post-purchase intelligence. Integrations span 1,000+ carriers and major commerce platforms including Shopify, Salesforce, Magento, and BigCommerce.
examples:
- key_count: 1
  name: Narvar Create Order Example
  slug: narvar-create-order-example
finops:
- name: Narvar Finops
  service_category: ''
  slug: narvar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/narvar.png
json_schemas:
- name: NarvarOrder
  property_count: 1
  slug: narvar-order
jsonld:
- class_count: 7
  name: Narvar Context
  property_count: 42
  slug: narvar-context
layout: provider
modified: '2026-06-12'
name: Narvar
nav: Providers
network: true
overview: 'Narvar publishes 1 API on the [APIs.io](https://apis.io/) network: Orders API. Tagged areas include Post-Purchase, Order Tracking, Delivery Notifications, Returns, and Exchanges.


  The Narvar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Narvar''s developer surface includes authentication, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Narvar Plans Pricing
  plan_count: 3
  slug: narvar-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Narvar Rate Limits
  slug: narvar-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Narvar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: narvar-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 29.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 25.0
    contract_quality: 70.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 46.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/narvar/refs/heads/main/screenshots/narvar-2026-06-20T185948.png
security:
- kind: authentication
  name: Narvar Authentication
  slug: narvar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Narvar Domain Security
  slug: narvar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Narvar Trust Center
  slug: narvar-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: narvar
tags:
- Post-Purchase
- Order Tracking
- Delivery Notifications
- Returns
- Exchanges
- E-Commerce
- Shipments
- Customer Experience
website: https://corp.narvar.com/
---
