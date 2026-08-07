---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-06'
api_count: 7
apis:
- description: Canopy API for self-service tasking of Umbra's SAR satellite constellation. Create feasibility requests to discover collection opportunities for a target, submit Tasks in Spotlight, Dwell or Scan imag
  name: Umbra Canopy Tasking API
  slug: tasking
- description: Spec-compliant SpatioTemporal Asset Catalog (STAC) API v2 over the Collects an organization has tasked. Implements the STAC API Item Search Specification and the STAC API Filter Extension, with simple
  name: Umbra Canopy STAC API v2
  slug: stac-api-v2
- description: STAC API over Umbra's Archive Catalog of previously collected SAR imagery. Supports simple and advanced item search with the STAC API Filter Extension, collection listing and retrieval, single-item lo
  name: Umbra Canopy Archive Catalog (STAC) API
  slug: stac-archive
- description: Canopy API for delivery of Umbra customer data. Create, list, delete and verify DeliveryConfigs that push collected SAR products directly into a customer-owned AWS S3 or Google Cloud Storage bucket, a
  name: Umbra Canopy Delivery API
  slug: delivery
- description: Canopy Admin API for machine-to-machine token management and organization configuration. Create, read, rotate and delete the organization's OAuth2 client credentials, read organization settings, and r
  name: Umbra Canopy Admin API
  slug: admin
- description: Canopy API for map tiles and preview images. Generates a preview of a cloud-optimized GeoTIFF (COG) dataset for display in map and imagery viewers.
  name: Umbra Canopy Tiles API
  slug: tiles
- description: 'Anonymous, hosted Model Context Protocol server published by Umbra on the Canopy documentation host. Exposes six tools that let an agent enumerate the Canopy OpenAPI specs, list and search endpoints, '
  name: Umbra Canopy Documentation MCP Server
  slug: docs-mcp
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://umbra.space/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.canopy.umbra.space/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.canopy.umbra.space/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.canopy.umbra.space/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.canopy.umbra.space/docs/task-lifecycle-tutorial
- group: operate
  title: ''
  type: Support
  url: https://help.umbra.space/
- group: company
  title: ''
  type: Blog
  url: https://umbra.space/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://umbra.space/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Umbra-Space
- group: commercial
  title: ''
  type: Pricing
  url: https://umbra.space/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://canopy.umbra.space/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://umbra.space/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://umbra.space/privacy-notice/
- group: other
  title: ''
  type: OpenData
  url: https://umbra.space/open-data/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.canopy.umbra.space/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/umbra-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.canopy.umbra.space/docs/versioning-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/umbra-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/umbra-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/umbra-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/umbra-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/umbra-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/umbra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/umbra-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/umbra-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/umbra-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/umbra-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/umbra-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/umbra-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/umbra-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/umbra-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/umbra-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/umbra-domain-security.yml
created: '2026-08-05'
description: 'Umbra is an American space technology company operating a constellation of commercial synthetic aperture radar (SAR) satellites capable of sub-25cm resolution imaging, day or night and through cloud cover. Its Canopy platform gives customers self-service access to the constellation through both a web application and a public REST API: customers calculate tasking feasibility against targets of interest, submit Tasks to collect new imagery in Spotlight, Dwell or Scan imaging modes, track Task and Collect status through the full collection-downlink-processing-delivery lifecycle, search a STAC-compliant archive catalog of existing imagery, and configure direct data delivery into their own AWS S3 or Google Cloud Storage buckets. Umbra licenses its imagery under CC BY 4.0, publishes open pricing, and runs an open data program.'
image: https://umbra.space/wp-content/uploads/2025/10/cropped-site-identifier-logo_.png
layout: provider
mcp_servers:
- description: ''
  name: umbra-mcp.yml
  slug: umbra-mcpyml
modified: '2026-08-05'
name: Umbra
nav: Providers
network: true
overview: 'Umbra publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Canopy Tasking API, Canopy STAC API v2, Canopy Archive Catalog (STAC) API, and 3 more. Tagged areas include Satellite Imagery, Synthetic Aperture Radar, Earth Observation, Geospatial, and Space.


  Umbra''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 83
rate_limits:
- limit_count: 6
  name: Umbra Rate Limits
  slug: umbra-rate-limits
scopes:
- name: Umbra Scopes
  scope_count: 0
  slug: umbra-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.3
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Umbra Authentication
  slug: umbra-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Umbra Domain Security
  slug: umbra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: umbra
tags:
- Satellite Imagery
- Synthetic Aperture Radar
- Earth Observation
- Geospatial
- Space
- STAC
- Remote Sensing
- Tasking
- Defense and Intelligence
- Company
website: https://umbra.space/
---
