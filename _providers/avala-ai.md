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
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Avala Ai Agentic Access
  operation_count: 115
  slug: avala-ai-agentic-access
  summary_line: 115 operations · 64 acting
api_count: 1
apis:
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The agents API from Avala AI, Inc. — 4 operation(s) for agents.
  name: Avala AI, Inc. Agents API
  slug: avala-ai-agents-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: To be completed...
  name: Avala AI, Inc. Exports API
  slug: avala-ai-exports-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The fleet API from Avala AI, Inc. — 21 operation(s) for fleet.
  name: Avala AI, Inc. Fleet API
  slug: avala-ai-fleet-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The inference-providers API from Avala AI, Inc. — 3 operation(s) for inference-providers.
  name: Avala AI, Inc. Inference Providers API
  slug: avala-ai-inference-providers-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The models API from Avala AI, Inc. — 6 operation(s) for models.
  name: Avala AI, Inc. Models API
  slug: avala-ai-models-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The organizations API from Avala AI, Inc. — 17 operation(s) for organizations.
  name: Avala AI, Inc. Organizations API
  slug: avala-ai-organizations-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: To be completed...
  name: Avala AI, Inc. Projects API
  slug: avala-ai-projects-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The session-definitions API from Avala AI, Inc. — 1 operation(s) for session-definitions.
  name: Avala AI, Inc. Session Definitions API
  slug: avala-ai-session-definitions-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The slices API from Avala AI, Inc. — 5 operation(s) for slices.
  name: Avala AI, Inc. Slices API
  slug: avala-ai-slices-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The storage-configs API from Avala AI, Inc. — 3 operation(s) for storage-configs.
  name: Avala AI, Inc. Storage Configs API
  slug: avala-ai-storage-configs-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: List and retrieve annotation tasks.
  name: Avala AI, Inc. Tasks API
  slug: avala-ai-tasks-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The webhook-deliveries API from Avala AI, Inc. — 2 operation(s) for webhook-deliveries.
  name: Avala AI, Inc. Webhook Deliveries API
  slug: avala-ai-webhook-deliveries-api
- baseURL: https://api.avala.ai/api/v1
  baseurl_source: declared
  description: The webhooks API from Avala AI, Inc. — 3 operation(s) for webhooks.
  name: Avala AI, Inc. Webhooks API
  slug: avala-ai-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/avala-ai/agentic-access/avala-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avala-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/avala-ai/rules/avala-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/avala-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/avala-ai/json-ld/avala-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avala-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/avala-ai/vocabulary/avala-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avala-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/avala-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/avala-ai/data-model/avala-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avala-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/avala-ai/conventions/avala-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avala-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://avala.ai/platform/security
- group: auth
  href: https://artifacts.apis.io/avala-ai/authentication/avala-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avala-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/avala-ai/errors/avala-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avala-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/avala-ai/conformance/avala-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avala-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/avala-ai/overlays/avala-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avala-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/avala-ai/llms/avala-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avala-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/avala-ai/a2a/avala-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/avala-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/avala-ai/well-known/avala-ai-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avala-ai-security-security.txt
- group: agent
  href: https://artifacts.apis.io/avala-ai/well-known/avala-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avala-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/avala-ai/hosts/avala-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avala-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/avala-ai/vendors/avala-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avala-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/avala-ai/packages/avala-ai-packages.yml
  title: ''
  type: Packages
  url: packages/avala-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avala.ai
- group: auth
  title: ''
  type: Security
  url: https://avala.ai/platform/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@avala-ai/sdk
- group: company
  title: ''
  type: Newsroom
  url: https://avala.ai/news
- group: auth
  href: https://artifacts.apis.io/avala-ai/security/avala-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avala-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/avala-ai/security/avala-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avala-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avala-ai/security/avala-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avala-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avala.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avala.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://avala.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://avala.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://avala.ai/docs/getting-started/introduction
- group: operate
  title: ''
  type: Support
  url: https://avala.ai/support
- group: company
  title: ''
  type: Blog
  url: https://avala.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avala-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://avala.ai/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://avala.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avala.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avala.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://avala.ai/signup
- group: start
  title: ''
  type: Login
  url: https://avala.ai/login
created: '2026-11-02'
description: Turn fleet data into better Physical AI models. Avala AI, Inc. provides a fleet learning infrastructure that ingests MCAP and RRD, imports LeRobot and ROS bag streams via SDKs, connects custom formats with adapters, and publishes traceable training releases. The platform offers versioned, traceable datasets, labeling with full audit, quality control, and model feedback loops, enabling organizations to turn their sensor data into continuously improving AI models.
image: https://avala.ai/api/og?title=Fleet+Learning+Infrastructure+for+Physical+AI&description=Turn+fleet+data+into+better+Physical+AI+models.+Ingest+MCAP+and+RRD%2C+publish+traceable+training+releases+and+trace+model+failures+to+the+data+that+shaped+them.
json_schemas:
- name: DatasetItem
  property_count: 20
  slug: avala-ai-dataset-item
- name: OrganizationDetail
  property_count: 31
  slug: avala-ai-organization-detail
- name: OrganizationList
  property_count: 17
  slug: avala-ai-organization-list
- name: OrganizationUpdate
  property_count: 15
  slug: avala-ai-organization-update
- name: QualityTarget
  property_count: 16
  slug: avala-ai-quality-target
- name: StorageConfigList
  property_count: 20
  slug: avala-ai-storage-config-list
jsonld:
- class_count: 81
  name: Avala Ai Context
  property_count: 237
  slug: avala-ai-context
layout: provider
modified: '2026-11-02'
name: Avala AI, Inc.
nav: Providers
network: true
overview: 'Avala AI, Inc. publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Exports API, Fleet API, and 10 more. Tagged areas include Artificial Intelligence, Fleet Management, Data, Platform, and Machine Learning.


  The Avala AI, Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Avala AI, Inc.''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 33 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Avala AI, Inc. API Rules
  rule_count: 52
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 5
  slug: avala-ai-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.1
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 61.1
    developer_ergonomics: 48.1
    discoverability: 67.0
    operational_transparency: 18.4
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avala Ai Authentication
  slug: avala-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Avala Ai Domain Security
  slug: avala-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Avala Ai Vulnerability Disclosure
  slug: avala-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Avala Ai Trust Center
  slug: avala-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: agents-list
  slug: avala-ai-agents-list-skill
slug: avala-ai
tags:
- Artificial Intelligence
- Fleet Management
- Data
- Platform
- Machine Learning
website: https://avala.ai/
---
