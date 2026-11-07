---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Capital Company API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Capital Company API
  slug: capitalcompany-ai-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/capitalcompany-ai/plans/capitalcompany-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capitalcompany-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/capitalcompany-ai/rules/capitalcompany-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/capitalcompany-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/capitalcompany-ai/json-ld/capitalcompany-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capitalcompany-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/capitalcompany-ai/vocabulary/capitalcompany-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capitalcompany-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capitalcompany-ai/data-model/capitalcompany-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capitalcompany-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/capitalcompany-ai/security/capitalcompany-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/capitalcompany-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/capitalcompany-ai/conformance/capitalcompany-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capitalcompany-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capitalcompany-ai/llms/capitalcompany-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capitalcompany-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/capitalcompany-ai/well-known/capitalcompany-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capitalcompany-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/capitalcompany-ai/well-known/capitalcompany-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capitalcompany-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/capitalcompany-ai/hosts/capitalcompany-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capitalcompany-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/capitalcompany-ai/vendors/capitalcompany-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capitalcompany-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://capitalcompany.ai/login
- group: auth
  href: https://artifacts.apis.io/capitalcompany-ai/security/capitalcompany-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/capitalcompany-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/capitalcompany-ai/security/capitalcompany-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capitalcompany-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capitalcompany.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://capitalcompany.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://capitalcompany.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://capitalcompany.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capitalcompany.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capitalcompany.ai/privacy
coverage:
  checked: '2026-11-04'
  detail: Documentation at https://capitalcompany.ai/docs is a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://capitalcompany.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Capital Company provides fund administration services for SPVs and funds, offering a platform to launch SPVs, manage funds, onboard limited partners, automate K‑1s, and run capital calls. It supports the full fund lifecycle from formation to exit, delivering tools for compliance, reporting, and investor communications.
image: https://capitalcompany.ai/images/social-preview.png
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: capitalcompany-ai-post-mcp-request
- name: PostOauthDeviceAuthorizationRequest
  property_count: 1
  slug: capitalcompany-ai-post-oauth-device-authorization-request
- name: PostOauthRegisterRequest
  property_count: 2
  slug: capitalcompany-ai-post-oauth-register-request
- name: PostOauthTokenRequest
  property_count: 3
  slug: capitalcompany-ai-post-oauth-token-request
jsonld:
- class_count: 4
  name: Capitalcompany Ai Context
  property_count: 8
  slug: capitalcompany-ai-context
layout: provider
modified: '2026-11-04'
name: Capital Company
nav: Providers
network: true
overview: 'Capital Company is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Fund Administration, SPV, Investment, and CapitalManagement.


  The Capital Company catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capital Company''s developer surface includes documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Capitalcompany Ai Plans Pricing
  plan_count: 4
  slug: capitalcompany-ai-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Capital Company API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: capitalcompany-ai-rules
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capitalcompany Ai Domain Security
  slug: capitalcompany-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Capitalcompany Ai Vulnerability Disclosure
  slug: capitalcompany-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: capitalcompany-ai
tags:
- Finance
- Fund Administration
- SPV
- Investment
- CapitalManagement
website: https://capitalcompany.ai/
---
