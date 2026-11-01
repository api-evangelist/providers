---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 85
  human_in_the_loop: 2
  name: Trajectory Agentic Access
  operation_count: 236
  slug: trajectory-agentic-access
  summary_line: 236 operations · 85 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The agents API from Trajectory — 15 operation(s) for agents.
  name: Trajectory Agents API
  slug: trajectory-agents-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The aperture API from Trajectory — 35 operation(s) for aperture.
  name: Trajectory Aperture API
  slug: trajectory-aperture-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The api-keys API from Trajectory — 2 operation(s) for api-keys.
  name: Trajectory API Keys API
  slug: trajectory-api-keys-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The artifacts API from Trajectory — 4 operation(s) for artifacts.
  name: Trajectory Artifacts API
  slug: trajectory-artifacts-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The auth API from Trajectory — 1 operation(s) for auth.
  name: Trajectory Auth API
  slug: trajectory-auth-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The benchmark-ingestion API from Trajectory — 6 operation(s) for benchmark-ingestion.
  name: Trajectory Benchmark Ingestion API
  slug: trajectory-benchmark-ingestion-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The benchmarks API from Trajectory — 22 operation(s) for benchmarks.
  name: Trajectory Benchmarks API
  slug: trajectory-benchmarks-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The billing API from Trajectory — 15 operation(s) for billing.
  name: Trajectory Billing API
  slug: trajectory-billing-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The deployments API from Trajectory — 8 operation(s) for deployments.
  name: Trajectory Deployments API
  slug: trajectory-deployments-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The diagnostics API from Trajectory — 5 operation(s) for diagnostics.
  name: Trajectory Diagnostics API
  slug: trajectory-diagnostics-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The eval API from Trajectory — 11 operation(s) for eval.
  name: Trajectory Eval API
  slug: trajectory-eval-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The experiments API from Trajectory — 13 operation(s) for experiments.
  name: Trajectory Experiments API
  slug: trajectory-experiments-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The inference API from Trajectory — 9 operation(s) for inference.
  name: Trajectory Inference API
  slug: trajectory-inference-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The krun API from Trajectory — 4 operation(s) for krun.
  name: Trajectory Krun API
  slug: trajectory-krun-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The model-endpoints API from Trajectory — 2 operation(s) for model-endpoints.
  name: Trajectory Model Endpoints API
  slug: trajectory-model-endpoints-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The model-slugs API from Trajectory — 1 operation(s) for model-slugs.
  name: Trajectory Model Slugs API
  slug: trajectory-model-slugs-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The organizations API from Trajectory — 14 operation(s) for organizations.
  name: Trajectory Organizations API
  slug: trajectory-organizations-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The pipelines API from Trajectory — 2 operation(s) for pipelines.
  name: Trajectory Pipelines API
  slug: trajectory-pipelines-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The regression-reports API from Trajectory — 2 operation(s) for regression-reports.
  name: Trajectory Regression Reports API
  slug: trajectory-regression-reports-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The sandboxes API from Trajectory — 1 operation(s) for sandboxes.
  name: Trajectory Sandboxes API
  slug: trajectory-sandboxes-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The secrets API from Trajectory — 2 operation(s) for secrets.
  name: Trajectory Secrets API
  slug: trajectory-secrets-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The sherlock API from Trajectory — 1 operation(s) for sherlock.
  name: Trajectory Sherlock API
  slug: trajectory-sherlock-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The supported-models API from Trajectory — 2 operation(s) for supported-models.
  name: Trajectory Supported Models API
  slug: trajectory-supported-models-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The tcli API from Trajectory — 5 operation(s) for tcli.
  name: Trajectory Tcli API
  slug: trajectory-tcli-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The telemetry API from Trajectory — 1 operation(s) for telemetry.
  name: Trajectory Telemetry API
  slug: trajectory-telemetry-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The training API from Trajectory — 17 operation(s) for training.
  name: Trajectory Training API
  slug: trajectory-training-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The trajectories API from Trajectory — 8 operation(s) for trajectories.
  name: Trajectory Trajectories API
  slug: trajectory-trajectories-api
