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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The unified Wix REST API exposes every Wix business solution — Stores, Bookings, Events, CMS/Data, Contacts, Payments, Marketing, Restaurants, Media, Members, and more — as JSON-over-HTTPS endpoints o
  name: Wix REST API
  slug: wix-rest-api
- description: 'The Wix GraphQL API (Developer Preview) exposes Wix APIs as a single unified GraphQL schema for queries and mutations, served at https://www.wixapis.com/graphql and also callable through the @wix/sdk '
  name: Wix GraphQL API
  slug: wix-graphql-api
artifact_total: 9
asyncapis:
- description: ''
  name: Wixcom Webhooks
  slug: wixcom-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wixcom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wix.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.wix.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.wix.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.wix.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.wix.com/docs/build-apps/get-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.wix.com
- group: company
  title: ''
  type: Blog
  url: https://www.wix.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wix
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wix.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://users.wix.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wix.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wix.com/about/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wix.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.wix.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wixcom-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://dev.wix.com/docs/api-reference/articles/work-with-wix-apis/platform/about-api-versions-and-deprecation
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wixcom-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wixcom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wixcom-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wixcom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wixcom-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/wixcom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wixcom-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/wixcom-cli.yml
- group: design
  title: ''
  type: Components
  url: components/wixcom-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wixcom-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wixcom-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wixcom-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wixcom-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wixcom-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wixcom-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.wix.com/website-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/wixcom-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wixcom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.wix.com/website-security
created: '2026-07-17'
description: Wix.com is a global website-building and business platform (founded 2006, 260M+ users across 190 countries) whose developer platform spans the Wix REST API at www.wixapis.com, a unified GraphQL API, the @wix JavaScript SDK family on npm, the Wix CLI for apps and headless projects, Velo site code, webhooks for every business solution (Stores, Bookings, Events, CMS, Payments, Marketing, Restaurants, and more), an official remote MCP server at mcp.wix.com, provider-published agent skills (wix/skills), and llms.txt machine-readable docs at dev.wix.com.
image: https://www.wix.com/favicon.ico
layout: provider
mcp_servers:
- description: Wix operates an official remote MCP server at https://mcp.wix.com/mcp (streamable HTTP; SSE also supported). Authentication is either the built-in OAuth flow or a Wix API key passed in the Authorizati
  name: Wix.com MCP Server
  slug: wixcom-mcp-server
modified: '2026-07-21'
name: Wix.com
nav: Providers
network: true
overview: 'Wix.com publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Website Builder, E-Commerce, CMS, and Bookings.


  The Wix.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wix.com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
random_paper: 12
scopes:
- name: Wixcom Scopes
  scope_count: 2
  slug: wixcom-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 63.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wixcom/refs/heads/main/screenshots/wixcom-2026-08-17T082949.png
security:
- kind: authentication
  name: Wixcom Authentication
  slug: wixcom-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Wixcom Domain Security
  slug: wixcom-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wixcom Vulnerability Disclosure
  slug: wixcom-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Wixcom Trust Center
  slug: wixcom-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, SOC 2 Type 2, PCI DSS Level 1, HIPAA
slug: wixcom
tags:
- Company
- Website Builder
- E-Commerce
- CMS
- Bookings
- Payments
- Headless
- Software-as-a-Service
- No-Code
website: https://www.wix.com
---
