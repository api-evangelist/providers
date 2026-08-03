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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for TOUR (TOhoku University Repository), the university's institutional repository hosted on NII JAIRO Cloud (WEKO3). Verified live, returning a valid Identify
  name: TOUR Institutional Repository OAI-PMH
  slug: tour-oai-pmh
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tohoku-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tohoku.ac.jp/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cl-tohoku
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tohoku-univ/
- group: build
  title: ''
  type: Library
  url: https://www.library.tohoku.ac.jp/en/
- group: other
  title: ''
  type: Catalog
  url: https://opac.library.tohoku.ac.jp/opac/opac_search/?lang=1&smode=1
- group: commercial
  title: ''
  type: Plans
  url: plans/tohoku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tohoku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tohoku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tohoku University is a national research university in Sendai, Japan, founded in 1907 and ranked #107 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on scholarly infrastructure rather than a central developer portal: the TOUR (TOhoku University Repository) institutional repository runs on NII''s JAIRO Cloud (WEKO3) and exposes a live OAI-PMH 2.0 endpoint for metadata harvesting. The library also operates a public OPAC. No central, self-service API developer portal, open-data platform, or SSO/OAuth client-registration program was found publicly documented; most research-code APIs live in individual lab GitHub organizations.'
finops:
- name: Tohoku Finops
  service_category: Education
  slug: tohoku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tohoku.png
jsonld:
- class_count: 25
  name: Tohoku Context
  property_count: 4
  slug: tohoku-context
layout: provider
modified: '2026-06-03'
name: Tohoku University
nav: Providers
network: true
overview: 'Tohoku University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Japan.


  The Tohoku University catalog on APIs.io includes 1 JSON-LD context.


  Tohoku University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Tohoku Plans Pricing
  plan_count: 2
  slug: tohoku-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Tohoku Rate Limits
  slug: tohoku-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tohoku/refs/heads/main/screenshots/tohoku-2026-06-20T195441.png
security:
- kind: domain-security
  name: Tohoku Domain Security
  slug: tohoku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tohoku
tags:
- Education
- Higher Education
- University
- Research
- Japan
- Open Access
- Institutional Repository
- OAI-PMH
- Library
website: https://www.tohoku.ac.jp/en/
---
