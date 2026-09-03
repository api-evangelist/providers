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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Graylog provides a REST API for managing log data, streams, dashboards, alerts, users, and system configuration. The API is browseable via the bundled API Browser at /api/api-browser/.
  name: Graylog REST API
  slug: graylog
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Graylog2/graylog2-server/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Graylog2/graylog2-server/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Graylog2/graylog2-server/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Graylog2/graylog2-server/blob/master/CONTRIBUTING.md
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


  Graylog''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Graylog Plans Pricing
  plan_count: 3
  slug: graylog-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Graylog Rate Limits
  slug: graylog-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -6.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: falling
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
