---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Public DSpace 7.6.5 REST/HATEOAS API for uO Research (Recherche uO Research), the University of Ottawa's institutional repository. The API root reports dspaceVersion "DSpace 7.6.5" and dspaceName "Rec
  name: uO Research DSpace REST API
  slug: ruor-rest
- description: OAI-PMH 2.0 metadata-harvesting endpoint for uO Research. An Identify request confirms protocol version 2.0 and repository name "Recherche uO Research", supporting standard verbs (Identify, ListRecord
  name: uO Research OAI-PMH
  slug: ruor-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-ottawa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uottawa.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uottawa-wcms
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/uottawa/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-ottawa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-ottawa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-ottawa-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Ottawa (uOttawa) is a public bilingual research university in Ottawa, Ontario, Canada, and the largest English-French bilingual university in the world. It is ranked #189 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is concentrated in the library''s institutional repository, uO Research (Recherche uO Research), which runs on DSpace 7.6.5 and exposes both a public DSpace REST/HATEOAS API and an OAI-PMH 2.0 metadata-harvesting endpoint. uOttawa does not operate a single unified public developer portal; most enterprise and student-information systems are gated behind institutional SSO.'
finops:
- name: University Of Ottawa Finops
  service_category: Education
  slug: university-of-ottawa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-ottawa.png
jsonld:
- class_count: 17
  name: University Of Ottawa Context
  property_count: 14
  slug: university-of-ottawa-context
layout: provider
modified: '2026-06-03'
name: University of Ottawa
nav: Providers
network: true
overview: 'University of Ottawa publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Canada, and Bilingual.


  The University of Ottawa catalog on APIs.io includes 1 JSON-LD context.


  University of Ottawa''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: University Of Ottawa Plans Pricing
  plan_count: 2
  slug: university-of-ottawa-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: University Of Ottawa Rate Limits
  slug: university-of-ottawa-rate-limits
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-ottawa/refs/heads/main/screenshots/university-of-ottawa-2026-06-20T200215.png
security:
- kind: domain-security
  name: University Of Ottawa Domain Security
  slug: university-of-ottawa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-ottawa
tags:
- Education
- Higher Education
- University
- Canada
- Bilingual
- Library
- Institutional Repository
- DSpace
- OAI-PMH
- Open Access
website: https://www.uottawa.ca/
---
