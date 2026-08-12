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
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for Enlighten, the University of Glasgow's EPrints institutional repository of publications (journal articles, theses, conference papers, books and more). Supp
  name: Enlighten Publications OAI-PMH
  slug: enlighten-oai
- description: OAI-PMH 2.0 metadata harvesting endpoint for Enlighten Research Data, the University of Glasgow's EPrints research data repository and registry. Returns a valid Identify response and supports standard
  name: Enlighten Research Data OAI-PMH
  slug: researchdata-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-glasgow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gla.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UoGSoE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-glasgow/
- group: auth
  title: ''
  type: Authentication
  url: https://www.gla.ac.uk/myglasgow/it/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-glasgow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-glasgow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-glasgow-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-glasgow-context.jsonld
created: '2026-06-03'
description: 'The University of Glasgow is a public research university in Glasgow, Scotland, United Kingdom, founded in 1451 and ranked #62 in the QS World University Rankings 2025. Its public, machine-accessible developer footprint is centered on scholarly infrastructure rather than a unified developer portal: the Enlighten institutional repository and Enlighten Research Data repository both run on EPrints and expose OAI-PMH 2.0 metadata harvesting endpoints. There is no single university-wide API developer portal; departmental engineering teams publish open-source code on GitHub, and access to most internal systems is gated behind Shibboleth/SAML single sign-on (GUID).'
finops:
- name: University Of Glasgow Finops
  service_category: Education
  slug: university-of-glasgow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-glasgow.png
jsonld:
- class_count: 18
  name: University Of Glasgow Context
  property_count: 6
  slug: university-of-glasgow-context
layout: provider
modified: '2026-06-03'
name: University of Glasgow
nav: Providers
network: true
overview: 'University of Glasgow publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Glasgow catalog on APIs.io includes 1 JSON-LD context.


  University of Glasgow''s developer surface includes GitHub presence, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: University Of Glasgow Plans Pricing
  plan_count: 2
  slug: university-of-glasgow-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 1
  name: University Of Glasgow Rate Limits
  slug: university-of-glasgow-rate-limits
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-glasgow/refs/heads/main/screenshots/university-of-glasgow-2026-06-20T200152.png
security:
- kind: domain-security
  name: University Of Glasgow Domain Security
  slug: university-of-glasgow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-glasgow
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- OAI-PMH
- United Kingdom
- Scotland
website: https://www.gla.ac.uk/
---
