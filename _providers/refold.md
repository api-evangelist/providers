---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://app.refold.ai
  baseurl_source: declared
  description: 'Refold API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Refold API
  slug: refold-api
artifact_total: 14
asyncapis:
- description: ''
  name: Refold Webhooks
  slug: refold-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/refold/rate-limits/refold-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/refold-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/refold/rules/refold-rules.yml
  title: ''
  type: Spectral
  url: rules/refold-rules.yml
- group: design
  href: https://artifacts.apis.io/refold/json-ld/refold-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/refold-context.jsonld
- group: design
  href: https://artifacts.apis.io/refold/vocabulary/refold-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/refold-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/refold/asyncapi/refold-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/refold-webhooks.yml
- group: design
  href: https://artifacts.apis.io/refold/data-model/refold-data-model.yml
  title: ''
  type: DataModel
  url: data-model/refold-data-model.yml
- group: operate
  href: https://artifacts.apis.io/refold/changelog/refold-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/refold-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.refold.ai/
- group: auth
  href: https://artifacts.apis.io/refold/authentication/refold-authentication.yml
  title: ''
  type: Authentication
  url: authentication/refold-authentication.yml
- group: design
  href: https://artifacts.apis.io/refold/conformance/refold-conformance.yml
  title: ''
  type: Conformance
  url: conformance/refold-conformance.yml
- group: agent
  href: https://artifacts.apis.io/refold/llms/refold-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/refold-llms.txt
- group: other
  href: https://artifacts.apis.io/refold/a2a/refold-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/refold-a2a.yml
- group: agent
  href: https://artifacts.apis.io/refold/well-known/refold-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/refold-well-known.yml
- group: other
  href: https://artifacts.apis.io/refold/hosts/refold-hosts.yml
  title: ''
  type: Hosts
  url: hosts/refold-hosts.yml
- group: other
  href: https://artifacts.apis.io/refold/vendors/refold-vendors.yml
  title: ''
  type: Vendors
  url: vendors/refold-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.refold.ai/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.refold.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.refold.ai/sign-up
- group: auth
  title: ''
  type: Security
  url: https://www.refold.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.refold.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.refold.ai/v3/changelog/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.refold.ai/implement/implementation/integrate/setup-linked-account
- group: docs
  title: ''
  type: Documentation
  url: https://docs.refold.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.refold.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/refold/security/refold-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/refold-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/refold/security/refold-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/refold-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.refold.ai/
coverage:
  checked: '2026-10-21'
  detail: The domain refold.com hosts a parking page with no API documentation.
  evidence:
  - status: 200
    url: http://refold.com
  reason: not-a-software-company
  state: none
created: '2026-10-21'
description: Refold AI provides an AI‑powered, secure enterprise integrations platform that enables organizations to connect and automate workflows across major systems such as SAP, Oracle, and Workday. Its agents handle brittle APIs, custom logic, and self‑healing workflows, offering audit logs and over 1,000 pre‑built connectors. Refold focuses on security, scalability, and rapid deployment for large enterprises seeking to modernize their integration landscape.
image: https://www.refold.ai/og-image.svg
json_schemas:
- name: GetApiV2IntegrationSchemaHubspotActionsCreateContactExecuteR
  property_count: 3
  slug: refold-get-api-v2-integration-schema-hubspot-actions-create-contact-execute-r
- name: GetApiV2IntegrationSchemaHubspotActionsGetContactExecuteResp
  property_count: 3
  slug: refold-get-api-v2-integration-schema-hubspot-actions-get-contact-execute-resp
- name: GetApiV2PublicApplicationResponse
  property_count: 4
  slug: refold-get-api-v2-public-application-response
- name: PostApiV2PublicEventHubspotRequest
  property_count: 2
  slug: refold-post-api-v2-public-event-hubspot-request
- name: PostApiV2PublicEventHubspotResponse
  property_count: 4
  slug: refold-post-api-v2-public-event-hubspot-response
- name: PostApiV2PublicEventTriggerRequest
  property_count: 2
  slug: refold-post-api-v2-public-event-trigger-request
jsonld:
- class_count: 13
  name: Refold Context
  property_count: 19
  slug: refold-context
layout: provider
modified: '2026-10-21'
name: Refold
nav: Providers
network: true
overview: 'Refold is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Integration, Enterprise, and Automation.


  The Refold catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Refold''s developer surface includes changelog, authentication, signup flow, getting-started guide, documentation, API reference, and 21 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 2
  name: Refold Rate Limits
  slug: refold-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Refold API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: refold-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 33.8
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 71.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Refold Authentication
  slug: refold-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Refold Domain Security
  slug: refold-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Refold Trust Center
  slug: refold-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: refold
tags:
- Company
- Artificial Intelligence
- Integration
- Enterprise
- Automation
website: https://www.refold.ai/
---
