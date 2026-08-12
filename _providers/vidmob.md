---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vidmob Agentic Access
  operation_count: 11
  slug: vidmob-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 5
apis:
- description: Hosted remote MCP server exposing Vidmob creative intelligence to AI agents — organization and ad-account structure, media-library search, creative scoring, AI-detected creative attributes, full asset
  name: Vidmob MCP Server
  slug: vidmob-mcp-server
- description: The Media API from VidMob — 5 operation(s) for media.
  name: VidMob Media API
  slug: vidmob-media-api
- description: The Organization API from VidMob — 1 operation(s) for organization.
  name: VidMob Organization API
  slug: vidmob-organization-api
- description: The Scoring API from VidMob — 4 operation(s) for scoring.
  name: VidMob Scoring API
  slug: vidmob-scoring-api
- description: The Workspaces API from VidMob — 1 operation(s) for workspaces.
  name: VidMob Workspaces API
  slug: vidmob-workspaces-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vidmob-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://vidmob.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vidmob-api-docs.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://vidmob-api-docs.readme.io/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://vidmob-api-docs.readme.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://vidmob-api-docs.readme.io/docs/glossary
- group: operate
  title: ''
  type: Support
  url: https://help.vidmob.com/en/
- group: company
  title: ''
  type: Blog
  url: https://vidblog.vidmob.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VidMob
- group: start
  title: ''
  type: SignUp
  url: https://acs.vidmob.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vidmob.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vidmob.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vidmob.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.vidmob.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/vidmob-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vidmob-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vidmob-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vidmob-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vidmob-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vidmob-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vidmob-no-data-codes.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vidmob-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vidmob-creative-scoring-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vidmob-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vidmob-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vidmob-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vidmob-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vidmob-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vidmob-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vidmob-mcp.yml
created: '2026-08-05'
description: Vidmob is a creative data platform that connects creative production to media performance for brands and agencies. Its AI analyzes the elements inside an ad creative — on-screen text, logos, objects, scenes, audio cues, storytelling approach, calls-to-action — and joins those detections to in-flight performance across Meta, TikTok, Google Ads, DV360, LinkedIn, Pinterest, Snapchat, Reddit, Amazon Advertising, The Trade Desk and Yahoo DSP. The Vidmob Public API exposes two programmatic capabilities on https://public-api.vidmob.com/v1 — Creative Scoring, which evaluates a media asset against configured brand and channel guidelines and returns a weighted score plus a per-guideline pass/fail breakdown, and Creative Aperture (Creative Tags), which returns structured AI-detected creative attributes for an asset. Both are asynchronous submit-then-poll surfaces bound to an Organization and its Workspaces. Vidmob also runs a hosted remote MCP server at https://mcp.vidmob.com/mcp with
  OAuth + PKCE, dynamic client registration and scope-gated tool visibility, so agents on Claude, ChatGPT, Gemini Enterprise or a customer's own framework can query creative inventory, scores, attributes and performance directly.
image: https://vidmob.com/hubfs/VM_FaviconArtboard%201.png
layout: provider
mcp_servers:
- description: ''
  name: vidmob-mcp.yml
  slug: vidmob-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-05'
name: VidMob
nav: Providers
network: true
overview: 'VidMob publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Media API, Organization API, Scoring API, and 1 more. Tagged areas include creative-intelligence, creative-data, advertising, marketing, and media-measurement.


  VidMob''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 61
scopes:
- name: Vidmob Scopes
  scope_count: 12
  slug: vidmob-scopes
  summary_line: 12 scopes · authorizationCode/refreshToken/jwtBearer
score:
  band: developing
  composite: 49.4
  delta: 0.4
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.3
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Vidmob Authentication
  slug: vidmob-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Vidmob Domain Security
  slug: vidmob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vidmob Trust Center
  slug: vidmob-trust-center
  summary_line: trust center published
slug: vidmob
tags:
- creative-intelligence
- creative-data
- advertising
- marketing
- media-measurement
- video
- computer-vision
- creative-analytics
- adtech
- mcp
- agent-native
- martech
website: https://vidmob.com/
---
