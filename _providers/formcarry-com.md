---
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- baseURL: https://api.formcarry.com
  baseurl_source: declared
  description: 'formcarry-com api API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: formcarry-com api API
  slug: api-api
- baseURL: https://api.formcarry.com
  baseurl_source: declared
  description: 'formcarry-com api reference API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: formcarry-com api reference API
  slug: api-reference-api
artifact_total: 17
asyncapis:
- description: ''
  name: Formcarry Com Webhooks
  slug: formcarry-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/formcarry-com/plans/formcarry-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/formcarry-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/formcarry-com/rules/formcarry-com-rules.yml
  title: ''
  type: Spectral
  url: rules/formcarry-com-rules.yml
- group: design
  href: https://artifacts.apis.io/formcarry-com/json-ld/formcarry-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/formcarry-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/formcarry-com/vocabulary/formcarry-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/formcarry-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/formcarry-com/asyncapi/formcarry-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/formcarry-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/formcarry-com/data-model/formcarry-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/formcarry-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/formcarry-com/authentication/formcarry-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/formcarry-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/formcarry-com/conformance/formcarry-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/formcarry-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/formcarry-com/llms/formcarry-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/formcarry-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/formcarry-com/well-known/formcarry-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/formcarry-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/formcarry-com/hosts/formcarry-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/formcarry-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/formcarry-com/vendors/formcarry-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/formcarry-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://formcarry.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.formcarry.com
- group: start
  title: ''
  type: SignUp
  url: https://app.formcarry.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://formcarry.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://formcarry.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/formcarry
- group: docs
  title: ''
  type: Documentation
  url: https://formcarry.com/docs
- group: company
  title: ''
  type: Blog
  url: https://formcarry.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://formcarry.com/docs/api-reference/forms/list-forms
- group: start
  title: ''
  type: GettingStarted
  url: https://formcarry.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/formcarry-com/security/formcarry-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/formcarry-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://formcarry.com/
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec at https://formcarry.com/api/openapi.json requires an API key, blocking unauthenticated access.
  evidence:
  - status: 200
    url: https://formcarry.com/api/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Formcarry provides a simple API for handling form submissions, file uploads, and email notifications without building backend infrastructure. It enables developers to quickly collect data from web forms, mobile apps, or static sites, offering features like spam protection, custom redirects, and webhook integrations. The service is designed for ease of use, scalability, and security, supporting JSON and multipart/form-data payloads. Formcarry aims to streamline data collection workflows for startups, agencies, and enterprises, reducing the need for custom server-side code and allowing focus on front‑end development and user experience.
image: https://formcarry.com/og-image.jpg
json_schemas:
- name: GetV1EmailServersResponse
  property_count: 2
  slug: formcarry-com-get-v1-email-servers-response
- name: GetV1FormsFormidImagesResponse
  property_count: 1
  slug: formcarry-com-get-v1-forms-formid-images-response
- name: GetV1FormsFormidSelfEmailNotificationRecipientsEmailResponse
  property_count: 1
  slug: formcarry-com-get-v1-forms-formid-self-email-notification-recipients-email-response
- name: GetV1FormsFormidSelfEmailNotificationRecipientsResponse
  property_count: 1
  slug: formcarry-com-get-v1-forms-formid-self-email-notification-recipients-response
- name: GetV1FormsFormidSubmissionsResponse
  property_count: 1
  slug: formcarry-com-get-v1-forms-formid-submissions-response
- name: GetV1FormsResponse
  property_count: 1
  slug: formcarry-com-get-v1-forms-response
- name: GetV1MeResponse
  property_count: 1
  slug: formcarry-com-get-v1-me-response
- name: PostV1FormsResponse
  property_count: 6
  slug: formcarry-com-post-v1-forms-response
- name: PutApiFormRequest
  property_count: 1
  slug: formcarry-com-put-api-form-request
jsonld:
- class_count: 9
  name: Formcarry Com Context
  property_count: 13
  slug: formcarry-com-context
layout: provider
modified: '2026-10-30'
name: formcarry-com
nav: Providers
network: true
overview: 'formcarry-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network: api API and api reference API. Tagged areas include Company, API, Forms, Backend-as-a-Service, and Webhooks.


  The formcarry-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  formcarry-com''s developer surface includes authentication, signup flow, pricing, documentation, engineering blog, API reference, getting-started guide, and 17 more developer resources.'
plans:
- name: Formcarry Com Plans Pricing
  plan_count: 4
  slug: formcarry-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: formcarry-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: formcarry-com-rules
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 63.3
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 28.9
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
  name: Formcarry Com Authentication
  slug: formcarry-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Formcarry Com Domain Security
  slug: formcarry-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: formcarry-com
tags:
- Company
- API
- Forms
- Backend-as-a-Service
- Webhooks
website: https://formcarry.com/
---
