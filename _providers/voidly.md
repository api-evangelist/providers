---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
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
  score: 1.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries
  name: Voidly
  slug: voidly
artifact_total: 3
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/voidly-a2a.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/voidly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voidly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voidly.ai/api-docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries
layout: provider
modified: '2026-05-28'
name: Voidly
nav: Providers
network: true
overview: Voidly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 67
score:
  band: minimal
  composite: 7.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voidly/refs/heads/main/screenshots/voidly-2026-06-20T201129.png
security:
- kind: domain-security
  name: Voidly Domain Security
  slug: voidly-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Voidly Vulnerability Disclosure
  slug: voidly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: voidly
tags:
- Open Data
- Public APIs
website: https://voidly.ai/api-docs
---
