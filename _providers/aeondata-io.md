---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aeondata-io/plans/aeondata-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeondata-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/aeondata-io/security/aeondata-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aeondata-io-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/aeondata-io/llms/aeondata-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeondata-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/aeondata-io/well-known/aeondata-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeondata-io-security.txt
- group: agent
  href: https://artifacts.apis.io/aeondata-io/well-known/aeondata-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeondata-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aeondata-io/hosts/aeondata-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aeondata-io-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://aeondata.io/signin
- group: auth
  href: https://artifacts.apis.io/aeondata-io/security/aeondata-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aeondata-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aeondata-io/security/aeondata-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeondata-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeondata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://aeondata.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://aeondata.io/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://aeondata.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://aeondata.io/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeondata.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeondata.io/privacy
- group: operate
  title: ''
  type: Contact
  url: https://aeondata.io/contact
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on the API host.
  evidence:
  - status: 0
    url: https://api.aeondata.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Aeon provides real-time, plain‑language data on insider trades, congressional transactions, fund holdings and federal contracts. Pull JSON feeds or use the API to get up‑to‑date filings from SEC, House, Senate, White House and USAspending sources. Free tier offers 500 daily requests, with paid plans for higher volume and faster latency. The service aims to make complex financial disclosures accessible to developers, analysts and AI assistants.
image: https://aeondata.io/og.png?v=1
layout: provider
modified: '2026-10-31'
name: Aeon
nav: Providers
network: true
overview: 'Aeon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Data, Insider Trading, and Government.


  Aeon''s developer surface includes documentation, API reference, pricing, and 14 more developer resources.'
plans:
- name: Aeondata Io Plans Pricing
  plan_count: 5
  slug: aeondata-io-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 39.3
    operational_transparency: 18.4
  previous_composite: 28.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeondata Io Domain Security
  slug: aeondata-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aeondata Io Vulnerability Disclosure
  slug: aeondata-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aeondata-io
tags:
- Finance
- Data
- Insider Trading
- Government
website: https://aeondata.io/
---
