---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 7.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: A web-based archive of legal live audio recordings of the improvisational rock band Phish
  name: Phishin
  slug: phishin
artifact_total: 2
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/phishin-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phishin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phish.in/api-docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: A web-based archive of legal live audio recordings of the improvisational rock band Phish
layout: provider
modified: '2026-05-28'
name: Phishin
nav: Providers
network: true
overview: Phishin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music and Public APIs.
random_paper: 35
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phishin/refs/heads/main/screenshots/phishin-2026-06-20T191641.png
security:
- kind: domain-security
  name: Phishin Domain Security
  slug: phishin-domain-security
  summary_line: TLSv1.3 · HSTS
slug: phishin
tags:
- Music
- Public APIs
website: https://phish.in/api-docs
---
