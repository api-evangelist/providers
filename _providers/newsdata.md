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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: NewsData.io API for retrieving live breaking news and historical news data from over 82,000 sources, with search, filtering, and multi-language support.
  name: NewsData
  slug: newsdata
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newsdata-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newsdataapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/newsdata
- group: docs
  title: ''
  type: Documentation
  url: https://newsdata.io/documentation
- group: start
  title: ''
  type: Signup
  url: https://newsdata.io/register
- group: commercial
  title: ''
  type: Pricing
  url: https://newsdata.io/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://newsdata.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://newsdata.io/blog/feed/
created: '2025-02-09'
description: NewsData.io provides live breaking news and historical news data going back to January 2018, sourced from over 82,000 sources worldwide. The API supports searching, filtering by source, language, country, and category, and returns results in JSON format suitable for analytics, monitoring, and AI training.
finops:
- name: Newsdata Finops
  service_category: API
  slug: newsdata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newsdata.png
layout: provider
modified: '2026-07-25'
name: NewsData
nav: Providers
network: true
overview: 'NewsData publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Media, Search, and Content.


  NewsData''s developer surface includes documentation, signup flow, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Newsdata Plans Pricing
  plan_count: 3
  slug: newsdata-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Newsdata Rate Limits
  slug: newsdata-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newsdata/refs/heads/main/screenshots/newsdata-2026-06-20T190303.png
security:
- kind: domain-security
  name: Newsdata Domain Security
  slug: newsdata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: newsdata
tags:
- News
- Media
- Search
- Content
---
