---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP JSON-RPC server for 1ClickReport, enabling Claude to query marketing data.
  name: 1ClickReport MCP
  slug: 1clickreport-mcp
- description: '1ClickReport API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 1ClickReport API
  slug: 1clickreport-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/1clickreport-com/rules/1clickreport-com-rules.yml
  title: ''
  type: Spectral
  url: rules/1clickreport-com-rules.yml
- group: design
  href: https://artifacts.apis.io/1clickreport-com/json-ld/1clickreport-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/1clickreport-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/1clickreport-com/vocabulary/1clickreport-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/1clickreport-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/1clickreport-com/data-model/1clickreport-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/1clickreport-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/1clickreport-com/cli/1clickreport-com-cli.yml
  title: ''
  type: CLI
  url: cli/1clickreport-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/1clickreport-com/authentication/1clickreport-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/1clickreport-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/1clickreport-com/conformance/1clickreport-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/1clickreport-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/1clickreport-com/llms/1clickreport-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1clickreport-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/1clickreport-com/mcp/1clickreport-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1clickreport-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/1clickreport-com/well-known/1clickreport-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1clickreport-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/1clickreport-com/hosts/1clickreport-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1clickreport-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/1clickreport-com/vendors/1clickreport-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/1clickreport-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.1clickreport.com/blog/meta-advantage-plus-campaign-setup-2026
- group: auth
  href: https://artifacts.apis.io/1clickreport-com/security/1clickreport-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1clickreport-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1clickreport.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.1clickreport.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://www.1clickreport.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.1clickreport.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1clickreport.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1clickreport.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1clickreport
coverage:
  checked: '2026-10-31'
  detail: MCP JSON-RPC endpoint requires a valid session ID, returning 400 Bad Request without authentication.
  evidence:
  - status: 400
    url: https://mcp.1clickreport.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: 1ClickReport – From wasted spend to your next move. Connect Google Ads, Meta, GA4, Search Console & Stripe to Claude. Find wasted spend, put SEO & AEO on autopilot, and approve every change — without leaving Claude. 3‑day free trial.
image: https://www.1clickreport.com/logos/og-image-v2.png
json_schemas:
- name: GetInstallMcpShResponse
  property_count: 1
  slug: 1clickreport-com-get-install-mcp-sh-response
jsonld:
- class_count: 1
  name: 1Clickreport Com Context
  property_count: 1
  slug: 1clickreport-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.1clickreport.com.
  name: 1ClickReport MCP Server
  slug: 1clickreport-com-mcp-yml
modified: '2026-10-31'
name: 1ClickReport
nav: Providers
network: true
overview: '1ClickReport is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Analytics, Automation, and SEO.


  The 1ClickReport catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  1ClickReport''s developer surface includes CLI, authentication, getting-started guide, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: 1Clickreport Com Plans Pricing
  plan_count: 0
  slug: 1clickreport-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: 1Clickreport Com Rate Limits
  slug: 1clickreport-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: 1ClickReport API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: 1clickreport-com-rules
scopes:
- name: 1Clickreport Com Scopes
  scope_count: 0
  slug: 1clickreport-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 16.4
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 32.1
  provenance:
    conformance: first-party
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 1Clickreport Com Authentication
  slug: 1clickreport-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 1Clickreport Com Domain Security
  slug: 1clickreport-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 1clickreport-com
tags:
- Artificial Intelligence
- Marketing
- Analytics
- Automation
- SEO
website: https://1clickreport.com/
---
