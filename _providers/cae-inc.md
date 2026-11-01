---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cae-inc/well-known/cae-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cae-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/cae-inc/hosts/cae-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cae-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/cae-inc/vendors/cae-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cae-inc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cae.com/terms-of-use-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cae.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.cae.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.cae.com/
- group: auth
  href: https://artifacts.apis.io/cae-inc/security/cae-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cae-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cae.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.cae.com/mcp
  - status: 200
    url: http://www.cae.com
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: CAE Inc. is a global leader in simulation and training solutions for civil aviation, defense, and healthcare. The company provides advanced modeling, virtual reality, and data analytics platforms that enable organizations to train personnel, design aircraft, and improve operational efficiency. With a focus on immersive technologies and real‑time data integration, CAE serves customers worldwide across aerospace, defense, and health sectors, delivering comprehensive training ecosystems and digital services.
layout: provider
modified: '2026-10-23'
name: CAE Inc.
nav: Providers
network: true
overview: 'CAE Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Defense, Healthcare, and Simulation.


  CAE Inc.''s developer surface includes engineering blog, documentation, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cae Inc Domain Security
  slug: cae-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cae-inc
tags:
- Company
- Aviation
- Defense
- Healthcare
- Simulation
- Training
website: https://www.cae.com
---
