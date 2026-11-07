---
access_model:
  confidence: high
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
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 66.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://control.patronus.studio/api/v1
  baseurl_source: declared
  description: The Scan API from Patronus Protect — 2 operation(s) for scan.
  name: Patronus Protect Scan API
  slug: patronus-protect-scan-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/patronus-protect/rate-limits/patronus-protect-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/patronus-protect-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/patronus-protect/capabilities/patronus-protect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/patronus-protect-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/patronus-protect/overlays/patronus-protect-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/patronus-protect-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/patronus-protect/mcp/patronus-protect-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/patronus-protect-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://patronus.studio/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.patronus.studio/
- group: start
  title: ''
  type: GettingStarted
  url: https://patronus-protect.github.io/patronus-security/getting-started/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://patronus.studio/pricing
- group: company
  title: ''
  type: Blog
  url: https://patronus.studio/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/patronus-protect
- group: build
  href: https://artifacts.apis.io/patronus-protect/packages/patronus-protect-packages.yml
  title: ''
  type: Packages
  url: packages/patronus-protect-packages.yml
- group: build
  href: https://artifacts.apis.io/patronus-protect/packages/patronus-protect-packages.yml
  title: ''
  type: SDKs
  url: packages/patronus-protect-packages.yml
- group: build
  href: https://artifacts.apis.io/patronus-protect/cli/patronus-protect-cli.yml
  title: ''
  type: CLI
  url: cli/patronus-protect-cli.yml
- group: agent
  href: https://artifacts.apis.io/patronus-protect/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/patronus-protect/llms/patronus-protect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/patronus-protect-llms.txt
- group: docs
  href: https://artifacts.apis.io/patronus-protect/json-schema/patronus-protect-runtime-v1.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/patronus-protect-runtime-v1.schema.json
- group: design
  href: https://artifacts.apis.io/patronus-protect/conformance/patronus-protect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/patronus-protect-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/patronus-protect/plans/patronus-protect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/patronus-protect-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/patronus-protect/changelog/patronus-protect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/patronus-protect-changelog.yml
- group: agent
  href: https://artifacts.apis.io/patronus-protect/well-known/patronus-protect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/patronus-protect-well-known.yml
- group: auth
  href: https://artifacts.apis.io/patronus-protect/well-known/patronus-protect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/patronus-protect-security.txt
- group: auth
  href: https://artifacts.apis.io/patronus-protect/security/patronus-protect-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/patronus-protect-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/patronus-protect/security/patronus-protect-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/patronus-protect-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/patronus-protect/security/patronus-protect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/patronus-protect-domain-security.yml
created: '2026-09-20'
description: Patronus Protect, from Casdo Labs GmbH, is an on-device AI firewall that detects prompt injection, PII/DLP, sensitive documents and agentic tool risk in text, public HTTPS webpages, documents and MCP servers before they are used by AI agents, RAG pipelines or LLM applications. It exposes a REST Scan API (control.patronus.studio/api/v1), first-party Rust, TypeScript and Python SDK clients, a local CLI with Codex, Claude Code and DeepSeek plugins, a remote OAuth-protected MCP server and a local stdio MCP server, and the open-source Patronus Ark scanning core.
finops:
- has_sources: true
  method: derived
  name: Patronus Protect Finops
  primary_unit: pro gerät
  service_category: ''
  slug: patronus-protect-finops
  template: false
json_schemas:
- name: Patronus local runtime v1 NDJSON frame
  property_count: 0
  slug: patronus-protect-runtime-v1.schema
layout: provider
mcp_servers:
- description: Patronus ships an MCP server in two deployments. A remote, OAuth-protected MCP server is served at control.patronus.studio/api/mcp (DCR + PKCE, scopes scan:read/scan:write). A local stdio MCP server (
  name: Patronus Protect MCP Server
  slug: patronus-native
modified: '2026-09-20'
name: Patronus Protect
nav: Providers
network: true
overview: 'Patronus Protect publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Scan API. Tagged areas include AI Safety, Prompt Injection, Security, LLM, and Agent-Native.


  The Patronus Protect catalog on APIs.io includes 1 Spectral governance ruleset.


  Patronus Protect''s developer surface includes getting-started guide, pricing, engineering blog, CLI, changelog, and 19 more developer resources.'
plans:
- name: Patronus Protect Plans Pricing
  plan_count: 6
  slug: patronus-protect-plans-pricing
- name: Patronus Protect Price Estimates
  plan_count: 0
  slug: patronus-protect-price-estimates
random_paper: 2
rate_limits:
- limit_count: 0
  name: Patronus Protect Rate Limits
  slug: patronus-protect-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Patronus Protect API Rules
  rule_count: 57
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 4
  slug: patronus-protect-rules
scopes:
- name: Patronus Protect Scopes
  scope_count: 2
  slug: patronus-protect-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 57.8
    developer_ergonomics: 53.6
    discoverability: 71.7
    operational_transparency: 28.9
  previous_composite: 54.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/patronus-protect/patronus-protect-2026-10-11T112408.png
security:
- kind: authentication
  name: Patronus Protect Authentication
  slug: patronus-protect-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Patronus Protect Domain Security
  slug: patronus-protect-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Patronus Protect Vulnerability Disclosure
  slug: patronus-protect-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: patronus-security-scan
  slug: patronus-protect-security-scan
slug: patronus-protect
tags:
- AI Safety
- Prompt Injection
- Security
- LLM
- Agent-Native
- MCP
- DLP
- PII
- On-Device
- AI Firewall
website: https://patronus.studio/
---
