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
- description: Deterministic market-state engine API providing market readings and signals.
  name: Decker Public API
  slug: decker-public-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/decker-ai-com/conformance/decker-ai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decker-ai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decker-ai-com/llms/decker-ai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decker-ai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/decker-ai-com/hosts/decker-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decker-ai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/decker-ai-com/vendors/decker-ai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decker-ai-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/decker-ai-com/packages/decker-ai-com-packages.yml
  title: ''
  type: Packages
  url: packages/decker-ai-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decker-ai.com/legal/terms
- group: start
  title: ''
  type: SignUp
  url: https://decker-ai.com/register
- group: build
  title: ''
  type: SDKs
  url: https://github.com/gigshow/decker-ai/tree/main/sdk/python
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decker-ai.com/legal/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://api.decker-ai.com/docs
- group: auth
  href: https://artifacts.apis.io/decker-ai-com/security/decker-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decker-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decker-ai.com/
created: '2026-11-05'
description: Decker AI provides real‑time Korean stock market signals, trading strategies, and market data via a public REST API. The platform offers live briefings, watchlists, and AI‑driven insights for KRX listings, delivering JSON payloads for signals, positions, and market state. It also hosts an MCP server exposing tool integrations and webhook notifications.
image: https://decker-ai.com/logo.png
layout: provider
modified: '2026-11-05'
name: Decker AI
nav: Providers
network: true
overview: 'Decker AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Finance, Stock Market, and Real-Time.


  Decker AI''s developer surface includes signup flow, API reference, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Decker Ai Com Domain Security
  slug: decker-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: decker-ai-com
tags:
- Company
- Artificial Intelligence
- Finance
- Stock Market
- Real-Time
website: https://decker-ai.com/
---
