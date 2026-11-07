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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API for Day3 email marketing and transactional email services. Documentation is available at the developer portal.
  name: Day3 API
  slug: day3-api
- baseURL: https://go.day3.app
  baseurl_source: declared
  description: 'day3 API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: day3 API
  slug: day3-app-api
artifact_total: 16
asyncapis:
- description: ''
  name: Day3 App Webhooks
  slug: day3-app-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/day3-app/plans/day3-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/day3-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/day3-app/rules/day3-app-rules.yml
  title: ''
  type: Spectral
  url: rules/day3-app-rules.yml
- group: design
  href: https://artifacts.apis.io/day3-app/json-ld/day3-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/day3-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/day3-app/vocabulary/day3-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/day3-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/day3-app/asyncapi/day3-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/day3-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/day3-app/data-model/day3-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/day3-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/day3-app/conventions/day3-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/day3-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/day3-app/conventions/day3-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/day3-app-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://day3.app/security
- group: auth
  href: https://artifacts.apis.io/day3-app/authentication/day3-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/day3-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/day3-app/conformance/day3-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/day3-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/day3-app/llms/day3-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/day3-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/day3-app/well-known/day3-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/day3-app-security.txt
- group: agent
  href: https://artifacts.apis.io/day3-app/well-known/day3-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/day3-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/day3-app/hosts/day3-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/day3-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/day3-app/vendors/day3-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/day3-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://day3.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://day3.app/features/signup-forms
- group: auth
  title: ''
  type: Security
  url: https://day3.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://day3.app/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://day3.app/changelog
- group: company
  title: ''
  type: Blog
  url: https://day3.app/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.day3.app/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.day3.app\
- group: auth
  href: https://artifacts.apis.io/day3-app/security/day3-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/day3-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/day3-app/security/day3-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/day3-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/day3-app/security/day3-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/day3-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://day3.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.day3.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://day3.app/pricing
- group: operate
  title: ''
  type: Support
  url: mailto:hello@day3.app
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found despite documented API reference.
  evidence:
  - status: 200
    url: https://docs.day3.app/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Day3 provides email marketing and transactional email services billed by the number of emails sent. It offers unlimited subscribers, tiered pricing starting at $1 per month, and features such as deliverability tools, GDPR compliance, and one‑click unsubscribe. The platform targets startups and indie developers looking for a simple, usage‑based pricing model.
image: https://day3.app/opengraph-image?0c8c7c3940d0fd10
json_schemas:
- name: GetEmailsIdResponse
  property_count: 10
  slug: day3-app-get-emails-id-response
- name: GetV1WebhooksResponse
  property_count: 11
  slug: day3-app-get-v1-webhooks-response
- name: GetV1WebhooksWebhookidDeliveriesResponse
  property_count: 13
  slug: day3-app-get-v1-webhooks-webhookid-deliveries-response
- name: GetV1WebhooksWebhookidResponse
  property_count: 11
  slug: day3-app-get-v1-webhooks-webhookid-response
- name: PostApiV1EmailsResponse
  property_count: 10
  slug: day3-app-post-api-v1-emails-response
- name: PostYourEndpointRequest
  property_count: 4
  slug: day3-app-post-your-endpoint-request
jsonld:
- class_count: 19
  name: Day3 App Context
  property_count: 34
  slug: day3-app-context
layout: provider
modified: '2026-11-05'
name: day3
nav: Providers
network: true
overview: 'day3 is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Transactional Email, Software-as-a-Service, and Startup Tools.


  The day3 catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  day3''s developer surface includes authentication, signup flow, changelog, engineering blog, getting-started guide, documentation, pricing, and 24 more developer resources.'
plans:
- name: Day3 App Plans Pricing
  plan_count: 9
  slug: day3-app-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: day3 API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: day3-app-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 33.8
    developer_ergonomics: 50.0
    discoverability: 48.2
    operational_transparency: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Day3 App Authentication
  slug: day3-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Day3 App Domain Security
  slug: day3-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Day3 App Vulnerability Disclosure
  slug: day3-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Day3 App Trust Center
  slug: day3-app-trust-center
  summary_line: SOC 2, GDPR
slug: day3-app
tags:
- Email Marketing
- Transactional Email
- Software-as-a-Service
- Startup Tools
website: https://day3.app/
---
