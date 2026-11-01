---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Mailjunky Ai Agentic Access
  operation_count: 13
  slug: mailjunky-ai-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://www.mailjunky.ai/api/v1
  baseurl_source: declared
  description: Email and event statistics
  name: mailjunky-ai Analytics API
  slug: mailjunky-ai-analytics-api
- baseURL: https://www.mailjunky.ai/api/v1
  baseurl_source: declared
  description: API key validation
  name: mailjunky-ai Auth API
  slug: mailjunky-ai-auth-api
- baseURL: https://www.mailjunky.ai/api/v1
  baseurl_source: declared
  description: Manage your contact lists and subscriber data
  name: mailjunky-ai Contacts API
  slug: mailjunky-ai-contacts-api
- baseURL: https://www.mailjunky.ai/api/v1
  baseurl_source: declared
  description: Send transactional emails via API
  name: mailjunky-ai Emails API
  slug: mailjunky-ai-emails-api
- baseURL: https://www.mailjunky.ai/api/v1
  baseurl_source: declared
  description: Track user behavior and custom events
  name: mailjunky-ai Events API
  slug: mailjunky-ai-events-api
- baseURL: https://www.mailjunky.ai/api/v1
  baseurl_source: declared
  description: Service health checks
  name: mailjunky-ai Health API
  slug: mailjunky-ai-health-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/mailjunky-ai/agentic-access/mailjunky-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailjunky-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mailjunky-ai/plans/mailjunky-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailjunky-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mailjunky-ai/rules/mailjunky-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/mailjunky-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/mailjunky-ai/json-ld/mailjunky-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailjunky-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailjunky-ai/vocabulary/mailjunky-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailjunky-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mailjunky-ai/data-model/mailjunky-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailjunky-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mailjunky-ai/authentication/mailjunky-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailjunky-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/mailjunky-ai/errors/mailjunky-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailjunky-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mailjunky-ai/conformance/mailjunky-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailjunky-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/mailjunky-ai/hosts/mailjunky-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailjunky-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/mailjunky-ai/vendors/mailjunky-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailjunky-ai-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@mailjunky/sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://mailjunky.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://mailjunky.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://mailjunky.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://mailjunky.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://mailjunky.ai/api-reference
- group: auth
  href: https://artifacts.apis.io/mailjunky-ai/security/mailjunky-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailjunky-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailjunky.ai/
created: '2026-10-30'
description: MailJunky AI provides AI‑enhanced email marketing automation, offering advanced segmentation, predictive content generation, and real‑time analytics to help businesses optimize campaign performance. Their platform integrates with major CRMs and supports multi‑channel outreach, aiming to increase engagement and conversion rates through machine‑learning driven insights and personalization.
json_schemas:
- name: BatchEmailRequest
  property_count: 1
  slug: mailjunky-ai-batch-email-request
- name: ContactBasic
  property_count: 9
  slug: mailjunky-ai-contact-basic
- name: Contact
  property_count: 16
  slug: mailjunky-ai-contact
- name: CreateContactRequest
  property_count: 6
  slug: mailjunky-ai-create-contact-request
- name: SendEmailRequest
  property_count: 11
  slug: mailjunky-ai-send-email-request
- name: TrackEventRequest
  property_count: 6
  slug: mailjunky-ai-track-event-request
jsonld:
- class_count: 10
  name: Mailjunky Ai Context
  property_count: 41
  slug: mailjunky-ai-context
layout: provider
modified: '2026-10-30'
name: mailjunky-ai
nav: Providers
network: true
overview: 'mailjunky-ai publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Contacts API, and 3 more. Tagged areas include Company, Email Marketing, AI, Automation, and Analytics.


  The mailjunky-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mailjunky-ai''s developer surface includes authentication, pricing, documentation, engineering blog, API reference, and 14 more developer resources.'
plans:
- name: Mailjunky Ai Plans Pricing
  plan_count: 5
  slug: mailjunky-ai-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: mailjunky-ai API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: mailjunky-ai-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 67.2
    developer_ergonomics: 38.1
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mailjunky Ai Authentication
  slug: mailjunky-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mailjunky Ai Domain Security
  slug: mailjunky-ai-domain-security
  summary_line: TLSv1.3
slug: mailjunky-ai
tags:
- Company
- Email Marketing
- AI
- Automation
- Analytics
website: https://mailjunky.ai/
---
