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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aggreigator-com/plans/aggreigator-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aggreigator-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/aggreigator-com/security/aggreigator-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aggreigator-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aggreigator-com/well-known/aggreigator-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aggreigator-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aggreigator-com/well-known/aggreigator-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aggreigator-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aggreigator-com/hosts/aggreigator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aggreigator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aggreigator-com/vendors/aggreigator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aggreigator-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://aggreigator.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aggreigator.com/
- group: auth
  href: https://artifacts.apis.io/aggreigator-com/security/aggreigator-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aggreigator-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aggreigator-com/security/aggreigator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aggreigator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aggreigator.com/
- group: company
  title: ''
  type: Blog
  url: https://aggreigator.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aggreigator.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://aggreigator.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aggreigator.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aggreigator.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Documentation pages return JavaScript-rendered error shells preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://docs.aggreigator.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AggREIgator is a software platform for real estate wholesalers, offering tools to calculate ARV, MAO, exit strategies, and manage deals from offer to assignment. The portal provides free calculators, pricing plans, and a marketplace for investors, supporting operations across many US states while ensuring compliance and providing extensive documentation and support resources.
layout: provider
modified: '2026-11-01'
name: AggREIgator
nav: Providers
network: true
overview: 'AggREIgator is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Wholesaling, Platform, Tools, and Finance.


  AggREIgator''s developer surface includes documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Aggreigator Com Plans Pricing
  plan_count: 5
  slug: aggreigator-com-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 44.6
    operational_transparency: 10.5
  previous_composite: 25.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aggreigator Com Domain Security
  slug: aggreigator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aggreigator Com Vulnerability Disclosure
  slug: aggreigator-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aggreigator-com
tags:
- Real Estate
- Wholesaling
- Platform
- Tools
- Finance
website: https://aggreigator.com/
---
