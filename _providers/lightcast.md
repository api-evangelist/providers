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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Career Coach Careers API is a RESTful API service that contains economic data for all careers in the Career Coach app stored in JSON format.
  name: Lightcast Careers API
  slug: lightcast
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightcast-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightcast-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightcastdata
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lightcast.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lightcast.io/resources/blog
created: '2025-01-07'
description: Lightcast (formerly Emsi Burning Glass) provides labor market data and analytics including the Career Coach Careers API, a RESTful service that contains economic data for careers stored in JSON format.
finops:
- name: Lightcast Finops
  service_category: API
  slug: lightcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightcast.png
layout: provider
modified: '2026-04-28'
name: Lightcast
nav: Providers
network: true
overview: 'Lightcast publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Careers, Economics, Labor Market, and Workforce.


  Lightcast''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Lightcast Plans Pricing
  plan_count: 3
  slug: lightcast-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Lightcast Rate Limits
  slug: lightcast-rate-limits
score:
  band: minimal
  composite: 11.1
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightcast/refs/heads/main/screenshots/lightcast-2026-06-20T184514.png
security:
- kind: domain-security
  name: Lightcast Domain Security
  slug: lightcast-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lightcast
tags:
- Careers
- Economics
- Labor Market
- Workforce
---
