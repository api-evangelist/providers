---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Internal service-to-service API for tenant provisioning, user management, session issuance, and provisioning token exchange.
  name: Levirge DevOps Platform Service API
  slug: levirge-devops-platform-service-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/levirge-com/rules/levirge-com-rules.yml
  title: ''
  type: Spectral
  url: rules/levirge-com-rules.yml
- group: design
  href: https://artifacts.apis.io/levirge-com/json-ld/levirge-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/levirge-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/levirge-com/vocabulary/levirge-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/levirge-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/levirge-com/conformance/levirge-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/levirge-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/levirge-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/levirge-com/data-model/levirge-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/levirge-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://levirge.com/security
- group: design
  href: https://artifacts.apis.io/levirge-com/errors/levirge-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/levirge-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/levirge-com/llms/levirge-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/levirge-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/levirge-com/mcp/levirge-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/levirge-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/levirge-com/well-known/levirge-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/levirge-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/levirge-com/hosts/levirge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/levirge-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/levirge-com/vendors/levirge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/levirge-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://levirge.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://levirge.com/brain/pricing
- group: auth
  href: https://artifacts.apis.io/levirge-com/security/levirge-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/levirge-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/levirge-com/security/levirge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/levirge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://levirge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://levirge.com/brain/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://levirge.com/brain/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://levirge.com/brain/docs
- group: operate
  title: ''
  type: Support
  url: https://levirge.com/contact
- group: company
  title: ''
  type: Blog
  url: https://levirge.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/levirge
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/levirge
- group: commercial
  title: ''
  type: TermsOfService
  url: https://levirge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://levirge.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://signup.levirge.com/brain
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://signup.levirge.com/openapi.json
  - status: 401
    url: https://signup.levirge.com/mcp
  - status: 200
    url: https://levirge.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Levirge provides AI-powered MCP servers that enable agents to read and remember web content. Levirge Search reads sources that block ordinary tools and returns clean, structured data. Levirge Brain gives agents and teammates shared memory, installing in about a minute. Both products share a single account, token model, and MCP surface, allowing seamless integration. Upcoming offerings include Levirge DevOps for behind‑firewall systems and Levirge Teams to unify coding agents.
image: https://levirge.com/assets/logo-levirge.svg
jsonld:
- class_count: 20
  name: Levirge Com Context
  property_count: 79
  slug: levirge-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at brain.levirge.com.
  name: levirge-com MCP Server
  slug: levirge-com-mcp-yml
modified: '2026-10-30'
name: levirge-com
nav: Providers
network: true
overview: 'levirge-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Search, Knowledge, MCP, and Platform.


  The levirge-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  levirge-com''s developer surface includes pricing, documentation, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Levirge Com Plans Pricing
  plan_count: 0
  slug: levirge-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Levirge Com Rate Limits
  slug: levirge-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: levirge-com API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 5
  slug: levirge-com-rules
scopes:
- name: Levirge Com Scopes
  scope_count: 0
  slug: levirge-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 16.6
    developer_ergonomics: 44.6
    discoverability: 56.7
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
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
  name: Levirge Com Authentication
  slug: levirge-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Levirge Com Domain Security
  slug: levirge-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Levirge Com Trust Center
  slug: levirge-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 2
skills:
- name: invitation-flow
  slug: levirge-com-invitation-flow
- name: tenant-management
  slug: levirge-com-tenant-management
slug: levirge-com
tags:
- AI
- Search
- Knowledge
- MCP
- Platform
website: https://levirge.com/
---
