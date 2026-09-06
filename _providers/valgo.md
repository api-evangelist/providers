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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Valgo Agentic Access
  operation_count: 14
  slug: valgo-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Compute API from Valgo — 1 operation(s) for compute.
  name: Valgo Compute API
  slug: valgo-compute-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Compute Batch API from Valgo — 1 operation(s) for compute batch.
  name: Valgo Compute Batch API
  slug: valgo-compute-batch-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Compute Depot Route API from Valgo — 1 operation(s) for compute depot route.
  name: Valgo Compute Depot Route API
  slug: valgo-compute-depot-route-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Compute Route API from Valgo — 1 operation(s) for compute route.
  name: Valgo Compute Route API
  slug: valgo-compute-route-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Health API from Valgo — 1 operation(s) for health.
  name: Valgo Health API
  slug: valgo-health-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Manifest API from Valgo — 1 operation(s) for manifest.
  name: Valgo Manifest API
  slug: valgo-manifest-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The Request Api Key API from Valgo — 1 operation(s) for request api key.
  name: Valgo Request Api Key API
  slug: valgo-request-api-key-api
- baseURL: https://humanbaselines.com/v1
  baseurl_source: declared
  description: The v1 API from Valgo — 7 operation(s) for v1.
  name: Valgo v1 API
  slug: valgo-v1-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Human Crash Baselines Compute API
  slug: open-valgo-compute-api
- collection_type: open
  name: Human Crash Baselines Compute Compute Batch API
  slug: open-valgo-compute-batch-api
- collection_type: open
  name: Human Crash Baselines Compute Compute Depot Route API
  slug: open-valgo-compute-depot-route-api
- collection_type: open
  name: Human Crash Baselines Compute Compute Route API
  slug: open-valgo-compute-route-api
- collection_type: open
  name: Human Crash Baselines Compute Health API
  slug: open-valgo-health-api
- collection_type: open
  name: Human Crash Baselines Compute Manifest API
  slug: open-valgo-manifest-api
- collection_type: open
  name: Human Crash Baselines Compute Request Api Key API
  slug: open-valgo-request-api-key-api
- collection_type: open
  name: Human Crash Baselines Compute v1 API
  slug: open-valgo-v1-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/valgo-humanbaselines-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/valgo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valgo-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/valgo-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/valgo-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valgo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/valgo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/valgo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valgo-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/valgo-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/valgo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/valgo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valgo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valgo-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/valgo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.humanbaselines.com/getting-started/api-access
- group: start
  title: ''
  type: SignUp
  url: https://docs.humanbaselines.com/getting-started/api-access
- group: company
  title: ''
  type: Website
  url: https://valgo.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valgorithmic
- group: company
  title: ''
  type: Blog
  url: https://valgo.ai/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valgo.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valgo.ai/privacy/
created: '2026-07-17'
description: Valgo is a public benefit corporation building the risk quantification layer for physical AI - the insurance risk layer autonomous systems need. Insurers struggle to price autonomous trucks, robotaxis, and robots because the historical claims data does not exist, so Valgo builds probabilistic models of routes, tasks, and environments from the bottom up and outputs the simulated loss estimates insurers need to price coverage across validation, deployment, and insurance. Founded by Stanford safety-validation researchers and an actuary with over a decade of insurance leadership, Valgo is a Y Combinator W26 company backed by Floodgate and Menlo Ventures, and publishes research including human crash baselines for robotaxis and robotrucks.
image: https://valgo.ai/media/valgo-social-media.png
layout: provider
modified: '2026-07-21'
name: Valgo
nav: Providers
network: true
overview: 'Valgo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Compute API, Compute Batch API, Compute Depot Route API, and 5 more. Tagged areas include Company, Insurance, Risk Management, Autonomous Vehicles, and Robotics.


  Valgo''s developer surface includes authentication, changelog, support, signup flow, engineering blog, and 18 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 46.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valgo/refs/heads/main/screenshots/valgo-2026-09-02T165318.png
security:
- kind: authentication
  name: Valgo Authentication
  slug: valgo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valgo Domain Security
  slug: valgo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: valgo
tags:
- Company
- Insurance
- Risk Management
- Autonomous Vehicles
- Robotics
- Artificial Intelligence
- Safety Validation
- Actuarial
website: https://valgo.ai
---
