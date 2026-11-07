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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ChainFX provides a digital FX payments platform with tools and calculators; API details are documented on the website.
  name: ChainFX API
  slug: chainfx-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/chainfx-store/llms/chainfx-store-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainfx-store-llms.txt
- group: other
  href: https://artifacts.apis.io/chainfx-store/hosts/chainfx-store-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chainfx-store-hosts.yml
- group: auth
  href: https://artifacts.apis.io/chainfx-store/security/chainfx-store-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainfx-store-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chainfx.in/
- group: docs
  title: ''
  type: Documentation
  url: https://chainfx.in/about
- group: company
  title: ''
  type: Blog
  url: https://chainfx.in/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chainfx.in/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainfx.in/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://chainfx.in/contact
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://chainfx.in/about
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ChainFX Payments provides a digital FX payments platform enabling instant buying and selling of digital assets such as USDT and EURUSD with real-time PIX settlement. It offers a suite of free crypto and forex trading tools, fee calculators, and exchange comparisons, serving users in India, UAE, and globally. The service is web-based, free to use, and emphasizes transparency and security.
layout: provider
modified: '2026-11-03'
name: ChainFX Payments
nav: Providers
network: true
overview: 'ChainFX Payments is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Cryptocurrency, Foreign Exchange, and Tools.


  ChainFX Payments'' developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chainfx Store Domain Security
  slug: chainfx-store-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chainfx-store
tags:
- Fintech
- Payments
- Cryptocurrency
- Foreign Exchange
- Tools
website: https://chainfx.in/
---
