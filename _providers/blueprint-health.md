---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/blueprint-health/plans/blueprint-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blueprint-health-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blueprint.ai/
- group: auth
  href: https://artifacts.apis.io/blueprint-health/well-known/blueprint-health-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blueprint-health-status-security.txt
- group: auth
  href: https://artifacts.apis.io/blueprint-health/well-known/blueprint-health-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blueprint-health-help-security.txt
- group: agent
  href: https://artifacts.apis.io/blueprint-health/well-known/blueprint-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blueprint-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/blueprint-health/hosts/blueprint-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blueprint-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/blueprint-health/vendors/blueprint-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blueprint-health-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.blueprint.ai/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blueprint-health.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueprint.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blueprint.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://help.blueprint-health.com/
- group: auth
  href: https://artifacts.apis.io/blueprint-health/security/blueprint-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blueprint-health-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/blueprint-health/security/blueprint-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blueprint-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blueprint-health.com
coverage:
  checked: '2026-10-22'
  detail: Documentation is available at https://help.blueprint.ai/en/ but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract was found.
  evidence:
  - status: 200
    url: https://help.blueprint.ai/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Blueprint Health provides an AI‑powered assistant platform for therapists, helping with clinical documentation, administrative tasks, and patient care. The solution integrates with existing electronic health record (EHR) systems or can be used as a standalone all‑in‑one EHR, delivering automated note‑taking, billing support, and workflow automation to improve efficiency and reduce burnout among mental‑health professionals.
image: https://cdn.prod.website-files.com/66d8ac88a5a4db1eb8930999/6a760ce2769e7f93413fedb3_OpenGraph_Aug2026.png
layout: provider
modified: '2026-10-21'
name: Blueprint Health
nav: Providers
network: true
overview: 'Blueprint Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HealthTech, AI, Therapy, SaaS, and MentalHealth.


  Blueprint Health''s developer surface includes support, pricing, documentation, and 12 more developer resources.'
plans:
- name: Blueprint Health Plans Pricing
  plan_count: 3
  slug: blueprint-health-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blueprint Health Domain Security
  slug: blueprint-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blueprint Health Trust Center
  slug: blueprint-health-trust-center
  summary_line: SOC 2, HIPAA
slug: blueprint-health
tags:
- HealthTech
- AI
- Therapy
- SaaS
- MentalHealth
website: https://blueprint-health.com
---
