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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: HAL-based REST API for Biblos-e Archivo, the UAM institutional repository, running DSpace 7.6.5. Provides programmatic, HATEOAS-navigable access to communities, collections, items, bitstreams, search,
  name: Biblos-e Archivo REST API (DSpace 7)
  slug: biblos-rest
- description: OAI-PMH 2.0 metadata-harvesting endpoint for Biblos-e Archivo. Supports Identify, ListRecords, ListSets, and other standard OAI verbs for harvesting Dublin Core and other metadata formats from the UAM
  name: Biblos-e Archivo OAI-PMH Endpoint
  slug: biblos-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uam.es/
- group: company
  title: ''
  type: LinkedIn
  url: https://es.linkedin.com/school/universidad-autonoma-de-madrid/
- group: auth
  title: ''
  type: Authentication
  url: https://id.uam.es/
- group: commercial
  title: ''
  type: Plans
  url: plans/uam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Autonomous University of Madrid (Universidad Autónoma de Madrid, UAM) is a public research university in Madrid, Spain, founded in 1968 and ranked #198 in the QS World University Rankings 2025. Its primary public, machine-readable API footprint is delivered through Biblos-e Archivo, the UAM institutional repository running DSpace 7.6.5, which exposes a HAL-based REST API and an OAI-PMH 2.0 metadata-harvesting endpoint. UAM does not publish a centralized developer portal; authentication is handled through the gated ID-UAM federated identity service, and most institutional systems (secretaria virtual, mobile app backend) are not openly documented.'
finops:
- name: Uam Finops
  service_category: Education
  slug: uam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uam.png
jsonld:
- class_count: 8
  name: Uam Context
  property_count: 0
  slug: uam-context
layout: provider
modified: '2026-06-03'
name: Autonomous University of Madrid
nav: Providers
network: true
overview: 'Autonomous University of Madrid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Spain, and Open Access.


  The Autonomous University of Madrid catalog on APIs.io includes 1 JSON-LD context.


  Autonomous University of Madrid''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Uam Plans Pricing
  plan_count: 2
  slug: uam-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 1
  name: Uam Rate Limits
  slug: uam-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uam/refs/heads/main/screenshots/uam-2026-06-20T195920.png
security:
- kind: domain-security
  name: Uam Domain Security
  slug: uam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uam
tags:
- Education
- Higher Education
- University
- Spain
- Open Access
- Institutional Repository
- DSpace
- OAI-PMH
- Research
website: https://www.uam.es/
---
