---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
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
  score: 41.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Coverwhaleinsurancesolutions Agentic Access
  operation_count: 43
  slug: coverwhaleinsurancesolutions-agentic-access
  summary_line: 43 operations · 28 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: Authenticating & Interacting with the API
  name: Cover Whale Authentication API
  slug: coverwhaleinsurancesolutions-authentication-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Binding API from Cover Whale — 1 operation(s) for binding.
  name: Cover Whale Binding API
  slug: coverwhaleinsurancesolutions-binding-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Policy Lifecycle API from Cover Whale — 7 operation(s) for policy lifecycle.
  name: Cover Whale Policy Lifecycle API
  slug: coverwhaleinsurancesolutions-policy-lifecycle-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Quoting API from Cover Whale — 5 operation(s) for quoting.
  name: Cover Whale Quoting API
  slug: coverwhaleinsurancesolutions-quoting-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Reference Data API from Cover Whale — 1 operation(s) for reference data.
  name: Cover Whale Reference Data API
  slug: coverwhaleinsurancesolutions-reference-data-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Submission Data API from Cover Whale — 13 operation(s) for submission data.
  name: Cover Whale Submission Data API
  slug: coverwhaleinsurancesolutions-submission-data-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Submissions API from Cover Whale — 4 operation(s) for submissions.
  name: Cover Whale Submissions API
  slug: coverwhaleinsurancesolutions-submissions-api
- baseURL: https://api.coverwhale.dev/v1
  baseurl_source: declared
  description: The Webhooks API from Cover Whale — 3 operation(s) for webhooks.
  name: Cover Whale Webhooks API
  slug: coverwhaleinsurancesolutions-webhooks-api
artifact_total: 23
asyncapis:
- description: ''
  name: Coverwhaleinsurancesolutions Webhooks
  slug: coverwhaleinsurancesolutions-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/agentic-access/coverwhaleinsurancesolutions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coverwhaleinsurancesolutions-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/rate-limits/coverwhaleinsurancesolutions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coverwhaleinsurancesolutions-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/rules/coverwhaleinsurancesolutions-rules.yml
  title: ''
  type: Spectral
  url: rules/coverwhaleinsurancesolutions-rules.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/json-ld/coverwhaleinsurancesolutions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coverwhaleinsurancesolutions-context.jsonld
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/vocabulary/coverwhaleinsurancesolutions-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coverwhaleinsurancesolutions-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/asyncapi/coverwhaleinsurancesolutions-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coverwhaleinsurancesolutions-webhooks.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/data-model/coverwhaleinsurancesolutions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coverwhaleinsurancesolutions-data-model.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/conventions/coverwhaleinsurancesolutions-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coverwhaleinsurancesolutions-conventions.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/conventions/coverwhaleinsurancesolutions-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coverwhaleinsurancesolutions-conventions.yml
- group: start
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/sandbox/coverwhaleinsurancesolutions-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/coverwhaleinsurancesolutions-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/security/coverwhaleinsurancesolutions-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/coverwhaleinsurancesolutions-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/lifecycle/coverwhaleinsurancesolutions-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/coverwhaleinsurancesolutions-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/lifecycle/coverwhaleinsurancesolutions-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coverwhaleinsurancesolutions-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/errors/coverwhaleinsurancesolutions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coverwhaleinsurancesolutions-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/conformance/coverwhaleinsurancesolutions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coverwhaleinsurancesolutions-conformance.yml
- group: other
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/overlays/coverwhaleinsurancesolutions-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coverwhaleinsurancesolutions-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/llms/coverwhaleinsurancesolutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coverwhaleinsurancesolutions-llms.txt
- group: other
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/a2a/coverwhaleinsurancesolutions-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coverwhaleinsurancesolutions-a2a.yml
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/well-known/coverwhaleinsurancesolutions-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coverwhaleinsurancesolutions-security.txt
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/well-known/coverwhaleinsurancesolutions-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coverwhaleinsurancesolutions-app-security.txt
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/well-known/coverwhaleinsurancesolutions-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coverwhaleinsurancesolutions-api-security.txt
- group: agent
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/well-known/coverwhaleinsurancesolutions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coverwhaleinsurancesolutions-well-known.yml
- group: build
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/packages/coverwhaleinsurancesolutions-packages.yml
  title: ''
  type: SDKs
  url: packages/coverwhaleinsurancesolutions-packages.yml
