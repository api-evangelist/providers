---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Amfionhq Com Agentic Access
  operation_count: 42
  slug: amfionhq-com-agentic-access
  summary_line: 42 operations · 24 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.amfionhq.com/v1/partner
  baseurl_source: declared
  description: The Fleet API from amfionhq-com — 3 operation(s) for fleet.
  name: amfionhq-com Fleet API
  slug: amfionhq-com-fleet-api
- baseURL: https://api.amfionhq.com/v1/partner
  baseurl_source: declared
  description: The Tenants API from amfionhq-com — 30 operation(s) for tenants.
  name: amfionhq-com Tenants API
  slug: amfionhq-com-tenants-api
- baseURL: https://api.amfionhq.com/v1/partner
  baseurl_source: declared
  description: The Tools API from amfionhq-com — 1 operation(s) for tools.
  name: amfionhq-com Tools API
  slug: amfionhq-com-tools-api
- baseURL: https://api.amfionhq.com/v1/partner
  baseurl_source: declared
  description: The Usage API from amfionhq-com — 1 operation(s) for usage.
  name: amfionhq-com Usage API
  slug: amfionhq-com-usage-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/amfionhq-com/agentic-access/amfionhq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amfionhq-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/amfionhq-com/plans/amfionhq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amfionhq-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/amfionhq-com/rules/amfionhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/amfionhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/amfionhq-com/json-ld/amfionhq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amfionhq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/amfionhq-com/vocabulary/amfionhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amfionhq-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amfionhq-com/data-model/amfionhq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amfionhq-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/amfionhq-com/changelog/amfionhq-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amfionhq-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/amfionhq-com/conventions/amfionhq-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/amfionhq-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/amfionhq-com/conventions/amfionhq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amfionhq-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://amfionhq.com/security
- group: design
  href: https://artifacts.apis.io/amfionhq-com/errors/amfionhq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amfionhq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amfionhq-com/conformance/amfionhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amfionhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amfionhq-com/llms/amfionhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amfionhq-com-llms.txt
- group: other
  href: https://artifacts.apis.io/amfionhq-com/hosts/amfionhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amfionhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/amfionhq-com/vendors/amfionhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amfionhq-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amfionhq.com/terms
- group: auth
  title: ''
  type: Security
  url: https://amfionhq.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amfionhq.com/privacy
- group: start
  title: ''
  type: Login
  url: https://amfionhq.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://amfionhq.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://amfionhq.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/amfionhq-com/authentication/amfionhq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amfionhq-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/amfionhq-com/security/amfionhq-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amfionhq-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amfionhq-com/security/amfionhq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amfionhq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amfionhq-com/security/amfionhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amfionhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amfionhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://amfionhq.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://amfionhq.com/try
- group: commercial
  title: ''
  type: Pricing
  url: https://amfionhq.com/ai-receptionist-pricing
- group: operate
  title: ''
  type: Support
  url: https://amfionhq.com/help/zapier
created: '2026-10-29'
description: Amfion provides an AI-powered front desk solution for bookable businesses, handling phone calls, texts, WhatsApp, email, and website chat. It offers a customizable widget, knowledge center, and booking integration with calendars and Stripe, enabling businesses to automate customer interactions, capture leads, and streamline appointments across various service industries.
image: https://amfionhq.com/og/amfion-og.png
json_schemas:
- name: FleetTenant
  property_count: 9
  slug: amfionhq-com-fleet-tenant
- name: RouteLeadRequest
  property_count: 8
  slug: amfionhq-com-route-lead-request
- name: RouteLeadResponse
  property_count: 6
  slug: amfionhq-com-route-lead-response
jsonld:
- class_count: 4
  name: Amfionhq Com Context
  property_count: 23
  slug: amfionhq-com-context
layout: provider
modified: '2026-10-29'
name: amfionhq-com
nav: Providers
network: true
overview: 'amfionhq-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Fleet API, Tenants API, Tools API, and 1 more. Tagged areas include Company, Artificial Intelligence, Front Desk, Booking, and Automation.


  The amfionhq-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  amfionhq-com''s developer surface includes changelog, API reference, authentication, documentation, getting-started guide, pricing, support, and 23 more developer resources.'
plans:
- name: Amfionhq Com Plans Pricing
  plan_count: 5
  slug: amfionhq-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: amfionhq-com API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: amfionhq-com-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.0
    catalog_earned_first_party: 12.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.2
  facets:
    access_clarity: 65.8
    contract_governance: 19.7
    contract_quality: 56.9
    developer_ergonomics: 28.6
    discoverability: 73.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/amfionhq-com/amfionhq-com-2026-11-03T120815.png
security:
- kind: authentication
  name: Amfionhq Com Authentication
  slug: amfionhq-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amfionhq Com Domain Security
  slug: amfionhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amfionhq Com Vulnerability Disclosure
  slug: amfionhq-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Amfionhq Com Trust Center
  slug: amfionhq-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: amfionhq-com
tags:
- Company
- Artificial Intelligence
- Front Desk
- Booking
- Automation
website: https://amfionhq.com/
---
