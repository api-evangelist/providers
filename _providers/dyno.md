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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Phi is a biomodal computation platform for protein design. The REST API lets a caller create datasets from PDB/CIF structures, submit structure-prediction and sequence-design jobs across twenty biomod
  name: Dyno Phi — Protein Design API
  slug: dyno-phi-protein-design-api
artifact_total: 7
collections:
- collection_type: open
  name: Phi — Protein Design API
  slug: open-dyno-phi
common:
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
- description: ''
  name: dyno-mcp.yml
  slug: dyno-mcpyml
modified: '2026-08-10'
name: Dyno
nav: Providers
network: true
overview: 'Dyno publishes 1 API on the [APIs.io](https://apis.io/) network: Phi — Protein Design API. Tagged areas include Company, Biotechnology, Gene Therapy, Genetic Medicine, and Gene Delivery.


  Dyno''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 25 more developer resources.'
plans:
- name: Dyno Plans Pricing
  plan_count: 0
  slug: dyno-plans-pricing
random_paper: 144
rate_limits:
- limit_count: 0
  name: Dyno Rate Limits
  slug: dyno-rate-limits
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 52.2
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 45.2
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- Machine Learning
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
