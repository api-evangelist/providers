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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: JSON-based REST API for Act! CRM exposing contacts, companies, groups, opportunities, activities, notes, and history. Supports OData querying and is described by an OpenAPI (Swagger) 2.0 specification
  name: Act! Web API
  slug: web-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/act-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/actsoftware
- group: company
  title: ''
  type: Website
  url: https://www.act.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.act.com/
- group: operate
  title: ''
  type: Support
  url: https://support.act.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.act.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.act.com/free-trial/
- group: company
  title: ''
  type: Blog
  url: https://www.act.com/blog/
created: '2026-05-11'
description: Act! is a CRM and marketing automation platform from Swiftpage built for small and mid-sized businesses, providing contact and activity management, opportunity tracking, email marketing, and pipeline reporting in cloud or on-premise editions. The Act! Web API is a JSON-based REST API that exposes contacts, companies, groups, opportunities, activities, notes, and history with OData query support and an OpenAPI (Swagger) 2.0 specification. The API supports both HTTP Basic Authentication and Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/act.png
layout: provider
modified: '2026-05-11'
name: Act! CRM
nav: Providers
network: true
overview: 'Act! CRM publishes 1 API on the [APIs.io](https://apis.io/) network: Act! Web API. Tagged areas include CRM, Customer Relationship Management, Marketing Automation, Contact Management, and Sales.


  Act! CRM''s developer surface includes documentation, support, pricing, signup flow, engineering blog, and 3 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 22.7
  delta: 2.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 32.3
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Act Domain Security
  slug: act-domain-security
  summary_line: TLSv1.3 · DMARC
slug: act
tags:
- CRM
- Customer Relationship Management
- Marketing Automation
- Contact Management
- Sales
- Swiftpage
website: https://www.act.com
---
