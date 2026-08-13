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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Knowi Agentic Access
  operation_count: 26
  slug: knowi-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Obtain and revoke bearer tokens.
  name: Knowi Authentication API
  slug: knowi-authentication-api
- description: Manage dashboards and shared URLs.
  name: Knowi Dashboards API
  slug: knowi-dashboards-api
- description: Manage user groups.
  name: Knowi Groups API
  slug: knowi-groups-api
- description: Retrieve dataset contents.
  name: Knowi Pull API
  slug: knowi-pull-api
- description: Send data to Knowi datasets in real time.
  name: Knowi Push API
  slug: knowi-push-api
- description: Manage workspace users.
  name: Knowi Users API
  slug: knowi-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Knowi Management API
  slug: open-knowi-management-api
- collection_type: open
  name: Knowi Push Data API
  slug: open-knowi-push-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knowi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/knowi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knowi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knowi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud9-charts
- group: company
  title: ''
  type: Website
  url: https://www.knowi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.knowi.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.knowi.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.knowi.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.knowi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.knowi.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.knowi.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.knowi.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://knowi.com/llms.txt
created: '2026-03-26'
description: Knowi is an analytics and business intelligence platform with native integration to NoSQL, SQL, and REST API data sources, providing AI-powered analytics, embedded dashboards, and natural language querying.
finops:
- name: Knowi Finops
  service_category: API
  slug: knowi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knowi.png
layout: provider
modified: '2026-05-19'
name: Knowi
nav: Providers
network: true
overview: 'Knowi publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Dashboards API, Groups API, and 3 more. Tagged areas include AI Analytics, API Analytics, Business Intelligence, Data Visualization, and Embedded Analytics.


  Knowi''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, support, and 8 more developer resources.'
plans:
- name: Knowi Plans Pricing
  plan_count: 3
  slug: knowi-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Knowi Rate Limits
  slug: knowi-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.7
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knowi/refs/heads/main/screenshots/knowi-2026-06-20T184113.png
security:
- kind: authentication
  name: Knowi Authentication
  slug: knowi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Knowi Domain Security
  slug: knowi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Knowi Trust Center
  slug: knowi-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: knowi
tags:
- AI Analytics
- API Analytics
- Business Intelligence
- Data Visualization
- Embedded Analytics
- NoSQL Analytics
website: https://www.knowi.com
---
