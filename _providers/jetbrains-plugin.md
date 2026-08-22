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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jetbrains Plugin Agentic Access
  operation_count: 3
  slug: jetbrains-plugin-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: REST API for listing available plugins, uploading new plugin builds, and downloading plugin updates from the JetBrains Marketplace. Permanent tokens are issued from the My Tokens tab in the marketplac
  name: JetBrains Marketplace API
  slug: marketplace-api
- description: The Plugins API from JetBrains Marketplace — 2 operation(s) for plugins.
  name: JetBrains Marketplace Plugins API
  slug: jetbrains-plugin-plugins-api
- description: The Updates API from JetBrains Marketplace — 1 operation(s) for updates.
  name: JetBrains Marketplace Updates API
  slug: jetbrains-plugin-updates-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JetBrains Marketplace Plugins API
  slug: open-jetbrains-plugin-plugins-api
- collection_type: open
  name: JetBrains Marketplace Plugins Updates API
  slug: open-jetbrains-plugin-updates-api
- collection_type: open
  name: JetBrains Marketplace API
  slug: open-jetbrains-plugin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jetbrains-plugin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jetbrains-plugin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetbrains-plugin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jetbrains-plugin-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/jetbrains-marketplace
- group: company
  title: ''
  type: Website
  url: https://plugins.jetbrains.com
- group: docs
  title: ''
  type: Documentation
  url: https://plugins.jetbrains.com/docs/marketplace/about-marketplace.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plugins.jetbrains.com/developers/marketplace
- group: docs
  title: ''
  type: GitHub Documentation
  url: https://github.com/JetBrains/marketplace-docs
- group: start
  title: ''
  type: Signup
  url: https://account.jetbrains.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://plugins.jetbrains.com/legal/marketplace-paid-plugins
created: '2026-05-11'
description: JetBrains Marketplace is the official plugin and theme distribution platform for JetBrains IDEs including IntelliJ IDEA, PyCharm, WebStorm, PhpStorm, GoLand, Rider, and other IntelliJ Platform products. The marketplace hosts thousands of free and paid plugins that extend IDE functionality with new languages, frameworks, tools, themes, and integrations. JetBrains Marketplace provides REST APIs for listing plugins, uploading new plugin builds, and downloading plugin updates programmatically.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jetbrains-plugin.png
layout: provider
modified: '2026-05-11'
name: JetBrains Marketplace
nav: Providers
network: true
overview: 'JetBrains Marketplace publishes 2 APIs on the [APIs.io](https://apis.io/) network: Plugins API and Updates API. Tagged areas include Plugins, IDE, Marketplace, Developer Tools, and JetBrains.


  JetBrains Marketplace''s developer surface includes authentication, documentation, signup flow, pricing, and 7 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 32.4
  delta: -0.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jetbrains-plugin/refs/heads/main/screenshots/jetbrains-plugin-2026-06-20T183726.png
security:
- kind: authentication
  name: Jetbrains Plugin Authentication
  slug: jetbrains-plugin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jetbrains Plugin Domain Security
  slug: jetbrains-plugin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jetbrains Plugin Vulnerability Disclosure
  slug: jetbrains-plugin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jetbrains-plugin
tags:
- Plugins
- IDE
- Marketplace
- Developer Tools
- JetBrains
- IntelliJ
website: https://plugins.jetbrains.com
---
