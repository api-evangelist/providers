---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.etlworks.com
  baseurl_source: declared
  description: 'Etlworks API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Etlworks API
  slug: etlworks-api
artifact_total: 13
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://etlworks.com/privacy-policy.html
- group: commercial
  href: https://artifacts.apis.io/etlworks/plans/etlworks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/etlworks-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/etlworks/rules/etlworks-rules.yml
  title: ''
  type: Spectral
  url: rules/etlworks-rules.yml
- group: design
  href: https://artifacts.apis.io/etlworks/json-ld/etlworks-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/etlworks-context.jsonld
- group: design
  href: https://artifacts.apis.io/etlworks/vocabulary/etlworks-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/etlworks-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/etlworks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/etlworks/data-model/etlworks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/etlworks-data-model.yml
- group: design
  href: https://artifacts.apis.io/etlworks/conventions/etlworks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/etlworks-conventions.yml
- group: auth
  href: https://artifacts.apis.io/etlworks/authentication/etlworks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/etlworks-authentication.yml
- group: design
  href: https://artifacts.apis.io/etlworks/conformance/etlworks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/etlworks-conformance.yml
- group: agent
  href: https://artifacts.apis.io/etlworks/llms/etlworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/etlworks-llms.txt
- group: other
  href: https://artifacts.apis.io/etlworks/hosts/etlworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/etlworks-hosts.yml
- group: other
  href: https://artifacts.apis.io/etlworks/vendors/etlworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/etlworks-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etlworks
- group: auth
  href: https://artifacts.apis.io/etlworks/security/etlworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/etlworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://etlworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://etlworks.com/dev/
- group: docs
  title: ''
  type: Documentation
  url: https://etlworks.com/dev/api/
- group: docs
  title: ''
  type: APIReference
  url: https://etlworks.com/dev/api/api-reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://etlworks.com/dev/api/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://support.etlworks.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://etlworks.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://etlworks.com/roadmap.html
- group: commercial
  title: ''
  type: Pricing
  url: https://etlworks.com/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://etlworks.com/downloads/request.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://etlworks.com/legal.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/etlworks/workspace/etlworks-api
created: '2026-10-20'
description: Etlworks provides a cloud‑based data integration platform that enables businesses to connect, transform, and orchestrate data across a wide variety of sources and destinations. The service offers a visual interface, AI‑assisted data mapping, and a robust REST API for programmatic access. With features such as real‑time CDC, schema drift handling, data quality checks, and on‑premise installers, Etlworks aims to simplify complex ETL workflows for enterprises of all sizes. The platform also includes a CLI, scripting capabilities, and extensive documentation to support developers and data engineers.
json_schemas:
- name: GetRestV1AiAgentApiResponse
  property_count: 3
  slug: etlworks-get-rest-v1-ai-agent-api-response
- name: PostEtlworksEventsRequest
  property_count: 8
  slug: etlworks-post-etlworks-events-request
- name: PostRestV1AiAgentMcpRequest
  property_count: 4
  slug: etlworks-post-rest-v1-ai-agent-mcp-request
- name: PostRestV1AiAgentMcpResponse
  property_count: 3
  slug: etlworks-post-rest-v1-ai-agent-mcp-response
- name: PostRestV1HttplistenerHl7PatientRequest
  property_count: 2
  slug: etlworks-post-rest-v1-httplistener-hl7-patient-request
- name: PostRestV1TokenAuthIssueRequest
  property_count: 2
  slug: etlworks-post-rest-v1-token-auth-issue-request
jsonld:
- class_count: 14
  name: Etlworks Context
  property_count: 22
  slug: etlworks-context
layout: provider
modified: '2026-10-20'
name: Etlworks
nav: Providers
network: true
overview: 'Etlworks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, ETL, and Cloud.


  The Etlworks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Etlworks'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Etlworks Plans Pricing
  plan_count: 6
  slug: etlworks-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Etlworks API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: etlworks-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.4
    developer_ergonomics: 38.7
    discoverability: 60.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/etlworks/etlworks-2026-11-03T131629.png
security:
- kind: authentication
  name: Etlworks Authentication
  slug: etlworks-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Etlworks Domain Security
  slug: etlworks-domain-security
  summary_line: TLSv1.2 · HSTS
skill_count: 1
skills:
- name: etlworks-rest-chat-agent
  slug: etlworks-rest-chat-agent
slug: etlworks
tags:
- Company
- Data Integration
- ETL
- Cloud
website: https://etlworks.com/
---
