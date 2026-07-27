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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Modern REST API for managing contacts, companies, opportunities, tags, emails, appointments, notes, and tasks in Keap CRM. Authentication uses OAuth 2.0 with the authorization code and refresh token g
  name: Keap REST API v2
  slug: rest-v2
- description: Original REST API for Keap (formerly Infusionsoft) covering contacts, orders, products, subscriptions, campaigns, files, tags, and merchants. Authentication uses OAuth 2.0 with Bearer access tokens.
  name: Keap REST API v1
  slug: rest-v1
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infusionsoft-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infusionsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keap-growing
- group: company
  title: ''
  type: Website
  url: https://keap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.infusionsoft.com
- group: commercial
  title: ''
  type: Pricing
  url: https://keap.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://keap.com/signup
- group: operate
  title: ''
  type: Developer Community
  url: https://integration.keap.com
created: '2026-05-11'
description: Infusionsoft, now branded as Keap, is a sales and marketing automation CRM built for small businesses that combines contact management, email marketing, e-commerce, pipeline automation, appointments, and invoicing in a single platform. Keap exposes REST APIs (v1 and v2) and a legacy XML-RPC API for managing contacts, companies, opportunities, orders, products, tags, emails, and campaigns, all authenticated via OAuth 2.0 authorization code and refresh token grants.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infusionsoft.png
layout: provider
modified: '2026-05-11'
name: Infusionsoft (Keap)
nav: Providers
network: true
overview: 'Infusionsoft (Keap) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Marketing Automation, Sales Automation, Email Marketing, and E-Commerce.


  Infusionsoft (Keap)''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 27
score:
  band: minimal
  composite: 13.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infusionsoft/refs/heads/main/screenshots/infusionsoft-2026-06-20T183345.png
security:
- kind: domain-security
  name: Infusionsoft Domain Security
  slug: infusionsoft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: infusionsoft
tags:
- CRM
- Marketing Automation
- Sales Automation
- Email Marketing
- E-Commerce
- Small Business
website: https://keap.com
---
