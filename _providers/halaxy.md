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
  - rate-limits
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Halaxy Agentic Access
  operation_count: 49
  slug: halaxy-agentic-access
  summary_line: 49 operations · 15 acting
api_count: 1
apis:
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Appointment API from Halaxy — 4 operation(s) for appointment.
  name: Halaxy Appointment API
  slug: halaxy-appointment-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The ChargeItemDefinition API from Halaxy — 2 operation(s) for chargeitemdefinition.
  name: Halaxy Charge Item Definition API
  slug: halaxy-chargeitemdefinition-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Coverage API from Halaxy — 2 operation(s) for coverage.
  name: Halaxy Coverage API
  slug: halaxy-coverage-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Invoice API from Halaxy — 2 operation(s) for invoice.
  name: Halaxy Invoice API
  slug: halaxy-invoice-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The InvoiceLine API from Halaxy — 2 operation(s) for invoiceline.
  name: Halaxy Invoice Line API
  slug: halaxy-invoiceline-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Organization API from Halaxy — 2 operation(s) for organization.
  name: Halaxy Organization API
  slug: halaxy-organization-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Patient API from Halaxy — 3 operation(s) for patient.
  name: Halaxy Patient API
  slug: halaxy-patient-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The PaymentTransaction API from Halaxy — 2 operation(s) for paymenttransaction.
  name: Halaxy Payment Transaction API
  slug: halaxy-paymenttransaction-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Practitioner API from Halaxy — 2 operation(s) for practitioner.
  name: Halaxy Practitioner API
  slug: halaxy-practitioner-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Referral API from Halaxy — 2 operation(s) for referral.
  name: Halaxy Referral API
  slug: halaxy-referral-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The ReferralDefinition API from Halaxy — 2 operation(s) for referraldefinition.
  name: Halaxy Referral Definition API
  slug: halaxy-referraldefinition-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Schedule API from Halaxy — 3 operation(s) for schedule.
  name: Halaxy Schedule API
  slug: halaxy-schedule-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Slot API from Halaxy — 2 operation(s) for slot.
  name: Halaxy Slot API
  slug: halaxy-slot-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Capability Statement API from Halaxy — 1 operation(s) for capability statement.
  name: Halaxy Capability Statement API
  slug: halaxy-capability-statement-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Document Reference API from Halaxy — 1 operation(s) for document reference.
  name: Halaxy Document Reference API
  slug: halaxy-document-reference-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Healthcare Service API from Halaxy — 2 operation(s) for healthcare service.
  name: Halaxy Healthcare Service API
  slug: halaxy-healthcare-service-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Practitioner Role API from Halaxy — 2 operation(s) for practitioner role.
  name: Halaxy Practitioner Role API
  slug: halaxy-practitioner-role-api
- baseURL: https://au-api.halaxy.com
  baseurl_source: declared
  description: The Search Parameter API from Halaxy — 1 operation(s) for search parameter.
  name: Halaxy Search Parameter API
  slug: halaxy-search-parameter-api
artifact_total: 40
common:
- group: agent
  href: https://artifacts.apis.io/halaxy/agentic-access/halaxy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/halaxy-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/halaxy/rate-limits/halaxy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/halaxy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/halaxy/plans/halaxy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/halaxy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/halaxy/rules/halaxy-rules.yml
  title: ''
  type: Spectral
  url: rules/halaxy-rules.yml
- group: design
  href: https://artifacts.apis.io/halaxy/json-ld/halaxy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/halaxy-context.jsonld
- group: design
  href: https://artifacts.apis.io/halaxy/vocabulary/halaxy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/halaxy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/halaxy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/halaxy/data-model/halaxy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/halaxy-data-model.yml
- group: operate
  href: https://artifacts.apis.io/halaxy/changelog/halaxy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/halaxy-changelog.yml
- group: design
  href: https://artifacts.apis.io/halaxy/conventions/halaxy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/halaxy-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.halaxy.com/
- group: auth
  href: https://artifacts.apis.io/halaxy/security/halaxy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/halaxy-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/halaxy/lifecycle/halaxy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/halaxy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/halaxy/lifecycle/halaxy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/halaxy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/halaxy/errors/halaxy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/halaxy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/halaxy/conformance/halaxy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/halaxy-conformance.yml
- group: other
  href: https://artifacts.apis.io/halaxy/overlays/halaxy-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/halaxy-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/halaxy/llms/halaxy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/halaxy-llms.txt
- group: auth
  href: https://artifacts.apis.io/halaxy/well-known/halaxy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/halaxy-security.txt
- group: agent
  href: https://artifacts.apis.io/halaxy/well-known/halaxy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/halaxy-well-known.yml
- group: other
  href: https://artifacts.apis.io/halaxy/hosts/halaxy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/halaxy-hosts.yml
