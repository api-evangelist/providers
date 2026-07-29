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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Connect to bank accounts using official bank APIs and get raw transaction data
  name: Nordigen
  slug: nordigen
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nordigen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordigen.com/en/account_information_documenation/integration/quickstart_guide/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Connect to bank accounts using official bank APIs and get raw transaction data
graphqls:
- description: This is a conceptual GraphQL schema for the GoCardless Bank Account Data API (formerly Nordigen). It models the open banking REST API that enables access to EU bank account data under PSD2 regulation.
  name: GoCardless (Nordigen) GraphQL Schema
  slug: nordigen-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nordigen.png
layout: provider
modified: '2026-05-28'
name: Nordigen
nav: Providers
network: true
overview: Nordigen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 54
score:
  band: emerging
  composite: 16.5
  delta: 9.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.2
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: domain-security
  name: Nordigen Domain Security
  slug: nordigen-domain-security
  summary_line: DMARC
slug: nordigen
tags:
- Finance
- Public APIs
website: https://nordigen.com/en/account_information_documenation/integration/quickstart_guide/
---
