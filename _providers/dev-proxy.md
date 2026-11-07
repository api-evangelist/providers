---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
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
  name: Dev Proxy API
  slug: dev-proxy-proxy-api
artifact_total: 22
collections:
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
- group: commercial
  href: https://artifacts.apis.io/dev-proxy/plans/dev-proxy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dev-proxy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dev-proxy/rate-limits/dev-proxy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dev-proxy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dev-proxy/finops/dev-proxy-finops.yml
  title: ''
  type: FinOps
  url: finops/dev-proxy-finops.yml
- group: agent
  href: https://artifacts.apis.io/dev-proxy/agentic-access/dev-proxy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dev-proxy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dev-proxy/security/dev-proxy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dev-proxy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dev-proxy/security/dev-proxy-domain-security.yml
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
- has_sources: false
  method: generated
  name: Dev Proxy Finops
  primary_unit: request
  service_category: API
  slug: dev-proxy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dev-proxy.png
layout: provider
modified: '2026-09-16'
name: Dev Proxy
nav: Providers
network: true
overview: 'Dev Proxy publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including JWT API, and 2 more. Tagged areas include Debugging Proxy and Proxy.


  The Dev Proxy catalog on APIs.io includes 1 Spectral governance ruleset.


  Dev Proxy''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Dev Proxy Plans Pricing
  plan_count: 3
  slug: dev-proxy-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Dev Proxy Rate Limits
  slug: dev-proxy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Dev Proxy API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: dev-proxy-rules
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.5
    catalog_earned_first_party: 0.0
    catalog_gap: 82.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 36.1
    developer_ergonomics: 18.3
    discoverability: 39.3
    operational_transparency: 21.1
  previous_composite: 21.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dev-proxy/dev-proxy-2026-06-20T175945.png
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
