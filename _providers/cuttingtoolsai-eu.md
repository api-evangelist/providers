---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 6.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides endpoints for grade cross‑reference lookup via GET /api/xref returning JSON with matching grades.
  name: CuttingToolsAI API
  slug: cuttingtoolsai-api
- description: Free public JSON API for cross-brand carbide grade equivalence. Look up a grade, get the ISO class and other manufacturers at the same position. No key, no signup.
  name: CuttingToolsAI Cross-Reference JSON API
  slug: crossref-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/cuttingtoolsai-eu/plans/cuttingtoolsai-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cuttingtoolsai-eu-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cuttingtoolsai-eu/llms/cuttingtoolsai-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuttingtoolsai-eu-llms.txt
- group: build
  href: https://artifacts.apis.io/cuttingtoolsai-eu/mcp/cuttingtoolsai-eu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cuttingtoolsai-eu-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cuttingtoolsai-eu/mcp/cuttingtoolsai-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cuttingtoolsai-eu-mcp.yml
- group: other
  href: https://artifacts.apis.io/cuttingtoolsai-eu/hosts/cuttingtoolsai-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuttingtoolsai-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/cuttingtoolsai-eu/vendors/cuttingtoolsai-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuttingtoolsai-eu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuttingtoolsai.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuttingtoolsai.eu/privacy
- group: auth
  href: https://artifacts.apis.io/cuttingtoolsai-eu/security/cuttingtoolsai-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuttingtoolsai-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuttingtoolsai.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://cuttingtoolsai.eu/ref/
- group: operate
  title: ''
  type: Support
  url: https://cuttingtoolsai.eu/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://cuttingtoolsai.eu/
- group: start
  title: ''
  type: SignUp
  url: https://cuttingtoolsai.eu/account
- group: start
  title: ''
  type: GettingStarted
  url: https://cuttingtoolsai.eu/guides
coverage:
  checked: '2026-10-30'
  detail: The provider offers a free public JSON API but does not publish an OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://cuttingtoolsai.eu/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: CuttingToolsAI provides a brand‑neutral AI advisor for cutting tools, helping users find second sources for any carbide grade. It offers instant insert recommendations, cross‑references and ISO grade guidance for turning, milling and drilling, with free access to a chart behind every match.
image: https://cuttingtoolsai.eu/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cuttingtoolsai.eu.
  name: cuttingtoolsai-eu MCP Server
  slug: cuttingtoolsai-eu-mcp-yml
modified: '2026-10-29'
name: cuttingtoolsai-eu
nav: Providers
network: true
overview: 'cuttingtoolsai-eu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Cutting-Tools, Manufacturing, and Metalworking.


  cuttingtoolsai-eu''s developer surface includes documentation, support, pricing, signup flow, getting-started guide, and 10 more developer resources.'
plans:
- name: Cuttingtoolsai Eu Plans Pricing
  plan_count: 2
  slug: cuttingtoolsai-eu-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Cuttingtoolsai Eu Rate Limits
  slug: cuttingtoolsai-eu-rate-limits
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cuttingtoolsai Eu Authentication
  slug: cuttingtoolsai-eu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cuttingtoolsai Eu Domain Security
  slug: cuttingtoolsai-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuttingtoolsai-eu
tags:
- Company
- AI
- Cutting-Tools
- Manufacturing
- Metalworking
website: https://cuttingtoolsai.eu/
---
