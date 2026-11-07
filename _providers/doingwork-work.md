---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Doingwork Work Agentic Access
  operation_count: 1
  slug: doingwork-work-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://app.doingwork.work
  baseurl_source: declared
  description: The status API from doingwork-work — 1 operation(s) for status.
  name: doingwork-work Status API
  slug: doingwork-work-status-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/doingwork-work/agentic-access/doingwork-work-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doingwork-work-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/doingwork-work/plans/doingwork-work-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doingwork-work-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/doingwork-work/rules/doingwork-work-rules.yml
  title: ''
  type: Spectral
  url: rules/doingwork-work-rules.yml
- group: design
  href: https://artifacts.apis.io/doingwork-work/json-ld/doingwork-work-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/doingwork-work-context.jsonld
- group: design
  href: https://artifacts.apis.io/doingwork-work/vocabulary/doingwork-work-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doingwork-work-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/doingwork-work/data-model/doingwork-work-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doingwork-work-data-model.yml
- group: operate
  href: https://artifacts.apis.io/doingwork-work/changelog/doingwork-work-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/doingwork-work-changelog.yml
- group: design
  href: https://artifacts.apis.io/doingwork-work/errors/doingwork-work-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doingwork-work-problem-types.yml
- group: design
  href: https://artifacts.apis.io/doingwork-work/conformance/doingwork-work-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doingwork-work-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doingwork-work/llms/doingwork-work-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doingwork-work-llms.txt
- group: agent
  href: https://artifacts.apis.io/doingwork-work/mcp/doingwork-work-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doingwork-work-mcp.yml
- group: agent
  href: https://artifacts.apis.io/doingwork-work/well-known/doingwork-work-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doingwork-work-well-known.yml
- group: other
  href: https://artifacts.apis.io/doingwork-work/hosts/doingwork-work-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doingwork-work-hosts.yml
- group: other
  href: https://artifacts.apis.io/doingwork-work/vendors/doingwork-work-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doingwork-work-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://doingwork.work/whats-new/
- group: auth
  href: https://artifacts.apis.io/doingwork-work/scopes/doingwork-work-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/doingwork-work-scopes.yml
- group: auth
  href: https://artifacts.apis.io/doingwork-work/authentication/doingwork-work-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doingwork-work-authentication.yml
- group: auth
  href: https://artifacts.apis.io/doingwork-work/security/doingwork-work-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doingwork-work-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doingwork.work/
- group: docs
  title: ''
  type: Documentation
  url: https://doingwork.work/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://doingwork.work/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://doingwork.work/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://doingwork.work/start/
- group: start
  title: ''
  type: SignUp
  url: https://app.doingwork.work/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doingwork.work/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doingwork.work/privacy/
created: '2026-10-30'
description: Doing Work provides a platform that lets field service businesses create job photo‑based quotes, send invoices and get paid, all from a mobile‑friendly web app. It offers free starter plans, paid crew and pro tiers with AI minutes, messaging and storage, integrates with Stripe and upcoming QuickBooks sync, and supplies public API documentation at https://doingwork.work/openapi.json.
image: https://doingwork.work/og/doing-work-share.png?v=3
json_schemas:
- name: Health
  property_count: 9
  slug: doingwork-work-health
jsonld:
- class_count: 2
  name: Doingwork Work Context
  property_count: 10
  slug: doingwork-work-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.doingwork.work requiring OAuth.
  name: doingwork-work MCP Server
  slug: doingwork-work-mcp-yml
modified: '2026-10-30'
name: doingwork-work
nav: Providers
network: true
overview: 'doingwork-work publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Status API. Tagged areas include Company, Field Service Management, Invoicing, and Mobile.


  The doingwork-work catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  doingwork-work''s developer surface includes changelog, authentication, documentation, API reference, pricing, getting-started guide, signup flow, and 19 more developer resources.'
plans:
- name: Doingwork Work Plans Pricing
  plan_count: 3
  slug: doingwork-work-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: doingwork-work API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: doingwork-work-rules
scopes:
- name: Doingwork Work Scopes
  scope_count: 4
  slug: doingwork-work-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 56.3
    developer_ergonomics: 26.2
    discoverability: 66.7
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/doingwork-work/doingwork-work-2026-11-03T130910.png
security:
- kind: authentication
  name: Doingwork Work Authentication
  slug: doingwork-work-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Doingwork Work Domain Security
  slug: doingwork-work-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doingwork-work
tags:
- Company
- Field Service Management
- Invoicing
- Mobile
website: https://doingwork.work/
---
