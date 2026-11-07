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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bgpt-pro/plans/bgpt-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bgpt-pro-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/bgpt-pro/hosts/bgpt-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bgpt-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/bgpt-pro/vendors/bgpt-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bgpt-pro-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bgpt-pro/security/bgpt-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bgpt-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bgpt.pro/
- group: docs
  title: ''
  type: Documentation
  url: https://bgpt.pro/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bgpt.pro/privacy
- group: start
  title: ''
  type: SignUp
  url: https://bgpt.pro/signup
coverage:
  checked: '2026-11-02'
  detail: The provider's website offers only user login and signup pages with no public API documentation.
  evidence:
  - status: 200
    url: https://bgpt.pro/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: BGPT provides an evidence layer for scientific AI, linking claims to experiments, results, limitations, and sources. It enables researchers, clinicians, and AI builders to verify scientific statements with versioned records, offering subscription plans for individuals and API usage for AI tools. The platform aggregates new studies daily and supports detailed query interfaces.
image: https://bgpt.pro/static/art/bgpt_social.jpg
layout: provider
modified: '2026-11-02'
name: BGPT
nav: Providers
network: true
overview: 'BGPT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Scientific, Evidence, Research, and Data.


  BGPT''s developer surface includes documentation, signup flow, and 6 more developer resources.'
plans:
- name: Bgpt Pro Plans Pricing
  plan_count: 2
  slug: bgpt-pro-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bgpt Pro Domain Security
  slug: bgpt-pro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bgpt-pro
tags:
- Artificial Intelligence
- Scientific
- Evidence
- Research
- Data
website: https://bgpt.pro/
---
