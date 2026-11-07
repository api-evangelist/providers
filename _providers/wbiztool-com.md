---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Wbiztool Com Agentic Access
  operation_count: 26
  slug: wbiztool-com-agentic-access
  summary_line: 26 operations · 12 acting
api_count: 1
apis:
- description: Send WhatsApp messages via REST API
  name: WbizTool API
  slug: wbiztool-api
- baseURL: https://wbiztool.com/api/v1
  baseurl_source: declared
  description: Credential and health checks.
  name: wbiztool-com Account API
  slug: wbiztool-com-account-api
- baseURL: https://wbiztool.com/api/v1
  baseurl_source: declared
  description: Host files in the workspace Media directory and reuse their URLs.
  name: wbiztool-com Media API
  slug: wbiztool-com-media-api
- baseURL: https://wbiztool.com/api/v1
  baseurl_source: declared
  description: Send, schedule, cancel and track WhatsApp messages.
  name: wbiztool-com Messages API
  slug: wbiztool-com-messages-api
- baseURL: https://wbiztool.com/api/v1
  baseurl_source: declared
  description: Check whether numbers are on WhatsApp. Uses a Bearer header.
  name: wbiztool-com Number verification API
  slug: wbiztool-com-number-verification-api
- baseURL: https://wbiztool.com/api/v1
  baseurl_source: declared
  description: Recurring messages on a cron schedule.
  name: wbiztool-com Reminders API
  slug: wbiztool-com-reminders-api
- baseURL: https://wbiztool.com/api/v1
  baseurl_source: declared
  description: Connect numbers and check which are connected.
  name: wbiztool-com WhatsApp numbers API
  slug: wbiztool-com-whatsapp-numbers-api
artifact_total: 17
asyncapis:
- description: ''
  name: Wbiztool Com Webhooks
  slug: wbiztool-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/wbiztool-com/agentic-access/wbiztool-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wbiztool-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/wbiztool-com/plans/wbiztool-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wbiztool-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wbiztool-com/rules/wbiztool-com-rules.yml
  title: ''
  type: Spectral
  url: rules/wbiztool-com-rules.yml
- group: design
  href: https://artifacts.apis.io/wbiztool-com/json-ld/wbiztool-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wbiztool-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/wbiztool-com/vocabulary/wbiztool-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wbiztool-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/wbiztool-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/wbiztool-com/asyncapi/wbiztool-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wbiztool-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/wbiztool-com/data-model/wbiztool-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wbiztool-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/wbiztool-com/authentication/wbiztool-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wbiztool-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/wbiztool-com/errors/wbiztool-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wbiztool-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wbiztool-com/conformance/wbiztool-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wbiztool-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wbiztool-com/llms/wbiztool-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wbiztool-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/wbiztool-com/well-known/wbiztool-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wbiztool-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wbiztool-com/hosts/wbiztool-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wbiztool-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wbiztool-com/vendors/wbiztool-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wbiztool-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/wbiztool-com/packages/wbiztool-com-packages.yml
  title: ''
  type: SDKs
  url: packages/wbiztool-com-packages.yml
- group: build
  href: https://artifacts.apis.io/wbiztool-com/packages/wbiztool-com-packages.yml
  title: ''
  type: Packages
  url: packages/wbiztool-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://wbiztool.com/login/
- group: company
  title: ''
  type: Blog
  url: https://blog.wbiztool.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wbiztool
- group: auth
  href: https://artifacts.apis.io/wbiztool-com/security/wbiztool-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wbiztool-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wbiztool.com/
- group: docs
  title: ''
  type: Documentation
  url: https://wbiztool.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://wbiztool.com/docs/api/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://wbiztool.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://wbiztool.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wbiztool.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wbiztool.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://wbiztool.com/contact-us/
created: '2026-10-31'
description: WbizTool provides a WhatsApp API that lets businesses send messages from their own phone numbers. It offers a simple REST interface, spreadsheet integration, and various tool integrations to automate order updates, payment reminders, and marketing campaigns. Users can start for free with 50 messages, no credit card required, and scale with flexible pricing plans. The platform supports text, images, files, audio, and video, catering to both personal and business numbers.
image: https://wbiztool.com/og/home.png
jsonld:
- class_count: 27
  name: Wbiztool Com Context
  property_count: 58
  slug: wbiztool-com-context
layout: provider
modified: '2026-10-31'
name: wbiztool-com
nav: Providers
network: true
overview: 'wbiztool-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Media API, Messages API, and 4 more. Tagged areas include Company, WhatsApp, Messaging, Automation, and Business.


  The wbiztool-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  wbiztool-com''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
plans:
- name: Wbiztool Com Plans Pricing
  plan_count: 4
  slug: wbiztool-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: wbiztool-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: wbiztool-com-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 67.1
    developer_ergonomics: 36.3
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
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
security:
- kind: authentication
  name: Wbiztool Com Authentication
  slug: wbiztool-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wbiztool Com Domain Security
  slug: wbiztool-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: wbiztool-com-connect-whatsapp-number
  slug: wbiztool-com-connect-whatsapp-number
- name: wbiztool-com-number-verification
  slug: wbiztool-com-number-verification
- name: wbiztool-com-reminder-workflow
  slug: wbiztool-com-reminder-workflow
slug: wbiztool-com
tags:
- Company
- WhatsApp
- Messaging
- Automation
- Business
website: https://wbiztool.com/
---
