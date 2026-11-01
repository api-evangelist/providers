---
agent_readiness:
  band: agent-ready
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Transactional email API providing endpoints for sending email, managing domains, templates, webhooks and more.
  name: SecureSMTP API
  slug: securesmtp-api
- description: 'securessmtp-com API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: securessmtp-com API
  slug: securessmtp-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Securessmtp Com Webhooks
  slug: securessmtp-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/securessmtp-com/plans/securessmtp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/securessmtp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/securessmtp-com/rules/securessmtp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/securessmtp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/securessmtp-com/json-ld/securessmtp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/securessmtp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/securessmtp-com/vocabulary/securessmtp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/securessmtp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/securessmtp-com/asyncapi/securessmtp-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/securessmtp-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/securessmtp-com/data-model/securessmtp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/securessmtp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/securessmtp-com/authentication/securessmtp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/securessmtp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/securessmtp-com/conformance/securessmtp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/securessmtp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/securessmtp-com/llms/securessmtp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/securessmtp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/securessmtp-com/well-known/securessmtp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/securessmtp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/securessmtp-com/hosts/securessmtp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/securessmtp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/securessmtp-com/vendors/securessmtp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/securessmtp-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://securessmtp.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://securessmtp.com/press
- group: auth
  href: https://artifacts.apis.io/securessmtp-com/security/securessmtp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/securessmtp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://securessmtp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://securessmtp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://securessmtp.com/docs/api/send-email
- group: start
  title: ''
  type: GettingStarted
  url: https://securessmtp.com/docs/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://securessmtp.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://securessmtp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://securessmtp.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://securessmtp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://securessmtp.com/dpa
- group: operate
  title: ''
  type: StatusPage
  url: https://securessmtp.com/status
- group: company
  title: ''
  type: Blog
  url: https://securessmtp.com/blog
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are JavaScript-rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://securessmtp.com/docs/api/send-email
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: SecureSMTP provides a transactional email API and SMTP service that lets developers send password resets, sign‑in codes, receipts, order updates and other transactional messages. The platform offers a REST API and SMTP integration, DKIM signing, spam checks, analytics, and a dashboard for managing domains, templates, automations and webhooks. Free tier includes 5,000 emails per month with no credit card required, and paid plans add higher volume and advanced features.
json_schemas:
- name: GetApiV1FormsRenderSlugResponse
  property_count: 8
  slug: securessmtp-com-get-api-v1-forms-render-slug-response
- name: GetApiV1MailDomainStatusResponse
  property_count: 7
  slug: securessmtp-com-get-api-v1-mail-domain-status-response
- name: GetApiV1TemplatesResponse
  property_count: 7
  slug: securessmtp-com-get-api-v1-templates-response
- name: GetFormsRenderSlugResponse
  property_count: 8
  slug: securessmtp-com-get-forms-render-slug-response
- name: GetTemplatesResponse
  property_count: 7
  slug: securessmtp-com-get-templates-response
- name: PostFormsSubmitRequest
  property_count: 19
  slug: securessmtp-com-post-forms-submit-request
jsonld:
- class_count: 30
  name: Securessmtp Com Context
  property_count: 78
  slug: securessmtp-com-context
layout: provider
modified: '2026-10-31'
name: securessmtp-com
nav: Providers
network: true
overview: 'securessmtp-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Transactional, API, SMTP, and Service.


  The securessmtp-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  securessmtp-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Securessmtp Com Plans Pricing
  plan_count: 5
  slug: securessmtp-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: securessmtp-com API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: securessmtp-com-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 78.8
    catalog_earned_first_party: 0.0
    catalog_gap: 36.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 70.9
    contract_quality: 55.0
    developer_ergonomics: 47.6
    discoverability: 55.4
    operational_transparency: 34.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Securessmtp Com Authentication
  slug: securessmtp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Securessmtp Com Domain Security
  slug: securessmtp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: securessmtp-com
tags:
- Email
- Transactional
- API
- SMTP
- Service
- SecureSMTP
website: https://securessmtp.com/
---
