---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hoursquare Agentic Access
  operation_count: 7
  slug: hoursquare-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.hoursquare.com
  baseurl_source: declared
  description: The Attendance API from HourSquare — 2 operation(s) for attendance.
  name: HourSquare Attendance API
  slug: hoursquare-attendance-api
- baseURL: https://api.hoursquare.com
  baseurl_source: declared
  description: The Employees API from HourSquare — 2 operation(s) for employees.
  name: HourSquare Employees API
  slug: hoursquare-employees-api
- baseURL: https://api.hoursquare.com
  baseurl_source: declared
  description: The Me API from HourSquare — 1 operation(s) for me.
  name: HourSquare Me API
  slug: hoursquare-me-api
- baseURL: https://api.hoursquare.com
  baseurl_source: declared
  description: Turning an API key into a short-lived access token.
  name: HourSquare OAuth API
  slug: hoursquare-oauth-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/hoursquare/agentic-access/hoursquare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hoursquare-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/hoursquare/rate-limits/hoursquare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hoursquare-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hoursquare/plans/hoursquare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hoursquare-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/rules/hoursquare-rules.yml
  title: ''
  type: Spectral
  url: rules/hoursquare-rules.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/json-ld/hoursquare-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hoursquare-context.jsonld
- group: design
  href: https://artifacts.apis.io/hoursquare/vocabulary/hoursquare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hoursquare-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hoursquare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/data-model/hoursquare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hoursquare-data-model.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/conventions/hoursquare-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hoursquare-conventions.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/conventions/hoursquare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hoursquare-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hoursquare.com/security/
- group: auth
  href: https://artifacts.apis.io/hoursquare/authentication/hoursquare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hoursquare-authentication.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/errors/hoursquare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hoursquare-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hoursquare/conformance/hoursquare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hoursquare-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hoursquare/llms/hoursquare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hoursquare-llms.txt
- group: auth
  href: https://artifacts.apis.io/hoursquare/well-known/hoursquare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hoursquare-security.txt
- group: agent
  href: https://artifacts.apis.io/hoursquare/well-known/hoursquare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hoursquare-well-known.yml
- group: other
  href: https://artifacts.apis.io/hoursquare/hosts/hoursquare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hoursquare-hosts.yml
- group: other
  href: https://artifacts.apis.io/hoursquare/vendors/hoursquare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hoursquare-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hoursquare.com/terms-conditions/
- group: start
  title: ''
  type: SignUp
  url: https://hoursquare.com/register/
- group: auth
  title: ''
  type: Security
  url: https://hoursquare.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hoursquare.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://hoursquare.com/tools/hr-setup-planner/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.hoursquare.com</code
- group: auth
  href: https://artifacts.apis.io/hoursquare/scopes/hoursquare-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hoursquare-scopes.yml
- group: auth
  href: https://artifacts.apis.io/hoursquare/security/hoursquare-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hoursquare-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hoursquare/security/hoursquare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hoursquare-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hoursquare/security/hoursquare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hoursquare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hoursquare.com
- group: docs
  title: ''
  type: Documentation
  url: https://hoursquare.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://hoursquare.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://hoursquare.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://hoursquare.com/contact/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://hoursquare.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: HourSquare provides HR software for people, time off, time tracking and payroll in one workspace. It offers a free forever plan for up to 10 people and scalable solutions for larger teams, focusing on simplifying workforce management and payroll processing.
image: https://hoursquare.com/og-image.jpg
json_schemas:
- name: CreateTimeEntryRequest
  property_count: 5
  slug: hoursquare-create-time-entry-request
- name: MeResponse
  property_count: 8
  slug: hoursquare-me-response
- name: OAuthTokenResponse
  property_count: 3
  slug: hoursquare-oauth-token-response
- name: SetEmployeeExternalIdRequest
  property_count: 1
  slug: hoursquare-set-employee-external-id-request
- name: TimeClockEventRequest
  property_count: 5
  slug: hoursquare-time-clock-event-request
- name: TimeEntryWriteResponse
  property_count: 13
  slug: hoursquare-time-entry-write-response
jsonld:
- class_count: 19
  name: Hoursquare Context
  property_count: 55
  slug: hoursquare-context
layout: provider
modified: '2026-11-03'
name: HourSquare
nav: Providers
network: true
overview: 'HourSquare publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attendance API, Employees API, Me API, and 1 more. Tagged areas include Human Resources, Payroll, Time Tracking, Workforce Management, and Software-as-a-Service.


  The HourSquare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HourSquare''s developer surface includes authentication, signup flow, getting-started guide, documentation, engineering blog, pricing, support, and 27 more developer resources.'
plans:
- name: Hoursquare Plans Pricing
  plan_count: 1
  slug: hoursquare-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Hoursquare Rate Limits
  slug: hoursquare-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: HourSquare API Rules
  rule_count: 59
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 4
  slug: hoursquare-rules
scopes:
- name: Hoursquare Scopes
  scope_count: 5
  slug: hoursquare-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 26.3
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
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hoursquare Authentication
  slug: hoursquare-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hoursquare Domain Security
  slug: hoursquare-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Hoursquare Vulnerability Disclosure
  slug: hoursquare-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Hoursquare Trust Center
  slug: hoursquare-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: hoursquare-attendance-record
  slug: hoursquare-attendance-record
slug: hoursquare
tags:
- Human Resources
- Payroll
- Time Tracking
- Workforce Management
- Software-as-a-Service
website: https://hoursquare.com
---
