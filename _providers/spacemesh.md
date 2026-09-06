---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Spacemesh Agentic Access
  operation_count: 26
  slug: spacemesh-agentic-access
  summary_line: 26 operations · 16 acting
api_count: 2
apis:
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The AccountService API from Spacemesh — 2 operation(s) for accountservice.
  name: Spacemesh AccountService API
  slug: spacemesh-accountservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The ActivationService API from Spacemesh — 6 operation(s) for activationservice.
  name: Spacemesh ActivationService API
  slug: spacemesh-activationservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The LayerService API from Spacemesh — 2 operation(s) for layerservice.
  name: Spacemesh LayerService API
  slug: spacemesh-layerservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The MalfeasanceService API from Spacemesh — 2 operation(s) for malfeasanceservice.
  name: Spacemesh MalfeasanceService API
  slug: spacemesh-malfeasanceservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The NetworkService API from Spacemesh — 2 operation(s) for networkservice.
  name: Spacemesh NetworkService API
  slug: spacemesh-networkservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The NodeService API from Spacemesh — 2 operation(s) for nodeservice.
  name: Spacemesh NodeService API
  slug: spacemesh-nodeservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The RewardService API from Spacemesh — 2 operation(s) for rewardservice.
  name: Spacemesh RewardService API
  slug: spacemesh-rewardservice-api
- baseURL: https://api.spacemesh.network
  baseurl_source: declared
  description: The TransactionService API from Spacemesh — 8 operation(s) for transactionservice.
  name: Spacemesh TransactionService API
  slug: spacemesh-transactionservice-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spacemesh AccountService API
  slug: open-spacemesh-accountservice-api
- collection_type: open
  name: Spacemesh AccountService ActivationService API
  slug: open-spacemesh-activationservice-api
- collection_type: open
  name: Spacemesh AccountService LayerService API
  slug: open-spacemesh-layerservice-api
- collection_type: open
  name: Spacemesh AccountService MalfeasanceService API
  slug: open-spacemesh-malfeasanceservice-api
- collection_type: open
  name: Spacemesh AccountService NetworkService API
  slug: open-spacemesh-networkservice-api
- collection_type: open
  name: Spacemesh AccountService NodeService API
  slug: open-spacemesh-nodeservice-api
- collection_type: open
  name: Spacemesh AccountService RewardService API
  slug: open-spacemesh-rewardservice-api
- collection_type: open
  name: Spacemesh AccountService TransactionService API
  slug: open-spacemesh-transactionservice-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/spacemeshos/go-spacemesh/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/spacemeshos/go-spacemesh/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/spacemeshos/go-spacemesh/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spacemeshos/go-spacemesh/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spacemeshos/go-spacemesh/blob/develop/CONTRIBUTING.md
- group: other
  title: ''
  type: Overlay
  url: overlays/spacemesh-v1-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/spacemeshos/go-spacemesh/blob/develop/LICENSE
- group: company
  title: ''
  type: Website
  url: https://spacemesh.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spacemeshos
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/spacemeshos/go-spacemesh
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/spacemeshos/api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/spacemeshos/api
- group: other
  title: ''
  type: Protobuf
  url: grpc/spacemesh/v2beta1/v2beta1.proto
- group: build
  title: ''
  type: Packages
  url: packages/spacemesh-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spacemesh-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/spacemesh-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spacemesh-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spacemesh-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/spacemesh-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spacemesh-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spacemesh-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spacemesh-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spacemesh-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spacemesh-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spacemesh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spacemesh-domain-security.yml
created: '2026-07-17'
description: Spacemesh is a permissionless, self-mining proof-of-space-time (PoST) layer-1 blockchain built to run on ordinary home computers using unused disk space rather than specialized hardware or large capital stake. Its full-node software (go-spacemesh) exposes a gRPC API with a grpc-gateway REST/JSON facade for reading chain state — accounts, transactions, layers, rewards and activations (ATXs) — and for submitting transactions. Surfaced as a Paradigm portfolio company; the protocol, node, API design and developer tooling remain open source under the spacemeshos GitHub org, though the company's spacemesh.io / spacemesh.network web and hosted-API domains are now parked and the last node release was April 2025 (project appears dormant).
image: https://github.com/spacemeshos.png
layout: provider
modified: '2026-07-21'
name: Spacemesh
nav: Providers
network: true
overview: 'Spacemesh publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AccountService API, ActivationService API, LayerService API, and 5 more. Tagged areas include Company, Crypto Infrastructure, Blockchain, Cryptocurrency, and Proof of Space-Time.


  Spacemesh''s developer surface includes documentation, API reference, CLI, changelog, and 23 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spacemesh/refs/heads/main/screenshots/spacemesh-2026-09-02T160328.png
security:
- kind: domain-security
  name: Spacemesh Domain Security
  slug: spacemesh-domain-security
  summary_line: TLSv1.3
slug: spacemesh
tags:
- Company
- Crypto Infrastructure
- Blockchain
- Cryptocurrency
- Proof of Space-Time
- Layer 1
- gRPC
- Node API
- Open-Source
website: https://spacemesh.io
---
