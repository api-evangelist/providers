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
    agent_card: conformant
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
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AlgoTrada trading platform API (no public documentation found).
  name: AlgoTrada API
  slug: algotrada-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/algotrada-com/plans/algotrada-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algotrada-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/algotrada-com/llms/algotrada-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algotrada-com-llms.txt
- group: other
  href: https://artifacts.apis.io/algotrada-com/a2a/algotrada-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/algotrada-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/algotrada-com/well-known/algotrada-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algotrada-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/algotrada-com/hosts/algotrada-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algotrada-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/algotrada-com/vendors/algotrada-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algotrada-com-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.algotrada.com/cubicle/roadmap
- group: auth
  href: https://artifacts.apis.io/algotrada-com/security/algotrada-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algotrada-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algotrada.com/
- group: company
  title: ''
  type: Blog
  url: https://www.algotrada.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.algotrada.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.algotrada.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.algotrada.com/status
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine‑readable contract was found after probing standard contract URLs on all discovered hosts.
  evidence:
  - status: 6
    url: https://api.algotrada.com/openapi.json
  - status: 404
    url: https://cubicle.algotrada.com/openapi.json
  - status: 404
    url: https://www.algotrada.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: AlgoTrada builds trading technology for professional financial markets, offering a platform that connects to crypto exchanges, runs rule‑based strategies, and includes a kill‑switch to protect capital. The system supports multiple exchanges, provides tiered pricing, and operates as software‑as‑a‑service without custodial responsibilities. It emphasizes transparency, real‑time monitoring, and AI‑driven optimization, aiming to democratize algorithmic trading for both individual and institutional users.
image: https://algotrada.com/brand/logo/mark@512.png
layout: provider
modified: '2026-11-01'
name: AlgoTrada
nav: Providers
network: true
overview: 'AlgoTrada is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Cryptocurrency, Algorithmic Trading, Automation, and Software-as-a-Service.


  AlgoTrada''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Algotrada Com Plans Pricing
  plan_count: 3
  slug: algotrada-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 19.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 14.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Algotrada Com Domain Security
  slug: algotrada-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: algotrada-com
tags:
- Finance
- Cryptocurrency
- Algorithmic Trading
- Automation
- Software-as-a-Service
website: https://algotrada.com/
---
