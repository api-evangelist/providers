---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 34
  human_in_the_loop: 2
  name: Integration App Agentic Access
  operation_count: 63
  slug: integration-app-agentic-access
  summary_line: 63 operations · 34 acting · 2 human-in-the-loop
api_count: 16
apis:
- description: The Membrane platform (formerly Integration.app) provides a unified surface for building embedded and agentic integrations across 100,000+ apps with managed OAuth, observability, MCP server support, a
  name: Membrane (formerly Integration.app) Platform
  slug: platform
- description: The Actions API from Integration.app (Membrane) — 2 operation(s) for actions.
  name: Integration.app (Membrane) Actions API
  slug: integration-app-actions-api
- description: The App Event Subscriptions API from Integration.app (Membrane) — 2 operation(s) for app event subscriptions.
  name: Integration.app (Membrane) App Event Subscriptions API
  slug: integration-app-app-event-subscriptions-api
- description: The Connections API from Integration.app (Membrane) — 7 operation(s) for connections.
  name: Integration.app (Membrane) Connections API
  slug: integration-app-connections-api
- description: The Connectors API from Integration.app (Membrane) — 3 operation(s) for connectors.
  name: Integration.app (Membrane) Connectors API
  slug: integration-app-connectors-api
- description: The Customers API from Integration.app (Membrane) — 2 operation(s) for customers.
  name: Integration.app (Membrane) Customers API
  slug: integration-app-customers-api
- description: The Data Collections API from Integration.app (Membrane) — 2 operation(s) for data collections.
  name: Integration.app (Membrane) Data Collections API
  slug: integration-app-data-collections-api
- description: The External Event Subscriptions API from Integration.app (Membrane) — 2 operation(s) for external event subscriptions.
  name: Integration.app (Membrane) External Event Subscriptions API
  slug: integration-app-external-event-subscriptions-api
- description: The Field Mappings API from Integration.app (Membrane) — 2 operation(s) for field mappings.
  name: Integration.app (Membrane) Field Mappings API
  slug: integration-app-field-mappings-api
- description: The Flow Runs API from Integration.app (Membrane) — 5 operation(s) for flow runs.
  name: Integration.app (Membrane) Flow Runs API
  slug: integration-app-flow-runs-api
- description: The Flows API from Integration.app (Membrane) — 2 operation(s) for flows.
  name: Integration.app (Membrane) Flows API
  slug: integration-app-flows-api
- description: The Integrations API from Integration.app (Membrane) — 2 operation(s) for integrations.
  name: Integration.app (Membrane) Integrations API
  slug: integration-app-integrations-api
- description: The Logs API from Integration.app (Membrane) — 3 operation(s) for logs.
  name: Integration.app (Membrane) Logs API
  slug: integration-app-logs-api
- description: The Public API from Integration.app (Membrane) — 3 operation(s) for public.
  name: Integration.app (Membrane) Public API
  slug: integration-app-public-api
- description: The Search API from Integration.app (Membrane) — 2 operation(s) for search.
  name: Integration.app (Membrane) Search API
  slug: integration-app-search-api
- description: The Sessions API from Integration.app (Membrane) — 4 operation(s) for sessions.
  name: Integration.app (Membrane) Sessions API
  slug: integration-app-sessions-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions API
  slug: open-integration-app-actions-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions App Event Subscriptions API
  slug: open-integration-app-app-event-subscriptions-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Connections API
  slug: open-integration-app-connections-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Connectors API
  slug: open-integration-app-connectors-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Customers API
  slug: open-integration-app-customers-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Data Collections API
  slug: open-integration-app-data-collections-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions External Event Subscriptions API
  slug: open-integration-app-external-event-subscriptions-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Field Mappings API
  slug: open-integration-app-field-mappings-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Flow Runs API
  slug: open-integration-app-flow-runs-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Flows API
  slug: open-integration-app-flows-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Integrations API
  slug: open-integration-app-integrations-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Logs API
  slug: open-integration-app-logs-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Public API
  slug: open-integration-app-public-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Search API
  slug: open-integration-app-search-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform Actions Sessions API
  slug: open-integration-app-sessions-api
- collection_type: open
  name: Membrane (formerly Integration.app) Platform API
  slug: open-integration-app
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/integration-app-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/integration-app-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integration-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/integration-app-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://getmembrane.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmembrane.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getmembrane.com/reference/overview/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://getmembrane.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://getmembrane.com/articles
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.getmembrane.com
- group: start
  title: ''
  type: Signup
  url: https://console.getmembrane.com
- group: start
  title: ''
  type: Login
  url: https://console.getmembrane.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmembrane.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.getmembrane.com
- group: commercial
  title: ''
  type: Privacy
  url: https://getmembrane.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getmembrane.com/terms-and-conditions
- group: company
  title: ''
  type: About
  url: https://getmembrane.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/membrane
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/membranehq
- group: other
  title: ''
  type: X
  url: https://x.com/membrane_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getmembrane
created: '2026-03-27'
description: Integration.app, now operating as Membrane (getmembrane.com), is an agentic integration infrastructure platform that lets AI agents, products, and internal tools connect with 100,000+ applications through a unified interface. It exposes integrations via API, CLI, SDK, MCP servers, and embedded UI, with managed authentication, observability, self-hosting, and enterprise compliance (SOC 2 Type II, GDPR).
finops:
- name: Integration App Finops
  service_category: API
  slug: integration-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/integration-app.png
layout: provider
modified: '2026-04-28'
name: Integration.app (Membrane)
nav: Providers
network: true
overview: 'Integration.app (Membrane) publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Actions API, App Event Subscriptions API, Connections API, and 12 more. Tagged areas include Agentic Integrations, AI Agents, Connectors, Embedded Integrations, and Embedded iPaaS.


  The Integration.app (Membrane) catalog on APIs.io includes 1 Spectral governance ruleset.


  Integration.app (Membrane)''s developer surface includes authentication, developer portal, documentation, API reference, pricing, engineering blog, changelog, and 14 more developer resources.'
plans:
- name: Integration App Plans Pricing
  plan_count: 3
  slug: integration-app-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Integration App Rate Limits
  slug: integration-app-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Integration.app (Membrane) API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: integration-app-rules
score:
  band: developing
  composite: 41.8
  delta: -7.5
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/integration-app/refs/heads/main/screenshots/integration-app-2026-06-20T183430.png
security:
- kind: authentication
  name: Integration App Authentication
  slug: integration-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Integration App Domain Security
  slug: integration-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Integration App Trust Center
  slug: integration-app-trust-center
  summary_line: SOC 2, GDPR
slug: integration-app
tags:
- Agentic Integrations
- AI Agents
- Connectors
- Embedded Integrations
- Embedded iPaaS
- Integration Marketplace
- MCP
- Model Context Protocol
- Self-Hosting
- Unified API
website: https://getmembrane.com
---
