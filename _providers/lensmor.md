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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: unknown
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Lensmor Agentic Access
  operation_count: 31
  slug: lensmor-agentic-access
  summary_line: 31 operations · 11 acting
api_count: 1
apis:
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Preflight access and credit-sensitive actions before executing them.
  name: Lensmor Actions API
  slug: lensmor-actions-api
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Search contacts and run asynchronous email or phone unlock workflows.
  name: Lensmor Contacts API
  slug: lensmor-contacts-api
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Inspect the credit balance available to the authenticated API key owner.
  name: Lensmor Credits API
  slug: lensmor-credits-api
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Discover, inspect, score, rank, and unlock trade show event records.
  name: Lensmor Events API
  slug: lensmor-events-api
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Search and inspect exhibiting companies and their related events.
  name: Lensmor Exhibitors API
  slug: lensmor-exhibitors-api
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Browse event personnel, related events, LinkedIn activity, and outreach content.
  name: Lensmor Personnel API
  slug: lensmor-personnel-api
- baseURL: https://platform.lensmor.com
  baseurl_source: declared
  description: Apply a buyer profile to rank events and recommend exhibitors.
  name: Lensmor Profile Matching API
  slug: lensmor-profile-matching-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/lensmor/agentic-access/lensmor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lensmor-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lensmor/rate-limits/lensmor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lensmor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lensmor/plans/lensmor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lensmor-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lensmor/rules/lensmor-rules.yml
  title: ''
  type: Spectral
  url: rules/lensmor-rules.yml
- group: design
  href: https://artifacts.apis.io/lensmor/json-ld/lensmor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lensmor-context.jsonld
- group: design
  href: https://artifacts.apis.io/lensmor/vocabulary/lensmor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lensmor-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lensmor/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lensmor/data-model/lensmor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lensmor-data-model.yml
- group: design
  href: https://artifacts.apis.io/lensmor/conventions/lensmor-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lensmor-conventions.yml
- group: design
  href: https://artifacts.apis.io/lensmor/conventions/lensmor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lensmor-conventions.yml
- group: auth
  href: https://artifacts.apis.io/lensmor/authentication/lensmor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lensmor-authentication.yml
- group: design
  href: https://artifacts.apis.io/lensmor/lifecycle/lensmor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lensmor-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lensmor/errors/lensmor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lensmor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lensmor/conformance/lensmor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lensmor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lensmor/llms/lensmor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lensmor-llms.txt
- group: other
  href: https://artifacts.apis.io/lensmor/a2a/lensmor-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lensmor-a2a.yml
- group: agent
  href: https://artifacts.apis.io/lensmor/mcp/lensmor-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lensmor-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lensmor/well-known/lensmor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lensmor-well-known.yml
- group: other
  href: https://artifacts.apis.io/lensmor/hosts/lensmor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lensmor-hosts.yml
- group: other
  href: https://artifacts.apis.io/lensmor/vendors/lensmor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lensmor-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.lensmor.com/integration/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lensmor.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.lensmor.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lensmor.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.lensmor.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://api.lensmor.com/guides/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://api.lensmor.com/api-reference/credits/get-credits-balance
- group: auth
  href: https://artifacts.apis.io/lensmor/security/lensmor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lensmor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lensmor.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.lensmor.com
- group: operate
  title: ''
  type: Support
  url: https://help.lensmor.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lensmor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LensmorOfficial
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lensmor.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.lensmor.com/request-a-demo
created: '2026-11-02'
description: Lensmor is a pre‑show event intelligence platform that helps B2B revenue teams turn event audience data into high‑intent prospects and pipeline. It provides exhibitor, social‑signal attendee, and visitor intelligence to find the right B2B events and decision‑makers, enabling focused outreach before shows. The platform aggregates event footprints, ICP matching, and contact enrichment to deliver actionable leads for trade‑show marketing.
image: https://cdn.prod.website-files.com/691bdb22805dbb6a57758d15/691bde9132ab7532c68b6f51_Logo-white.svg
json_schemas:
- name: ContactItem
  property_count: 17
  slug: lensmor-contact-item
- name: ContactUnlockSubmission
  property_count: 5
  slug: lensmor-contact-unlock-submission
- name: EventDetail
  property_count: 32
  slug: lensmor-event-detail
- name: EventFullAccessUnlockResult
  property_count: 8
  slug: lensmor-event-full-access-unlock-result
- name: EventItem
  property_count: 17
  slug: lensmor-event-item
- name: OutreachDetail
  property_count: 10
  slug: lensmor-outreach-detail
jsonld:
- class_count: 36
  name: Lensmor Context
  property_count: 134
  slug: lensmor-context
layout: provider
mcp_servers:
- description: Remote MCP server at platform.lensmor.com.
  name: Lensmor MCP Server
  slug: lensmor-mcp-yml
modified: '2026-11-02'
name: Lensmor
nav: Providers
network: true
overview: 'Lensmor publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Contacts API, Credits API, and 4 more. Tagged areas include Event-Intelligence, B2B, Software-as-a-Service, Lead Generation, and Trade Shows.


  The Lensmor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lensmor''s developer surface includes authentication, pricing, changelog, getting-started guide, API reference, documentation, support, and 28 more developer resources.'
plans:
- name: Lensmor Plans Pricing
  plan_count: 4
  slug: lensmor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Lensmor Rate Limits
  slug: lensmor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Lensmor API Rules
  rule_count: 64
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 5
  slug: lensmor-rules
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 65.5
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 40.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
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
- kind: authentication
  name: Lensmor Authentication
  slug: lensmor-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lensmor Domain Security
  slug: lensmor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lensmor
tags:
- Event-Intelligence
- B2B
- Software-as-a-Service
- Lead Generation
- Trade Shows
website: https://www.lensmor.com
---
