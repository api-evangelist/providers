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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://<your-tenant>.senseon.io
  baseurl_source: declared
  description: 'SenseOn API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: SenseOn API
  slug: senseon-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/senseon/plans/senseon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/senseon-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/senseon/rules/senseon-rules.yml
  title: ''
  type: Spectral
  url: rules/senseon-rules.yml
- group: design
  href: https://artifacts.apis.io/senseon/json-ld/senseon-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/senseon-context.jsonld
- group: design
  href: https://artifacts.apis.io/senseon/vocabulary/senseon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/senseon-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/senseon/data-model/senseon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/senseon-data-model.yml
- group: operate
  href: https://artifacts.apis.io/senseon/changelog/senseon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/senseon-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.senseon.io/responsible-disclosure-policy
- group: design
  href: https://artifacts.apis.io/senseon/conformance/senseon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/senseon-conformance.yml
- group: agent
  href: https://artifacts.apis.io/senseon/llms/senseon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/senseon-llms.txt
- group: auth
  href: https://artifacts.apis.io/senseon/well-known/senseon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/senseon-security.txt
- group: agent
  href: https://artifacts.apis.io/senseon/well-known/senseon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/senseon-well-known.yml
- group: other
  href: https://artifacts.apis.io/senseon/hosts/senseon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/senseon-hosts.yml
- group: other
  href: https://artifacts.apis.io/senseon/vendors/senseon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/senseon-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.senseon.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.senseon.io/en/latest/onboarding/scoping_questions/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.senseon.io\
- group: auth
  href: https://artifacts.apis.io/senseon/security/senseon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/senseon-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/senseon/security/senseon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/senseon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.senseon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.senseon.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.senseon.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.senseon.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.senseon.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.senseon.io/terms
created: '2026-10-24'
description: SenseOn provides an evidence‑led AI security operations platform that unifies security telemetry, analysts, and AI agents into a governed investigation plane. It offers outcome‑based pricing, integrates with existing security tools, and delivers automated incident response with human oversight. Trusted by Fortune 1000 and public‑sector organizations, SenseOn helps reduce alert noise, accelerate detection, and improve response times across managed‑service environments.
image: https://www.senseon.io/images/og-default.png
json_schemas:
- name: GetV1SettingsResponse
  property_count: 6
  slug: senseon-get-v1-settings-response
- name: PostSenseonapiCaaPatsRequest
  property_count: 3
  slug: senseon-post-senseonapi-caa-pats-request
- name: PostSenseonapiCaaPatsResponse
  property_count: 2
  slug: senseon-post-senseonapi-caa-pats-response
- name: PostSenseonapiServiceAccountsRequest
  property_count: 2
  slug: senseon-post-senseonapi-service-accounts-request
- name: PostSenseonapiServiceAccountsUseridTokenRequest
  property_count: 2
  slug: senseon-post-senseonapi-service-accounts-userid-token-request
- name: PutV1SettingsRequest
  property_count: 1
  slug: senseon-put-v1-settings-request
jsonld:
- class_count: 14
  name: Senseon Context
  property_count: 16
  slug: senseon-context
layout: provider
modified: '2026-10-24'
name: SenseOn
nav: Providers
network: true
overview: 'SenseOn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Artificial Intelligence, Platform, and Incident Response.


  The SenseOn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SenseOn''s developer surface includes changelog, getting-started guide, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Senseon Plans Pricing
  plan_count: 6
  slug: senseon-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: SenseOn API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: senseon-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 51.3
    contract_governance: 22.0
    contract_quality: 26.9
    developer_ergonomics: 16.7
    discoverability: 73.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/senseon/senseon-2026-11-03T143032.png
security:
- kind: domain-security
  name: Senseon Domain Security
  slug: senseon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Senseon Vulnerability Disclosure
  slug: senseon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: senseon
tags:
- Company
- Security
- Artificial Intelligence
- Platform
- Incident Response
website: https://www.senseon.io/
---
