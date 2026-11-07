---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AIData.Broker provides data marketplace pricing and buyer information via JSON endpoints.
  name: AIData.Broker API
  slug: aidata-broker-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aidata-broker/llms/aidata-broker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidata-broker-llms.txt
- group: other
  href: https://artifacts.apis.io/aidata-broker/hosts/aidata-broker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidata-broker-hosts.yml
- group: other
  href: https://artifacts.apis.io/aidata-broker/vendors/aidata-broker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aidata-broker-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aidata-broker/security/aidata-broker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidata-broker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidata.broker
- group: docs
  title: ''
  type: Documentation
  url: https://aidata.broker/datasets
- group: company
  title: ''
  type: Blog
  url: https://aidata.broker/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aidata.broker/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidata.broker/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidata.broker/legal/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://aidata.broker/about
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://aidata.broker/mcp
  - status: 200
    url: https://aidata.broker
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: AIData.Broker provides an open data marketplace for AI training data, offering pricing, buyer information, and deal records. It aggregates public price observations across data types such as images, video, code, and text, enabling companies to discover the value of their data and connect with AI labs interested in purchasing it. The platform also supplies tools for valuation, negotiation, and compliance, aiming to streamline data sales for enterprises.
image: https://aidata.broker/opengraph-image
layout: provider
modified: '2026-10-15'
name: AIData.Broker open data API
nav: Providers
network: true
overview: 'AIData.Broker open data API is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Marketplace, AI Training, Pricing, and Buyers.


  AIData.Broker open data API''s developer surface includes documentation, engineering blog, pricing, getting-started guide, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 17.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aidata-broker/aidata-broker-2026-11-03T120456.png
security:
- kind: domain-security
  name: Aidata Broker Domain Security
  slug: aidata-broker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aidata-broker
tags:
- Company
- Data Marketplace
- AI Training
- Pricing
- Buyers
website: https://aidata.broker
---
