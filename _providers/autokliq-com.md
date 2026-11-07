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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/autokliq-com/plans/autokliq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autokliq-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://autokliq.com/privacy
- group: agent
  href: https://artifacts.apis.io/autokliq-com/llms/autokliq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autokliq-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/autokliq-com/well-known/autokliq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autokliq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/autokliq-com/well-known/autokliq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autokliq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/autokliq-com/hosts/autokliq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autokliq-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://autokliq.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://autokliq.com/changelog
- group: auth
  href: https://artifacts.apis.io/autokliq-com/security/autokliq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autokliq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autokliq-com/security/autokliq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autokliq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autokliq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://autokliq.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://autokliq.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autokliq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autokliq.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Provider documentation exists but no machine‑readable OpenAPI, AsyncAPI, GraphQL or gRPC spec was found.
  evidence:
  - status: 200
    url: https://autokliq.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: autokliq is an AI-powered YouTube thumbnail generator operated by Ipsum AI LLC. Founded by Korean creator Alex (careerhackeralex) with over 196k subscribers, the service automates thumbnail creation, title and hook generation, offering multiple style concepts per video. It aims to reduce creators’ production time by analyzing audience data and delivering ready‑to‑upload 16:9 thumbnails.
image: https://autokliq.com/opengraph-image
layout: provider
modified: '2026-11-02'
name: autokliq
nav: Providers
network: true
overview: 'autokliq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence and YouTube.


  autokliq''s developer surface includes changelog, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Autokliq Com Plans Pricing
  plan_count: 3
  slug: autokliq-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 39.3
    operational_transparency: 13.2
  previous_composite: 24.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autokliq Com Domain Security
  slug: autokliq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Autokliq Com Vulnerability Disclosure
  slug: autokliq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: autokliq-com
tags:
- Artificial Intelligence
- YouTube
website: https://autokliq.com/
---
