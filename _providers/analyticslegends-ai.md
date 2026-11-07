---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP (Model Context Protocol) server at https://analyticslegends.ai/mcp providing tools for SAP AI & analytics firm directory.
  name: Analytics Legends MCP Server
  slug: mcp-server
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/analyticslegends-ai/plans/analyticslegends-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/analyticslegends-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://analyticslegends.ai/security/
- group: agent
  href: https://artifacts.apis.io/analyticslegends-ai/llms/analyticslegends-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/analyticslegends-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/analyticslegends-ai/well-known/analyticslegends-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/analyticslegends-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/analyticslegends-ai/well-known/analyticslegends-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/analyticslegends-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/analyticslegends-ai/hosts/analyticslegends-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/analyticslegends-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/analyticslegends-ai/vendors/analyticslegends-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/analyticslegends-ai-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://analyticslegends.ai/guides/
- group: auth
  href: https://artifacts.apis.io/analyticslegends-ai/security/analyticslegends-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/analyticslegends-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/analyticslegends-ai/security/analyticslegends-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/analyticslegends-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://analyticslegends.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://analyticslegends.ai/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://analyticslegends.ai/terms/
- group: company
  title: ''
  type: Blog
  url: https://analyticslegends.ai/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/analyticslegends
- group: docs
  title: ''
  type: APIReference
  url: https://analyticslegends.ai/api/contracts-lean.json
- group: commercial
  title: ''
  type: Pricing
  url: https://analyticslegends.ai/pricing/
created: '2026-11-01'
description: Analytics Legends provides an AI‑driven platform for SAP analytics experts, delivering verified missions, market signals, and learning assets in a daily workflow. The service aggregates SAP analytics postings, offers a curated knowledge base, and supports consultants with benchmarks, directories, and freelance opportunities, all without affiliation to SAP.
image: https://analyticslegends.ai/og-card.png?v=1-84-0
layout: provider
mcp_servers:
- description: ''
  name: Analytics Legends MCP Server
  slug: analyticslegends-ai-mcp-json
- description: ''
  name: Analytics Legends MCP endpoint (Streamable HTTP)
  slug: analytics-legends-mcp-endpoint-streamable-http
modified: '2026-11-01'
name: Analytics Legends
nav: Providers
network: true
overview: 'Analytics Legends is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, SAP, Artificial Intelligence, Data, and Platform.


  Analytics Legends'' developer surface includes documentation, engineering blog, API reference, pricing, and 13 more developer resources.'
plans:
- name: Analyticslegends Ai Plans Pricing
  plan_count: 4
  slug: analyticslegends-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Analyticslegends Ai Rate Limits
  slug: analyticslegends-ai-rate-limits
scopes:
- name: Analyticslegends Ai Scopes
  scope_count: 0
  slug: analyticslegends-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 26.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Analyticslegends Ai Authentication
  slug: analyticslegends-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Analyticslegends Ai Domain Security
  slug: analyticslegends-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Analyticslegends Ai Vulnerability Disclosure
  slug: analyticslegends-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: analyticslegends-ai
tags:
- Analytics
- SAP
- Artificial Intelligence
- Data
- Platform
website: https://analyticslegends.ai/
---
