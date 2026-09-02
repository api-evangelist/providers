---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The News API from NewTqnia | Technology News, AI and Innovation — 2 operation(s) for news.
  name: NewTqnia | Technology News, AI and Innovation News API
  slug: newtqnia-news-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://newtqnia.com/mcp
- group: other
  title: ''
  type: Overlay
  url: overlays/newtqnia-daily-digest-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://newtqnia.com/en/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://newtqnia.com/en/connect
- group: operate
  title: ''
  type: Support
  url: https://newtqnia.com/en/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newtqnia
- group: start
  title: ''
  type: SignUp
  url: https://newtqnia.com/en/register
- group: start
  title: ''
  type: Login
  url: https://newtqnia.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newtqnia.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newtqnia.com/en/privacy
- group: build
  title: ''
  type: Packages
  url: packages/newtqnia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/newtqnia-packages.yml
- group: design
  title: ''
  type: Components
  url: components/newtqnia-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/newtqnia-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newtqnia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/newtqnia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newtqnia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newtqnia-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newtqnia-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/newtqnia-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newtqnia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/newtqnia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/newtqnia-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newtqnia-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-28'
description: 'An independent bilingual (English/Arabic) technology newsroom covering artificial intelligence, cybersecurity, developer tools, science, space, robotics, energy and global technology policy. NewTqnia ships a genuinely keyless public REST news API (the Daily Digest, at api.newtqnia.com), an OpenAPI 3.1 contract, a hosted Streamable-HTTP MCP server whose tools/list is anonymously discoverable, an llms.txt, OAuth 2.1 + PKCE discovery documents, an embeddable news widget with a WordPress plugin, and four MIT-licensed first-party SDKs for Python, Node/TypeScript, PHP and Go. Every API response carries its own attribution licence: displaying ''Powered by NewTqnia'' with a visible link and preserving the returned article URLs is a condition of use.'
examples:
- key_count: 1
  name: Newtqnia Error 404
  slug: newtqnia-error-404
- key_count: 11
  name: Newtqnia Getlatestnews 200 Ar
  slug: newtqnia-getLatestNews-200-ar
- key_count: 12
  name: Newtqnia Gettodaysnews 200
  slug: newtqnia-getTodaysNews-200
image: https://newtqnia.com/storage/social/ce46e49c898edb9ac69deab4c3a4cf41bf569102-1200x630.jpg
layout: provider
mcp_servers:
- description: ''
  name: NewTqnia | Technology News, AI and Innovation MCP Server
  slug: newtqnia-technology-news-ai-and-innovation-mcp-server
modified: '2026-08-28'
name: NewTqnia | Technology News, AI and Innovation
nav: Providers
network: true
overview: 'NewTqnia | Technology News, AI and Innovation publishes 1 API on the [APIs.io](https://apis.io/) network: News API. Tagged areas include News API, News, Technology, Artificial Intelligence, and Cybersecurity.


  NewTqnia | Technology News, AI and Innovation''s developer surface includes getting-started guide, support, signup flow, authentication, changelog, and 20 more developer resources.'
plans:
- name: Newtqnia Plans Pricing
  plan_count: 3
  slug: newtqnia-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Newtqnia Rate Limits
  slug: newtqnia-rate-limits
scopes:
- name: Newtqnia Scopes
  scope_count: 0
  slug: newtqnia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 53.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Newtqnia Authentication
  slug: newtqnia-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Newtqnia Domain Security
  slug: newtqnia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newtqnia
tags:
- News API
- News
- Technology
- Artificial Intelligence
- Cybersecurity
- Developer Tools
- Cloud Computing
- Media
- Publishing
- Bilingual
website: https://newtqnia.com/en/developers
---
