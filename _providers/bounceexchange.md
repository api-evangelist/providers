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
api_count: 6
apis:
- description: API reference for Wunderkind platform
  name: Wunderkind API
  slug: wunderkind-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Contacts API from Bounceexchange — 1 operation(s) for contacts.
  name: Bounceexchange Contacts API
  slug: bounceexchange-contacts-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Createcontactactivities API from Bounceexchange — 1 operation(s) for createcontactactivities.
  name: Bounceexchange Createcontactactivities API
  slug: bounceexchange-createcontactactivities-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Id Resolution API from Bounceexchange — 2 operation(s) for id resolution.
  name: Bounceexchange Id Resolution API
  slug: bounceexchange-id-resolution-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Interaction API from Bounceexchange — 1 operation(s) for interaction.
  name: Bounceexchange Interaction API
  slug: bounceexchange-interaction-api
- baseURL: https://api.wknd.ai
  baseurl_source: declared
  description: The Text API from Bounceexchange — 6 operation(s) for text.
  name: Bounceexchange Text API
  slug: bounceexchange-text-api
artifact_total: 16
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/rules/bounceexchange-rules.yml
  title: ''
  type: Spectral
  url: rules/bounceexchange-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/json-ld/bounceexchange-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bounceexchange-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/vocabulary/bounceexchange-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bounceexchange-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/data-model/bounceexchange-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bounceexchange-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/changelog/bounceexchange-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bounceexchange-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/authentication/bounceexchange-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bounceexchange-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/conformance/bounceexchange-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bounceexchange-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/llms/bounceexchange-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bounceexchange-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/well-known/bounceexchange-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bounceexchange-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/well-known/bounceexchange-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bounceexchange-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/well-known/bounceexchange-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bounceexchange-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/hosts/bounceexchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bounceexchange-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/vendors/bounceexchange-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bounceexchange-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/bounceexchange/refs/heads/main/security/bounceexchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bounceexchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wunderkind.co
coverage:
  checked: '2026-10-03'
  detail: Developer portal provides HTML reference but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://developer.wunderkind.co/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Bounceexchange, now operating as Wunderkind, provides an autonomous marketing platform that leverages AI-driven identity and decisioning to help brands maximize revenue. The platform offers tools for identity resolution, audience segmentation, analytics, and programmatic advertising, targeting e‑commerce, travel, hospitality, and other consumer‑facing industries. Founded in 2010, the company has evolved to integrate AI and data privacy‑safe consumer identity networks, serving over 700 brands worldwide.
json_schemas:
- name: PostCreatecontactactivitiesRequest
  property_count: 13
  slug: bounceexchange-post-createcontactactivities-request
- name: PostCreatecontactactivitiesResponse
  property_count: 2
  slug: bounceexchange-post-createcontactactivities-response
- name: PostTextBulkMessageSendResponse
  property_count: 2
  slug: bounceexchange-post-text-bulk-message-send-response
- name: PostTextMessageSendRequest
  property_count: 6
  slug: bounceexchange-post-text-message-send-request
- name: PostTextSubscriptionStatusResponse
  property_count: 2
  slug: bounceexchange-post-text-subscription-status-response
- name: PostTextTextidRequest
  property_count: 2
  slug: bounceexchange-post-text-textid-request
jsonld:
- class_count: 11
  name: Bounceexchange Context
  property_count: 26
  slug: bounceexchange-context
layout: provider
modified: '2026-10-03'
name: Bounceexchange
nav: Providers
network: true
overview: 'Bounceexchange publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Createcontactactivities API, Id Resolution API, and 3 more. Tagged areas include Company.


  The Bounceexchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bounceexchange''s developer surface includes changelog, authentication, support, engineering blog, API reference, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bounceexchange API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: bounceexchange-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 54.8
    discoverability: 57.1
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
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bounceexchange Authentication
  slug: bounceexchange-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bounceexchange Domain Security
  slug: bounceexchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bounceexchange
tags:
- Company
website: https://www.wunderkind.co
---
