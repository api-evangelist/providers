---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for DevInbox, providing endpoints for email notifications and inbox management.
  name: DevInbox API
  slug: devinbox-api
- baseURL: https://api.devinbox.io
  baseurl_source: declared
  description: 'DevInbox API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DevInbox API
  slug: devinbox-io-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/devinbox-io/rules/devinbox-io-rules.yml
  title: ''
  type: Spectral
  url: rules/devinbox-io-rules.yml
- group: design
  href: https://artifacts.apis.io/devinbox-io/json-ld/devinbox-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/devinbox-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/devinbox-io/vocabulary/devinbox-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/devinbox-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/devinbox-io/data-model/devinbox-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/devinbox-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/devinbox-io/conformance/devinbox-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devinbox-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/devinbox-io/llms/devinbox-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devinbox-io-llms.txt
- group: other
  href: https://artifacts.apis.io/devinbox-io/hosts/devinbox-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devinbox-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/devinbox-io/packages/devinbox-io-packages.yml
  title: ''
  type: SDKs
  url: packages/devinbox-io-packages.yml
- group: build
  href: https://artifacts.apis.io/devinbox-io/packages/devinbox-io-packages.yml
  title: ''
  type: Packages
  url: packages/devinbox-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devinbox.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devinbox.io/privacy
- group: start
  title: ''
  type: Login
  url: https://app.devinbox.io/Account/Login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dev-inbox-io
- group: start
  title: ''
  type: GettingStarted
  url: https://devinbox.io/doc/getting-started
- group: auth
  href: https://artifacts.apis.io/devinbox-io/security/devinbox-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devinbox-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devinbox.io/
coverage:
  checked: '2026-11-05'
  detail: OpenAPI spec endpoints on api.devinbox.io return 401 Unauthorized, requiring an API key.
  evidence:
  - status: 401
    url: https://api.devinbox.io/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-05'
description: DevInbox is a service that provides developers with a unified inbox for API notifications, alerts, and messages. The platform is shutting down on 31 December 2026, with new sign‑ups closed but existing accounts retaining full access until the shutdown date. It offers integrations for various API providers, customizable routing, and a web dashboard for managing inbound communications.
image: https://devinbox.io/images/logo/logo-light.png
json_schemas:
- name: GetMailboxesResponse
  property_count: 2
  slug: devinbox-io-get-mailboxes-response
- name: GetMessagesKeyResponse
  property_count: 3
  slug: devinbox-io-get-messages-key-response
- name: GetMessagesKeySingleResponse
  property_count: 9
  slug: devinbox-io-get-messages-key-single-response
- name: GetMessagesKeyTemplateSingleResponse
  property_count: 10
  slug: devinbox-io-get-messages-key-template-single-response
- name: PostMailboxesRequest
  property_count: 2
  slug: devinbox-io-post-mailboxes-request
- name: PostMessagesKeySendRequest
  property_count: 7
  slug: devinbox-io-post-messages-key-send-request
jsonld:
- class_count: 10
  name: Devinbox Io Context
  property_count: 19
  slug: devinbox-io-context
layout: provider
modified: '2026-11-05'
name: DevInbox
nav: Providers
network: true
overview: 'DevInbox is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Email, Notification, API Integration, and Shutdown.


  The DevInbox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DevInbox''s developer surface includes getting-started guide and 15 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DevInbox API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: devinbox-io-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devinbox Io Domain Security
  slug: devinbox-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: devinbox-io
tags:
- Developer Tools
- Email
- Notification
- API Integration
- Shutdown
website: https://devinbox.io/
---
