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
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'ITB''s campus-wide single sign-on, built on the Apereo CAS (Central Authentication Service) protocol. Applications integrate against the CAS login/validation endpoints to authenticate ITB members. The '
  name: ITB Single Sign-On (CAS)
  slug: sso-cas
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://itb.ac.id/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/institut-teknologi-bandung/
- group: auth
  title: ''
  type: Authentication
  url: https://login.itb.ac.id/
- group: commercial
  title: ''
  type: Plans
  url: plans/itb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/itb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/itb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://digilib.itb.ac.id/
created: '2026-06-03'
description: 'Institut Teknologi Bandung (ITB) is a public research university in Bandung, Indonesia, ranked #256 in the QS World University Rankings 2025. ITB operates a number of public-facing web systems including an institutional digital library (Ganesha Digital Library / GDL), an academic portal, and a campus-wide single sign-on service. As of this review ITB does not publish a dedicated developer portal or documented public API program; its machine-readable surfaces are limited to a CAS-based SSO endpoint and an institutional repository whose historical OAI-PMH/RSS endpoints no longer resolve after a platform migration. The entries below reflect only what could be verified live and publicly.'
finops:
- name: Itb Finops
  service_category: Education
  slug: itb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/itb.png
jsonld:
- class_count: 15
  name: Itb Context
  property_count: 2
  slug: itb-context
layout: provider
modified: '2026-07-25'
name: Bandung Institute of Technology
nav: Providers
network: true
overview: 'Bandung Institute of Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Indonesia.


  The Bandung Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  Bandung Institute of Technology''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Itb Plans Pricing
  plan_count: 2
  slug: itb-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Itb Rate Limits
  slug: itb-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/itb/refs/heads/main/screenshots/itb-2026-06-20T183631.png
security:
- kind: domain-security
  name: Itb Domain Security
  slug: itb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: itb
tags:
- Education
- Higher Education
- University
- Research
- Indonesia
- Authentication
- Digital Library
website: https://itb.ac.id/
---
