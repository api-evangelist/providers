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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/claratech-ai/hosts/claratech-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claratech-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/claratech-ai/vendors/claratech-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claratech-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claratech.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://www.claratech.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claratech.ai/privacy
- group: auth
  href: https://artifacts.apis.io/claratech-ai/security/claratech-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claratech-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claratech.ai/
coverage:
  checked: '2026-11-03'
  detail: No public API documentation or machine‑readable contract was found on claratech.ai.
  evidence:
  - status: 200
    url: https://claratech.ai/
  reason: tenant-only
  state: none
created: '2026-11-03'
description: Clara is an AI-powered assistant designed specifically for mortgage brokers, streamlining the entire loan origination workflow. It captures every call, email, and document related to a deal, providing instant insights and automating repetitive tasks. By centralizing communication and data, Clara reduces deal review time from hours to minutes, improves accuracy, and enhances collaboration between brokers, lenders, and clients. The platform is accessible via desktop, mobile, and on‑the‑road, ensuring brokers stay productive wherever they work.
image: https://www.claratech.ai/assets/og-clara.png
layout: provider
modified: '2026-11-03'
name: Clara
nav: Providers
network: true
overview: 'Clara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Mortgage, Fintech, Assistant, and Brokerage.


  Clara''s developer surface includes support and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 8.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claratech Ai Domain Security
  slug: claratech-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: claratech-ai
tags:
- Artificial Intelligence
- Mortgage
- Fintech
- Assistant
- Brokerage
website: https://claratech.ai/
---
