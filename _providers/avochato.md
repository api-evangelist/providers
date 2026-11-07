---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://ww
  baseurl_source: declared
  description: The Avochato API API from Avochato — 3 operation(s) for avochato api.
  name: Avochato Avochato API
  slug: avochato-avochato-api-api
- baseURL: https://ww
  baseurl_source: declared
  description: The Broadcasts API from Avochato — 3 operation(s) for broadcasts.
  name: Avochato Broadcasts API
  slug: avochato-broadcasts-api
- baseURL: https://ww
  baseurl_source: declared
  description: The Campaigns API from Avochato — 2 operation(s) for campaigns.
  name: Avochato Campaigns API
  slug: avochato-campaigns-api
- baseURL: https://ww
  baseurl_source: declared
  description: The Contacts API from Avochato — 4 operation(s) for contacts.
  name: Avochato Contacts API
  slug: avochato-contacts-api
- baseURL: https://ww
  baseurl_source: declared
  description: The Links API from Avochato — 1 operation(s) for links.
  name: Avochato Links API
  slug: avochato-links-api
- baseURL: https://ww
  baseurl_source: declared
  description: The Messages API from Avochato — 2 operation(s) for messages.
  name: Avochato Messages API
  slug: avochato-messages-api
- baseURL: https://ww
  baseurl_source: declared
  description: The Tickets API from Avochato — 2 operation(s) for tickets.
  name: Avochato Tickets API
  slug: avochato-tickets-api
artifact_total: 20
asyncapis:
- description: ''
  name: Avochato Webhooks
  slug: avochato-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/avochato/plans/avochato-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avochato-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avochato/rules/avochato-rules.yml
  title: ''
  type: Spectral
  url: rules/avochato-rules.yml
- group: design
  href: https://artifacts.apis.io/avochato/json-ld/avochato-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avochato-context.jsonld
- group: design
  href: https://artifacts.apis.io/avochato/vocabulary/avochato-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avochato-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avochato/asyncapi/avochato-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/avochato-webhooks.yml
- group: design
  href: https://artifacts.apis.io/avochato/data-model/avochato-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avochato-data-model.yml
- group: design
  href: https://artifacts.apis.io/avochato/conformance/avochato-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avochato-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avochato/llms/avochato-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avochato-llms.txt
- group: auth
  href: https://artifacts.apis.io/avochato/well-known/avochato-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avochato-status-security.txt
- group: agent
  href: https://artifacts.apis.io/avochato/well-known/avochato-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avochato-well-known.yml
- group: other
  href: https://artifacts.apis.io/avochato/hosts/avochato-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avochato-hosts.yml
- group: other
  href: https://artifacts.apis.io/avochato/vendors/avochato-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avochato-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.avochato.com/integrations/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avochato.com/
- group: start
  title: ''
  type: Login
  url: https://www.avochato.com/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://help.avochato.com/using-avochato/1c4ChajMJ1RX2ELRWZWrih/how-to-setup-avoai/uA2BDgaLjHZGdMsPpgbQG1
- group: auth
  href: https://artifacts.apis.io/avochato/security/avochato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avochato-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avochato.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.avochato.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.avochato.com/apis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avochato.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.avochato.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.avochato.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avochato.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avochato.com/privacy
coverage:
  checked: '2026-09-27'
  detail: API reference page returns HTML without a machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.avochato.com/apis
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Avochato provides the easiest business text messaging software, offering SMS, RCS, voice calls, and live chat solutions. Their platform includes automation features, AI agents, shared inbox, broadcasting, analytics, and integrations, targeting sales, support, marketing, and operations teams.
finops:
- has_sources: true
  method: derived
  name: Avochato Finops
  primary_unit: platform fee
  service_category: ''
  slug: avochato-finops
  template: false
json_schemas:
- name: DeleteV1Messages43Y83XbvnmResponse
  property_count: 1
  slug: avochato-delete-v1-messages43-y83-xbvnm-response
- name: GetV1Contacts2Jrbk681Pv2Cenl8Alj7NwResponse
  property_count: 1
  slug: avochato-get-v1-contacts2-jrbk681-pv2-cenl8-alj7-nw-response
- name: GetV1V1IdResponse
  property_count: 1
  slug: avochato-get-v1-v1-id-response
- name: PostV1BroadcastsBlp9Me9QyxPublishResponse
  property_count: 1
  slug: avochato-post-v1-broadcasts-blp9-me9-qyx-publish-response
- name: PostV1BroadcastsXdjjbrjooeResponse
  property_count: 1
  slug: avochato-post-v1-broadcasts-xdjjbrjooe-response
- name: PostV1V1IdResponse
  property_count: 1
  slug: avochato-post-v1-v1-id-response
jsonld:
- class_count: 18
  name: Avochato Context
  property_count: 24
  slug: avochato-context
layout: provider
modified: '2026-09-27'
name: Avochato
nav: Providers
network: true
overview: 'Avochato is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Avochato API, Broadcasts API, Campaigns API, and 4 more. Tagged areas include Messaging, SMS, RCS, Voice, and Business.


  The Avochato catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Avochato''s developer surface includes getting-started guide, documentation, API reference, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Avochato Plans Pricing
  plan_count: 3
  slug: avochato-plans-pricing
- name: Avochato Price Estimates
  plan_count: 0
  slug: avochato-price-estimates
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Avochato API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: avochato-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 78.8
    catalog_earned_first_party: 12.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 61.8
    contract_governance: 35.6
    contract_quality: 31.6
    developer_ergonomics: 17.9
    discoverability: 75.0
    operational_transparency: 22.4
  previous_composite: 46.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/avochato/avochato-2026-10-11T101202.png
security:
- kind: domain-security
  name: Avochato Domain Security
  slug: avochato-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: avochato
tags:
- Messaging
- SMS
- RCS
- Voice
- Business
website: https://www.avochato.com/
---
