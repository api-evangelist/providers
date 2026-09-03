---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://nip.io/
- group: company
  title: ''
  type: Website
  url: https://sslip.io/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cunnie/sslip.io
- group: commercial
  title: ''
  type: License
  url: https://github.com/cunnie/sslip.io/blob/main/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/nipio-source-repo.json
created: '2026-08-23'
description: 'nip.io and sslip.io are a single wildcard-DNS service that resolves any hostname containing an embedded IP address to that address — 93-184-216-34.nip.io and 93.184.216.34.sslip.io both return 93.184.216.34, with no signup, no configuration and no records to create. It exists so developers can put a real hostname in front of an arbitrary IP for local development, TLS testing, Kubernetes ingress and CI, and it has been in operation for over ten years. The operators state the service answers more than 20,000 queries per second. The DNS server behind it is open source: cunnie/sslip.io, written in Go and licensed Apache-2.0.'
layout: provider
modified: '2026-08-23'
name: nip.io / sslip.io
nav: Providers
network: true
overview: nip.io / sslip.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include DNS, wildcard dns, Developer Tools, and Infrastructure.
random_paper: 18
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 98.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 31.5
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 3.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nipio/refs/heads/main/screenshots/nipio-2026-09-02T150755.png
slug: nipio
tags:
- DNS
- wildcard dns
- Developer Tools
- Infrastructure
website: https://nip.io/
---
