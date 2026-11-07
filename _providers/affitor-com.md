---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Affitor Com Agentic Access
  operation_count: 1
  slug: affitor-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.affitor.com
  baseurl_source: declared
  description: Click, lead, sale, and refund tracking
  name: Affitor Tracking API
  slug: affitor-com-tracking-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/affitor-com/data-model/affitor-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/affitor-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/affitor-com/agentic-access/affitor-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/affitor-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/affitor-com/plans/affitor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affitor-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/affitor-com/rules/affitor-com-rules.yml
  title: ''
  type: Spectral
  url: rules/affitor-com-rules.yml
- group: design
  href: https://artifacts.apis.io/affitor-com/vocabulary/affitor-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/affitor-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/affitor-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/affitor-com/cli/affitor-com-cli.yml
  title: ''
  type: CLI
  url: cli/affitor-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/affitor-com/changelog/affitor-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/affitor-com-changelog.yml
- group: start
  href: https://artifacts.apis.io/affitor-com/sandbox/affitor-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/affitor-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/affitor-com/authentication/affitor-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/affitor-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/affitor-com/conformance/affitor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affitor-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/affitor-com/llms/affitor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affitor-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/affitor-com/well-known/affitor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affitor-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/affitor-com/hosts/affitor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/affitor-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/affitor-com/vendors/affitor-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/affitor-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://affitor.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://affitor.com/changelog
- group: auth
  href: https://artifacts.apis.io/affitor-com/security/affitor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affitor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affitor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://affitor.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://affitor.com/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://affitor.com/docs/brand/quickstart
- group: operate
  title: ''
  type: Support
  url: https://affitor.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://affitor.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://affitor.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://affitor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://affitor.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://affitor.com/openapi.json
  - status: null
    url: https://docs.affitor.com/openapi.yaml
  - status: 401
    url: https://api.affitor.com/mcp
  - status: 200
    url: https://affitor.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Affitor is an AI‑native affiliate network designed for SaaS companies. It enables brands to run affiliate programs where partners can promote their products and get paid based on actual sales, not just clicks. The platform integrates with Stripe for real‑time tracking, supports payouts via Wise or bank transfers, and offers a suite of APIs and SDKs for developers to embed affiliate functionality directly into their applications. Affitor provides comprehensive documentation, a developer portal, and tools for partners to manage campaigns, track performance, and handle tax compliance.
image: https://affitor.com/api/og?title=Affitor&description=AI-Native%20Affiliate%20Network%20for%20SaaS&path=/
json_schemas:
- name: ClickRequest
  property_count: 0
  slug: affitor-com-click-request
- name: ClickResponse
  property_count: 0
  slug: affitor-com-click-response
- name: TestModeResponse
  property_count: 0
  slug: affitor-com-test-mode-response
layout: provider
modified: '2026-10-31'
name: Affitor
nav: Providers
network: true
overview: 'Affitor publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Tracking API. Tagged areas include Affiliates, Software-as-a-Service, Artificial Intelligence, Marketing, and Affiliate Network.


  The Affitor catalog on APIs.io includes 1 Spectral governance ruleset.


  Affitor''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 20 more developer resources.'
plans:
- name: Affitor Com Plans Pricing
  plan_count: 2
  slug: affitor-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Affitor API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: affitor-com-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 53.3
    developer_ergonomics: 50.5
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Affitor Com Authentication
  slug: affitor-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Affitor Com Domain Security
  slug: affitor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affitor-com
tags:
- Affiliates
- Software-as-a-Service
- Artificial Intelligence
- Marketing
- Affiliate Network
website: https://affitor.com/
---
