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
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Tenpace Com Agentic Access
  operation_count: 30
  slug: tenpace-com-agentic-access
  summary_line: 30 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.tenpace.com
  baseurl_source: declared
  description: Plan, authorize, apply, and verify a Review Router connection without exposing provider credentials to the calling agent.
  name: tenpace-com Review Router setup API
  slug: tenpace-com-review-router-setup-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/tenpace-com/agentic-access/tenpace-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tenpace-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/tenpace-com/plans/tenpace-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tenpace-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/rules/tenpace-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tenpace-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/json-ld/tenpace-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tenpace-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tenpace-com/vocabulary/tenpace-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tenpace-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tenpace-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/data-model/tenpace-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tenpace-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/conventions/tenpace-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tenpace-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/conventions/tenpace-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tenpace-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tenpace-com/authentication/tenpace-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tenpace-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/errors/tenpace-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tenpace-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tenpace-com/conformance/tenpace-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tenpace-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tenpace-com/llms/tenpace-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tenpace-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tenpace-com/hosts/tenpace-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tenpace-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tenpace-com/vendors/tenpace-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tenpace-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tenpace-com/security/tenpace-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenpace-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tenpace.com/
- group: docs
  title: ''
  type: APIReference
  url: https://tenpace.com/api/
- group: operate
  title: ''
  type: Support
  url: https://tenpace.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://tenpace.com/products
- group: start
  title: ''
  type: SignUp
  url: https://tenpace.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tenpace.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tenpace.com/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://tenpace.com/openapi.json
  - status: null
    url: https://review-router.tenpace.com/openapi.json
  - status: null
    url: https://api.tenpace.com/openapi.json
  - status: 401
    url: https://tenpace.com/mcp
  - status: 401
    url: https://api.tenpace.com/mcp
  - status: 401
    url: https://tenpace.com/api/graphql
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Tenpace provides a suite of web‑based tools focused on health tracking and workflow automation. Tenpace Health offers training, nutrition, shared recipes, measurements and progress tracking in a daily system, with free and paid plans. Review Router automates software team processes by sending GitHub pull requests to the appropriate Slack channels and reviewers, available in free and team tiers. The platform emphasizes private, consent‑based accountability and contributes 1 % of revenue to carbon removal. All services are delivered via secure web applications hosted on tenpace.com and its subdomains.
image: https://tenpace.com/tenpace-og-follow-through.png
json_schemas:
- name: ConnectionUrl
  property_count: 1
  slug: tenpace-com-connection-url
- name: CreatedSetupSession
  property_count: 19
  slug: tenpace-com-created-setup-session
- name: SetupIntent
  property_count: 5
  slug: tenpace-com-setup-intent
- name: SetupSession
  property_count: 18
  slug: tenpace-com-setup-session
- name: SetupSource
  property_count: 0
  slug: tenpace-com-setup-source
jsonld:
- class_count: 5
  name: Tenpace Com Context
  property_count: 26
  slug: tenpace-com-context
layout: provider
modified: '2026-10-30'
name: tenpace-com
nav: Providers
network: true
overview: 'tenpace-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Review Router setup API. Tagged areas include Health, Software-as-a-Service, Productivity, Workflows, and Integration.


  The tenpace-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tenpace-com''s developer surface includes authentication, API reference, support, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Tenpace Com Plans Pricing
  plan_count: 7
  slug: tenpace-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: tenpace-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: tenpace-com-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 19.6
    discoverability: 73.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tenpace-com/tenpace-com-2026-11-03T144439.png
security:
- kind: authentication
  name: Tenpace Com Authentication
  slug: tenpace-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tenpace Com Domain Security
  slug: tenpace-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: review-router-setup
  slug: tenpace-com-review-router-setup
slug: tenpace-com
tags:
- Health
- Software-as-a-Service
- Productivity
- Workflows
- Integration
- Company
website: https://tenpace.com/
---
