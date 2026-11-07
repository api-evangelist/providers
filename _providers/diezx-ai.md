---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Official diezX MCP server ai.diezx/diezx (v0.2.0) as published in the MCP registry: "Business Observability: process inventory, AP risk, sales temperature, savings", offered to diezX customers over st'
  name: diezX MCP Server
  slug: diezx-mcp
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/diezx-ai/hosts/diezx-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diezx-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/diezx-ai/security/diezx-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diezx-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diezx.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://app.diezx.ai/docs/mcp
created: '2026-11-05'
description: 'diezX (diezx.ai) is a business observability and AI execution company for small and mid-sized businesses. Its official MCP server, ai.diezx/diezx (v0.2.0, published to the MCP registry 2026-08-20), is described as "Business Observability: process inventory, AP risk, sales temperature, savings" and is offered to diezX customers only, served remotely over streamable HTTP at agents.diezx.ai, with documentation at app.diezx.ai/docs/mcp.'
layout: provider
modified: '2026-11-05'
name: diezX
nav: Providers
network: true
overview: 'diezX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Observability, AI Agents, MCP, and Process Automation.


  diezX''s developer surface includes documentation and 3 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diezx Ai Domain Security
  slug: diezx-ai-domain-security
  summary_line: DMARC
slug: diezx-ai
tags:
- Company
- Business Observability
- AI Agents
- MCP
- Process Automation
- Accounts Payable
- Sales Analytics
- Small Business
website: https://diezx.ai/
---
