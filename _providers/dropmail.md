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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: GraphQL API for creating and managing ephemeral e-mail inboxes
  name: DropMail
  slug: dropmail
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dropmail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dropmail.me/api/#live-demo
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: GraphQL API for creating and managing ephemeral e-mail inboxes
graphqls:
- description: ''
  name: DropMail GraphQL API
  slug: dropmail-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dropmail.png
layout: provider
modified: '2026-05-28'
name: DropMail
nav: Providers
network: true
overview: DropMail publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email and Public APIs.
random_paper: 111
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dropmail/refs/heads/main/screenshots/dropmail-2026-06-20T180245.png
security:
- kind: domain-security
  name: Dropmail Domain Security
  slug: dropmail-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dropmail
tags:
- Email
- Public APIs
website: https://dropmail.me/api/#live-demo
---
