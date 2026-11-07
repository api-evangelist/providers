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
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kyanitelabs Tech Agentic Access
  operation_count: 6
  slug: kyanitelabs-tech-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: Public discovery, health, contact, newsletter, and implementation-intake endpoints.
  name: Public Website API
  slug: public-website-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/kyanitelabs-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kyanitelabs-tech/agentic-access/kyanitelabs-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kyanitelabs-tech-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/kyanitelabs-tech/rules/kyanitelabs-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/kyanitelabs-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/kyanitelabs-tech/errors/kyanitelabs-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kyanitelabs-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kyanitelabs-tech/conformance/kyanitelabs-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kyanitelabs-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kyanitelabs-tech/llms/kyanitelabs-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kyanitelabs-tech-llms.txt
- group: other
  href: https://artifacts.apis.io/kyanitelabs-tech/a2a/kyanitelabs-tech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kyanitelabs-tech-a2a.yml
- group: build
  href: https://artifacts.apis.io/kyanitelabs-tech/mcp/kyanitelabs-tech-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kyanitelabs-tech-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/kyanitelabs-tech/mcp/kyanitelabs-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kyanitelabs-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kyanitelabs-tech/well-known/kyanitelabs-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kyanitelabs-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/kyanitelabs-tech/hosts/kyanitelabs-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kyanitelabs-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/kyanitelabs-tech/vendors/kyanitelabs-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kyanitelabs-tech-vendors.yml
- group: auth
  href: https://artifacts.apis.io/kyanitelabs-tech/security/kyanitelabs-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kyanitelabs-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kyanitelabs.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kyanitelabs.tech/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://kyanitelabs.tech/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://kyanitelabs.tech/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://kyanitelabs.tech/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KyaniteLabs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kyanitelabs.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kyanitelabs.tech/privacy
created: '2026-10-29'
description: KyaniteLabs helps builders and teams get open-source AI tools, MCP systems, media pipelines, localization QA, and repo diagnostics working in their real environment. The company provides a public API for discovery, contact, newsletter, and implementation intake workflows, exposing endpoints for health checks and an OpenAPI specification. Their platform focuses on integrating AI tools into production pipelines, offering resources such as documentation, blog posts, and open-source repositories.
image: https://kyanitelabs.tech/static/brand/kyanite-open-graph-generated-original-1200x630.png
layout: provider
mcp_servers:
- description: Remote MCP server at kyanitelabs.tech.
  name: kyanitelabs-tech MCP Server
  slug: kyanitelabs-tech-mcp-yml
modified: '2026-10-29'
name: kyanitelabs-tech
nav: Providers
network: true
overview: 'kyanitelabs-tech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, MCP, Media Pipelines, Localization, and Diagnostics.


  The kyanitelabs-tech catalog on APIs.io includes 1 Spectral governance ruleset.


  kyanitelabs-tech''s developer surface includes documentation, API reference, engineering blog, and 18 more developer resources.'
plans:
- name: Kyanitelabs Tech Plans Pricing
  plan_count: 0
  slug: kyanitelabs-tech-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Kyanitelabs Tech Rate Limits
  slug: kyanitelabs-tech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: kyanitelabs-tech API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: kyanitelabs-tech-rules
scopes:
- name: Kyanitelabs Tech Scopes
  scope_count: 0
  slug: kyanitelabs-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 75.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kyanitelabs-tech/kyanitelabs-tech-2026-11-03T134613.png
security:
- kind: authentication
  name: Kyanitelabs Tech Authentication
  slug: kyanitelabs-tech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kyanitelabs Tech Domain Security
  slug: kyanitelabs-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kyanitelabs-tech
tags:
- Artificial Intelligence
- MCP
- Media Pipelines
- Localization
- Diagnostics
website: https://kyanitelabs.tech/
---
