---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Smartlook Agentic Access
  operation_count: 24
  slug: smartlook-agentic-access
  summary_line: 24 operations · 9 acting
api_count: 7
apis:
- description: Manage and query analytics events
  name: Smartlook Events API
  slug: smartlook-events-api
- description: Manage and query funnel analysis data
  name: Smartlook Funnels API
  slug: smartlook-funnels-api
- description: Upload mapping files for crash reports
  name: Smartlook mappingFiles API
  slug: smartlook-mappingfiles-api
- description: Search and retrieve session recordings
  name: Smartlook Sessions API
  slug: smartlook-sessions-api
- description: API stats and project information
  name: Smartlook System API
  slug: smartlook-system-api
- description: Manage and query visitor data
  name: Smartlook Visitors API
  slug: smartlook-visitors-api
- description: Create and manage webhooks
  name: Smartlook Webhooks API
  slug: smartlook-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smartlook REST Events API
  slug: open-smartlook-events-api
- collection_type: open
  name: Smartlook REST Events Funnels API
  slug: open-smartlook-funnels-api
- collection_type: open
  name: Smartlook REST Events mappingFiles API
  slug: open-smartlook-mappingfiles-api
- collection_type: open
  name: Smartlook REST Events Sessions API
  slug: open-smartlook-sessions-api
- collection_type: open
  name: Smartlook REST Events System API
  slug: open-smartlook-system-api
- collection_type: open
  name: Smartlook REST Events Visitors API
  slug: open-smartlook-visitors-api
- collection_type: open
  name: Smartlook REST Events Webhooks API
  slug: open-smartlook-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartlook-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartlook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartlook-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartlook.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.smartlook.com/docs/rest-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/smartlook
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartlook
- group: company
  title: ''
  type: Blog
  url: https://www.smartlook.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartlook.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://smartlook.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/getsmartlook
- group: commercial
  title: ''
  type: Plans
  url: plans/smartlook-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartlook-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smartlook-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/smartlook-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/smartlook-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Smartlook is a product analytics and session recording platform that helps businesses understand how users interact with their web and mobile applications. The platform offers a REST API for programmatically accessing session replays, heatmaps, funnel analysis, event analytics, and visitor behavior insights. Developers can retrieve data across four primary resources—Visitors, Events, Funnels, and Sessions—using bearer token authentication against regional API endpoints. Smartlook supports multiple data regions and provides SDK integrations for web, iOS, Android, and cross-platform frameworks including Cordova and React Native.
finops:
- name: Smartlook Finops
  service_category: ''
  slug: smartlook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartlook.png
jsonld:
- class_count: 14
  name: Smartlook Context
  property_count: 100
  slug: smartlook-context
layout: provider
modified: '2026-06-13'
name: Smartlook
nav: Providers
network: true
overview: 'Smartlook publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Events API, Funnels API, mappingFiles API, and 4 more. Tagged areas include Product Analytics, Session Recording, Heatmaps, Funnels, and User Behavior.


  The Smartlook catalog on APIs.io includes 1 JSON-LD context.


  Smartlook''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Smartlook Plans Pricing
  plan_count: 4
  slug: smartlook-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 0
  name: Smartlook Rate Limits
  slug: smartlook-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 21.1
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartlook/refs/heads/main/screenshots/smartlook-2026-06-20T194043.png
security:
- kind: authentication
  name: Smartlook Authentication
  slug: smartlook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smartlook Domain Security
  slug: smartlook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartlook
tags:
- Product Analytics
- Session Recording
- Heatmaps
- Funnels
- User Behavior
- Event Tracking
- Visitor Analytics
- Digital Experience
website: https://www.smartlook.com/
---
