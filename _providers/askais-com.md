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
- description: API for AskAI platform providing AI chat services
  name: AskAI API
  slug: askai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/askais-com/plans/askais-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askais-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/askais-com/changelog/askais-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/askais-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/askais-com/llms/askais-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askais-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/askais-com/well-known/askais-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askais-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askais-com/hosts/askais-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askais-com-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://askais.com/en/changelog
- group: auth
  href: https://artifacts.apis.io/askais-com/security/askais-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askais-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askais.com/
- group: docs
  title: ''
  type: Documentation
  url: https://askais.com/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://askais.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://askais.com/en/blog
- group: start
  title: ''
  type: SignUp
  url: https://askais.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://askais.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askais.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askais.com/en/privacy
coverage:
  checked: '2026-11-01'
  detail: Docs are served as JavaScript‑rendered pages, no machine‑readable spec was found.
  evidence:
  - status: 404
    url: https://api.askais.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: MiniCode LLC, operating under the brand telmini, provides AI-powered live chat and customer support solutions for websites and apps. Their platform combines AI-driven automated responses with human takeover, ensuring quick, multilingual assistance. MiniCode emphasizes data privacy, secure encryption, and isolated workspaces, serving businesses of all sizes with flexible pricing plans and a free tier for small teams.
image: https://telmini.com/en/opengraph-image
layout: provider
modified: '2026-11-01'
name: MiniCode LLC
nav: Providers
network: true
overview: 'MiniCode LLC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Service, Live Chat, Multilingual, and Software-as-a-Service.


  MiniCode LLC''s developer surface includes changelog, documentation, pricing, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Askais Com Plans Pricing
  plan_count: 3
  slug: askais-com-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 25.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askais Com Domain Security
  slug: askais-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askais-com
tags:
- Artificial Intelligence
- Customer Service
- Live Chat
- Multilingual
- Software-as-a-Service
website: https://askais.com/
---
