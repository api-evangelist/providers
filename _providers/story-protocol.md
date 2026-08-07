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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Story Protocol Agentic Access
  operation_count: 33
  slug: story-protocol-agentic-access
  summary_line: 33 operations · 18 acting
api_count: 13
apis:
- description: The Collections API from Story Protocol — 2 operation(s) for collections.
  name: Story Protocol Collections API
  slug: story-protocol-collections-api
- description: The Disputes API from Story Protocol — 2 operation(s) for disputes.
  name: Story Protocol Disputes API
  slug: story-protocol-disputes-api
- description: The IPAssets API from Story Protocol — 4 operation(s) for ipassets.
  name: Story Protocol IPAssets API
  slug: story-protocol-ipassets-api
- description: The IPGroup API from Story Protocol — 2 operation(s) for ipgroup.
  name: Story Protocol IPGroup API
  slug: story-protocol-ipgroup-api
- description: The IPLicenseTerms API from Story Protocol — 4 operation(s) for iplicenseterms.
  name: Story Protocol IPLicenseTerms API
  slug: story-protocol-iplicenseterms-api
- description: The Licenses API from Story Protocol — 4 operation(s) for licenses.
  name: Story Protocol Licenses API
  slug: story-protocol-licenses-api
- description: The LicenseTemplates API from Story Protocol — 2 operation(s) for licensetemplates.
  name: Story Protocol LicenseTemplates API
  slug: story-protocol-licensetemplates-api
- description: The LicenseTerms API from Story Protocol — 2 operation(s) for licenseterms.
  name: Story Protocol LicenseTerms API
  slug: story-protocol-licenseterms-api
- description: The LicenseTokens API from Story Protocol — 2 operation(s) for licensetokens.
  name: Story Protocol LicenseTokens API
  slug: story-protocol-licensetokens-api
- description: The Modules API from Story Protocol — 2 operation(s) for modules.
  name: Story Protocol Modules API
  slug: story-protocol-modules-api
- description: The Permissions API from Story Protocol — 2 operation(s) for permissions.
  name: Story Protocol Permissions API
  slug: story-protocol-permissions-api
- description: The Royalties API from Story Protocol — 2 operation(s) for royalties.
  name: Story Protocol Royalties API
  slug: story-protocol-royalties-api
- description: The Transactions API from Story Protocol — 3 operation(s) for transactions.
  name: Story Protocol Transactions API
  slug: story-protocol-transactions-api
artifact_total: 17
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.story.foundation/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.story.foundation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.story.foundation/api-reference/protocol/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.story.foundation/developers/typescript-sdk/setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/storyprotocol
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/story-protocol-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/story-protocol-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/story-protocol-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/story-protocol-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/story-protocol-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/story-protocol-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/story-protocol-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/story-protocol-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/story-protocol-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/story-protocol-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/story-protocol-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/story-protocol-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/story-protocol-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/story-protocol-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/story-protocol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/story-protocol-domain-security.yml
created: '2026-07-17'
description: Story Protocol is a purpose-built EVM Layer 1 blockchain for onchain intellectual property (the "IP blockchain"), powered by Proof of Creativity, built by Pip Labs and backed by a16z. Its public REST API (api.storyapis.com) is a read-only indexer that exposes IP assets, collections, license terms, license templates and tokens, minting fees, disputes, IP groups, royalties, protocol modules, permissions, and transactions across Story mainnet (chain 1514) and the Aeneid testnet (chain 1315). Authentication is an X-Api-Key header plus an X-Chain network selector; official TypeScript and Python SDKs wrap both the API and the onchain protocol.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/story-protocol.png
layout: provider
mcp_servers:
- description: ''
  name: story-protocol-mcp.yml
  slug: story-protocol-mcpyml
modified: '2026-07-21'
name: Story Protocol
nav: Providers
network: true
overview: 'Story Protocol publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Disputes API, IPAssets API, and 10 more. Tagged areas include Company, Blockchain, Intellectual Property, Licensing, and Royalties.


  Story Protocol''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 16 more developer resources.'
random_paper: 35
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 55.8
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Story Protocol Authentication
  slug: story-protocol-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Story Protocol Domain Security
  slug: story-protocol-domain-security
  summary_line: TLSv1.3
slug: story-protocol
tags:
- Company
- Blockchain
- Intellectual Property
- Licensing
- Royalties
- Web3
- NFT
- API
- Developer Tools
website: https://docs.story.foundation/developers
---
