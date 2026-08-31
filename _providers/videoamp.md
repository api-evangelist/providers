---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 57
  human_in_the_loop: 4
  name: Videoamp Agentic Access
  operation_count: 118
  slug: videoamp-agentic-access
  summary_line: 118 operations · 57 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: VideoAmp's hosted remote Model Context Protocol server, exposing 101 tools that mirror the VideoAmp Public API operations for audiences, measurement, planning, inventory, data streams and sharing. Str
  name: VideoAmp MCP Server
  slug: videoamp-mcp-server
- description: adMeasurements operations.
  name: VideoAmp Ad Measurements API
  slug: videoamp-admeasurements-api
- description: audiences operations.
  name: VideoAmp Audiences API
  slug: videoamp-audiences-api
- description: campaigns operations.
  name: VideoAmp Campaigns API
  slug: videoamp-campaigns-api
- description: consents operations.
  name: VideoAmp Consents API
  slug: videoamp-consents-api
- description: content operations.
  name: VideoAmp Content API
  slug: videoamp-content-api
- description: currency-of-record operations.
  name: VideoAmp Currency Of Record API
  slug: videoamp-currency-of-record-api
- description: dataStreams operations.
  name: VideoAmp Data Streams API
  slug: videoamp-datastreams-api
- description: dataStreamTypes operations.
  name: VideoAmp Data Stream Types API
  slug: videoamp-datastreamtypes-api
- description: inventories operations.
  name: VideoAmp Inventories API
  slug: videoamp-inventories-api
- description: library operations.
  name: VideoAmp Library API
  slug: videoamp-library-api
- description: me operations.
  name: VideoAmp Me API
  slug: videoamp-me-api
- description: plans operations.
  name: VideoAmp Plans API
  slug: videoamp-plans-api
- description: reports operations.
  name: VideoAmp Reports API
  slug: videoamp-reports-api
- description: shares operations.
  name: VideoAmp Shares API
  slug: videoamp-shares-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VideoAmp Public Ad Measurements API
  slug: open-videoamp-admeasurements-api
- collection_type: open
  name: VideoAmp Public Audiences API
  slug: open-videoamp-audiences-api
- collection_type: open
  name: VideoAmp Public Campaigns API
  slug: open-videoamp-campaigns-api
- collection_type: open
  name: VideoAmp Public Consents API
  slug: open-videoamp-consents-api
- collection_type: open
  name: VideoAmp Public Content API
  slug: open-videoamp-content-api
- collection_type: open
  name: VideoAmp Public Currency Of Record API
  slug: open-videoamp-currency-of-record-api
- collection_type: open
  name: VideoAmp Public Data Streams API
  slug: open-videoamp-datastreams-api
- collection_type: open
  name: VideoAmp Public Data Stream Types API
  slug: open-videoamp-datastreamtypes-api
- collection_type: open
  name: VideoAmp Public Inventories API
  slug: open-videoamp-inventories-api
- collection_type: open
  name: VideoAmp Public Library API
  slug: open-videoamp-library-api
- collection_type: open
  name: VideoAmp Public Me API
  slug: open-videoamp-me-api
- collection_type: open
  name: VideoAmp Public Plans API
  slug: open-videoamp-plans-api
- collection_type: open
  name: VideoAmp Public Reports API
  slug: open-videoamp-reports-api
- collection_type: open
  name: VideoAmp Public Shares API
  slug: open-videoamp-shares-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/videoamp-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://videoamp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.videoamp.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.videoamp.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.videoamp.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/VideoAmp/cli#mcp-getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.videoamp.dev/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.videoamp.dev/
- group: company
  title: ''
  type: Blog
  url: https://videoamp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VideoAmp
- group: start
  title: ''
  type: Login
  url: https://platform.videoamp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://videoamp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://videoamp.com/privacy-notices/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.videoamp.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/videoamp-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/videoamp-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/videoamp-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/videoamp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/videoamp-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/videoamp-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/videoamp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/videoamp-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/videoamp-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/videoamp-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/videoamp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/videoamp-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/videoamp-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/videoamp-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/videoamp-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/videoamp-llms.txt
created: '2026-08-02'
description: VideoAmp is a Los Angeles-based media measurement and advertising technology company, founded in 2014, that operates as a certified national TV currency provider alongside Nielsen and Comscore. Its platform unifies linear TV, streaming and digital viewership onto a single dataset and identity spine (VALID) so agencies, brands and publishers can build audiences, plan and optimize cross-screen media, and measure ad and content outcomes. VideoAmp exposes this as a read-and-write Public API at api.videoamp.dev covering audiences, campaigns, media plans, inventories and rate cards, reach curves, ad and content measurement, data streams and ingestion, and cross-organization data sharing and consent — plus a first-party CLI and a hosted remote MCP server so agents can drive the same operations.
image: https://videoamp.com/wp-content/uploads/2020/06/5e8e31e378cb39dc533b5e00_blog_covid19-response.jpg
layout: provider
mcp_servers:
- description: ''
  name: VideoAmp MCP
  slug: videoamp-mcp
modified: '2026-08-02'
name: VideoAmp
nav: Providers
network: true
overview: 'VideoAmp publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Ad Measurements API, Audiences API, Campaigns API, and 11 more. Tagged areas include media-measurement, Advertising, adtech, tv-currency, and audience-measurement.


  VideoAmp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 24 more developer resources.'
random_paper: 13
scopes:
- name: Videoamp Scopes
  scope_count: 4
  slug: videoamp-scopes
  summary_line: 4 scopes · authorizationCode/deviceAuthorization
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 58.1
    developer_ergonomics: 57.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/videoamp/refs/heads/main/screenshots/videoamp-2026-08-17T082744.png
security:
- kind: authentication
  name: Videoamp Authentication
  slug: videoamp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Videoamp Domain Security
  slug: videoamp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Videoamp Vulnerability Disclosure
  slug: videoamp-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Videoamp Trust Center
  slug: videoamp-trust-center
  summary_line: trust center published
slug: videoamp
tags:
- media-measurement
- Advertising
- adtech
- tv-currency
- audience-measurement
- media-planning
- streaming
- Attribution
- data-collaboration
- MCP
- agent-native
website: https://videoamp.com/
---
