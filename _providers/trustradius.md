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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trustradius Agentic Access
  operation_count: 9
  slug: trustradius-agentic-access
  summary_line: 9 operations
api_count: 6
apis:
- description: 'The TrustRadius Downstream Intent Data API delivers buyer and deal intelligence, revealing which accounts are actively researching a vendor''s products, competitor products, and software categories on '
  name: TrustRadius Downstream Intent Data API
  slug: trustradius-intent-data-api
- description: The TrustRadius Content Syndication API (TrustQuotes) enables vendors to extract and embed customer review quotes across marketing channels. Businesses can retrieve licensed review excerpts, quotes, a
  name: TrustRadius Content Syndication API
  slug: trustradius-content-syndication-api
- description: Software category operations
  name: TrustRadius Categories API
  slug: trustradius-categories-api
- description: Software company operations
  name: TrustRadius Companies API
  slug: trustradius-companies-api
- description: Software product operations
  name: TrustRadius Products API
  slug: trustradius-products-api
- description: Product review retrieval operations
  name: TrustRadius Reviews API
  slug: trustradius-reviews-api
artifact_total: 21
collections:
- collection_type: open
  name: TrustRadius Public API
  slug: open-trustradius-public
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trustradius-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustradius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustradius-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustradius.com/
- group: start
  title: ''
  type: Portal
  url: https://solutions.trustradius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.trustradius.com/
- group: auth
  title: ''
  type: Authentication
  url: https://trustradius.freshdesk.com/support/solutions/articles/43000639047
- group: other
  title: ''
  type: Products
  url: https://solutions.trustradius.com/products/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustradius.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustradius.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustradius
- group: other
  title: ''
  type: X
  url: https://twitter.com/TrustRadius
- group: build
  title: ''
  type: GitHub
  url: https://github.com/trustradius
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/rules/trustradius-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://solutions.trustradius.com/feed/
created: '2026-05-03'
description: TrustRadius is a B2B buyer intelligence and software review platform that helps technology buyers make confident purchasing decisions and enables vendors to turn verified customer reviews into demand generation. Founded in 2012 and headquartered in Austin, Texas, TrustRadius hosts in-depth verified reviews averaging 400+ words, and provides vendors with downstream intent data showing who is actively researching their products, competitors, and categories. The platform offers REST APIs for accessing product review data, buyer intent signals, and content licensing capabilities, with integrations into Salesforce, HubSpot, 6sense, Demandbase, LinkedIn, Marketo, and Snowflake. Authentication uses API key access from the TrustRadius Vendor Portal.
examples:
- key_count: 2
  name: Trustradius Get Product Reviews Example
  slug: trustradius-get-product-reviews-example
- key_count: 2
  name: Trustradius List Products Example
  slug: trustradius-list-products-example
finops:
- name: Trustradius Finops
  service_category: B2B Software Reviews
  slug: trustradius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustradius.png
json_schemas:
- name: TrustRadius Product
  property_count: 10
  slug: trustradius-product
- name: TrustRadius Review
  property_count: 12
  slug: trustradius-review
json_structures:
- name: Trustradius Review Structure
  property_count: 0
  slug: trustradius-review-structure
jsonld:
- class_count: 9
  name: Trustradius Context
  property_count: 22
  slug: trustradius-context
layout: provider
modified: '2026-05-19'
name: TrustRadius
nav: Providers
network: true
overview: 'TrustRadius publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Companies API, Products API, and 1 more. Tagged areas include B2B Software Reviews, Buyer Intelligence, Intent Data, Software Reviews, and Reviews.


  The TrustRadius catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TrustRadius'' developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Trustradius Plans Pricing
  plan_count: 1
  slug: trustradius-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 1
  name: Trustradius Rate Limits
  slug: trustradius-rate-limits
rules:
- name: TrustRadius API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trustradius-jsonschema-spectral-rules
- name: TrustRadius API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: trustradius-rules
score:
  band: developing
  composite: 50.9
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/screenshots/trustradius-2026-06-20T195813.png
security:
- kind: authentication
  name: Trustradius Authentication
  slug: trustradius-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trustradius Domain Security
  slug: trustradius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trustradius
tags:
- B2B Software Reviews
- Buyer Intelligence
- Intent Data
- Software Reviews
- Reviews
- Product Reviews
- Categories
website: https://www.trustradius.com/
---
