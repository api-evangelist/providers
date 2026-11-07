---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sitey My Agentic Access
  operation_count: 10
  slug: sitey-my-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 1
apis:
- baseURL: https://sitey.my
  baseurl_source: declared
  description: The Check API from sitey-my — 1 operation(s) for check.
  name: sitey-my Check API
  slug: sitey-my-check-api
- baseURL: https://sitey.my
  baseurl_source: declared
  description: The Domains API from sitey-my — 1 operation(s) for domains.
  name: sitey-my Domains API
  slug: sitey-my-domains-api
- baseURL: https://sitey.my
  baseurl_source: declared
  description: The Subdomains API from sitey-my — 6 operation(s) for subdomains.
  name: sitey-my Subdomains API
  slug: sitey-my-subdomains-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/sitey-my/agentic-access/sitey-my-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sitey-my-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sitey-my/rules/sitey-my-rules.yml
  title: ''
  type: Spectral
  url: rules/sitey-my-rules.yml
- group: design
  href: https://artifacts.apis.io/sitey-my/json-ld/sitey-my-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sitey-my-context.jsonld
- group: design
  href: https://artifacts.apis.io/sitey-my/vocabulary/sitey-my-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sitey-my-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sitey-my/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sitey-my/data-model/sitey-my-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sitey-my-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://sitey.my/terms
- group: design
  href: https://artifacts.apis.io/sitey-my/errors/sitey-my-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sitey-my-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sitey-my/conformance/sitey-my-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sitey-my-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sitey-my/llms/sitey-my-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sitey-my-llms.txt
- group: agent
  href: https://artifacts.apis.io/sitey-my/mcp/sitey-my-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sitey-my-mcp.yml
- group: auth
  href: https://artifacts.apis.io/sitey-my/well-known/sitey-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sitey-my-security.txt
- group: agent
  href: https://artifacts.apis.io/sitey-my/well-known/sitey-my-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sitey-my-well-known.yml
- group: other
  href: https://artifacts.apis.io/sitey-my/hosts/sitey-my-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sitey-my-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://sitey.my/blog
- group: auth
  href: https://artifacts.apis.io/sitey-my/security/sitey-my-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sitey-my-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sitey-my/security/sitey-my-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sitey-my-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sitey.my/
- group: docs
  title: ''
  type: Documentation
  url: https://sitey.my/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sitey.my/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sitey.my/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sitey.my/privacy
- group: operate
  title: ''
  type: Support
  url: https://sitey.my/about
created: '2026-10-29'
description: Sitey provides AI‑generated personal websites on custom domains without requiring sign‑up or accounts. Users can claim a subdomain (e.g., myapp.sitey.my), point it to their hosting provider (Vercel, Netlify, GitHub Pages, etc.), and the platform automatically builds and serves the site. The service includes an MCP for subdomain creation, open OpenAPI documentation, and tools like llms.txt. It emphasizes privacy, simplicity, and rapid deployment, targeting developers and creators who want a ready‑to‑use web presence powered by AI.
image: https://sitey.my/favicon-32.png
json_schemas:
- name: Subdomain
  property_count: 7
  slug: sitey-my-subdomain
jsonld:
- class_count: 2
  name: Sitey My Context
  property_count: 10
  slug: sitey-my-context
layout: provider
mcp_servers:
- description: Remote MCP server at sitey.my.
  name: sitey-my MCP Server
  slug: sitey-my-mcp-yml
modified: '2026-10-29'
name: sitey-my
nav: Providers
network: true
overview: 'sitey-my publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Check API, Domains API, and Subdomains API. Tagged areas include Artificial Intelligence, Website Builder, Sub Domain, and MCP.


  The sitey-my catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sitey-my''s developer surface includes engineering blog, documentation, API reference, support, and 19 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: sitey-my API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: sitey-my-rules
scopes:
- name: Sitey My Scopes
  scope_count: 0
  slug: sitey-my-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 63.8
    developer_ergonomics: 18.3
    discoverability: 66.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sitey-my/sitey-my-2026-11-03T143247.png
security:
- kind: authentication
  name: Sitey My Authentication
  slug: sitey-my-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sitey My Domain Security
  slug: sitey-my-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sitey My Vulnerability Disclosure
  slug: sitey-my-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sitey-my
tags:
- Artificial Intelligence
- Website Builder
- Sub Domain
- MCP
website: https://sitey.my/
---
