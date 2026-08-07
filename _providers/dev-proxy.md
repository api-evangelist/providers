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
    agent_skills: true
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
  score: 26.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 2
  name: Dev Proxy Agentic Access
  operation_count: 6
  slug: dev-proxy-agentic-access
  summary_line: 6 operations · 4 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Dev Proxy is a Microsoft command-line tool for simulating, testing, and debugging API interactions during development.
  name: Dev Proxy
  slug: dev-proxy
- description: The JWT API from Dev Proxy — 1 operation(s) for jwt.
  name: Dev Proxy JWT API
  slug: dev-proxy-jwt-api
- description: The Proxy API from Dev Proxy — 4 operation(s) for proxy.
  name: Dev Proxy Proxy API
  slug: dev-proxy-proxy-api
artifact_total: 19
collections:
- collection_type: open
  name: Microsoft Dev Proxy — Proxy API
  slug: open-dev-proxy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dev-proxy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dev-proxy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dev-proxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/dev-proxy
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/microsoft/win-dev-skills
created: '2026-03-27'
description: Dev Proxy is a Microsoft command-line tool for simulating, testing, and debugging API interactions during development.
finops:
- name: Dev Proxy Finops
  service_category: API
  slug: dev-proxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dev-proxy.png
layout: provider
modified: '2026-05-19'
name: Dev Proxy
nav: Providers
network: true
overview: 'Dev Proxy publishes 2 APIs on the [APIs.io](https://apis.io/) network: JWT API and Proxy API. Tagged areas include Debugging Proxy and Proxy.


  Dev Proxy''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dev Proxy Plans Pricing
  plan_count: 3
  slug: dev-proxy-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Dev Proxy Rate Limits
  slug: dev-proxy-rate-limits
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.7
    developer_ergonomics: 8.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dev-proxy/refs/heads/main/screenshots/dev-proxy-2026-06-20T175945.png
security:
- kind: domain-security
  name: Dev Proxy Domain Security
  slug: dev-proxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dev Proxy Vulnerability Disclosure
  slug: dev-proxy-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 9
skills:
- name: pr-review
  slug: pr-review
- name: winui-code-review
  slug: winui-code-review
- name: winui-design
  slug: winui-design
- name: winui-dev-workflow
  slug: winui-dev-workflow
- name: winui-packaging
  slug: winui-packaging
- name: winui-session-report
  slug: winui-session-report
- name: winui-setup
  slug: winui-setup
- name: winui-ui-testing
  slug: winui-ui-testing
- name: winui-wpf-migration
  slug: winui-wpf-migration
slug: dev-proxy
tags:
- Debugging Proxy
- Proxy
website: https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/overview
---
