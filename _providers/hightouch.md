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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hightouch Agentic Access
  operation_count: 13
  slug: hightouch-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 4
apis:
- description: Data destinations
  name: Hightouch Destinations API
  slug: hightouch-destinations-api
- description: Data models
  name: Hightouch Models API
  slug: hightouch-models-api
- description: Data sources
  name: Hightouch Sources API
  slug: hightouch-sources-api
- description: Data syncs and runs
  name: Hightouch Syncs API
  slug: hightouch-syncs-api
artifact_total: 13
collections:
- collection_type: open
  name: Hightouch Management API
  slug: open-hightouch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hightouch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hightouch-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hightouch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hightouch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hightouchio
- group: company
  title: ''
  type: Website
  url: https://hightouch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hightouch.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hightouch.com/docs/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://hightouch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://hightouch.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.hightouch.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hightouchio
- group: agent
  title: ''
  type: LlmsText
  url: https://hightouch.com/llms.txt
created: '2026-03-27'
description: Hightouch is a composable Customer Data Platform (CDP) and data activation platform that syncs data from warehouses such as Snowflake and BigQuery to more than 300 SaaS destinations including Salesforce, HubSpot, Google Ads, and Facebook Ads. The platform supports reverse ETL, audience segmentation, journey orchestration, real-time personalization, AI Decisioning, and an Ad Studio for advertising campaigns. A Resource API provides programmatic management of the platform with git version control and approval workflows.
finops:
- name: Hightouch Finops
  service_category: API
  slug: hightouch-finops
graphqls:
- description: Hightouch is a composable Customer Data Platform (CDP) and data activation platform that syncs data from cloud data warehouses such as Snowflake and BigQuery to over 300 SaaS destinations. The platfor
  name: Hightouch GraphQL API
  slug: hightouch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hightouch.png
layout: provider
modified: '2026-05-19'
name: Hightouch
nav: Providers
network: true
overview: 'Hightouch publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Destinations API, Models API, Sources API, and 1 more. Tagged areas include CDP, Data Activation, Reverse ETL, Audience Management, and Unified API.


  Hightouch''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Hightouch Plans Pricing
  plan_count: 3
  slug: hightouch-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Hightouch Rate Limits
  slug: hightouch-rate-limits
score:
  band: developing
  composite: 44.4
  delta: -0.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 59.9
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hightouch/refs/heads/main/screenshots/hightouch-2026-06-20T182738.png
security:
- kind: authentication
  name: Hightouch Authentication
  slug: hightouch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hightouch Domain Security
  slug: hightouch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hightouch Trust Center
  slug: hightouch-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: hightouch
tags:
- CDP
- Data Activation
- Reverse ETL
- Audience Management
- Unified API
- Marketing
website: https://hightouch.com/
---
