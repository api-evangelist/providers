---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Pi Hole Agentic Access
  operation_count: 7
  slug: pi-hole-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 4
apis:
- description: Session authentication.
  name: Pi-hole Auth API
  slug: pi-hole-auth-api
- description: DNS blocking configuration.
  name: Pi-hole DNS API
  slug: pi-hole-dns-api
- description: Manage DNS blocking groups.
  name: Pi-hole Groups API
  slug: pi-hole-groups-api
- description: Pi-hole instance information.
  name: Pi-hole Info API
  slug: pi-hole-info-api
artifact_total: 8
collections:
- collection_type: open
  name: Pi-hole REST API
  slug: open-pi-hole
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pi-hole-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pi-hole-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pi-hole-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-pi-hole
- group: company
  title: ''
  type: Website
  url: https://pi-hole.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pi-hole.net
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pi-hole
- group: build
  title: ''
  type: Source Code
  url: https://github.com/pi-hole/pi-hole
- group: other
  title: ''
  type: FTL Source
  url: https://github.com/pi-hole/FTL
- group: learn
  title: ''
  type: Discourse Forum
  url: https://discourse.pi-hole.net
- group: other
  title: ''
  type: Donate
  url: https://pi-hole.net/donate/
- group: company
  title: ''
  type: Blog
  url: https://pi-hole.net/blog/
created: '2026-05-11'
description: Pi-hole is an open source network-wide DNS sinkhole that blocks ads, tracking, and unwanted domains across all devices on a local network without requiring per-device software. It runs on lightweight hardware such as Raspberry Pi and offers a web admin interface plus a REST API (introduced in v6 via the pihole-FTL binary) for programmatic management of blocklists, allowlists, groups, clients, DNS settings, and live query logs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pi-hole.png
layout: provider
modified: '2026-05-11'
name: Pi-hole
nav: Providers
network: true
overview: 'Pi-hole publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Auth API, DNS API, Groups API, and 1 more. Tagged areas include DNS, Ad Blocking, Network Security, Privacy, and Open Source.


  Pi-hole''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 28.1
  delta: 3.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 52.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pi-hole/refs/heads/main/screenshots/pi-hole-2026-06-20T191657.png
security:
- kind: authentication
  name: Pi Hole Authentication
  slug: pi-hole-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pi Hole Domain Security
  slug: pi-hole-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pi-hole
tags:
- DNS
- Ad Blocking
- Network Security
- Privacy
- Open Source
- Self-Hosted
website: https://pi-hole.net
---
