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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Kingo Portal is SKKU's single sign-on environment that integrates and secures access to university online services (Gmail/Google Workspace, GLS, iCampus, electronic approval, notice boards). Access is
  name: Kingo Portal (SSO / Identity)
  slug: kingo-portal
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skku-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skku.edu/eng/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/GDG-SKKU
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sungkyunkwan-university
- group: commercial
  title: ''
  type: Plans
  url: plans/skku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/skku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Sungkyunkwan University (SKKU) is a private research university in Seoul and Suwon, South Korea, with roots dating to 1398, and is ranked #123 in the QS World University Rankings 2025. Its digital footprint centers on the Kingo Portal single sign-on environment, the iCampus learning system, the university library, and the KINGO-M mobile app. As of this review SKKU publishes no public, documented developer API or open-data portal; integration and identity services (Kingo SSO, eduroam) are gated to enrolled students, faculty, and staff. Public software activity exists mainly through research-lab and student developer-community GitHub organizations rather than a central institutional developer program.'
finops:
- name: Skku Finops
  service_category: Education
  slug: skku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skku.png
jsonld:
- class_count: 7
  name: Skku Context
  property_count: 3
  slug: skku-context
layout: provider
modified: '2026-06-03'
name: Sungkyunkwan University
nav: Providers
network: true
overview: 'Sungkyunkwan University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and South Korea.


  The Sungkyunkwan University catalog on APIs.io includes 1 JSON-LD context.


  Sungkyunkwan University''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Skku Plans Pricing
  plan_count: 2
  slug: skku-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 1
  name: Skku Rate Limits
  slug: skku-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skku/refs/heads/main/screenshots/skku-2026-06-20T194017.png
security:
- kind: domain-security
  name: Skku Domain Security
  slug: skku-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skku
tags:
- Education
- Higher Education
- University
- Research
- South Korea
- Seoul
website: https://www.skku.edu/eng/
---
