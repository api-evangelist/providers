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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macrofab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.macrofab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.macrofab.com
- group: operate
  title: ''
  type: Support
  url: https://support.macrofab.com
- group: company
  title: ''
  type: Blog
  url: https://www.macrofab.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://factory.macrofab.com/login
- group: start
  title: ''
  type: Login
  url: https://factory.macrofab.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.macrofab.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.macrofab.com/legal/msa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MacroFab
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/macrofab-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/macrofab-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/macrofab-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/macrofab-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/macrofab-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/macrofab-conformance.yml
created: '2026-07-17'
description: 'MacroFab is a US-based electronics manufacturing services (EMS) company operating a digital manufacturing platform for PCB assembly, from prototype to production. Its platform is powered by FabIQ, a manufacturing AI that automates instant quoting, component sourcing, and supply-chain intelligence: engineers upload design files (Gerbers, ODB++, native EDA formats) and receive itemized quotes with live BOM pricing against distributor inventory, component alternate suggestions, tariff impact analysis, consigned inventory management, and real-time order tracking. Founded in 2013 and headquartered in Houston, TX, MacroFab runs ITAR-registered, ISO 9001:2015 certified, DPAS-rated US manufacturing lines serving industrial, defense, autonomous systems, and test-and-measurement customers. The customer platform (factory.macrofab.com) is authenticated via OpenID Connect / OAuth2; MacroFab does not publish an open API specification.'
image: https://www.macrofab.com/
layout: provider
modified: '2026-07-20'
name: MacroFab
nav: Providers
network: true
overview: 'MacroFab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Electronics Manufacturing, PCB Assembly, and Contract Manufacturing.


  MacroFab''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 11 more developer resources.'
random_paper: 8
scopes:
- name: Macrofab Scopes
  scope_count: 2
  slug: macrofab-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.5
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macrofab/refs/heads/main/screenshots/macrofab-2026-07-25T225819.png
security:
- kind: authentication
  name: Macrofab Authentication
  slug: macrofab-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Macrofab Domain Security
  slug: macrofab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: macrofab
tags:
- Company
- Hardware
- Electronics Manufacturing
- PCB Assembly
- Contract Manufacturing
- Supply Chain
- Manufacturing AI
- ITAR
website: https://www.macrofab.com/
---
