---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Howtoromania Io Agentic Access
  operation_count: 24
  slug: howtoromania-io-agentic-access
  summary_line: 24 operations · 5 acting
api_count: 1
apis:
- description: Data from Romanian public registries for AI agents.
  name: HowToRomania API
  slug: howtoromania-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/howtoromania-io/plans/howtoromania-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/howtoromania-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/howtoromania-io/conformance/howtoromania-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/howtoromania-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/howtoromania-io/llms/howtoromania-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/howtoromania-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/howtoromania-io/mcp/howtoromania-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/howtoromania-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/howtoromania-io/well-known/howtoromania-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/howtoromania-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/howtoromania-io/hosts/howtoromania-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/howtoromania-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/howtoromania-io/vendors/howtoromania-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/howtoromania-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/howtoromania-io/security/howtoromania-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/howtoromania-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://howtoromania.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.howtoromania.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.howtoromania.io/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://api.howtoromania.io/v1/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://howtoromania.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://howtoromania.io/privacy
created: '2026-10-30'
description: HowToRomania provides a comprehensive Romanian public registry data API, offering access to company information, court cases, e‑Factura processing, and legislation. It serves AI agents and developers with REST and MCP endpoints, delivering structured JSON data for corporate due‑diligence, legal compliance, and financial analysis across Romania.
image: https://howtoromania.io/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.howtoromania.io.
  name: howtoromania-io MCP Server
  slug: howtoromania-io-mcp-yml
modified: '2026-10-30'
name: howtoromania-io
nav: Providers
network: true
overview: 'howtoromania-io publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Finance, Legal, and AI.


  The howtoromania-io catalog on APIs.io includes 1 Spectral governance ruleset.


  howtoromania-io''s developer surface includes documentation, API reference, pricing, and 11 more developer resources.'
plans:
- name: Howtoromania Io Plans Pricing
  plan_count: 3
  slug: howtoromania-io-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Howtoromania Io Rate Limits
  slug: howtoromania-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: howtoromania-io API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 4
  slug: howtoromania-io-rules
scopes:
- name: Howtoromania Io Scopes
  scope_count: 0
  slug: howtoromania-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 72.4
    catalog_earned_first_party: 12.0
    catalog_gap: 42.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 53.6
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 18.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Howtoromania Io Authentication
  slug: howtoromania-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Howtoromania Io Domain Security
  slug: howtoromania-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: company-info
  slug: howtoromania-io-company-info
slug: howtoromania-io
tags:
- Company
- Data
- Finance
- Legal
- AI
website: https://howtoromania.io/
---
