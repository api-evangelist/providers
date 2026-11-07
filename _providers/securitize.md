---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 64
  human_in_the_loop: 64
  name: Securitize Agentic Access
  operation_count: 125
  slug: securitize-agentic-access
  summary_line: 125 operations · 64 acting · 64 human-in-the-loop
api_count: 1
apis:
- description: OAuth-based identity API that lets partners add "Log in with Securitize iD" to their own application and, with investor consent, retrieve verified KYC/KYB/AML identity data — investor information, ver
  name: Securitize Connect API (Securitize iD)
  slug: securitize-connect-api-securitize-id
- description: Public, unauthenticated Model Context Protocol server ("Securitize Connector") that gives AI assistants and agents real-time, standardized access to the Securitize tokenized-asset catalog — listing as
  name: Securitize MCP Server
  slug: securitize-mcp-server
- baseURL: https://public-api.securitize.io/
  baseurl_source: declared
  description: The APAC API from Securitize — 4 operation(s) for apac.
  name: Securitize APAC API
  slug: securitize-apac-api
- baseURL: https://public-api.securitize.io/
  baseurl_source: declared
  description: The Domains API from Securitize — 74 operation(s) for domains.
  name: Securitize Domains API
  slug: securitize-domains-api
- baseURL: https://public-api.securitize.io/
  baseurl_source: declared
  description: The Health Check API from Securitize — 1 operation(s) for health check.
  name: Securitize Health Check API
  slug: securitize-health-check-api
- baseURL: https://public-api.securitize.io/
  baseurl_source: declared
  description: The Travel Rule API from Securitize — 4 operation(s) for travel rule.
  name: Securitize Travel Rule API
  slug: securitize-travel-rule-api
- baseURL: https://public-api.securitize.io/
  baseurl_source: declared
  description: The Webhooks API from Securitize — 4 operation(s) for webhooks.
  name: Securitize Webhooks API
  slug: securitize-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Securitize Webhooks
  slug: securitize-webhooks
collections:
- collection_type: open
  name: Securitize Domains APAC API
  slug: open-securitize-apac-api
- collection_type: open
  name: Securitize Domains API
  slug: open-securitize-domains-api
- collection_type: open
  name: Securitize Domains API
  slug: open-securitize-domains-openapi-original
- collection_type: open
  name: Securitize Domains Health Check API
  slug: open-securitize-health-check-api
- collection_type: open
  name: Securitize Domains Travel Rule API
  slug: open-securitize-travel-rule-api
- collection_type: open
  name: Securitize Domains Webhooks API
  slug: open-securitize-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/securitize/capabilities/securitize-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/securitize-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://securitize.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://securitize.io/apis
- group: docs
  title: ''
  type: Documentation
  url: https://domain-api-docs.securitize.io/
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.sandbox.securitize.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://domain-api-docs.securitize.io/api/api-specs
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/16645978/UVsEVopd
- group: operate
  title: ''
  type: Support
  url: https://developersupport.securitize.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://securitize.io/learn/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/securitize-io
- group: start
  title: ''
  type: SignUp
  url: https://id.securitize.io/
- group: auth
  title: ''
  type: Security
  url: https://securitize.io/bug-bounty
- group: auth
  href: https://artifacts.apis.io/securitize/security/securitize-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/securitize-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/securitize/security/securitize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/securitize-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/securitize/authentication/securitize-authentication.yml
  title: ''
  type: Authentication
  url: authentication/securitize-authentication.yml
- group: auth
  href: https://artifacts.apis.io/securitize/scopes/securitize-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/securitize-scopes.yml
- group: design
  href: https://artifacts.apis.io/securitize/conformance/securitize-conformance.yml
  title: ''
  type: Conformance
  url: conformance/securitize-conformance.yml
- group: design
  href: https://artifacts.apis.io/securitize/conventions/securitize-conventions.yml
  title: ''
  type: Conventions
  url: conventions/securitize-conventions.yml
