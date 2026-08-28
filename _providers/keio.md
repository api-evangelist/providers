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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: KOARA (KeiO Associated Repository of Academic resources) is Keio University's institutional repository, released in 2006 and running on the XooNips platform. It exposes a publicly accessible OAI-PMH 2
  name: KOARA OAI-PMH Metadata API
  slug: koara-oai-pmh
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.keio.ac.jp/en/
- group: build
  title: ''
  type: LibraryWebsite
  url: https://www.lib.keio.ac.jp/en/
- group: auth
  title: ''
  type: Authentication
  url: https://www.gakunin.jp/en
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Keio_PR_eng
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/keio-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/keio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/keio-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/keio-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'Keio University is a private research university in Tokyo, Japan, founded in 1858, and ranked #188 in the QS World University Rankings 2025. Its public machine-readable footprint is led by KOARA (KeiO Associated Repository of Academic resources), the institutional repository, which exposes a live OAI-PMH 2.0 metadata-harvesting endpoint. Most other institutional systems (keio.jp SSO over Google Workspace, Canvas K-LMS, the K-RIS researcher system, KOSMOS library discovery, and the Keio Object Hub culture portal) are account-gated and do not publish open developer API documentation. Identity is federated through GakuNin, the Japanese academic SAML/Shibboleth federation that participates in eduGAIN.'
finops:
- name: Keio Finops
  service_category: Education
  slug: keio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keio.png
jsonld:
- class_count: 14
  name: Keio Context
  property_count: 3
  slug: keio-context
layout: provider
modified: '2026-06-03'
name: Keio University
nav: Providers
network: true
overview: 'Keio University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Institutional Repository.


  The Keio University catalog on APIs.io includes 1 JSON-LD context.


  Keio University''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Keio Plans Pricing
  plan_count: 2
  slug: keio-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Keio Rate Limits
  slug: keio-rate-limits
score:
  band: emerging
  composite: 23.4
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/screenshots/keio-2026-06-20T183942.png
security:
- kind: domain-security
  name: Keio Domain Security
  slug: keio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keio
tags:
- Education
- Higher Education
- University
- Research
- Institutional Repository
- OAI-PMH
- Open Access
- Japan
website: https://www.keio.ac.jp/en/
---
