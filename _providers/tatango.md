---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.tatango.com
  baseurl_source: declared
  description: 'Tatango API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Tatango API
  slug: tatango-api
artifact_total: 14
asyncapis:
- description: ''
  name: Tatango Webhooks
  slug: tatango-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/tatango/rate-limits/tatango-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tatango-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tatango/rules/tatango-rules.yml
  title: ''
  type: Spectral
  url: rules/tatango-rules.yml
- group: design
  href: https://artifacts.apis.io/tatango/json-ld/tatango-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tatango-context.jsonld
- group: design
  href: https://artifacts.apis.io/tatango/vocabulary/tatango-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tatango-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tatango/asyncapi/tatango-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tatango-webhooks.yml
- group: design
  href: https://artifacts.apis.io/tatango/data-model/tatango-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tatango-data-model.yml
- group: design
  href: https://artifacts.apis.io/tatango/conventions/tatango-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tatango-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tatango.com/trust
- group: auth
  href: https://artifacts.apis.io/tatango/security/tatango-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tatango-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/tatango/conformance/tatango-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tatango-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tatango/llms/tatango-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tatango-llms.txt
- group: other
  href: https://artifacts.apis.io/tatango/a2a/tatango-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tatango-a2a.yml
- group: auth
  href: https://artifacts.apis.io/tatango/well-known/tatango-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tatango-help-security.txt
- group: agent
  href: https://artifacts.apis.io/tatango/well-known/tatango-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tatango-well-known.yml
- group: other
  href: https://artifacts.apis.io/tatango/hosts/tatango-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tatango-hosts.yml
- group: other
  href: https://artifacts.apis.io/tatango/vendors/tatango-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tatango-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.tatango.com/login
- group: start
  title: ''
  type: GettingStarted
  url: http://help.tatango.com/en/articles/10178331-getting-started-with-segments
- group: docs
  title: ''
  type: APIReference
  url: https://developers.momogood.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tatango
- group: auth
  href: https://artifacts.apis.io/tatango/security/tatango-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tatango-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tatango/security/tatango-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tatango-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tatango/security/tatango-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tatango-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tatango.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tatango.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.tatango.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tatango.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.tatango.com/contact-sales/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tatango.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tatango.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable extraction.
  evidence:
  - status: 200
    url: https://www.tatango.com/resources
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Tatango provides a cloud‑based SMS fundraising platform for nonprofit organizations, enabling them to create, send, and manage text‑message donation campaigns at scale. Founded in 2007, the service supports integrations with major donor‑management tools, offers AI‑driven segmentation, and reports high open‑rate and ROI metrics. It serves thousands of nonprofits and political campaigns, handling billions of messages annually, and emphasizes compliance with TCPA and 10DLC regulations.
image: https://www.tatango.com/wp-content/uploads/2021/06/tatango.png
json_schemas:
- name: GetApiV2AccountsMeResponse
  property_count: 2
  slug: tatango-get-api-v2-accounts-me-response
- name: GetApiV2ListsIdOptInSettingsResponse
  property_count: 3
  slug: tatango-get-api-v2-lists-id-opt-in-settings-response
- name: GetApiV2ListsIdSubscribersResponse
  property_count: 2
  slug: tatango-get-api-v2-lists-id-subscribers-response
- name: GetBlackbaudV1EventsEventidItemsResponse
  property_count: 1
  slug: tatango-get-blackbaud-v1-events-eventid-items-response
- name: GetBlackbaudV1EventsEventidPurchasesResponse
  property_count: 1
  slug: tatango-get-blackbaud-v1-events-eventid-purchases-response
- name: GetSalesforceV1EventsEventidItemsResponse
  property_count: 1
  slug: tatango-get-salesforce-v1-events-eventid-items-response
jsonld:
- class_count: 22
  name: Tatango Context
  property_count: 14
  slug: tatango-context
layout: provider
modified: '2026-10-27'
name: Tatango
nav: Providers
network: true
overview: 'Tatango is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Fundraising, Non-Profit, and Marketing.


  The Tatango catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Tatango''s developer surface includes getting-started guide, API reference, documentation, engineering blog, pricing, support, and 24 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 5
  name: Tatango Rate Limits
  slug: tatango-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Tatango API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: tatango-rules
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 36.1
    developer_ergonomics: 17.9
    discoverability: 73.2
    operational_transparency: 52.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tatango/tatango-2026-11-03T144329.png
security:
- kind: domain-security
  name: Tatango Domain Security
  slug: tatango-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tatango Vulnerability Disclosure
  slug: tatango-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Tatango Trust Center
  slug: tatango-trust-center
  summary_line: GDPR
slug: tatango
tags:
- Company
- SMS
- Fundraising
- Non-Profit
- Marketing
website: https://tatango.com/
---
