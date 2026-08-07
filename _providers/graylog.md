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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Graylog provides a REST API for managing log data, streams, dashboards, alerts, users, and system configuration. The API is browseable via the bundled API Browser at /api/api-browser/.
  name: Graylog REST API
  slug: graylog
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graylog-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graylog
- group: company
  title: ''
  type: Website
  url: https://graylog.org
- group: docs
  title: ''
  type: Documentation
  url: https://go2docs.graylog.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Graylog2
- group: company
  title: ''
  type: Blog
  url: https://graylog.org/post/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Graylog2/graylog-mcp-registry
- group: agent
  title: ''
  type: LlmsText
  url: https://graylog.org/llms.txt
created: '2026-03-25'
description: Graylog is an open source log management platform for collecting, indexing, and analyzing log data with alerting and dashboard capabilities.
finops:
- name: Graylog Finops
  service_category: API
  slug: graylog-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graylog.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Graylog
nav: Providers
network: true
overview: 'Graylog publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logging, Observability, Log Management, and SIEM.


  Graylog''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Graylog Plans Pricing
  plan_count: 3
  slug: graylog-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 5
  name: Graylog Rate Limits
  slug: graylog-rate-limits
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graylog/refs/heads/main/screenshots/graylog-2026-06-20T182348.png
security:
- kind: domain-security
  name: Graylog Domain Security
  slug: graylog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: graylog
tags:
- Logging
- Observability
- Log Management
- SIEM
website: https://graylog.org
---
