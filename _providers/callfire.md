---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-17'
api_count: 13
apis:
- description: CallFire API provides voice calls, SMS, and related communication services.
  name: CallFire API
  slug: callfire-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Callfire API API from Callfire — 2 operation(s) for callfire api.
  name: Callfire Callfire API
  slug: callfire-callfire-api-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Callfirexml API from Callfire — 2 operation(s) for callfirexml.
  name: Callfire Callfirexml API
  slug: callfire-callfirexml-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Calls API from Callfire — 6 operation(s) for calls.
  name: Callfire Calls API
  slug: callfire-calls-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Campaign API from Callfire — 1 operation(s) for campaign.
  name: Callfire Campaign API
  slug: callfire-campaign-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Contacts API from Callfire — 3 operation(s) for contacts.
  name: Callfire Contacts API
  slug: callfire-contacts-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Files API from Callfire — 4 operation(s) for files.
  name: Callfire Files API
  slug: callfire-files-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Inbound API from Callfire — 1 operation(s) for inbound.
  name: Callfire Inbound API
  slug: callfire-inbound-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Me API from Callfire — 2 operation(s) for me.
  name: Callfire Me API
  slug: callfire-me-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Reports API from Callfire — 5 operation(s) for reports.
  name: Callfire Reports API
  slug: callfire-reports-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Service API from Callfire — 1 operation(s) for service.
  name: Callfire Service API
  slug: callfire-service-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Sms API from Callfire — 1 operation(s) for sms.
  name: Callfire Sms API
  slug: callfire-sms-api
- baseURL: https://api.callfire.com/v2
  baseurl_source: declared
  description: The Utils API from Callfire — 1 operation(s) for utils.
  name: Callfire Utils API
  slug: callfire-utils-api
artifact_total: 24
asyncapis:
- description: ''
  name: Callfire Webhooks
  slug: callfire-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/rules/callfire-rules.yml
  title: ''
  type: Spectral
  url: rules/callfire-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/json-ld/callfire-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/callfire-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/vocabulary/callfire-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/callfire-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/data-model/callfire-data-model.yml
  title: ''
  type: DataModel
  url: data-model/callfire-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/plans/callfire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/callfire-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/asyncapi/callfire-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/callfire-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/conformance/callfire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/callfire-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/well-known/callfire-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/callfire-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/well-known/callfire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/callfire-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/hosts/callfire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/callfire-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/vendors/callfire-vendors.yml
  title: ''
  type: Vendors
  url: vendors/callfire-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/packages/callfire-packages.yml
  title: ''
  type: SDKs
  url: packages/callfire-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/packages/callfire-packages.yml
  title: ''
  type: Packages
  url: packages/callfire-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: http://status.callfire.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.callfire.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CallFire
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/callfire/refs/heads/main/security/callfire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/callfire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.callfire.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.callfire.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.callfire.com/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://developers.callfire.com/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.callfire.com/learn.html
- group: operate
  title: ''
  type: Support
  url: https://www.callfire.com/help/docs/faq
- group: company
  title: ''
  type: Blog
  url: https://www.callfire.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.callfire.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.callfire.com/ui/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.callfire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.callfire.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.callfire.com/legal/compliance
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.callfire.com
  - status: 403
    url: https://equityzen.com/company/callfire
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Callfire provides cloud-based communication solutions that enable businesses to engage customers via voice calls, text messaging, and IVR. Their platform offers tools for call tracking, voice broadcasting, and automated messaging, helping companies improve outreach, increase revenue, and streamline customer interactions. With over 4 billion messages delivered, Callfire serves a wide range of industries and integrates with popular CRMs and marketing platforms.
image: https://www.callfire.com/sites/default/files/OpenGraph/callfire-social-post.png
json_schemas:
- name: GetV2CallsBroadcastsIdRecipientsResponse
  property_count: 1
  slug: callfire-get-v2-calls-broadcasts-id-recipients-response
- name: GetV2CallsBroadcastsResponse
  property_count: 2
  slug: callfire-get-v2-calls-broadcasts-response
- name: GetV2V2IdResponse
  property_count: 15
  slug: callfire-get-v2-v2-id-response
- name: PostCallsRequest
  property_count: 14
  slug: callfire-post-calls-request
- name: PostV2CallsBroadcastsBroadcastidIdResponse
  property_count: 1
  slug: callfire-post-v2-calls-broadcasts-broadcastid-id-response
- name: PostV2V2IdResponse
  property_count: 1
  slug: callfire-post-v2-v2-id-response
jsonld:
- class_count: 12
  name: Callfire Context
  property_count: 31
  slug: callfire-context
layout: provider
modified: '2026-10-06'
name: Callfire
nav: Providers
network: true
overview: 'Callfire is listed with 13 APIs on the [APIs.io](https://apis.io/) network, including Callfire API, Callfirexml API, Calls API, and 10 more. Tagged areas include Company, Communications, Cloud, Messaging, and Voice.


  The Callfire catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Callfire''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Callfire Plans Pricing
  plan_count: 5
  slug: callfire-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Callfire API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: callfire-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 32.2
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Callfire Domain Security
  slug: callfire-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: callfire
tags:
- Company
- Communications
- Cloud
- Messaging
- Voice
website: https://www.callfire.com
---
