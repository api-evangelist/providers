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
api_count: 1
apis:
- description: API for Dimetrics MCP and data services as documented
  name: Dimetrics API
  slug: dimetrics-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dimetrics-ai/plans/dimetrics-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dimetrics-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dimetrics-ai/llms/dimetrics-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dimetrics-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dimetrics-ai/well-known/dimetrics-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dimetrics-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dimetrics-ai/hosts/dimetrics-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dimetrics-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dimetrics-ai/vendors/dimetrics-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dimetrics-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dimetrics.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dimetrics.ai/privacy
- group: auth
  href: https://artifacts.apis.io/dimetrics-ai/security/dimetrics-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimetrics-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dimetrics.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dimetrics.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dimetrics.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.dimetrics.ai/signup?src=marketing-nav
- group: other
  title: ''
  type: SignIn
  url: https://www.dimetrics.ai/login
coverage:
  checked: '2026-11-05'
  detail: MCP documentation pages are rendered via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://www.dimetrics.ai/docs/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Dimetrics provides an analyst toolkit for the AI infrastructure buildout, covering lease and offtake underwriting, debt-per-lease pricing, capacity and dispersion screens, and county-level development risk, with every figure cited to SEC filings. It serves investors, allocators, and analysts seeking detailed data on AI compute infrastructure and related financial metrics.
layout: provider
modified: '2026-11-05'
name: Dimetrics
nav: Providers
network: true
overview: 'Dimetrics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Finance, Data Analytics, Infrastructure, and Investment.


  Dimetrics'' developer surface includes documentation, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Dimetrics Ai Plans Pricing
  plan_count: 2
  slug: dimetrics-ai-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dimetrics Ai Domain Security
  slug: dimetrics-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dimetrics-ai
tags:
- Artificial Intelligence
- Finance
- Data Analytics
- Infrastructure
- Investment
website: https://dimetrics.ai/
---
