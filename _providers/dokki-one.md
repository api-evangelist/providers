---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.7
  scored_at: '2026-09-24'
api_count: 2
apis:
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: 'REST API to the same resources and permissions the Dokki app uses: workspaces and the resource tree (documents, tables, artifacts, folders, files), content and snapshots, keyword/semantic/hybrid searc'
  name: Dokki API
  slug: dokki-api
- description: Hosted remote MCP over stateless Streamable HTTP. The canonical /mcp/v2 facade exposes eight action-routed tools — find, read, create, edit, share, message, publish, connect (1000+ external integratio
  name: Dokki MCP Server
  slug: dokki-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://dokki.one/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dokki.one/pub/docs/build-with-dokki
- group: docs
  title: ''
  type: Documentation
  url: https://dokki.one/pub/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dokki.one/pub/api/api-documentation-home
- group: start
  title: ''
  type: GettingStarted
  url: https://dokki.one/pub/api/quickstart-first-request
- group: operate
  title: ''
  type: HelpCenter
  url: https://dokki.one/pub/docs/faq
- group: company
  title: ''
  type: Blog
  url: https://dokki.one/pub/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dokki-lab
- group: commercial
  title: ''
  type: Pricing
  url: https://dokki.one/plans
- group: start
  title: ''
  type: SignUp
  url: https://dokki.one/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://dokki.one/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dokki.one/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dokki.one/privacy
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://dokki.one/pub/docs/release-notes
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/changelog/dokki-one-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dokki-one-changelog.yml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dokki_one
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/llms/dokki-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokki-one-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dokki.one/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/well-known/dokki-one-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dokki-one-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/well-known/dokki-one-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/dokki-one-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/mcp/dokki-one-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dokki-one-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/mcp/dokki-one-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dokki-one-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/packages/dokki-one-packages.yml
  title: ''
  type: Packages
  url: packages/dokki-one-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/authentication/dokki-one-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dokki-one-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/scopes/dokki-one-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dokki-one-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/conformance/dokki-one-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dokki-one-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/errors/dokki-one-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dokki-one-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/conventions/dokki-one-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dokki-one-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/lifecycle/dokki-one-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dokki-one-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/plans/dokki-one-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dokki-one-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/rate-limits/dokki-one-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dokki-one-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/data-model/dokki-one-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dokki-one-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/overlays/dokki-one-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dokki-one-openapi-overlay.yaml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://dokki.one/privacy
- group: other
  title: ''
  type: ExitAssistance
  url: https://dokki.one/pub/docs/import-and-export
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dokki-one/refs/heads/main/security/dokki-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokki-one-domain-security.yml
created: '2026-09-19'
description: Dokki (UEVNS PTE. LTD., Singapore) is an agent-native collaboration workspace where people and AI agents share the same documents, tables, artifacts, chat and permissions. It exposes a 158-operation REST API under https://dokki.one/api/v1 (documented across ~200 public reference pages, no OpenAPI published — the one in this repo is generated from that reference), hosted remote MCP servers — the /mcp/v2 facade of eight action-routed tools plus preview_resource, and a legacy flat /api/mcp server — with OAuth 2.0 / OIDC discovery (RFC 8414, RFC 9728, dynamic client registration) served from its own .well-known, ten provider-published Agent Skills across Claude Code and Codex plugins, a public llms.txt, and a macOS desktop app. Formerly stubbed as "Brad" from an a2aregistry.org listing whose card is hosted on the third-party registry openagora.cc, not on a Dokki host.
image: https://dokki.one/brand/dokki-v1/icon-dark-512.png
layout: provider
mcp_servers:
- description: ''
  name: Dokki MCP Server
  slug: dokki-mcp-server
modified: '2026-09-19'
name: Dokki
nav: Providers
network: true
overview: 'Dokki publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Knowledge Management, Documents, Agents, and MCP.


  Dokki''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, release notes, and 30 more developer resources.'
plans:
- name: Dokki One Plans Pricing
  plan_count: 4
  slug: dokki-one-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Dokki One Rate Limits
  slug: dokki-one-rate-limits
scopes:
- name: Dokki One Scopes
  scope_count: 0
  slug: dokki-one-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 17.7
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 44.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dokki One Authentication
  slug: dokki-one-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Dokki One Domain Security
  slug: dokki-one-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dokki-one
tags:
- Collaboration
- Knowledge Management
- Documents
- Agents
- MCP
- Artificial Intelligence
- Productivity
- Workspace
- Publishing
- Search
- Singapore
website: https://dokki.one/
---
