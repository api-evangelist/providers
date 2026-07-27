---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Triple Whale Agentic Access
  operation_count: 16
  slug: triple-whale-agentic-access
  summary_line: 16 operations · 15 acting
api_count: 4
apis:
- description: The API Keys API from Triple Whale — 1 operation(s) for api keys.
  name: Triple Whale API Keys API
  slug: triple-whale-api-keys-api
- description: The Compliance API from Triple Whale — 1 operation(s) for compliance.
  name: Triple Whale Compliance API
  slug: triple-whale-compliance-api
- description: The Data In API from Triple Whale — 10 operation(s) for data in.
  name: Triple Whale Data In API
  slug: triple-whale-data-in-api
- description: The Data Out API from Triple Whale — 4 operation(s) for data out.
  name: Triple Whale Data Out API
  slug: triple-whale-data-out-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/triple-whale-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/triple-whale-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triple-whale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/triple-whale-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.triplewhale.com
- group: docs
  title: ''
  type: Documentation
  url: https://triplewhale.readme.io/reference/introduction-to-the-triple-whale-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Triple-Whale
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triple-whale
- group: company
  title: ''
  type: Blog
  url: https://www.triplewhale.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.triplewhale.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.triplewhale.com
- group: other
  title: ''
  type: X
  url: https://x.com/triplewhale
- group: commercial
  title: ''
  type: Plans
  url: plans/triple-whale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/triple-whale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/triple-whale-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/triple-whale-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/triple-whale-context.jsonld
created: '2026-06-13'
description: E-commerce analytics and attribution platform for Shopify brands with a REST API for accessing pixel data, cohort analytics, creative metrics, and blended ROAS. Offers a two-way data highway with Data-In and Data-Out APIs supporting OAuth2 and API key authentication.
finops:
- name: Triple Whale Finops
  service_category: ''
  slug: triple-whale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triple-whale.png
json_schemas:
- name: Triple Whale Ad Record
  property_count: 10
  slug: triple-whale-ad
- name: Triple Whale Order
  property_count: 19
  slug: triple-whale-order
jsonld:
- class_count: 0
  name: Triple Whale Context
  property_count: 37
  slug: triple-whale-context
layout: provider
modified: '2026-06-13'
name: Triple Whale
nav: Providers
network: true
overview: 'Triple Whale publishes 4 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Compliance API, Data In API, and 1 more. Tagged areas include E-commerce, Analytics, Attribution, Shopify, and Pixel Tracking.


  The Triple Whale catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Triple Whale''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Triple Whale Plans Pricing
  plan_count: 4
  slug: triple-whale-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Triple Whale Rate Limits
  slug: triple-whale-rate-limits
rules:
- name: Triple Whale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: triple-whale-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.5
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 73.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 61.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triple-whale/refs/heads/main/screenshots/triple-whale-2026-06-20T195726.png
security:
- kind: authentication
  name: Triple Whale Authentication
  slug: triple-whale-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Triple Whale Domain Security
  slug: triple-whale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Triple Whale Trust Center
  slug: triple-whale-trust-center
  summary_line: SOC 2, GDPR
slug: triple-whale
tags:
- E-commerce
- Analytics
- Attribution
- Shopify
- Pixel Tracking
- ROAS
- DTC
- Marketing
website: https://www.triplewhale.com
---
