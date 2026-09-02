---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eql.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.eql.com/
- group: start
  title: ''
  type: Login
  url: https://portal.eql.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eql.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.eql.com/news
- group: operate
  title: ''
  type: Support
  url: https://support.eql.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vault.pactsafe.io/s/762ea5a7-e5e0-43bd-a023-6de504198d51/sjgeaocwel.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.eql.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.eql.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://eql.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://www.eql.com/legal/responsible-disclosure-policy
- group: other
  title: ''
  type: ShopifyApp
  url: https://apps.shopify.com/eql-launches
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eql-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/eql-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eql-vulnerability-disclosure.yml
created: '2026-07-17'
description: EQL is the infrastructure behind fair launches for high-demand, limited-supply products — sneakers, collectibles, art, coins, alcohol, trading cards, and brand collaborations. Every EQL launch is certified Run Fair®, combining bot mitigation, resilient infrastructure, and fair allocation to put products in the hands of genuine fans instead of bots and resellers. The platform serves brands and retailers who run launches (including a native Shopify app) and the fans who enter for a shot at products, providing queue-free entry, real-time launch data, payment capture, audience/allocation controls, and secondary-sale opportunities. Brands running launches on EQL include Nike, Crocs, Funko, Foot Locker, Undefeated, and Stanley. EQL is based in Melbourne, Australia.
image: https://cdn.prod.website-files.com/6899a9ebdcf39f5ff0aa276d/68e67286cfc4d1e0d8c16aa7_app-icon.png
layout: provider
modified: '2026-07-19'
name: EQL
nav: Providers
network: true
overview: 'EQL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Product Launches, and Bot Mitigation.


  EQL''s developer surface includes developer portal, pricing, engineering blog, support, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 22.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eql/refs/heads/main/screenshots/eql-2026-07-25T213535.png
security:
- kind: domain-security
  name: Eql Domain Security
  slug: eql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eql Vulnerability Disclosure
  slug: eql-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Eql Trust Center
  slug: eql-trust-center
  summary_line: SOC 2 Type 2, PCI DSS, ISO 27001
slug: eql
tags:
- Company
- Commerce
- E-Commerce
- Product Launches
- Bot Mitigation
- Fraud Prevention
- Retail
- Shopify
- Queue Management
- Fair Allocation
website: https://www.eql.com/
---
