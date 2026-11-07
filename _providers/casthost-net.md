---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/casthost-net/plans/casthost-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/casthost-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/casthost-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/casthost-net/llms/casthost-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/casthost-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/casthost-net/well-known/casthost-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/casthost-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/casthost-net/hosts/casthost-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casthost-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/casthost-net/vendors/casthost-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/casthost-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.casthost.net/terms_and_conditions.php
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.casthost.net/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.casthost.net/privacy.php
- group: commercial
  title: ''
  type: Pricing
  url: https://www.casthost.net/pricing.php
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.casthost.net/
- group: company
  title: ''
  type: Blog
  url: https://www.casthost.net/blog/
- group: auth
  href: https://artifacts.apis.io/casthost-net/security/casthost-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casthost-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://casthost.net/
coverage:
  checked: '2026-11-04'
  detail: The provider's developer portal only offers login pages and no public OpenAPI or other machine‑readable specifications.
  evidence:
  - status: 200
    url: https://api.casthost.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CastHost provides reliable internet radio hosting services, offering free Shoutcast and Icecast hosting with a 7‑day free trial, 24/7 expert support, and affordable plans. The platform also includes cPanel web hosting and mobile app development services, serving customers worldwide from its Canadian base.
image: https://www.casthost.net/images/newbanners/home-slide-stream.webp
layout: provider
modified: '2026-11-04'
name: CastHost
nav: Providers
network: true
overview: 'CastHost is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Internet Radio, Hosting, Shoutcast, Icecast, and cPanel.


  CastHost''s developer surface includes signup flow, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Casthost Net Plans Pricing
  plan_count: 18
  slug: casthost-net-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Casthost Net Domain Security
  slug: casthost-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: casthost-net
tags:
- Internet Radio
- Hosting
- Shoutcast
- Icecast
- cPanel
website: https://casthost.net/
---
