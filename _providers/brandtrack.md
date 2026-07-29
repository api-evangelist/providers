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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Brandtrack Agentic Access
  operation_count: 32
  slug: brandtrack-agentic-access
  summary_line: 32 operations · 18 acting
api_count: 9
apis:
- description: The Accounts API from Brandtrack — 3 operation(s) for accounts.
  name: Brandtrack Accounts API
  slug: brandtrack-accounts-api
- description: The Groups API from Brandtrack — 2 operation(s) for groups.
  name: Brandtrack Groups API
  slug: brandtrack-groups-api
- description: The Locations API from Brandtrack — 2 operation(s) for locations.
  name: Brandtrack Locations API
  slug: brandtrack-locations-api
- description: The Other API from Brandtrack — 1 operation(s) for other.
  name: Brandtrack Other API
  slug: brandtrack-other-api
- description: The Partner API from Brandtrack — 2 operation(s) for partner.
  name: Brandtrack Partner API
  slug: brandtrack-partner-api
- description: The Roles API from Brandtrack — 1 operation(s) for roles.
  name: Brandtrack Roles API
  slug: brandtrack-roles-api
- description: The Subscriptions API from Brandtrack — 2 operation(s) for subscriptions.
  name: Brandtrack Subscriptions API
  slug: brandtrack-subscriptions-api
- description: The Users API from Brandtrack — 4 operation(s) for users.
  name: Brandtrack Users API
  slug: brandtrack-users-api
- description: The Zones API from Brandtrack — 3 operation(s) for zones.
  name: Brandtrack Zones API
  slug: brandtrack-zones-api
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.brandtrack.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.brandtrack.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.brandtrack.ai/
- group: build
  title: ''
  type: Postman
  url: packages/brandtrack-postman-collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/brandtrack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brandtrack-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brandtrack-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brandtrack-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brandtrack-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brandtrack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brandtrack-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brandtrack-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brandtrack-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brandtrack-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandtrack-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brandtrack-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://help.brandtrack.fm/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.brandtrack.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brandtrack.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://new.my.brandtrack.ai/register
- group: start
  title: ''
  type: Login
  url: https://new.my.brandtrack.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brandtrack.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brandtrack.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.brandtrack.ai
created: '2026-07-17'
description: Brandtrack is a licensed background-music and in-store audio platform for commercial spaces — retail, hospitality, and food & beverage. It centralizes multi-location music management with smart scheduling, real-time playlist adaptation to signals like foot traffic, weather, and time of day, brand guardrails, AI audio-ad creation, and audit-ready licensing documentation. The Brandtrack v2 REST API manages accounts, subscriptions, users, locations, zones, groups, and roles, authenticated with an x-customer-api-key header, with a partner flow for provisioning customers.
image: https://cdn.prod.website-files.com/643faaa7da666b82bfd92bfd/6980cdfb5017b7621777a8eb_The%20right%20song%20at%20the%20right%20time%20(2).png
layout: provider
mcp_servers:
- description: ''
  name: brandtrack-mcp.yml
  slug: brandtrack-mcpyml
modified: '2026-07-18'
name: Brandtrack
nav: Providers
network: true
overview: 'Brandtrack publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Groups API, Locations API, and 6 more. Tagged areas include Company, Music, Background Music, Audio, and Streaming.


  Brandtrack''s developer surface includes documentation, API reference, authentication, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 12
scopes:
- name: Brandtrack Scopes
  scope_count: 1
  slug: brandtrack-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.2
  delta: -1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.8
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brandtrack/refs/heads/main/screenshots/brandtrack-2026-07-25T203725.png
security:
- kind: authentication
  name: Brandtrack Authentication
  slug: brandtrack-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Brandtrack Domain Security
  slug: brandtrack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brandtrack
tags:
- Company
- Music
- Background Music
- Audio
- Streaming
- Retail
- Hospitality
- In-Store Experience
- Media
- Sound
website: https://www.brandtrack.ai
---
