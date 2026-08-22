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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.parative.com/
- group: build
  title: ''
  type: Packages
  url: packages/parative-packages.yml
coverage:
  checked: '2026-08-13'
  detail: Parative's team and technology were acquired by Totango on 2024-10-22 and folded into Totango's Unison churn-intelligence line, and the company has since been fully decommissioned rather than redirected — parative.com still holds an active registration delegating to four Route 53 nameservers, but the hosted zone behind it is gone, so every host (apex, www, api, docs, developer, app) returns SERVFAIL and no HTTP connection can be opened at all; the only surviving first-party artifact is the npm package @parative/library, whose publishing stopped on 2024-08-07, ten weeks before the acquisition was announced.
  evidence:
  - status: 0
    url: https://parative.com/.well-known/agent-card.json
  - status: 0
    url: https://parative.com/openapi.json
  - status: 0
    url: https://www.parative.com/
  - status: 200
    url: https://registry.npmjs.org/@parative/library
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Parative was an AI-powered customer intelligence / customer behavior platform (founded 2017, Boston, MA) that surfaced product-usage signals to define ICP fit, forecast net revenue retention, and predict churn, renewal, and expansion for go-to-market and customer success teams. It was surfaced in the API Evangelist network as a portfolio company of bain-capital-ventures (sector: ai-apps). Parative was acquired by Totango on 2024-10-22 and no longer operates independently; its domain parative.com no longer resolves (no DNS/NS records) and it exposes no reachable public API, developer portal, or documentation surface. Its product API was never public: an Amplify config embedded in the company''s own published npm package shows the backend was a private AWS AppSync GraphQL endpoint (us-west-2, Cognito User Pools auth) serving its React web client, and that endpoint no longer resolves either. One first-party artifact outlives the domain — the npm package @parative/library, the
  compiled front-end of the Parative app, last published 2024-08-07. This profile is retained as a historical company record.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parative.png
layout: provider
modified: '2026-08-13'
name: Parative
nav: Providers
network: true
overview: Parative is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Customer Intelligence, Customer Success, and Net Revenue Retention.
random_paper: 20
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: parative
tags:
- Company
- Ai Apps
- Customer Intelligence
- Customer Success
- Net Revenue Retention
- Product Usage Analytics
- Go To Market
website: https://www.parative.com/
---
