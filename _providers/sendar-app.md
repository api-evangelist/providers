---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
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
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Sendar App Agentic Access
  operation_count: 19
  slug: sendar-app-agentic-access
  summary_line: 19 operations · 8 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://sendar.app/api
  baseurl_source: declared
  description: The emails API from sendar-app — 4 operation(s) for emails.
  name: sendar-app Emails API
  slug: sendar-app-emails-api
- baseURL: https://sendar.app/api
  baseurl_source: declared
  description: The Headless API from sendar-app — 1 operation(s) for headless.
  name: sendar-app Headless API
  slug: sendar-app-headless-api
- baseURL: https://sendar.app/api
  baseurl_source: declared
  description: The Inboxes API from sendar-app — 8 operation(s) for inboxes.
  name: sendar-app Inboxes API
  slug: sendar-app-inboxes-api
- baseURL: https://sendar.app/api
  baseurl_source: declared
  description: The Link Checks API from sendar-app — 3 operation(s) for link checks.
  name: sendar-app Link Checks API
  slug: sendar-app-link-checks-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/sendar-app/agentic-access/sendar-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendar-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sendar-app/plans/sendar-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendar-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/rules/sendar-app-rules.yml
  title: ''
  type: Spectral
  url: rules/sendar-app-rules.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/json-ld/sendar-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sendar-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/sendar-app/vocabulary/sendar-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendar-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sendar-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/data-model/sendar-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendar-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/conventions/sendar-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sendar-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/conventions/sendar-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendar-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/errors/sendar-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendar-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sendar-app/conformance/sendar-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendar-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sendar-app/llms/sendar-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendar-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/sendar-app/well-known/sendar-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sendar-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/sendar-app/hosts/sendar-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendar-app-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://sendar.app/sign-up
- group: auth
  href: https://artifacts.apis.io/sendar-app/authentication/sendar-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendar-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sendar-app/security/sendar-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendar-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendar.app/
- group: docs
  title: ''
  type: Documentation
  url: https://sendar.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sendar.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://sendar.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://sendar.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendar.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendar.app/privacy
- group: company
  title: ''
  type: Blog
  url: https://sendar.app/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://sendar.app/openapi.json
  - status: 401
    url: https://sendar.app/api/mcp
  - status: 200
    url: https://sendar.app/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Sendar App provides a platform for managing and automating delivery logistics, offering APIs that enable businesses to integrate shipment tracking, route optimization, and real-time notifications into their applications. The service focuses on scalability, security, and ease of use, supporting multiple transport providers and providing comprehensive documentation for developers. By leveraging modern cloud infrastructure, Sendar App ensures high availability and performance for enterprise and SMB customers alike.
json_schemas:
- name: BatchEmailItem
  property_count: 9
  slug: sendar-app-batch-email-item
- name: BatchSendResponse
  property_count: 1
  slug: sendar-app-batch-send-response
- name: EmailDetail
  property_count: 18
  slug: sendar-app-email-detail
- name: EmailEvent
  property_count: 4
  slug: sendar-app-email-event
- name: EmailInput
  property_count: 11
  slug: sendar-app-email-input
- name: EmailLog
  property_count: 16
  slug: sendar-app-email-log
jsonld:
- class_count: 6
  name: Sendar App Context
  property_count: 30
  slug: sendar-app-context
layout: provider
modified: '2026-10-31'
name: sendar-app
nav: Providers
network: true
overview: 'sendar-app publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Emails API, Headless API, Inboxes API, and 1 more. Tagged areas include Company, Logistics, Delivery, and Automation.


  The sendar-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sendar-app''s developer surface includes signup flow, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Sendar App Plans Pricing
  plan_count: 5
  slug: sendar-app-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: sendar-app API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: sendar-app-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 29.2
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 50.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sendar-app/sendar-app-2026-11-03T143022.png
security:
- kind: authentication
  name: Sendar App Authentication
  slug: sendar-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendar App Domain Security
  slug: sendar-app-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: sendar-app-send-email-with-status
  slug: sendar-app-send-email-with-status
slug: sendar-app
tags:
- Company
- Logistics
- Delivery
- Automation
website: https://sendar.app/
---
