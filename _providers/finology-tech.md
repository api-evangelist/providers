---
access_model:
  confidence: high
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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Finology Tech Agentic Access
  operation_count: 16
  slug: finology-tech-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.finology.tech
  baseurl_source: declared
  description: The Finology.PublicApi API from finology-tech — 16 operation(s) for finology.publicapi.
  name: finology-tech Finology.Public API
  slug: finology-tech-finology-publicapi-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/finology-tech/agentic-access/finology-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/finology-tech-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/finology-tech/plans/finology-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finology-tech-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/finology-tech/rules/finology-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/finology-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/finology-tech/json-ld/finology-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/finology-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/finology-tech/vocabulary/finology-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/finology-tech-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/finology-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/finology-tech/data-model/finology-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finology-tech-data-model.yml
- group: start
  href: https://artifacts.apis.io/finology-tech/sandbox/finology-tech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/finology-tech-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/finology-tech/authentication/finology-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finology-tech-authentication.yml
- group: design
  href: https://artifacts.apis.io/finology-tech/errors/finology-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finology-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/finology-tech/conformance/finology-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finology-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/finology-tech/llms/finology-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finology-tech-llms.txt
- group: auth
  href: https://artifacts.apis.io/finology-tech/well-known/finology-tech-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finology-tech-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/finology-tech/well-known/finology-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finology-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/finology-tech/hosts/finology-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finology-tech-hosts.yml
- group: build
  href: https://artifacts.apis.io/finology-tech/packages/finology-tech-packages.yml
  title: ''
  type: SDKs
  url: packages/finology-tech-packages.yml
- group: build
  href: https://artifacts.apis.io/finology-tech/packages/finology-tech-packages.yml
  title: ''
  type: Packages
  url: packages/finology-tech-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://finology.tech/press/
- group: start
  title: ''
  type: Login
  url: https://identity.finology.tech/Account/Login
- group: auth
  href: https://artifacts.apis.io/finology-tech/security/finology-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finology-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finology.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://finology.tech/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://finology.tech/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://finology.tech/pricing/
- group: company
  title: ''
  type: Blog
  url: https://finology.tech/finology-software-blog-and-news/
- group: operate
  title: ''
  type: Support
  url: https://finology.tech/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finology.tech/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finology.tech/privacy-policy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://finology.tech/openapi.json
  - status: null
    url: https://api.finology.tech/swagger/v1/swagger.json
  - status: 401
    url: https://mcp.finology.tech/mcp
  - status: 200
    url: https://finology.tech/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Finology Software provides student loan assistance tools for financial advisors, integrating AI chat platforms like Claude and ChatGPT. The service offers free loan answers, liability planning, and automated calculations via an API and MCP, with pricing plans starting at $49 per month. It aims to help advisors save clients thousands by forecasting tax liabilities and loan forgiveness outcomes.
image: https://finology.tech/wp-content/uploads/2026/10/mike-matheny-headshot.jpg
json_schemas:
- name: AgentPackResponse
  property_count: 11
  slug: finology-tech-agent-pack-response
- name: ComparisonRequest
  property_count: 2
  slug: finology-tech-comparison-request
- name: KeylessLoanRequest
  property_count: 14
  slug: finology-tech-keyless-loan-request
- name: ProjectionRequest
  property_count: 3
  slug: finology-tech-projection-request
- name: ProjectionResult
  property_count: 13
  slug: finology-tech-projection-result
- name: SandboxKeyResponse
  property_count: 12
  slug: finology-tech-sandbox-key-response
jsonld:
- class_count: 35
  name: Finology Tech Context
  property_count: 132
  slug: finology-tech-context
layout: provider
modified: '2026-10-30'
name: finology-tech
nav: Providers
network: true
overview: 'finology-tech publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Finology.Public API. Tagged areas include Company, Fintech, Student Loans, AI Integration, and Financial Advisors.


  The finology-tech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  finology-tech''s developer surface includes sandbox, authentication, documentation, pricing, engineering blog, support, and 22 more developer resources.'
plans:
- name: Finology Tech Plans Pricing
  plan_count: 4
  slug: finology-tech-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: finology-tech API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 1
  slug: finology-tech-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 54.6
    developer_ergonomics: 41.1
    discoverability: 74.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/finology-tech/finology-tech-2026-11-03T132038.png
security:
- kind: authentication
  name: Finology Tech Authentication
  slug: finology-tech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Finology Tech Domain Security
  slug: finology-tech-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: finology-tech-run-loan-projection
  slug: finology-tech-run-loan-projection
slug: finology-tech
tags:
- Company
- Fintech
- Student Loans
- AI Integration
- Financial Advisors
website: https://finology.tech/
---
