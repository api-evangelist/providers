---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Promethium REST API submits and manages GPU-accelerated quantum chemistry workflows and the files they consume and produce. Thirteen operations across two resources — Workflows (list, create, get,
  name: Promethium REST API
  slug: qc-ware-promethium-rest-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qc-ware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qcware.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.promethium.qcware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/qcware/promethium-examples
- group: docs
  title: ''
  type: APIReference
  url: https://app.promethium.qcware.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/qcware/promethium-examples#getting-started-with-the-promethium-api--software-development-kit-sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qcware
- group: company
  title: ''
  type: Blog
  url: https://www.promethium.qcware.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.promethium.qcware.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promethium.qcware.com/pricing-details
- group: start
  title: ''
  type: SignUp
  url: https://app.promethium.qcware.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qcware.com/privacy/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://promethium-status.qcware.com/
- group: build
  title: ''
  type: Packages
  url: packages/qc-ware-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qc-ware-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qc-ware-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qc-ware-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qc-ware-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qc-ware-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qc-ware-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qc-ware-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/qc-ware-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qc-ware-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qc-ware-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qc-ware-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qc-ware-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qc-ware-problem-types.yml
created: '2026-08-26'
description: QC Ware is a quantum and GPU-accelerated computational chemistry company based in Palo Alto, California. Its commercial product is Promethium, a cloud-native quantum chemistry platform that runs ab initio DFT and TD-DFT calculations on NVIDIA A100/V100 GPUs for systems up to roughly 2,000 atoms, used by pharmaceutical and materials-science discovery teams. Promethium exposes a public REST API at api.promethium.qcware.com covering workflow submission (single point, geometry optimization, conformer search, torsion scan, interaction energy / F-SAPT, reaction path and transition state optimization) and a file/project store, plus a Python SDK and a `promethium`/`pm` command-line tool. QC Ware also ran Forge, an earlier quantum computing cloud service with a Python client library, and hosts the Q2B quantum computing conference series.
examples:
- key_count: 5
  name: Qc Ware Conformer Search Request
  slug: qc-ware-conformer-search-request
- key_count: 5
  name: Qc Ware Geometry Optimization Request
  slug: qc-ware-geometry-optimization-request
- key_count: 5
  name: Qc Ware Single Point Calculation Request
  slug: qc-ware-single-point-calculation-request
image: https://cdn.prod.website-files.com/6422991955e15300c0604528/642fbef90d1ede08ed7eee51_openg.avif
layout: provider
modified: '2026-08-26'
name: QC Ware
nav: Providers
network: true
overview: 'QC Ware publishes 1 API on the [APIs.io](https://apis.io/) network: Promethium REST API. Tagged areas include Company, Quantum Computing, Computational Chemistry, Quantum Chemistry, and Drug Discovery.


  QC Ware''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Qc Ware Plans Pricing
  plan_count: 3
  slug: qc-ware-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Qc Ware Rate Limits
  slug: qc-ware-rate-limits
score:
  band: strong
  composite: 56.2
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 16.7
    contract_quality: 50.3
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Qc Ware Authentication
  slug: qc-ware-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Qc Ware Domain Security
  slug: qc-ware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qc-ware
tags:
- Company
- Quantum Computing
- Computational Chemistry
- Quantum Chemistry
- Drug Discovery
- Materials Science
- Scientific Computing
- GPU Computing
- Life Sciences
- Simulation
website: https://www.qcware.com/
---
