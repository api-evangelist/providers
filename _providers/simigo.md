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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simigo/refs/heads/main/hosts/simigo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simigo-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simigo/refs/heads/main/security/simigo-domain-security.yml
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
random_paper: 10
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
