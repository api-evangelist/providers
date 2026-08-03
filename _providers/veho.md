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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Veho Agentic Access
  operation_count: 26
  slug: veho-agentic-access
  summary_line: 26 operations · 14 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Labels
  name: Veho labels API
  slug: veho-labels-api
- description: Manifests
  name: Veho manifests API
  slug: veho-manifests-api
- description: Merchants
  name: Veho merchants API
  slug: veho-merchants-api
- description: Orders
  name: Veho orders API
  slug: veho-orders-api
- description: Packages
  name: Veho packages API
  slug: veho-packages-api
- description: Quotes
  name: Veho quotes API
  slug: veho-quotes-api
- description: Webhooks
  name: Veho webhooks API
  slug: veho-webhooks-api
- description: Serviceable Zips
  name: Veho zips API
  slug: veho-zips-api
artifact_total: 15
asyncapis:
- description: ''
  name: Veho Webhooks
  slug: veho-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.shipveho.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.shipveho.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.shipveho.com/docs/veho-api/j2rbld9w9jm76-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.shipveho.com/docs/veho-api/e777wryv1msks-veho-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.shipveho.com/docs/veho-api/j2rbld9w9jm76-introduction
- group: operate
  title: ''
  type: Support
  url: https://www.shipveho.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.shipveho.com/resource-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veho-technologies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shipveho.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shipveho.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.shipveho.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.shipveho.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/veho-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/veho-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/veho-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/veho-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/veho-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/veho-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/veho-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/veho-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/veho-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/veho-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veho-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/veho-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/veho-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/veho-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veho-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/veho-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veho-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veho-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veho-authentication.yml
created: '2026-07-17'
description: Veho is a US last-mile delivery and returns carrier built for e-commerce brands, pairing a crowdsourced driver network with purpose-built logistics software. The Veho API (Version 2) is a REST/JSON API for shippers and 3PLs to create delivery orders, manage packages and shipping labels (PDF/PNG/ZPL), quote rates, check serviceable ZIP codes, manage merchants under a client account, and subscribe to 22 package milestone webhook event types, with a full sandbox environment and bulk manifest uploads over S3 or SFTP.
image: https://cdn.prod.website-files.com/64a643946cb644441bae82c9/64a652f0e51e8362078cfd2e_Group%2055.svg
layout: provider
mcp_servers:
- description: ''
  name: veho-mcp.yml
  slug: veho-mcpyml
modified: '2026-07-21'
name: Veho
nav: Providers
network: true
overview: 'Veho publishes 8 APIs on the [APIs.io](https://apis.io/) network, including labels API, manifests API, merchants API, and 5 more. Tagged areas include Company, Logistics, Shipping, Last Mile Delivery, and Package Tracking.


  The Veho catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Veho''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, sandbox, and 25 more developer resources.'
random_paper: 54
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 75.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Veho Authentication
  slug: veho-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veho Domain Security
  slug: veho-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Veho Vulnerability Disclosure
  slug: veho-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Veho Trust Center
  slug: veho-trust-center
  summary_line: ISO 27001
slug: veho
tags:
- Company
- Logistics
- Shipping
- Last Mile Delivery
- Package Tracking
- eCommerce
- Webhooks
- Delivery
website: https://www.shipveho.com/
---
