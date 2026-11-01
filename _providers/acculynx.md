---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Acculynx Agentic Access
  operation_count: 127
  slug: acculynx-agentic-access
  summary_line: 127 operations · 38 acting
api_count: 2
apis:
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: The accuLynxCommon API from AccuLynx — 5 operation(s) for acculynxcommon.
  name: AccuLynx Accu Lynx Common API
  slug: acculynx-acculynxcommon-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage company calendars and their appointments.
  name: AccuLynx Calendar API
  slug: acculynx-calendar-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage company-level configuration, including job file settings, lead sources, workflow milestones, account types, and payment methods.
  name: AccuLynx Company API
  slug: acculynx-company-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage contacts and their associated phone numbers, email addresses, notes, logs, and job relationships.
  name: AccuLynx Contacts API
  slug: acculynx-contacts-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Verify API availability and connectivity.
  name: AccuLynx Diagnostics API
  slug: acculynx-diagnostics-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage estimates and their sections and line items.
  name: AccuLynx Estimates API
  slug: acculynx-estimates-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage financial records, worksheets, worksheet items, and amendments for a job.
  name: AccuLynx Financials API
  slug: acculynx-financials-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage invoice records.
  name: AccuLynx Invoices API
  slug: acculynx-invoices-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage jobs and their associated data, including address, contacts, custom fields, financials, history, insurance, measurements, messages, milestones, payments, and representatives.
  name: AccuLynx Jobs API
  slug: acculynx-jobs-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage lead records and their history.
  name: AccuLynx Leads API
  slug: acculynx-leads-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage scheduled report instances and their recipients.
  name: AccuLynx Reports API
  slug: acculynx-reports-api
- baseURL: https://api.acculynx.com/webhooks/v2
  baseurl_source: declared
  description: Subscription related endpoints
  name: AccuLynx Subscriptions API
  slug: acculynx-subscriptions-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage insurance supplement claims and their associated items and notations.
  name: AccuLynx Supplements API
  slug: acculynx-supplements-api
- baseURL: https://api.acculynx.com/webhooks/v2
  baseurl_source: declared
  description: Topics related endpoints
  name: AccuLynx Topics API
  slug: acculynx-topics-api
- baseURL: https://api.acculynx.com/api/v2
  baseurl_source: declared
  description: Manage user accounts within the company.
  name: AccuLynx Users API
  slug: acculynx-users-api
- baseURL: https://api.acculynx.com/webhooks/v2
  baseurl_source: declared
  description: The Webhooks API API from AccuLynx — 0 operation(s) for webhooks api.
  name: AccuLynx Webhooks API
  slug: acculynx-webhooks-api-api
artifact_total: 38
asyncapis:
- description: ''
  name: Acculynx Webhooks
  slug: acculynx-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/acculynx/agentic-access/acculynx-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acculynx-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/acculynx/rate-limits/acculynx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acculynx-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/acculynx/rules/acculynx-rules.yml
  title: ''
  type: Spectral
  url: rules/acculynx-rules.yml
- group: design
  href: https://artifacts.apis.io/acculynx/json-ld/acculynx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/acculynx-context.jsonld
- group: design
  href: https://artifacts.apis.io/acculynx/vocabulary/acculynx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acculynx-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/acculynx/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/acculynx/asyncapi/acculynx-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/acculynx-webhooks.yml
- group: design
  href: https://artifacts.apis.io/acculynx/data-model/acculynx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acculynx-data-model.yml
- group: design
  href: https://artifacts.apis.io/acculynx/errors/acculynx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acculynx-problem-types.yml
- group: design
  href: https://artifacts.apis.io/acculynx/conformance/acculynx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acculynx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/acculynx/llms/acculynx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acculynx-llms.txt
- group: auth
  href: https://artifacts.apis.io/acculynx/well-known/acculynx-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acculynx-status-security.txt
- group: agent
  href: https://artifacts.apis.io/acculynx/well-known/acculynx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acculynx-well-known.yml
- group: other
  href: https://artifacts.apis.io/acculynx/hosts/acculynx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acculynx-hosts.yml
- group: other
  href: https://artifacts.apis.io/acculynx/vendors/acculynx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acculynx-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.acculynx.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acculynx.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.acculynx.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.acculynx.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.acculynx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AccuLynx
- group: auth
  href: https://artifacts.apis.io/acculynx/authentication/acculynx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acculynx-authentication.yml
- group: auth
  href: https://artifacts.apis.io/acculynx/security/acculynx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acculynx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acculynx.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://acculynx.com/demonstration-request/
- group: commercial
  title: ''
  type: Pricing
  url: https://acculynx.com/pricing-request/
- group: company
  title: ''
  type: Blog
  url: https://acculynx.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://acculynx.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acculynx.com/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: The provider’s website offers only HTML pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://acculynx.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: AccuLynx provides a cloud‑based roofing CRM and business management platform that helps roofing contractors manage sales pipelines, production, finance, crew coordination, and customer relationships. The SaaS solution includes mobile field apps, integrated payment processing, document automation, and extensive reporting, targeting the construction and roofing industry.
image: https://acculynx.com/wp-content/uploads/2020/06/AcculynxLogoStack-RGB-1.png
json_schemas:
- name: calendarEvent
  property_count: 11
  slug: acculynx-calendar-event
- name: estimateItem
  property_count: 19
  slug: acculynx-estimate-item
- name: invoice
  property_count: 0
  slug: acculynx-invoice
- name: jobContact
  property_count: 0
  slug: acculynx-job-contact
- name: jobMeasurementsPostFiles
  property_count: 11
  slug: acculynx-job-measurements-post-files
- name: job
  property_count: 0
  slug: acculynx-job
- name: subscriptionBodyPost
  property_count: 4
  slug: acculynx-subscription-body-post
- name: subscriptionBodyPut
  property_count: 2
  slug: acculynx-subscription-body-put
- name: subscriptionCollection
  property_count: 0
  slug: acculynx-subscription-collection
- name: subscription
  property_count: 0
  slug: acculynx-subscription
- name: testEventBodyPost
  property_count: 1
  slug: acculynx-test-event-body-post
- name: topicCollection
  property_count: 0
  slug: acculynx-topic-collection
jsonld:
- class_count: 120
  name: Acculynx Context
  property_count: 184
  slug: acculynx-context
layout: provider
modified: '2026-10-28'
name: AccuLynx
nav: Providers
network: true
overview: 'AccuLynx publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accu Lynx Common API, Calendar API, Company API, and 13 more. Tagged areas include Company, Roofing, CRM, SaaS, and Construction.


  The AccuLynx catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AccuLynx''s developer surface includes changelog, API reference, documentation, authentication, getting-started guide, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Acculynx Plans Pricing
  plan_count: 0
  slug: acculynx-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Acculynx Rate Limits
  slug: acculynx-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: AccuLynx API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: acculynx-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 69.6
    developer_ergonomics: 49.4
    discoverability: 57.1
    operational_transparency: 86.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acculynx Authentication
  slug: acculynx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acculynx Domain Security
  slug: acculynx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: acculynx-create-contact-with-communication
  slug: acculynx-create-contact-with-communication
- name: acculynx-financials-create-worksheet-item
  slug: acculynx-financials-create-worksheet-item
slug: acculynx
tags:
- Company
- Roofing
- CRM
- SaaS
- Construction
website: https://acculynx.com/
---
