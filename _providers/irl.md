---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://irl.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/irl_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/irl-domain-security.yml
coverage:
  checked: '2026-08-23'
  detail: IRL (Get Together, Inc.) was dissolved by its own board in June 2023 after a special committee found ~95% of its users were bots; irl.com now returns only an asset-inquiry notice, the Postman-hosted developer docs at docs.irl.com are deleted, and api.irl.com is a dangling CNAME to a removed AWS Elastic Beanstalk environment.
  evidence:
  - status: 200
    url: https://irl.com/
  - status: 404
    url: https://docs.irl.com/
  - status: 403
    url: https://irl.com/openapi.json
  - status: 200
    url: https://www.irl.com/.well-known/api-catalog
  - status: 0
    url: https://api.irl.com/
  reason: defunct
  state: none
created: '2026-08-23'
description: 'IRL (legal name Get Together, Inc.) was a San Francisco social calendar and group-messaging app that let people share and sync calendars with friends and follow venues, organizations and notable figures. It raised more than $200 million in venture capital, including a $170 million Series C led by SoftBank Vision Fund 2 in 2021 that valued the company at $1.17 billion. In June 2023 a special committee of the board reported that roughly 95 percent of the app''s claimed users were automated or bot accounts, and the board voted to dissolve the company; the SEC charged founder and former CEO Abraham Shafi with fraud on July 31, 2024. The company is defunct: irl.com now serves only an asset-inquiry notice, the marketing and app hosts are abandoned Netlify shells, docs.irl.com (Postman-hosted developer docs) returns 404, and api.irl.com is a dangling CNAME to a deleted AWS Elastic Beanstalk environment. No public API, OpenAPI, SDK, or developer program remains.'
image: https://www.irl.com/apple-touch-icon.png
layout: provider
modified: '2026-08-23'
name: IRL
nav: Providers
network: true
overview: IRL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Messaging, Events, and Calendar.
random_paper: 12
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Irl Domain Security
  slug: irl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: irl
tags:
- Company
- Social
- Messaging
- Events
- Calendar
- Consumer
- Mobile
- Defunct
website: https://irl.com/
---
