---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Autohost Agentic Access
  operation_count: 96
  slug: autohost-agentic-access
  summary_line: 96 operations · 30 acting
api_count: 1
apis:
- description: The Accounts API from Autohost — 7 operation(s) for accounts.
  name: Autohost Accounts API
  slug: autohost-accounts-api
- description: The Background Check API from Autohost — 2 operation(s) for background check.
  name: Autohost Background Check API
  slug: autohost-background-check-api
- description: The Fraud API from Autohost — 1 operation(s) for fraud.
  name: Autohost Fraud API
  slug: autohost-fraud-api
- description: The Idcheck API from Autohost — 3 operation(s) for idcheck.
  name: Autohost Idcheck API
  slug: autohost-idcheck-api
- description: The Listings API from Autohost — 4 operation(s) for listings.
  name: Autohost Listings API
  slug: autohost-listings-api
- description: The Lookup API from Autohost — 12 operation(s) for lookup.
  name: Autohost Lookup API
  slug: autohost-lookup-api
- description: The Reservations API from Autohost — 11 operation(s) for reservations.
  name: Autohost Reservations API
  slug: autohost-reservations-api
- description: The Validate API from Autohost — 2 operation(s) for validate.
  name: Autohost Validate API
  slug: autohost-validate-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/autohost/capabilities/autohost-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/autohost-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/autohost/agentic-access/autohost-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/autohost-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/autohost/rules/autohost-rules.yml
  title: ''
  type: Spectral
  url: rules/autohost-rules.yml
- group: design
  href: https://artifacts.apis.io/autohost/json-ld/autohost-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autohost-context.jsonld
- group: design
  href: https://artifacts.apis.io/autohost/vocabulary/autohost-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autohost-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/autohost/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/autohost/data-model/autohost-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autohost-data-model.yml
- group: operate
  href: https://artifacts.apis.io/autohost/changelog/autohost-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/autohost-changelog.yml
- group: auth
  href: https://artifacts.apis.io/autohost/authentication/autohost-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autohost-authentication.yml
- group: design
  href: https://artifacts.apis.io/autohost/errors/autohost-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autohost-problem-types.yml
- group: design
  href: https://artifacts.apis.io/autohost/conformance/autohost-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autohost-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autohost/llms/autohost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autohost-llms.txt
- group: other
  href: https://artifacts.apis.io/autohost/hosts/autohost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autohost-hosts.yml
- group: other
  href: https://artifacts.apis.io/autohost/vendors/autohost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autohost-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autohost.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.autohost.ai/docs/category/reference
- group: auth
  href: https://artifacts.apis.io/autohost/security/autohost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autohost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autohost.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.autohost.ai/knowledge
- group: commercial
  title: ''
  type: Pricing
  url: https://www.autohost.ai/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autohost.ai/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.autohost.ai/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AutohostAI/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.autohost.ai/knowledge/getting-started?hsLang=en
created: '2026-10-28'
description: Autohost provides AI-powered identity verification, background checks, credit history verification, and fraud detection services tailored for the hospitality and real‑estate sectors. Their platform offers a suite of APIs that enable businesses to integrate secure guest screening, touchless verification, and risk assessment into property‑management systems, with flexible, usage‑based pricing and comprehensive privacy and support resources.
image: https://www.autohost.ai/images/social.jpg
json_schemas:
- name: BackgroundCheckResultsResponse
  property_count: 8
  slug: autohost-background-check-results-response
- name: PaymentEventRequest
  property_count: 32
  slug: autohost-payment-event-request
- name: ReservationCreateRequest
  property_count: 11
  slug: autohost-reservation-create-request
- name: ReservationPaymentsResponse
  property_count: 4
  slug: autohost-reservation-payments-response
- name: ReservationScreensResponse
  property_count: 22
  slug: autohost-reservation-screens-response
- name: ReservationSummaryResponse
  property_count: 11
  slug: autohost-reservation-summary-response
jsonld:
- class_count: 48
  name: Autohost Context
  property_count: 176
  slug: autohost-context
layout: provider
modified: '2026-10-28'
name: Autohost
nav: Providers
network: true
overview: 'Autohost publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Background Check API, Fraud API, and 5 more. Tagged areas include Company, Identity Verification, Background Checks, Fraud Prevention, and Hospitality.


  The Autohost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Autohost''s developer surface includes changelog, authentication, API reference, documentation, pricing, support, getting-started guide, and 17 more developer resources.'
plans:
- name: Autohost Plans Pricing
  plan_count: 0
  slug: autohost-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Autohost Rate Limits
  slug: autohost-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Autohost API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: autohost-rules
scopes:
- name: Autohost Scopes
  scope_count: 0
  slug: autohost-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 53.3
    developer_ergonomics: 35.0
    discoverability: 64.3
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/autohost/autohost-2026-11-03T121400.png
security:
- kind: authentication
  name: Autohost Authentication
  slug: autohost-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Autohost Domain Security
  slug: autohost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: create-listing
  slug: autohost-create-listing
slug: autohost
tags:
- Company
- Identity Verification
- Background Checks
- Fraud Prevention
- Hospitality
- Real Estate
website: https://www.autohost.ai/
---
