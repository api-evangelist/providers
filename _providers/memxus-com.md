---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for Memxus providing endpoints for memory storage and retrieval.
  name: Memxus API
  slug: memxus-api
- description: 'memxus-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: memxus-com API
  slug: memxus-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/memxus-com/plans/memxus-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memxus-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/memxus-com/rules/memxus-com-rules.yml
  title: ''
  type: Spectral
  url: rules/memxus-com-rules.yml
- group: design
  href: https://artifacts.apis.io/memxus-com/vocabulary/memxus-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/memxus-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/memxus-com/authentication/memxus-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memxus-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/memxus-com/conformance/memxus-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memxus-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/memxus-com/mcp/memxus-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/memxus-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/memxus-com/well-known/memxus-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/memxus-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/memxus-com/hosts/memxus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memxus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/memxus-com/vendors/memxus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memxus-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.memxus.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.memxus.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.memxus.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.memxus.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.memxus.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.memxus.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/memxus-com/security/memxus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memxus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memxus.com/
coverage:
  checked: '2026-10-31'
  detail: API reference page provides HTML docs but no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://www.memxus.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Memxus provides an AI context engine that stores and retrieves developer knowledge across tools such as Claude, Cursor, and ChatGPT. By saving documents, code, decisions, and discussions, it lets AI models access the right context instantly, boosting productivity and reducing repetitive prompting. The platform offers a hosted REST API at https://api.memxus.com/api/v1, OAuth and API‑key authentication, and tiered pricing from free to enterprise. It emphasizes security with AES‑256‑GCM encryption and GDPR compliance, positioning it as a shared memory layer for modern development workflows.
image: https://memxus.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.memxus.com.
  name: memxus-com MCP Server
  slug: memxus-com-mcp-yml
modified: '2026-10-30'
name: memxus-com
nav: Providers
network: true
overview: 'memxus-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Context Engine, Developer Tools, Productivity, and Memory.


  The memxus-com catalog on APIs.io includes 1 Spectral governance ruleset.


  memxus-com''s developer surface includes authentication, signup flow, pricing, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Memxus Com Plans Pricing
  plan_count: 2
  slug: memxus-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: memxus-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: memxus-com-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 22.6
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 31.9
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/memxus-com/memxus-com-2026-11-03T135653.png
security:
- kind: authentication
  name: Memxus Com Authentication
  slug: memxus-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Memxus Com Domain Security
  slug: memxus-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memxus-com
tags:
- Artificial Intelligence
- Context Engine
- Developer Tools
- Productivity
- Memory
website: https://memxus.com/
---
