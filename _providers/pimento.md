---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pimento-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pimento.design/
- group: start
  title: ''
  type: SignUp
  url: https://www.pimento.design/signup
- group: start
  title: ''
  type: Login
  url: https://www.pimento.design/auth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pimento.design/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pimento.design/terms
- group: operate
  title: ''
  type: Support
  url: https://help.pimento.design/en/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pimento-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pimento-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pimento-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pimentodesign
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@pimento.design
coverage:
  checked: '2026-08-12'
  detail: Pimento's only API is the first-party backend behind its own web app — https://app.pimento.design/api/* answers 401 {"detail":"Unable to authenticate"} to anonymous callers and is guarded by the Auth0 tenant gopimento.eu.auth0.com with audience https://api.gopimento.co (a name that does not resolve in public DNS) — and Pimento publishes no developer portal, reference, spec, or SDK for it anywhere; docs.pimento.design and api.pimento.design do not exist, and every /openapi.json, /llms.txt and /.well-known/* path on www and app answers 200 with the identical single-page-app shell rather than a document.
  evidence:
  - status: 401
    url: https://app.pimento.design/api/users/me
  - status: 200
    url: https://www.pimento.design/openapi.json
  - status: 200
    url: https://www.pimento.design/sitemap.xml
  - status: 200
    url: https://gopimento.eu.auth0.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Pimento is an AI ad-creative platform that helps marketing and advertising teams generate, analyze, and benchmark advertising creatives at scale. Its published product surface spans creative generation (Create), performance analysis (Analyze), competitive benchmarking (Benchmark), reusable brand kits, a Meta Score for predicting ad performance, multiformat output, and Meta Advantage+ support. Pimento is a venture-backed company in Partech''s portfolio. It ships an end-user SaaS application at app.pimento.design backed by a private REST API and an Auth0 tenant, but that API is first-party only: it is undocumented, returns 401 to anonymous callers, and is not offered to developers. No developer portal, API reference, OpenAPI or other machine-readable specification, SDK, package, webhook catalog, CLI, changelog, status page, public pricing page, or MCP/A2A agent surface is published anywhere on a Pimento-controlled host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pimento.png
layout: provider
modified: '2026-08-12'
name: Pimento
nav: Providers
network: true
overview: 'Pimento is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai/Ml, Advertising, Creative, and Marketing.


  Pimento''s developer surface includes signup flow, support, YouTube channel, and 9 more developer resources.'
plans:
- name: Pimento Plans Pricing
  plan_count: 0
  slug: pimento-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Pimento Rate Limits
  slug: pimento-rate-limits
score:
  band: emerging
  composite: 14.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Pimento Authentication
  slug: pimento-authentication
  summary_line: oauth2/openIdConnect · 0 schemes
- kind: domain-security
  name: Pimento Domain Security
  slug: pimento-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pimento
tags:
- Company
- Ai/Ml
- Advertising
- Creative
- Marketing
- Generative AI
- AdTech
website: https://www.pimento.design/
---
