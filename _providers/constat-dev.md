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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Constat provides a searchable FDA AI/ML medical device evidence database via its API. Documentation is at https://constat.dev/guides.
  name: Constat API
  slug: constat-api
artifact_total: 3
common:
- group: operate
  title: ''
  type: Support
  url: https://constat.dev/support
- group: commercial
  href: https://artifacts.apis.io/constat-dev/plans/constat-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/constat-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/constat-dev/llms/constat-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/constat-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/constat-dev/hosts/constat-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constat-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/constat-dev/vendors/constat-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constat-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constat.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://constat.dev/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://constat.dev/guides
- group: auth
  href: https://artifacts.apis.io/constat-dev/security/constat-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constat-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constat.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://constat.dev/pricing
coverage:
  checked: '2026-11-04'
  detail: Guides page renders via JavaScript, preventing machine‑readable OpenAPI discovery.
  evidence:
  - status: 200
    url: https://constat.dev/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Constat provides a searchable database of FDA AI/ML medical device evidence, aggregating source‑linked information such as 510(k) predicates, validation studies, MAUDE reports, recalls, reimbursement pathways, warning letters, and Form 483s. Users can explore pre‑market and post‑deployment signals, compliance records, and regulatory insights across the FDA and CMS ecosystem, enabling better decision‑making for health AI product development and monitoring.
image: https://constat.dev/opengraph-image.png?ca701f0a45a4c426
layout: provider
modified: '2026-11-04'
name: Constat
nav: Providers
network: true
overview: 'Constat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health AI, FDA, Medical Devices, and Artificial Intelligence.


  Constat''s developer surface includes support, documentation, pricing, and 8 more developer resources.'
plans:
- name: Constat Dev Plans Pricing
  plan_count: 3
  slug: constat-dev-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constat Dev Domain Security
  slug: constat-dev-domain-security
  summary_line: TLSv1.3
slug: constat-dev
tags:
- Company
- Health AI
- FDA
- Medical Devices
- Artificial Intelligence
website: https://constat.dev/
---
