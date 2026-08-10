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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qubit-smart-tickets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boletosqubit.co
created: '2026-07-17'
description: Qubit Smart Tickets (Boletos Qubit) is a Colombian event-ticketing platform operating at boletosqubit.co, a Spanish-language consumer web application for buying and validating tickets to concerts, sports, and live events, with local payment methods including Nequi. It was surfaced as a 500 Global portfolio company and added to the API Evangelist network as a stub. An enrichment pass on 2026-07-20 found no publicly documented API, developer portal, OpenAPI/Swagger specification, SDKs, changelog, or /.well-known discovery endpoints; the only server-side surface reachable is an internal PHP backend not intended for public integration, so no API artifacts were generated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qubit-smart-tickets.png
layout: provider
modified: '2026-07-20'
name: Qubit Smart Tickets
nav: Providers
network: true
overview: Qubit Smart Tickets is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Events, Entertainment, and Payments.
random_paper: 93
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Qubit Smart Tickets Domain Security
  slug: qubit-smart-tickets-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qubit-smart-tickets
tags:
- Company
- Ticketing
- Events
- Entertainment
- Payments
- Colombia
- Latin America
website: https://boletosqubit.co
---
