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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Budgeting & Planning
  name: YNAB
  slug: ynab
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ynab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ynab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.youneedabudget.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ynab.com/blog/rss.xml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Budgeting & Planning
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ynab.png
layout: provider
modified: '2026-05-28'
name: YNAB
nav: Providers
network: true
overview: 'YNAB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.


  YNAB''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 26
score:
  band: minimal
  composite: 6.2
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ynab/refs/heads/main/screenshots/ynab-2026-06-20T201741.png
security:
- kind: domain-security
  name: Ynab Domain Security
  slug: ynab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ynab Vulnerability Disclosure
  slug: ynab-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: ynab
tags:
- Finance
- Public APIs
website: https://api.youneedabudget.com/
---