- group: build
  href: https://artifacts.apis.io/halaxy/integrations/halaxy-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/halaxy-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/halaxy/vendors/halaxy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/halaxy-vendors.yml
- group: auth
  href: https://artifacts.apis.io/halaxy/authentication/halaxy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/halaxy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.halaxy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.halaxy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.halaxy.com/docs/about-this-guide
- group: docs
  title: ''
  type: APIReference
  url: https://developers.halaxy.com/reference/patient
- group: learn
  title: ''
  type: Recipes
  url: https://developers.halaxy.com/recipes
- group: operate
  title: ''
  type: Support
  url: https://support.halaxy.com/hc/en-au
- group: company
  title: ''
  type: Blog
  url: https://blog.halaxy.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://blog.halaxy.com/tag/whats-new/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.halaxy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.halaxy.com/a/signup
- group: start
  title: ''
  type: Login
  url: https://www.halaxy.com/a/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.halaxy.com/terms/practitioner/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.halaxy.com/privacy/
- group: company
  title: ''
  type: AboutUs
  url: https://www.halaxy.com/article/about-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/halaxy
- group: other
  title: ''
  type: Email
  url: mailto:community@halaxy.com
- group: auth
  href: https://artifacts.apis.io/halaxy/security/halaxy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/halaxy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/halaxy/security/halaxy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/halaxy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/halaxy/security/halaxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/halaxy-domain-security.yml
created: '2026-10-22'
description: Halaxy is a global health platform built for both practitioners and patients, providing free practice management software including online bookings, clinical notes, invoicing and payments, telehealth and patient records for allied health and medical practices in Australia, New Zealand, the UK, Ireland, Canada, Singapore and other countries. Its developer portal at developers.halaxy.com documents the Halaxy API, a FHIR R4-based REST API (OAuth-secured, with AU and EU production hosts) covering resources such as Patient, Appointment, Practitioner, Schedule, Slot, Invoice and Coverage, plus webhooks.
examples:
- key_count: 17
  name: Halaxy Fhir Capabilitystatement
  slug: halaxy-fhir-capabilitystatement
image: https://files.readme.io/8dfcf90955338f72c92553c41e4bf930d700d518db32bffdab5ba77c44b3656a-logo.png
json_schemas:
- name: CapabilityStatement.jsonfhir
  property_count: 26
  slug: halaxy-capability-statement-jsonfhir
- name: CapabilityStatement
  property_count: 26
  slug: halaxy-capability-statement
- name: Referral.jsonfhir
  property_count: 20
  slug: halaxy-referral-jsonfhir
- name: Referral
  property_count: 20
  slug: halaxy-referral
- name: SearchParameter.jsonfhir
  property_count: 28
  slug: halaxy-search-parameter-jsonfhir
- name: SearchParameter
  property_count: 28
  slug: halaxy-search-parameter
jsonld:
- class_count: 120
  name: Halaxy Context
  property_count: 186
  slug: halaxy-context
layout: provider
modified: '2026-10-22'
name: Halaxy
nav: Providers
network: true
overview: 'Halaxy publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointment API, Charge Item Definition API, Coverage API, and 15 more. Tagged areas include Company, Healthcare, Practice Management, FHIR, and Telehealth.


  The Halaxy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Halaxy''s developer surface includes changelog, authentication, documentation, API reference, support, engineering blog, pricing, and 36 more developer resources.'
plans:
- name: Halaxy Plans Pricing
  plan_count: 4
  slug: halaxy-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Halaxy Rate Limits
  slug: halaxy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Halaxy API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 3
  slug: halaxy-rules
scopes:
- name: Halaxy Scopes
  scope_count: 0
  slug: halaxy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 69.1
    developer_ergonomics: 24.4
    discoverability: 73.2
    operational_transparency: 51.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/halaxy/halaxy-2026-11-03T133133.png
security:
- kind: authentication
  name: Halaxy Authentication
  slug: halaxy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Halaxy Domain Security
  slug: halaxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Halaxy Vulnerability Disclosure
  slug: halaxy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Halaxy Trust Center
  slug: halaxy-trust-center
  summary_line: ISO 27001
skill_count: 5
skills:
- name: halaxy-book-an-appointment
  slug: halaxy-book-an-appointment
- name: halaxy-create-a-referral
  slug: halaxy-create-a-referral
- name: halaxy-publish-schedule-slots
  slug: halaxy-publish-schedule-slots
- name: halaxy-reconcile-invoices-and-payments
  slug: halaxy-reconcile-invoices-and-payments
- name: halaxy-register-and-update-a-patient
  slug: halaxy-register-and-update-a-patient
slug: halaxy
tags:
- Company
- Healthcare
- Practice Management
- FHIR
- Telehealth
- Appointments
- Billing
- Patients
website: https://www.halaxy.com/
---
