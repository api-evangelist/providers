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
    agent_skills: derived
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blocktorch Agentic Access
  operation_count: 2
  slug: blocktorch-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://c6yaznpyf4.execute-api.us-east-1.amazonaws.com/prod/api
  baseurl_source: declared
  description: Manage managed Hardhat fork instances.
  name: Blocktorch Hardhat API
  slug: blocktorch-hardhat-api
artifact_total: 6
collections:
- collection_type: open
  name: Blocktorch Forking Hardhat API
  slug: open-blocktorch-hardhat-api
common:
- group: other
  href: https://artifacts.apis.io/blocktorch/capabilities/blocktorch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/blocktorch-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/blocktorch/overlays/blocktorch-hardhat-forking-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/blocktorch-hardhat-forking-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blocktorch.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blocktorch.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blocktorch.xyz/overview/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://beta.blocktorch.xyz
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@blocktorch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blocktorch-xyz
- group: operate
  title: ''
  type: Support
  url: mailto:contact@blocktorch.xyz
- group: company
  title: ''
  type: Website
  url: https://blocktorch.xyz
- group: agent
  href: https://artifacts.apis.io/blocktorch/llms/blocktorch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blocktorch-llms.txt
- group: build
  href: https://artifacts.apis.io/blocktorch/packages/blocktorch-packages.yml
  title: ''
  type: Packages
  url: packages/blocktorch-packages.yml
- group: build
  href: https://artifacts.apis.io/blocktorch/packages/blocktorch-packages.yml
  title: ''
  type: SDKs
  url: packages/blocktorch-packages.yml
- group: build
  href: https://artifacts.apis.io/blocktorch/cli/blocktorch-cli.yml
  title: ''
  type: CLI
  url: cli/blocktorch-cli.yml
- group: agent
  href: https://artifacts.apis.io/blocktorch/mcp/blocktorch-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/blocktorch-mcp.yml
- group: agent
  href: https://artifacts.apis.io/blocktorch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/blocktorch/well-known/blocktorch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blocktorch-well-known.yml
- group: auth
  href: https://artifacts.apis.io/blocktorch/authentication/blocktorch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blocktorch-authentication.yml
- group: design
  href: https://artifacts.apis.io/blocktorch/conventions/blocktorch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blocktorch-conventions.yml
- group: design
  href: https://artifacts.apis.io/blocktorch/conformance/blocktorch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blocktorch-conformance.yml
- group: design
  href: https://artifacts.apis.io/blocktorch/data-model/blocktorch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blocktorch-data-model.yml
- group: agent
  href: https://artifacts.apis.io/blocktorch/agentic-access/blocktorch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blocktorch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/blocktorch/security/blocktorch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocktorch-domain-security.yml
created: '2026-07-17'
description: Blocktorch is an end-to-end observability platform built specifically for web3 services and decentralized applications (dApps). It gives engineering teams real-time monitoring of smart contract events, state variables and transaction data, plus log search, alerting, tracing, dashboarding, debugging and collaboration across multiple layers of the web3 stack (EVM chains, roll-ups, local Hardhat forks, oracles, account-abstraction modules and decentralized storage). Blocktorch also exposes a Hardhat Forking API for programmatically managing managed Hardhat fork instances for continuous development and testing. Backed by Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blocktorch.png
layout: provider
modified: '2026-07-18'
name: Blocktorch
nav: Providers
network: true
overview: 'Blocktorch publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Hardhat API. Tagged areas include Company, Web3, Observability, Monitoring, and Blockchain.


  Blocktorch''s developer surface includes documentation, getting-started guide, signup flow, engineering blog, support, CLI, authentication, and 16 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 47.1
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blocktorch/blocktorch-2026-07-25T203347.png
security:
- kind: authentication
  name: Blocktorch Authentication
  slug: blocktorch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blocktorch Domain Security
  slug: blocktorch-domain-security
  summary_line: no transport/DNS hardening detected
skill_count: 1
skills:
- name: Manage a Blocktorch managed Hardhat fork
  slug: blocktorch-manage-hardhat-fork
slug: blocktorch
tags:
- Company
- Web3
- Observability
- Monitoring
- Blockchain
- Smart Contracts
- DApps
- Developer Tools
website: https://blocktorch.xyz
---
