---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    event_surface_described: true
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
  score: 23.9
  scored_at: '2026-11-06'
api_count: 11
apis:
- description: API for NICE Contact Center platform, providing endpoints for contact management, reporting, and integration.
  name: NICE Contact Center API
  slug: nice-contact-center-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Channels API from NICE — 1 operation(s) for channels.
  name: NICE Channels API
  slug: nice-channels-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Contacts API from NICE — 1 operation(s) for contacts.
  name: NICE Contacts API
  slug: nice-contacts-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Incontactapi API from NICE — 3 operation(s) for incontactapi.
  name: NICE Incontactapi API
  slug: nice-incontactapi-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Perform Action API from NICE — 1 operation(s) for perform action.
  name: NICE Perform Action API
  slug: nice-perform-action-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Result API from NICE — 1 operation(s) for result.
  name: NICE Result API
  slug: nice-result-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Segments API from NICE — 1 operation(s) for segments.
  name: NICE Segments API
  slug: nice-segments-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Status API from NICE — 1 operation(s) for status.
  name: NICE Status API
  slug: nice-status-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The User Management API from NICE — 14 operation(s) for user management.
  name: NICE User Management API
  slug: nice-user-management-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The Voice Print Status API from NICE — 1 operation(s) for voice print status.
  name: NICE Voice Print Status API
  slug: nice-voice-print-status-api
- baseURL: https://api-do72.dev.nice-incontact.com
  baseurl_source: declared
  description: The .well Known API from NICE — 1 operation(s) for .well known.
  name: NICE .well Known API
  slug: nice-well-known-api
artifact_total: 25
asyncapis:
- description: ''
  name: Nice Webhooks
  slug: nice-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/nice/plans/nice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nice-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nice/rules/nice-rules.yml
  title: ''
  type: Spectral
  url: rules/nice-rules.yml
- group: design
  href: https://artifacts.apis.io/nice/json-ld/nice-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nice-context.jsonld
- group: design
  href: https://artifacts.apis.io/nice/vocabulary/nice-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nice-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nice/asyncapi/nice-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/nice-webhooks.yml
- group: design
  href: https://artifacts.apis.io/nice/data-model/nice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nice-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nice.com/company/trust-center
- group: auth
  href: https://artifacts.apis.io/nice/authentication/nice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nice-authentication.yml
- group: design
  href: https://artifacts.apis.io/nice/conformance/nice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nice-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nice/llms/nice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nice-llms.txt
- group: auth
  href: https://artifacts.apis.io/nice/well-known/nice-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nice-help-security.txt
- group: agent
  href: https://artifacts.apis.io/nice/well-known/nice-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nice-well-known.yml
- group: other
  href: https://artifacts.apis.io/nice/hosts/nice-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nice-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nice.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nice.com/company/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/nice/security/nice-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nice-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/nice/security/nice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nice.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.niceincontact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.niceincontact.com/Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.niceincontact.com/Documentation/GettingStarted
- group: company
  title: ''
  type: Blog
  url: https://www.nice.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nice.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.nice.com/services/customer-support
coverage:
  detail: Developer portal pages are HTML only and return no machine‑readable OpenAPI spec (e.g., https://developer.niceincontact.com/openapi.json redirects to a NotFound page).
  evidence:
  - status: 302
    url: https://developer.niceincontact.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: NICE provides a comprehensive Customer Experience (CX) AI platform that orchestrates human and AI agents, automates service, and empowers workforces. Their solutions span enterprise CX AI, integrations, cloud architecture, and agent workspaces, delivering scalable intelligent experiences across industries.
finops:
- has_sources: true
  method: derived
  name: Nice Finops
  primary_unit: agent per month / per session
  service_category: ''
  slug: nice-finops
  template: false
image: https://resources.nice.com/wp-content/uploads/2025/08/NiCE-logo.jpg
json_schemas:
- name: GetStatusRequestidResponse
  property_count: 2
  slug: nice-get-status-requestid-response
- name: GetWellKnownOpenidConfigurationResponse
  property_count: 16
  slug: nice-get-well-known-openid-configuration-response
- name: PostChannelsRequest
  property_count: 1
  slug: nice-post-channels-request
- name: PostContactsResponse
  property_count: 1
  slug: nice-post-contacts-response
- name: PostSegmentsResponse
  property_count: 1
  slug: nice-post-segments-response
jsonld:
- class_count: 5
  name: Nice Context
  property_count: 20
  slug: nice-context
layout: provider
modified: '2026-10-14'
name: NICE
nav: Providers
network: true
overview: 'NICE is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Contacts API, Incontactapi API, and 8 more. Tagged areas include Company, Customer Experience, Artificial Intelligence, Cloud, and Integration.


  The NICE catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  NICE''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, and 18 more developer resources.'
plans:
- name: Nice Plans Pricing
  plan_count: 10
  slug: nice-plans-pricing
- name: Nice Price Estimates
  plan_count: 0
  slug: nice-price-estimates
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: NICE API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: nice-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 75.8
    catalog_earned_first_party: 12.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 67.1
    contract_governance: 35.6
    contract_quality: 32.4
    developer_ergonomics: 31.0
    discoverability: 69.6
    operational_transparency: 18.4
  previous_composite: 50.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nice/nice-2026-11-03T140215.png
security:
- kind: authentication
  name: Nice Authentication
  slug: nice-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nice Domain Security
  slug: nice-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Nice Trust Center
  slug: nice-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP
slug: nice
tags:
- Company
- Customer Experience
- Artificial Intelligence
- Cloud
- Integration
website: https://www.nice.com
---
