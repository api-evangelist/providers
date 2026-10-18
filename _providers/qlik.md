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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Qlik Agentic Access
  operation_count: 48
  slug: qlik-agentic-access
  summary_line: 48 operations · 24 acting
api_count: 1
apis:
- description: Qlik provides APIs to support automation, configuration, observability, and integration with third-party applications to incorporate Qlik Cloud capabilities directly into those applications.
  name: Qlik
  slug: qlik
- description: Manages IP restriction policies for controlling network access to the Qlik Cloud tenant.
  name: Qlik IP Policies API
  slug: ip-policies
- description: Manages change store configurations for tracking and storing changes in analytics data.
  name: Qlik Change Stores API
  slug: change-stores
- description: Manages data products within the Qlik data governance framework, enabling the packaging and sharing of curated data assets.
  name: Qlik Data Products API
  slug: data-products
- description: The JSON-RPC API over WebSocket that enables interaction with the Qlik Associative Engine for Qlik Sense applications, providing session-based access to app data models, objects, and calculations.
  name: Qlik Engine JSON-RPC API
  slug: qix
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The Apps API from Qlik — 22 operation(s) for apps.
  name: Qlik Apps API
  slug: qlik-apps-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The evaluation API from Qlik — 5 operation(s) for evaluation.
  name: Qlik Evaluation API
  slug: qlik-evaluation-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The filters API from Qlik — 3 operation(s) for filters.
  name: Qlik Filters API
  slug: qlik-filters-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The insight-analyses API from Qlik — 3 operation(s) for insight-analyses.
  name: Qlik Insight Analyses API
  slug: qlik-insight-analyses-api
artifact_total: 18
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/plans/qlik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qlik-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/finops/qlik-finops.yml
  title: ''
  type: FinOps
  url: finops/qlik-finops.yml
- group: company
  title: ''
  type: Website
  url: https://qlik.dev
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/security/qlik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qlik-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qlik
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/get-started
- group: build
  title: ''
  type: SDKs
  url: https://qlik.dev/toolkits/qlik-api/
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: docs
  title: ''
  type: Documentation
  url: https://qlik.dev/apis/rest/
- group: operate
  title: ''
  type: RateLimits
  url: https://qlik.dev/apis/rest/rate-limiting/
- group: build
  title: ''
  type: CodeExamples
  url: https://qlik.dev/examples/
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com/
- group: company
  title: ''
  type: Blog
  url: https://community.qlik.com/t5/Qlik-Design-Blog/bg-p/qlik-design-blog
- group: operate
  title: ''
  type: Community
  url: https://community.qlik.com
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/license-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/qlik-oss/qlik-mcp-registry
created: '2025-02-24'
description: APIs for Qlik's analytics and data integration platform.
finops:
- has_sources: false
  method: generated
  name: Qlik Finops
  primary_unit: ''
  service_category: API
  slug: qlik-finops
  template: true
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
jsonld:
- class_count: 96
  name: Qlik Context
  property_count: 275
  slug: qlik-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: Qlik
nav: Providers
network: true
overview: 'Qlik publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Evaluation API, Filters API, and 6 more. Tagged areas include Security, Access Control, Machine Learning, and Artificial Intelligence.


  The Qlik catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qlik''s developer surface includes authentication, getting-started guide, CLI, documentation, code examples, changelog, engineering blog, and 15 more developer resources.'
plans:
- name: Qlik Plans Pricing
  plan_count: 3
  slug: qlik-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Qlik Rate Limits
  slug: qlik-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Qlik API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 2
  slug: qlik-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 43.5
    catalog_earned_first_party: 0.0
    catalog_gap: 71.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 52.4
    discoverability: 39.3
    operational_transparency: 44.7
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/screenshots/qlik-2026-06-20T192340.png
security:
- kind: authentication
  name: Qlik Authentication
  slug: qlik-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qlik Domain Security
  slug: qlik-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: qlik
tags:
- Security
- Access Control
- Machine Learning
- Artificial Intelligence
website: https://qlik.dev
---
