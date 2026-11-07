---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Windsurf Agentic Access
  operation_count: 6
  slug: windsurf-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: Standalone AI-native IDE forked from VS Code featuring Cascade agent, autocomplete (Fill-In-The-Middle), Chat, Command, MCP server integration, and Devin Cloud sessions for background development. SWE
  name: Windsurf Editor
  slug: editor
- description: VS Code, JetBrains, Vim, Emacs, Visual Studio, Sublime Text plugins. Surface autocomplete, chat, and command capabilities backed by Windsurf's hosted inference.
  name: Windsurf Plugins
  slug: plugins
- description: Self-hosted / managed enterprise SKU with admin dashboards, analytics, RBAC, and SSO.
  name: Windsurf Enterprise (Codeium for Enterprise)
  slug: enterprise
- baseURL: https://server.codeium.com/api/v1
  baseurl_source: declared
  description: The CascadeAnalytics API from Windsurf — 1 operation(s) for cascadeanalytics.
  name: Windsurf CascadeAnalytics API
  slug: windsurf-cascadeanalytics-api
- baseURL: https://server.codeium.com/api/v1
  baseurl_source: declared
  description: The CreditBalance API from Windsurf — 1 operation(s) for creditbalance.
  name: Windsurf CreditBalance API
  slug: windsurf-creditbalance-api
- baseURL: https://server.codeium.com/api/v1
  baseurl_source: declared
  description: The CustomAnalytics API from Windsurf — 1 operation(s) for customanalytics.
  name: Windsurf CustomAnalytics API
  slug: windsurf-customanalytics-api
- baseURL: https://server.codeium.com/api/v1
  baseurl_source: declared
  description: The UsageConfiguration API from Windsurf — 2 operation(s) for usageconfiguration.
  name: Windsurf UsageConfiguration API
  slug: windsurf-usageconfiguration-api
- baseURL: https://server.codeium.com/api/v1
  baseurl_source: declared
  description: The User Analytics API from Windsurf — 1 operation(s) for user analytics.
  name: Windsurf User Analytics API
  slug: windsurf-user-analytics-api
artifact_total: 24
collections:
- collection_type: open
  name: Windsurf Enterprise Analytics CascadeAnalytics API
  slug: open-windsurf-cascadeanalytics-api
- collection_type: open
  name: Windsurf Enterprise Analytics CascadeAnalytics CreditBalance API
  slug: open-windsurf-creditbalance-api
- collection_type: open
  name: Windsurf Enterprise Analytics CascadeAnalytics CustomAnalytics API
  slug: open-windsurf-customanalytics-api
- collection_type: open
  name: Windsurf Enterprise Analytics CascadeAnalytics UsageConfiguration API
  slug: open-windsurf-usageconfiguration-api
- collection_type: open
  name: Windsurf Enterprise Analytics CascadeAnalytics UserAnalytics API
  slug: open-windsurf-useranalytics-api
- collection_type: open
  name: Windsurf Enterprise Analytics API
  slug: open-windsurf
common:
- group: other
  href: https://artifacts.apis.io/windsurf/capabilities/windsurf-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/windsurf-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/windsurf/agentic-access/windsurf-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/windsurf-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/windsurf/security/windsurf-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/windsurf-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/windsurf/security/windsurf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/windsurf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/windsurf/security/windsurf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/windsurf-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/windsurf/authentication/windsurf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/windsurf-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://windsurf.com/feed.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/windsurf123321
- group: company
  title: ''
  type: Website
  url: https://windsurf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.windsurf.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://windsurf.com/pricing
- group: commercial
  href: https://artifacts.apis.io/windsurf/plans/windsurf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/windsurf-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/windsurf/rate-limits/windsurf-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/windsurf-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/windsurf/finops/windsurf-finops.yml
  title: ''
  type: FinOps
  url: finops/windsurf-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.windsurf.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.windsurf.com/plugins/accounts/api-reference/api-introduction
- group: company
  title: ''
  type: Blog
  url: https://windsurf.com/blog
created: '2026-05-08'
description: Windsurf (formerly Codeium) is the AI-native code editor and plugin family from the Codeium team, featuring Cascade - an agentic chatbot that collaborates with the user across files. Built on a VS Code base with proprietary inference, MCP server support, Devin Cloud sessions, and the SWE-1.5 fast agent model. Plans range from Free / Light / Pro / Max / Teams / Enterprise. No public REST API for application developers.
finops:
- has_sources: true
  method: generated
  name: Windsurf Finops
  primary_unit: ''
  service_category: AI
  slug: windsurf-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windsurf.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.windsurf.com over HTTP; 3 tools listed.
  name: Windsurf MCP Server
  slug: windsurf
modified: '2026-05-08'
name: Windsurf
nav: Providers
network: true
overview: 'Windsurf publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including CascadeAnalytics API, CreditBalance API, CustomAnalytics API, and 5 more. Tagged areas include Artificial Intelligence, Developer Tools, Code Editor, Agents, and Cascade.


  The Windsurf catalog on APIs.io includes 1 Spectral governance ruleset.


  Windsurf''s developer surface includes authentication, engineering blog, documentation, pricing, API reference, and 12 more developer resources.'
plans:
- name: Windsurf Plans Pricing
  plan_count: 5
  slug: windsurf-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Windsurf Rate Limits
  slug: windsurf-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Windsurf API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: windsurf-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 50.5
    catalog_earned_first_party: 12.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 49.0
    developer_ergonomics: 31.0
    discoverability: 66.7
    operational_transparency: 15.8
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/windsurf/windsurf-2026-06-20T201508.png
security:
- kind: authentication
  name: Windsurf Authentication
  slug: windsurf-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Windsurf Domain Security
  slug: windsurf-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Windsurf Vulnerability Disclosure
  slug: windsurf-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Windsurf Trust Center
  slug: windsurf-trust-center
  summary_line: SOC 2, ISO 27001
slug: windsurf
tags:
- Artificial Intelligence
- Developer Tools
- Code Editor
- Agents
- Cascade
- IDE
- MCP
website: https://windsurf.com/
---
