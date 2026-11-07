---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Soundcheck Live platform, providing endpoints for crew management, scheduling, and event operations.
  name: Soundcheck Live API
  slug: soundcheck-live-api
- description: 'soundchecklive-io API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: soundchecklive-io API
  slug: soundchecklive-io-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/soundchecklive-io/plans/soundchecklive-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/soundchecklive-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/soundchecklive-io/rules/soundchecklive-io-rules.yml
  title: ''
  type: Spectral
  url: rules/soundchecklive-io-rules.yml
- group: design
  href: https://artifacts.apis.io/soundchecklive-io/json-ld/soundchecklive-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/soundchecklive-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/soundchecklive-io/vocabulary/soundchecklive-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/soundchecklive-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/soundchecklive-io/data-model/soundchecklive-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/soundchecklive-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/soundchecklive-io/changelog/soundchecklive-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/soundchecklive-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/soundchecklive-io/conformance/soundchecklive-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/soundchecklive-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/soundchecklive-io/llms/soundchecklive-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soundchecklive-io-llms.txt
- group: other
  href: https://artifacts.apis.io/soundchecklive-io/a2a/soundchecklive-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/soundchecklive-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/soundchecklive-io/mcp/soundchecklive-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/soundchecklive-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/soundchecklive-io/well-known/soundchecklive-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/soundchecklive-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/soundchecklive-io/hosts/soundchecklive-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soundchecklive-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/soundchecklive-io/vendors/soundchecklive-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soundchecklive-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soundchecklive.io
- group: auth
  title: ''
  type: Security
  url: https://soundchecklive.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://soundchecklive.io/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.soundchecklive.io/changelog
- group: auth
  href: https://artifacts.apis.io/soundchecklive-io/security/soundchecklive-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soundchecklive-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soundchecklive.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soundchecklive.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.soundchecklive.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.soundchecklive.io/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://soundchecklive.io/support
- group: company
  title: ''
  type: Blog
  url: https://soundchecklive.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://soundchecklive.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soundchecklive.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soundchecklive.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://docs.soundchecklive.io/getting-started/signup-and-org-setup.md
coverage:
  checked: '2026-10-30'
  detail: The public documentation is readable but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://docs.soundchecklive.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Soundcheck Live provides crew management and event staffing software for live events, enabling production companies, entertainment agencies, and bands to coordinate crews, equipment, venues, and show schedules from load‑in through settlement. Built by musicians for the live‑events ecosystem, the platform offers scheduling, run‑of‑show sharing, payment processing, and a unified workspace to streamline operations and grow careers.
image: https://soundchecklive.io/soundcheck-logo-whites.png
json_schemas:
- name: PostApiV1OrganizationsOrgidImportsUefRequest
  property_count: 1
  slug: soundchecklive-io-post-api-v1-organizations-orgid-imports-uef-request
- name: PostApiV1OrganizationsOrgidImportsUefResponse
  property_count: 1
  slug: soundchecklive-io-post-api-v1-organizations-orgid-imports-uef-response
jsonld:
- class_count: 2
  name: Soundchecklive Io Context
  property_count: 2
  slug: soundchecklive-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.soundchecklive.io.
  name: soundchecklive-io MCP Server
  slug: soundchecklive-io-mcp-yml
modified: '2026-10-30'
name: soundchecklive-io
nav: Providers
network: true
overview: 'soundchecklive-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Crew Management, Live Events, Software, Entertainment, and Scheduling.


  The soundchecklive-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  soundchecklive-io''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Soundchecklive Io Plans Pricing
  plan_count: 4
  slug: soundchecklive-io-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Soundchecklive Io Rate Limits
  slug: soundchecklive-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: soundchecklive-io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: soundchecklive-io-rules
scopes:
- name: Soundchecklive Io Scopes
  scope_count: 0
  slug: soundchecklive-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 17.9
    discoverability: 67.5
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/soundchecklive-io/soundchecklive-io-2026-11-03T143546.png
security:
- kind: authentication
  name: Soundchecklive Io Authentication
  slug: soundchecklive-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Soundchecklive Io Domain Security
  slug: soundchecklive-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: soundchecklive-io
tags:
- Crew Management
- Live Events
- Software
- Entertainment
- Scheduling
website: https://soundchecklive.io/
---
