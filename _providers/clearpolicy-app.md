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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Access your organization's people, groups, documents, and document requests.
  name: ClearPolicy API
  slug: clearpolicy-api
- baseURL: https://api.clearpolicy.app/api/v1
  baseurl_source: declared
  description: Access your organization's people, groups, documents, and document requests. API tokens are organization-scoped and require an active trial or subscription. Owners and administrators can use all liste
  name: ClearPolicy API API
  slug: clearpolicy-api-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/clearpolicy-app/rules/clearpolicy-app-rules.yml
  title: ''
  type: Spectral
  url: rules/clearpolicy-app-rules.yml
- group: design
  href: https://artifacts.apis.io/clearpolicy-app/json-ld/clearpolicy-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearpolicy-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearpolicy-app/vocabulary/clearpolicy-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearpolicy-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clearpolicy-app/conformance/clearpolicy-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearpolicy-app-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/clearpolicy-app/plans/clearpolicy-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearpolicy-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clearpolicy-app/data-model/clearpolicy-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearpolicy-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/clearpolicy-app/changelog/clearpolicy-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clearpolicy-app-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.clearpolicy.app/security/
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/authentication/clearpolicy-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearpolicy-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/clearpolicy-app/errors/clearpolicy-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearpolicy-app-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/clearpolicy-app/llms/clearpolicy-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearpolicy-app-llms.txt
- group: other
  href: https://artifacts.apis.io/clearpolicy-app/a2a/clearpolicy-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clearpolicy-app-a2a.yml
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/well-known/clearpolicy-app-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearpolicy-app-www-security.txt
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/well-known/clearpolicy-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearpolicy-app-security.txt
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/well-known/clearpolicy-app-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearpolicy-app-app-security.txt
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/well-known/clearpolicy-app-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearpolicy-app-api-security.txt
- group: agent
  href: https://artifacts.apis.io/clearpolicy-app/well-known/clearpolicy-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearpolicy-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearpolicy-app/hosts/clearpolicy-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearpolicy-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearpolicy-app/vendors/clearpolicy-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearpolicy-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearpolicy.app/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://www.clearpolicy.app/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearpolicy.app/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.clearpolicy.app/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.clearpolicy.app/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.clearpolicy.app/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clearpolicy.app/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clearpolicy.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clearpolicy.app/api-reference/me/get-current-user
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/security/clearpolicy-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clearpolicy-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/security/clearpolicy-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearpolicy-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clearpolicy-app/security/clearpolicy-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearpolicy-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearpolicy.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clearpolicy.app/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.clearpolicy.app/support/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://clearpolicy.app/openapi.json
  - status: null
    url: https://app.clearpolicy.app/openapi.json
  - status: null
    url: https://docs.clearpolicy.app/openapi.json
  - status: null
    url: https://docs.clearpolicy.app/mcp
  - status: null
    url: https://www.clearpolicy.app/openapi.json
  - status: null
    url: https://api.clearpolicy.app/openapi.json
  reason: partner-login
  state: gated
created: '2026-11-03'
description: ClearPolicy provides policy acknowledgment and e‑signature software for small teams, nonprofits, churches, and volunteer‑led organizations. Users can upload policies, send them for signatures, and automatically follow up to ensure completion. The platform offers a 30‑day free trial and then a subscription at $29 per month, with unlimited people and documents. It emphasizes ease of use, compliance tracking, and secure proof of acknowledgment for businesses and community groups.
image: https://www.clearpolicy.app/_astro/og-image.Do-T3NVu_Z1rQFsi.jpg
json_schemas:
- name: AddGroupPeopleRequest
  property_count: 1
  slug: clearpolicy-app-add-group-people-request
- name: AttestationRequest
  property_count: 21
  slug: clearpolicy-app-attestation-request
- name: CreateAttestationRequestBody
  property_count: 4
  slug: clearpolicy-app-create-attestation-request-body
- name: CreatePersonRequest
  property_count: 4
  slug: clearpolicy-app-create-person-request
- name: Me
  property_count: 4
  slug: clearpolicy-app-me
- name: Person
  property_count: 12
  slug: clearpolicy-app-person
jsonld:
- class_count: 17
  name: Clearpolicy App Context
  property_count: 57
  slug: clearpolicy-app-context
layout: provider
modified: '2026-11-03'
name: ClearPolicy
nav: Providers
network: true
overview: 'ClearPolicy publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Policy, E-Signature, Software-as-a-Service, Small Business, and Non-Profit.


  The ClearPolicy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClearPolicy''s developer surface includes changelog, authentication, engineering blog, getting-started guide, documentation, API reference, pricing, and 27 more developer resources.'
plans:
- name: Clearpolicy App Plans Pricing
  plan_count: 1
  slug: clearpolicy-app-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: ClearPolicy API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: clearpolicy-app-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clearpolicy App Authentication
  slug: clearpolicy-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Clearpolicy App Domain Security
  slug: clearpolicy-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearpolicy App Vulnerability Disclosure
  slug: clearpolicy-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clearpolicy App Trust Center
  slug: clearpolicy-app-trust-center
  summary_line: SOC 2, ISO 27001
slug: clearpolicy-app
tags:
- Policy
- E-Signature
- Software-as-a-Service
- Small Business
- Non-Profit
website: https://clearpolicy.app/
---
