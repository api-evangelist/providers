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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Mailfloss Agentic Access
  operation_count: 33
  slug: mailfloss-agentic-access
  summary_line: 33 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Account info, credits, API key management
  name: mailfloss Account API
  slug: mailfloss-account-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Asynchronous batch verification jobs
  name: mailfloss Batch API
  slug: mailfloss-batch-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: ESP connections — connect, list, manage, and configure email-platform integrations (incl. per-connection keyword rules)
  name: mailfloss Integrations API
  slug: mailfloss-integrations-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Data privacy / erasure API
  name: mailfloss Privacy API
  slug: mailfloss-privacy-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Verification usage analytics
  name: mailfloss Reports API
  slug: mailfloss-reports-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Organization members / seats
  name: mailfloss Team API
  slug: mailfloss-team-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Single-email verification endpoints
  name: mailfloss Verification API
  slug: mailfloss-verification-api
- baseURL: https://api.mailfloss.com
  baseurl_source: declared
  description: Webhook subscriptions — event notifications POSTed to your endpoints
  name: mailfloss Webhooks API
  slug: mailfloss-webhooks-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/mailfloss/agentic-access/mailfloss-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailfloss-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/mailfloss/rate-limits/mailfloss-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mailfloss-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mailfloss/plans/mailfloss-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailfloss-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/rules/mailfloss-rules.yml
  title: ''
  type: Spectral
  url: rules/mailfloss-rules.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/json-ld/mailfloss-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailfloss-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailfloss/vocabulary/mailfloss-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailfloss-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/data-model/mailfloss-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailfloss-data-model.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/conventions/mailfloss-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mailfloss-conventions.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/conventions/mailfloss-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mailfloss-conventions.yml
- group: auth
  href: https://artifacts.apis.io/mailfloss/security/mailfloss-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mailfloss-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailfloss/authentication/mailfloss-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailfloss-authentication.yml
- group: operate
  href: https://artifacts.apis.io/mailfloss/lifecycle/mailfloss-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mailfloss-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/lifecycle/mailfloss-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mailfloss-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/errors/mailfloss-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailfloss-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mailfloss/conformance/mailfloss-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailfloss-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mailfloss/llms/mailfloss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailfloss-llms.txt
- group: auth
  href: https://artifacts.apis.io/mailfloss/well-known/mailfloss-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailfloss-security.txt
- group: agent
  href: https://artifacts.apis.io/mailfloss/well-known/mailfloss-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailfloss-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailfloss/hosts/mailfloss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailfloss-hosts.yml
- group: other
  href: https://artifacts.apis.io/mailfloss/vendors/mailfloss-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailfloss-vendors.yml
- group: build
  href: https://artifacts.apis.io/mailfloss/packages/mailfloss-packages.yml
  title: ''
  type: Packages
  url: packages/mailfloss-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@mailfloss/sdk
- group: start
  title: ''
  type: Login
  url: https://app.mailfloss.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.mailfloss.com\
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailfloss
- group: auth
  href: https://artifacts.apis.io/mailfloss/security/mailfloss-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mailfloss-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailfloss/security/mailfloss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailfloss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailfloss.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mailfloss.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.mailfloss.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.mailfloss.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://status.mailfloss.com
- group: company
  title: ''
  type: Blog
  url: https://mailfloss.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://mailfloss.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailfloss.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailfloss.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developers.mailfloss.com/mcp
  - status: null
    url: https://api.mailfloss.com/swagger.json
  - status: 401
    url: https://api.mailfloss.com/mcp
  - status: 200
    url: https://mailfloss.com/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: mailfloss provides an automated email verification service that cleans email lists on autopilot, preventing bot sign‑ups, typos, and bounces. Founded to solve deliverability problems, it integrates with major ESPs, offers real‑time typo fixing, and supports teams of any size. The platform runs continuously, protecting sender reputation and reducing ad spend by ensuring only valid addresses remain in marketing lists.
image: https://mailfloss.com/og-default.png
jsonld:
- class_count: 1
  name: Mailfloss Context
  property_count: 1
  slug: mailfloss-context
layout: provider
modified: '2026-11-03'
name: mailfloss
nav: Providers
network: true
overview: 'mailfloss publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batch API, Integrations API, and 5 more. Tagged areas include Email Verification, Marketing, Software-as-a-Service, Automation, and Deliverability.


  The mailfloss catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mailfloss'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Mailfloss Plans Pricing
  plan_count: 3
  slug: mailfloss-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Mailfloss Rate Limits
  slug: mailfloss-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: mailfloss API Rules
  rule_count: 62
  severity_counts:
    error: 55
    hint: 0
    info: 3
    warn: 4
  slug: mailfloss-rules
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 56.1
    developer_ergonomics: 41.7
    discoverability: 66.1
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mailfloss Authentication
  slug: mailfloss-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mailfloss Domain Security
  slug: mailfloss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mailfloss Vulnerability Disclosure
  slug: mailfloss-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mailfloss
tags:
- Email Verification
- Marketing
- Software-as-a-Service
- Automation
- Deliverability
website: https://mailfloss.com/
---
