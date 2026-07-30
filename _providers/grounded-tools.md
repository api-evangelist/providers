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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Grounded Tools Agentic Access
  operation_count: 3
  slug: grounded-tools-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: Model Context Protocol transport endpoints for connecting AI assistants. Supports SSE and streamable HTTP transports.
  name: Grounded.tools MCP Transport API
  slug: grounded-tools-mcp-transport-api
- description: Web-based management interface for documentation sources, library browsing, job monitoring, and search.
  name: Grounded.tools Web UI API
  slug: grounded-tools-web-ui-api
artifact_total: 14
collections:
- collection_type: open
  name: grounded.tools Docs MCP Server API
  slug: open-grounded-tools-docs-mcp-server
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grounded-tools-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grounded-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grounded.tools/
created: '2026-01-02'
description: Grounded.tools (Grounded Docs MCP Server) is an open-source, privacy-first documentation indexing tool that keeps AI assistants informed with up-to-date, version-specific documentation from multiple sources.
finops:
- name: Grounded Tools Finops
  service_category: API
  slug: grounded-tools-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grounded-tools.png
json_schemas:
- name: grounded.tools Job
  property_count: 9
  slug: job
- name: grounded.tools Library
  property_count: 2
  slug: library
- name: grounded.tools Search Result
  property_count: 2
  slug: search-result
- name: grounded.tools Version
  property_count: 6
  slug: version
jsonld:
- class_count: 0
  name: Grounded Tools Context
  property_count: 4
  slug: grounded-tools-context
layout: provider
modified: '2026-05-19'
name: Grounded.tools
nav: Providers
network: true
overview: 'Grounded.tools publishes 2 APIs on the [APIs.io](https://apis.io/) network: MCP Transport API and Web UI API. Tagged areas include Developer Tools, Developers, Documentation, and Experience.


  The Grounded.tools catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Grounded Tools Plans Pricing
  plan_count: 3
  slug: grounded-tools-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Grounded Tools Rate Limits
  slug: grounded-tools-rate-limits
rules:
- name: Grounded.tools API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: grounded-tools-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.6
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grounded-tools/refs/heads/main/screenshots/grounded-tools-2026-06-20T182414.png
security:
- kind: domain-security
  name: Grounded Tools Domain Security
  slug: grounded-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: grounded-tools
tags:
- Developer Tools
- Developers
- Documentation
- Experience
website: https://grounded.tools/
---
