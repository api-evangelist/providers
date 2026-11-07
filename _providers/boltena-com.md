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
    agent_skills: derived
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Boltena Com Agentic Access
  operation_count: 8
  slug: boltena-com-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- baseURL: https://app.boltena.com
  baseurl_source: declared
  description: 연동(CONN) 모듈만 있으면 사용
  name: 볼테나 기본 API
  slug: boltena-com-default-api
- baseURL: https://app.boltena.com
  baseurl_source: declared
  description: EQP 모듈 계약이 있어야 호출됩니다
  name: 볼테나 EQP 모듈 필요 API
  slug: boltena-com-eqp-api
- baseURL: https://app.boltena.com
  baseurl_source: declared
  description: HR 모듈 계약이 있어야 호출됩니다
  name: 볼테나 HR 모듈 필요 API
  slug: boltena-com-hr-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/boltena-com/agentic-access/boltena-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boltena-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/boltena-com/plans/boltena-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boltena-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boltena-com/rules/boltena-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boltena-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boltena-com/vocabulary/boltena-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boltena-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/boltena-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/boltena-com/errors/boltena-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boltena-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boltena-com/conformance/boltena-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boltena-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boltena-com/llms/boltena-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boltena-com-llms.txt
- group: other
  href: https://artifacts.apis.io/boltena-com/hosts/boltena-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boltena-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boltena.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boltena.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://boltena.com/pricing
- group: start
  title: ''
  type: Login
  url: https://boltena.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://boltena.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://boltena.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://boltena.com/developers
- group: auth
  href: https://artifacts.apis.io/boltena-com/authentication/boltena-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boltena-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/boltena-com/security/boltena-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boltena-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boltena.com/
created: '2026-11-02'
description: 'boltena-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://boltena.com/assets/img/scene-bi.png
layout: provider
modified: '2026-11-02'
name: 볼테나
nav: Providers
network: true
overview: '볼테나 publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: 기본 API, EQP 모듈 필요 API, and HR 모듈 필요 API. Tagged areas include ERP, Human Resources, MES, and Business Intelligence.


  The 볼테나 catalog on APIs.io includes 1 Spectral governance ruleset.


  볼테나''s developer surface includes pricing, documentation, engineering blog, API reference, authentication, and 14 more developer resources.'
plans:
- name: Boltena Com Plans Pricing
  plan_count: 5
  slug: boltena-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: 볼테나 API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: boltena-com-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 53.9
    developer_ergonomics: 23.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boltena Com Authentication
  slug: boltena-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Boltena Com Domain Security
  slug: boltena-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: boltena-com-send-production-result
  slug: boltena-com-send-production-result
slug: boltena-com
tags:
- ERP
- Human Resources
- MES
- Business Intelligence
website: https://boltena.com/
---
