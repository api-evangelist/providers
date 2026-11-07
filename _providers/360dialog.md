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
  - security
  - sandbox
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: WhatsApp Business API platform
  name: 360dialog API
  slug: 360dialog-api-2
- description: '360dialog API as documented publicly: 44 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: 360dialog API
  slug: 360dialog-api
artifact_total: 14
asyncapis:
- description: ''
  name: 360Dialog Webhooks
  slug: 360dialog-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/360dialog/plans/360dialog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/360dialog-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/360dialog/rules/360dialog-rules.yml
  title: ''
  type: Spectral
  url: rules/360dialog-rules.yml
- group: design
  href: https://artifacts.apis.io/360dialog/json-ld/360dialog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/360dialog-context.jsonld
- group: design
  href: https://artifacts.apis.io/360dialog/vocabulary/360dialog-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/360dialog-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/360dialog/asyncapi/360dialog-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/360dialog-webhooks.yml
- group: design
  href: https://artifacts.apis.io/360dialog/data-model/360dialog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/360dialog-data-model.yml
- group: start
  href: https://artifacts.apis.io/360dialog/sandbox/360dialog-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/360dialog-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/360dialog/authentication/360dialog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/360dialog-authentication.yml
- group: design
  href: https://artifacts.apis.io/360dialog/conformance/360dialog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/360dialog-conformance.yml
- group: agent
  href: https://artifacts.apis.io/360dialog/llms/360dialog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/360dialog-llms.txt
- group: auth
  href: https://artifacts.apis.io/360dialog/well-known/360dialog-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/360dialog-portal-security.txt
- group: agent
  href: https://artifacts.apis.io/360dialog/well-known/360dialog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/360dialog-well-known.yml
- group: other
  href: https://artifacts.apis.io/360dialog/hosts/360dialog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/360dialog-hosts.yml
- group: other
  href: https://artifacts.apis.io/360dialog/vendors/360dialog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/360dialog-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.360dialog.com/partner/signup
- group: company
  title: ''
  type: Newsroom
  url: https://360dialog.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.360dialog.com/docs/mba/meta-business-agent/onboarding-options
- group: docs
  title: ''
  type: APIReference
  url: https://docs.360dialog.com/docs/messaging-api/api-reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/360dialog
- group: auth
  href: https://artifacts.apis.io/360dialog/security/360dialog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/360dialog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.360dialog.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.360dialog.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.360dialog.com
- group: commercial
  title: ''
  type: Pricing
  url: https://360dialog.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://360dialog.com/blog
- group: company
  title: ''
  type: About
  url: https://360dialog.com/about
- group: operate
  title: ''
  type: Contact
  url: https://360dialog.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.360dialog.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://360dialog.com/legal/privacy-policy
created: '2026-11-01'
description: 360dialog provides a WhatsApp Business Solutions Platform that enables enterprises to integrate WhatsApp messaging into their customer communication channels. Through a robust API, businesses can send notifications, support messages, and marketing content at scale, leveraging official Meta partnership and compliance. The platform offers features such as message templates, webhooks, sandbox testing, and detailed analytics, helping over 100,000 businesses handle billions of messages monthly.
image: https://framerusercontent.com/assets/t3ELN7eRqVUEWAur35U4YNOszNs.png
json_schemas:
- name: GetFlowsFlowidResponse
  property_count: 11
  slug: 360dialog-get-flows-flowid-response
- name: GetGroupsGroupidResponse
  property_count: 9
  slug: 360dialog-get-groups-groupid-response
- name: GetMediaidResponse
  property_count: 6
  slug: 360dialog-get-mediaid-response
- name: GetRcsV1SendersSenderResponse
  property_count: 17
  slug: 360dialog-get-rcs-v1-senders-sender-response
- name: PostFlowsRequest
  property_count: 6
  slug: 360dialog-post-flows-request
- name: PostRcsV1SendersRequest
  property_count: 15
  slug: 360dialog-post-rcs-v1-senders-request
jsonld:
- class_count: 59
  name: 360Dialog Context
  property_count: 72
  slug: 360dialog-context
layout: provider
modified: '2026-11-01'
name: 360dialog
nav: Providers
network: true
overview: '360dialog is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WhatsApp, Messaging, and Business.


  The 360dialog catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  360dialog''s developer surface includes sandbox, authentication, signup flow, getting-started guide, API reference, documentation, pricing, and 22 more developer resources.'
plans:
- name: 360Dialog Plans Pricing
  plan_count: 7
  slug: 360dialog-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: 360dialog API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: 360dialog-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 35.0
    developer_ergonomics: 39.3
    discoverability: 49.1
    operational_transparency: 28.9
  previous_composite: 49.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 360Dialog Authentication
  slug: 360dialog-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 360Dialog Domain Security
  slug: 360dialog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 360dialog
tags:
- Company
- WhatsApp
- Messaging
- Business
website: https://www.360dialog.com
---
