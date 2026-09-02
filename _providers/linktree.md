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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Linktree Agentic Access
  operation_count: 30
  slug: linktree-agentic-access
  summary_line: 30 operations
api_count: 2
apis:
- description: OAuth 2.0-protected Model Context Protocol server, speaking streamable-http, that lets agents manage Linktree profiles, links, collections, appearance, social icon links, workspaces, and analytics. Th
  name: Linktree MCP
  slug: linktree-mcp
- description: Arbor is Linktree's design system, published as a public HTTP component registry. Anonymous, unauthenticated GETs return a versioned JSON manifest of 51 React components (/manifest.json, registry vers
  name: Linktree Arbor Registry
  slug: linktree-arbor-registry
artifact_total: 11
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
- group: build
  title: ''
  type: Packages
  url: packages/linktree-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/linktree-cli.yml
- group: design
  title: ''
  type: Components
  url: components/linktree-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/linktree-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linktree-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blstrco
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
description: Linktree is the link-in-bio platform used by 70M+ creators, brands, and businesses to share everything they create, curate, and sell from a single URL. Operated by Linktree Pty Ltd from Collingwood, Victoria, Australia, the product builds a mobile-friendly landing page that aggregates social profiles, content, products, and services behind one link, with paid Starter, Pro, and Premium plans adding customization, analytics, commerce, scheduling, and AI features. Linktree publishes no general-purpose public REST API — its developer program is an expression-of-interest waitlist for forthcoming APIs and SDKs. It does, however, run a live, fully documented OAuth 2.0-protected Model Context Protocol server at mcp.linktr.ee exposing 30 tools for managing profiles, links, collections, appearance, social icons, workspaces, and analytics, discoverable from an RFC 9727 api-catalog on the apex domain. Alongside it Linktree operates Arbor, a public unauthenticated component registry at arbor.linktr.ee
  serving a versioned JSON manifest of 51 React components plus a health endpoint and an llms.txt, and it ships first-party developer tooling on npm under the @linktr.ee scope — the LinkApps scaffold/build/deploy CLIs and a stdio Arbor MCP server.
image: https://linktr.ee/_marketing/og/linktree-default.jpg
layout: provider
mcp_servers:
- description: Manage Linktree profiles, links, appearance, and analytics via the Model Context Protocol.
  name: Linktree MCP
  slug: linktree-mcp
modified: '2026-08-13'
name: Linktree
nav: Providers
network: true
overview: 'Linktree publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Link in Bio, Creator Economy, and Social-Media.


  Linktree''s developer surface includes documentation, API reference, authentication, CLI, changelog, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Linktree Plans Pricing
  plan_count: 5
  slug: linktree-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Linktree Rate Limits
  slug: linktree-rate-limits
scopes:
- name: Linktree Scopes
  scope_count: 30
  slug: linktree-scopes
  summary_line: 30 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 44.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Social-Media
- Marketing
- Analytics
- MCP
- Agents
- Design System
- Developer Tools
website: https://linktr.ee/
---
