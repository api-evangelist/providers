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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 2
  name: Dev Proxy Agentic Access
  operation_count: 6
  slug: dev-proxy-agentic-access
  summary_line: 6 operations · 4 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Dev Proxy is a Microsoft command-line tool for simulating, testing, and debugging API interactions during development.
  name: Dev Proxy
  slug: dev-proxy
- baseURL: http://localhost:8897
  baseurl_source: spec
  description: The JWT API from Dev Proxy — 1 operation(s) for jwt.
  name: Dev Proxy JWT API
  slug: dev-proxy-jwt-api
- baseURL: http://localhost:8897
  baseurl_source: spec
  description: The Proxy API from Dev Proxy — 4 operation(s) for proxy.
  name: Dev Proxy Proxy API
  slug: dev-proxy-proxy-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Dev Proxy — Proxy JWT API
  slug: open-dev-proxy-jwt-api
- collection_type: open
  name: Microsoft Dev — JWT Proxy API
  slug: open-dev-proxy-proxy-api
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
random_paper: 18
rate_limits:
- limit_count: 5
  name: Dev Proxy Rate Limits
  slug: dev-proxy-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 40.1
    developer_ergonomics: 19.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
