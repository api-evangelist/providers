---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: A live Model Context Protocol endpoint served from the Cardiosense corporate host. It is a WordPress MCP Adapter deployment over the website's content and abilities rather than a product API for the C
  name: Cardiosense MCP Server
  slug: cardiosense-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardiosense-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardiosense.com/
- group: company
  title: ''
  type: About
  url: https://cardiosense.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://cardiosense.com/companynews/
- group: company
  title: ''
  type: BlogRSS
  url: https://cardiosense.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardiosense.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cardiosense
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cardiosense
- group: company
  title: ''
  type: Twitter
  url: https://x.com/cardiosenseinc
- group: other
  title: ''
  type: Publications
  url: https://cardiosense.com/publications/
- group: other
  title: ''
  type: Regulatory
  url: https://cardiosense.com/regulatory/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cardiosense-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cardiosense-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cardiosense-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardiosense-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cardiosense-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cardiosense-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cardiosense-conformance.yml
- group: other
  title: ''
  type: RobotsTxt
  url: agentic-access/cardiosense-robots.txt
created: '2026-08-09'
description: Cardiosense, Inc. is a Chicago-based medical technology company developing AI-powered, noninvasive cardiac hemodynamic monitoring for heart failure care. Its CardioTag device is a wearable chest biosensor that captures seismocardiographic (SCG), electrocardiographic (ECG) and photoplethysmographic (PPG) signals, and its PCWP Analysis Software is a standalone AI software-as-a-medical-device that estimates Pulmonary Capillary Wedge Pressure from those signals without right heart catheterization or an implantable sensor. Both are authorized by the FDA as Class II medical devices, and the company received an FDA De Novo classification. Cardiosense publishes no developer program, SDK or API specification; its only machine-readable surfaces are an authored llms.txt, an extended AI-context document, an explicit AI-crawler allowance in robots.txt, and an OAuth-protected Model Context Protocol server on its own host.
image: https://cardiosense.com/wp-content/themes/hello-elementor-child/assets/images/social_1200.png
layout: provider
mcp_servers:
- description: ''
  name: cardiosense-mcp.yml
  slug: cardiosense-mcpyml
modified: '2026-08-09'
name: Cardiosense
nav: Providers
network: true
overview: 'Cardiosense publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Medical Devices, and Cardiology.


  Cardiosense''s developer surface includes engineering blog, authentication, and 17 more developer resources.'
random_paper: 125
scopes:
- name: Cardiosense Scopes
  scope_count: 0
  slug: cardiosense-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.2
  delta: -3.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.2
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Cardiosense Authentication
  slug: cardiosense-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cardiosense Domain Security
  slug: cardiosense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardiosense
tags:
- Company
- Health
- Digital Health
- Medical Devices
- Cardiology
- Heart Failure
- Remote Patient Monitoring
- Wearables
- Artificial Intelligence
- Machine Learning
- Model Context Protocol
website: https://cardiosense.com/
---
