---
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
    error_semantics: false
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
  score: 19.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Lastmileai Agentic Access
  operation_count: 53
  slug: lastmileai-agentic-access
  summary_line: 53 operations · 29 acting
api_count: 1
apis:
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Dataset API from Last Mile AI — 12 operation(s) for dataset.
  name: Last Mile AI Dataset API
  slug: lastmileai-dataset-api
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Evaluation API from Last Mile AI — 8 operation(s) for evaluation.
  name: Last Mile AI Evaluation API
  slug: lastmileai-evaluation-api
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Experiment API from Last Mile AI — 4 operation(s) for experiment.
  name: Last Mile AI Experiment API
  slug: lastmileai-experiment-api
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Fine Tune Job API from Last Mile AI — 6 operation(s) for fine tune job.
  name: Last Mile AI Fine Tune Job API
  slug: lastmileai-fine-tune-job-api
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Project API from Last Mile AI — 12 operation(s) for project.
  name: Last Mile AI Project API
  slug: lastmileai-project-api
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Pseudo Label Job API from Last Mile AI — 3 operation(s) for pseudo label job.
  name: Last Mile AI Pseudo Label Job API
  slug: lastmileai-pseudo-label-job-api
- baseURL: https://lastmileai.dev
  baseurl_source: spec
  description: The Resource Permission API from Last Mile AI — 8 operation(s) for resource permission.
  name: Last Mile AI Resource Permission API
  slug: lastmileai-resource-permission-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/lastmileai/agentic-access/lastmileai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lastmileai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lastmileai/rules/lastmileai-rules.yml
  title: ''
  type: Spectral
  url: rules/lastmileai-rules.yml
- group: design
  href: https://artifacts.apis.io/lastmileai/json-ld/lastmileai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lastmileai-context.jsonld
- group: design
  href: https://artifacts.apis.io/lastmileai/vocabulary/lastmileai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lastmileai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lastmileai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lastmileai/data-model/lastmileai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lastmileai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/lastmileai/changelog/lastmileai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lastmileai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/lastmileai/authentication/lastmileai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lastmileai-authentication.yml
- group: design
  href: https://artifacts.apis.io/lastmileai/conformance/lastmileai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lastmileai-conformance.yml
- group: other
  href: https://artifacts.apis.io/lastmileai/hosts/lastmileai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lastmileai-hosts.yml
- group: other
  href: https://artifacts.apis.io/lastmileai/vendors/lastmileai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lastmileai-vendors.yml
- group: build
  href: https://artifacts.apis.io/lastmileai/packages/lastmileai-packages.yml
  title: ''
  type: SDKs
  url: packages/lastmileai-packages.yml
- group: build
  href: https://artifacts.apis.io/lastmileai/packages/lastmileai-packages.yml
  title: ''
  type: Packages
  url: packages/lastmileai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lastmileai.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lastmileai.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lastmile-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lastmileai.dev/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lastmileai.dev/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lastmileai.dev/
- group: auth
  href: https://artifacts.apis.io/lastmileai/security/lastmileai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lastmileai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lastmileai.dev/
created: '2026-10-20'
description: Last Mile AI builds the first cognitive computer, a generative AI‑powered platform that empowers people, teams and organizations by providing context‑aware assistance across vision, speech and text. The company offers APIs that let developers integrate cognitive capabilities into applications, enabling tools to understand intent, automate tasks, and orchestrate workflows with human‑in‑the‑loop AI. Backed by Gradient Ventures, AME Cloud Ventures and other luminaries, Last Mile AI aims to create a new kind of computer that always has perfect context about users and their environment.
image: https://lastmileai.dev/images/social-card.png
json_schemas:
- name: CreateExperimentRequest
  property_count: 4
  slug: lastmileai-lmai-proto-webserver-v2-create-experiment-request
- name: EvaluateDatasetRequest
  property_count: 6
  slug: lastmileai-lmai-proto-webserver-v2-evaluate-dataset-request
- name: EvaluateRequest
  property_count: 6
  slug: lastmileai-lmai-proto-webserver-v2-evaluate-request
- name: EvaluateRunRequest
  property_count: 7
  slug: lastmileai-lmai-proto-webserver-v2-evaluate-run-request
- name: GetDatasetViewRequest
  property_count: 11
  slug: lastmileai-lmai-proto-webserver-v2-get-dataset-view-request
- name: UpdateDatasetRowRequest
  property_count: 4
  slug: lastmileai-lmai-proto-webserver-v2-update-dataset-row-request
jsonld:
- class_count: 120
  name: Lastmileai Context
  property_count: 146
  slug: lastmileai-context
layout: provider
modified: '2026-10-20'
name: Last Mile AI
nav: Providers
network: true
overview: 'Last Mile AI publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dataset API, Evaluation API, Experiment API, and 4 more. Tagged areas include Company, Artificial Intelligence, Generative AI, CognitiveComputing, and Platform.


  The Last Mile AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Last Mile AI''s developer surface includes changelog, authentication, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Last Mile AI API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: lastmileai-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 42.3
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lastmileai Authentication
  slug: lastmileai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lastmileai Domain Security
  slug: lastmileai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: lastmileai-create-and-upload-dataset
  slug: lastmileai-create-and-upload-dataset
- name: lastmileai-evaluate-dataset-and-fetch-run
  slug: lastmileai-evaluate-dataset-and-fetch-run
slug: lastmileai
tags:
- Company
- Artificial Intelligence
- Generative AI
- CognitiveComputing
- Platform
website: https://lastmileai.dev/
---
