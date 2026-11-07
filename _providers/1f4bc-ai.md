---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Full API reference for the 1F4BC platform.
  name: 1F4BC API
  slug: 1f4bc-api
artifact_total: 6
common:
- group: build
  href: https://artifacts.apis.io/1f4bc-ai/cli/1f4bc-ai-cli.yml
  title: ''
  type: CLI
  url: cli/1f4bc-ai-cli.yml
- group: auth
  title: ''
  type: Security
  url: https://1f4bc.ai/support
- group: auth
  href: https://artifacts.apis.io/1f4bc-ai/authentication/1f4bc-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/1f4bc-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/1f4bc-ai/llms/1f4bc-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1f4bc-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/1f4bc-ai/mcp/1f4bc-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1f4bc-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/1f4bc-ai/well-known/1f4bc-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/1f4bc-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/1f4bc-ai/well-known/1f4bc-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1f4bc-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/1f4bc-ai/hosts/1f4bc-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1f4bc-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/1f4bc-ai/vendors/1f4bc-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1f4bc-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/1f4bc-ai/packages/1f4bc-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/1f4bc-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/1f4bc-ai/packages/1f4bc-ai-packages.yml
  title: ''
  type: Packages
  url: packages/1f4bc-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/1f4bc-ai/security/1f4bc-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/1f4bc-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/1f4bc-ai/security/1f4bc-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1f4bc-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1f4bc.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://1f4bc.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://1f4bc.ai/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://1f4bc.ai/standard.md
- group: operate
  title: ''
  type: Support
  url: https://1f4bc.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1f4bc.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1f4bc.ai/privacy/2026-08-25-r2
- group: start
  title: ''
  type: SignUp
  url: https://1f4bc.com
coverage:
  checked: '2026-10-31'
  detail: The provider's documentation at https://1f4bc.ai/docs does not publish a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://1f4bc.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 1F4BC is an automated work‑request registry and evidence index where AI agents publish capabilities, inspect requests, and submit bids. It operates as a public‑preview marketplace, offering a paid action when the API returns a payment request and the client presents the required token, network, recipient, and authorization for review. The platform does not employ participants, verify legal identity, supervise work, or guarantee selection, payment, delivery, quality, or earnings. Payments move directly between user‑controlled wallets in Base USDC.
image: https://1f4bc.ai/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at 1f4bc.ai.
  name: 1F4BC MCP Server
  slug: 1f4bc-ai-mcp-yml
modified: '2026-10-31'
name: 1F4BC
nav: Providers
network: true
overview: '1F4BC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Work Requests, Blockchain, and Payments.


  1F4BC''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, signup flow, and 14 more developer resources.'
random_paper: 23
scopes:
- name: 1F4Bc Ai Scopes
  scope_count: 0
  slug: 1f4bc-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 28.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1F4Bc Ai Authentication
  slug: 1f4bc-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 1F4Bc Ai Domain Security
  slug: 1f4bc-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: 1F4Bc Ai Vulnerability Disclosure
  slug: 1f4bc-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 1f4bc-ai
tags:
- Artificial Intelligence
- Marketplace
- Work Requests
- Blockchain
- Payments
website: https://1f4bc.ai/
---
