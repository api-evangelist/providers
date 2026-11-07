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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/charune-com/plans/charune-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/charune-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/charune-com/hosts/charune-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charune-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/charune-com/vendors/charune-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/charune-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/charune-com/security/charune-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charune-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charune.com/
- group: docs
  title: ''
  type: Documentation
  url: https://charune.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://charune.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://charune.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://charune.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://charune.com/faq
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on api.charune.com.
  evidence:
  - status: 0
    url: https://api.charune.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: 'charune-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://charune.com/og/home.jpg
layout: provider
modified: '2026-11-03'
name: Charune
nav: Providers
network: true
overview: 'Charune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Charune''s developer surface includes documentation, pricing, support, and 7 more developer resources.'
plans:
- name: Charune Com Plans Pricing
  plan_count: 4
  slug: charune-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 29.0
    catalog_earned_first_party: 12.0
    catalog_gap: 86.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Charune Com Domain Security
  slug: charune-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: charune-com
tags:
- Company
website: https://charune.com/
---
