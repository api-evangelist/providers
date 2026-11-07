---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sendbridge Com Agentic Access
  operation_count: 9
  slug: sendbridge-com-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.sendbridge.com/v2
  baseurl_source: declared
  description: Inspect the current API key. Free — does not charge credits.
  name: SendBridge Account API
  slug: sendbridge-com-account-api
- baseURL: https://api.sendbridge.com/v2
  baseurl_source: declared
  description: Read monitored domains, 7-day DMARC stats, and recent aggregate reports. Live calls are free. Test keys return fixtures.
  name: SendBridge DMARC API
  slug: sendbridge-com-dmarc-api
- baseURL: https://api.sendbridge.com/v2
  baseurl_source: declared
  description: Generate a unique inbox, send a message to it, then poll the deliverability report. Live calls charge 200 credits. Test keys return a completed demo report for free.
  name: SendBridge Mail Tester API
  slug: sendbridge-com-mail-tester-api
- baseURL: https://api.sendbridge.com/v2
  baseurl_source: declared
  description: Verify a single email address. Charges 1 credit on live keys. Test keys return fixtures and are free.
  name: SendBridge Validation API
  slug: sendbridge-com-validation-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/sendbridge-com/agentic-access/sendbridge-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendbridge-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/sendbridge-com/rate-limits/sendbridge-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sendbridge-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sendbridge-com/plans/sendbridge-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendbridge-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/rules/sendbridge-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sendbridge-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/json-ld/sendbridge-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sendbridge-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sendbridge-com/vocabulary/sendbridge-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendbridge-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sendbridge-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/data-model/sendbridge-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendbridge-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/conventions/sendbridge-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sendbridge-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/conventions/sendbridge-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendbridge-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sendbridge-com/authentication/sendbridge-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendbridge-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/lifecycle/sendbridge-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sendbridge-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/errors/sendbridge-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendbridge-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sendbridge-com/conformance/sendbridge-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendbridge-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/sendbridge-com/hosts/sendbridge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendbridge-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sendbridge-com/vendors/sendbridge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sendbridge-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendbridge.com/tos
- group: start
  title: ''
  type: SignUp
  url: https://app.sendbridge.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendbridge.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendbridge
- group: auth
  href: https://artifacts.apis.io/sendbridge-com/security/sendbridge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendbridge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendbridge.com
- group: docs
  title: ''
  type: Documentation
  url: https://sendbridge.com/email-verification-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.sendbridge.com/#tag/validation
- group: commercial
  title: ''
  type: Pricing
  url: https://sendbridge.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://sendbridge.com/support
- group: company
  title: ''
  type: Blog
  url: https://sendbridge.com/blog
created: '2026-10-29'
description: SendBridge provides an email verification service that helps businesses ensure high deliverability by validating email addresses in real time. Their API offers a simple GET endpoint that returns JSON indicating whether an address is valid, disposable, or risky, enabling marketers and developers to clean mailing lists, reduce bounce rates, and improve inbox placement. The platform emphasizes fast responses, easy integration, and detailed validation results, supporting use cases such as sign‑up forms, CRM data hygiene, and campaign targeting.
image: https://sendbridge.com/assets/img/logo1.svg
json_schemas:
- name: CreateMailTestRequest
  property_count: 1
  slug: sendbridge-com-create-mail-test-request
- name: MailTestAddress
  property_count: 5
  slug: sendbridge-com-mail-test-address
- name: MailTestResult
  property_count: 3
  slug: sendbridge-com-mail-test-result
- name: Me
  property_count: 6
  slug: sendbridge-com-me
- name: Meta
  property_count: 4
  slug: sendbridge-com-meta
- name: VerificationResult
  property_count: 7
  slug: sendbridge-com-verification-result
jsonld:
- class_count: 11
  name: Sendbridge Com Context
  property_count: 62
  slug: sendbridge-com-context
layout: provider
modified: '2026-10-29'
name: SendBridge
nav: Providers
network: true
overview: 'SendBridge publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, DMARC API, Mail Tester API, and 1 more. Tagged areas include Email, Verification, Deliverability, Validation, and Marketing.


  The SendBridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SendBridge''s developer surface includes authentication, signup flow, documentation, API reference, pricing, support, engineering blog, and 20 more developer resources.'
plans:
- name: Sendbridge Com Plans Pricing
  plan_count: 4
  slug: sendbridge-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Sendbridge Com Rate Limits
  slug: sendbridge-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: SendBridge API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: sendbridge-com-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 63.2
    developer_ergonomics: 30.2
    discoverability: 66.1
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sendbridge-com/sendbridge-com-2026-11-03T143021.png
security:
- kind: authentication
  name: Sendbridge Com Authentication
  slug: sendbridge-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sendbridge Com Domain Security
  slug: sendbridge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: email-verification
  slug: sendbridge-com-email-verification
slug: sendbridge-com
tags:
- Email
- Verification
- Deliverability
- Validation
- Marketing
- Services
website: https://sendbridge.com
---
