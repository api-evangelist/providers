---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/simigo/hosts/simigo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simigo-hosts.yml
- group: auth
  href: https://artifacts.apis.io/simigo/security/simigo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simigo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://partners.simigo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.simigo.ai/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.simigo.ai/api-docs/
created: '2026-10-05'
description: Simigo by Telmobil Inc provides a vendor API platform for resellers to integrate telecom services. The platform offers endpoints under /v1/reseller/* for operations such as checking reseller balances, managing customers, and provisioning services. Hosted at api.simigo.ai with Swagger UI documentation, the service targets partners and developers needing programmatic access to Telmobil’s telecom offerings. The company is part of Telmobil Inc and focuses on enabling automated telecom workflows via RESTful APIs.
layout: provider
modified: '2026-10-05'
name: Simigo by Telmobil Inc
nav: Providers
network: true
overview: 'Simigo by Telmobil Inc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Platform, Reseller, and Telmobil.


  Simigo by Telmobil Inc''s developer surface includes documentation, API reference, and 3 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 4.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/simigo/simigo-2026-11-03T143215.png
security:
- kind: domain-security
  name: Simigo Domain Security
  slug: simigo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: simigo
tags:
- Telecommunications
- Platform
- Reseller
- Telmobil
website: https://partners.simigo.ai/
---
