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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Mireye Agentic Access
  operation_count: 30
  slug: mireye-agentic-access
  summary_line: 30 operations · 22 acting · 3 human-in-the-loop
api_count: 17
apis:
- description: The Ask API from Mireye — 2 operation(s) for ask.
  name: Mireye Ask API
  slug: mireye-ask-api
- description: The Ask Site API from Mireye — 1 operation(s) for ask site.
  name: Mireye Ask Site API
  slug: mireye-ask-site-api
- description: The Auth API from Mireye — 1 operation(s) for auth.
  name: Mireye Auth API
  slug: mireye-auth-api
- description: The Authorize API from Mireye — 1 operation(s) for authorize.
  name: Mireye Authorize API
  slug: mireye-authorize-api
- description: The Feature Requests API from Mireye — 1 operation(s) for feature requests.
  name: Mireye Feature Requests API
  slug: mireye-feature-requests-api
- description: The Fetch API from Mireye — 1 operation(s) for fetch.
  name: Mireye Fetch API
  slug: mireye-fetch-api
- description: The Healthz API from Mireye — 1 operation(s) for healthz.
  name: Mireye Healthz API
  slug: mireye-healthz-api
- description: The Mcp API from Mireye — 3 operation(s) for mcp.
  name: Mireye Mcp API
  slug: mireye-mcp-api
- description: The Meta API from Mireye — 1 operation(s) for meta.
  name: Mireye Meta API
  slug: mireye-meta-api
- description: The Oauth API from Mireye — 4 operation(s) for oauth.
  name: Mireye Oauth API
  slug: mireye-oauth-api
- description: The Readyz API from Mireye — 1 operation(s) for readyz.
  name: Mireye Readyz API
  slug: mireye-readyz-api
- description: The Register API from Mireye — 1 operation(s) for register.
  name: Mireye Register API
  slug: mireye-register-api
- description: The Revoke API from Mireye — 1 operation(s) for revoke.
  name: Mireye Revoke API
  slug: mireye-revoke-api
- description: The Sites API from Mireye — 2 operation(s) for sites.
  name: Mireye Sites API
  slug: mireye-sites-api
- description: The Token API from Mireye — 1 operation(s) for token.
  name: Mireye Token API
  slug: mireye-token-api
- description: The Users API from Mireye — 5 operation(s) for users.
  name: Mireye Users API
  slug: mireye-users-api
- description: The .well Known API from Mireye — 1 operation(s) for .well known.
  name: Mireye .well Known API
  slug: mireye-well-known-api
artifact_total: 22
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mireye.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mireye.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mireye.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mireye.ai/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://www.mireye.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mireye.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mireye.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mireye.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.mireye.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.mireye.ai/mcp/troubleshooting
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mireye-Labs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mireye.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mireye-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mireye-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mireye-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mireye-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mireye-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mireye-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mireye-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mireye-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mireye-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mireye-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mireye-openapi-overlay.yaml
- group: build
  title: ''
  type: CLI
  url: cli/mireye-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/mireye-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mireye-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mireye-agentic-access.yml
created: '2026-07-17'
description: 'Mireye is infrastructure for physical-world AI agents, turning any US latitude and longitude into sourced, structured geospatial ground truth. Its Mireye Earth API exposes two HTTP endpoints — POST /v1/fetch for deterministic per-field values and POST /v1/ask for natural-language, citation-backed Q&A — plus GET /v1/meta/fields for a self-describing catalog of 175+ fields across seven layers (terrain, land cover, built environment, utilities and energy, climate and resource, hazards, and parcels and boundaries) and 14 preset bundles. Every value carries provenance: the source identifier, upstream URL, dataset vintage, timestamp, and a confidence rating, sourced from federal agencies (USGS, NOAA, USDA, USFS, FEMA, EPA, EIA, NREL, US Census) and open and commercial datasets (Sentinel-2, Overture Maps, Regrid). Mireye also runs a hosted OAuth 2.1 MCP server (com.mireye/earth) and a local stdio adapter so agents in Claude, Cursor, and custom loops can query the earth as easily as
  the web. Founded 2026 by Ansh Chokshi and Shashwat Kapoor; Y Combinator S26.'
image: https://www.mireye.com/assets/favicon-Bk0nCQH7.svg
layout: provider
mcp_servers:
- description: ''
  name: mireye-mcp.yml
  slug: mireye-mcpyml
modified: '2026-07-20'
name: Mireye
nav: Providers
network: true
overview: 'Mireye publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Ask API, Ask Site API, Auth API, and 14 more. Tagged areas include Company, Geospatial, Geographic Information System, Location, and AI Agents.


  Mireye''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 21 more developer resources.'
random_paper: 71
scopes:
- name: Mireye Scopes
  scope_count: 1
  slug: mireye-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 49.3
  delta: -1.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 43.1
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mireye/refs/heads/main/screenshots/mireye-2026-08-07T183719.png
security:
- kind: authentication
  name: Mireye Authentication
  slug: mireye-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mireye Domain Security
  slug: mireye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mireye
tags:
- Company
- Geospatial
- Geographic Information System
- Location
- AI Agents
- Model Context Protocol
- Government Data
- Risk
- Insurance
- Data
website: https://docs.mireye.ai
---
