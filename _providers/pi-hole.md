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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Pi Hole Agentic Access
  operation_count: 7
  slug: pi-hole-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
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
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pi-hole REST Auth API
  slug: open-pi-hole-auth-api
- collection_type: open
  name: Pi-hole REST Auth DNS API
  slug: open-pi-hole-dns-api
- collection_type: open
  name: Pi-hole REST Auth Groups API
  slug: open-pi-hole-groups-api
- collection_type: open
  name: Pi-hole REST Auth Info API
  slug: open-pi-hole-info-api
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
overview: 'Pi-hole publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Auth API, DNS API, Groups API, and 1 more. Tagged areas include DNS, Ad Blocking, Network Security, Privacy, and Open-Source.


  Pi-hole''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 23.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Open-Source
- Self-Hosted
website: https://pi-hole.net
---
