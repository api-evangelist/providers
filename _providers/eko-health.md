---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 19.9
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: A live, anonymously reachable Model Context Protocol server published on Eko Health's own www.ekohealth.com host, implementing the Shopify storefront / Universal Commerce Protocol (UCP) shopping servi
  name: Eko Health Storefront MCP
  slug: eko-storefront-mcp
- description: Eko Connect is Eko Health's integration surface for telehealth vendors, telemedicine cart makers, and life-science partners. It ships as native Android and iOS SDKs plus a REST API hosted at api.ekode
  name: Eko Connect Enterprise SDK and API
  slug: eko-connect
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eko-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ekohealth.com/
- group: operate
  title: ''
  type: Support
  url: https://support.ekohealth.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.ekohealth.com/blogs/eko-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EkoDevices
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ekohealth.com/pages/software
- group: start
  title: ''
  type: SignUp
  url: https://account.ekohealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.ekohealth.com/hc/en-us/articles/13156765697563-Terms-of-Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.ekohealth.com/hc/en-us/articles/13156748616731-Privacy-Policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ekohealth.com/
- group: auth
  title: ''
  type: Security
  url: https://support.ekohealth.com/hc/en-us/articles/13156748752155-Security-and-HIPAA
- group: auth
  title: ''
  type: Compliance
  url: https://support.ekohealth.com/hc/en-us/articles/13156748752155-Security-and-HIPAA
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eko-health-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eko-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eko-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eko-health-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/eko-health-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/eko-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eko-health-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eko-health-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/eko-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eko-health-plans.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eko-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eko-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Eko Health Inc. is an Oakland, California digital health company that builds FDA-cleared digital stethoscopes (CORE 500, CORE Digital Attachment, DUO, and the 3M Littmann CORE) together with cloud software and AI algorithms for the detection of cardiovascular and pulmonary disease. Its platform pairs the hardware with the Eko App (iOS/Android), the Eko web Dashboard, Eko AI murmur/AFib/low-ejection-fraction detection, and SENSORA, an enterprise AI cardiac disease detection platform for health systems. For integrators Eko publishes Eko Connect — an Enterprise SDK and API surface that live-streams auscultation audio and single-lead ECG into third-party telehealth, telemedicine cart, and life-science applications. The Enterprise SDK and its backing REST API at api.ekodevices.com are commercially gated: there is no public developer portal, OpenAPI, or self-serve documentation, and access is arranged through Eko sales. The company''s public agent-facing surface is its Shopify storefront,
  which serves a live anonymous MCP server, an agents.md / llms.txt, and Universal Commerce Protocol discovery.'
image: https://www.ekohealth.com/cdn/shop/files/eko-logo_1.svg?v=1743130101&width=500
layout: provider
mcp_servers:
- description: ''
  name: eko-health-mcp.yml
  slug: eko-health-mcpyml
modified: '2026-08-04'
name: Eko Health
nav: Providers
network: true
overview: 'Eko Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical Devices, and Digital Health.


  Eko Health''s developer surface includes support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Eko Health Plans
  plan_count: 5
  slug: eko-health-plans
random_paper: 100
scopes:
- name: Eko Health Scopes
  scope_count: 4
  slug: eko-health-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 42.8
  delta: 1.7
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eko-health/refs/heads/main/screenshots/eko-health-2026-08-07T164805.png
security:
- kind: authentication
  name: Eko Health Authentication
  slug: eko-health-authentication
  summary_line: oauth2/openIdConnect/undocumented · 3 schemes
- kind: domain-security
  name: Eko Health Domain Security
  slug: eko-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Eko Health Vulnerability Disclosure
  slug: eko-health-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: eko-health
tags:
- Company
- Health
- Healthcare
- Medical Devices
- Digital Health
- Telehealth
- Artificial Intelligence
- Cardiology
- Remote Patient Monitoring
- Commerce
website: https://www.ekohealth.com/
---
