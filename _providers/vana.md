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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 12.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The protocol's read/write boundary — a caching and relay layer between protocol participants and the Vana L1 covering the onchain primitives (identity, permissions, fees, PGE, schemas, files, DLP cont
  name: Vana Data Portability RPC
  slug: vana-data-portability-rpc
- description: 'Standard Ethereum JSON-RPC for the EVM-compatible Vana L1 blockchain, which records registrations, grants, file records, and schemas. Mainnet at rpc.vana.org (explorer vanascan.io); Moksha testnet at '
  name: Vana L1 JSON-RPC
  slug: vana-l1-json-rpc
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.vana.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vana.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vana.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vana.org/protocol-reference/full-specification
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vana.org/build-a-vana-app
- group: operate
  title: ''
  type: Support
  url: https://docs.vana.org/resources/community-discord
- group: company
  title: ''
  type: Blog
  url: https://vana.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vana-com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vana.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vana.org/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.vana.org
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.vana.org/resources/whitepaper
- group: build
  href: https://artifacts.apis.io/vana/packages/vana-packages.yml
  title: ''
  type: Packages
  url: packages/vana-packages.yml
- group: build
  href: https://artifacts.apis.io/vana/packages/vana-packages.yml
  title: ''
  type: SDKs
  url: packages/vana-packages.yml
- group: agent
  href: https://artifacts.apis.io/vana/well-known/vana-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vana-well-known.yml
- group: agent
  href: https://artifacts.apis.io/vana/mcp/vana-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vana-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vana/llms/vana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vana-llms.txt
- group: agent
  href: https://artifacts.apis.io/vana/llms/vana-website-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vana-website-llms.txt
- group: design
  href: https://artifacts.apis.io/vana/conformance/vana-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vana-conformance.yml
- group: design
  href: https://artifacts.apis.io/vana/errors/vana-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vana-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vana/lifecycle/vana-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vana-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/vana/authentication/vana-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vana-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vana/security/vana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vana-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vana/security/vana-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vana-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.vana.org/resources/security
- group: start
  href: https://artifacts.apis.io/vana/sandbox/vana-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vana-sandbox.yml
- group: design
  href: https://artifacts.apis.io/vana/conventions/vana-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vana-conventions.yml
- group: build
  href: https://artifacts.apis.io/vana/cli/vana-cli.yml
  title: ''
  type: CLI
  url: cli/vana-cli.yml
- group: design
  href: https://artifacts.apis.io/vana/components/vana-components.yml
  title: ''
  type: Components
  url: components/vana-components.yml
- group: agent
  href: https://artifacts.apis.io/vana/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vana is an open protocol for user-owned, portable personal data — sovereign data infrastructure for the AI economy. Users store personal data in Personal Servers, grant builders access via signed, scope-native EIP-712 permissions, pay protocol fees from an onchain escrow, and revoke access at any time, with all consent recorded on the EVM-compatible Vana L1. Builders integrate through the @opendatalabs/vana-sdk, the Data Portability RPC, a local-first data-collection CLI, and an MCP interface on every Personal Server. Stewarded by the Vana Foundation and developed by Open Data Labs; backed by Paradigm.
image: https://vana.org/assets/logos/vana-asterisk-data-signal.svg
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP.
  name: Vana MCP Server
  slug: vana-personal-server
modified: '2026-07-21'
name: Vana
nav: Providers
network: true
overview: 'Vana is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Ai, Data Portability, Personal Data, and Data Sovereignty.


  Vana''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 71.7
    operational_transparency: 13.2
  previous_composite: 37.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vana/vana-2026-09-02T165348.png
security:
- kind: authentication
  name: Vana Authentication
  slug: vana-authentication
  summary_line: web3-signed/eip712-grants/oauth2-oidc · 4 schemes
- kind: domain-security
  name: Vana Domain Security
  slug: vana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vana Vulnerability Disclosure
  slug: vana-vulnerability-disclosure
  summary_line: contact published
skill_count: 3
skills:
- name: connect-data
  slug: vana-connect-data
- name: create-connector
  slug: vana-create-connector
- name: next-prompt
  slug: vana-next-prompt
slug: vana
tags:
- Company
- Crypto Ai
- Data Portability
- Personal Data
- Data Sovereignty
- Blockchain
- Web3
- Agents
- Artificial Intelligence
website: https://www.vana.org
---
