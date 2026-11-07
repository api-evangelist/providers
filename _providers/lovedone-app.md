---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Lovedone App Agentic Access
  operation_count: 16
  slug: lovedone-app-agentic-access
  summary_line: 16 operations · 1 acting
api_count: 1
apis:
- baseURL: https://lovedone.app
  baseurl_source: declared
  description: 'Public HTML pages; send Accept: text/markdown for a text/markdown variant'
  name: lovedone-app Content API
  slug: lovedone-app-content-api
- baseURL: https://lovedone.app
  baseurl_source: declared
  description: Unauthenticated machine-readable files on lovedone.app
  name: lovedone-app Discovery API
  slug: lovedone-app-discovery-api
- baseURL: https://lovedone.app
  baseurl_source: declared
  description: Authenticated family-inbox Model Context Protocol (hosted off this landing origin)
  name: lovedone-app MCP API
  slug: lovedone-app-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/lovedone-app/agentic-access/lovedone-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lovedone-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lovedone-app/rate-limits/lovedone-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lovedone-app-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lovedone-app/rules/lovedone-app-rules.yml
  title: ''
  type: Spectral
  url: rules/lovedone-app-rules.yml
- group: design
  href: https://artifacts.apis.io/lovedone-app/json-ld/lovedone-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lovedone-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/lovedone-app/vocabulary/lovedone-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lovedone-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lovedone-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lovedone-app/data-model/lovedone-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lovedone-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/lovedone-app/authentication/lovedone-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lovedone-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/lovedone-app/errors/lovedone-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lovedone-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lovedone-app/conformance/lovedone-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lovedone-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lovedone-app/llms/lovedone-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lovedone-app-llms.txt
- group: build
  href: https://artifacts.apis.io/lovedone-app/mcp/lovedone-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lovedone-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lovedone-app/mcp/lovedone-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lovedone-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lovedone-app/well-known/lovedone-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lovedone-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/lovedone-app/hosts/lovedone-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lovedone-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/lovedone-app/vendors/lovedone-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lovedone-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/lovedone-app/packages/lovedone-app-packages.yml
  title: ''
  type: SDKs
  url: packages/lovedone-app-packages.yml
- group: build
  href: https://artifacts.apis.io/lovedone-app/packages/lovedone-app-packages.yml
  title: ''
  type: Packages
  url: packages/lovedone-app-packages.yml
- group: auth
  href: https://artifacts.apis.io/lovedone-app/scopes/lovedone-app-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lovedone-app-scopes.yml
- group: auth
  href: https://artifacts.apis.io/lovedone-app/security/lovedone-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lovedone-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lovedone.app/
- group: company
  title: ''
  type: Blog
  url: https://lovedone.app/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lovedone.app
- group: start
  title: ''
  type: GettingStarted
  url: https://lovedone.app/getting-started
- group: start
  title: ''
  type: Login
  url: https://inbox.lovedone.app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lovedone.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lovedone.app/terms
- group: docs
  title: ''
  type: APIReference
  url: https://lovedone.app/openapi.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lovedone.app
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Terahertz-Inc
created: '2026-10-30'
description: LovedOne is the family inbox for caring for aging parents — one private @lovedone.app email, shared by the whole family. Built by Terahertz Inc. in Virginia Beach, VA. It provides a private email address for every message about your parent's care, consolidating doctors, pharmacies, insurers, and attorneys into one place for the whole family to see.
image: https://lovedone.app/og.png
jsonld:
- class_count: 1
  name: Lovedone App Context
  property_count: 1
  slug: lovedone-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.lovedone.app.
  name: lovedone-app MCP Server
  slug: lovedone-app-mcp-yml
modified: '2026-10-30'
name: lovedone-app
nav: Providers
network: true
overview: 'lovedone-app publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Content API, Discovery API, and MCP API. Tagged areas include Family Care, Inbox, Healthcare, Communications, and Privacy.


  The lovedone-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lovedone-app''s developer surface includes authentication, engineering blog, documentation, getting-started guide, API reference, and 25 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 1
  name: Lovedone App Rate Limits
  slug: lovedone-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: lovedone-app API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: lovedone-app-rules
scopes:
- name: Lovedone App Scopes
  scope_count: 4
  slug: lovedone-app-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 49.1
    developer_ergonomics: 41.1
    discoverability: 75.0
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 29.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lovedone-app/lovedone-app-2026-11-03T135049.png
security:
- kind: authentication
  name: Lovedone App Authentication
  slug: lovedone-app-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Lovedone App Domain Security
  slug: lovedone-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: mcp-family
  slug: lovedone-app-mcp
slug: lovedone-app
tags:
- Family Care
- Inbox
- Healthcare
- Communications
- Privacy
website: https://lovedone.app/
---
