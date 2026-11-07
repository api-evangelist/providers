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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bootify provides a code generation tool for Spring Boot applications. Documentation is available at the provided docs pages.
  name: Bootify API
  slug: bootify-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bootify-io/plans/bootify-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bootify-io-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/bootify-io/hosts/bootify-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bootify-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bootify.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bootify.io/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://bootify.io/docs/
- group: auth
  href: https://artifacts.apis.io/bootify-io/security/bootify-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bootify-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bootify.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://bootify.io/pricing.html
- group: start
  title: ''
  type: GettingStarted
  url: https://bootify.io/quickstart.html
- group: other
  title: ''
  type: Image
  url: https://bootify.io/img/logo-bootify-io.webp
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are served as HTML shells requiring JavaScript rendering, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://bootify.io/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: 'bootify-io is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://bootify.io/img/home/spring-boot-entity-creation.png
layout: provider
modified: '2026-11-02'
name: Bootify
nav: Providers
network: true
overview: 'Bootify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Spring Boot, Code Generation, API Generation, Database Design, and Frontend Integration.


  Bootify''s developer surface includes documentation, pricing, getting-started guide, and 7 more developer resources.'
plans:
- name: Bootify Io Plans Pricing
  plan_count: 3
  slug: bootify-io-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
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
  name: Bootify Io Domain Security
  slug: bootify-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bootify-io
tags:
- Spring Boot
- Code Generation
- API Generation
- Database Design
- Frontend Integration
website: https://bootify.io/
---
