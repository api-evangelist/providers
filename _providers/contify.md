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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Contify News API is a developer-friendly REST/JSON API that aggregates, deduplicates, and enriches business news from over a million curated sources, covering 700,000+ companies and 117+ languages
  name: Contify News API
  slug: news-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contify-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contifyhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contify
- group: company
  title: ''
  type: Website
  url: https://www.contify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.contify.com/news-api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.contify.com/
- group: company
  title: ''
  type: Blog
  url: https://www.contify.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.contify.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.contify.com/terms-of-service/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.contify.com/contact-us/
created: '2025-02-09'
description: Contify is an AI-powered market and competitive intelligence platform that helps businesses track competitor activity, market trends, and industry news. It exposes a REST News API that delivers structured, deduplicated, and enriched business news data on companies, industries, and topics.
finops:
- name: Contify Finops
  service_category: API
  slug: contify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contify.png
layout: provider
modified: '2026-04-28'
name: Contify
nav: Providers
network: true
overview: 'Contify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Competitive Intelligence, Market Intelligence, News, and Strategies.


  Contify''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Contify Plans Pricing
  plan_count: 3
  slug: contify-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Contify Rate Limits
  slug: contify-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 27.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contify/refs/heads/main/screenshots/contify-2026-06-20T174939.png
security:
- kind: domain-security
  name: Contify Domain Security
  slug: contify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contify
tags:
- Competitive Intelligence
- Market Intelligence
- News
- Strategies
website: https://www.contify.com/
---
