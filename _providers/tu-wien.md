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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Public REST API of the TU Wien Research Data repository, built on InvenioRDM. Provides programmatic access to records, metadata, search and file content. Read operations such as retrieving and searchi
  name: TU Wien Research Data REST API
  slug: researchdata-api
- description: OAI-PMH metadata harvesting interface for the TU Wien Research Data repository (InvenioRDM), supporting standard verbs such as Identify, ListRecords and GetRecord for harvesting dataset metadata.
  name: TU Wien Research Data OAI-PMH
  slug: researchdata-oai
- description: OAI-PMH metadata harvesting interface for reposiTUm, the open-access institutional repository of TU Wien, implemented on DSpace-CRIS by Campus IT. Exposes metadata for scientific documents, theses, re
  name: reposiTUm OAI-PMH
  slug: repositum-oai
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tu-wien-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-wien-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tuwien.at/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tuwien-csd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tuwien
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-wien-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-wien-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-wien-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'TU Wien (Vienna University of Technology, TU Wien) is Austria''s largest science and technology university, founded in 1815, with more than 30,000 students and eight faculties. It is ranked #190 in the QS World University Rankings 2025. Its public, documented developer footprint centers on research infrastructure: the TU Wien Research Data repository exposes a public REST API and an OAI-PMH interface built on InvenioRDM, and the reposiTUm open-access institutional repository (DSpace-CRIS) exposes OAI-PMH for metadata harvesting. Several departmental GitHub organizations publish open-source code, but there is no single unified, public developer portal for the university as a whole.'
finops:
- name: Tu Wien Finops
  service_category: Education
  slug: tu-wien-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-wien.png
jsonld:
- class_count: 16
  name: Tu Wien Context
  property_count: 5
  slug: tu-wien-context
layout: provider
modified: '2026-06-03'
name: TU Wien
nav: Providers
network: true
overview: 'TU Wien publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The TU Wien catalog on APIs.io includes 1 JSON-LD context.


  TU Wien''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Tu Wien Plans Pricing
  plan_count: 2
  slug: tu-wien-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: Tu Wien Rate Limits
  slug: tu-wien-rate-limits
score:
  band: emerging
  composite: 19.8
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tu-wien/refs/heads/main/screenshots/tu-wien-2026-06-20T195820.png
security:
- kind: domain-security
  name: Tu Wien Domain Security
  slug: tu-wien-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tu Wien Vulnerability Disclosure
  slug: tu-wien-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tu-wien
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Repository
- OAI-PMH
- InvenioRDM
- Austria
- Europe
website: https://www.tuwien.at/en/
---
