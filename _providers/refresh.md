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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refresh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://refresh.si
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/refresh-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Refresh is a marketing agency whose entire public surface is one WordPress splash page ("WE BUILD AND GROW DIGITAL BRANDS", (c)2019) with a mailto contact — its Yoast sitemap lists exactly two URLs, both last modified 2019-05-24, and wp/v2/posts returns an empty array, so there is no product, portal or documentation for an API to sit behind.
  evidence:
  - status: 200
    url: https://refresh.si/
  - status: 200
    url: https://refresh.si/page-sitemap.xml
  - status: 404
    url: https://refresh.si/openapi.json
  - status: 404
    url: https://refresh.si/.well-known/agent-card.json
  - status: 404
    url: https://refresh.si/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-07-17'
description: Refresh (refresh.si) is a Slovenian digital marketing agency focused on building and growing digital brands. It was surfaced as a portfolio company of Slow Ventures and added to the API Evangelist network for enrichment. Contract discovery re-run on 2026-08-13 found the entire public footprint is a single WordPress splash page carrying a 2019 copyright, with two URLs in its sitemap and no blog posts — no API, developer portal, documentation, SDK, package, changelog or pricing surface, and HTTP 404 on /openapi.json, /llms.txt and every /.well-known/ discovery path. The profile is retained as a company lead with domain security captured from live TLS/DNS probes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refresh.png
layout: provider
modified: '2026-08-13'
name: refresh
nav: Providers
network: true
overview: refresh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Marketing, Marketing Agency, Branding, and Slovenia.
plans:
- name: Refresh Plans Pricing
  plan_count: 0
  slug: refresh-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Refresh Rate Limits
  slug: refresh-rate-limits
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Refresh Domain Security
  slug: refresh-domain-security
  summary_line: TLSv1.3
slug: refresh
tags:
- Company
- Digital Marketing
- Marketing Agency
- Branding
- Slovenia
website: https://refresh.si
---
