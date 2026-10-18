---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: Conversational AI platform API documented at Haptik Docs
  name: Haptik API
  slug: haptik-api-2
- baseURL: https://staging-messenger.haptikapi.com
  baseurl_source: declared
  description: The Gccs Ws API from Haptik — 1 operation(s) for gccs ws.
  name: Haptik Gccs Ws API
  slug: haptik-gccs-ws-api
- baseURL: https://staging-messenger.haptikapi.com
  baseurl_source: declared
  description: The Haptik API API from Haptik — 2 operation(s) for haptik api.
  name: Haptik Haptik API
  slug: haptik-haptik-api-api
- baseURL: https://staging-messenger.haptikapi.com
  baseurl_source: declared
  description: The Integration API from Haptik — 2 operation(s) for integration.
  name: Haptik Integration API
  slug: haptik-integration-api
- baseURL: https://staging-messenger.haptikapi.com
  baseurl_source: declared
  description: The Log File From User API from Haptik — 1 operation(s) for log file from user.
  name: Haptik Log File From User API
  slug: haptik-log-file-from-user-api
- baseURL: https://staging-messenger.haptikapi.com
  baseurl_source: declared
  description: The Mogambo Api API from Haptik — 2 operation(s) for mogambo api.
  name: Haptik Mogambo API
  slug: haptik-mogambo-api-api
- baseURL: https://staging-messenger.haptikapi.com
  baseurl_source: declared
  description: The User API from Haptik — 2 operation(s) for user.
  name: Haptik User API
  slug: haptik-user-api
artifact_total: 18
asyncapis:
- description: ''
  name: Haptik Webhooks
  slug: haptik-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/well-known/haptik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/haptik-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/rules/haptik-rules.yml
  title: ''
  type: Spectral
  url: rules/haptik-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/json-ld/haptik-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/haptik-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/vocabulary/haptik-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/haptik-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/asyncapi/haptik-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/haptik-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/data-model/haptik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/haptik-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/changelog/haptik-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/haptik-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.haptik.ai/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/conformance/haptik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/haptik-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/hosts/haptik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/haptik-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/vendors/haptik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/haptik-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.haptik.ai/terms-india
- group: operate
  title: ''
  type: Support
  url: https://www.haptik.ai/ai-agents/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.haptik.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.haptik.ai/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.haptik.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.haptik.ai/getting-started-guides
- group: docs
  title: ''
  type: Documentation
  url: https://docs.haptik.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/security/haptik-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/haptik-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/haptik/refs/heads/main/security/haptik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/haptik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.haptik.ai
coverage:
  checked: '2026-10-13'
  detail: Documentation is public but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://docs.haptik.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Haptik, part of Jio Platforms, provides AI‑powered conversational agents for enterprises, enabling customer service, sales, bookings, and lead qualification across messaging channels like WhatsApp, Voice, Instagram, and web chat. Their platform offers analytics, generative AI consulting, and integration tools for building intelligent chatbots that enhance customer experience and drive business outcomes.
json_schemas:
- name: GetMogamboApiNodesFaqCreateStatusTaskidResponse
  property_count: 2
  slug: haptik-get-mogambo-api-nodes-faq-create-status-taskid-response
- name: PostIntegrationExternalV20SendChatToAgentRequest
  property_count: 5
  slug: haptik-post-integration-external-v20-send-chat-to-agent-request
- name: PostV10LogFileFromUserRequest
  property_count: 5
  slug: haptik-post-v10-log-file-from-user-request
- name: PostV10LogFileFromUserResponse
  property_count: 5
  slug: haptik-post-v10-log-file-from-user-response
- name: PostV10UserRequest
  property_count: 6
  slug: haptik-post-v10-user-request
- name: PutV10UserRequest2
  property_count: 6
  slug: haptik-put-v10-user-request2
jsonld:
- class_count: 14
  name: Haptik Context
  property_count: 24
  slug: haptik-context
layout: provider
modified: '2026-10-13'
name: Haptik
nav: Providers
network: true
overview: 'Haptik is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Gccs Ws API, Haptik API, Integration API, and 4 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, Messaging, and Enterprise.


  The Haptik catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Haptik''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Haptik API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: haptik-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 33.3
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 23.7
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: domain-security
  name: Haptik Domain Security
  slug: haptik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Haptik Trust Center
  slug: haptik-trust-center
  summary_line: ISO 27001, HIPAA, GDPR, FIPS 140
slug: haptik
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Messaging
- Enterprise
website: https://www.haptik.ai
---
