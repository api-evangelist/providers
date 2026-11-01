---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Partner API for integrating with Lula's property maintenance platform.
  name: Lula Partner API
  slug: lula-partner-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/lula-life/llms/lula-life-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lula-life-llms.txt
- group: auth
  href: https://artifacts.apis.io/lula-life/well-known/lula-life-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lula-life-help-security.txt
- group: agent
  href: https://artifacts.apis.io/lula-life/well-known/lula-life-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lula-life-well-known.yml
- group: other
  href: https://artifacts.apis.io/lula-life/hosts/lula-life-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lula-life-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lula.life/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.lula.life/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lula.life/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://lula.life/login
- group: start
  title: ''
  type: GettingStarted
  url: https://lula.life/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.lula.life/
- group: auth
  href: https://artifacts.apis.io/lula-life/security/lula-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lula-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lula.life/
- group: company
  title: ''
  type: Blog
  url: https://lula.life/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lula.life/flat-rate-maintenance-price
coverage:
  checked: '2026-10-28'
  detail: Partner API page provides HTML documentation but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://lula.life/partner-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Lula provides end-to-end residential property maintenance for property managers, offering a vetted network of over 9,000 professionals, flat‑rate pricing, and coordinated work order management across more than 350,000 properties in 50+ U.S. markets. Their platform integrates with major property management systems and delivers real‑time job tracking, AI‑driven intake, and quality assurance, aiming to simplify maintenance operations for landlords and managers.
image: https://lula.life/wp-content/uploads/2025/09/lula_og.jpg
layout: provider
modified: '2026-10-28'
name: Lula (maintenance)
nav: Providers
network: true
overview: 'Lula (maintenance) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Management, Maintenance, Real Estate, and API.


  Lula (maintenance)''s developer surface includes support, getting-started guide, documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lula Life Domain Security
  slug: lula-life-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: lula-life
tags:
- Company
- Property Management
- Maintenance
- Real Estate
- API
website: https://lula.life/
---
