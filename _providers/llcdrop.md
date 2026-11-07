---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Llcdrop Agentic Access
  operation_count: 30
  slug: llcdrop-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Account API from LLCDrop — 1 operation(s) for account.
  name: LLCDrop Account API
  slug: llcdrop-account-api
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Businesses API from LLCDrop — 4 operation(s) for businesses.
  name: LLCDrop Businesses API
  slug: llcdrop-businesses-api
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Counties and stats API from LLCDrop — 3 operation(s) for counties and stats.
  name: LLCDrop Counties and stats API
  slug: llcdrop-counties-and-stats-api
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Datasets API from LLCDrop — 14 operation(s) for datasets.
  name: LLCDrop Datasets API
  slug: llcdrop-datasets-api
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Filings API from LLCDrop — 2 operation(s) for filings.
  name: LLCDrop Filings API
  slug: llcdrop-filings-api
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Parcels API from LLCDrop — 4 operation(s) for parcels.
  name: LLCDrop Parcels API
  slug: llcdrop-parcels-api
- baseURL: https://api.llcdrop.com
  baseurl_source: declared
  description: The Reference lists API from LLCDrop — 2 operation(s) for reference lists.
  name: LLCDrop Reference lists API
  slug: llcdrop-reference-lists-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/llcdrop/agentic-access/llcdrop-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/llcdrop-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/llcdrop/rate-limits/llcdrop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/llcdrop-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/llcdrop/plans/llcdrop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/llcdrop-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/llcdrop/rules/llcdrop-rules.yml
  title: ''
  type: Spectral
  url: rules/llcdrop-rules.yml
- group: design
  href: https://artifacts.apis.io/llcdrop/vocabulary/llcdrop-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/llcdrop-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/llcdrop/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/llcdrop/conventions/llcdrop-conventions.yml
  title: ''
  type: Conventions
  url: conventions/llcdrop-conventions.yml
- group: auth
  href: https://artifacts.apis.io/llcdrop/authentication/llcdrop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/llcdrop-authentication.yml
- group: auth
  href: https://artifacts.apis.io/llcdrop/scopes/llcdrop-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/llcdrop-scopes.yml
- group: design
  href: https://artifacts.apis.io/llcdrop/errors/llcdrop-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/llcdrop-problem-types.yml
- group: design
  href: https://artifacts.apis.io/llcdrop/conformance/llcdrop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llcdrop-conformance.yml
- group: agent
  href: https://artifacts.apis.io/llcdrop/llms/llcdrop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llcdrop-llms.txt
- group: build
  href: https://artifacts.apis.io/llcdrop/mcp/llcdrop-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/llcdrop-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/llcdrop/mcp/llcdrop-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/llcdrop-mcp.yml
- group: agent
  href: https://artifacts.apis.io/llcdrop/well-known/llcdrop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llcdrop-well-known.yml
- group: other
  href: https://artifacts.apis.io/llcdrop/hosts/llcdrop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llcdrop-hosts.yml
- group: other
  href: https://artifacts.apis.io/llcdrop/vendors/llcdrop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llcdrop-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eliran-cuantolabs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.llcdrop.com</code
- group: auth
  href: https://artifacts.apis.io/llcdrop/security/llcdrop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llcdrop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llcdrop.com
- group: docs
  title: ''
  type: Documentation
  url: https://llcdrop.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://llcdrop.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://llcdrop.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://llcdrop.com/marketing/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://llcdrop.com/marketing/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://llcdrop.com/marketing/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://llcdrop.com/marketing/legal/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.llcdrop.com/openapi.json
  - status: 401
    url: https://api.llcdrop.com/mcp
  - status: 403
    url: https://llcdrop.com/api/mcp
  - status: 403
    url: https://app.llcdrop.com/api/mcp
  - status: 200
    url: https://llcdrop.com
  reason: partner-login
  state: gated
created: '2026-10-30'
description: LLCDrop provides real-time access to newly filed Florida business records, offering searchable data on owners, contact information, and business details the day they are filed. Users can search by name, trade, city, or ZIP, and obtain leads for outreach via email or postcard. The platform includes tiered credit plans, API and MCP access for developers, and integrates with CRM tools. It serves marketers, insurers, accountants, and other professionals targeting new Florida businesses.
image: https://llcdrop.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at api.llcdrop.com.
  name: LLCDrop MCP Server
  slug: llcdrop-mcp-yml
modified: '2026-10-30'
name: LLCDrop
nav: Providers
network: true
overview: 'LLCDrop publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Businesses API, Counties and stats API, and 4 more. Tagged areas include Lead Generation, Business Data, Marketing, and Real Estate.


  The LLCDrop catalog on APIs.io includes 1 Spectral governance ruleset.


  LLCDrop''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 22 more developer resources.'
plans:
- name: Llcdrop Plans Pricing
  plan_count: 4
  slug: llcdrop-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 12
  name: Llcdrop Rate Limits
  slug: llcdrop-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: LLCDrop API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: llcdrop-rules
scopes:
- name: Llcdrop Scopes
  scope_count: 1
  slug: llcdrop-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.8
    catalog_earned_first_party: 24.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 48.8
    developer_ergonomics: 39.8
    discoverability: 56.7
    operational_transparency: 34.2
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/llcdrop/llcdrop-2026-11-03T134944.png
security:
- kind: authentication
  name: Llcdrop Authentication
  slug: llcdrop-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Llcdrop Domain Security
  slug: llcdrop-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: businesses-search
  slug: llcdrop-businesses-search
slug: llcdrop
tags:
- Lead Generation
- Business Data
- Marketing
- Real Estate
website: https://llcdrop.com
---
