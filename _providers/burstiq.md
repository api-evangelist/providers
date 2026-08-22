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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 85
  human_in_the_loop: 1
  name: Burstiq Agentic Access
  operation_count: 171
  slug: burstiq-agentic-access
  summary_line: 171 operations · 85 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: Set of operations for Blast AI
  name: BurstIQ BlastAI APIs API
  slug: burstiq-blastai-apis-api
- description: Manages all customers and their Secure Data Zones
  name: BurstIQ Customer Directory APIs API
  slug: burstiq-customer-directory-apis-api
- description: Data Pipelines are managed for use of manipulating data
  name: BurstIQ Data Pipeline APIs API
  slug: burstiq-data-pipeline-apis-api
- description: Field Mapping Step is a step used in Data Pipelines and is used to map fields
  name: BurstIQ Data Pipeline Field Mapping Step APIs API
  slug: burstiq-data-pipeline-field-mapping-step-apis-api
- description: JS Transform Step is a step used in Data Pipelines and is used to transform fields
  name: BurstIQ Data Pipeline JS Transform Step APIs API
  slug: burstiq-data-pipeline-js-transform-step-apis-api
- description: DataPipeline Rule are created individually then later added to rule sets
  name: BurstIQ Data Pipeline Rule APIs API
  slug: burstiq-data-pipeline-rule-apis-api
- description: RuleSet Step is a step used in Data Pipelines and is used to execute a series of rules
  name: BurstIQ Data Pipeline RuleSet Step APIs API
  slug: burstiq-data-pipeline-ruleset-step-apis-api
- description: DbSchema is an alternative method to define the dictionaries of the SDZ; it is a 3rd party tool https://dbschema.com/
  name: BurstIQ DbSchema APIs API
  slug: burstiq-dbschema-apis-api
- description: Dictionaries are schemas essentially, they describe the data allowed within a Node of a LifeGraph (can be thought of as a record too); a Node in the LG is akin to a Smart Data Object
  name: BurstIQ Dictionary Metadata APIs API
  slug: burstiq-dictionary-metadata-apis-api
- description: Edge Definitions are required for the system to know what edges are allowed between live node data
  name: BurstIQ Edge Definition Metadata APIs API
  slug: burstiq-edge-definition-metadata-apis-api
- description: Glossary items hold no actual function in the secure data zone, merely a method for defining the business terms, usage, interactions, etc of the data within the SDZ
  name: BurstIQ Glossary Metadata APIs API
  slug: burstiq-glossary-metadata-apis-api
- description: In basic terms, these endpoints are the CRUD+T operations for transactional data on the platform
  name: BurstIQ Graph Chain APIs API
  slug: burstiq-graph-chain-apis-api
- description: Platform support asynchronous jobs, and these endpoints allow for the creation, status, and management of these jobs
  name: BurstIQ Job Manager APIs API
  slug: burstiq-job-manager-apis-api
- description: various metadata endpoints/functions
  name: BurstIQ Metadata Util APIs API
  slug: burstiq-metadata-util-apis-api
- description: Set of operations metrics in a secure data zone
  name: BurstIQ Metrics APIs API
  slug: burstiq-metrics-apis-api
- description: 'Reference OData v4 documentation for usage: https://www.odata.org/getting-started/'
  name: BurstIQ OData v4 APIs API
  slug: burstiq-odata-v4-apis-api
- description: Terms are managed for the developer's use to find, present terms to users and records acceptance
  name: BurstIQ SDZ Specific Term APIs API
  slug: burstiq-sdz-specific-term-apis-api
- description: System wallets are used for non-humans to perform functions in the platform; ie custodian, etc
  name: BurstIQ System Wallet APIs API
  slug: burstiq-system-wallet-apis-api
- description: User Groups are ways of identifying groups of users by name and referencing in various parts of the platform
  name: BurstIQ User Group APIs API
  slug: burstiq-user-group-apis-api
- description: For managing and obtaining information about user wallets
  name: BurstIQ User Wallet APIs API
  slug: burstiq-user-wallet-apis-api
