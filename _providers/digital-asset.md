---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: The common API from Digital Asset — 3 operation(s) for common.
  name: Digital Asset Common API
  slug: digital-asset-common-api
- description: The operator API from Digital Asset — 5 operation(s) for operator.
  name: Digital Asset Operator API
  slug: digital-asset-operator-api
- description: The public API from Digital Asset — 11 operation(s) for public.
  name: Digital Asset Public API
  slug: digital-asset-public-api
- description: The registry API from Digital Asset — 18 operation(s) for registry.
  name: Digital Asset Registry API
  slug: digital-asset-registry-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Utilities Common API
  slug: open-digital-asset-common-api
- collection_type: open
  name: Digital Asset Operator API
  slug: open-digital-asset-operator-api
- collection_type: open
  name: Digital Asset Public API
  slug: open-digital-asset-public-api
- collection_type: open
  name: Digital Asset Registry API
  slug: open-digital-asset-registry-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/digital-asset-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalasset.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.digitalasset.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalasset.com/registry/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.digitalasset.com/api-reference/operator/get-apiutilitiesv0operator
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.digitalasset.com/registry/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.digitalasset.com/registry/support/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.digitalasset.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.digitalasset.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digital-asset
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalasset.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.digitalasset.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.digitalasset.com/trust-center
- group: auth
  title: ''
  type: Security
  url: https://www.digitalasset.com/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/digital-asset-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digital-asset-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digital-asset-authentication.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/digital-asset-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digital-asset-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/digital-asset-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/digital-asset-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digital-asset-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/digital-asset-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/digital-asset-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digital-asset-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.digitalasset.com/registry/releases/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/digital-asset-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digital-asset-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/digital-asset-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/digital-asset-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/digital-asset-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/digital-asset-utilities-overlay.yaml
created: '2026-08-04'
description: 'Digital Asset is the company behind Canton, a privacy-enabled public blockchain built for regulated institutional finance, and Daml, the smart-contract language that runs on it. Its commercial products sit on top of the Canton Network: the DA Registry, a production platform for issuing, minting, burning, transferring and redeeming institutional-grade tokenized assets with credential-based allowlists, blocklists and proof-of-transfer; xReserve, which brings Circle''s USDC onto Canton; and a Covalidation Service for operating validator infrastructure. Its public developer surface is the Utilities (Operator Backend) API plus four Canton Token Standard (CIP-56) off-ledger APIs — token metadata, transfer instruction, allocation and allocation instruction — all published as OpenAPI 3.0 and served across MainNet, TestNet and DevNet environments. Digital Asset also publishes an A2A agent card and a packaged Agent Skill for its Registry workflows.'
image: https://www.digitalasset.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Digital Asset MCP Server
  slug: digital-asset-mcp-server
modified: '2026-08-04'
name: Digital Asset
nav: Providers
network: true
overview: 'Digital Asset publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Common API, Operator API, Public API, and 1 more. Tagged areas include Blockchain, Tokenization, Digital Assets, Financial-Services, and Distributed Ledger.


  Digital Asset''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 26 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 47.7
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 16.7
    contract_quality: 41.5
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 47.7
  provenance:
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digital-asset/refs/heads/main/screenshots/digital-asset-2026-08-07T164342.png
security:
- kind: authentication
  name: Digital Asset Authentication
  slug: digital-asset-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Digital Asset Domain Security
  slug: digital-asset-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Digital Asset Vulnerability Disclosure
  slug: digital-asset-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Digital Asset Trust Center
  slug: digital-asset-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type II, Cloud Security Alliance STAR (Level 1, CAIQ v4.0.2), CIS SecureSuite Member
slug: digital-asset
tags:
- Blockchain
- Tokenization
- Digital Assets
- Financial-Services
- Distributed Ledger
- Smart Contracts
- Capital Markets
- Canton Network
- Daml
- Stablecoins
website: https://www.digitalasset.com/
---
