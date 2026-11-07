---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Open-source email API for sending transactional emails and managing inboxes.
  name: e2a.dev Email API
  slug: e2a-dev-email-api
- baseURL: https://api.e2a.dev
  baseurl_source: declared
  description: e2a — authenticated email gateway for AI agents. v1 contract.
  name: e2a API API
  slug: e2a-api-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/e2a-dev/rules/e2a-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/e2a-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/e2a-dev/json-ld/e2a-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/e2a-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/e2a-dev/vocabulary/e2a-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/e2a-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/e2a-dev/conformance/e2a-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/e2a-dev-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/e2a-dev/plans/e2a-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/e2a-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/e2a-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/e2a-dev/data-model/e2a-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/e2a-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/e2a-dev/conventions/e2a-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/e2a-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/e2a-dev/conventions/e2a-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/e2a-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/e2a-dev/authentication/e2a-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/e2a-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/e2a-dev/errors/e2a-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/e2a-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/e2a-dev/llms/e2a-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e2a-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/e2a-dev/well-known/e2a-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/e2a-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/e2a-dev/hosts/e2a-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e2a-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/e2a-dev/vendors/e2a-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/e2a-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/e2a-dev/packages/e2a-dev-packages.yml
  title: ''
  type: Packages
  url: packages/e2a-dev-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@e2a/sdk
- group: auth
  href: https://artifacts.apis.io/e2a-dev/security/e2a-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e2a-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://e2a.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://e2a.dev/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://e2a.dev/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://e2a.dev/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://e2a.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://e2a.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokencanopy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tokencanopy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://e2a.dev/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://e2a.dev/openapi.yaml
  - status: null
    url: https://staging.e2a.dev/v1/openapi.json
  - status: null
    url: https://api.e2a.dev/v1/openapi.json
  - status: 401
    url: https://api.e2a.dev/mcp
  - status: 200
    url: https://e2a.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: e2a.dev provides an open-source email API designed for applications and AI agents. It enables sending transactional emails, managing two-way inboxes, and integrating email workflows into products. Available as a hosted service or self‑hosted under Apache‑2.0, it targets developers, agent‑native teams, and businesses seeking flexible, privacy‑focused email solutions.
image: https://e2a.dev/og-image.png
json_schemas:
- name: ContactEngagementView
  property_count: 18
  slug: e2a-dev-contact-engagement-view
- name: ForwardRequest
  property_count: 10
  slug: e2a-dev-forward-request
- name: MessageView
  property_count: 33
  slug: e2a-dev-message-view
- name: ReplyRequest
  property_count: 11
  slug: e2a-dev-reply-request
- name: SendEmailRequest
  property_count: 14
  slug: e2a-dev-send-email-request
- name: VerifyDomainView
  property_count: 6
  slug: e2a-dev-verify-domain-view
jsonld:
- class_count: 120
  name: E2A Dev Context
  property_count: 303
  slug: e2a-dev-context
layout: provider
modified: '2026-10-30'
name: e2a-dev
nav: Providers
network: true
overview: 'e2a-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including e2a API API, and 1 more. Tagged areas include Company, Email, Open Source, and Artificial Intelligence.


  The e2a-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  e2a-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: E2A Dev Plans Pricing
  plan_count: 4
  slug: e2a-dev-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: e2a-dev API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: e2a-dev-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 57.3
    developer_ergonomics: 41.0
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 54.7
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/e2a-dev/e2a-dev-2026-11-03T131153.png
security:
- kind: authentication
  name: E2A Dev Authentication
  slug: e2a-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: E2A Dev Domain Security
  slug: e2a-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: e2a-dev
tags:
- Company
- Email
- Open Source
- Artificial Intelligence
website: https://e2a.dev/
---
