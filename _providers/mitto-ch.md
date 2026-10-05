---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-04'
api_count: 6
apis:
- baseURL: https://messaging.mittoapi.com
  baseurl_source: declared
  description: The Apis API from Mitto — 1 operation(s) for apis.
  name: Mitto APIs API
  slug: mitto-ch-apis-api
- baseURL: https://messaging.mittoapi.com
  baseurl_source: declared
  description: The AutoReplyConfigs API from Mitto — 1 operation(s) for autoreplyconfigs.
  name: Mitto Auto Reply Configs API
  slug: mitto-ch-autoreplyconfigs-api
- baseURL: https://messaging.mittoapi.com
  baseurl_source: declared
  description: The Customers API from Mitto — 2 operation(s) for customers.
  name: Mitto Customers API
  slug: mitto-ch-customers-api
- baseURL: https://messaging.mittoapi.com
  baseurl_source: declared
  description: The Mitto API API from Mitto — 4 operation(s) for mitto api.
  name: Mitto Mitto API
  slug: mitto-ch-mitto-api-api
- baseURL: https://messaging.mittoapi.com
  baseurl_source: declared
  description: The Statistic API from Mitto — 2 operation(s) for statistic.
  name: Mitto Statistic API
  slug: mitto-ch-statistic-api
- baseURL: https://messaging.mittoapi.com
  baseurl_source: declared
  description: The Webhooks API from Mitto — 2 operation(s) for webhooks.
  name: Mitto Webhooks API
  slug: mitto-ch-webhooks-api
artifact_total: 16
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.mitto.ch/getting-started/quickstart
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/rules/mitto-ch-rules.yml
  title: ''
  type: Spectral
  url: rules/mitto-ch-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/json-ld/mitto-ch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mitto-ch-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/vocabulary/mitto-ch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mitto-ch-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/data-model/mitto-ch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mitto-ch-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/authentication/mitto-ch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mitto-ch-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/conformance/mitto-ch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mitto-ch-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/llms/mitto-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mitto-ch-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/well-known/mitto-ch-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mitto-ch-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/well-known/mitto-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mitto-ch-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/hosts/mitto-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mitto-ch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/vendors/mitto-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mitto-ch-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mitto.ch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mitto.ch/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mitto.ch/signup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitto-ch/refs/heads/main/security/mitto-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mitto-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mitto.ch
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.mitto.ch
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.mitto.ch/api-reference.md
- group: commercial
  title: ''
  type: Pricing
  url: https://mitto.ch/pricing/
- group: company
  title: ''
  type: Blog
  url: https://mitto.ch/blog/
- group: operate
  title: ''
  type: Support
  url: https://mitto.ch/contact/
coverage:
  checked: '2026-10-03'
  detail: Documentation is served via GitBook with no machine‑readable OpenAPI or other contract found.
  evidence:
  - status: 200
    url: https://documentation.mitto.ch
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Mitto provides omnichannel messaging solutions, enabling businesses to engage customers across SMS, RCS, voice, Telegram, Viber, WhatsApp, Facebook Messenger, and Instagram. Their platform offers products for campaigns, conversations, number lookup, verification, and integrates with HubSpot, Salesforce, Zoho, and Oracle Responsys. Mitto aims to streamline communication, improve customer experiences, and support omnichannel strategies for enterprises worldwide.
image: https://mitto.ch/wp-content/uploads/2025/06/adobe-1.svg
json_schemas:
- name: GetApiV1V1IdIdResponse
  property_count: 14
  slug: mitto-ch-get-api-v1-v1-id-id-response
- name: PostApiV1CustomersCustomeridRequest
  property_count: 2
  slug: mitto-ch-post-api-v1-customers-customerid-request
- name: PostApiV1WebhooksRequest
  property_count: 5
  slug: mitto-ch-post-api-v1-webhooks-request
- name: PostApiV11CustomersCustomeridRequest
  property_count: 2
  slug: mitto-ch-post-api-v11-customers-customerid-request
- name: PostApiV11V11IdResponse
  property_count: 3
  slug: mitto-ch-post-api-v11-v11-id-response
- name: PutApiV1WebhooksIdRequest
  property_count: 5
  slug: mitto-ch-put-api-v1-webhooks-id-request
jsonld:
- class_count: 20
  name: Mitto Ch Context
  property_count: 21
  slug: mitto-ch-context
layout: provider
modified: '2026-10-03'
name: Mitto
nav: Providers
network: true
overview: 'Mitto publishes 6 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Auto Reply Configs API, Customers API, and 3 more. Tagged areas include Messaging, Omnichannel, Communications, and Enterprise.


  The Mitto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mitto''s developer surface includes getting-started guide, authentication, signup flow, documentation, API reference, pricing, engineering blog, and 15 more developer resources.'
random_paper: 13
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Mitto API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mitto-ch-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 25.9
    developer_ergonomics: 47.6
    discoverability: 69.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Mitto Ch Authentication
  slug: mitto-ch-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mitto Ch Domain Security
  slug: mitto-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitto-ch
tags:
- Messaging
- Omnichannel
- Communications
- Enterprise
website: https://www.mitto.ch
---
