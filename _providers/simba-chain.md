---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-09-16'
api_count: 2
apis:
- description: The SIMBA Build dynamic API generator. When a smart contract is deployed into an application, Blocks auto-generates REST endpoints for every method and public variable of that contract — POST to invok
  name: SIMBA Blocks Platform Service (Dynamic Contract API)
  slug: simba-chain-platform-service-api
- description: A live, unauthenticated remote Model Context Protocol server published on SIMBA's own documentation host. tools/list returns four tools — searchDocumentation, getPage, askQuestion and sendFeedback — t
  name: SIMBA Blocks Documentation MCP Server
  slug: simba-chain-documentation-mcp
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Authentication API from SIMBA Chain — 9 operation(s) for authentication.
  name: SIMBA Chain Authentication API
  slug: simba-chain-authentication-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Bulk Users Import Requests API from SIMBA Chain — 2 operation(s) for bulk users import requests.
  name: SIMBA Chain Bulk Users Import Requests API
  slug: simba-chain-bulk-users-import-requests-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The DeviceAppAdmin API from SIMBA Chain — 3 operation(s) for deviceappadmin.
  name: SIMBA Chain Device App Admin API
  slug: simba-chain-deviceappadmin-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The DeviceAppRegistration API from SIMBA Chain — 2 operation(s) for deviceappregistration.
  name: SIMBA Chain Device App Registration API
  slug: simba-chain-deviceappregistration-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Domains API from SIMBA Chain — 4 operation(s) for domains.
  name: SIMBA Chain Domains API
  slug: simba-chain-domains-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Events API from SIMBA Chain — 1 operation(s) for events.
  name: SIMBA Chain Events API
  slug: simba-chain-events-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Invites API from SIMBA Chain — 8 operation(s) for invites.
  name: SIMBA Chain Invites API
  slug: simba-chain-invites-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Organisations API from SIMBA Chain — 4 operation(s) for organisations.
  name: SIMBA Chain Organisations API
  slug: simba-chain-organisations-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Passkeys API from SIMBA Chain — 5 operation(s) for passkeys.
  name: SIMBA Chain Passkeys API
  slug: simba-chain-passkeys-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Permissions API from SIMBA Chain — 5 operation(s) for permissions.
  name: SIMBA Chain Permissions API
  slug: simba-chain-permissions-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Probes API from SIMBA Chain — 4 operation(s) for probes.
  name: SIMBA Chain Probes API
  slug: simba-chain-probes-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Roles API from SIMBA Chain — 6 operation(s) for roles.
  name: SIMBA Chain Roles API
  slug: simba-chain-roles-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The ServiceAdmin API from SIMBA Chain — 2 operation(s) for serviceadmin.
  name: SIMBA Chain Service Admin API
  slug: simba-chain-serviceadmin-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Templates API from SIMBA Chain — 2 operation(s) for templates.
  name: SIMBA Chain Templates API
  slug: simba-chain-templates-api
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The Users API from SIMBA Chain — 11 operation(s) for users.
  name: SIMBA Chain Users API
  slug: simba-chain-users-api
- baseURL: https://blocks.simbachain.com/api/platform-service
  baseurl_source: declared
  description: The Client Credentials API from SIMBA Chain — 10 operation(s) for client credentials.
  name: SIMBA Chain Client Credentials API
  slug: simba-chain-client-credentials-api
- baseURL: https://blocks.simbachain.com/api/platform-service
  baseurl_source: declared
  description: The Two Factor API from SIMBA Chain — 7 operation(s) for two factor.
  name: SIMBA Chain Two Factor API
  slug: simba-chain-two-factor-api
artifact_total: 26
asyncapis:
- description: ''
  name: Simba Chain Subscriptions Webhooks
  slug: simba-chain-subscriptions-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/overlays/simba-chain-member-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/simba-chain-member-service-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/overlays/simba-chain-member-service-validator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/simba-chain-member-service-validator-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/security/simba-chain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simba-chain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simbachain.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.simbachain.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simbachain.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simbachain.com/documentation/api-reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.simbachain.com/documentation/getting-started/quickstart-guides/api-quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.simbachain.com/documentation/getting-started/quickstart-guides
