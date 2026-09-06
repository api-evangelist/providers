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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The Admin API from Boltz — 7 operation(s) for admin.
  name: Boltz Admin API
  slug: boltz-admin-api
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The Auth API from Boltz — 1 operation(s) for auth.
  name: Boltz Auth API
  slug: boltz-auth-api
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The CLI API from Boltz — 1 operation(s) for cli.
  name: Boltz CLI API
  slug: boltz-cli-api
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The Predictions API from Boltz — 8 operation(s) for predictions.
  name: Boltz Predictions API
  slug: boltz-predictions-api
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The Protein API from Boltz — 15 operation(s) for protein.
  name: Boltz Protein API
  slug: boltz-protein-api
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The Share Links API from Boltz — 4 operation(s) for share links.
  name: Boltz Share Links API
  slug: boltz-share-links-api
- baseURL: https://api.boltz.bio
  baseurl_source: declared
  description: The Small Molecule API from Boltz — 14 operation(s) for small molecule.
  name: Boltz Small Molecule API
  slug: boltz-small-molecule-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Boltz Compute Admin API
  slug: open-boltz-admin-api
- collection_type: open
  name: Boltz Compute Admin Auth API
  slug: open-boltz-auth-api
- collection_type: open
  name: Boltz Compute Admin CLI API
  slug: open-boltz-cli-api
- collection_type: open
  name: Boltz Compute Admin Predictions API
  slug: open-boltz-predictions-api
- collection_type: open
  name: Boltz Compute Admin Protein API
  slug: open-boltz-protein-api
- collection_type: open
  name: Boltz Compute Admin Share Links API
  slug: open-boltz-share-links-api
- collection_type: open
  name: Boltz Compute Admin Small Molecule API
  slug: open-boltz-small-molecule-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/boltz-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://boltz.bio
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.boltz.bio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boltz.bio
- group: docs
  title: ''
  type: APIReference
  url: https://api.boltz.bio/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.boltz.bio/user-guide/introduction/Quickstart.md
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/boltz-compute.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boltz-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/boltz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/boltz-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/boltz-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boltz-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boltz-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/boltz-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/boltz-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/boltz-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boltz-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boltz-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.boltz.bio
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/boltz-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/boltz-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boltz-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://boltz.bio/pricing
- group: company
  title: ''
  type: Blog
  url: https://boltz.bio/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boltz-bio
- group: start
  title: ''
  type: SignUp
  url: https://lab.boltz.bio
- group: operate
  title: ''
  type: Support
  url: https://boltz.bio/join-slack
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.boltz.bio/terms-of-service/terms-of-service.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.boltz.bio/privacy-policy/privacy-policy.md
created: '2026-07-17'
description: Boltz (Boltz PBC) is a public-benefit AI research company building open-source and proprietary foundation models for biomolecular structure prediction, binding-affinity estimation, and generative protein and small-molecule design. Its open-source models (Boltz-1, Boltz-2, BoltzGen, all MIT-licensed) are used by 100,000+ scientists across pharma and biotech, and its commercial platform, Boltz Lab, pairs those models with managed compute and collaborative interfaces. The Boltz Compute API exposes these capabilities as asynchronous jobs - structure & binding prediction, ADME prediction, and small-molecule / protein design and library screening - with official Python, TypeScript, and Go SDKs, a CLI, and an MCP server for agentic drug-discovery workflows. Backed by a $28M seed round led by Amplify Partners, a16z, and Zetta Venture Partners.
image: https://boltz.bio/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Official Boltz MCP server, distributed as an MCP Bundle (.mcpb) named "boltz". Wraps the Boltz Compute API so agents can estimate/run structure & binding predictions, small-molecule and protein design
  name: Boltz MCP Server
  slug: boltz-mcp-server
modified: '2026-07-18'
name: Boltz
nav: Providers
network: true
overview: 'Boltz publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, CLI API, and 4 more. Tagged areas include Company, Digital Biology, Drug Discovery, Artificial Intelligence, and Machine-Learning.


  Boltz''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, sandbox, and 23 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 50.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boltz/refs/heads/main/screenshots/boltz-2026-07-25T203543.png
security:
- kind: authentication
  name: Boltz Authentication
  slug: boltz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Boltz Domain Security
  slug: boltz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boltz
tags:
- Company
- Digital Biology
- Drug Discovery
- Artificial Intelligence
- Machine-Learning
- Protein Design
- Structure Prediction
- Life Sciences
- Compute
website: https://boltz.bio
---
