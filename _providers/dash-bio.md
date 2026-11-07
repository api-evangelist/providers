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
  href: https://artifacts.apis.io/dash-bio/plans/dash-bio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dash-bio-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/dash-bio/hosts/dash-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dash-bio-hosts.yml
- group: other
  href: https://artifacts.apis.io/dash-bio/vendors/dash-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dash-bio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dash-bio/security/dash-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dash-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dash.bio
- group: docs
  title: ''
  type: Documentation
  url: https://www.dash.bio/services
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dash.bio/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dash.bio/pricing
- group: operate
  title: ''
  type: Contact
  url: https://www.dash.bio/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dash.bio/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dash.bio/legal/terms-of-use
coverage:
  checked: '2026-10-22'
  detail: Access to OpenAPI spec at https://api.dash.bio/openapi.json is blocked with HTTP 403.
  evidence:
  - status: 403
    url: https://api.dash.bio/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Dash Bio is a technology-driven bioanalysis contract research organization (CRO) that provides automated, AI‑enhanced laboratory services to accelerate drug development. Leveraging robotics, integrated software, and transparent pricing, Dash Bio delivers high‑quality assay results in days rather than months, supporting preclinical to late‑stage clinical programs. The platform aims to modernize bioanalysis with speed, consistency, and guaranteed outcomes for biotech and pharmaceutical companies.
image: https://www.dash.bio/static/default.BXTuH9WZ_1BPyEa.webp
layout: provider
modified: '2026-10-22'
name: Dash Bio
nav: Providers
network: true
overview: 'Dash Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bioanalysis, CRO, Automation, and Artificial Intelligence.


  Dash Bio''s developer surface includes documentation, getting-started guide, pricing, and 8 more developer resources.'
plans:
- name: Dash Bio Plans Pricing
  plan_count: 19
  slug: dash-bio-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dash-bio/dash-bio-2026-11-03T130108.png
security:
- kind: domain-security
  name: Dash Bio Domain Security
  slug: dash-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dash-bio
tags:
- Company
- Bioanalysis
- CRO
- Automation
- Artificial Intelligence
website: https://www.dash.bio
---
