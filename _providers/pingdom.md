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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for managing uptime checks, transaction checks, results, alerts, contacts, maintenance windows, teams, and reports in the Pingdom monitoring platform. Authentication uses Bearer token API key
  name: Pingdom Public API
  slug: public-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pingdom-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pingdom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pingdom
- group: company
  title: ''
  type: Website
  url: https://www.pingdom.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pingdom.com/
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.pingdom.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pingdom.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.pingdom.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://my.pingdom.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pingdom.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.pingdom.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pingdom.com/
- group: other
  title: ''
  type: Parent Company
  url: https://www.solarwinds.com/
created: '2026-05-11'
description: Pingdom is a website uptime and performance monitoring service from SolarWinds that tracks availability, response time, transactions, real user monitoring, and page speed from a global network of probe servers. It alerts teams via email, SMS, webhooks, and integrations when websites, APIs, or critical user journeys experience downtime or degraded performance. The Pingdom Public REST API (v3.1) provides programmatic access to checks, results, alerts, contacts, maintenance windows, and reports using Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pingdom.png
layout: provider
modified: '2026-05-11'
name: Pingdom
nav: Providers
network: true
overview: 'Pingdom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, Uptime Monitoring, Website Monitoring, Performance Monitoring, and Real User Monitoring.


  Pingdom''s developer surface includes documentation, pricing, signup flow, engineering blog, support, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.9
  delta: 2.4
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 16.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pingdom/refs/heads/main/screenshots/pingdom-2026-06-20T191713.png
security:
- kind: domain-security
  name: Pingdom Domain Security
  slug: pingdom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pingdom
tags:
- Monitoring
- Uptime Monitoring
- Website Monitoring
- Performance Monitoring
- Real User Monitoring
- Synthetic Monitoring
- Observability
website: https://www.pingdom.com
---
