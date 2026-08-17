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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'REST API to create and manage (deploy, start, stop, undeploy, drop) Striim applications, execute TQL commands, retrieve monitoring and file lineage data, plus WActionStore queries (GET /wactions/def, '
  name: Striim Application Management REST API
  slug: striim-application-management-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/striim-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.striim.com/feed/
- group: build
  title: ''
  type: Packages
  url: packages/striim-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/striim-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/striim-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/striim-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/striim-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/striim-conformance.yml
created: '2026-07-02'
description: Unified data integration and streaming platform offering change data capture (CDC), real-time streaming analytics, and data validation. Exposes a token-authenticated REST API (WActionStore queries, system health, Application Management) consumed against your own Striim instance or Striim Cloud service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/striim.png
layout: provider
mcp_servers:
- description: ''
  name: striim-mcp.yml
  slug: striim-mcpyml
modified: '2026-06-20'
name: Striim
nav: Providers
network: true
overview: 'Striim publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Streaming, Change Data Capture, Real-time, and Data Integration.


  Striim''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 68
score:
  band: minimal
  composite: 10.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 10.7
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Striim Domain Security
  slug: striim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: striim
tags:
- Data
- Streaming
- Change Data Capture
- Real-time
- Data Integration
- Streaming Analytics
---
