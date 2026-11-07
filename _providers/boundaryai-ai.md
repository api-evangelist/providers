---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for BoundaryAI platform
  name: BoundaryAI API
  slug: boundaryai-api
- description: 'BoundaryAI API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BoundaryAI API
  slug: boundaryai-ai-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/boundaryai-ai/plans/boundaryai-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boundaryai-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boundaryai-ai/rules/boundaryai-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/boundaryai-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/boundaryai-ai/json-ld/boundaryai-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/boundaryai-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/boundaryai-ai/vocabulary/boundaryai-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boundaryai-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/boundaryai-ai/data-model/boundaryai-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boundaryai-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://boundaryai.ai/security
- group: auth
  href: https://artifacts.apis.io/boundaryai-ai/authentication/boundaryai-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boundaryai-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/boundaryai-ai/conformance/boundaryai-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boundaryai-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boundaryai-ai/llms/boundaryai-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boundaryai-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/boundaryai-ai/hosts/boundaryai-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boundaryai-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/boundaryai-ai/vendors/boundaryai-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boundaryai-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://boundaryai.ai/security
- group: auth
  href: https://artifacts.apis.io/boundaryai-ai/security/boundaryai-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boundaryai-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/boundaryai-ai/security/boundaryai-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boundaryai-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boundaryai.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://boundaryai.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://boundaryai.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://boundaryai.ai/docs/python-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://boundaryai.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://boundaryai.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boundaryai.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boundaryai.ai/privacy
- group: operate
  title: ''
  type: Contact
  url: https://boundaryai.ai/contact
- group: other
  title: ''
  type: SignIn
  url: https://boundaryai.ai/login
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on documented hosts.
  evidence:
  - status: 0
    url: https://api.boundaryai.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BoundaryAI provides an enforcement layer that ensures AI-generated actions comply with safety, policy, and regulatory constraints before execution. By intercepting AI agent decisions, it blocks destructive or non‑compliant actions, protects data privacy, and offers cryptographically verifiable audit trails. The platform serves enterprises needing real‑time governance of AI agents across digital, physical, and data‑governance use cases, helping avoid costly incidents and regulatory penalties.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/U5TEK59P6phHYSCZEd8AmI5Siun1/social-images/social-1783354125534-Screenshot_2026-07-06_120718.webp
json_schemas:
- name: PostV1ApproveRequest
  property_count: 1
  slug: boundaryai-ai-post-v1-approve-request
- name: PostV1CheckRequest
  property_count: 4
  slug: boundaryai-ai-post-v1-check-request
- name: PostV1PoliciesRequest
  property_count: 1
  slug: boundaryai-ai-post-v1-policies-request
jsonld:
- class_count: 3
  name: Boundaryai Ai Context
  property_count: 6
  slug: boundaryai-ai-context
layout: provider
modified: '2026-11-02'
name: BoundaryAI
nav: Providers
network: true
overview: 'BoundaryAI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Governance, Action enforcement, Policy compliance, Security, and Developer Tools.


  The BoundaryAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BoundaryAI''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Boundaryai Ai Plans Pricing
  plan_count: 4
  slug: boundaryai-ai-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: BoundaryAI API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: boundaryai-ai-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 59.2
    contract_governance: 35.6
    contract_quality: 20.1
    developer_ergonomics: 27.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boundaryai Ai Authentication
  slug: boundaryai-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Boundaryai Ai Domain Security
  slug: boundaryai-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Boundaryai Ai Trust Center
  slug: boundaryai-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: boundaryai-ai
tags:
- AI Governance
- Action enforcement
- Policy compliance
- Security
- Developer Tools
website: https://boundaryai.ai/
---
