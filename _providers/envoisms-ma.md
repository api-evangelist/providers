---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Telecom messaging and phone verification APIs for Morocco
  name: EnvoiSMS API
  slug: envoisms-api
- baseURL: https://api.envoisms.ma/v1
  baseurl_source: declared
  description: Send SMS and WhatsApp messages and verify phone numbers, as JSON over HTTPS.
  name: EnvoiSMS API API
  slug: envoisms-api-api
artifact_total: 17
common:
- group: operate
  href: https://artifacts.apis.io/envoisms-ma/rate-limits/envoisms-ma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/envoisms-ma-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/envoisms-ma/plans/envoisms-ma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/envoisms-ma-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/rules/envoisms-ma-rules.yml
  title: ''
  type: Spectral
  url: rules/envoisms-ma-rules.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/json-ld/envoisms-ma-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/envoisms-ma-context.jsonld
- group: design
  href: https://artifacts.apis.io/envoisms-ma/vocabulary/envoisms-ma-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/envoisms-ma-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/envoisms-ma/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/data-model/envoisms-ma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/envoisms-ma-data-model.yml
- group: operate
  href: https://artifacts.apis.io/envoisms-ma/changelog/envoisms-ma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/envoisms-ma-changelog.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/conventions/envoisms-ma-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/envoisms-ma-conventions.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/conventions/envoisms-ma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/envoisms-ma-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://envoisms.ma/fr/legal/privacy/
- group: auth
  href: https://artifacts.apis.io/envoisms-ma/authentication/envoisms-ma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/envoisms-ma-authentication.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/errors/envoisms-ma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/envoisms-ma-problem-types.yml
- group: design
  href: https://artifacts.apis.io/envoisms-ma/conformance/envoisms-ma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/envoisms-ma-conformance.yml
- group: agent
  href: https://artifacts.apis.io/envoisms-ma/llms/envoisms-ma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/envoisms-ma-llms.txt
- group: other
  href: https://artifacts.apis.io/envoisms-ma/a2a/envoisms-ma-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/envoisms-ma-a2a.yml
- group: auth
  href: https://artifacts.apis.io/envoisms-ma/well-known/envoisms-ma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envoisms-ma-security.txt
- group: auth
  href: https://artifacts.apis.io/envoisms-ma/well-known/envoisms-ma-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/envoisms-ma-app-security.txt
- group: agent
  href: https://artifacts.apis.io/envoisms-ma/well-known/envoisms-ma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/envoisms-ma-well-known.yml
- group: other
  href: https://artifacts.apis.io/envoisms-ma/hosts/envoisms-ma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/envoisms-ma-hosts.yml
- group: other
  href: https://artifacts.apis.io/envoisms-ma/vendors/envoisms-ma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/envoisms-ma-vendors.yml
- group: build
  href: https://artifacts.apis.io/envoisms-ma/packages/envoisms-ma-packages.yml
  title: ''
  type: SDKs
  url: packages/envoisms-ma-packages.yml
- group: build
  href: https://artifacts.apis.io/envoisms-ma/packages/envoisms-ma-packages.yml
  title: ''
  type: Packages
  url: packages/envoisms-ma-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://envoisms.ma/fr/trust/
- group: start
  title: ''
  type: Login
  url: https://envoisms.ma/fr/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://envoisms.ma/fr/docs/changelog/
- group: auth
  href: https://artifacts.apis.io/envoisms-ma/security/envoisms-ma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/envoisms-ma-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/envoisms-ma/security/envoisms-ma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/envoisms-ma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://envoisms.ma/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://envoisms.ma/en/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://envoisms.ma/en/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://envoisms.ma/en/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://envoisms.ma/en/docs/
- group: operate
  title: ''
  type: Support
  url: mailto:support@envoisms.ma
- group: company
  title: ''
  type: Blog
  url: https://envoisms.ma/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envoisms
- group: commercial
  title: ''
  type: Pricing
  url: https://envoisms.ma/en/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://envoisms.ma/en/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://envoisms.ma/en/legal/terms/
created: '2026-10-30'
description: EnvoiSMS.ma provides a RESTful API platform for sending SMS, WhatsApp Business messages, OTP verification, and bulk campaigns across Morocco's major carriers (IAM, Orange, Inwi). Features include real‑time delivery reports, signed webhooks, virtual numbers, and multi‑language support, with pricing from 0.60 MAD per SMS.
image: https://envoisms.ma/logo.png
json_schemas:
- name: BulkSendRequest
  property_count: 3
  slug: envoisms-ma-bulk-send-request
- name: MessageRecord
  property_count: 21
  slug: envoisms-ma-message-record
- name: Message
  property_count: 11
  slug: envoisms-ma-message
- name: QualifiedLead
  property_count: 15
  slug: envoisms-ma-qualified-lead
- name: SendMessageRequest
  property_count: 20
  slug: envoisms-ma-send-message-request
- name: VerifySendRequest
  property_count: 14
  slug: envoisms-ma-verify-send-request
jsonld:
- class_count: 13
  name: Envoisms Ma Context
  property_count: 94
  slug: envoisms-ma-context
layout: provider
modified: '2026-10-30'
name: envoisms-ma
nav: Providers
network: true
overview: 'envoisms-ma publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including EnvoiSMS API API, and 1 more. Tagged areas include Company, SMS, WhatsApp, Messaging, and Morocco.


  The envoisms-ma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  envoisms-ma''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
plans:
- name: Envoisms Ma Plans Pricing
  plan_count: 6
  slug: envoisms-ma-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Envoisms Ma Rate Limits
  slug: envoisms-ma-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: envoisms-ma API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: envoisms-ma-rules
scopes:
- name: Envoisms Ma Scopes
  scope_count: 0
  slug: envoisms-ma-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.2
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 50.5
    discoverability: 66.1
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - morocco
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - mena
    - north-africa
  previous_composite: 63.3
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 38.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/envoisms-ma/envoisms-ma-2026-11-03T131552.png
security:
- kind: authentication
  name: Envoisms Ma Authentication
  slug: envoisms-ma-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Envoisms Ma Domain Security
  slug: envoisms-ma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Envoisms Ma Vulnerability Disclosure
  slug: envoisms-ma-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-analytics
  slug: envoisms-ma-get-analytics
slug: envoisms-ma
tags:
- Company
- SMS
- WhatsApp
- Messaging
- Morocco
- CPaaS
website: https://envoisms.ma/
---
