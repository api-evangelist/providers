---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impactyn-bv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impactyn.com
- group: company
  title: ''
  type: About
  url: https://impactyn.com/about
- group: operate
  title: ''
  type: Support
  url: https://impactyn.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impactyn.com/tac
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impactyn.com/privacy_policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impactyn-bv-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Impactyn ships only end-user iOS/Android apps and a hosted brand console — every machine-readable contract path on impactyn.com (/openapi.json, /swagger.json, /graphql, /api-docs, /llms.txt, all nine /.well-known/ paths) returned a real 404, there is no GitHub organization or published package, and the partner console host in the site footer (admin.impactyn.com) resolves NOERROR with zero address records.
  evidence:
  - status: 404
    url: https://impactyn.com/openapi.json
  - status: 404
    url: https://impactyn.com/.well-known/agent-card.json
  - status: 404
    url: https://impactyn.com/graphql
  - status: 0
    url: http://admin.impactyn.com/home/login
  - status: 200
    url: https://impactyn.com/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Impactyn B.V is an AI-powered crowd-marketing platform that turns authentic user-generated video reviews into brand marketing assets. Based in Cairo, Egypt, Impactyn connects brands with real customers who record genuine video testimonials, letting businesses leverage user-generated video content to increase visibility, credibility, and engagement. The platform is delivered primarily through consumer iOS and Android mobile apps plus a partner/brand web console, and was surfaced as a portfolio company of 500 Global. Founded by Mohamed Wahid and registered in Egypt under Commercial Register No. 18682, the company reports 51,000 consumer signups in its first year and sells brands a campaign-based service with a live views/engagement/ROI dashboard. No public API, developer portal, SDK, machine-readable specification or /.well-known/ document is published — verified by probe on 2026-08-12 — and the partner console host advertised on the website no longer resolves. This profile captures
  company identity, the domain-security posture, a verified well-known probe, and the absence of published pricing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impactyn-bv.png
layout: provider
modified: '2026-08-12'
name: Impactyn B.V
nav: Providers
network: true
overview: 'Impactyn B.V is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Video, User Generated Content, and Advertising.


  Impactyn B.V''s developer surface includes support and 6 more developer resources.'
plans:
- name: Impactyn Bv Plans Pricing
  plan_count: 0
  slug: impactyn-bv-plans-pricing
random_paper: 17
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 10.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impactyn-bv/refs/heads/main/screenshots/impactyn-bv-2026-07-25T222142.png
security:
- kind: domain-security
  name: Impactyn Bv Domain Security
  slug: impactyn-bv-domain-security
  summary_line: TLSv1.3
slug: impactyn-bv
tags:
- Company
- Marketing
- Video
- User Generated Content
- Advertising
- Reviews
- Mobile
website: https://impactyn.com
---