- description: For interacting with wallets when the type of wallet (user or system) is unknown
  name: BurstIQ Wallet APIs API
  slug: burstiq-wallet-apis-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LifeGraph APIs BlastAI APIs API
  slug: open-burstiq-blastai-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Customer Directory APIs API
  slug: open-burstiq-customer-directory-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Data Pipeline APIs API
  slug: open-burstiq-data-pipeline-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Data Pipeline Field Mapping Step APIs API
  slug: open-burstiq-data-pipeline-field-mapping-step-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Data Pipeline JS Transform Step APIs API
  slug: open-burstiq-data-pipeline-js-transform-step-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Data Pipeline Rule APIs API
  slug: open-burstiq-data-pipeline-rule-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Data Pipeline RuleSet Step APIs API
  slug: open-burstiq-data-pipeline-ruleset-step-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs DbSchema APIs API
  slug: open-burstiq-dbschema-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Dictionary Metadata APIs API
  slug: open-burstiq-dictionary-metadata-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Edge Definition Metadata APIs API
  slug: open-burstiq-edge-definition-metadata-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Glossary Metadata APIs API
  slug: open-burstiq-glossary-metadata-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Graph Chain APIs API
  slug: open-burstiq-graph-chain-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Job Manager APIs API
  slug: open-burstiq-job-manager-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Metadata Util APIs API
  slug: open-burstiq-metadata-util-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Metrics APIs API
  slug: open-burstiq-metrics-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs OData v4 APIs API
  slug: open-burstiq-odata-v4-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs SDZ Specific Term APIs API
  slug: open-burstiq-sdz-specific-term-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs System Wallet APIs API
  slug: open-burstiq-system-wallet-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs User Group APIs API
  slug: open-burstiq-user-group-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs User Wallet APIs API
  slug: open-burstiq-user-wallet-apis-api
- collection_type: open
  name: LifeGraph APIs BlastAI APIs Wallet APIs API
  slug: open-burstiq-wallet-apis-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/burstiq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/burstiq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/burstiq-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/burstiq-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/burstiq-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/burstiq-lifegraph-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/burstiq-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/burstiq-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/burstiq-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/burstiq-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/burstiq-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.burstiq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.burstiq.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.burstiq.com/api-docs
- group: company
  title: ''
  type: Blog
  url: https://burstiq.com/blog
- group: operate
  title: ''
  type: Support
  url: https://burstiq.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://burstiq.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BurstIQ
- group: company
  title: ''
  type: Website
  url: https://burstiq.com
created: '2026-07-17'
description: BurstIQ is a health-and-data technology company whose LifeGraph platform pairs a blockchain-secured knowledge graph (GraphChain) with granular consent-and-ownership wallets and configurable data pipelines to give enterprises trusted, agent-ready data. The LifeGraph REST API (OpenAPI 3.1, version 2.42.0) exposes 171 operations across GraphChain Smart Data Objects, user and system wallets, dictionaries, glossaries, edge definitions, data pipelines, job management, and an OData v4 query surface, secured with bearer (JWT) authentication. BurstIQ was surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://burstiq.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: burstiq-mcp.yml
  slug: burstiq-mcpyml
modified: '2026-07-18'
name: BurstIQ
nav: Providers
network: true
overview: 'BurstIQ publishes 21 APIs on the [APIs.io](https://apis.io/) network, including BlastAI APIs API, Customer Directory APIs API, Data Pipeline APIs API, and 18 more. Tagged areas include Company, Health, Data, Blockchain, and Knowledge Graph.


  BurstIQ''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 15 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 30.6
  delta: -1.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 50.8
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/burstiq/refs/heads/main/screenshots/burstiq-2026-07-25T204112.png
security:
- kind: authentication
  name: Burstiq Authentication
  slug: burstiq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Burstiq Domain Security
  slug: burstiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: burstiq
tags:
- Company
- Health
- Data
- Blockchain
- Knowledge Graph
- Consent
- Agentic AI
website: https://burstiq.com
---
