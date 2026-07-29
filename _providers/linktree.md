---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Linktree Agentic Access
  operation_count: 30
  slug: linktree-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- description: OAuth 2.0-protected Model Context Protocol server, speaking streamable-http, that lets agents manage Linktree profiles, links, collections, appearance, social icon links, workspaces, and analytics. Th
  name: Linktree MCP
  slug: linktree-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://linktr.ee/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://linktr.ee/marketplace/developer
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.linktr.ee/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.linktr.ee/docs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linktree-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linktree-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linktree-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linktree-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linktree-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linktree-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linktree-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/linktree-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://linktr.ee/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linktree-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linktree-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.linktr.ee/
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.getbeamer.com/linktree/en
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/linktree-mbb-og
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linktree-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/linktree-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linktree-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.linktr.ee/en/collections/3020860-getting-started-with-linktree
- group: operate
  title: ''
  type: Support
  url: https://linktr.ee/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.linktr.ee/
- group: company
  title: ''
  type: Blog
  url: https://linktr.ee/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://linktr.ee/s/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://linktr.ee/register
- group: start
  title: ''
  type: Login
  url: https://linktr.ee/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linktr.ee/s/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linktr.ee/s/privacy/
- group: other
  title: ''
  type: Marketplace
  url: https://linktr.ee/marketplace
- group: company
  title: ''
  type: About
  url: https://linktr.ee/s/about/
- group: operate
  title: ''
  type: Contact
  url: https://linktr.ee/s/contact/
- group: company
  title: ''
  type: Press
  url: https://linktr.ee/s/about/press/
created: '2026-07-17'
description: Linktree is the link-in-bio platform used by 70M+ creators, brands, and businesses to share everything they create, curate, and sell from a single URL. Operated by Linktree Pty Ltd from Collingwood, Victoria, Australia, the product builds a mobile-friendly landing page that aggregates social profiles, content, products, and services behind one link, with paid Starter, Pro, and Premium plans adding customization, analytics, commerce, scheduling, and AI features. Linktree publishes no general-purpose public REST API — its developer program is an expression-of-interest waitlist for forthcoming APIs and SDKs. It does, however, run a live, fully documented OAuth 2.0-protected Model Context Protocol server at mcp.linktr.ee exposing 30 tools for managing profiles, links, collections, appearance, social icons, workspaces, and analytics, discoverable from an RFC 9727 api-catalog on the apex domain.
image: https://linktr.ee/_marketing/og/linktree-default.jpg
layout: provider
mcp_servers:
- description: ''
  name: linktree-mcp.yml
  slug: linktree-mcpyml
modified: '2026-07-19'
name: Linktree
nav: Providers
network: true
overview: 'Linktree publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Link in Bio, Creator Economy, and Social Media.


  Linktree''s developer surface includes documentation, API reference, authentication, changelog, getting-started guide, support, engineering blog, and 28 more developer resources.'
random_paper: 15
scopes:
- name: Linktree Scopes
  scope_count: 30
  slug: linktree-scopes
  summary_line: 30 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 42.1
  previous_composite: 38.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linktree/refs/heads/main/screenshots/linktree-2026-07-25T225257.png
security:
- kind: authentication
  name: Linktree Authentication
  slug: linktree-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Linktree Domain Security
  slug: linktree-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Linktree Vulnerability Disclosure
  slug: linktree-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Linktree Trust Center
  slug: linktree-trust-center
  summary_line: trust center published
slug: linktree
tags:
- Company
- Media
- Link in Bio
- Creator Economy
- Social Media
- Marketing
- Analytics
- MCP
- Agents
website: https://linktr.ee/
---