- group: build
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/packages/coverwhaleinsurancesolutions-packages.yml
  title: ''
  type: Packages
  url: packages/coverwhaleinsurancesolutions-packages.yml
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/authentication/coverwhaleinsurancesolutions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coverwhaleinsurancesolutions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coverwhale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coverwhale.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coverwhale.com/api-reference/authentication/check-api-health
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coverwhale.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://coverwhale.com/brokers/signup
- group: start
  title: ''
  type: Login
  url: https://app.coverwhale.com/login
- group: company
  title: ''
  type: Newsroom
  url: https://coverwhale.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coverwhale.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coverwhale.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoverWhale
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/security/coverwhaleinsurancesolutions-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coverwhaleinsurancesolutions-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/hosts/coverwhaleinsurancesolutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coverwhaleinsurancesolutions-hosts.yml
- group: other
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/vendors/coverwhaleinsurancesolutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coverwhaleinsurancesolutions-vendors.yml
- group: auth
  href: https://artifacts.apis.io/coverwhaleinsurancesolutions/security/coverwhaleinsurancesolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coverwhaleinsurancesolutions-domain-security.yml
created: '2026-10-11'
description: Cover Whale is a commercial auto insurtech that quotes, binds, and issues policies through an always-on underwriting engine called DriveSmart. The platform pre-fills DOT and fleet data, pulls real-time driver and vehicle records, analyzes telematics for safety trends, and reviews loss runs so brokers can produce a bindable quote in an average of eighteen minutes rather than two to five days. It pairs instant policy issuance with continuous underwriting, digital driver coaching for more than sixteen thousand drivers, and A-rated carrier partnerships. The company (legally Cover Whale Insurance Solutions, founded 2019) publishes a public REST API at docs.coverwhale.com covering authentication, quoting, submissions, policy lifecycle, endorsements, and webhook subscriptions.
image: https://coverwhale.com/og-image.png
json_schemas:
- name: CancellationNoticeDecision
  property_count: 29
  slug: coverwhaleinsurancesolutions-cancellation-notice-decision
jsonld:
- class_count: 4
  name: Coverwhaleinsurancesolutions Context
  property_count: 39
  slug: coverwhaleinsurancesolutions-context
layout: provider
modified: '2026-11-04'
name: Cover Whale
nav: Providers
network: true
overview: 'Cover Whale publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Binding API, Policy Lifecycle API, and 5 more. Tagged areas include Insurance, Commercial Auto Insurance, Insurtech, Underwriting, and Telematics.


  The Cover Whale catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cover Whale''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, signup flow, and 34 more developer resources.'
plans:
- name: Coverwhaleinsurancesolutions Plans Pricing
  plan_count: 0
  slug: coverwhaleinsurancesolutions-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Coverwhaleinsurancesolutions Rate Limits
  slug: coverwhaleinsurancesolutions-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Cover Whale API Rules
  rule_count: 61
  severity_counts:
    error: 48
    hint: 0
    info: 4
    warn: 9
  slug: coverwhaleinsurancesolutions-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.2
    catalog_earned_first_party: 12.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 45.2
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 69.2
    developer_ergonomics: 36.3
    discoverability: 67.0
    operational_transparency: 56.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 23.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coverwhaleinsurancesolutions Authentication
  slug: coverwhaleinsurancesolutions-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Coverwhaleinsurancesolutions Domain Security
  slug: coverwhaleinsurancesolutions-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coverwhaleinsurancesolutions Vulnerability Disclosure
  slug: coverwhaleinsurancesolutions-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: bind-a-quoted-policy
  slug: coverwhaleinsurancesolutions-bind-a-quoted-policy
- name: cancel-or-reinstate-a-policy
  slug: coverwhaleinsurancesolutions-cancel-or-reinstate-a-policy
- name: create-a-mid-term-endorsement
  slug: coverwhaleinsurancesolutions-create-a-mid-term-endorsement
- name: manage-webhook-subscriptions
  slug: coverwhaleinsurancesolutions-manage-webhook-subscriptions
- name: quote-a-commercial-auto-submission
  slug: coverwhaleinsurancesolutions-quote-a-commercial-auto-submission
slug: coverwhaleinsurancesolutions
tags:
- Insurance
- Commercial Auto Insurance
- Insurtech
- Underwriting
- Telematics
- Risk Management
- Fleet Safety
- Policy Lifecycle
- Webhook
- Company
website: https://coverwhale.com/
---
