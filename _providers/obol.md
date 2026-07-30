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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 18
  name: Obol Agentic Access
  operation_count: 71
  slug: obol-agentic-access
  summary_line: 71 operations · 18 acting · 18 human-in-the-loop
api_count: 17
apis:
- description: The Address API from Obol — 7 operation(s) for address.
  name: Obol Address API
  slug: obol-address-api
- description: The Cluster Definition API from Obol — 4 operation(s) for cluster definition.
  name: Obol Cluster Definition API
  slug: obol-cluster-definition-api
- description: The Cluster Effectiveness API from Obol — 1 operation(s) for cluster effectiveness.
  name: Obol Cluster Effectiveness API
  slug: obol-cluster-effectiveness-api
- description: The Cluster Lock API from Obol — 22 operation(s) for cluster lock.
  name: Obol Cluster Lock API
  slug: obol-cluster-lock-api
- description: The Deposit Data API from Obol — 4 operation(s) for deposit data.
  name: Obol Deposit Data API
  slug: obol-deposit-data-api
- description: The DV Exit API from Obol — 8 operation(s) for dv exit.
  name: Obol DV Exit API
  slug: obol-dv-exit-api
- description: The DV Migrate API from Obol — 1 operation(s) for dv migrate.
  name: Obol DV Migrate API
  slug: obol-dv-migrate-api
- description: The Fee Recipient API from Obol — 4 operation(s) for fee recipient.
  name: Obol Fee Recipient API
  slug: obol-fee-recipient-api
- description: The Metrics API from Obol — 1 operation(s) for metrics.
  name: Obol Metrics API
  slug: obol-metrics-api
- description: The OWR Information API from Obol — 1 operation(s) for owr information.
  name: Obol OWR Information API
  slug: obol-owr-information-api
- description: The Positions API from Obol — 2 operation(s) for positions.
  name: Obol Positions API
  slug: obol-positions-api
- description: The State API from Obol — 1 operation(s) for state.
  name: Obol State API
  slug: obol-state-api
- description: System related endpoints.
  name: Obol System API
  slug: obol-system-api
- description: The Techne Credentials API from Obol — 4 operation(s) for techne credentials.
  name: Obol Techne Credentials API
  slug: obol-techne-credentials-api
- description: The Terms And Conditions API from Obol — 2 operation(s) for terms and conditions.
  name: Obol Terms And Conditions API
  slug: obol-terms-and-conditions-api
- description: The Test API from Obol — 2 operation(s) for test.
  name: Obol Test API
  slug: obol-test-api
- description: The tvs API from Obol — 2 operation(s) for tvs.
  name: Obol tvs API
  slug: obol-tvs-api
artifact_total: 22
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.obol.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.obol.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.obol.org/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.obol.org/next/run-a-dv/start
- group: company
  title: ''
  type: Blog
  url: https://blog.obol.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ObolNetwork
- group: operate
  title: ''
  type: Support
  url: https://community.obol.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://obol.org/terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://obol.org/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.obol.tech
- group: auth
  title: ''
  type: Authentication
  url: authentication/obol-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/obol-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/obol-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/obol-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/obol-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/obol-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/obol-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/obol-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/obol-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/obol-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/obol-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/obol-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/obol-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/obol-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/obol-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/obol-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/obol-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/obol-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/obol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.obol.org/adv/security/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/obol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://obol.org/
created: '2026-07-17'
description: Obol builds distributed validator infrastructure for Ethereum, letting a validator be run across multiple independent operators and machines (a Distributed Validator, or DV) instead of a single node, which removes single points of failure in proof-of-stake staking. Its core software is Charon, a Go middleware client that coordinates the operators, plus the DV Launchpad dapp, the Obol Splits smart contracts, and the Obol API (api.obol.tech) with a TypeScript SDK for creating and managing clusters. The Obol API exposes cluster definitions, cluster locks, validator states, exits, deposits, fee recipients, effectiveness, peer scores, Techne credentials, and network staking metrics.
image: https://obol.org/obolnetwork.png
layout: provider
mcp_servers:
- description: ''
  name: obol-mcp.yml
  slug: obol-mcpyml
modified: '2026-07-20'
name: Obol
nav: Providers
network: true
overview: 'Obol publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Address API, Cluster Definition API, Cluster Effectiveness API, and 14 more. Tagged areas include Company, Crypto, Ethereum, Staking, and Distributed Validators.


  Obol''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, CLI, and 26 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 49.9
  delta: -1.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 55.0
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Obol Authentication
  slug: obol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Obol Domain Security
  slug: obol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Obol Vulnerability Disclosure
  slug: obol-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: obol
tags:
- Company
- Crypto
- Ethereum
- Staking
- Distributed Validators
- Blockchain Infrastructure
- Web3
website: https://obol.org/
---
