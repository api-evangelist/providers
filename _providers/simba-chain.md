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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.7
  scored_at: '2026-09-05'
api_count: 4
apis:
- baseURL: https://blocks.simbachain.com/api/member-service
  baseurl_source: declared
  description: The organization, user, role, permission and API-credential control plane behind SIMBA Build. Creates and manages organisations, domains, invites, org-scoped and custom system roles, bulk user imports
  name: SIMBA Blocks Member Service API
  slug: simba-chain-member-service-api
- baseURL: https://blocks.simbachain.com/api/member-service-validator
  baseurl_source: declared
  description: SIMBA's OAuth 2.0 / OpenID Connect authorization server and token validator (the "member service validator"). Publishes an OIDC discovery document and a JWKS, issues tokens over the authorization_code
  name: SIMBA Blocks Authentication Service API
  slug: simba-chain-authentication-api
- description: The SIMBA Build dynamic API generator. When a smart contract is deployed into an application, Blocks auto-generates REST endpoints for every method and public variable of that contract — POST to invok
  name: SIMBA Blocks Platform Service (Dynamic Contract API)
  slug: simba-chain-platform-service-api
- description: A live, unauthenticated remote Model Context Protocol server published on SIMBA's own documentation host. tools/list returns four tools — searchDocumentation, getPage, askQuestion and sendFeedback — t
  name: SIMBA Blocks Documentation MCP Server
  slug: simba-chain-documentation-mcp
artifact_total: 11
asyncapis:
- description: ''
  name: Simba Chain Subscriptions Webhooks
  slug: simba-chain-subscriptions-webhooks
common:
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/simba-chain-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/simba-chain-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/simba-chain-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/simba-chain-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simba-chain-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/simba-chain-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simba-chain-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simba-chain-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/simba-chain-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simba-chain-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simba-chain-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simba-chain-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simba-chain-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/simba-chain-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/simba-chain-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/simba-chain-subscriptions-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/simba-chain-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simba-chain-rate-limits.yml
- group: agent
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
overview: 'SIMBA Chain publishes 2 APIs on the [APIs.io](https://apis.io/) network: SIMBA Blocks Member Service API and SIMBA Blocks Authentication Service API. Tagged areas include Company, Blockchain, Supply Chain, Traceability, and Digital Product Passport.


  The SIMBA Chain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SIMBA Chain''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, changelog, and 26 more developer resources.'
plans:
- name: Simba Chain Plans Pricing
  plan_count: 0
  slug: simba-chain-plans-pricing
random_paper: 13
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
  composite: 53.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 53.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
