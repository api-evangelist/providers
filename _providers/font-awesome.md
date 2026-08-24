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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Public GraphQL API for programmatically querying Font Awesome releases, searching icons and their metadata (family-styles, unicode, aliases, SVG path data), and — with an access token — reading accoun
  name: Font Awesome GraphQL API
  slug: font-awesome-graphql-api
artifact_total: 9
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fontawesome.com/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fontawesome.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fontawesome.com/apis/graphql/query-fields
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fontawesome.com/apis/graphql/get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/font-awesome-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/font-awesome-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/font-awesome-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/font-awesome-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/font-awesome-cli.yml
- group: design
  title: ''
  type: Components
  url: components/font-awesome-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/font-awesome-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/font-awesome-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/font-awesome-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/font-awesome-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/font-awesome-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/font-awesome-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/font-awesome-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/font-awesome-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/font-awesome-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.fontawesome.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FortAwesome
- group: commercial
  title: ''
  type: Pricing
  url: https://fontawesome.com/plans
- group: start
  title: ''
  type: Login
  url: https://fontawesome.com/account
- group: operate
  title: ''
  type: Support
  url: https://fontawesome.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fontawesome.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fontawesome.com/license
created: '2026-07-17'
description: Font Awesome is the web's most popular icon library and toolkit, providing thousands of SVG, font, and CSS icons across multiple styles and families for web, desktop, and mobile projects. Beyond the icon sets and framework components (React, Vue, Angular, Ember, Svelte, React Native, WordPress), Font Awesome operates a public GraphQL API at api.fontawesome.com that lets developers programmatically query releases, search icons and their metadata, resolve family-styles and unicode values, and — with an authenticated access token — read account Kits, entitlements, and download subsets. The API uses a token-exchange endpoint that resolves an account API token into a short-lived bearer access token scoped by permission (public, kits_read, svg_icons_free, svg_icons_pro, and more). Font Awesome also ships a first-party `fa` CLI and official AI agent skills for icon discovery and setup.
image: https://fontawesome.com/images/open-graph/default.png
layout: provider
mcp_servers:
- description: ''
  name: Font Awesome MCP Server
  slug: font-awesome-mcp-server
modified: '2026-07-19'
name: Font Awesome
nav: Providers
network: true
overview: 'Font Awesome publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Icons, SVG, Fonts, Web Design, and Developer Tools.


  Font Awesome''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 20 more developer resources.'
random_paper: 19
scopes:
- name: Font Awesome Scopes
  scope_count: 8
  slug: font-awesome-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 43.3
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 50.3
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/font-awesome/refs/heads/main/screenshots/font-awesome-2026-07-25T214913.png
security:
- kind: authentication
  name: Font Awesome Authentication
  slug: font-awesome-authentication
  summary_line: http/bearer/token-exchange · 2 schemes
- kind: domain-security
  name: Font Awesome Domain Security
  slug: font-awesome-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: add-icon
  slug: add-icon
- name: fa-help
  slug: fa-help
- name: setup-fa
  slug: setup-fa
- name: suggest-icon
  slug: suggest-icon
slug: font-awesome
tags:
- Icons
- SVG
- Fonts
- Web Design
- Developer Tools
- GraphQL
- Icon Library
- Frontend
- Design System
- Company
website: https://docs.fontawesome.com/apis/
---
