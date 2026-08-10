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
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: HCM v2 REST API for accessing worker demographics, payroll, time and attendance, benefits, talent, and organization data in ADP Workforce Now. Authentication uses OAuth 2.0 (client credentials) with m
  name: ADP Workforce Now HCM API
  slug: hcm-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adp-workforce-now-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.adp.com/~/spark_feed/insights-trends
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/adpworkforcenow
- group: company
  title: ''
  type: Website
  url: https://www.adp.com/what-we-offer/products/adp-workforce-now.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://developers.adp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.adp.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adp.com/what-we-offer/products/adp-workforce-now.aspx
- group: start
  title: ''
  type: Signup
  url: https://developers.adp.com/register
- group: start
  title: ''
  type: Login
  url: https://workforcenow.adp.com
- group: other
  title: ''
  type: Marketplace
  url: https://apps.adp.com
- group: operate
  title: ''
  type: Support
  url: https://www.adp.com/contact-us/customer-service.aspx
created: '2026-05-11'
description: ADP Workforce Now is ADP's cloud-based human capital management (HCM) suite for mid-sized businesses, covering payroll, HR, benefits administration, time and attendance, talent management, and analytics in a single platform. The product offers tax filing, compliance reporting, mobile self-service, and marketplace integrations through ADP's developer ecosystem. The ADP Workforce Now APIs (HCM v2) use OAuth 2.0 / OpenID Connect with mutual TLS client certificates and expose worker, payroll, time, benefits, and talent data through ADP API Central.
graphqls:
- description: This directory contains a conceptual GraphQL schema for the ADP Workforce Now HCM v2 REST API. ADP Workforce Now is ADP's cloud-based human capital management (HCM) suite for mid-sized businesses, cov
  name: ADP Workforce Now GraphQL Schema
  slug: adp-workforce-now-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adp-workforce-now.png
layout: provider
modified: '2026-05-11'
name: ADP Workforce Now
nav: Providers
network: true
overview: 'ADP Workforce Now publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HCM, Human Capital Management, Payroll, HR, and Workforce Management.


  ADP Workforce Now''s developer surface includes engineering blog, documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 93
score:
  band: emerging
  composite: 27.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 43.2
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adp-workforce-now/refs/heads/main/screenshots/adp-workforce-now-2026-06-20T165101.png
security:
- kind: domain-security
  name: Adp Workforce Now Domain Security
  slug: adp-workforce-now-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adp-workforce-now
tags:
- HCM
- Human Capital Management
- Payroll
- HR
- Workforce Management
- Benefits
- Time and Attendance
- Talent Management
website: https://www.adp.com/what-we-offer/products/adp-workforce-now.aspx
---
