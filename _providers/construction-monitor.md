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
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: REST + JSON service backed by Elasticsearch that lets partners search building permits, retrieve full permit detail records, and pull delta updates on a polling schedule. Authentication is handled wit
  name: Construction Monitor Permits API
  slug: permits-api
- description: Weekly bulk delivery of permit records over secure FTP for partners that prefer batch ingestion to live API polling. Suitable for warehousing millions of permits without operating a live integration.
  name: Construction Monitor Weekly Data Dump (SFTP)
  slug: weekly-ftp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/construction-monitor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Construction-Monitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/construction-monitor
- group: company
  title: ''
  type: Website
  url: https://www.constructionmonitor.com
- group: other
  title: ''
  type: Data Products
  url: https://www.constructionmonitor.com/data
- group: operate
  title: ''
  type: Contact / API Access
  url: https://www.constructionmonitor.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.constructionmonitor.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.constructionmonitor.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.constructionmonitor.com/terms-of-use
created: '2025-02-08'
description: Construction Monitor aggregates building-permit data from county and municipal sources nationwide and resells it as construction leads, contractor intelligence, and historical permit research. Programmatic access is offered through a REST + JSON API backed by Elasticsearch and a weekly data-dump option delivered over secure FTP. Both channels are account-managed; partners receive credentials and a documented endpoint contract directly from Construction Monitor.
finops:
- name: Construction Monitor Finops
  service_category: API
  slug: construction-monitor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/construction-monitor.png
layout: provider
modified: '2026-04-29'
name: Construction Monitor
nav: Providers
network: true
overview: 'Construction Monitor publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Contractors, Lead Generation, Permits, and Real Estate.


  Construction Monitor''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Construction Monitor Plans Pricing
  plan_count: 3
  slug: construction-monitor-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 5
  name: Construction Monitor Rate Limits
  slug: construction-monitor-rate-limits
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/construction-monitor/refs/heads/main/screenshots/construction-monitor-2026-06-20T174915.png
security:
- kind: domain-security
  name: Construction Monitor Domain Security
  slug: construction-monitor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: construction-monitor
tags:
- Construction
- Contractors
- Lead Generation
- Permits
- Real Estate
website: https://www.constructionmonitor.com
---
