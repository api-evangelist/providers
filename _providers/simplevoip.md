---
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Simplevoip Agentic Access
  operation_count: 5
  slug: simplevoip-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://public.simplevoip.us
  baseurl_source: declared
  description: Retrieval of recorded call audio.
  name: SimpleVoIP Call Recordings API
  slug: simplevoip-call-recordings-api
- baseURL: https://public.simplevoip.us
  baseurl_source: declared
  description: Call detail record (CDR) notification webhook, fired when a call completes.
  name: SimpleVoIP CDR API
  slug: simplevoip-cdr-api
- baseURL: https://public.simplevoip.us
  baseurl_source: declared
  description: Bulk management of per-site Music on Hold settings.
  name: SimpleVoIP Music on Hold API
  slug: simplevoip-music-on-hold-api
- baseURL: https://public.simplevoip.us
  baseurl_source: declared
  description: Programmatic SMS/MMS sending and inbound/outbound notification webhooks.
  name: SimpleVoIP SMS API
  slug: simplevoip-sms-api
- baseURL: https://public.simplevoip.us
  baseurl_source: declared
  description: Bulk management of per-site call routing rules based on time of day.
  name: SimpleVoIP Time of Day API
  slug: simplevoip-time-of-day-api
artifact_total: 19
asyncapis:
- description: ''
  name: Simplevoip Webhooks
  slug: simplevoip-webhooks
common:
- group: other
  href: https://artifacts.apis.io/simplevoip/capabilities/simplevoip-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/simplevoip-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/simplevoip/well-known/simplevoip-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/simplevoip-status-security.txt
- group: agent
  href: https://artifacts.apis.io/simplevoip/well-known/simplevoip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simplevoip-well-known.yml
- group: agent
  href: https://artifacts.apis.io/simplevoip/agentic-access/simplevoip-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/simplevoip-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/simplevoip/rules/simplevoip-rules.yml
  title: ''
  type: Spectral
  url: rules/simplevoip-rules.yml
- group: design
  href: https://artifacts.apis.io/simplevoip/json-ld/simplevoip-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/simplevoip-context.jsonld
- group: design
  href: https://artifacts.apis.io/simplevoip/vocabulary/simplevoip-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/simplevoip-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/simplevoip/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/simplevoip/asyncapi/simplevoip-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/simplevoip-webhooks.yml
- group: design
  href: https://artifacts.apis.io/simplevoip/data-model/simplevoip-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simplevoip-data-model.yml
- group: auth
  href: https://artifacts.apis.io/simplevoip/authentication/simplevoip-authentication.yml
  title: ''
  type: Authentication
  url: authentication/simplevoip-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simplevoip.us/
- group: design
  href: https://artifacts.apis.io/simplevoip/lifecycle/simplevoip-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/simplevoip-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/simplevoip/errors/simplevoip-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/simplevoip-problem-types.yml
- group: design
  href: https://artifacts.apis.io/simplevoip/conformance/simplevoip-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simplevoip-conformance.yml
- group: other
  href: https://artifacts.apis.io/simplevoip/hosts/simplevoip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simplevoip-hosts.yml
- group: other
  href: https://artifacts.apis.io/simplevoip/vendors/simplevoip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simplevoip-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://simplevoip.com/sign-up-for-simplevoip-newsletter/
- group: auth
  href: https://artifacts.apis.io/simplevoip/security/simplevoip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplevoip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simplevoip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://simplevoip.com/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://simplevoip.github.io/sv_portal/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://q.simplevoip.com/
- group: operate
  title: ''
  type: Support
  url: https://support.simplevoip.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://simplevoip.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simplevoip
- group: commercial
  title: ''
  type: Pricing
  url: https://simplevoip.com/features-and-plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.simplevoip.com/hc/en-us/articles/360056923954
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.simplevoip.com/hc/en-us/articles/27831208180247-SMS-Privacy-Policy-Template
created: '2026-10-28'
description: SimpleVoIP provides cloud‑based voice communication solutions for distributed enterprises and small‑to‑medium businesses. Their platform offers VoIP phone services, AI‑driven call analytics, integration with CRM and POS systems, and customizable deployment options, aiming to simplify communications and improve operational efficiency.
image: https://simplevoip.com/wp-content/uploads/Updated-SV-Logo.png
json_schemas:
- name: EnqueueJobResponse
  property_count: 2
  slug: simplevoip-enqueue-job-response
- name: ModifyMohRequest
  property_count: 4
  slug: simplevoip-modify-moh-request
- name: ModifyTodRulesRequest
  property_count: 2
  slug: simplevoip-modify-tod-rules-request
- name: SendSmsRequest
  property_count: 5
  slug: simplevoip-send-sms-request
- name: SendSmsResponseFailure
  property_count: 2
  slug: simplevoip-send-sms-response-failure
- name: SendSmsResponseSuccess
  property_count: 2
  slug: simplevoip-send-sms-response-success
jsonld:
- class_count: 9
  name: Simplevoip Context
  property_count: 65
  slug: simplevoip-context
layout: provider
modified: '2026-10-28'
name: SimpleVoIP
nav: Providers
network: true
overview: 'SimpleVoIP publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Call Recordings API, CDR API, Music on Hold API, and 2 more. Tagged areas include VoIP, Communications, UCaaS, AI, and SMB.


  The SimpleVoIP catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SimpleVoIP''s developer surface includes authentication, signup flow, documentation, API reference, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: SimpleVoIP API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: simplevoip-rules
scopes:
- name: Simplevoip Scopes
  scope_count: 0
  slug: simplevoip-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 71.5
    developer_ergonomics: 51.7
    discoverability: 66.1
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Simplevoip Authentication
  slug: simplevoip-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Simplevoip Domain Security
  slug: simplevoip-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: send-sms
  slug: simplevoip-send-sms
slug: simplevoip
tags:
- VoIP
- Communications
- UCaaS
- AI
- SMB
website: https://simplevoip.com/
---
