---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API providing program data, requires token authentication.
  name: BountyHunte.rs API
  slug: bountyhunte-rs-api-2
- description: 'BountyHunte.rs API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BountyHunte.rs API
  slug: bountyhunte-rs-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/bountyhunte-rs/plans/bountyhunte-rs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bountyhunte-rs-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bountyhunte-rs/rules/bountyhunte-rs-rules.yml
  title: ''
  type: Spectral
  url: rules/bountyhunte-rs-rules.yml
- group: design
  href: https://artifacts.apis.io/bountyhunte-rs/json-ld/bountyhunte-rs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bountyhunte-rs-context.jsonld
- group: design
  href: https://artifacts.apis.io/bountyhunte-rs/vocabulary/bountyhunte-rs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bountyhunte-rs-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bountyhunte-rs/data-model/bountyhunte-rs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bountyhunte-rs-data-model.yml
- group: design
  href: https://artifacts.apis.io/bountyhunte-rs/conformance/bountyhunte-rs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bountyhunte-rs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bountyhunte-rs/llms/bountyhunte-rs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bountyhunte-rs-llms.txt
- group: auth
  href: https://artifacts.apis.io/bountyhunte-rs/well-known/bountyhunte-rs-bsky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bountyhunte-rs-bsky-security.txt
- group: agent
  href: https://artifacts.apis.io/bountyhunte-rs/well-known/bountyhunte-rs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bountyhunte-rs-well-known.yml
- group: other
  href: https://artifacts.apis.io/bountyhunte-rs/hosts/bountyhunte-rs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bountyhunte-rs-hosts.yml
- group: other
  href: https://artifacts.apis.io/bountyhunte-rs/vendors/bountyhunte-rs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bountyhunte-rs-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bountyhunte.rs/
- group: auth
  title: ''
  type: Security
  url: https://bountyhunte.rs/programs/security
- group: auth
  href: https://artifacts.apis.io/bountyhunte-rs/security/bountyhunte-rs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bountyhunte-rs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bountyhunte.rs/
- group: docs
  title: ''
  type: Documentation
  url: https://bountyhunte.rs/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bountyhunte.rs/api/v1/programs
- group: commercial
  title: ''
  type: Pricing
  url: https://bountyhunte.rs/pricing
- group: company
  title: ''
  type: Blog
  url: https://bountyhunte.rs/blog
- group: operate
  title: ''
  type: Support
  url: https://bountyhunte.rs/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bountyhunte.rs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bountyhunte.rs/privacy
- group: start
  title: ''
  type: SignUp
  url: https://bountyhunte.rs/login
created: '2026-11-02'
description: BountyHunte.rs aggregates public bug bounty programs and audit contests from platforms like HackerOne, Bugcrowd, Immunefi, and others, providing a unified feed with reward, scope, and status updates. Users can filter programs, receive alerts via Slack, Discord, or webhooks, and access detailed program pages. The service offers free browsing with optional paid tiers for advanced filtering and notification limits, supporting multiple blockchain networks and traditional web security programs.
image: https://bountyhunte.rs/og-live.png?v=2
json_schemas:
- name: GetApiV1ProgramsResponse
  property_count: 2
  slug: bountyhunte-rs-get-api-v1-programs-response
- name: GetApiV1ProgramsSlugResponse
  property_count: 17
  slug: bountyhunte-rs-get-api-v1-programs-slug-response
jsonld:
- class_count: 2
  name: Bountyhunte Rs Context
  property_count: 19
  slug: bountyhunte-rs-context
layout: provider
modified: '2026-11-02'
name: BountyHunte.rs
nav: Providers
network: true
overview: 'BountyHunte.rs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bug Bounty, Security, Auditing, and Blockchain.


  The BountyHunte.rs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BountyHunte.rs'' developer surface includes documentation, API reference, pricing, engineering blog, support, signup flow, and 17 more developer resources.'
plans:
- name: Bountyhunte Rs Plans Pricing
  plan_count: 3
  slug: bountyhunte-rs-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: BountyHunte.rs API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: bountyhunte-rs-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 22.2
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bountyhunte Rs Domain Security
  slug: bountyhunte-rs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bountyhunte-rs
tags:
- Bug Bounty
- Security
- Auditing
- Blockchain
website: https://bountyhunte.rs/
---
