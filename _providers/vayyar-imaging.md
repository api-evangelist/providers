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
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Agent-facing commerce surface of the Walabot DIY storefront (walabot.com, a Shopify store operated by Vayyar): unauthenticated read-only product JSON endpoints (/products/{handle}.json, /collections/{'
  name: Walabot Storefront Agent Commerce (UCP)
  slug: walabot-storefront-agent-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vayyar-imaging-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vayyar.com
- group: company
  title: ''
  type: Blog
  url: https://vayyar.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://api.walabot.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.walabot.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vayyar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vayyar.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://walabot.com/pages/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://walabot.com/pages/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vayyar-imaging-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vayyar-imaging-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vayyar-imaging-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vayyar-imaging-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vayyar-imaging-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vayyar-imaging-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/vayyar-imaging-packages.yml
created: '2026-07-17'
description: Vayyar Imaging is an Israeli sensor company whose 4D imaging radar-on-chip technology senses, monitors, and images people and objects without cameras. Its RF sensors power Vayyar Care touchless fall detection for elderly care, automotive in-cabin monitoring, smart buildings, public safety, robotics, and the consumer Walabot DIY in-wall imager. Vayyar's developer surface today centers on the Walabot SDK documentation (api.walabot.com) and the Walabot storefront's agent-commerce endpoints (llms.txt, UCP, and a hosted MCP endpoint on walabot.com).
image: https://vayyar.com/wp-content/uploads/2022/08/vayyar-logo.png
layout: provider
mcp_servers:
- description: 'Vayyar''s Walabot DIY storefront (walabot.com, a Shopify store) operates a live agent-commerce MCP endpoint as part of its Universal Commerce Protocol (UCP) implementation. The UCP merchant profile at '
  name: Vayyar Imaging MCP Server
  slug: vayyar-imaging-mcp-server
modified: '2026-07-21'
name: Vayyar Imaging
nav: Providers
network: true
overview: 'Vayyar Imaging publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, Radar, Imaging, and IoT.


  Vayyar Imaging''s developer surface includes engineering blog, documentation, API reference, support, authentication, and 11 more developer resources.'
random_paper: 17
scopes:
- name: Vayyar Imaging Scopes
  scope_count: 4
  slug: vayyar-imaging-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Vayyar Imaging Authentication
  slug: vayyar-imaging-authentication
  summary_line: oauth2/openIdConnect/none · 1 scheme
- kind: domain-security
  name: Vayyar Imaging Domain Security
  slug: vayyar-imaging-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vayyar-imaging
tags:
- Company
- Sensors
- Radar
- Imaging
- IoT
- Healthcare
- Elderly Care
- Automotive
- Smart Home
website: https://vayyar.com
---
