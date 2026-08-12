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
    agent_skills: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-11'
api_count: 7
apis:
- description: The authorizations API from OpenLattice — 1 operation(s) for authorizations.
  name: OpenLattice authorizations API
  slug: openlattice-authorizations-api
- description: API endpoints to reading and writing data.
  name: OpenLattice data API
  slug: openlattice-data-api
- description: API endpoints to the entity data model.
  name: OpenLattice edm API
  slug: openlattice-edm-api
- description: API endpoints related to organizations.
  name: OpenLattice organizations API
  slug: openlattice-organizations-api
- description: API endpoints for permissions for organisations, roles and users.
  name: OpenLattice permissions API
  slug: openlattice-permissions-api
- description: The principal API from OpenLattice — 5 operation(s) for principal.
  name: OpenLattice principal API
  slug: openlattice-principal-api
- description: API endpoints to search data.
  name: OpenLattice search API
  slug: openlattice-search-api
artifact_total: 10
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/openlattice-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openlattice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openlattice-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/openlattice-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openlattice-packages.yml
- group: design
  title: ''
  type: Components
  url: components/openlattice-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openlattice-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openlattice-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openlattice-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openlattice-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openlattice
- group: company
  title: ''
  type: Website
  url: https://github.com/openlattice
created: '2026-07-17'
description: OpenLattice was a data-integration and analytics platform built around an Entity Data Model (EDM) — a graph of entity types, property types, association types, and EntitySets — with a fine-grained ACL permissions model over organizations, roles, and principals. It was adopted by public-sector and criminal-justice programs such as reentry case management, community work programs, childcare, and courts. The company's hosted service and website (openlattice.com, api.openlattice.com) no longer resolve, but its OpenAPI 3.0 specification (91 operations), multi-language SDKs, and React UI kit remain published under the github.com/openlattice organization, from which this profile was enriched.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openlattice.png
layout: provider
mcp_servers:
- description: ''
  name: openlattice-mcp.yml
  slug: openlattice-mcpyml
modified: '2026-07-20'
name: OpenLattice
nav: Providers
network: true
overview: 'OpenLattice publishes 7 APIs on the [APIs.io](https://apis.io/) network, including authorizations API, data API, edm API, and 4 more. Tagged areas include Company, Data Integration, Entity Data Model, Public Sector, and Analytics.


  OpenLattice''s developer surface includes authentication and 12 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 25.6
  delta: -1.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 48.5
    developer_ergonomics: 21.2
    discoverability: 81.5
    governance: 8.3
    operational_transparency: 5.3
  previous_composite: 26.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openlattice/refs/heads/main/screenshots/openlattice-2026-08-07T190610.png
security:
- kind: authentication
  name: Openlattice Authentication
  slug: openlattice-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Openlattice Domain Security
  slug: openlattice-domain-security
  summary_line: no transport/DNS hardening detected
slug: openlattice
tags:
- Company
- Data Integration
- Entity Data Model
- Public Sector
- Analytics
- Graph
- Criminal Justice
---
