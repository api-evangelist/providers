---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.8
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: 'Anonymous, hosted Model Context Protocol server published by Umbra on the Canopy documentation host. Exposes six tools that let an agent enumerate the Canopy OpenAPI specs, list and search endpoints, '
  name: Umbra Canopy Documentation MCP Server
  slug: docs-mcp
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Client Credentials API from Umbra — 1 operation(s) for client credentials.
  name: Umbra Client Credentials API
  slug: umbra-client-credentials-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Collections API from Umbra — 4 operation(s) for collections.
  name: Umbra Collections API
  slug: umbra-collections-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The CollectMetadata API from Umbra — 1 operation(s) for collectmetadata.
  name: Umbra Collect Metadata API
  slug: umbra-collectmetadata-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Collects API from Umbra — 2 operation(s) for collects.
  name: Umbra Collects API
  slug: umbra-collects-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The DeliveryConfig API from Umbra — 3 operation(s) for deliveryconfig.
  name: Umbra Delivery Config API
  slug: umbra-deliveryconfig-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Feasibility API from Umbra — 2 operation(s) for feasibility.
  name: Umbra Feasibility API
  slug: umbra-feasibility-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Organizations API from Umbra — 2 operation(s) for organizations.
  name: Umbra Organizations API
  slug: umbra-organizations-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Preview API from Umbra — 1 operation(s) for preview.
  name: Umbra Preview API
  slug: umbra-preview-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Preview Image API from Umbra — 1 operation(s) for preview image.
  name: Umbra Preview Image API
  slug: umbra-preview-image-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Product Constraints API from Umbra — 1 operation(s) for product constraints.
  name: Umbra Product Constraints API
  slug: umbra-product-constraints-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Restricted Access Areas API from Umbra — 1 operation(s) for restricted access areas.
  name: Umbra Restricted Access Areas API
  slug: umbra-restricted-access-areas-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Search API from Umbra — 2 operation(s) for search.
  name: Umbra Search API
  slug: umbra-search-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Tasks API from Umbra — 5 operation(s) for tasks.
  name: Umbra Tasks API
  slug: umbra-tasks-api
- baseURL: https://api.canopy.umbra.space/tasking
  baseurl_source: declared
  description: The Thumbnail API from Umbra — 1 operation(s) for thumbnail.
  name: Umbra Thumbnail API
  slug: umbra-thumbnail-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Admin Client Credentials API
  slug: open-umbra-client-credentials-api
- collection_type: open
  name: Umbra Collections API
  slug: open-umbra-collections-api
- collection_type: open
  name: Delivery Collect Metadata API
  slug: open-umbra-collectmetadata-api
- collection_type: open
  name: Tasking Collects API
  slug: open-umbra-collects-api
- collection_type: open
  name: Delivery Delivery Config API
  slug: open-umbra-deliveryconfig-api
- collection_type: open
  name: Tasking Feasibility API
  slug: open-umbra-feasibility-api
- collection_type: open
  name: Admin Organizations API
  slug: open-umbra-organizations-api
- collection_type: open
  name: Admin Product Constraints API
  slug: open-umbra-product-constraints-api
- collection_type: open
  name: Tasking Restricted Access Areas API
  slug: open-umbra-restricted-access-areas-api
- collection_type: open
  name: Umbra Search API
  slug: open-umbra-search-api
- collection_type: open
  name: Tasking Tasks API
  slug: open-umbra-tasks-api
- collection_type: open
  name: STAC Archive Thumbnail API
  slug: open-umbra-thumbnail-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/umbra-admin-overlay.yaml
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
  name: Umbra MCP Server
  slug: umbra-mcp-server
modified: '2026-08-05'
name: Umbra
nav: Providers
network: true
overview: 'Umbra publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Client Credentials API, Collections API, Collect Metadata API, and 11 more. Tagged areas include Satellite Imagery, Synthetic Aperture Radar, Earth Observation, Geospatial, and Space.


  Umbra''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 10
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
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 46.1
  previous_composite: 44.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/umbra/refs/heads/main/screenshots/umbra-2026-08-17T082544.png
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
