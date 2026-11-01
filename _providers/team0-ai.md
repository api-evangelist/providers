---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Connect any MCP agent to Team0 at api.team0.ai/v1/mcp, or read the same understanding from your product over HTTP. Per-agent access, scoped reads.
  name: Team0 External API
  slug: team0-external-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/team0-ai/rules/team0-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/team0-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/team0-ai/json-ld/team0-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/team0-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/team0-ai/vocabulary/team0-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/team0-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/team0-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/team0-ai/data-model/team0-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/team0-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/team0-ai/conventions/team0-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/team0-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/team0-ai/conventions/team0-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/team0-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/team0-ai/authentication/team0-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/team0-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/team0-ai/scopes/team0-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/team0-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/team0-ai/errors/team0-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/team0-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/team0-ai/conformance/team0-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/team0-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/team0-ai/llms/team0-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/team0-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/team0-ai/well-known/team0-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/team0-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/team0-ai/hosts/team0-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/team0-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/team0-ai/vendors/team0-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/team0-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://team0.ai/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://team0.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://team0.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://team0.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://team0.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://team0.ai/developers
- group: auth
  href: https://artifacts.apis.io/team0-ai/security/team0-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/team0-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://team0.ai/
- group: operate
  title: ''
  type: Support
  url: https://team0.ai/support
- group: commercial
  title: ''
  type: Pricing
  url: https://team0.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://team0.ai/product
- group: start
  title: ''
  type: GettingStarted
  url: https://team0.ai/product
created: '2026-10-30'
description: 'Team0 builds a brain for a company’s AI agents: one for each person and one for the company, kept current from the work itself and installed in the company’s own cloud. It gives every employee a brain and one to the company, learns from meetings, tools and AI chats, and keeps decisions, promises and changes current for every agent your team uses, in your cloud or ours.'
image: https://team0.ai/logo/logo_color.png
jsonld:
- class_count: 85
  name: Team0 Ai Context
  property_count: 228
  slug: team0-ai-context
layout: provider
modified: '2026-10-30'
name: team0-ai
nav: Providers
network: true
overview: 'team0-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Enterprise, KnowledgeManagement, and Automation.


  The team0-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  team0-ai''s developer surface includes authentication, engineering blog, API reference, support, pricing, documentation, getting-started guide, and 20 more developer resources.'
plans:
- name: Team0 Ai Plans Pricing
  plan_count: 0
  slug: team0-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Team0 Ai Rate Limits
  slug: team0-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: team0-ai API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: team0-ai-rules
scopes:
- name: Team0 Ai Scopes
  scope_count: 0
  slug: team0-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 33.3
    contract_quality: 20.7
    developer_ergonomics: 54.0
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Team0 Ai Authentication
  slug: team0-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Team0 Ai Domain Security
  slug: team0-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: team0-ai
tags:
- Company
- AI
- Enterprise
- KnowledgeManagement
- Automation
website: https://team0.ai/
---
