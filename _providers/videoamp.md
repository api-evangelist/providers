---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 57
  human_in_the_loop: 4
  name: Videoamp Agentic Access
  operation_count: 118
  slug: videoamp-agentic-access
  summary_line: 118 operations · 57 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: The VideoAmp Public API powers audience building and lookup, campaign and media plan creation and optimization, inventory sets, rate cards and reach curves, ad and content measurement reporting with p
  name: VideoAmp Public API
  slug: videoamp-public-api
- description: VideoAmp's hosted remote Model Context Protocol server, exposing 101 tools that mirror the VideoAmp Public API operations for audiences, measurement, planning, inventory, data streams and sharing. Str
  name: VideoAmp MCP Server
  slug: videoamp-mcp-server
artifact_total: 9
common:
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
  name: videoamp-mcp.yml
  slug: videoamp-mcpyml
modified: '2026-08-02'
name: VideoAmp
nav: Providers
network: true
overview: 'VideoAmp publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include media-measurement, advertising, adtech, tv-currency, and audience-measurement.


  VideoAmp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 23 more developer resources.'
random_paper: 62
scopes:
- name: Videoamp Scopes
  scope_count: 4
  slug: videoamp-scopes
  summary_line: 4 scopes · authorizationCode/deviceAuthorization
score:
  band: developing
  composite: 51.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 65.1
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- advertising
- adtech
- tv-currency
- audience-measurement
- media-planning
- streaming
- attribution
- data-collaboration
- mcp
- agent-native
website: https://videoamp.com/
---
