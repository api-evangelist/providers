---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Uetr Ai Agentic Access
  operation_count: 33
  slug: uetr-ai-agentic-access
  summary_line: 33 operations · 19 acting
api_count: 1
apis:
- description: Track international bank transfers by their UETR and read what the banks report about them.
  name: uetr.ai API
  slug: uetr-ai-api
- baseURL: https://uetr.ai/api/v1
  baseurl_source: declared
  description: The Account API from SWIFT UETR Tracker — 4 operation(s) for account.
  name: SWIFT UETR Tracker Account API
  slug: uetr-ai-account-api
- baseURL: https://uetr.ai/api/v1
  baseurl_source: declared
  description: The Owner confirmation API from SWIFT UETR Tracker — 1 operation(s) for owner confirmation.
  name: SWIFT UETR Tracker Owner confirmation API
  slug: uetr-ai-owner-confirmation-api
- baseURL: https://uetr.ai/api/v1
  baseurl_source: declared
  description: The Payment records API from SWIFT UETR Tracker — 1 operation(s) for payment records.
  name: SWIFT UETR Tracker Payment records API
  slug: uetr-ai-payment-records-api
- baseURL: https://uetr.ai/api/v1
  baseurl_source: declared
  description: The Team API from SWIFT UETR Tracker — 5 operation(s) for team.
  name: SWIFT UETR Tracker Team API
  slug: uetr-ai-team-api
- baseURL: https://uetr.ai/api/v1
  baseurl_source: declared
  description: The Transfers API from SWIFT UETR Tracker — 11 operation(s) for transfers.
  name: SWIFT UETR Tracker Transfers API
  slug: uetr-ai-transfers-api
- baseURL: https://uetr.ai/api/v1
  baseurl_source: declared
  description: The Webhooks API from SWIFT UETR Tracker — 6 operation(s) for webhooks.
  name: SWIFT UETR Tracker Webhooks API
  slug: uetr-ai-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Uetr Ai Webhooks
  slug: uetr-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/uetr-ai/agentic-access/uetr-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/uetr-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/uetr-ai/rate-limits/uetr-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/uetr-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/uetr-ai/plans/uetr-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uetr-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/rules/uetr-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/uetr-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/json-ld/uetr-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/uetr-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/uetr-ai/vocabulary/uetr-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/uetr-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/uetr-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/asyncapi/uetr-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uetr-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/data-model/uetr-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uetr-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/uetr-ai/changelog/uetr-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uetr-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/conventions/uetr-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uetr-ai-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://uetr.ai/terms
- group: auth
  href: https://artifacts.apis.io/uetr-ai/authentication/uetr-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uetr-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/errors/uetr-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uetr-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uetr-ai/conformance/uetr-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uetr-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/uetr-ai/llms/uetr-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uetr-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/uetr-ai/well-known/uetr-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uetr-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/uetr-ai/well-known/uetr-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uetr-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/uetr-ai/hosts/uetr-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uetr-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/uetr-ai/vendors/uetr-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uetr-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uetr.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uetr.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://uetr.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://uetr.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://uetr.ai/docs/api/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://uetr.ai/mcp
- group: auth
  href: https://artifacts.apis.io/uetr-ai/security/uetr-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/uetr-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/uetr-ai/security/uetr-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uetr-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uetr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://uetr.ai/docs/api
created: '2026-11-05'
description: UETR.ai provides a SWIFT payment tracking service that allows financial institutions and businesses to monitor the status of international wire transfers using the Unique End-to-Transaction Reference (UETR). The platform offers real‑time visibility into GPI payment progress, detailed transaction metadata, and alerts for delays or issues. It includes a RESTful API for creating, querying, and managing transfer records, as well as webhook notifications for status changes. Documentation, pricing, and support resources are publicly available.
image: https://img.uetr.ai/diagrams/how-to-track-swift-transfer-by-uetr-og.png
jsonld:
- class_count: 1
  name: Uetr Ai Context
  property_count: 11
  slug: uetr-ai-context
layout: provider
modified: '2026-11-05'
name: SWIFT UETR Tracker
nav: Providers
network: true
overview: 'SWIFT UETR Tracker publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Owner confirmation API, Payment records API, and 4 more. Tagged areas include Payments, SWIFT, Tracking, and Financial Services.


  The SWIFT UETR Tracker catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SWIFT UETR Tracker''s developer surface includes changelog, authentication, pricing, getting-started guide, documentation, and 25 more developer resources.'
plans:
- name: Uetr Ai Plans Pricing
  plan_count: 3
  slug: uetr-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 9
  name: Uetr Ai Rate Limits
  slug: uetr-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: SWIFT UETR Tracker API Rules
  rule_count: 64
  severity_counts:
    error: 59
    hint: 0
    info: 2
    warn: 3
  slug: uetr-ai-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 24.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 65.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Uetr Ai Authentication
  slug: uetr-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Uetr Ai Domain Security
  slug: uetr-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uetr Ai Vulnerability Disclosure
  slug: uetr-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: uetr-ai-create-and-retrieve-transfer
  slug: uetr-ai-create-and-retrieve-transfer
- name: uetr-ai-invite-team-member
  slug: uetr-ai-invite-team-member
- name: uetr-ai-setup-webhook
  slug: uetr-ai-setup-webhook
slug: uetr-ai
tags:
- Payments
- SWIFT
- Tracking
- Financial Services
website: https://uetr.ai/
---
