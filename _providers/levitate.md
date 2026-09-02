---
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Hosted remote MCP server (streamable HTTP) that connects Levitate to AI assistants — Claude Desktop, Claude Code, ChatGPT, Cursor, VS Code Copilot, Windsurf and any MCP-compatible HTTP client. Tools c
  name: Levitate MCP Server
  slug: levitate-mcp-server
- description: The Companies API from Levitate — 2 operation(s) for companies.
  name: Levitate Companies API
  slug: levitate-companies-api
- description: The Contacts API from Levitate — 5 operation(s) for contacts.
  name: Levitate Contacts API
  slug: levitate-contacts-api
- description: The Notes API from Levitate — 2 operation(s) for notes.
  name: Levitate Notes API
  slug: levitate-notes-api
artifact_total: 13
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/levitate-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/levitate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levitate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.levitate.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.levitate.ai/article/735-levitate-public-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.levitate.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.levitate.ai/article/322-api-keys
- group: operate
  title: ''
  type: Support
  url: https://help.levitate.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.levitate.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.levitate.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.levitate.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://login.levitate.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.levitate.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.levitate.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.levitate.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.levitate.ai/category/108-latest-releases
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.levitate.ai
- group: auth
  title: ''
  type: Compliance
  url: conformance/levitate-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/levitate-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/levitate-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/levitate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/levitate-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/levitate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/levitate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/levitate-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/levitate-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/levitate-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/levitate-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/levitate-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/levitate-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/levitate-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levitate-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/levitate-vulnerability-disclosure.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/levitate-public-v1-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/levitate-tool-crosswalk.yml
created: '2026-08-25'
description: 'Levitate is a relationship-marketing and "Happiness Platform" SaaS for relationship-based small businesses — insurance agencies, financial advisors, law firms, nonprofits, home services and faith organizations — founded in 2017 in Raleigh, North Carolina by ShareFile founder Jesse Lipson. The product combines AI-assisted personal email at scale, text messaging, social posting, surveys and event registration, review generation, meeting booking, handwritten cards, donation and opportunity boards, and website publishing, all built around a contact record that stores "key facts" (birthdays, anniversaries, hobbies) used to drive timely, personalized outreach. Levitate exposes two developer surfaces: a REST Public API (OpenAPI 3.1.1) over Contacts, Key Facts, Companies and Notes at api.levitate.ai/public/v1, authenticated with Personal API Keys or OAuth 2.0 authorization-code + PKCE bearer tokens; and a hosted, OAuth-protected remote MCP server at mcp.levitate.ai/mcp that gives AI
  assistants natural-language access to contacts, action items, donations, campaigns, opportunities, policies, notes and connected-integration data.'
image: https://cdn.prod.website-files.com/645165b093e7c8d734211d5d/64ac9c0f52d7bf5e396e6261_og%20image.png
layout: provider
mcp_servers:
- description: ''
  name: Levitate MCP Server
  slug: levitate-mcp-server
- description: ''
  name: Levitate MCP Server
  slug: levitate-mcp-server-2
modified: '2026-08-25'
name: Levitate
nav: Providers
network: true
overview: 'Levitate publishes 3 APIs on the [APIs.io](https://apis.io/) network: Companies API, Contacts API, and Notes API. Tagged areas include relationship-marketing, CRM, Email Marketing, Contacts, and Small Business.


  Levitate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 29 more developer resources.'
plans:
- name: Levitate Plans Pricing
  plan_count: 6
  slug: levitate-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Levitate Rate Limits
  slug: levitate-rate-limits
scopes:
- name: Levitate Scopes
  scope_count: 2
  slug: levitate-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 49.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 61.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Levitate Authentication
  slug: levitate-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Levitate Domain Security
  slug: levitate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Levitate Vulnerability Disclosure
  slug: levitate-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Levitate Trust Center
  slug: levitate-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II
slug: levitate
tags:
- relationship-marketing
- CRM
- Email Marketing
- Contacts
- Small Business
- Insurance
- Financial-Services
- Non-Profit
- Marketing Automation
- MCP
- agent-native
- Software-as-a-Service
website: https://www.levitate.ai/
---
