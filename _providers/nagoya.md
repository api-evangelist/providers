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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for the NAGOYA Repository, the Nagoya University institutional repository running on the NII WEKO3 / JAIRO Cloud platform. Supports the standard OAI-PMH verbs
  name: NAGOYA Repository OAI-PMH
  slug: repo-oai
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nagoya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.nagoya-u.ac.jp/
- group: other
  title: ''
  type: InstitutionalRepository
  url: https://nagoya.repo.nii.ac.jp/
- group: other
  title: ''
  type: ITServices
  url: https://icts.nagoya-u.ac.jp/en/
- group: auth
  title: ''
  type: Authentication
  url: https://icts.nagoya-u.ac.jp/en/services/nuid/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nagoya-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/nagoya-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nagoya-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nagoya-finops.yml
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
  url: json-ld/nagoya-context.jsonld
created: '2026-06-03'
description: 'Nagoya University (名古屋大学) is a national research university in Nagoya, Aichi, Japan, ranked #152 in the QS World University Rankings 2025. As a leading research institution it operates a range of academic and IT services through its Information & Communications (ICTS) division and university library. Its most clearly documented public, machine-readable API surface is the NAGOYA Repository institutional repository, which runs on the NII WEKO3 / JAIRO Cloud platform and exposes an OAI-PMH 2.0 interface for harvesting scholarly metadata. Most other systems (student portal, NU-ID identity, course registration) are gated behind THERS/GakuNin (Shibboleth/SAML) authentication and are not publicly documented developer APIs.'
finops:
- name: Nagoya Finops
  service_category: Education
  slug: nagoya-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nagoya.png
jsonld:
- class_count: 16
  name: Nagoya Context
  property_count: 6
  slug: nagoya-context
layout: provider
modified: '2026-06-03'
name: Nagoya University
nav: Providers
network: true
overview: 'Nagoya University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Nagoya University catalog on APIs.io includes 1 JSON-LD context.


  Nagoya University''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Nagoya Plans Pricing
  plan_count: 2
  slug: nagoya-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 1
  name: Nagoya Rate Limits
  slug: nagoya-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nagoya/refs/heads/main/screenshots/nagoya-2026-06-20T185937.png
security:
- kind: domain-security
  name: Nagoya Domain Security
  slug: nagoya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nagoya
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- OAI-PMH
- Japan
website: https://en.nagoya-u.ac.jp/
---
