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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
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
  score: 5.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Partner-delivered, contact-sales data API that serves PREDIK''s enriched location-intelligence products - POI data, aggregated foot-traffic and mobility data, company and commercial-area intelligence, '
  name: PREDIK Location Intelligence & Foot Traffic Data API
  slug: predikt-ai-location-intelligence-data-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/predikt-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://predikdata.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/predik-data-driven-us/
- group: docs
  title: ''
  type: Documentation
  url: https://predikdata.com/location-intelligence-solutions/
- group: other
  title: ''
  type: Listing
  url: https://datarade.ai/data-providers/centralamericadata/profile
- group: commercial
  title: ''
  type: Plans
  url: plans/predikt-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/predikt-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/predikt-ai-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/predikt-ai-robots.txt
- group: company
  title: ''
  type: Blog
  url: https://predikdata.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://predikdata.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://predikdata.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://predikdata.com/predik-data-driven-privacy-policy/
coverage:
  checked: '2026-08-14'
  detail: PREDIK runs a real, live API - https://api.predikdata.com is an AWS API Gateway on its own domain whose /ping endpoint answers HTTP 200 "Healthy Connection" - but every other path returns 403 {"message":"Missing Authentication Token"}, and the provider's own llms.txt, a complete inventory of all ~200 pages on predikdata.com, lists no developer, documentation, API-reference or pricing page at all, so the contract is reachable only after a "Request a Demo" sales conversation.
  evidence:
  - status: 200
    url: https://api.predikdata.com/ping
  - status: 403
    url: https://api.predikdata.com/
  - status: 200
    url: https://predikdata.com/llms.txt
  - status: 404
    url: https://predikdata.com/.well-known/agent-card.json
  - status: 403
    url: https://predikdata.com/request_demo/
  reason: sales-gate
  state: gated
created: '2026-07-11'
description: PREDIK Data-Driven is a big-data analytics and location-intelligence research firm (founded 2008, Coral Gables, Florida) that builds enriched geospatial datasets for site selection, demand forecasting, and web/reference intelligence. Its products cover Point-of-Interest (POI) data, aggregated foot-traffic and human mobility data derived from anonymized mobile devices, company and commercial-area intelligence, and socio-demographic enrichment - divided into geohash-7 (150x150m) cells with 100-200+ variables and coverage of up to 96 countries. PREDIK is a data-delivery / contact-sales provider - datasets are licensed and delivered as managed feeds via REST API, SOAP API, Feed API, or S3 bucket in JSON, CSV, and SQL formats. There is no public self-serve developer API portal or published API reference; access is arranged directly with PREDIK or through the Datarade marketplace. Endpoints are not publicly documented and are therefore not modeled here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/predikt-ai.png
layout: provider
modified: '2026-08-14'
name: PREDIK Data-Driven
nav: Providers
network: true
overview: 'PREDIK Data-Driven publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Intelligence, Data Enrichment, Company Data, B2B Data, and Sales Intelligence.


  PREDIK Data-Driven''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Predikt Ai Plans Pricing
  plan_count: 0
  slug: predikt-ai-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 0
  name: Predikt Ai Rate Limits
  slug: predikt-ai-rate-limits
score:
  band: emerging
  composite: 15.2
  delta: 0.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Predikt Ai Domain Security
  slug: predikt-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: predikt-ai
tags:
- Web Intelligence
- Data Enrichment
- Company Data
- B2B Data
- Sales Intelligence
- Reference Data
- Location Intelligence
- Geospatial
- Foot Traffic
- POI Data
- Mobility Data
- Demand Forecasting
- Site Selection
- Alternative Data
website: https://predikdata.com/
---
