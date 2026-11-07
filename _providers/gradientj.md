---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for GradientJ platform providing AI automation for back‑office tasks
  name: GradientJ API
  slug: gradientj-api-2
- baseURL: https://api.sandbox.gradientj.com
  baseurl_source: declared
  description: 'GradientJ API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: GradientJ API
  slug: gradientj-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/gradientj/rules/gradientj-rules.yml
  title: ''
  type: Spectral
  url: rules/gradientj-rules.yml
- group: design
  href: https://artifacts.apis.io/gradientj/json-ld/gradientj-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gradientj-context.jsonld
- group: design
  href: https://artifacts.apis.io/gradientj/vocabulary/gradientj-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gradientj-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gradientj/data-model/gradientj-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gradientj-data-model.yml
- group: design
  href: https://artifacts.apis.io/gradientj/conformance/gradientj-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gradientj-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gradientj/llms/gradientj-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gradientj-llms.txt
- group: agent
  href: https://artifacts.apis.io/gradientj/well-known/gradientj-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gradientj-well-known.yml
- group: other
  href: https://artifacts.apis.io/gradientj/hosts/gradientj-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gradientj-hosts.yml
- group: other
  href: https://artifacts.apis.io/gradientj/vendors/gradientj-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gradientj-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gradientj/security/gradientj-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gradientj-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gradientj.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gradientj.com/
- group: start
  title: ''
  type: Login
  url: https://auth.tryvelos.com/en/login
- group: company
  title: ''
  type: Newsroom
  url: https://tryvelos.com/media
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryvelos.com/glossary/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryvelos.com/glossary/terms-of-use
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://gradientj.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: GradientJ, now operating under the Velos brand, provides AI-driven automation solutions for back‑office processes in the insurance and finance sectors. Their platform streamlines post‑bind workflows, reduces expense ratios, and offers auditable AI‑powered services for MGAs and program managers. By replacing traditional outsourced labor with intelligent software, Velos helps clients achieve faster, cheaper, and scalable operations while maintaining compliance and accuracy.
image: https://framerusercontent.com/images/0eyuFy49JARfXwssMQSulkkEE.png
json_schemas:
- name: PostApiV0DeployCheckBatchInferenceRequest
  property_count: 1
  slug: gradientj-post-api-v0-deploy-check-batch-inference-request
- name: PostApiV0DeployCheckBatchInferenceResponse
  property_count: 1
  slug: gradientj-post-api-v0-deploy-check-batch-inference-response
- name: PostApiV0DeployCreateBatchInferenceRequest
  property_count: 2
  slug: gradientj-post-api-v0-deploy-create-batch-inference-request
- name: PostApiV0DeployCreateBatchInferenceResponse
  property_count: 1
  slug: gradientj-post-api-v0-deploy-create-batch-inference-response
- name: PostApiV0DeployInferenceRequest
  property_count: 4
  slug: gradientj-post-api-v0-deploy-inference-request
- name: PostApiV0DeployInferenceResponse
  property_count: 1
  slug: gradientj-post-api-v0-deploy-inference-response
jsonld:
- class_count: 6
  name: Gradientj Context
  property_count: 7
  slug: gradientj-context
layout: provider
modified: '2026-10-20'
name: GradientJ
nav: Providers
network: true
overview: 'GradientJ is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Insurance, and Finance.


  The GradientJ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GradientJ''s developer surface includes documentation and 15 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: GradientJ API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: gradientj-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 4.8
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 23.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gradientj/gradientj-2026-11-03T133008.png
security:
- kind: domain-security
  name: Gradientj Domain Security
  slug: gradientj-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gradientj
tags:
- Company
- Artificial Intelligence
- Automation
- Insurance
- Finance
website: https://gradientj.com/
---
