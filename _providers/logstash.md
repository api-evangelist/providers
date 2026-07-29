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
- description: The Logstash Monitoring API exposes node info, plugin info, node stats, hot threads, and a health report endpoint over HTTP on port 9600 by default. There is no published OpenAPI specification; see El
  name: Logstash Monitoring API
  slug: logstash-monitoring-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/logstash-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logstash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/logstash
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/en/logstash/current/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic/logstash
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/feed
created: '2025-01-01'
description: Open source server-side data processing pipeline that ingests data from multiple sources, transforms it, and sends it to a specified destination. Part of the Elastic Stack.
finops:
- name: Logstash Finops
  service_category: API
  slug: logstash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logstash.png
layout: provider
modified: '2026-04-28'
name: Logstash
nav: Providers
network: true
overview: 'Logstash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Processing, ETL, Log Management, and Pipeline.


  Logstash''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Logstash Plans Pricing
  plan_count: 3
  slug: logstash-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Logstash Rate Limits
  slug: logstash-rate-limits
score:
  band: emerging
  composite: 20.5
  delta: -1.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logstash/refs/heads/main/screenshots/logstash-2026-06-20T184700.png
security:
- kind: domain-security
  name: Logstash Domain Security
  slug: logstash-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Logstash Trust Center
  slug: logstash-trust-center
  summary_line: GDPR
slug: logstash
tags:
- Data Processing
- ETL
- Log Management
- Pipeline
website: https://www.elastic.co/logstash
---
