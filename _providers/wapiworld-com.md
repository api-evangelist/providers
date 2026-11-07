---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Wapiworld Com Agentic Access
  operation_count: 14
  slug: wapiworld-com-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.wapiworld.com
  baseurl_source: declared
  description: The Instances API from wapiworld-com — 4 operation(s) for instances.
  name: wapiworld-com Instances API
  slug: wapiworld-com-instances-api
- baseURL: https://api.wapiworld.com
  baseurl_source: declared
  description: The Messages API from wapiworld-com — 1 operation(s) for messages.
  name: wapiworld-com Messages API
  slug: wapiworld-com-messages-api
- baseURL: https://api.wapiworld.com
  baseurl_source: declared
  description: The Projects API from wapiworld-com — 2 operation(s) for projects.
  name: wapiworld-com Projects API
  slug: wapiworld-com-projects-api
- baseURL: https://api.wapiworld.com
  baseurl_source: declared
  description: The Webhook subscriptions API from wapiworld-com — 2 operation(s) for webhook subscriptions.
  name: wapiworld-com Webhook subscriptions API
  slug: wapiworld-com-webhook-subscriptions-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/wapiworld-com/agentic-access/wapiworld-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wapiworld-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/rules/wapiworld-com-rules.yml
  title: ''
  type: Spectral
  url: rules/wapiworld-com-rules.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/json-ld/wapiworld-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wapiworld-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/wapiworld-com/vocabulary/wapiworld-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wapiworld-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/data-model/wapiworld-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wapiworld-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/conventions/wapiworld-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wapiworld-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/conventions/wapiworld-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wapiworld-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/errors/wapiworld-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wapiworld-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wapiworld-com/conformance/wapiworld-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wapiworld-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wapiworld-com/llms/wapiworld-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wapiworld-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/wapiworld-com/well-known/wapiworld-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wapiworld-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wapiworld-com/hosts/wapiworld-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wapiworld-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wapiworld-com/vendors/wapiworld-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wapiworld-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.wapiworld.com/login
- group: auth
  href: https://artifacts.apis.io/wapiworld-com/authentication/wapiworld-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wapiworld-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wapiworld-com/security/wapiworld-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wapiworld-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wapiworld.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wapiworld.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wapiworld.com/docs/en/
- group: docs
  title: ''
  type: APIReference
  url: https://www.wapiworld.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wapiworld.com/docs/en/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.wapiworld.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.wapiworld.com/blog/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wapiworld
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wapiworld.com/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wapiworld.com/en/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wapiworld.com/en/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/wapiworld/workspace
created: '2026-10-31'
description: Wapiworld provides a WhatsApp API platform for developers, enabling project‑scoped integrations to send and receive messages through a REST API, CLI, or OAuth‑protected MCP. The service includes webhook event handling, explicit message confirmation, and safety boundaries that protect API keys, token data, and message content. Documentation covers REST endpoints, authentication, pricing, and developer guides, while the public npm package and open source CLI facilitate easy integration. Wapiworld emphasizes data safety, compliance, and reliable messaging workflows for businesses and developers.
image: https://www.imagelato.com/images/favicon-cron-10ee1248.svg
json_schemas:
- name: IdempotentSendResult
  property_count: 2
  slug: wapiworld-com-idempotent-send-result
- name: InstanceActionResult
  property_count: 0
  slug: wapiworld-com-instance-action-result
- name: Instance
  property_count: 6
  slug: wapiworld-com-instance
- name: Project
  property_count: 5
  slug: wapiworld-com-project
- name: RecordedMessage
  property_count: 7
  slug: wapiworld-com-recorded-message
- name: WebhookSubscription
  property_count: 8
  slug: wapiworld-com-webhook-subscription
jsonld:
- class_count: 7
  name: Wapiworld Com Context
  property_count: 20
  slug: wapiworld-com-context
layout: provider
modified: '2026-10-31'
name: wapiworld-com
nav: Providers
network: true
overview: 'wapiworld-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Instances API, Messages API, Projects API, and 1 more. Tagged areas include Messaging, WhatsApp, Developer Platform, and Communications.


  The wapiworld-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  wapiworld-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: wapiworld-com API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: wapiworld-com-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 60.0
    developer_ergonomics: 36.9
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
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
  name: Wapiworld Com Authentication
  slug: wapiworld-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wapiworld Com Domain Security
  slug: wapiworld-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wapiworld-com
tags:
- Messaging
- WhatsApp
- Developer Platform
- Communications
website: https://www.wapiworld.com/
---
