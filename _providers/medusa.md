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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: ''
  name: Medusa GraphQL API
  slug: medusa-graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medusa-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://medusajs.com/blog/
description: Medusa is an open-source headless commerce platform with a modular architecture.
graphqls:
- description: Medusa is an open-source headless commerce platform with a modular architecture that enables developers to build custom commerce applications. The GraphQL API exposes the full store surface for buildi
  name: Medusa GraphQL API
  slug: medusa-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medusa.png
layout: provider
name: Medusa
nav: Providers
network: true
overview: 'Medusa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Headless Commerce, Open-Source, GraphQL, and Node.js.


  Medusa''s developer surface includes engineering blog and 1 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 2.4
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 15.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medusa/refs/heads/main/screenshots/medusa-2026-08-07T172412.png
security:
- kind: domain-security
  name: Medusa Domain Security
  slug: medusa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medusa
tags:
- E-Commerce
- Headless Commerce
- Open-Source
- GraphQL
- Node.js
---
