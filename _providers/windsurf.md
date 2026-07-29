---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Windsurf Agentic Access
  operation_count: 6
  slug: windsurf-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 8
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
- description: The CascadeAnalytics API from Windsurf — 1 operation(s) for cascadeanalytics.
  name: Windsurf CascadeAnalytics API
  slug: windsurf-cascadeanalytics-api
- description: The CreditBalance API from Windsurf — 1 operation(s) for creditbalance.
  name: Windsurf CreditBalance API
  slug: windsurf-creditbalance-api
- description: The CustomAnalytics API from Windsurf — 1 operation(s) for customanalytics.
  name: Windsurf CustomAnalytics API
  slug: windsurf-customanalytics-api
- description: The UsageConfiguration API from Windsurf — 2 operation(s) for usageconfiguration.
  name: Windsurf UsageConfiguration API
  slug: windsurf-usageconfiguration-api
- description: The UserAnalytics API from Windsurf — 1 operation(s) for useranalytics.
  name: Windsurf UserAnalytics API
  slug: windsurf-useranalytics-api
artifact_total: 17
collections:
- collection_type: open
  name: Windsurf Enterprise Analytics API
  slug: open-windsurf
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windsurf-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/windsurf-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/windsurf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windsurf-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/windsurf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/windsurf-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/windsurf-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.windsurf.com/llms.txt
created: '2026-05-08'
description: Windsurf (formerly Codeium) is the AI-native code editor and plugin family from the Codeium team, featuring Cascade - an agentic chatbot that collaborates with the user across files. Built on a VS Code base with proprietary inference, MCP server support, Devin Cloud sessions, and the SWE-1.5 fast agent model. Plans range from Free / Light / Pro / Max / Teams / Enterprise. No public REST API for application developers.
finops:
- name: Windsurf Finops
  service_category: AI
  slug: windsurf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windsurf.png
layout: provider
modified: '2026-05-08'
name: Windsurf
nav: Providers
network: true
overview: 'Windsurf publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CascadeAnalytics API, CreditBalance API, CustomAnalytics API, and 2 more. Tagged areas include AI, Developer Tools, Code Editor, Agent, and Cascade.


  Windsurf''s developer surface includes authentication, engineering blog, documentation, pricing, and 10 more developer resources.'
plans:
- name: Windsurf Plans Pricing
  plan_count: 1
  slug: windsurf-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Windsurf Rate Limits
  slug: windsurf-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/windsurf/refs/heads/main/screenshots/windsurf-2026-06-20T201508.png
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
  summary_line: disclosure policy published
- kind: trust-center
  name: Windsurf Trust Center
  slug: windsurf-trust-center
  summary_line: SOC 2, ISO 27001
slug: windsurf
tags:
- AI
- Developer Tools
- Code Editor
- Agent
- Cascade
- IDE
- MCP
website: https://windsurf.com/
---
