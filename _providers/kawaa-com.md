---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Kawaa Com Agentic Access
  operation_count: 38
  slug: kawaa-com-agentic-access
  summary_line: 38 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Plan, credits and usage.
  name: kawaa-com Account API
  slug: kawaa-com-account-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Engagement your own account's tracking has recorded for an address. Never another account's data.
  name: kawaa-com Activity API
  slug: kawaa-com-activity-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: The credentials that reach this API.
  name: kawaa-com API keys API
  slug: kawaa-com-api-keys-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Public plan and credit-pack prices.
  name: kawaa-com Catalogue API
  slug: kawaa-com-catalogue-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: How a domain is set up to send mail.
  name: kawaa-com Deliverability API
  slug: kawaa-com-deliverability-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Owned exports and scheduled-export requests.
  name: kawaa-com Exports API
  slug: kawaa-com-exports-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Is the API up.
  name: kawaa-com Health API
  slug: kawaa-com-health-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Follow asynchronous work and read its results.
  name: kawaa-com Jobs API
  slug: kawaa-com-jobs-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Find an address, or look at a domain.
  name: kawaa-com Search API
  slug: kawaa-com-search-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: Check whether an address can receive mail.
  name: kawaa-com Verification API
  slug: kawaa-com-verification-api
- baseURL: https://api.kawaa.com
  baseurl_source: declared
  description: 'Be told when work finishes instead of polling. **Verifying a delivery.** Every signed delivery carries `X-Kawaa-Signature-V2: t=<unix seconds>,v1=<hex>`. `t` is when that request was sent and `v1` is '
  name: kawaa-com Webhooks API
  slug: kawaa-com-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Kawaa Com Webhooks
  slug: kawaa-com-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://kawaa.com/docs/quickstart/
- group: agent
  href: https://artifacts.apis.io/kawaa-com/agentic-access/kawaa-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kawaa-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/kawaa-com/rate-limits/kawaa-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kawaa-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kawaa-com/plans/kawaa-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kawaa-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/rules/kawaa-com-rules.yml
  title: ''
  type: Spectral
  url: rules/kawaa-com-rules.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/json-ld/kawaa-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kawaa-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/kawaa-com/vocabulary/kawaa-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kawaa-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/kawaa-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/asyncapi/kawaa-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/kawaa-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/data-model/kawaa-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kawaa-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/conventions/kawaa-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kawaa-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/conventions/kawaa-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kawaa-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/kawaa-com/authentication/kawaa-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kawaa-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/errors/kawaa-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kawaa-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kawaa-com/conformance/kawaa-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kawaa-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kawaa-com/llms/kawaa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kawaa-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/kawaa-com/well-known/kawaa-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kawaa-com-status-security.txt
- group: auth
  href: https://artifacts.apis.io/kawaa-com/well-known/kawaa-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kawaa-com-security.txt
- group: auth
  href: https://artifacts.apis.io/kawaa-com/well-known/kawaa-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kawaa-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/kawaa-com/well-known/kawaa-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kawaa-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/kawaa-com/hosts/kawaa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kawaa-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kawaa-com/vendors/kawaa-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kawaa-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/kawaa-com/packages/kawaa-com-packages.yml
  title: ''
  type: SDKs
  url: packages/kawaa-com-packages.yml
- group: build
  href: https://artifacts.apis.io/kawaa-com/packages/kawaa-com-packages.yml
  title: ''
  type: Packages
  url: packages/kawaa-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://kawaa.com/integrations/webhooks/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kawaa.com
- group: auth
  title: ''
  type: Security
  url: https://kawaa.com/support/security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.kawaa.com</code
- group: auth
  href: https://artifacts.apis.io/kawaa-com/scopes/kawaa-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/kawaa-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/kawaa-com/security/kawaa-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kawaa-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kawaa-com/security/kawaa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kawaa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kawaa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kawaa.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://kawaa.com/docs/api/
- group: operate
  title: ''
  type: Support
  url: https://kawaa.com/support/
- group: company
  title: ''
  type: Blog
  url: https://kawaa.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://kawaa.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kawaa.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kawaa.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://kawaa.com/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://kawaa.com/openapi.json
  - status: 401
    url: https://api.kawaa.com/mcp
  - status: 403
    url: https://kawaa.com/mcp
  - status: 403
    url: https://app.kawaa.com/mcp
  - status: 403
    url: https://status.kawaa.com/mcp
  - status: 200
    url: https://kawaa.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Kawaa offers a comprehensive email verification and bulk validation platform tailored for developers, marketers, agencies, and SaaS teams. The service provides real‑time email address checks, list monitoring, and a robust playground for testing integrations. It includes SDKs for multiple languages, webhook notifications, and detailed documentation covering API reference, quick‑start guides, pricing, and support resources, enabling users to maintain high deliverability and clean mailing lists across their applications.
image: https://kawaa.com/og-image.png
json_schemas:
- name: Account
  property_count: 9
  slug: kawaa-com-account
- name: BatchAccepted
  property_count: 16
  slug: kawaa-com-batch-accepted
- name: DeliverabilityCheck
  property_count: 21
  slug: kawaa-com-deliverability-check
- name: Job
  property_count: 22
  slug: kawaa-com-job
- name: SubAccount
  property_count: 8
  slug: kawaa-com-sub-account
- name: VerificationResult
  property_count: 23
  slug: kawaa-com-verification-result
jsonld:
- class_count: 28
  name: Kawaa Com Context
  property_count: 132
  slug: kawaa-com-context
layout: provider
modified: '2026-10-30'
name: kawaa-com
nav: Providers
network: true
overview: 'kawaa-com publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Activity API, API keys API, and 8 more. Tagged areas include Company, Email Verification, Software-as-a-Service, and Marketing.


  The kawaa-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  kawaa-com''s developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Kawaa Com Plans Pricing
  plan_count: 5
  slug: kawaa-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Kawaa Com Rate Limits
  slug: kawaa-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: kawaa-com API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 5
  slug: kawaa-com-rules
scopes:
- name: Kawaa Com Scopes
  scope_count: 21
  slug: kawaa-com-scopes
  summary_line: 21 scopes · authorizationCode
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.7
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 73.8
    developer_ergonomics: 43.5
    discoverability: 57.1
    operational_transparency: 48.7
  previous_composite: 70.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kawaa-com/kawaa-com-2026-11-03T134334.png
security:
- kind: authentication
  name: Kawaa Com Authentication
  slug: kawaa-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kawaa Com Domain Security
  slug: kawaa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kawaa Com Vulnerability Disclosure
  slug: kawaa-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: kawaa-com-get-multiple-email-activity
  slug: kawaa-com-get-multiple-email-activity
- name: kawaa-com-job-retrieval
  slug: kawaa-com-job-retrieval
- name: kawaa-com-main
  slug: kawaa-com-main-skill
- name: kawaa-com-manage-webhook
  slug: kawaa-com-manage-webhook
- name: kawaa-com-run-export-schedule
  slug: kawaa-com-run-export-schedule
slug: kawaa-com
tags:
- Company
- Email Verification
- Software-as-a-Service
- Marketing
website: https://kawaa.com/
---
