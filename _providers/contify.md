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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
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
random_paper: 8
rate_limits:
- limit_count: 5
  name: Contify Rate Limits
  slug: contify-rate-limits
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
