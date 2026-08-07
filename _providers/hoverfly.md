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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Hoverfly Agentic Access
  operation_count: 42
  slug: hoverfly-agentic-access
  summary_line: 42 operations · 23 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Inspect and clear the cache of matched request-response pairs.
  name: Hoverfly Cache API
  slug: hoverfly-cache-api
- description: Inspect and clear response difference reports.
  name: Hoverfly Diff API
  slug: hoverfly-diff-api
- description: Manage Hoverfly runtime configuration.
  name: Hoverfly Hoverfly API
  slug: hoverfly-hoverfly-api
- description: Inspect and filter the journal of intercepted requests.
  name: Hoverfly Journal API
  slug: hoverfly-journal-api
- description: Retrieve runtime logs.
  name: Hoverfly Logs API
  slug: hoverfly-logs-api
- description: Manage post-serve actions executed after responses are served.
  name: Hoverfly Post-Serve Actions API
  slug: hoverfly-post-serve-actions-api
- description: Manage simulation request-response pairs and metadata.
  name: Hoverfly Simulation API
  slug: hoverfly-simulation-api
- description: Manage stateful keys used during simulation.
  name: Hoverfly State API
  slug: hoverfly-state-api
- description: System-level controls.
  name: Hoverfly System API
  slug: hoverfly-system-api
- description: Manage CSV-based templating data sources.
  name: Hoverfly Templating Data API
  slug: hoverfly-templating-data-api
artifact_total: 16
collections:
- collection_type: open
  name: Hoverfly Admin API
  slug: open-hoverfly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hoverfly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hoverfly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hoverfly
- group: company
  title: ''
  type: Website
  url: https://hoverfly.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hoverfly.io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SpectoLabs/hoverfly
created: '2026-03-25'
description: Hoverfly is an open source API simulation tool for creating realistic mock services and capturing-replaying HTTP traffic for testing.
finops:
- name: Hoverfly Finops
  service_category: API
  slug: hoverfly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hoverfly.png
layout: provider
modified: '2026-05-19'
name: Hoverfly
nav: Providers
network: true
overview: 'Hoverfly publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Cache API, Diff API, Hoverfly API, and 7 more. Tagged areas include Mocking and Testing.


  Hoverfly''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Hoverfly Plans Pricing
  plan_count: 3
  slug: hoverfly-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Hoverfly Rate Limits
  slug: hoverfly-rate-limits
score:
  band: thin
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.7
    developer_ergonomics: 8.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hoverfly/refs/heads/main/screenshots/hoverfly-2026-06-20T182852.png
security:
- kind: domain-security
  name: Hoverfly Domain Security
  slug: hoverfly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hoverfly
tags:
- Mocking
- Testing
website: https://hoverfly.io
---
