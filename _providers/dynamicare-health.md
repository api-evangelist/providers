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
- description: DynamiCare Health provides a digital therapeutics platform; API details are not publicly documented.
  name: DynamiCare Health API
  slug: dynamicare-health-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dynamicare-health/plans/dynamicare-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamicare-health-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/dynamicare-health/hosts/dynamicare-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynamicare-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/dynamicare-health/vendors/dynamicare-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynamicare-health-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dynamicarehealth.com/pricing
- group: auth
  href: https://artifacts.apis.io/dynamicare-health/security/dynamicare-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamicare-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dynamicarehealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynamicarehealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynamicarehealth.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.dynamicarehealth.com/news
coverage:
  checked: '2026-10-24'
  detail: Pricing page provides only HTML documentation with no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://www.dynamicarehealth.com/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: DynamiCare Health provides technology solutions for substance use recovery, offering digital therapeutics, contingency management, and support tools for individuals, families, and health plans. Their platform integrates evidence‑based interventions, insurance navigation, and outcome tracking to improve recovery outcomes.
image: http://static1.squarespace.com/static/5bfc6a4db98a78e1c648c1bd/t/62ea0b966e6ec602d25c874d/1761931210827/Dynamicare-OpenGraph-Image.jpg?format=1500w
layout: provider
modified: '2026-10-24'
name: DynamiCare Health
nav: Providers
network: true
overview: 'DynamiCare Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Digital Therapeutics, SubstanceUseRecovery, Health Tech, and Mental Health.


  DynamiCare Health''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Dynamicare Health Plans Pricing
  plan_count: 5
  slug: dynamicare-health-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dynamicare-health/dynamicare-health-2026-11-03T131140.png
security:
- kind: domain-security
  name: Dynamicare Health Domain Security
  slug: dynamicare-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dynamicare-health
tags:
- Health
- Digital Therapeutics
- SubstanceUseRecovery
- Health Tech
- Mental Health
website: https://www.dynamicarehealth.com/
---
