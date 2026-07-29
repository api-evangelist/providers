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
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Dipòsit Digital de Documents de la UAB (DDD), the university's institutional repository of theses, articles, preprints, postprints, ebooks, periodicals
  name: DDD Digital Document Repository OAI-PMH
  slug: ddd-oai-pmh
- description: UAB research data is published via the Catalan Consortium of University Services (CSUC) federated, multidisciplinary research data repository (CORA Repositori de Dades de Recerca), where Catalan unive
  name: CSUC Research Data Repository (CORA RDR)
  slug: rdr-research-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uab.cat/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uabbarcelona/
- group: commercial
  title: ''
  type: Plans
  url: plans/uab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uab-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Autonomous University of Barcelona (Universitat Autònoma de Barcelona, UAB) is a public research university in Bellaterra, near Barcelona, Spain, founded in 1968 and ranked #175 in the QS World University Rankings 2025. UAB''s public, machine-accessible footprint centers on its open scholarly infrastructure rather than a formal developer portal: the Dipòsit Digital de Documents (DDD), the institutional repository built on the Invenio platform, exposes an OAI-PMH 2.0 metadata endpoint and is OpenAIRE-compliant. Research data is published through the Catalan consortium (CSUC) federated research data repository. No dedicated, publicly documented UAB developer/API program or official institutional GitHub organization was confirmed; student-facing academic services (SIA) are gated login portals without public API documentation.'
finops:
- name: Uab Finops
  service_category: Education
  slug: uab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uab.png
jsonld:
- class_count: 10
  name: Uab Context
  property_count: 3
  slug: uab-context
layout: provider
modified: '2026-06-03'
name: Autonomous University of Barcelona
nav: Providers
network: true
overview: 'Autonomous University of Barcelona publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Spain, and Catalonia.


  The Autonomous University of Barcelona catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Uab Plans Pricing
  plan_count: 2
  slug: uab-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Uab Rate Limits
  slug: uab-rate-limits
score:
  band: emerging
  composite: 17.7
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uab/refs/heads/main/screenshots/uab-2026-06-20T195920.png
security:
- kind: domain-security
  name: Uab Domain Security
  slug: uab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uab
tags:
- Education
- Higher Education
- University
- Spain
- Catalonia
- Open Access
- Institutional Repository
- OAI-PMH
- Research Data
website: https://www.uab.cat/
---
