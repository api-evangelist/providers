---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: AI/ML engineering job aggregator with REST, RSS, and MCP endpoints
  name: AI Dev Jobs
  slug: ai-dev-jobs
artifact_total: 3
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/ai-dev-jobs-a2a.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-dev-jobs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-dev-jobs-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://aidevboard.com/feed.xml
- group: company
  title: ''
  type: Website
  url: https://aidevboard.com/openapi.yaml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: AI/ML engineering job aggregator with REST, RSS, and MCP endpoints
layout: provider
modified: '2026-05-28'
name: AI Dev Jobs
nav: Providers
network: true
overview: 'AI Dev Jobs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Jobs and Public APIs.


  AI Dev Jobs'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 69
score:
  band: minimal
  composite: 5.8
  delta: -1.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-dev-jobs/refs/heads/main/screenshots/ai-dev-jobs-2026-06-20T170624.png
security:
- kind: domain-security
  name: Ai Dev Jobs Domain Security
  slug: ai-dev-jobs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ai Dev Jobs Vulnerability Disclosure
  slug: ai-dev-jobs-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ai-dev-jobs
tags:
- Jobs
- Public APIs
website: https://aidevboard.com/openapi.yaml
---
