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
api_count: 2
apis:
- description: REST API for programmatic access to Kissmetrics reports, segments, events, properties, and account metadata. Used to pull report data into dashboards, spreadsheets, and BI tools, and to export user se
  name: Kissmetrics REST API
  slug: rest-api
- description: Legacy Data Out API for exporting raw Kissmetrics data. Documented in the older support portal alongside the current v3 REST API.
  name: Kissmetrics Data Out API
  slug: data-out-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kissmetrics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kissmetrics
- group: company
  title: ''
  type: Website
  url: https://www.kissmetrics.io
- group: docs
  title: ''
  type: Documentation
  url: https://support.kissmetrics.io
- group: other
  title: ''
  type: Product Page
  url: https://www.kissmetrics.io/product/workflows/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kissmetrics
- group: start
  title: ''
  type: Signup
  url: https://www.kissmetrics.io/signup
- group: operate
  title: ''
  type: Support
  url: https://support.kissmetrics.io
- group: agent
  title: ''
  type: LlmsText
  url: https://kissmetrics.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.kissmetrics.io/feed.xml
created: '2026-05-11'
description: Kissmetrics is a product and behavioral analytics platform that tracks individual user activity across web and mobile, surfacing funnels, cohorts, retention, and revenue reports tied to identified people. The platform helps product, marketing, and growth teams understand user journeys and pinpoint conversion drop-off. Kissmetrics provides REST APIs for querying reports, exporting segments, and ingesting events, authenticated via HTTP Basic auth.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kissmetrics.png
layout: provider
modified: '2026-05-11'
name: Kissmetrics
nav: Providers
network: true
overview: 'Kissmetrics publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Product Analytics, Behavioral Analytics, Marketing Analytics, and Funnels.


  Kissmetrics'' developer surface includes documentation, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 53
score:
  band: minimal
  composite: 10.6
  delta: -2.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kissmetrics/refs/heads/main/screenshots/kissmetrics-2026-06-20T184049.png
security:
- kind: domain-security
  name: Kissmetrics Domain Security
  slug: kissmetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kissmetrics
tags:
- Analytics
- Product Analytics
- Behavioral Analytics
- Marketing Analytics
- Funnels
- Cohorts
website: https://www.kissmetrics.io
---
