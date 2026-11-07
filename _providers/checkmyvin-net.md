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
api_count: 1
apis:
- description: Free vehicle report by VIN using official NHTSA data.
  name: CheckMyVIN API
  slug: checkmyvin-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/checkmyvin-net/plans/checkmyvin-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/checkmyvin-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/checkmyvin-net/conformance/checkmyvin-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/checkmyvin-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/checkmyvin-net/llms/checkmyvin-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/checkmyvin-net-llms.txt
- group: other
  href: https://artifacts.apis.io/checkmyvin-net/hosts/checkmyvin-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/checkmyvin-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/checkmyvin-net/vendors/checkmyvin-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/checkmyvin-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://checkmyvin.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://checkmyvin.net/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://checkmyvin.net/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://checkmyvin.net/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://checkmyvin.net/docs/api
- group: auth
  href: https://artifacts.apis.io/checkmyvin-net/security/checkmyvin-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/checkmyvin-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://checkmyvin.net
created: '2026-10-27'
description: CheckMyVIN provides a free AI-powered VIN decoder for US‑market vehicles, delivering official NHTSA specifications, open recall data, and detailed vehicle information from any 17‑character VIN. The service is worldwide, offers printable reports, and includes optional paid briefings for deeper recall interpretation, while keeping core safety‑critical data freely accessible without sign‑up or email gating.
image: https://checkmyvin.net/og/default.png
layout: provider
modified: '2026-10-27'
name: CheckMyVIN
nav: Providers
network: true
overview: 'CheckMyVIN is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VIN, Automotive, NHTSA, and Free.


  CheckMyVIN''s developer surface includes pricing, documentation, API reference, and 9 more developer resources.'
plans:
- name: Checkmyvin Net Plans Pricing
  plan_count: 3
  slug: checkmyvin-net-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/checkmyvin-net/checkmyvin-net-2026-11-03T123930.png
security:
- kind: domain-security
  name: Checkmyvin Net Domain Security
  slug: checkmyvin-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: checkmyvin-net
tags:
- Company
- VIN
- Automotive
- NHTSA
- Free
website: https://checkmyvin.net
---