- group: start
  title: ''
  type: Login
  url: https://blocks.simbachain.com/
- group: operate
  title: ''
  type: Support
  url: https://simbachain.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://simbachain.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SIMBAChain
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simbachain.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simbachain.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.simbachain.com/documentation/release-notes/release-notes
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/llms/simba-chain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simba-chain-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/packages/simba-chain-packages.yml
  title: ''
  type: Packages
  url: packages/simba-chain-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/packages/simba-chain-packages.yml
  title: ''
  type: SDKs
  url: packages/simba-chain-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/cli/simba-chain-cli.yml
  title: ''
  type: CLI
  url: cli/simba-chain-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/mcp/simba-chain-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/simba-chain-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/mcp/simba-chain-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/simba-chain-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/well-known/simba-chain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simba-chain-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/authentication/simba-chain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/simba-chain-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/scopes/simba-chain-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/simba-chain-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/conventions/simba-chain-conventions.yml
  title: ''
  type: Conventions
  url: conventions/simba-chain-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/conformance/simba-chain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simba-chain-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/errors/simba-chain-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/simba-chain-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/lifecycle/simba-chain-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/simba-chain-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/changelog/simba-chain-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/simba-chain-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/data-model/simba-chain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simba-chain-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/asyncapi/simba-chain-subscriptions-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/simba-chain-subscriptions-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/plans/simba-chain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simba-chain-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/rate-limits/simba-chain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/simba-chain-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-27'
description: SIMBA Chain is a South Bend, Indiana enterprise data company spun out of the University of Notre Dame under U.S. Department of Defense research funding. Its platform — marketed today as SIMBA Trace and built on the SIMBA Blocks / Build / Ensure / Insights product suite — turns products, components, assets, credentials and organizations into tamper-evident, cryptographically sealed records on permissioned blockchains (Ethereum, Hyperledger Fabric, Polygon, Quorum) for supply-chain visibility, traceability, digital thread and EU Digital Product Passport compliance. Developers deploy Solidity or Chaincode smart contracts through SIMBA Build, which auto-generates a REST API (OpenAPI + SwaggerUI) per application, plus a GraphQL query surface, event/notification subscriptions, and DID/Verifiable Credential issuance through SIMBA Ensure. Customers include the U.S. Air Force, Boeing, the Defense Logistics Agency and the Australian Defence Force.
image: https://simbachain.com/wp-content/uploads/2024/01/SIMBA-Chain-logo.svg
layout: provider
mcp_servers:
- description: 'SIMBA Chain serves a live, anonymous, remote MCP endpoint from its own documentation host. It is a DOCUMENTATION server, not a platform-control server: the four tools search, fetch, question and repor'
  name: SIMBA Chain MCP Server
  slug: simba-chain-mcp-server
modified: '2026-08-27'
name: SIMBA Chain
nav: Providers
network: true
overview: 'SIMBA Chain publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Bulk Users Import Requests API, Device App Admin API, and 14 more. Tagged areas include Company, Blockchain, Supply Chain, Traceability, and Digital Product Passport.


  The SIMBA Chain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SIMBA Chain''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, changelog, and 28 more developer resources.'
plans:
- name: Simba Chain Plans Pricing
  plan_count: 0
  slug: simba-chain-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Simba Chain Rate Limits
  slug: simba-chain-rate-limits
scopes:
- name: Simba Chain Scopes
  scope_count: 0
  slug: simba-chain-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 52.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/simba-chain/refs/heads/main/screenshots/simba-chain-2026-09-02T155524.png
security:
- kind: authentication
  name: Simba Chain Authentication
  slug: simba-chain-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Simba Chain Domain Security
  slug: simba-chain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simba-chain
tags:
- Company
- Blockchain
- Supply Chain
- Traceability
- Digital Product Passport
- Smart Contracts
- Identity
- Verifiable Credentials
- Defense
- Government
- Data Management
website: https://simbachain.com/
---
