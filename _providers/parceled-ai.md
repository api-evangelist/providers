---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Parceled Ai Agentic Access
  operation_count: 1
  slug: parceled-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://www.parceled.ai
  baseurl_source: declared
  description: Balance, pricing, and usage info (free).
  name: parceled-ai Account API
  slug: parceled-ai-account-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/parceled-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/parceled-ai/agentic-access/parceled-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/parceled-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/parceled-ai/plans/parceled-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parceled-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/parceled-ai/rules/parceled-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/parceled-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/parceled-ai/vocabulary/parceled-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/parceled-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/parceled-ai/conformance/parceled-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parceled-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/parceled-ai/llms/parceled-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parceled-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/parceled-ai/mcp/parceled-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/parceled-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/parceled-ai/well-known/parceled-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parceled-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/parceled-ai/hosts/parceled-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parceled-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/parceled-ai/vendors/parceled-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/parceled-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/parceled-ai/security/parceled-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parceled-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parceled.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.parceled.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parceled.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parceled.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parceled.ai/tos
- group: start
  title: ''
  type: SignUp
  url: https://www.parceled.ai/api/parceled
created: '2026-10-30'
description: Parceled.ai provides a comprehensive suite of APIs delivering US property data, including parcel boundaries, tax assessor records, ownership details, building permits, zoning information, and hail history. The platform enables developers to integrate rich real‑estate datasets into applications, supporting use cases from mapping and analytics to AI agents accessing property information. Free tier and pay‑as‑you‑go pricing are available, with extensive documentation and support resources.
image: https://www.parceled.ai/logo-icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.parceled.ai requiring OAuth.
  name: parceled-ai MCP Server
  slug: parceled-ai-mcp-yml
modified: '2026-10-30'
name: parceled-ai
nav: Providers
network: true
overview: 'parceled-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Account API. Tagged areas include Company, RealEstate, DataAPI, Mapping, and AI.


  The parceled-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  parceled-ai''s developer surface includes documentation, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Parceled Ai Plans Pricing
  plan_count: 3
  slug: parceled-ai-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: parceled-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: parceled-ai-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 40.4
    developer_ergonomics: 16.0
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Parceled Ai Domain Security
  slug: parceled-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parceled-ai
tags:
- Company
- RealEstate
- DataAPI
- Mapping
- AI
website: https://parceled.ai/
---
