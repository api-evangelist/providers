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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Disban Io Agentic Access
  operation_count: 16
  slug: disban-io-agentic-access
  summary_line: 16 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Auth API from disban-io — 5 operation(s) for auth.
  name: disban-io Auth API
  slug: disban-io-auth-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Batch API from disban-io — 1 operation(s) for batch.
  name: disban-io Batch API
  slug: disban-io-batch-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Check API from disban-io — 1 operation(s) for check.
  name: disban-io Check API
  slug: disban-io-check-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Features API from disban-io — 1 operation(s) for features.
  name: disban-io Features API
  slug: disban-io-features-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Keys API from disban-io — 2 operation(s) for keys.
  name: disban-io Keys API
  slug: disban-io-keys-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Plans API from disban-io — 1 operation(s) for plans.
  name: disban-io Plans API
  slug: disban-io-plans-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Referrals API from disban-io — 1 operation(s) for referrals.
  name: disban-io Referrals API
  slug: disban-io-referrals-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Subscription API from disban-io — 1 operation(s) for subscription.
  name: disban-io Subscription API
  slug: disban-io-subscription-api
- baseURL: https://disban.io
  baseurl_source: declared
  description: The Webhooks API from disban-io — 1 operation(s) for webhooks.
  name: disban-io Webhooks API
  slug: disban-io-webhooks-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/disban-io/agentic-access/disban-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/disban-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/disban-io/rate-limits/disban-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/disban-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/disban-io/rules/disban-io-rules.yml
  title: ''
  type: Spectral
  url: rules/disban-io-rules.yml
- group: design
  href: https://artifacts.apis.io/disban-io/json-ld/disban-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/disban-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/disban-io/vocabulary/disban-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/disban-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/disban-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/disban-io/data-model/disban-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/disban-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/disban-io/cli/disban-io-cli.yml
  title: ''
  type: CLI
  url: cli/disban-io-cli.yml
- group: auth
  href: https://artifacts.apis.io/disban-io/authentication/disban-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/disban-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/disban-io/errors/disban-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/disban-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/disban-io/conformance/disban-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/disban-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/disban-io/llms/disban-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/disban-io-llms.txt
- group: build
  href: https://artifacts.apis.io/disban-io/mcp/disban-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/disban-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/disban-io/mcp/disban-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/disban-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/disban-io/hosts/disban-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disban-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/disban-io/vendors/disban-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/disban-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/disban-io/packages/disban-io-packages.yml
  title: ''
  type: SDKs
  url: packages/disban-io-packages.yml
- group: build
  href: https://artifacts.apis.io/disban-io/packages/disban-io-packages.yml
  title: ''
  type: Packages
  url: packages/disban-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disban.io/terms
- group: start
  title: ''
  type: Login
  url: https://disban.io/login
- group: auth
  href: https://artifacts.apis.io/disban-io/security/disban-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disban-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disban.io/
- group: docs
  title: ''
  type: Documentation
  url: https://disban.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://disban.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://disban.io/signup
- group: operate
  title: ''
  type: Support
  url: https://disban.io/support
- group: company
  title: ''
  type: Blog
  url: https://disban.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://disban.io/privacy
created: '2026-10-30'
description: Disban provides an email‑domain classification API that helps developers detect disposable, free, alias, testing, parked or unknown email domains during user sign‑up flows. The service offers a free beta with 2,000 checks per month and supports GET requests without authentication for limited usage. It supplies SDKs for npm and PyPI, and an MCP server for batch checks. Disban aims to improve signup security and reduce fraud by filtering low‑quality email addresses.
image: https://disban.io/og.png
json_schemas:
- name: Account
  property_count: 1
  slug: disban-io-account
- name: Key
  property_count: 6
  slug: disban-io-key
- name: Offer
  property_count: 6
  slug: disban-io-offer
- name: Plan
  property_count: 6
  slug: disban-io-plan
- name: Subscription
  property_count: 10
  slug: disban-io-subscription
- name: Verdict
  property_count: 26
  slug: disban-io-verdict
jsonld:
- class_count: 7
  name: Disban Io Context
  property_count: 56
  slug: disban-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at disban.io.
  name: disban-io MCP Server
  slug: disban-io-mcp-yml
modified: '2026-10-30'
name: disban-io
nav: Providers
network: true
overview: 'disban-io publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Batch API, Check API, and 6 more. Tagged areas include Company, Email, Disposable Email, Security, and Fraud Prevention.


  The disban-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  disban-io''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Disban Io Plans Pricing
  plan_count: 0
  slug: disban-io-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Disban Io Rate Limits
  slug: disban-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: disban-io API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: disban-io-rules
scopes:
- name: Disban Io Scopes
  scope_count: 0
  slug: disban-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 59.5
    developer_ergonomics: 50.5
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
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
screenshot: https://apis.io/screenshots/disban-io/disban-io-2026-11-03T130749.png
security:
- kind: authentication
  name: Disban Io Authentication
  slug: disban-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Disban Io Domain Security
  slug: disban-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: check-email-domain
  slug: disban-io-check-email-domain
slug: disban-io
tags:
- Company
- Email
- Disposable Email
- Security
- Fraud Prevention
website: https://disban.io/
---
