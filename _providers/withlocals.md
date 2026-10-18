---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Withlocals Agentic Access
  operation_count: 12
  slug: withlocals-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- baseURL: https://test-api.withlocals.com/v1/partner
  baseurl_source: declared
  description: Availability calendar.
  name: Withlocals Availability API
  slug: withlocals-availability-api
- baseURL: https://test-api.withlocals.com/v1/partner
  baseurl_source: declared
  description: Reserve, confirm, amend, cancel, and read bookings.
  name: Withlocals Bookings API
  slug: withlocals-bookings-api
- baseURL: https://test-api.withlocals.com/v1/partner
  baseurl_source: declared
  description: Bookable products.
  name: Withlocals Products API
  slug: withlocals-products-api
- baseURL: https://test-api.withlocals.com/v1/partner
  baseurl_source: declared
  description: Self-describing supplier metadata.
  name: Withlocals Supplier API
  slug: withlocals-supplier-api
- baseURL: https://test-api.withlocals.com/v1/partner
  baseurl_source: declared
  description: Out-of-band events delivered by Withlocals to a partner-registered URL. Register at `PUT /webhooks`. See the *Webhooks* section for the delivery contract and the events Withlocals sends.
  name: Withlocals Webhooks API
  slug: withlocals-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Withlocals Webhooks
  slug: withlocals-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/agentic-access/withlocals-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/withlocals-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/rules/withlocals-rules.yml
  title: ''
  type: Spectral
  url: rules/withlocals-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/rules/withlocals-partner-api-doc-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/withlocals-partner-api-doc-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/json-ld/withlocals-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/withlocals-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/vocabulary/withlocals-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/withlocals-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/asyncapi/withlocals-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/withlocals-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/data-model/withlocals-data-model.yml
  title: ''
  type: DataModel
  url: data-model/withlocals-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/conventions/withlocals-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/withlocals-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/conventions/withlocals-conventions.yml
  title: ''
  type: Conventions
  url: conventions/withlocals-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/sandbox/withlocals-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/withlocals-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/security/withlocals-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/withlocals-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/lifecycle/withlocals-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/withlocals-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/errors/withlocals-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/withlocals-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/errors/withlocals-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/withlocals-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/conformance/withlocals-conformance.yml
  title: ''
  type: Conformance
  url: conformance/withlocals-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/overlays/withlocals-partner-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/withlocals-partner-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/llms/withlocals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withlocals-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/well-known/withlocals-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/withlocals-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/well-known/withlocals-helpcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/withlocals-helpcenter-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/well-known/withlocals-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withlocals-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/hosts/withlocals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withlocals-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/vendors/withlocals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withlocals-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/packages/withlocals-packages.yml
  title: ''
  type: SDKs
  url: packages/withlocals-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/packages/withlocals-packages.yml
  title: ''
  type: Packages
  url: packages/withlocals-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/authentication/withlocals-authentication.yml
  title: ''
  type: Authentication
  url: authentication/withlocals-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/security/withlocals-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/withlocals-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/security/withlocals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withlocals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withlocals.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/WithlocalsDev/partner-api-doc/blob/d56d26baa8ec926871b573ae62522d2ffa6cbf61/.spectral.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.withlocals.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.withlocals.com/api-reference/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.withlocals.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WithlocalsDev
- group: start
  title: ''
  type: SignUp
  url: https://www.withlocals.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.withlocals.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withlocals.com/info/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withlocals.com/info/privacy-policy/
created: '2026-10-09'
description: Withlocals is an experiential travel platform that connects travelers with verified local hosts for private, personalized tours, food experiences and home dinners — over 2,500 experiences in more than 250 destinations (per withlocals.com). It publishes a Withlocals Partner API for distribution partners, documented at developers.withlocals.com, and maintains the WithlocalsDev GitHub organization.
image: https://withlocals-com-res.cloudinary.com/image/upload/w_800,h_600,c_fill,g_auto,q_auto,f_auto/441436ac4b7884bfc389f46739606bf8
json_schemas:
- name: AvailabilityRequest
  property_count: 2
  slug: withlocals-availability-request
- name: Booking
  property_count: 16
  slug: withlocals-booking
- name: CreateBookingRequest
  property_count: 10
  slug: withlocals-create-booking-request
- name: Product
  property_count: 11
  slug: withlocals-product
- name: Supplier
  property_count: 2
  slug: withlocals-supplier
- name: Webhook
  property_count: 2
  slug: withlocals-webhook
jsonld:
- class_count: 22
  name: Withlocals Context
  property_count: 68
  slug: withlocals-context
layout: provider
modified: '2026-10-09'
name: Withlocals
nav: Providers
network: true
overview: 'Withlocals publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Products API, and 2 more. Tagged areas include Company, Travel, Tours, Experience, and Tourism.


  The Withlocals catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Withlocals'' developer surface includes sandbox, authentication, API reference, signup flow, and 34 more developer resources.'
plans:
- name: Withlocals Plans Pricing
  plan_count: 0
  slug: withlocals-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Withlocals Rate Limits
  slug: withlocals-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Withlocals — partner api doc rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: withlocals-partner-api-doc-spectral-rules
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Withlocals API Rules
  rule_count: 19
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 0
  slug: withlocals-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 78.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 23.7
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/withlocals/refs/heads/main/screenshots/withlocals-2026-10-11T195734.png
security:
- kind: authentication
  name: Withlocals Authentication
  slug: withlocals-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Withlocals Domain Security
  slug: withlocals-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Withlocals Vulnerability Disclosure
  slug: withlocals-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: withlocals
tags:
- Company
- Travel
- Tours
- Experience
- Tourism
- Marketplace
- Partner API
website: https://www.withlocals.com/
---
