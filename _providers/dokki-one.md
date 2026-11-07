---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted remote MCP over stateless Streamable HTTP. The canonical /mcp/v2 facade exposes eight action-routed tools — find, read, create, edit, share, message, publish, connect (1000+ external integratio
  name: Dokki MCP Server
  slug: dokki-mcp-server
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Usage, credits, storage and model availability.
  name: Dokki Account API
  slug: dokki-one-account-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Agents, runs, approvals, schedules, memories, automations and work items.
  name: Dokki Agents API
  slug: dokki-one-agents-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Members, comments, permissions, access requests, pins, IM conversations and chat sessions.
  name: Dokki Collaboration API
  slug: dokki-one-collaboration-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Identity, capability discovery, API keys, notifications and workspace templates.
  name: Dokki Core API
  slug: dokki-one-core-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Organizations and org membership.
  name: Dokki Organizations API
  slug: dokki-one-organizations-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Publishing workspaces and resources to public sites.
  name: Dokki Publishing API
  slug: dokki-one-publishing-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: 'Workspaces and the resource tree: documents, tables, artifacts, folders, files, content, snapshots, tags, trash, imports, connectors and forms.'
  name: Dokki Resources API
  slug: dokki-one-resources-api
- baseURL: https://dokki.one/api/v1
  baseurl_source: declared
  description: Keyword, semantic and hybrid search.
  name: Dokki Search API
  slug: dokki-one-search-api
artifact_total: 28
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
  href: https://artifacts.apis.io/dokki-one/changelog/dokki-one-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dokki-one-changelog.yml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dokki_one
- group: agent
  href: https://artifacts.apis.io/dokki-one/llms/dokki-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokki-one-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dokki.one/llms.txt
- group: agent
  href: https://artifacts.apis.io/dokki-one/well-known/dokki-one-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dokki-one-well-known.yml
- group: other
  href: https://artifacts.apis.io/dokki-one/well-known/dokki-one-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/dokki-one-openid-configuration.json
- group: agent
  href: https://artifacts.apis.io/dokki-one/mcp/dokki-one-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dokki-one-mcp.yml
- group: build
  href: https://artifacts.apis.io/dokki-one/mcp/dokki-one-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dokki-one-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dokki-one/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/dokki-one/packages/dokki-one-packages.yml
  title: ''
  type: Packages
  url: packages/dokki-one-packages.yml
- group: auth
  href: https://artifacts.apis.io/dokki-one/authentication/dokki-one-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dokki-one-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dokki-one/scopes/dokki-one-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dokki-one-scopes.yml
- group: design
  href: https://artifacts.apis.io/dokki-one/conformance/dokki-one-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dokki-one-conformance.yml
- group: design
  href: https://artifacts.apis.io/dokki-one/errors/dokki-one-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dokki-one-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dokki-one/conventions/dokki-one-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dokki-one-conventions.yml
- group: design
  href: https://artifacts.apis.io/dokki-one/lifecycle/dokki-one-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dokki-one-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/dokki-one/plans/dokki-one-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dokki-one-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dokki-one/rate-limits/dokki-one-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dokki-one-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/dokki-one/data-model/dokki-one-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dokki-one-data-model.yml
- group: other
  href: https://artifacts.apis.io/dokki-one/overlays/dokki-one-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/dokki-one/security/dokki-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokki-one-domain-security.yml
created: '2026-09-19'
description: Dokki (UEVNS PTE. LTD., Singapore) is an agent-native collaboration workspace where people and AI agents share the same documents, tables, artifacts, chat and permissions. It exposes a 158-operation REST API under https://dokki.one/api/v1 (documented across ~200 public reference pages, no OpenAPI published — the one in this repo is generated from that reference), hosted remote MCP servers — the /mcp/v2 facade of eight action-routed tools plus preview_resource, and a legacy flat /api/mcp server — with OAuth 2.0 / OIDC discovery (RFC 8414, RFC 9728, dynamic client registration) served from its own .well-known, ten provider-published Agent Skills across Claude Code and Codex plugins, a public llms.txt, and a macOS desktop app. Formerly stubbed as "Brad" from an a2aregistry.org listing whose card is hosted on the third-party registry openagora.cc, not on a Dokki host.
finops:
- has_sources: true
  method: derived
  name: Dokki One Finops
  primary_unit: user
  service_category: ''
  slug: dokki-one-finops
  template: false
image: https://dokki.one/brand/dokki-v1/icon-dark-512.png
layout: provider
mcp_servers:
- description: 'Dokki operates hosted, remote MCP servers on its primary domain. The canonical endpoint is the /mcp/v2 FACADE: eight high-level tools (find, read, create, edit, share, message, publish, connect) plus '
  name: Dokki MCP Server
  slug: dokki-one-mcp-yml
modified: '2026-09-19'
name: Dokki
nav: Providers
network: true
overview: 'Dokki publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Collaboration API, and 6 more. Tagged areas include Collaboration, Knowledge Management, Documents, Agents, and MCP.


  The Dokki catalog on APIs.io includes 1 Spectral governance ruleset.


  Dokki''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, release notes, and 30 more developer resources.'
plans:
- name: Dokki One Plans Pricing
  plan_count: 7
  slug: dokki-one-plans-pricing
- name: Dokki One Price Estimates
  plan_count: 0
  slug: dokki-one-price-estimates
random_paper: 9
rate_limits:
- limit_count: 0
  name: Dokki One Rate Limits
  slug: dokki-one-rate-limits
rules:
- authorship: generated
  effective_rule_count: 117
  extends:
  - spectral:oas
  name: Dokki API Rules
  rule_count: 76
  severity_counts:
    error: 73
    hint: 0
    info: 1
    warn: 2
  slug: dokki-one-rules
scopes:
- name: Dokki One Scopes
  scope_count: 0
  slug: dokki-one-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 17.0
    developer_ergonomics: 41.7
    discoverability: 75.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 50.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dokki-one/dokki-one-2026-10-11T103852.png
security:
- kind: authentication
  name: Dokki One Authentication
  slug: dokki-one-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Dokki One Domain Security
  slug: dokki-one-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 10
skills:
- name: dokki-artifact
  slug: dokki-one-dokki-artifact
- name: dokki-charts
  slug: dokki-one-dokki-charts
- name: dokki-document
  slug: dokki-one-dokki-document
- name: dokki-file
  slug: dokki-one-dokki-file
- name: dokki-mcp
  slug: dokki-one-dokki-mcp
- name: dokki-publish
  slug: dokki-one-dokki-publish
- name: dokki-slides
  slug: dokki-one-dokki-slides
- name: dokki-table
  slug: dokki-one-dokki-table
- name: dokki-workspace
  slug: dokki-one-dokki-workspace
- name: dokki
  slug: dokki-one-dokki
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
