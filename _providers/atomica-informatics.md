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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://atomicainformatics.com/
- group: company
  title: ''
  type: About
  url: https://www.atomicainformatics.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.atomicainformatics.com/archetypical
- group: company
  title: ''
  type: BlogRSS
  url: https://www.atomicainformatics.com/archetypical?format=rss
- group: operate
  title: ''
  type: Contact
  url: https://www.atomicainformatics.com/contact
- group: learn
  title: ''
  type: Training
  url: https://www.atomicainformatics.com/training-options
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atomica-informatics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atomica-informatics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/atomica-informatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atomica-informatics-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: Atomica Informatics is a single-practitioner openEHR clinical-modelling consultancy and training practice run by Dr Heather Leslie on a Squarespace marketing site - it sells workshops, mentoring and data-design advice, not software, so /openapi.json, /graphql and both agent-card paths all return the site's 404 page and there is no developer portal, SDK or GitHub organisation to find.
  evidence:
  - status: 404
    url: https://www.atomicainformatics.com/openapi.json
  - status: 404
    url: https://www.atomicainformatics.com/graphql
  - status: 404
    url: https://www.atomicainformatics.com/.well-known/agent-card.json
  - status: 404
    url: https://www.atomicainformatics.com/.well-known/api-catalog
  - status: 404
    url: https://github.com/atomicainformatics
  - status: 200
    url: https://www.atomicainformatics.com/training-options
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'Atomica Informatics is an independent health-informatics consultancy founded and run by Dr Heather Leslie, specialising in what it calls "little data" design: the modelling of atomic clinical data so that individual data points carry consistent format and reliable meaning across projects, domains and systems instead of being locked into single-purpose silos. The practice delivers openEHR archetype and template authoring, clinical knowledge governance, clinician engagement, and openEHR clinical-modelling training - a two-day introductory course, advanced modelling workshops, and ongoing remote mentoring for in-house modelling teams. Dr Leslie pioneered the openEHR clinical modelling methodology in volunteer roles at the openEHR Foundation from 2006 and co-leads its Clinical Program. Atomica Informatics operates no API of its own; the machine-readable standards its work depends on are published by the openEHR Foundation.'
image: https://static1.squarespace.com/static/5a9bab4675f9eef8f485b10a/t/5aaba2e21ae6cf1e32417039/1521197795190/favicon.png?format=1500w
layout: provider
modified: '2026-09-02'
name: Atomica Informatics
nav: Providers
network: true
overview: 'Atomica Informatics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Health Informatics, and Clinical Data.


  Atomica Informatics'' developer surface includes engineering blog, training material, and 8 more developer resources.'
plans:
- name: Atomica Informatics Plans Pricing
  plan_count: 0
  slug: atomica-informatics-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Atomica Informatics Rate Limits
  slug: atomica-informatics-rate-limits
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Atomica Informatics Domain Security
  slug: atomica-informatics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atomica-informatics
tags:
- Company
- Health
- Healthcare
- Health Informatics
- Clinical Data
- openEHR
- Interoperability
- Data Modeling
- Consulting
- Training
website: https://atomicainformatics.com/
---
