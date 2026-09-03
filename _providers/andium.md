---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Universal Commerce Protocol shopping service on Andium's merchandise storefront, exposed as a Model Context Protocol endpoint over JSON-RPC 2.0. Thirteen tools cover catalog search and lookup, pro
  name: Andium Store UCP / MCP
  slug: store-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.andium.com/
- group: company
  title: ''
  type: Blog
  url: https://www.andium.com/blog
- group: company
  title: ''
  type: Press
  url: https://www.andium.com/press
- group: operate
  title: ''
  type: Support
  url: https://www.andium.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.andium.com/andium-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.andium.com/andium-privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/andium
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/andium
- group: company
  title: ''
  type: Careers
  url: https://ats.rippling.com/andium-careers/jobs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/andium-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/andium-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/andium-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/andium-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/andium-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/andium-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/andium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/andium-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/andium-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/andium-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/andium-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/andium-packages.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/andium_stock/
created: '2026-08-06'
description: Andium is a New York City based industrial IoT company that combines its own hardware and AI software into an end-to-end remote field monitoring platform for the energy sector. Its InSite smart camera and edge software watch remote oil and gas wellsites for methane leaks, flare and pilot-light outages, tank levels, liquid spills, fire and asset movement, and push real-time alerts to operators instead of sending crews to look. The company reports cutting site greenhouse-gas emissions by up to 65%, field operating costs by up to 45% and windshield time by 80%, and raised a $21.7M Series B led by Aramco Ventures. Andium publishes no public developer program, documentation or specification for that monitoring platform; the only callable, machine-readable API surface on any andium.com host is the Universal Commerce Protocol MCP endpoint on its Shopify-backed merchandise storefront at shop.andium.com.
image: https://images.prismic.io/andium/a928cac3-dcf8-4940-b631-975802d4ceb0_meta-image-whole-site.jpg?auto=compress,format
layout: provider
mcp_servers:
- description: ''
  name: Andium Store UCP/MCP
  slug: andium-store-ucpmcp
modified: '2026-08-06'
name: Andium
nav: Providers
network: true
overview: 'Andium publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Oil and Gas, Industrial IoT, and Remote Monitoring.


  Andium''s developer surface includes engineering blog, support, authentication, and 21 more developer resources.'
random_paper: 8
scopes:
- name: Andium Scopes
  scope_count: 4
  slug: andium-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 15
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
  previous_composite: 27.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/andium/refs/heads/main/screenshots/andium-2026-08-07T161400.png
security:
- kind: authentication
  name: Andium Authentication
  slug: andium-authentication
  summary_line: oauth2/openIdConnect/none · 3 schemes
- kind: domain-security
  name: Andium Domain Security
  slug: andium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andium
tags:
- Company
- Energy
- Oil and Gas
- Industrial IoT
- Remote Monitoring
- Methane Detection
- Emissions
- Computer-Vision
- Edge Computing
- Commerce
- MCP
website: https://www.andium.com/
---
