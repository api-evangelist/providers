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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: 'Public REST API of the FenixEdu academic information system operated by Instituto Superior Tecnico, a school of the University of Lisbon. Exposes institutional data including people, spaces, degrees, '
  name: FenixEdu Academic API (Instituto Superior Tecnico)
  slug: fenixedu-tecnico
- description: OAI-PMH 2.0 metadata harvesting interface for the DSpace-based institutional open-access repository (Repositorio Cientifico de Acesso Aberto da ULisboa), containing theses, dissertations, articles and
  name: Repositorio da Universidade de Lisboa OAI-PMH
  slug: repositorio-oai-pmh
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-lisbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ulisboa.pt/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ULisboa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidade-de-lisboa/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ULisboa
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-lisbon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-lisbon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-lisbon-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Lisbon (Universidade de Lisboa, ULisboa) is Portugal''s largest public university, based in Lisbon, and is ranked #260 in the QS World University Rankings 2025. Its public developer/API footprint is decentralized across its schools and services rather than offered through a single institutional developer portal. The most prominent programmable interfaces are the FenixEdu academic API operated by Instituto Superior Tecnico (tecnico.ulisboa.pt) and the OAI-PMH metadata interface of the DSpace institutional repository (repositorio.ulisboa.pt). The ULisboa GitHub organization publishes open-source Java libraries focused on Erasmus Without Paper (EWP) data exchange. There is no single self-service commercial API program; most interfaces are open metadata endpoints or affiliation-gated systems.'
finops:
- name: University Of Lisbon Finops
  service_category: Education
  slug: university-of-lisbon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-lisbon.png
jsonld:
- class_count: 36
  name: University Of Lisbon Context
  property_count: 5
  slug: university-of-lisbon-context
layout: provider
modified: '2026-06-03'
name: University of Lisbon
nav: Providers
network: true
overview: 'University of Lisbon publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Portugal, and Open Data.


  The University of Lisbon catalog on APIs.io includes 1 JSON-LD context.


  University of Lisbon''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Lisbon Plans Pricing
  plan_count: 2
  slug: university-of-lisbon-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 1
  name: University Of Lisbon Rate Limits
  slug: university-of-lisbon-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-lisbon/refs/heads/main/screenshots/university-of-lisbon-2026-06-20T200201.png
security:
- kind: domain-security
  name: University Of Lisbon Domain Security
  slug: university-of-lisbon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-lisbon
tags:
- Education
- Higher Education
- University
- Portugal
- Open Data
- Repository
- Metadata
website: https://www.ulisboa.pt/en
---
