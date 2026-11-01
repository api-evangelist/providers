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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: WhatsApp Business API gateway allowing sending and receiving messages, media, and interactive content.
  name: WhatsApp Business API
  slug: whatsapp-business-api
- baseURL: https://api.green-api.com
  baseurl_source: declared
  description: 'green-api-com API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: green-api-com API
  slug: green-api-com-api
artifact_total: 12
asyncapis:
- description: ''
  name: Green Api Com Webhooks
  slug: green-api-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/green-api-com/rules/green-api-com-rules.yml
  title: ''
  type: Spectral
  url: rules/green-api-com-rules.yml
- group: design
  href: https://artifacts.apis.io/green-api-com/json-ld/green-api-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/green-api-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/green-api-com/vocabulary/green-api-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/green-api-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/green-api-com/asyncapi/green-api-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/green-api-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/green-api-com/data-model/green-api-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/green-api-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/green-api-com/conformance/green-api-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/green-api-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/green-api-com/llms/green-api-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/green-api-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/green-api-com/well-known/green-api-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/green-api-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/green-api-com/well-known/green-api-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/green-api-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/green-api-com/hosts/green-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/green-api-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://green-api.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://green-api.com/articles/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.greenapi.com/waInstance&
- group: auth
  href: https://artifacts.apis.io/green-api-com/security/green-api-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/green-api-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://green-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://green-api.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://green-api.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://green-api.com/docs/before-start/
- group: operate
  title: ''
  type: Support
  url: https://green-api.com/docs/faq/
- group: company
  title: ''
  type: Blog
  url: https://green-api.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.green-api.com/
coverage:
  checked: '2026-10-30'
  detail: API documentation pages return HTML shells and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://green-api.com/docs/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: GREEN-API provides a robust WhatsApp Business API gateway, enabling developers to send and receive messages, media, and interactive content at scale. The platform offers SDKs for multiple languages, integration with Telegram, MAX, GPT, and marketing tools, along with comprehensive documentation, pricing details, and a status page. It targets businesses seeking reliable messaging automation and customer engagement solutions.
image: https://green-api.com/og_image_ru.png
json_schemas:
- name: GetWainstanceIdinstanceGetsettingsApitokeninstanceResponse
  property_count: 27
  slug: green-api-com-get-wainstance-idinstance-getsettings-apitokeninstance-response
- name: GetWainstanceIdinstanceGetwasettingsApitokeninstanceResponse
  property_count: 9
  slug: green-api-com-get-wainstance-idinstance-getwasettings-apitokeninstance-response
- name: PostWainstanceIdinstanceSendfilebyurlApitokeninstanceRequest
  property_count: 7
  slug: green-api-com-post-wainstance-idinstance-sendfilebyurl-apitokeninstance-request
- name: PostWainstanceIdinstanceSendmessageApitokeninstanceRequest
  property_count: 7
  slug: green-api-com-post-wainstance-idinstance-sendmessage-apitokeninstance-request
- name: PostWainstanceIdinstanceSendpollApitokeninstanceRequest
  property_count: 6
  slug: green-api-com-post-wainstance-idinstance-sendpoll-apitokeninstance-request
- name: PostWainstanceIdinstanceSetsettingsApitokeninstanceRequest
  property_count: 26
  slug: green-api-com-post-wainstance-idinstance-setsettings-apitokeninstance-request
jsonld:
- class_count: 26
  name: Green Api Com Context
  property_count: 64
  slug: green-api-com-context
layout: provider
modified: '2026-10-30'
name: green-api-com
nav: Providers
network: true
overview: 'green-api-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, WhatsApp, API, and Integration.


  The green-api-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  green-api-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: green-api-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: green-api-com-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 72.7
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 79.1
    contract_quality: 55.0
    developer_ergonomics: 45.2
    discoverability: 58.9
    operational_transparency: 34.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Green Api Com Domain Security
  slug: green-api-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: green-api-com
tags:
- Company
- Messaging
- WhatsApp
- API
- Integration
website: https://green-api.com/
---
