---
access_model:
  confidence: medium
  label: Self-service signup, API key from dashboard
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://design.dynotx.com/
  - https://design.dynotx.com/cli
  trial: true
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The admin API from Dyno — 5 operation(s) for admin.
  name: Dyno Admin API
  slug: dyno-admin-api
- description: The agents API from Dyno — 3 operation(s) for agents.
  name: Dyno Agents API
  slug: dyno-agents-api
- description: The Artifacts API from Dyno — 2 operation(s) for artifacts.
  name: Dyno Artifacts API
  slug: dyno-artifacts-api
- description: The assets API from Dyno — 6 operation(s) for assets.
  name: Dyno Assets API
  slug: dyno-assets-api
- description: The auth API from Dyno — 2 operation(s) for auth.
  name: Dyno Auth API
  slug: dyno-auth-api
- description: The datasets API from Dyno — 4 operation(s) for datasets.
  name: Dyno Datasets API
  slug: dyno-datasets-api
- description: The files API from Dyno — 2 operation(s) for files.
  name: Dyno Files API
  slug: dyno-files-api
- description: The Health API from Dyno — 1 operation(s) for health.
  name: Dyno Health API
  slug: dyno-health-api
- description: The ingest API from Dyno — 5 operation(s) for ingest.
  name: Dyno Ingest API
  slug: dyno-ingest-api
- description: The jobs API from Dyno — 7 operation(s) for jobs.
  name: Dyno Jobs API
  slug: dyno-jobs-api
- description: The Phi API from Dyno — 2 operation(s) for phi.
  name: Dyno Phi API
  slug: dyno-phi-api
- description: The protocols API from Dyno — 7 operation(s) for protocols.
  name: Dyno Protocols API
  slug: dyno-protocols-api
- description: The research-notes API from Dyno — 1 operation(s) for research-notes.
  name: Dyno Research Notes API
  slug: dyno-research-notes-api
- description: The Runs API from Dyno — 4 operation(s) for runs.
  name: Dyno Runs API
  slug: dyno-runs-api
- description: The tools API from Dyno — 3 operation(s) for tools.
  name: Dyno Tools API
  slug: dyno-tools-api
- description: The tutorial API from Dyno — 1 operation(s) for tutorial.
  name: Dyno Tutorial API
  slug: dyno-tutorial-api
- description: The workflows API from Dyno — 9 operation(s) for workflows.
  name: Dyno Workflows API
  slug: dyno-workflows-api
artifact_total: 23
collections:
- collection_type: open
  name: Phi — Protein Design API
  slug: open-dyno-phi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dyno-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dyno-phi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dyno-mcp.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/dynotx/phi-cli/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.dynotx.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://design.dynotx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://design.dynotx.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.dyno-agents.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://design.dynotx.com/cli
- group: company
  title: ''
  type: Blog
  url: https://dynotx.substack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynotx
- group: operate
  title: ''
  type: Support
  url: https://github.com/dynotx/phi-cli/issues
- group: start
  title: ''
  type: SignUp
  url: https://design.dynotx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynotx.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynotx.com/legal/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://design.dynotx.com/acceptable-use
- group: other
  title: ''
  type: OpenSourceNotice
  url: https://design.dynotx.com/open-source
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/dynotx/phi-cli
- group: build
  title: ''
  type: Packages
  url: packages/dyno-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dyno-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dyno-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dyno-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dyno-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dyno-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dyno-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dyno-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dyno-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dyno-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dyno-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dyno-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dyno-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dyno-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dyno-domain-security.yml
created: '2026-07-17'
description: 'Dyno Therapeutics is an AI and biotechnology company building high-performance gene delivery technologies to unlock the potential of next-generation genetic medicine. Using its CapsidMap platform, which combines machine learning with high-throughput in vivo measurement, Dyno designs novel adeno-associated virus (AAV) capsids with improved tissue targeting, immune evasion, manufacturability, and payload capacity. Alongside its capsid partnerships, Dyno operates a public developer platform — Dyno Psi-Phi at design.dynotx.com — that exposes a REST API for agentic protein design: submit structure-prediction, inverse-folding and binder-scoring jobs against GPU-backed open models (AlphaFold2, ESMFold, ProteinMPNN, Boltz, ESM-2, RFDiffusion3, BoltzGen, OpenFold3), track job status, and retrieve scored results. The platform ships a first-party Python CLI (dyno-phi), an MIT-licensed open-source repository, and a provider-published Claude Code Agent Skill. Founded on research from George
  Church''s lab at Harvard, Dyno is headquartered in Watertown, Massachusetts, and is an a16z Bio+Health portfolio company.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dyno.png
layout: provider
mcp_servers:
- description: 'Dyno publishes NO MCP server. This file is an API Evangelist CANDIDATE tool surface derived from the provider''s OpenAPI, offered as a design sketch — it is NOT wired as a type: MCPServer pointer in ap'
  name: Dyno MCP Server
  slug: dyno-mcp-server
modified: '2026-08-10'
name: Dyno
nav: Providers
network: true
overview: 'Dyno publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agents API, Artifacts API, and 14 more. Tagged areas include Company, Biotechnology, Gene Therapy, Genetic Medicine, and Gene Delivery.


  Dyno''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 27 more developer resources.'
plans:
- name: Dyno Plans Pricing
  plan_count: 0
  slug: dyno-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Dyno Rate Limits
  slug: dyno-rate-limits
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.1
    developer_ergonomics: 85.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dyno/refs/heads/main/screenshots/dyno-2026-08-17T080911.png
security:
- kind: authentication
  name: Dyno Authentication
  slug: dyno-authentication
  summary_line: apiKey/http-bearer/oidc-session · 3 schemes
- kind: domain-security
  name: Dyno Domain Security
  slug: dyno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dyno
tags:
- Company
- Biotechnology
- Gene Therapy
- Genetic Medicine
- Gene Delivery
- AAV Capsid
- Artificial Intelligence
- Machine-Learning
- Drug Discovery
- Healthcare
- Protein Design
- Protein Structure Prediction
- Bioinformatics
- Computational Biology
- Agentic AI
- Life Sciences
website: https://www.dynotx.com
---
