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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Calculate Co Nz Agentic Access
  operation_count: 52
  slug: calculate-co-nz-agentic-access
  summary_line: 52 operations · 46 acting
api_count: 1
apis:
- baseURL: https://api.calculate.co.nz
  baseurl_source: declared
  description: 'New Zealand tax, money and health calculations. Each one is a port of the calculator of the same name on calculate.co.nz, and the website is the reference: where the two disagree the API is wrong unti'
  name: Calculate.co.nz Calculators API
  slug: calculate-co-nz-calculators-api
- baseURL: https://api.calculate.co.nz
  baseurl_source: declared
  description: Find the right page across all 2,377 calculators, 407 guides and 49 datasets. Only a handful of calculators have their own endpoint; everything else is reachable here as a URL.
  name: Calculate.co.nz Discovery API
  slug: calculate-co-nz-discovery-api
- baseURL: https://api.calculate.co.nz
  baseurl_source: declared
  description: 'Current, dated, sourced New Zealand statutory rates: tax brackets, ACC, student loan, KiwiSaver, benefits. Maintained on a review calendar tied to when each figure actually changes, and consumed by th'
  name: Calculate.co.nz Reference data API
  slug: calculate-co-nz-reference-data-api
- baseURL: https://api.calculate.co.nz
  baseurl_source: declared
  description: Liveness and the state of the search index.
  name: Calculate.co.nz Service API
  slug: calculate-co-nz-service-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/calculate-co-nz/agentic-access/calculate-co-nz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calculate-co-nz-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/calculate-co-nz/plans/calculate-co-nz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calculate-co-nz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/calculate-co-nz/rules/calculate-co-nz-rules.yml
  title: ''
  type: Spectral
  url: rules/calculate-co-nz-rules.yml
- group: design
  href: https://artifacts.apis.io/calculate-co-nz/json-ld/calculate-co-nz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/calculate-co-nz-context.jsonld
- group: design
  href: https://artifacts.apis.io/calculate-co-nz/vocabulary/calculate-co-nz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calculate-co-nz-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/calculate-co-nz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/calculate-co-nz/data-model/calculate-co-nz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/calculate-co-nz-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://calculate.co.nz/about-us.php
- group: design
  href: https://artifacts.apis.io/calculate-co-nz/errors/calculate-co-nz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calculate-co-nz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/calculate-co-nz/conformance/calculate-co-nz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calculate-co-nz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calculate-co-nz/llms/calculate-co-nz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calculate-co-nz-llms.txt
- group: auth
  href: https://artifacts.apis.io/calculate-co-nz/well-known/calculate-co-nz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calculate-co-nz-security.txt
- group: auth
  href: https://artifacts.apis.io/calculate-co-nz/well-known/calculate-co-nz-calculate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calculate-co-nz-calculate-security.txt
- group: agent
  href: https://artifacts.apis.io/calculate-co-nz/well-known/calculate-co-nz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calculate-co-nz-well-known.yml
- group: other
  href: https://artifacts.apis.io/calculate-co-nz/hosts/calculate-co-nz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calculate-co-nz-hosts.yml
- group: other
  href: https://artifacts.apis.io/calculate-co-nz/vendors/calculate-co-nz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calculate-co-nz-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.calculate.co.nz/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calculate.co.nz/privacy-policy.php
- group: commercial
  title: ''
  type: Pricing
  url: https://www.calculate.co.nz/learning-center/pricing-your-home-guide.php
- group: docs
  title: ''
  type: APIReference
  url: https://www.calculate.co.nz/llms.txt
- group: auth
  href: https://artifacts.apis.io/calculate-co-nz/authentication/calculate-co-nz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calculate-co-nz-authentication.yml
- group: auth
  href: https://artifacts.apis.io/calculate-co-nz/security/calculate-co-nz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/calculate-co-nz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/calculate-co-nz/security/calculate-co-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calculate-co-nz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calculate.co.nz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.calculate.co.nz/
- group: docs
  title: ''
  type: Documentation
  url: https://www.calculate.co.nz/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.calculate.co.nz/learning-center/
- group: company
  title: ''
  type: About
  url: https://www.calculate.co.nz/about-us.php
created: '2026-11-03'
description: Calculate.co.nz provides New Zealand’s most comprehensive free collection of online calculators and financial literacy guides. It offers over 2,490 NZ‑specific calculators covering tax, GST, KiwiSaver, mortgages, insurance and more, plus 433 plain‑English guides and 31 learning pathways. Independent, no sign‑up required, and trusted by over two million Kiwis since 2019.
image: https://www.calculate.co.nz/calculate_logo.png
json_schemas:
- name: ElectricityCostResponse
  property_count: 2
  slug: calculate-co-nz-electricity-cost-response
- name: FinalPayRequest
  property_count: 16
  slug: calculate-co-nz-final-pay-request
- name: HolidayPayRequest
  property_count: 24
  slug: calculate-co-nz-holiday-pay-request
- name: ImportDutyResponse
  property_count: 2
  slug: calculate-co-nz-import-duty-response
- name: MinimumWageResponse
  property_count: 2
  slug: calculate-co-nz-minimum-wage-response
- name: NceaRankScoreResponse
  property_count: 2
  slug: calculate-co-nz-ncea-rank-score-response
jsonld:
- class_count: 120
  name: Calculate Co Nz Context
  property_count: 606
  slug: calculate-co-nz-context
layout: provider
modified: '2026-11-03'
name: Calculate.co.nz
nav: Providers
network: true
overview: 'Calculate.co.nz publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calculators API, Discovery API, Reference data API, and 1 more. Tagged areas include Company, Finance, Calculators, New Zealand, and Free.


  The Calculate.co.nz catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Calculate.co.nz''s developer surface includes pricing, API reference, authentication, documentation, getting-started guide, and 23 more developer resources.'
plans:
- name: Calculate Co Nz Plans Pricing
  plan_count: 6
  slug: calculate-co-nz-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Calculate.co.nz API Rules
  rule_count: 67
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 6
  slug: calculate-co-nz-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 65.3
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Calculate Co Nz Authentication
  slug: calculate-co-nz-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Calculate Co Nz Domain Security
  slug: calculate-co-nz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Calculate Co Nz Vulnerability Disclosure
  slug: calculate-co-nz-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: calculate-co-nz-calculate-take-home-pay
  slug: calculate-co-nz-calculate-take-home-pay
slug: calculate-co-nz
tags:
- Company
- Finance
- Calculators
- New Zealand
- Free
- Education
website: https://calculate.co.nz/
---
