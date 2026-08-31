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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: REDU (Repositório de Dados de Pesquisa da Unicamp) is Unicamp's institutional research data repository running on Dataverse 6.0. It exposes the standard Dataverse REST API, including a public Search A
  name: REDU Dataverse Native & Search API
  slug: redu-dataverse-api
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for REDU, the Unicamp Research Data Repository. Confirmed live: verb=Identify returns the repository "Repositório de Dados de Pesquisa da Unicamp Dataverse OAI'
  name: REDU OAI-PMH Metadata Endpoint
  slug: redu-oai-pmh
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unicamp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unicamp.br/
- group: company
  title: ''
  type: LinkedIn
  url: https://br.linkedin.com/school/universidade-estadual-de-campinas/
- group: commercial
  title: ''
  type: Plans
  url: plans/unicamp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unicamp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unicamp-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Campinas (Universidade Estadual de Campinas, Unicamp) is a public research university in Campinas, São Paulo, Brazil, ranked #232 in the QS World University Rankings 2025. Its most visible public, machine-readable API footprint is REDU, the Unicamp Research Data Repository, which runs on the open-source Dataverse 6.0 platform and exposes a documented Native/Search API and an OAI-PMH metadata endpoint. Institutional data products are otherwise delivered through dashboards and gated portals (EDAT / dados.unicamp.br) and library discovery systems rather than a unified public developer portal.'
finops:
- name: Unicamp Finops
  service_category: Education
  slug: unicamp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unicamp.png
jsonld:
- class_count: 10
  name: Unicamp Context
  property_count: 4
  slug: unicamp-context
layout: provider
modified: '2026-06-03'
name: University of Campinas
nav: Providers
network: true
overview: 'University of Campinas publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Campinas catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Unicamp Plans Pricing
  plan_count: 2
  slug: unicamp-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Unicamp Rate Limits
  slug: unicamp-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unicamp/refs/heads/main/screenshots/unicamp-2026-06-20T200024.png
security:
- kind: domain-security
  name: Unicamp Domain Security
  slug: unicamp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: unicamp
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Brazil
website: https://www.unicamp.br/
---
