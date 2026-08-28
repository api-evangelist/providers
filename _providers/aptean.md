---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Aptean Agentic Access
  operation_count: 14
  slug: aptean-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 5
apis:
- description: The Consumers API from Aptean — 2 operation(s) for consumers.
  name: Aptean Consumers API
  slug: aptean-consumers-api
- description: The EventDefinitions API from Aptean — 2 operation(s) for eventdefinitions.
  name: Aptean EventDefinitions API
  slug: aptean-eventdefinitions-api
- description: The Events API from Aptean — 3 operation(s) for events.
  name: Aptean Events API
  slug: aptean-events-api
- description: The Producers API from Aptean — 2 operation(s) for producers.
  name: Aptean Producers API
  slug: aptean-producers-api
- description: The PublicKeys API from Aptean — 1 operation(s) for publickeys.
  name: Aptean PublicKeys API
  slug: aptean-publickeys-api
artifact_total: 17
asyncapis:
- description: ''
  name: Aptean Events Webhooks
  slug: aptean-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aptean Integration Platform Consumers API
  slug: open-aptean-consumers-api
- collection_type: open
  name: Aptean Integration Platform Consumers EventDefinitions API
  slug: open-aptean-eventdefinitions-api
- collection_type: open
  name: Aptean Integration Platform Consumers Events API
  slug: open-aptean-events-api
- collection_type: open
  name: Aptean Integration Platform Consumers Producers API
  slug: open-aptean-producers-api
- collection_type: open
  name: Aptean Integration Platform Consumers PublicKeys API
  slug: open-aptean-publickeys-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/aptean-integration-platform-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aptean-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aptean-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptean-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aptean-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aptean-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aptean-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.aptean.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/aptean-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aptean-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aptean-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aptean-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aptean-sandbox.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Aptean/integration-services
- group: docs
  title: ''
  type: APIReference
  url: https://stg.integration-graph.apteansharedservices.com/swagger/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aptean
- group: company
  title: ''
  type: Blog
  url: https://www.aptean.com/en-US/insights
- group: operate
  title: ''
  type: Support
  url: https://www.aptean.com/en-US/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aptean.com/en-US/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptean.com/en-US/privacy-statement
- group: company
  title: ''
  type: Website
  url: https://www.aptean.com/en-US/
created: '2026-07-17'
description: Aptean is a global provider of industry-specific, AI-powered enterprise software — ERP, CRM, supply chain and compliance solutions — for manufacturing, distribution, food & beverage, transportation and other complex industries. Headquartered in Alpharetta, Georgia and backed by Insight Partners, Aptean serves roughly 5,000 customers worldwide. Its developer-facing surface is the Aptean Integration Platform (AIP), an event/webhook integration API where products publish events against event definitions and consumer tenants subscribe to receive them, secured with Bearer JWT and APIM subscription headers.
image: https://images.ctfassets.net/grb5fvwhwnyo/6dl4ftg2p3o3438k9XcowL/feecf05daaad11081daa4b57173423a8/Default-og-image.webp
layout: provider
mcp_servers:
- description: ''
  name: Aptean MCP Server
  slug: aptean-mcp-server
modified: '2026-07-18'
name: Aptean
nav: Providers
network: true
overview: 'Aptean publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Consumers API, EventDefinitions API, Events API, and 2 more. Tagged areas include Company, Manufacturing, ERP, Supply Chain, and Integration.


  The Aptean catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aptean''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, support, and 16 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 43.3
  delta: 1.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 30.3
    contract_quality: 55.5
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aptean/refs/heads/main/screenshots/aptean-2026-07-25T200918.png
security:
- kind: authentication
  name: Aptean Authentication
  slug: aptean-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aptean Domain Security
  slug: aptean-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aptean Trust Center
  slug: aptean-trust-center
  summary_line: SOC 2 Type II, ISO 27001, NIST 800
slug: aptean
tags:
- Company
- Manufacturing
- ERP
- Supply Chain
- Integration
- Event-Driven
- Webhook
- Enterprise Software
website: https://www.aptean.com/en-US/
---
