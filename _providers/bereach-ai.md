---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'BeReach API: the agentic API for outreach, a REST API with 80+ operations for searching, retrieving profiles, emails, and sending messages.'
  name: BeReach API
  slug: bereach-api
- description: 'BeReach API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BeReach API
  slug: bereach-ai-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/bereach-ai/rate-limits/bereach-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bereach-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bereach-ai/plans/bereach-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bereach-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bereach-ai/rules/bereach-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bereach-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bereach-ai/json-ld/bereach-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bereach-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bereach-ai/vocabulary/bereach-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bereach-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bereach-ai/data-model/bereach-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bereach-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bereach-ai/changelog/bereach-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bereach-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/bereach-ai/authentication/bereach-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bereach-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/bereach-ai/lifecycle/bereach-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bereach-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bereach-ai/conformance/bereach-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bereach-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bereach-ai/llms/bereach-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bereach-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bereach-ai/mcp/bereach-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bereach-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bereach-ai/well-known/bereach-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bereach-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bereach-ai/hosts/bereach-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bereach-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bereach-ai/vendors/bereach-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bereach-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/bereach-ai/packages/bereach-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/bereach-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/bereach-ai/packages/bereach-ai-packages.yml
  title: ''
  type: Packages
  url: packages/bereach-ai-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bereach.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://bereach.ai/docs/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.bereach.ai</td
- group: auth
  href: https://artifacts.apis.io/bereach-ai/security/bereach-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bereach-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bereach.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bereach.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://bereach.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bereach.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bereach.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bereach.ai/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://bereach.ai/contact
coverage:
  checked: '2026-11-02'
  detail: The public API documentation describes endpoints but provides no machine‑readable OpenAPI, GraphQL, or other spec.
  evidence:
  - status: 200
    url: https://bereach.ai/bereach-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BeReach is an AI sales agent that finds the people who just showed interest in what you sell, writes a first LinkedIn message for each one, and sends only the ones you approve. It reads your ideal customer from your website or a single sentence, discovers companies and decision makers across markets, and crafts personalized outreach messages, streamlining LinkedIn prospecting.
image: https://bereach.ai/web-app-manifest-512x512.png
json_schemas:
- name: PostPublicSearchRequest
  property_count: 2
  slug: bereach-ai-post-public-search-request
jsonld:
- class_count: 1
  name: Bereach Ai Context
  property_count: 2
  slug: bereach-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bereach.ai.
  name: BeReach MCP Server
  slug: bereach-ai-mcp-yml
modified: '2026-11-02'
name: BeReach
nav: Providers
network: true
overview: 'BeReach is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, LinkedIn, Outreach, and Automation.


  The BeReach catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BeReach''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, pricing, support, and 21 more developer resources.'
plans:
- name: Bereach Ai Plans Pricing
  plan_count: 3
  slug: bereach-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Bereach Ai Rate Limits
  slug: bereach-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: BeReach API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: bereach-ai-rules
scopes:
- name: Bereach Ai Scopes
  scope_count: 0
  slug: bereach-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.2
    catalog_earned_first_party: 20.0
    catalog_gap: 46.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 18.6
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
  name: Bereach Ai Authentication
  slug: bereach-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bereach Ai Domain Security
  slug: bereach-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bereach-ai
tags:
- Artificial Intelligence
- Sales
- LinkedIn
- Outreach
- Automation
website: https://bereach.ai/
---
