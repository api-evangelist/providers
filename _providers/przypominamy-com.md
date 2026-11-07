---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Przypominamy Com Agentic Access
  operation_count: 36
  slug: przypominamy-com-agentic-access
  summary_line: 36 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Numery, na które konto nie wysyła; link opt-out
  name: przypominamy-com Czarna lista API
  slug: przypominamy-com-czarna-lista-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Książka odbiorców, grupy do wysyłki, personalizacja
  name: przypominamy-com Kontakty i grupy API
  slug: przypominamy-com-kontakty-i-grupy-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Saldo, nadpis, godziny wysyłki, webhook
  name: przypominamy-com Konto API
  slug: przypominamy-com-konto-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Śledzone linki {{link:…}} z licznikiem kliknięć
  name: przypominamy-com Linki API
  slug: przypominamy-com-linki-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: 'HLR: sprawdzenie, czy numer jest aktywny i w jakiej sieci, bez wysyłania SMS-a'
  name: przypominamy-com Numery API
  slug: przypominamy-com-numery-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: SMS-y przychodzące od odbiorców - na życzenie, po uruchomieniu numeru odbiorczego w usłudze (do tego czasu `inbound_number` jest `null`)
  name: przypominamy-com Odpowiedzi (2-way) API
  slug: przypominamy-com-odpowiedzi-2-way-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Endpointy publiczne
  name: przypominamy-com Status API
  slug: przypominamy-com-status-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Szablony SMS/MMS/głosowe z placeholderami {{klucz}} - te same co w panelu
  name: przypominamy-com Szablony API
  slug: przypominamy-com-szablony-api
- baseURL: https://api.przypominamy.com
  baseurl_source: declared
  description: Wysyłka SMS i historia wiadomości
  name: przypominamy-com Wiadomości API
  slug: przypominamy-com-wiadomo-ci-api
artifact_total: 27
asyncapis:
- description: ''
  name: Przypominamy Com Webhooks
  slug: przypominamy-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/przypominamy-com/agentic-access/przypominamy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/przypominamy-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/przypominamy-com/rate-limits/przypominamy-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/przypominamy-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/przypominamy-com/plans/przypominamy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/przypominamy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/rules/przypominamy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/przypominamy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/json-ld/przypominamy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/przypominamy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/przypominamy-com/vocabulary/przypominamy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/przypominamy-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/przypominamy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/asyncapi/przypominamy-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/przypominamy-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/data-model/przypominamy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/przypominamy-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/przypominamy-com/changelog/przypominamy-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/przypominamy-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/conventions/przypominamy-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/przypominamy-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/conventions/przypominamy-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/przypominamy-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/przypominamy-com/authentication/przypominamy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/przypominamy-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/przypominamy-com/scopes/przypominamy-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/przypominamy-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/errors/przypominamy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/przypominamy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/przypominamy-com/conformance/przypominamy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/przypominamy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/przypominamy-com/llms/przypominamy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/przypominamy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/przypominamy-com/hosts/przypominamy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/przypominamy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/przypominamy-com/vendors/przypominamy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/przypominamy-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/przypominamy-com/packages/przypominamy-com-packages.yml
  title: ''
  type: Packages
  url: packages/przypominamy-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://przypominamy.com/sdk
- group: auth
  href: https://artifacts.apis.io/przypominamy-com/security/przypominamy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/przypominamy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://przypominamy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://przypominamy.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.przypominamy.com
- group: operate
  title: ''
  type: Support
  url: https://przypominamy.com/kontakt
- group: company
  title: ''
  type: Blog
  url: https://przypominamy.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://przypominamy.com/cennik
- group: commercial
  title: ''
  type: TermsOfService
  url: https://przypominamy.com/regulamin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://przypominamy.com/polityka-prywatnosci
created: '2026-10-31'
description: Przypominamy.com is a Polish SMS gateway platform offering businesses a web panel and a RESTful API for sending SMS, MMS, voice messages, and managing contacts. Founded in 2010, it provides prepaid pricing starting at 0.15 PLN per message, with volume discounts, webhook delivery reports signed with HMAC, and SDKs for Node.js and Python. The service supports two‑way SMS on request, number lookup, templates, and integrates with AI assistants via its MCP server. Documentation, pricing, and support are available in Polish.
image: https://przypominamy.com/przypominamy-logo.png
json_schemas:
- name: Account
  property_count: 21
  slug: przypominamy-com-account
- name: ContactInput
  property_count: 6
  slug: przypominamy-com-contact-input
- name: HlrResult
  property_count: 9
  slug: przypominamy-com-hlr-result
- name: InboundMessage
  property_count: 8
  slug: przypominamy-com-inbound-message
- name: Message
  property_count: 17
  slug: przypominamy-com-message
- name: SendMessageRequest
  property_count: 10
  slug: przypominamy-com-send-message-request
jsonld:
- class_count: 16
  name: Przypominamy Com Context
  property_count: 72
  slug: przypominamy-com-context
layout: provider
modified: '2026-10-31'
name: przypominamy-com
nav: Providers
network: true
overview: 'przypominamy-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Czarna lista API, Kontakty i grupy API, Konto API, and 6 more. Tagged areas include Company, SMS, Communications, Poland, and Messaging.


  The przypominamy-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  przypominamy-com''s developer surface includes changelog, authentication, documentation, API reference, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Przypominamy Com Plans Pricing
  plan_count: 5
  slug: przypominamy-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Przypominamy Com Rate Limits
  slug: przypominamy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: przypominamy-com API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: przypominamy-com-rules
scopes:
- name: Przypominamy Com Scopes
  scope_count: 3
  slug: przypominamy-com-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 73.7
    developer_ergonomics: 37.4
    discoverability: 66.1
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/przypominamy-com/przypominamy-com-2026-11-03T141659.png
security:
- kind: authentication
  name: Przypominamy Com Authentication
  slug: przypominamy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Przypominamy Com Domain Security
  slug: przypominamy-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: account-info
  slug: przypominamy-com-account
- name: manage-contacts
  slug: przypominamy-com-contacts
- name: send-sms
  slug: przypominamy-com-send-sms
slug: przypominamy-com
tags:
- Company
- SMS
- Communications
- Poland
- Messaging
website: https://przypominamy.com/
---
