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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Documented HTTP GET API that exports the publication list for a given ULB scholar (identified by matricule or DAI). Supports output formats including APA, BibTeX, RIS, CSV, xml-brief, xml-brief-ext an
  name: DI-fusion Scholar Export API
  slug: difusion-scholar
- description: Documented HTTP GET API that exports the publication list for a group of ULB scholars, defined either by a valid group ID or a list of scholar IDs. Shares output formats and options with the Scholar e
  name: DI-fusion Group Export API
  slug: difusion-group
- description: ULB's DI-fusion institutional repository documents an OAI-PMH harvesting service allowing third parties to harvest metadata for non-profit purposes (provided the OAI identifier or source link is indic
  name: DI-fusion OAI-PMH Harvesting Service
  slug: difusion-oai
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ulb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ulb.be/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ulb
- group: company
  title: ''
  type: LinkedIn
  url: https://be.linkedin.com/school/universite-libre-de-bruxelles/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ulb
- group: commercial
  title: ''
  type: Plans
  url: plans/ulb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ulb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ulb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Université libre de Bruxelles (ULB) is a major French-speaking research university in Brussels, Belgium, ranked #230 in the QS World University Rankings 2025. Its public, documented developer footprint is centered on DI-fusion, the university''s institutional research repository, which exposes a documented HTTP export API for scholar and group publication lists, a search interface, RSS feeds, and an OAI-PMH harvesting service for metadata. ULB also maintains an official GitHub organization for departmental and research code. Beyond these, most ULB systems (student/SIS portals, library discovery, SSO) are gated and not publicly documented as APIs.'
finops:
- name: Ulb Finops
  service_category: Education
  slug: ulb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ulb.png
jsonld:
- class_count: 11
  name: Ulb Context
  property_count: 5
  slug: ulb-context
layout: provider
modified: '2026-06-03'
name: Université libre de Bruxelles
nav: Providers
network: true
overview: 'Université libre de Bruxelles publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Université libre de Bruxelles catalog on APIs.io includes 1 JSON-LD context.


  Université libre de Bruxelles'' developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Ulb Plans Pricing
  plan_count: 2
  slug: ulb-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 1
  name: Ulb Rate Limits
  slug: ulb-rate-limits
score:
  band: emerging
  composite: 17.4
  delta: -1.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ulb/refs/heads/main/screenshots/ulb-2026-06-20T200008.png
security:
- kind: domain-security
  name: Ulb Domain Security
  slug: ulb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ulb
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- Belgium
website: https://www.ulb.be/en
---
