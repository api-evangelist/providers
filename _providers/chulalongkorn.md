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
- description: Single sign-on authentication service for Chulalongkorn University, allowing applications to securely authenticate students and staff using their Chula ID without handling credentials directly. In pro
  name: Chula SSO Authentication API
  slug: sso
- description: Chulalongkorn University Intellectual Repository (CUIR), now served via the Chula Digiverse digital preservation platform built on DSpace. It holds theses, dissertations, academic papers, learning mat
  name: CUIR / Chula Digiverse Repository (OAI-PMH & DSpace REST)
  slug: cuir
- description: The university's central data exchange system that consolidates and shares data across departments. It supports two connection modes - Batch (SFTP) and Online (API). Access is restricted to officially
  name: CU Data Gateway API
  slug: data-gateway
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chulalongkorn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chula.ac.th/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ChulalongkornUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/chulalongkorn-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.it.chula.ac.th/
- group: commercial
  title: ''
  type: Plans
  url: plans/chulalongkorn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chulalongkorn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chulalongkorn-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Chulalongkorn University is Thailand''s oldest and a leading public research university, located in Bangkok and ranked #229 in the QS World University Rankings 2025. Its public developer/API footprint is limited and largely oriented toward identity and scholarly content: a campus single sign-on (Chula SSO) authentication API for student/staff login, an institutional repository (CUIR / Chula Digiverse, built on DSpace) exposing OAI-PMH and REST interfaces, and a staff-only central data exchange (CU Data Gateway) that offers an online API mode. There is no unified, openly documented public developer portal; access to most services is gated to university personnel or granted on request.'
finops:
- name: Chulalongkorn Finops
  service_category: Education
  slug: chulalongkorn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chulalongkorn.png
jsonld:
- class_count: 12
  name: Chulalongkorn Context
  property_count: 6
  slug: chulalongkorn-context
layout: provider
modified: '2026-06-03'
name: Chulalongkorn University
nav: Providers
network: true
overview: 'Chulalongkorn University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Thailand, and Identity.


  The Chulalongkorn University catalog on APIs.io includes 1 JSON-LD context.


  Chulalongkorn University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Chulalongkorn Plans Pricing
  plan_count: 2
  slug: chulalongkorn-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Chulalongkorn Rate Limits
  slug: chulalongkorn-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chulalongkorn/refs/heads/main/screenshots/chulalongkorn-2026-06-20T174339.png
security:
- kind: domain-security
  name: Chulalongkorn Domain Security
  slug: chulalongkorn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chulalongkorn
tags:
- Education
- Higher Education
- University
- Thailand
- Identity
- Single Sign-On
- Institutional Repository
- Open Access
- OAI-PMH
website: https://www.chula.ac.th/en/
---
