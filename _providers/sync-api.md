---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- description: The Sync API bidder platform provides enterprise-grade APIs for the in-app advertising ecosystem. The platform supports real-time bidding (RTB), user acquisition optimization, LTV (Lifetime Value) for
  name: Sync API Platform
  slug: sync-api-platform
- description: User acquisition API leveraging advanced algorithms to optimize user acquisition strategies for mobile apps. Provides targeting across 1.2B+ global audiences with LTV forecasting and in-app event conv
  name: Sync API User Acquisition
  slug: sync-api-user-acquisition
- description: Re-engagement API that analyzes behavioral data to identify relevant content for target audiences, enabling advertisers to re-engage lapsed users through personalized in-app advertising campaigns.
  name: Sync API User Re-Engagement
  slug: sync-api-re-engagement
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sync-api-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sync-api-llms.txt
- group: company
  title: ''
  type: Website
  url: https://sync-api.com
- group: operate
  title: ''
  type: Contact
  url: mailto:support@sync-api.com
coverage:
  checked: '2026-08-12'
  detail: 'Sync API markets itself as an "Enterprise API for the In-App advertising ecosystem" but ships no developer surface at all: the site is a five-page WordPress brochure with no docs, no reference, no signup and no SDKs, and the API host it advertised, api.sync-api.com, is authoritative NXDOMAIN on 8.8.8.8, 1.1.1.1 and 9.9.9.9 — so the placeholder baseURL was removed from this file. Every spec and /.well-known/ path returns the WordPress 404 template; the only machine-readable surface on the domain is the marketing site''s own WordPress REST API (/wp-json/, 268 CMS routes) and an auth-gated (401) WordPress MCP-adapter route, neither of which is the advertising product.'
  evidence:
  - status: 0
    url: https://api.sync-api.com
  - status: 404
    url: https://sync-api.com/openapi.json
  - status: 404
    url: https://sync-api.com/.well-known/agent-card.json
  - status: 404
    url: https://sync-api.com/docs
  - status: 401
    url: https://sync-api.com/wp-json/mcp/mcp-adapter-default-server
  - status: 200
    url: https://sync-api.com/
  reason: no-developer-program
  state: none
created: '2026-05-03'
description: Sync API is an enterprise API platform for the in-app mobile advertising ecosystem, delivering performance, transparency, and control for marketers. The platform provides a bidder platform and suite of APIs for user acquisition, mobile user growth, and user re-engagement. It enables data-driven, ROI-focused mobile advertising across 1.2 billion global audiences in 50+ countries, with 500+ robust API integrations and advanced algorithms for LTV forecasting and in-app event conversion tracking.
finops:
- name: Sync Api Finops
  service_category: API
  slug: sync-api-finops
image: https://sync-api.com/favicon.ico
jsonld:
- class_count: 0
  name: Sync Api Context
  property_count: 25
  slug: sync-api-context
layout: provider
modified: '2026-08-12'
name: Sync API
nav: Providers
network: true
overview: 'Sync API publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Digital Marketing, In-App Advertising, Mobile, and Programmatic.


  The Sync API catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Sync Api Plans Pricing
  plan_count: 0
  slug: sync-api-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Sync Api Rate Limits
  slug: sync-api-rate-limits
score:
  band: emerging
  composite: 11.6
  delta: -0.4
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sync-api/refs/heads/main/screenshots/sync-api-2026-06-20T194823.png
security:
- kind: domain-security
  name: Sync Api Domain Security
  slug: sync-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sync-api
tags:
- Advertising
- Digital Marketing
- In-App Advertising
- Mobile
- Programmatic
- Real-Time Bidding
- User Acquisition
website: https://sync-api.com
---
