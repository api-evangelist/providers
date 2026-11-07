---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.valet.dev/mcp
  baseurl_source: declared
  description: The Install API from valet-dev — 1 operation(s) for install.
  name: valet-dev Install API
  slug: valet-dev-install-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/valet-dev/plans/valet-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/valet-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/valet-dev/rules/valet-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/valet-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/valet-dev/vocabulary/valet-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/valet-dev-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/valet-dev/cli/valet-dev-cli.yml
  title: ''
  type: CLI
  url: cli/valet-dev-cli.yml
- group: auth
  href: https://artifacts.apis.io/valet-dev/authentication/valet-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/valet-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/valet-dev/errors/valet-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/valet-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/valet-dev/conformance/valet-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/valet-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/valet-dev/llms/valet-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/valet-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/valet-dev/mcp/valet-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/valet-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/valet-dev/well-known/valet-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/valet-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/valet-dev/hosts/valet-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/valet-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/valet-dev/vendors/valet-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/valet-dev-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://valet.dev/team
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.valet.dev/auth/signup
- group: auth
  href: https://artifacts.apis.io/valet-dev/security/valet-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/valet-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valet.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://valet.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://valet.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://valet.dev/docs
- group: operate
  title: ''
  type: Support
  url: https://valet.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://valet.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://valet.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valet.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valet.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valetdotdev
created: '2026-10-31'
description: Valet is the app platform enabling citizen developers. Stop data from leaving and credentials from spreading. Valet runs the tools your business users build inside your cloud, behind your SSO. One store for every dashboard, tool, and report your company builds with AI.
image: https://www.valet.dev/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.valet.dev.
  name: valet-dev MCP Server
  slug: valet-dev-mcp-yml
modified: '2026-10-31'
name: valet-dev
nav: Providers
network: true
overview: 'valet-dev is listed with 1 API on the [APIs.io](https://apis.io/) network: Install API. Tagged areas include Company, Platform, Citizen-Developer, Automation, and Integration.


  The valet-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  valet-dev''s developer surface includes CLI, authentication, signup flow, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Valet Dev Plans Pricing
  plan_count: 2
  slug: valet-dev-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: valet-dev API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: valet-dev-rules
scopes:
- name: Valet Dev Scopes
  scope_count: 0
  slug: valet-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 36.9
    discoverability: 65.8
    operational_transparency: 2.6
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Valet Dev Authentication
  slug: valet-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Valet Dev Domain Security
  slug: valet-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valet-dev
tags:
- Company
- Platform
- Citizen-Developer
- Automation
- Integration
website: https://valet.dev/
---
