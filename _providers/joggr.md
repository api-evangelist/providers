---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Joggr is a documentation platform purpose-built for software teams, helping engineering teams create and maintain technical documentation. Joggr exposes APIs and a Model Context Protocol (MCP) server '
  name: Joggr
  slug: joggr
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joggr-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/joggr
- group: company
  title: ''
  type: Website
  url: https://www.joggr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joggr.ai/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.joggr.ai/llms.txt
created: '2025-03-01'
description: Joggr is a documentation platform purpose-built for software teams. It bridges the gap between traditional dev docs and modern development workflows, helping engineering teams create and maintain technical documentation. Joggr ships native MCP integration with AI coding agents (Claude Code, Cursor, Windsurf) and APIs for building custom Slackbots, agents, and workflows on top of the platform. The primary domain has moved from joggr.io to joggr.ai.
finops:
- name: Joggr Finops
  service_category: API
  slug: joggr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/joggr.png
layout: provider
modified: '2026-04-28'
name: Joggr
nav: Providers
network: true
overview: 'Joggr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Documentation, Technical Writing, AI Coding Agents, and MCP.


  Joggr''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Joggr Plans Pricing
  plan_count: 3
  slug: joggr-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Joggr Rate Limits
  slug: joggr-rate-limits
score:
  band: minimal
  composite: 10.8
  delta: 0.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 10.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/joggr/refs/heads/main/screenshots/joggr-2026-06-20T183747.png
security:
- kind: domain-security
  name: Joggr Domain Security
  slug: joggr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: joggr
tags:
- Developer Tools
- Documentation
- Technical Writing
- AI Coding Agents
- MCP
website: https://www.joggr.ai/
---