- group: design
  href: https://artifacts.apis.io/securitize/lifecycle/securitize-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/securitize-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/securitize/errors/securitize-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/securitize-problem-types.yml
- group: design
  href: https://artifacts.apis.io/securitize/data-model/securitize-data-model.yml
  title: ''
  type: DataModel
  url: data-model/securitize-data-model.yml
- group: start
  href: https://artifacts.apis.io/securitize/sandbox/securitize-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/securitize-sandbox.yml
- group: build
  href: https://artifacts.apis.io/securitize/packages/securitize-packages.yml
  title: ''
  type: Packages
  url: packages/securitize-packages.yml
- group: agent
  href: https://artifacts.apis.io/securitize/mcp/securitize-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/securitize-mcp.yml
- group: build
  href: https://artifacts.apis.io/securitize/mcp/securitize-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/securitize-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/securitize/asyncapi/securitize-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/securitize-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/securitize/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/securitize/agentic-access/securitize-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/securitize-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/securitize/overlays/securitize-domains-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/securitize-domains-overlay.yaml
created: '2026-08-05'
description: 'Securitize is a tokenization platform and SEC-registered financial services group that issues, manages, and services digital securities representing real-world assets — tokenized U.S. Treasuries, private credit, private equity, funds, and equities — for asset managers including BlackRock (BUIDL), Apollo (ACRED), Hamilton Lane, KKR, and VanEck (VBILL). The company operates a registered transfer agent, broker-dealer (Securitize Markets), alternative trading system, fund administration business, and an EU-approved investment firm, and it publishes three developer-facing APIs: a Domain API covering the full securities lifecycle (investor onboarding, KYC/KYB, accreditation, fundraising, issuance, token wallets, blockchain transactions, snapshots, and holder records), a Connect API that acts as an OAuth provider for Securitize iD single sign-on and verified-identity sharing, and a Webhook API for real-time investor event delivery. Securitize also runs a public, unauthenticated MCP
  server that exposes its tokenized-asset catalog to AI agents.'
image: https://cdn.builder.io/api/v1/image/assets%2Fd39b51a544e84e2fbb2445f58c6c6f2c%2F0eeaf40c7ecd4ee0a05f030d32ae949e
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.securitize.io over HTTP; 5 tools listed.
  name: Securitize Connector
  slug: securitize-connector
modified: '2026-08-05'
name: Securitize
nav: Providers
network: true
overview: 'Securitize publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including APAC API, Domains API, Health Check API, and 4 more. Tagged areas include Tokenization, Digital Securities, Real World Assets, Capital Markets, and Fund Administration.


  The Securitize catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Securitize''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Securitize API Rules
  rule_count: 44
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 6
  slug: securitize-rules
scopes:
- name: Securitize Scopes
  scope_count: 3
  slug: securitize-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 68.5
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/securitize/securitize-2026-08-17T081751.png
security:
- kind: authentication
  name: Securitize Authentication
  slug: securitize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Securitize Domain Security
  slug: securitize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Securitize Vulnerability Disclosure
  slug: securitize-vulnerability-disclosure
  summary_line: contact published
skill_count: 4
skills:
- name: Add Securitize iD sign-in and read verified investor identity
  slug: securitize-connect-identity
- name: Fund an investment and issue digital securities on-chain
  slug: securitize-issue-and-settle-tokens
- name: Onboard an investor onto a Securitize domain
  slug: securitize-onboard-investor
- name: Register Travel Rule counterparties and subscribe to investor events
  slug: securitize-travel-rule-and-webhooks
slug: securitize
tags:
- Tokenization
- Digital Securities
- Real World Assets
- Capital Markets
- Fund Administration
- Transfer Agent
- KYC
- AML
- Identity Verification
- Blockchain
- Broker-Dealer
- Private Credit
- MCP
- Webhook
website: https://securitize.io/
---