- baseURL: https://api.trajectory.ai
  baseurl_source: declared
  description: The wandb API from Trajectory — 1 operation(s) for wandb.
  name: Trajectory Wandb API
  slug: trajectory-wandb-api
artifact_total: 43
common:
- group: agent
  href: https://artifacts.apis.io/trajectory/agentic-access/trajectory-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trajectory-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/trajectory/rules/trajectory-rules.yml
  title: ''
  type: Spectral
  url: rules/trajectory-rules.yml
- group: design
  href: https://artifacts.apis.io/trajectory/json-ld/trajectory-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trajectory-context.jsonld
- group: design
  href: https://artifacts.apis.io/trajectory/vocabulary/trajectory-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trajectory-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trajectory/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trajectory/data-model/trajectory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trajectory-data-model.yml
- group: design
  href: https://artifacts.apis.io/trajectory/conventions/trajectory-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trajectory-conventions.yml
- group: design
  href: https://artifacts.apis.io/trajectory/conventions/trajectory-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trajectory-conventions.yml
- group: design
  href: https://artifacts.apis.io/trajectory/conformance/trajectory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trajectory-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trajectory/well-known/trajectory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trajectory-well-known.yml
- group: other
  href: https://artifacts.apis.io/trajectory/hosts/trajectory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trajectory-hosts.yml
- group: other
  href: https://artifacts.apis.io/trajectory/vendors/trajectory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trajectory-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trajectory.ai/
- group: auth
  href: https://artifacts.apis.io/trajectory/authentication/trajectory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trajectory-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trajectory/security/trajectory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trajectory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trajectory.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trajectory.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trajectory.ai/legal/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.trajectory.ai/openapi.json
  - status: 401
    url: https://docs.trajectory.ai/mcp
  - status: 200
    url: https://www.trajectory.ai/
  reason: partner-login
  state: gated
created: '2026-10-24'
description: Trajectory builds infrastructure for continual learning AI models, enabling enterprises to develop steerable, evolving intelligence. Their platform supports model improvement over time, offering tools for field‑notes, intelligence‑in‑motion, and collaborative research. Backed by conviction and essence‑vc, Trajectory aims to advance AI reliability and adaptability across customer service and enterprise applications.
image: https://trajectory.ai/opengraph-image.png?opengraph-image.30srpd3dxqjbg.png?dpl=dpl_LXj5Sn7QCd2kTFPWGEmaogYrFx5D
json_schemas:
- name: CreateRunRequest
  property_count: 9
  slug: trajectory-create-run-request
- name: Deployment
  property_count: 18
  slug: trajectory-deployment
- name: EvalRun
  property_count: 19
  slug: trajectory-eval-run
- name: ExperimentDetail
  property_count: 34
  slug: trajectory-experiment-detail
- name: StartEvalRequest
  property_count: 11
  slug: trajectory-start-eval-request
- name: Trajectory
  property_count: 25
  slug: trajectory-trajectory
jsonld:
- class_count: 120
  name: Trajectory Context
  property_count: 424
  slug: trajectory-context
layout: provider
modified: '2026-10-24'
name: Trajectory
nav: Providers
network: true
overview: 'Trajectory publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Aperture API, API Keys API, and 25 more. Tagged areas include Company, AI, Continual Learning, Enterprise, and Platform.


  The Trajectory catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Trajectory''s developer surface includes documentation, authentication, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Trajectory API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: trajectory-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 51.5
    developer_ergonomics: 23.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Trajectory Authentication
  slug: trajectory-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trajectory Domain Security
  slug: trajectory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: trajectory-add-organization-members
  slug: trajectory-add-organization-members
- name: trajectory-create-and-complete-trajectory
  slug: trajectory-create-and-complete-trajectory
- name: trajectory-purchase-credits-and-check-balance
  slug: trajectory-purchase-credits-and-check-balance
- name: trajectory-start-and-monitor-deployment
  slug: trajectory-start-and-monitor-deployment
slug: trajectory
tags:
- Company
- AI
- Continual Learning
- Enterprise
- Platform
website: https://www.trajectory.ai/
---
