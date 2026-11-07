---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Chat Completions API from DoCoreAI — 1 operation(s) for chat completions.
  name: DoCoreAI Chat Completions API
  slug: docoreai-chat-completions-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/docoreai/plans/docoreai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docoreai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docoreai/rules/docoreai-rules.yml
  title: ''
  type: Spectral
  url: rules/docoreai-rules.yml
- group: design
  href: https://artifacts.apis.io/docoreai/json-ld/docoreai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docoreai-context.jsonld
- group: design
  href: https://artifacts.apis.io/docoreai/vocabulary/docoreai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docoreai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/docoreai/data-model/docoreai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docoreai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docoreai.com/security/
- group: design
  href: https://artifacts.apis.io/docoreai/conformance/docoreai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docoreai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docoreai/llms/docoreai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docoreai-llms.txt
- group: auth
  href: https://artifacts.apis.io/docoreai/well-known/docoreai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docoreai-security.txt
- group: agent
  href: https://artifacts.apis.io/docoreai/well-known/docoreai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docoreai-well-known.yml
- group: other
  href: https://artifacts.apis.io/docoreai/hosts/docoreai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docoreai-hosts.yml
- group: other
  href: https://artifacts.apis.io/docoreai/vendors/docoreai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docoreai-vendors.yml
- group: build
  href: https://artifacts.apis.io/docoreai/packages/docoreai-packages.yml
  title: ''
  type: SDKs
  url: packages/docoreai-packages.yml
- group: build
  href: https://artifacts.apis.io/docoreai/packages/docoreai-packages.yml
  title: ''
  type: Packages
  url: packages/docoreai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://docoreai.com/security
- group: start
  title: ''
  type: Login
  url: https://docoreai.com/login
- group: auth
  href: https://artifacts.apis.io/docoreai/security/docoreai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/docoreai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/docoreai/security/docoreai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docoreai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docoreai/security/docoreai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docoreai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docoreai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docoreai.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://docoreai.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://docoreai.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docoreai.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docoreai.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://docoreai.com/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://docoreai.com/docs/
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://docoreai.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: DoCoreAI provides an autonomous AI cost governance platform that reduces LLM API expenses by 40–70% in real time. It offers privacy‑first monitoring, token budgeting, and predictive spend control without logging prompts. Targeted at SaaS teams and AI‑native companies, DoCoreAI integrates via a Python package, works alongside applications, and supports major LLM providers such as OpenAI, Anthropic, Google Gemini, Groq, AWS Bedrock, and Ollama.
finops:
- has_sources: true
  method: derived
  name: Docoreai Finops
  primary_unit: seat
  service_category: ''
  slug: docoreai-finops
  template: false
image: https://docoreai.com/wp-content/uploads/2026/09/docoreai-cut-llm-api-costs-40-70-percent-cost-governance.png
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 3
  slug: docoreai-post-v1-chat-completions-request
jsonld:
- class_count: 1
  name: Docoreai Context
  property_count: 3
  slug: docoreai-context
layout: provider
modified: '2026-10-16'
name: DoCoreAI
nav: Providers
network: true
overview: 'DoCoreAI is listed with 1 API on the [APIs.io](https://apis.io/) network: Chat Completions API. Tagged areas include Company, AI Governance, Cost Management, LLM, and Software-as-a-Service.


  The DoCoreAI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DoCoreAI''s developer surface includes documentation, pricing, engineering blog, support, getting-started guide, and 22 more developer resources.'
plans:
- name: Docoreai Plans Pricing
  plan_count: 6
  slug: docoreai-plans-pricing
- name: Docoreai Price Estimates
  plan_count: 0
  slug: docoreai-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: DoCoreAI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: docoreai-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 68.2
    catalog_earned_first_party: 12.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 17.8
    developer_ergonomics: 21.4
    discoverability: 73.2
    operational_transparency: 5.3
  previous_composite: 45.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/docoreai/docoreai-2026-11-03T130847.png
security:
- kind: domain-security
  name: Docoreai Domain Security
  slug: docoreai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docoreai Vulnerability Disclosure
  slug: docoreai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Docoreai Trust Center
  slug: docoreai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: docoreai
tags:
- Company
- AI Governance
- Cost Management
- LLM
- Software-as-a-Service
website: https://docoreai.com/
---
