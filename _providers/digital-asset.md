---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: 'The Operator Backend for the DA Registry. Exposes publicly accessible endpoints that serve the off-ledger information required to advance Utility Daml workflows via explicit contract disclosure — the '
  name: Digital Asset Utilities API (Operator Backend)
  slug: utilities
- description: Canton Token Standard token metadata service. Read-only off-ledger API returning registry information — including the token-standard versions the registry supports — and the instruments a registrar ad
  name: Digital Asset Token Metadata API (CIP-56)
  slug: token-metadata-v1
- description: 'Canton Token Standard transfer-instruction off-ledger API. Returns the transfer factory and choice context needed to execute a direct transfer, and the choice contexts to accept, reject or withdraw a '
  name: Digital Asset Transfer Instruction API (CIP-56)
  slug: transfer-instruction-v1
- description: Canton Token Standard allocation off-ledger API. Returns the choice contexts required to execute the transfer of, withdraw, or cancel an existing allocation — the settlement primitive behind delivery-
  name: Digital Asset Allocation API (CIP-56)
  slug: allocation-v1
- description: Canton Token Standard allocation-instruction off-ledger API. Returns the allocation factory and choice context for creating allocations through the AllocationFactory_Allocate choice.
  name: Digital Asset Allocation Instruction API (CIP-56)
  slug: allocation-instruction-v1
artifact_total: 9
common:
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
modified: '2026-08-04'
name: Digital Asset
nav: Providers
network: true
overview: 'Digital Asset publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Utilities API (Operator Backend), Token Metadata API (CIP-56), Transfer Instruction API (CIP-56), and 2 more. Tagged areas include Blockchain, Tokenization, Digital Assets, Financial Services, and Distributed Ledger.


  Digital Asset''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 25 more developer resources.'
random_paper: 80
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 47.1
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Financial Services
- Distributed Ledger
- Smart Contracts
- Capital Markets
- Canton Network
- Daml
- Stablecoins
website: https://www.digitalasset.com/
---
