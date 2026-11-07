---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 50
  human_in_the_loop: 4
  name: Videoamp Agentic Access
  operation_count: 118
  slug: videoamp-agentic-access
  summary_line: 118 operations · 50 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: VideoAmp's hosted remote Model Context Protocol server, exposing 101 tools that mirror the VideoAmp Public API operations for audiences, measurement, planning, inventory, data streams and sharing. Str
  name: VideoAmp MCP Server
  slug: videoamp-mcp-server
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: adMeasurements operations.
  name: VideoAmp Ad Measurements API
  slug: videoamp-admeasurements-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: audiences operations.
  name: VideoAmp Audiences API
  slug: videoamp-audiences-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: campaigns operations.
  name: VideoAmp Campaigns API
  slug: videoamp-campaigns-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: consents operations.
  name: VideoAmp Consents API
  slug: videoamp-consents-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: content operations.
  name: VideoAmp Content API
  slug: videoamp-content-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: currency-of-record operations.
  name: VideoAmp Currency Of Record API
  slug: videoamp-currency-of-record-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: dataStreamTypes operations.
  name: VideoAmp Data Stream Types API
  slug: videoamp-datastreamtypes-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: inventories operations.
  name: VideoAmp Inventories API
  slug: videoamp-inventories-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: library operations.
  name: VideoAmp Library API
  slug: videoamp-library-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: me operations.
  name: VideoAmp Me API
  slug: videoamp-me-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: plans operations.
  name: VideoAmp Plans API
  slug: videoamp-plans-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: reports operations.
  name: VideoAmp Reports API
  slug: videoamp-reports-api
- baseURL: https://api.videoamp.dev
  baseurl_source: declared
  description: shares operations.
  name: VideoAmp Shares API
  slug: videoamp-shares-api
- baseURL: https://api.videoamp.dev/v1/mcp
  baseurl_source: declared
  description: dataStreams operations.
  name: VideoAmp Data Streams API
  slug: videoamp-data-streams-api
artifact_total: 42
collections:
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
- group: company
  title: ''
  type: BlogRSS
  url: https://videoamp.com/feed/
- group: other
  href: https://artifacts.apis.io/videoamp/overlays/videoamp-public-api-overlay.yaml
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
  href: https://artifacts.apis.io/videoamp/changelog/videoamp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/videoamp-changelog.yml
- group: build
  href: https://artifacts.apis.io/videoamp/cli/videoamp-cli.yml
  title: ''
  type: CLI
  url: cli/videoamp-cli.yml
- group: build
  href: https://artifacts.apis.io/videoamp/packages/videoamp-packages.yml
  title: ''
  type: Packages
  url: packages/videoamp-packages.yml
- group: agent
  href: https://artifacts.apis.io/videoamp/mcp/videoamp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/videoamp-mcp.yml
- group: build
  href: https://artifacts.apis.io/videoamp/mcp/videoamp-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/videoamp-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/videoamp/well-known/videoamp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/videoamp-well-known.yml
- group: auth
  href: https://artifacts.apis.io/videoamp/authentication/videoamp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/videoamp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/videoamp/scopes/videoamp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/videoamp-scopes.yml
- group: design
  href: https://artifacts.apis.io/videoamp/conventions/videoamp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/videoamp-conventions.yml
- group: design
  href: https://artifacts.apis.io/videoamp/conformance/videoamp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/videoamp-conformance.yml
- group: design
  href: https://artifacts.apis.io/videoamp/errors/videoamp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/videoamp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/videoamp/lifecycle/videoamp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/videoamp-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/videoamp/security/videoamp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/videoamp-domain-security.yml
- group: design
  href: https://artifacts.apis.io/videoamp/data-model/videoamp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/videoamp-data-model.yml
- group: agent
  href: https://artifacts.apis.io/videoamp/agentic-access/videoamp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/videoamp-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/videoamp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/videoamp/llms/videoamp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/videoamp-llms.txt
created: '2026-08-02'
description: VideoAmp is a Los Angeles-based media measurement and advertising technology company, founded in 2014, that operates as a certified national TV currency provider alongside Nielsen and Comscore. Its platform unifies linear TV, streaming and digital viewership onto a single dataset and identity spine (VALID) so agencies, brands and publishers can build audiences, plan and optimize cross-screen media, and measure ad and content outcomes. VideoAmp exposes this as a read-and-write Public API at api.videoamp.dev covering audiences, campaigns, media plans, inventories and rate cards, reach curves, ad and content measurement, data streams and ingestion, and cross-organization data sharing and consent — plus a first-party CLI and a hosted remote MCP server so agents can drive the same operations.
image: https://videoamp.com/wp-content/uploads/2020/06/5e8e31e378cb39dc533b5e00_blog_covid19-response.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.videoamp.dev over HTTP; 101 tools listed.
  name: VideoAmp MCP
  slug: videoamp-mcp
modified: '2026-10-06'
name: VideoAmp
nav: Providers
network: true
overview: 'VideoAmp publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Measurements API, Audiences API, Campaigns API, and 12 more. Tagged areas include Media Measurement, Advertising, AdTech, tv-currency, and Audience Measurement.


  The VideoAmp catalog on APIs.io includes 1 Spectral governance ruleset.


  VideoAmp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 25 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: VideoAmp API Rules
  rule_count: 68
  severity_counts:
    error: 60
    hint: 0
    info: 2
    warn: 6
  slug: videoamp-rules
scopes:
- name: Videoamp Scopes
  scope_count: 4
  slug: videoamp-scopes
  summary_line: 4 scopes · authorizationCode/deviceAuthorization
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 57.7
    discoverability: 75.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.1
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/videoamp/videoamp-2026-08-17T082744.png
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
skill_count: 5
skills:
- name: Build a VideoAmp audience and export it
  slug: videoamp-build-and-export-audience
- name: Onboard a data stream into VideoAmp
  slug: videoamp-onboard-data-stream
- name: Plan and optimize a VideoAmp media buy
  slug: videoamp-plan-and-optimize-media
- name: Run a VideoAmp ad measurement report
  slug: videoamp-run-ad-measurement
- name: Share VideoAmp audiences and revoke access
  slug: videoamp-share-and-revoke-audiences
slug: videoamp
tags:
- Media Measurement
- Advertising
- AdTech
- tv-currency
- Audience Measurement
- Media Planning
- Streaming
- Attribution
- Data Collaboration
- MCP
- Agent-Native
website: https://videoamp.com/
---
