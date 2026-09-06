---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The UCP-conforming Model Context Protocol endpoint Virtuix serves from its own domain. Thirteen tools cover catalog search and lookup, product detail, cart create/update/cancel, checkout create/update
  name: Virtuix Agent Commerce (UCP / MCP)
  slug: virtuix-agent-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://virtuix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.virtuix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtuix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.virtuix.com/doxygen/Unity%20SDK%20Docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.virtuix.com/unity-import-and-install-omni-one-sdk/
- group: operate
  title: ''
  type: Support
  url: https://support.virtuix.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/qUYvWPj
- group: company
  title: ''
  type: Blog
  url: https://virtuix.com/blogs/news
- group: commercial
  title: ''
  type: Pricing
  url: https://virtuix.com/products/omni-one-developer-license
- group: start
  title: ''
  type: SignUp
  url: https://virtuix.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtuix.com/terms-of-sale
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtuix.com/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://virtuix.com/omni-one-sdk-eula
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtuix-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/virtuix-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtuix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virtuix-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtuix-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtuix-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtuix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtuix-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/virtuix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/virtuix-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/virtuix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virtuix-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtuix-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtuix-domain-security.yml
created: '2026-09-04'
description: Virtuix is an Austin, Texas maker of omnidirectional VR treadmills. Omni One pairs a full-body VR movement system with its own game store, and Omni Arena is the turnkey location-based VR esports attraction it sells to entertainment venues, with built-in contests and leaderboards. Virtuix runs a real developer program for Omni One — a licensed Unity and Unreal Engine SDK exposing Core, Application, User, Achievements, Leaderboards, Multiplayer and Entitlement Check services, plus the Omni Dev portal where studios register game projects, define leaderboards and publish to the Omni One store — but that platform is reachable only through the game-engine SDK, and Virtuix publishes no OpenAPI and no public HTTP API for it. Its one machine-callable surface is an anonymous, UCP-conforming MCP agent-commerce endpoint on its own domain, which lets an agent search the Omni One catalog and build a cart and checkout with no credential.
image: https://cdn.shopify.com/s/files/1/0609/8989/8907/files/virtuix_omni_one_og_img.jpg?v=1738174948
layout: provider
mcp_servers:
- description: ''
  name: Virtuix MCP Server
  slug: virtuix-mcp-server
modified: '2026-09-04'
name: Virtuix
nav: Providers
network: true
overview: 'Virtuix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Virtual Reality, Gaming, Hardware, Agent Commerce, and Model Context Protocol.


  Virtuix''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Virtuix Plans Pricing
  plan_count: 0
  slug: virtuix-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Virtuix Rate Limits
  slug: virtuix-rate-limits
scopes:
- name: Virtuix Scopes
  scope_count: 4
  slug: virtuix-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: falling
security:
- kind: authentication
  name: Virtuix Authentication
  slug: virtuix-authentication
  summary_line: none/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Virtuix Domain Security
  slug: virtuix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virtuix
tags:
- Virtual Reality
- Gaming
- Hardware
- Agent Commerce
- Model Context Protocol
- Universal Commerce Protocol
- Esports
- Game Development
- Location Based Entertainment
- Consumer Electronics
website: https://virtuix.com/
---
