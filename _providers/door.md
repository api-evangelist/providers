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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Door Agentic Access
  operation_count: 15
  slug: door-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: User access management operations
  name: Door Access Management API
  slug: door-access-management-api
- description: Building operations
  name: Door Buildings API
  slug: door-buildings-api
- description: Door/Key and key operations
  name: Door Doors and Keys API
  slug: door-doors-and-keys-api
- description: Partner authentication operations
  name: Door Partner Authentication API
  slug: door-partner-authentication-api
- description: User authentication operations
  name: Door User Authentication API
  slug: door-user-authentication-api
- description: User operations
  name: Door Users API
  slug: door-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Authentication Access Management API
  slug: open-door-access-management-api
- collection_type: open
  name: Authentication Access Management Buildings API
  slug: open-door-buildings-api
- collection_type: open
  name: Authentication Access Management Doors and Keys API
  slug: open-door-doors-and-keys-api
- collection_type: open
  name: Authentication Access Management Partner Authentication API
  slug: open-door-partner-authentication-api
- collection_type: open
  name: Authentication Access Management User Authentication API
  slug: open-door-user-authentication-api
- collection_type: open
  name: Authentication Access Management Users API
  slug: open-door-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://door.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.door.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.door.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.door.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.door.com/docs
- group: operate
  title: ''
  type: Support
  url: https://support.door.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://door.com/articles
- group: start
  title: ''
  type: SignUp
  url: https://app.door.com
- group: start
  title: ''
  type: Login
  url: https://app.door.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://door.com/policy/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://door.com/policy/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.latch.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.door.com/docs/migrating-from-latch-sdk-v1-to-opendoor-sdk-v2.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/door-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/door-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/door-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/door-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/door-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/door-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/door-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/door-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/door-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/door-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/door-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/door-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/door-partner-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/door-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/door-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/door-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/door-changelog.yml
created: '2026-07-17'
description: DOOR (formerly Latch) is a multifamily proptech company providing a smart-building access and building-intelligence platform. It unifies smart locks, readers, intercoms, cameras, thermostats and sensors with software (DOOR OS) for property managers, and integrates with property-management systems such as Yardi, RealPage, Entrata, and AppFolio. DOOR exposes its capabilities to authorized partners through OpenDOOR - a set of REST APIs plus native iOS, Android, and Web SDKs - letting partner apps enumerate buildings, doors, keys, and users and grant, update, or revoke resident access. The API is secured with Auth0-issued JWTs (partner-scoped machine-to-machine and user-scoped passwordless tokens). This profile was enriched by the API Evangelist pipeline from DOOR's public developer hub at developers.door.com.
image: https://cdn.prod.website-files.com/6838ad705264e74df1653563/683f3efb468620cdf85dd643_door-logo-webclip.png
layout: provider
mcp_servers:
- description: ''
  name: Door MCP Server
  slug: door-mcp-server
modified: '2026-07-18'
name: Door
nav: Providers
network: true
overview: 'Door publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Access Management API, Buildings API, Doors and Keys API, and 3 more. Tagged areas include Company, Access Control, Smart Building, PropTech, and Physical Security.


  Door''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 44.3
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 51.4
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/door/refs/heads/main/screenshots/door-2026-07-25T212301.png
security:
- kind: authentication
  name: Door Authentication
  slug: door-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Door Domain Security
  slug: door-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: door
tags:
- Company
- Access Control
- Smart Building
- PropTech
- Physical Security
- IoT
- Multifamily
- Real-Estate
- Smart Lock
- Building Automation
website: https://door.com/
---
