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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: API to get Information about a Minecraft Server
  name: Minecraft Server Status
  slug: minecraft-server-status
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/minecraft-server-status-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minecraft-server-status-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.mcsrvstat.us
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: API to get Information about a Minecraft Server
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/minecraft-server-status.png
layout: provider
modified: '2026-05-28'
name: Minecraft Server Status
nav: Providers
network: true
overview: Minecraft Server Status publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Games And Comics and Public APIs.
random_paper: 9
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
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/minecraft-server-status/refs/heads/main/screenshots/minecraft-server-status-2026-06-20T185600.png
security:
- kind: domain-security
  name: Minecraft Server Status Domain Security
  slug: minecraft-server-status-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Minecraft Server Status Vulnerability Disclosure
  slug: minecraft-server-status-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: minecraft-server-status
tags:
- Games And Comics
- Public APIs
website: https://api.mcsrvstat.us
---
