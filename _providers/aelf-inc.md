---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-09-12'
api_count: 2
apis:
- baseURL: https://aelf-public-node.aelf.io
  baseurl_source: declared
  description: 'The AElf node Web API is the REST surface every aelf node exposes: chain status, blocks, block state, transaction pool, transaction submission and results, merkle paths, contract file descriptor sets,'
  name: aelf Node Web API
  slug: aelf-node-web-api
- baseURL: http://127.0.0.1:8787
  baseurl_source: declared
  description: 'A first-party, self-hosted execution gateway that puts the aelf chain behind typed OpenAPI/MCP tools for AI agents: chain and asset queries, EOA/CA wallet operations, an explicit prepare -> human appr'
  name: aelf Agent Gateway API
  slug: aelf-agent-gateway-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://aelf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aelf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aelf.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aelf.com/tools/web-api/chain-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aelf.com/quick-start/
- group: company
  title: ''
  type: Blog
  url: https://blog.aelf.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AElfProject
- group: operate
  title: ''
  type: Support
  url: https://form.aelf.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.aelf.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.aelf.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.aelf.com/resources/whitepaper-2/roadmap/
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-peer-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-crosschain-rpc.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-acs20-standard-token.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-acs721-standard-nft.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-acs0-genesis.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-token-contract.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/aelf-inc-core.proto
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aelf-inc-wallet-context-v1.schema.json
- group: build
  title: ''
  type: Packages
  url: packages/aelf-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aelf-inc-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aelf-inc-cli.yml
- group: design
  title: ''
  type: Components
  url: components/aelf-inc-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aelf-inc-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aelf-inc-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aelf-inc-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aelf-inc-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aelf-inc-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aelf-inc-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aelf-inc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aelf-inc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aelf-inc-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aelf-inc-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aelf-inc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aelf-inc-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aelf-inc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/AElfProject/.github/blob/master/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aelf-inc-domain-security.yml
created: '2026-09-09'
description: aelf (styled lowercase by the company, listed on the secondary market as "Aelf Inc") is a Singapore-headquartered AI-enhanced, cloud-native layer-1 blockchain network founded in 2017. It is written in C# with a modular multi-side-chain architecture, parallel transaction execution and built-in cross-chain communication. Its public machine-readable surface is the AElf node Web API — an OpenAPI 3.0.1 contract every node serves at /swagger/v1/swagger.json and reachable anonymously on the public mainnet nodes — alongside 89 published protobuf contract definitions (the ACS contract standards, plus the gRPC peer and cross-chain services), six first-party chain SDKs, the aelf-command CLI, and a first-party agent layer of packaged Agent Skills and a local MCP server.
image: https://docs.aelf.com/img/logo.svg
json_schemas:
- name: WalletContextFileV1
  property_count: 4
  slug: aelf-inc-wallet-context-v1.schema
layout: provider
mcp_servers:
- description: ''
  name: Aelf MCP Server
  slug: aelf-mcp-server
modified: '2026-09-09'
name: Aelf
nav: Providers
network: true
overview: 'Aelf publishes 2 APIs on the [APIs.io](https://apis.io/) network: Node Web API and Agent Gateway API. Tagged areas include Company, Blockchain, Layer 1, Web3, and Smart Contracts.


  Aelf''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 32 more developer resources.'
plans:
- name: Aelf Inc Plans Pricing
  plan_count: 0
  slug: aelf-inc-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Aelf Inc Rate Limits
  slug: aelf-inc-rate-limits
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.2
    developer_ergonomics: 85.7
    discoverability: 68.5
    operational_transparency: 34.2
  previous_composite: 42.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aelf Inc Authentication
  slug: aelf-inc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aelf Inc Domain Security
  slug: aelf-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aelf Inc Vulnerability Disclosure
  slug: aelf-inc-vulnerability-disclosure
  summary_line: Hackerone
slug: aelf-inc
tags:
- Company
- Blockchain
- Layer 1
- Web3
- Smart Contracts
- Cross-Chain
- Developer Tools
- Protobuf
- Agent Skills
- Cryptocurrency
website: https://aelf.com/
---
