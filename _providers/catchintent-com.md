---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Catchintent Com Agentic Access
  operation_count: 11
  slug: catchintent-com-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- description: Public discovery metadata for CatchIntent – the intent layer for B2B outbound.
  name: CatchIntent API
  slug: catchintent-api
- baseURL: https://engine.catchintent.com
  baseurl_source: declared
  description: Agent-readable discovery resources served from the marketing origin.
  name: CatchIntent Discovery API
  slug: catchintent-com-discovery-api
- baseURL: https://engine.catchintent.com
  baseurl_source: declared
  description: Service health checks.
  name: CatchIntent Health API
  slug: catchintent-com-health-api
- baseURL: https://engine.catchintent.com
  baseurl_source: declared
  description: Model Context Protocol endpoint and related discovery metadata.
  name: CatchIntent MCP API
  slug: catchintent-com-mcp-api
- baseURL: https://engine.catchintent.com
  baseurl_source: declared
  description: OAuth 2.1 discovery for MCP authentication.
  name: CatchIntent OAuth API
  slug: catchintent-com-oauth-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/catchintent-com/agentic-access/catchintent-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/catchintent-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/catchintent-com/plans/catchintent-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/catchintent-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/catchintent-com/rules/catchintent-com-rules.yml
  title: ''
  type: Spectral
  url: rules/catchintent-com-rules.yml
- group: design
  href: https://artifacts.apis.io/catchintent-com/json-ld/catchintent-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/catchintent-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/catchintent-com/vocabulary/catchintent-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/catchintent-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/catchintent-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/catchintent-com/data-model/catchintent-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/catchintent-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/catchintent-com/errors/catchintent-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/catchintent-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/catchintent-com/conformance/catchintent-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/catchintent-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/catchintent-com/llms/catchintent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catchintent-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/catchintent-com/well-known/catchintent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catchintent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/catchintent-com/hosts/catchintent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchintent-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/catchintent-com/vendors/catchintent-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catchintent-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catchintent.com/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://app.catchintent.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catchintent.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CatchIntent
- group: operate
  title: ''
  type: ChangeLog
  url: https://catchintent.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://catchintent.com/docs/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://catchintent.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/catchintent-com/scopes/catchintent-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/catchintent-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/catchintent-com/authentication/catchintent-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/catchintent-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/catchintent-com/security/catchintent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchintent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchintent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://catchintent.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://catchintent.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://catchintent.com/blog/
- group: start
  title: ''
  type: Demo
  url: https://catchintent.com/demo/
created: '2026-11-04'
description: CatchIntent finds B2B buyers showing real intent, ranks them, and drafts the opener. You get a daily queue of warm leads, ready to send or push to your CRM. The platform offers AI scoring, multi‑product workspaces, and integrations with major CRMs and outreach tools, targeting outbound sales teams and agencies.
image: https://catchintent.com/og/index.png
jsonld:
- class_count: 9
  name: Catchintent Com Context
  property_count: 26
  slug: catchintent-com-context
layout: provider
modified: '2026-11-04'
name: CatchIntent
nav: Providers
network: true
overview: 'CatchIntent publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Health API, MCP API, and 2 more. Tagged areas include B2B, Sales, Intent Data, Artificial Intelligence, and Outbound.


  The CatchIntent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CatchIntent''s developer surface includes signup flow, changelog, getting-started guide, API reference, authentication, documentation, pricing, and 21 more developer resources.'
plans:
- name: Catchintent Com Plans Pricing
  plan_count: 1
  slug: catchintent-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: CatchIntent API Rules
  rule_count: 50
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 3
  slug: catchintent-com-rules
scopes:
- name: Catchintent Com Scopes
  scope_count: 9
  slug: catchintent-com-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.8
    catalog_earned_first_party: 8.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 52.5
    developer_ergonomics: 33.8
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Catchintent Com Authentication
  slug: catchintent-com-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Catchintent Com Domain Security
  slug: catchintent-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: catchintent-com
tags:
- B2B
- Sales
- Intent Data
- Artificial Intelligence
- Outbound
website: https://catchintent.com/
---
