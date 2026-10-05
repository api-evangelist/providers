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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-10-04'
api_count: 5
apis:
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Contacts API from Wunderkind — 1 operation(s) for contacts.
  name: Wunderkind Contacts API
  slug: bouncex-contacts-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Createcontactactivities API from Wunderkind — 1 operation(s) for createcontactactivities.
  name: Wunderkind Createcontactactivities API
  slug: bouncex-createcontactactivities-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Id Resolution API from Wunderkind — 2 operation(s) for id resolution.
  name: Wunderkind Id Resolution API
  slug: bouncex-id-resolution-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Interaction API from Wunderkind — 1 operation(s) for interaction.
  name: Wunderkind Interaction API
  slug: bouncex-interaction-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Text API from Wunderkind — 6 operation(s) for text.
  name: Wunderkind Text API
  slug: bouncex-text-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/rules/bouncex-rules.yml
  title: ''
  type: Spectral
  url: rules/bouncex-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/json-ld/bouncex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bouncex-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/vocabulary/bouncex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bouncex-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/data-model/bouncex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bouncex-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/changelog/bouncex-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bouncex-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/authentication/bouncex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bouncex-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/conformance/bouncex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bouncex-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/llms/bouncex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bouncex-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/well-known/bouncex-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bouncex-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/well-known/bouncex-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bouncex-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/well-known/bouncex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bouncex-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/hosts/bouncex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bouncex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/vendors/bouncex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bouncex-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wunderkind.co/terms
- group: operate
  title: ''
  type: Support
  url: https://support.wunderkind.co/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wunderkind.co/
- group: build
  title: ''
  type: SDKs
  url: https://www.wunderkind.co/terms/sdk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wunderkind.co/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.wunderkind.co/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.wunderkind.co/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wunderkind.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wunderkind.co/docs/msdk-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wunderkind.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bouncex/refs/heads/main/security/bouncex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bouncex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wunderkind.co/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://developer.wunderkind.co/mcp
  - status: 403
    url: https://www.wunderkind.co/mcp
  - status: 403
    url: https://hello.wunderkind.co/mcp
  - status: null
    url: https://forgeglobal.com/bouncex_stock/
  reason: partner-login
  state: gated
created: '2026-10-03'
description: Wunderkind, formerly known as BounceX, provides an autonomous marketing platform that leverages AI-driven decisioning to personalize consumer experiences and drive revenue for ecommerce brands. The platform offers identity resolution, audience segmentation, and real‑time data activation across web, email, and advertising channels, helping marketers deliver targeted content and improve conversion rates.
json_schemas:
- name: PostContactsV1AddressesEmailSearchRequest
  property_count: 2
  slug: bouncex-post-contacts-v1-addresses-email-search-request
- name: PostCreatecontactactivitiesRequest
  property_count: 15
  slug: bouncex-post-createcontactactivities-request
- name: PostInteractionV1EventsRequest
  property_count: 3
  slug: bouncex-post-interaction-v1-events-request
- name: PostTextBulkMessageSendResponse
  property_count: 2
  slug: bouncex-post-text-bulk-message-send-response
- name: PostTextMessageSendRequest
  property_count: 6
  slug: bouncex-post-text-message-send-request
- name: PostTextSubscriptionStatusResponse
  property_count: 2
  slug: bouncex-post-text-subscription-status-response
jsonld:
- class_count: 12
  name: Bouncex Context
  property_count: 33
  slug: bouncex-context
layout: provider
modified: '2026-10-03'
name: Wunderkind
nav: Providers
network: true
overview: 'Wunderkind publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Createcontactactivities API, Id Resolution API, and 2 more. Tagged areas include Marketing, Artificial Intelligence, E-Commerce, Personalization, and Identity.


  The Wunderkind catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wunderkind''s developer surface includes changelog, authentication, support, engineering blog, API reference, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Wunderkind API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: bouncex-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 54.8
    discoverability: 75.0
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bouncex Authentication
  slug: bouncex-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bouncex Domain Security
  slug: bouncex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bouncex
tags:
- Marketing
- Artificial Intelligence
- E-Commerce
- Personalization
- Identity
website: https://www.wunderkind.co/
---
