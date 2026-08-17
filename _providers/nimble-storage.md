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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: REST API served on each Nimble Storage array (NimbleOS 5.x) for managing arrays, pools, volumes, snapshots, volume/snapshot collections, protection templates, initiator groups, access control records,
  name: NimbleOS REST API
  slug: nimbleos-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: http://www.nimblestorage.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hpe.com/platform/hpe-nimble-storage/home/
- group: docs
  title: ''
  type: Documentation
  url: https://infosight.hpe.com/InfoSight/media/cms/active/public/pubs_REST_API_Reference_NOS_51x.whz/jun1455055569904.html
- group: docs
  title: ''
  type: APIReference
  url: https://infosight.hpe.com/InfoSight/media/cms/active/public/pubs_REST_API_Reference_NOS_51x.whz/omq1488160167637.html
- group: company
  title: ''
  type: Blog
  url: https://developer.hpe.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NimbleStorage
- group: build
  title: ''
  type: Packages
  url: packages/nimble-storage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nimble-storage-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nimble-storage-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nimble-storage-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nimble-storage-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nimble-storage-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nimble-storage-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nimble-storage-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nimble-storage-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nimble-storage-domain-security.yml
created: '2026-07-17'
description: Nimble Storage is an enterprise flash and adaptive-flash storage platform, acquired by Hewlett Packard Enterprise in 2017 and now part of the HPE Nimble Storage / HPE Alletra 6000 product line. Its NimbleOS software exposes a REST API for programmatic management of arrays, storage pools, volumes, snapshots, initiator groups, and data-protection policies. The API is served per-array at https://<array>:5392/v1/ using session-token (X-Auth-Token) authentication, and HPE publishes first-party Python, Go, and Ansible client libraries for it. Originally venture-backed by Accel and Lightspeed Venture Partners, the company was added to the API Evangelist network and enriched from its public developer surface.
image: https://avatars.githubusercontent.com/u/9436637
layout: provider
mcp_servers:
- description: ''
  name: nimble-storage-mcp.yml
  slug: nimble-storage-mcpyml
modified: '2026-07-20'
name: Nimble Storage
nav: Providers
network: true
overview: 'Nimble Storage publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Big Data, Storage, Data Storage, and Infrastructure.


  Nimble Storage''s developer surface includes documentation, API reference, engineering blog, authentication, and 12 more developer resources.'
random_paper: 92
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 17.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nimble-storage/refs/heads/main/screenshots/nimble-storage-2026-08-07T185308.png
security:
- kind: authentication
  name: Nimble Storage Authentication
  slug: nimble-storage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nimble Storage Domain Security
  slug: nimble-storage-domain-security
  summary_line: DMARC
slug: nimble-storage
tags:
- Company
- Big Data
- Storage
- Data Storage
- Infrastructure
- Enterprise
- HPE
website: http://www.nimblestorage.com
---
