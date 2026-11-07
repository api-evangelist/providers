---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 53
  human_in_the_loop: 2
  name: Whatsync App Agentic Access
  operation_count: 91
  slug: whatsync-app-agentic-access
  summary_line: 91 operations · 53 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Account API from whatsync-app — 2 operation(s) for account.
  name: whatsync-app Account API
  slug: whatsync-app-account-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Business and pricing API from whatsync-app — 14 operation(s) for business and pricing.
  name: whatsync-app Business and pricing API
  slug: whatsync-app-business-and-pricing-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: List approved Meta WhatsApp templates and send one from an Attio workflow with a workspace service API key.
  name: whatsync-app Business templates (Attio workflows) API
  slug: whatsync-app-business-templates-attio-workflows-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Campaigns API from whatsync-app — 10 operation(s) for campaigns.
  name: whatsync-app Campaigns API
  slug: whatsync-app-campaigns-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Forms API from whatsync-app — 6 operation(s) for forms.
  name: whatsync-app Forms API
  slug: whatsync-app-forms-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Groups API from whatsync-app — 15 operation(s) for groups.
  name: whatsync-app Groups API
  slug: whatsync-app-groups-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Reading and account API from whatsync-app — 11 operation(s) for reading and account.
  name: whatsync-app Reading and account API
  slug: whatsync-app-reading-and-account-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Saving and filters API from whatsync-app — 6 operation(s) for saving and filters.
  name: whatsync-app Saving and filters API
  slug: whatsync-app-saving-and-filters-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Sending and message actions API from whatsync-app — 16 operation(s) for sending and message actions.
  name: whatsync-app Sending and message actions API
  slug: whatsync-app-sending-and-message-actions-api
- baseURL: https://whatsync.app
  baseurl_source: declared
  description: The Webhooks API from whatsync-app — 7 operation(s) for webhooks.
  name: whatsync-app Webhooks API
  slug: whatsync-app-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/whatsync-app/agentic-access/whatsync-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whatsync-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/whatsync-app/rules/whatsync-app-rules.yml
  title: ''
  type: Spectral
  url: rules/whatsync-app-rules.yml
- group: design
  href: https://artifacts.apis.io/whatsync-app/json-ld/whatsync-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whatsync-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/whatsync-app/vocabulary/whatsync-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whatsync-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/whatsync-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whatsync-app/data-model/whatsync-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whatsync-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/whatsync-app/errors/whatsync-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whatsync-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/whatsync-app/conformance/whatsync-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whatsync-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/whatsync-app/well-known/whatsync-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whatsync-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/whatsync-app/hosts/whatsync-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whatsync-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/whatsync-app/vendors/whatsync-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whatsync-app-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://whatsync.app/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whatsync.app/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whatsync.app/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://whatsync.app/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://whatsync.app/developers
- group: auth
  href: https://artifacts.apis.io/whatsync-app/security/whatsync-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whatsync-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whatsync.app/
- group: docs
  title: ''
  type: Documentation
  url: https://whatsync.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://whatsync.app/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://whatsync.app/attio/whatsapp-link-with-qrcode
- group: operate
  title: ''
  type: Support
  url: https://whatsync.app/contact
- group: company
  title: ''
  type: Blog
  url: https://whatsync.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://whatsync.app/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://whatsync.app/openapi.json
  - status: 401
    url: https://whatsync.app/api/mcp
  - status: 200
    url: https://whatsync.app/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: WhatSync connects WhatsApp to ChatGPT, Claude, and other AI agents, using personal numbers or the WhatsApp Business API. It offers two connection methods—personal WhatsApp linked via device screen, and the official WhatsApp Business API with Meta‑approved templates. Users can filter chats, control data sharing, and the service respects privacy, not selling message contents. Built by Appstronauts, it integrates AI assistants to read, search, and draft replies, with optional voice note transcription on Pro plans.
image: https://whatsync.app/opengraph-image?84b113d7734fa0d6
json_schemas:
- name: SendTemplateRequest
  property_count: 5
  slug: whatsync-app-send-template-request
jsonld:
- class_count: 4
  name: Whatsync App Context
  property_count: 14
  slug: whatsync-app-context
layout: provider
modified: '2026-10-30'
name: whatsync-app
nav: Providers
network: true
overview: 'whatsync-app publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Business and pricing API, Business templates (Attio workflows) API, and 7 more. Tagged areas include WhatsApp, Artificial Intelligence, ChatGPT, Claude, and Integration.


  The whatsync-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  whatsync-app''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: whatsync-app API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: whatsync-app-rules
scopes:
- name: Whatsync App Scopes
  scope_count: 0
  slug: whatsync-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 61.9
    developer_ergonomics: 29.0
    discoverability: 66.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/whatsync-app/whatsync-app-2026-11-03T150149.png
security:
- kind: authentication
  name: Whatsync App Authentication
  slug: whatsync-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Whatsync App Domain Security
  slug: whatsync-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: send-message
  slug: whatsync-app-send-message
slug: whatsync-app
tags:
- WhatsApp
- Artificial Intelligence
- ChatGPT
- Claude
- Integration
- MCP
website: https://whatsync.app/
---
