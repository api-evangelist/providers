---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api-gcp.alice-bob.com/v1
  baseurl_source: declared
  description: The Health API from Alice Bob — 1 operation(s) for health.
  name: Alice Bob Health API
  slug: alice--bob-health-api
- baseURL: https://api-gcp.alice-bob.com/v1
  baseurl_source: declared
  description: The Jobs API from Alice Bob — 7 operation(s) for jobs.
  name: Alice Bob Jobs API
  slug: alice--bob-jobs-api
- baseURL: https://api-gcp.alice-bob.com/v1
  baseurl_source: declared
  description: The Targets API from Alice Bob — 3 operation(s) for targets.
  name: Alice Bob Targets API
  slug: alice--bob-targets-api
artifact_total: 12
collections:
- collection_type: open
  name: Felis Cloud • API Reference Health API
  slug: open-alice--bob-health-api
- collection_type: open
  name: Felis Cloud • API Reference Jobs API
  slug: open-alice--bob-jobs-api
- collection_type: open
  name: Felis Cloud • API Reference Targets API
  slug: open-alice--bob-targets-api
common:
- group: agent
  href: https://artifacts.apis.io/alice--bob/mcp/alice--bob-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alice--bob-mcp.yml
- group: other
  href: https://artifacts.apis.io/alice--bob/overlays/alice--bob-felis-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alice--bob-felis-cloud-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/alice--bob/security/alice--bob-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alice--bob-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alice-bob.com/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/alice--bob-stock
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-gcp.alice-bob.com/console/
- group: docs
  title: ''
  type: Documentation
  url: https://felis.alice-bob.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api-gcp.alice-bob.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://felis.alice-bob.com/docs/getting_started/install_the_qiskit_provider/
- group: operate
  title: ''
  type: Support
  url: https://felis.alice-bob.com/docs/contact_us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alice-Bob-SW
- group: commercial
  title: ''
  type: Pricing
  url: https://felis.alice-bob.com/docs/felis_cloud/about_felis_cloud/
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.google.com/marketplace/product/cloud-prod-0/felis-cloud
- group: start
  title: ''
  type: Login
  url: https://api-gcp.alice-bob.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://api-gcp.alice-bob.com/console/status
- group: operate
  href: https://artifacts.apis.io/alice--bob/changelog/alice--bob-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alice--bob-changelog.yml
- group: build
  href: https://artifacts.apis.io/alice--bob/packages/alice--bob-packages.yml
  title: ''
  type: Packages
  url: packages/alice--bob-packages.yml
- group: build
  href: https://artifacts.apis.io/alice--bob/packages/alice--bob-packages.yml
  title: ''
  type: SDKs
  url: packages/alice--bob-packages.yml
- group: start
  href: https://artifacts.apis.io/alice--bob/sandbox/alice--bob-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/alice--bob-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/alice--bob/plans/alice--bob-plans.yml
  title: ''
  type: Plans
  url: plans/alice--bob-plans.yml
- group: agent
  href: https://artifacts.apis.io/alice--bob/llms/alice--bob-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alice--bob-llms.txt
- group: auth
  href: https://artifacts.apis.io/alice--bob/authentication/alice--bob-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alice--bob-authentication.yml
- group: design
  href: https://artifacts.apis.io/alice--bob/conventions/alice--bob-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alice--bob-conventions.yml
- group: design
  href: https://artifacts.apis.io/alice--bob/lifecycle/alice--bob-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alice--bob-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/alice--bob/conformance/alice--bob-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alice--bob-conformance.yml
- group: design
  href: https://artifacts.apis.io/alice--bob/errors/alice--bob-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alice--bob-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alice--bob/data-model/alice--bob-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alice--bob-data-model.yml
- group: agent
  href: https://artifacts.apis.io/alice--bob/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Alice & Bob is a quantum computing company headquartered in Paris with a presence in Boston, founded in 2020, building a universal fault-tolerant quantum computer on cat qubits — superconducting qubits that are intrinsically protected against bit-flip errors. Its commercial developer surface is Felis Cloud, a Quantum Computing as a Service (QCaaS) product that executes quantum circuits on Boson 4 cat-qubit QPUs hosted in Alice & Bob's own premises and on cloud-hosted physical and logical qubit emulators. Felis Cloud is reached through a public REST API (jobs, targets, availability and health) that accepts circuits in QIR format, and through the open-source qiskit-alice-bob-provider Qiskit provider that wraps it.
finops:
- has_sources: true
  method: derived
  name: Alice  Bob Finops
  primary_unit: hour
  service_category: ''
  slug: alice--bob-finops
  template: false
image: https://avatars.githubusercontent.com/u/72556371?v=4
layout: provider
modified: '2026-08-06'
name: Alice Bob
nav: Providers
network: true
overview: 'Alice Bob publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API, Jobs API, and Targets API. Tagged areas include Company, Quantum Computing, Quantum, Cloud Computing, and Emulation.


  Alice Bob''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 21 more developer resources.'
plans:
- name: Alice  Bob Plans
  plan_count: 2
  slug: alice--bob-plans
random_paper: 19
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 48.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
screenshot: https://apis.io/screenshots/alice--bob/alice--bob-2026-08-07T161203.png
security:
- kind: authentication
  name: Alice  Bob Authentication
  slug: alice--bob-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alice  Bob Domain Security
  slug: alice--bob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Run a quantum circuit on Felis Cloud
  slug: alice--bob-run-a-quantum-circuit
- name: Select and check a Felis Cloud backend
  slug: alice--bob-select-and-check-a-backend
slug: alice--bob
tags:
- Company
- Quantum Computing
- Quantum
- Cloud Computing
- Emulation
- Developer Tools
- Compute
- Hardware
- Research
- Qiskit
- QIR
website: https://alice-bob.com/
---
