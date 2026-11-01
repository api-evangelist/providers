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
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Aito Technologies Agentic Access
  operation_count: 34
  slug: aito-technologies-agentic-access
  summary_line: 34 operations · 25 acting
api_count: 1
apis:
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The data API from Aito Technologies — 7 operation(s) for data.
  name: Aito Technologies Data API
  slug: aito-technologies-data-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The query API from Aito Technologies — 15 operation(s) for query.
  name: Aito Technologies Query API
  slug: aito-technologies-query-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The schema API from Aito Technologies — 5 operation(s) for schema.
  name: Aito Technologies Schema API
  slug: aito-technologies-schema-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The envs API from Aito Technologies — 3 operation(s) for envs.
  name: Aito Technologies Envs API
  slug: aito-technologies-envs-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: Build and capability introspection — which core build answered, and which operators are live
  name: Aito Technologies Introspection API
  slug: aito-technologies-introspection-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: Asynchronous jobs — submit long operations and poll for status/result
  name: Aito Technologies Jobs API
  slug: aito-technologies-jobs-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The refs API from Aito Technologies — 2 operation(s) for refs.
  name: Aito Technologies Refs API
  slug: aito-technologies-refs-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The releases API from Aito Technologies — 2 operation(s) for releases.
  name: Aito Technologies Releases API
  slug: aito-technologies-releases-api
artifact_total: 20
collections:
- collection_type: open
  name: Aito Technologies data API
  slug: open-aito-technologies-data-api
- collection_type: open
  name: Aito Technologies data query API
  slug: open-aito-technologies-query-api
- collection_type: open
  name: Aito Technologies data schema API
  slug: open-aito-technologies-schema-api
common:
- group: commercial
  href: https://artifacts.apis.io/aito-technologies/plans/aito-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aito-technologies-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/aito-technologies/capabilities/aito-technologies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aito-technologies-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/aito-technologies/authentication/aito-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aito-technologies-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aito-technologies/security/aito-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aito-technologies-domain-security.yml
- group: design
  href: https://artifacts.apis.io/aito-technologies/conventions/aito-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aito-technologies-conventions.yml
- group: design
  href: https://artifacts.apis.io/aito-technologies/errors/aito-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aito-technologies-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aito-technologies/lifecycle/aito-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aito-technologies-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aitostatus.statuspage.io
- group: agent
  href: https://artifacts.apis.io/aito-technologies/mcp/aito-technologies-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aito-technologies-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aito-technologies/llms/aito-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aito-technologies-llms.txt
- group: build
  href: https://artifacts.apis.io/aito-technologies/packages/aito-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/aito-technologies-packages.yml
- group: build
  href: https://artifacts.apis.io/aito-technologies/packages/aito-technologies-packages.yml
  title: ''
  type: SDKs
  url: packages/aito-technologies-packages.yml
- group: build
  href: https://artifacts.apis.io/aito-technologies/cli/aito-technologies-cli.yml
  title: ''
  type: CLI
  url: cli/aito-technologies-cli.yml
- group: design
  href: https://artifacts.apis.io/aito-technologies/conformance/aito-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aito-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aito.ai/trust/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://aito.ai/trust/
- group: design
  href: https://artifacts.apis.io/aito-technologies/data-model/aito-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aito-technologies-data-model.yml
- group: other
  href: https://artifacts.apis.io/aito-technologies/overlays/aito-technologies-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aito-technologies-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aito-technologies/agentic-access/aito-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aito-technologies-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/aito-technologies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/aito-technologies/sandbox/aito-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aito-technologies-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://aito.releasenotes.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aito.ai/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://aito.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://aito.ai/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://aito.ai/docs/
- group: operate
  title: ''
  type: Support
  url: https://aito.ai/join-slack/
- group: company
  title: ''
  type: Blog
  url: https://aito.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AitoDotAI
- group: commercial
  title: ''
  type: Pricing
  url: https://aito.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.aito.ai/account/authentication/?signUp=true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aito.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aito.ai/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://aito.ai
created: '2026-07-17'
description: Aito Technologies (Aito.ai, legal entity Episto Oy of Vantaa, Finland) builds a predictive database that delivers instant, calibrated machine-learning predictions from live business data with no model training. Its REST Query API exposes a SQL-like JSON interface for prediction, recommendation, similarity search, classification, pattern matching, and statistical relation over your own tables, alongside schema and data-management endpoints. Aito powers predictive accounting (GL coding, invoice routing, fraud detection), predictive ERP, and predictive e-commerce, and is delivered as an EU-hosted cloud service (Ireland, eu-west-1) or a self-hosted Docker container. Authentication is an x-api-key header with read-only and read/write key types.
finops:
- has_sources: true
  method: derived
  name: Aito Technologies Finops
  primary_unit: subscription
  service_category: ''
  slug: aito-technologies-finops
  template: false
image: https://console.aito.ai/aito-favicon-128.png
layout: provider
modified: '2026-07-17'
name: Aito Technologies
nav: Providers
network: true
overview: 'Aito Technologies publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Query API, Schema API, and 5 more. Tagged areas include Company, Predictive Database, Machine Learning, Artificial Intelligence, and Recommendations.


  Aito Technologies'' developer surface includes authentication, CLI, sandbox, changelog, documentation, API reference, getting-started guide, and 27 more developer resources.'
plans:
- name: Aito Technologies Plans Pricing
  plan_count: 7
  slug: aito-technologies-plans-pricing
- name: Aito Technologies Price Estimates
  plan_count: 0
  slug: aito-technologies-price-estimates
random_paper: 6
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 80.4
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aito-technologies/aito-technologies-2026-07-25T195452.png
security:
- kind: authentication
  name: Aito Technologies Authentication
  slug: aito-technologies-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aito Technologies Domain Security
  slug: aito-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Predict a field value with Aito
  slug: aito-technologies-predict-a-field
- name: Recommend items that optimize a goal with Aito
  slug: aito-technologies-recommend-items
- name: Search and pattern-match rows with Aito
  slug: aito-technologies-search-and-match
slug: aito-technologies
tags:
- Company
- Predictive Database
- Machine Learning
- Artificial Intelligence
- Recommendations
- Search
- Predictive Analytics
- Automation
- Data
website: https://aito.ai
---
