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
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sornkan Com Agentic Access
  operation_count: 3
  slug: sornkan-com-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: API for publishing websites on SORNKan platform, offering claim, renew, and custom hostname operations.
  name: SORNKan Publish API
  slug: sornkan-publish-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/sornkan-com/agentic-access/sornkan-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sornkan-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sornkan-com/rules/sornkan-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sornkan-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/sornkan-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sornkan-com/errors/sornkan-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sornkan-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sornkan-com/conformance/sornkan-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sornkan-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sornkan-com/llms/sornkan-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sornkan-com-llms.txt
- group: other
  href: https://artifacts.apis.io/sornkan-com/a2a/sornkan-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sornkan-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/sornkan-com/mcp/sornkan-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sornkan-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sornkan-com/well-known/sornkan-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sornkan-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sornkan-com/hosts/sornkan-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sornkan-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sornkan-com/vendors/sornkan-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sornkan-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sornkan.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sornkan.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://sornkan.com/news
- group: company
  title: ''
  type: Blog
  url: https://sornkan.com/blog
- group: auth
  href: https://artifacts.apis.io/sornkan-com/security/sornkan-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sornkan-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sornkan.com/
created: '2026-10-30'
description: 'sornkan-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://sornkan.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at sornkan.com.
  name: sornkan-com MCP Server
  slug: sornkan-com-mcp-yml
modified: '2026-10-30'
name: sornkan-com
nav: Providers
network: true
overview: 'sornkan-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The sornkan-com catalog on APIs.io includes 1 Spectral governance ruleset.


  sornkan-com''s developer surface includes engineering blog and 16 more developer resources.'
plans:
- name: Sornkan Com Plans Pricing
  plan_count: 0
  slug: sornkan-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Sornkan Com Rate Limits
  slug: sornkan-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: sornkan-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: sornkan-com-rules
scopes:
- name: Sornkan Com Scopes
  scope_count: 0
  slug: sornkan-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.6
    discoverability: 59.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.0
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sornkan-com/sornkan-com-2026-11-03T143534.png
security:
- kind: authentication
  name: Sornkan Com Authentication
  slug: sornkan-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sornkan Com Domain Security
  slug: sornkan-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: claim-site
  slug: sornkan-com-claim-site
- name: connect-hostname
  slug: sornkan-com-connect-hostname
- name: renew-site
  slug: sornkan-com-renew-site
slug: sornkan-com
tags:
- Company
website: https://sornkan.com/
---
