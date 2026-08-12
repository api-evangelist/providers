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
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Open, REST-style API providing developer access to data about the Princeton University Art Museum and its collections. Returns JSON for objects, makers, packages, and full-text search, with IIIF image
  name: Princeton University Art Museum API
  slug: artmuseum
- description: Princeton Office of Information Technology API gateway. Default APIs include ActiveDirectory (user/group lookups) and PrincetonInfo (department data); a MobileApp API exposes course, dining, and campu
  name: Princeton OIT API Store
  slug: oit-api-store
- description: 'DataSpace is Princeton''s DSpace-based digital repository for archiving and disseminating research and academic output. It exposes an OAI-PMH metadata-harvesting endpoint. Content is being migrated to '
  name: DataSpace OAI-PMH
  slug: dataspace-oai
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/princeton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.princeton.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pulibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/princeton-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-store.princeton.edu/store/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Princeton-University-Art-Museum
- group: commercial
  title: ''
  type: Plans
  url: plans/princeton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/princeton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/princeton-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Princeton University is a private Ivy League research university in Princeton, New Jersey, ranked #13 in the QS World University Rankings 2025. Its public developer footprint is modest and centers on the Princeton University Art Museum API, an open, no-authentication REST service for collections data. Most institutional APIs (the OIT API Store covering Active Directory, PrincetonInfo, and the MobileApp course/dining/places data) are gated behind NetID/service-account OAuth2 and campus access. Library and research-data systems expose metadata through standard protocols such as OAI-PMH.'
finops:
- name: Princeton Finops
  service_category: Education
  slug: princeton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/princeton.png
jsonld:
- class_count: 25
  name: Princeton Context
  property_count: 0
  slug: princeton-context
layout: provider
modified: '2026-06-03'
name: Princeton University
nav: Providers
network: true
overview: 'Princeton University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Ivy League, and United States.


  The Princeton University catalog on APIs.io includes 1 JSON-LD context.


  Princeton University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Princeton Plans Pricing
  plan_count: 2
  slug: princeton-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Princeton Rate Limits
  slug: princeton-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/princeton/refs/heads/main/screenshots/princeton-2026-06-20T192107.png
security:
- kind: domain-security
  name: Princeton Domain Security
  slug: princeton-domain-security
  summary_line: TLSv1.3 · DMARC
slug: princeton
tags:
- Education
- Higher Education
- University
- Ivy League
- United States
- Open Data
- Museum
- Library
website: https://www.princeton.edu/
---
