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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Official Hanyang University Open API platform providing REST-style APIs that return XML or JSON. APIs are classified as Public (no personal data) or Private (require user authentication for personal i
  name: Hanyang University Open API Developer Center
  slug: developer-center
- description: Software development kits published by the Hanyang University Developer Center for building applications against the Open APIs, including Android and iOS SDKs and server-side sample integrations (e.g.
  name: Hanyang University Open API SDKs
  slug: sdk
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hanyang-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hanyang.ac.kr/web/eng
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.hanyang.ac.kr/develop/start.page
- group: auth
  title: ''
  type: Authentication
  url: https://api.hanyang.ac.kr/oauth/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hanyang-university
- group: commercial
  title: ''
  type: Plans
  url: plans/hanyang-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hanyang-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hanyang-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Hanyang University is a private research university in Seoul and Ansan, South Korea, ranked #162 in the QS World University Rankings 2025. It operates an official API Developer Center at api.hanyang.ac.kr that publishes REST-style Open APIs returning XML or JSON, with OAuth-based authentication, Android and iOS SDKs, an API testing console, and a developer community. Access to the Open APIs requires developer registration and authentication through the university''s HY-in portal; individual endpoints and personal-data ("Private") APIs are gated behind that login, so they are not publicly enumerable.'
finops:
- name: Hanyang Finops
  service_category: Education
  slug: hanyang-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hanyang.png
jsonld:
- class_count: 9
  name: Hanyang Context
  property_count: 4
  slug: hanyang-context
layout: provider
modified: '2026-06-03'
name: Hanyang University
nav: Providers
network: true
overview: 'Hanyang University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, South Korea, and Seoul.


  The Hanyang University catalog on APIs.io includes 1 JSON-LD context.


  Hanyang University''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Hanyang Plans Pricing
  plan_count: 2
  slug: hanyang-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Hanyang Rate Limits
  slug: hanyang-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hanyang/refs/heads/main/screenshots/hanyang-2026-06-20T182515.png
security:
- kind: domain-security
  name: Hanyang Domain Security
  slug: hanyang-domain-security
  summary_line: TLSv1.2
slug: hanyang
tags:
- Education
- Higher Education
- University
- South Korea
- Seoul
- Open API
- OAuth
website: https://www.hanyang.ac.kr/web/eng
---
