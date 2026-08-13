---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightloom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightloom.com/
- group: company
  title: ''
  type: Press
  url: https://www.brightloom.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.brightloom.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.brightloom.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightloom
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Brightloom
coverage:
  checked: '2026-08-08'
  detail: Brightloom sells its restaurant customer data platform as an end-user SaaS with prebuilt POS/loyalty connectors and ships no developer surface at all — its own homepage nav points at /how-it-works/, /integrations/, /sign-up/, /security/, /privacy/ and /terms/ and every one of them 404s on a 2023-vintage site whose /about/ page now serves injected SEO spam, no api./docs./developer./app. subdomain resolves for brightloom.com, and the legacy Eatsa API host api.eatsa.com is NXDOMAIN.
  evidence:
  - status: 200
    url: https://www.brightloom.com/
  - status: 404
    url: https://www.brightloom.com/integrations/
  - status: 404
    url: https://www.brightloom.com/openapi.json
  - status: 404
    url: https://www.brightloom.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: 'Brightloom is a San Francisco customer data and customer intelligence platform for restaurant and retail brands. It began as Eatsa, the automated quinoa-bowl restaurant chain, and rebranded to Brightloom in 2019 when Starbucks licensed select components of its Digital Flywheel customer engagement software to the company, took an equity stake and a board seat alongside a $30M round. The product unifies point-of-sale, loyalty, ecommerce and marketing data into a single customer view, reports on data health, runs AI-driven hyper-segmentation and anomaly detection over that data, and recommends the next campaign and audience a brand should target. Brightloom is sold as an end-user SaaS with prebuilt connectors to common POS, loyalty and marketing platforms rather than as a developer platform: it publishes no public API reference, developer portal, SDK or machine-readable specification.'
image: https://www.brightloom.com/assets/components/axl.theme/site/media/fav/apple-touch-icon_v-2.2.png
layout: provider
modified: '2026-08-08'
name: Brightloom
nav: Providers
network: true
overview: Brightloom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Data Platform, Customer Intelligence, Restaurants, and Retail.
random_paper: 119
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Brightloom Domain Security
  slug: brightloom-domain-security
  summary_line: TLSv1.3
slug: brightloom
tags:
- Company
- Customer Data Platform
- Customer Intelligence
- Restaurants
- Retail
- Marketing
- Loyalty
- Segmentation
- Point of Sale
- Analytics
website: https://www.brightloom.com/
---
