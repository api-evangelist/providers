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
- acting_count: 8
  human_in_the_loop: 0
  name: Tremendous Agentic Access
  operation_count: 22
  slug: tremendous-agentic-access
  summary_line: 22 operations · 8 acting
api_count: 9
apis:
- description: Manage reward presentation and product catalogs
  name: Tremendous Campaigns API
  slug: tremendous-campaigns-api
- description: Manage funding sources for sending rewards
  name: Tremendous Funding Sources API
  slug: tremendous-funding-sources-api
- description: View and manage invoices
  name: Tremendous Invoices API
  slug: tremendous-invoices-api
- description: Manage organization members
  name: Tremendous Members API
  slug: tremendous-members-api
- description: Create and manage reward orders
  name: Tremendous Orders API
  slug: tremendous-orders-api
- description: Manage organizations (team accounts)
  name: Tremendous Organizations API
  slug: tremendous-organizations-api
- description: Browse available payout products and gift cards
  name: Tremendous Products API
  slug: tremendous-products-api
- description: Manage individual rewards within orders
  name: Tremendous Rewards API
  slug: tremendous-rewards-api
- description: Configure webhook notifications
  name: Tremendous Webhooks API
  slug: tremendous-webhooks-api
artifact_total: 25
collections:
- collection_type: open
  name: Tremendous API
  slug: open-tremendous-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tremendous-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tremendous-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tremendous-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tremendous-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tremendous-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tremendous-rewards
- group: company
  title: ''
  type: Website
  url: https://www.tremendous.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tremendous.com/
- group: start
  title: ''
  type: Signup
  url: https://app.tremendous.com/auth/sign_up
- group: start
  title: ''
  type: Sandbox
  url: https://testflight.tremendous.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tremendous-rewards
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tremendous-rewards/tremendous-node
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.tremendous.com/changelog
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tremendous-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tremendous-product-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tremendous-order-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tremendous-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/tremendous-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tremendous-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.tremendous.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.tremendous.com/blog
created: '2025-02-08'
description: Tremendous allows businesses to send rewards, incentives, and payouts worldwide using their simple API and dashboard. Access 2000+ payout methods including US and global bank transfers, Amazon.com gift cards, Visa and Mastercard prepaid cards, PayPal, Venmo, and charity donations. Supports multi-product rewards (recipient choice) and single-product rewards.
examples:
- key_count: 2
  name: Tremendous Create Order Example
  slug: tremendous-create-order-example
finops:
- name: Tremendous Finops
  service_category: API
  slug: tremendous-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tremendous.png
json_schemas:
- name: Tremendous Order
  property_count: 6
  slug: tremendous-order
- name: Tremendous Product
  property_count: 7
  slug: tremendous-product
json_structures:
- name: Tremendous Order Structure
  property_count: 0
  slug: tremendous-order-structure
jsonld:
- class_count: 21
  name: Tremendous Context
  property_count: 16
  slug: tremendous-context
layout: provider
modified: '2026-05-19'
name: Tremendous
nav: Providers
network: true
overview: 'Tremendous publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Funding Sources API, Invoices API, and 6 more. Tagged areas include Employee Incentives, Global Payouts, Incentives, Market Research, and Payouts.


  The Tremendous catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tremendous'' developer surface includes authentication, documentation, signup flow, sandbox, changelog, engineering blog, and 15 more developer resources.'
plans:
- name: Tremendous Plans Pricing
  plan_count: 3
  slug: tremendous-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Tremendous Rate Limits
  slug: tremendous-rate-limits
rules:
- name: Tremendous API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tremendous-jsonschema-spectral-rules
- name: Tremendous API Rules
  rule_count: 20
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 13
  slug: tremendous-spectral-rules
scopes:
- name: Tremendous Scopes
  scope_count: 3
  slug: tremendous-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 55.2
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.2
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tremendous/refs/heads/main/screenshots/tremendous-2026-06-20T195654.png
security:
- kind: authentication
  name: Tremendous Authentication
  slug: tremendous-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Tremendous Domain Security
  slug: tremendous-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tremendous Vulnerability Disclosure
  slug: tremendous-vulnerability-disclosure
  summary_line: disclosure policy published
slug: tremendous
tags:
- Employee Incentives
- Global Payouts
- Incentives
- Market Research
- Payouts
- Rewards
website: https://www.tremendous.com/
---
