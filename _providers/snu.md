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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for S-Space, the SNU Open Repository and Archive (a DSpace institutional repository). Verified live (HTTP 200) with repositoryName "SNU Open Repository and Ar
  name: S-Space OAI-PMH Repository Interface
  slug: s-space-oai-pmh
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.snu.ac.kr/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/seoulnational-university
- group: commercial
  title: ''
  type: Plans
  url: plans/snu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/snu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Seoul National University (SNU) is South Korea''s flagship national research university, located in Seoul, and is ranked #34 in the QS World University Rankings 2025. Its primary public, machine-readable developer footprint is S-Space, the SNU Open Repository and Archive, a DSpace-based institutional repository that exposes a standards-compliant OAI-PMH 2.0 interface for metadata harvesting of theses, journal articles, and research outputs. SNU does not publish a centralized developer portal or general-purpose open-data API; most other digital services (mySNU portal, SSO, library discovery) are gated and not openly documented.'
finops:
- name: Snu Finops
  service_category: Education
  slug: snu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snu.png
jsonld:
- class_count: 16
  name: Snu Context
  property_count: 4
  slug: snu-context
layout: provider
modified: '2026-06-03'
name: Seoul National University
nav: Providers
network: true
overview: 'Seoul National University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Seoul National University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Snu Plans Pricing
  plan_count: 2
  slug: snu-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Snu Rate Limits
  slug: snu-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snu/refs/heads/main/screenshots/snu-2026-06-20T194118.png
security:
- kind: domain-security
  name: Snu Domain Security
  slug: snu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snu
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- OAI-PMH
- South Korea
website: https://en.snu.ac.kr/
---
