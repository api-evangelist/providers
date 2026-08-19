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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Teranet Connect is described by Teranet as an application programming interface providing secure access to Ontario's POLARIS land registration database and the Writs database, using XML and web servic
  name: Teranet Connect
  slug: teranet-connect
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teranet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teranet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teranet-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teranet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teranet-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.teraview.ca/en/system-status/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/teranet-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/teranet-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teranet-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.teranet.ca/
- group: company
  title: ''
  type: About
  url: https://www.teranet.ca/about-teranet/
- group: operate
  title: ''
  type: Contact
  url: https://www.teranet.ca/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.teranet.ca/insights/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.teranet.ca/press-releases/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teranet.ca/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teranet.ca/privacy/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.teranet.ca/legal-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teranet
- group: operate
  title: ''
  type: Support
  url: https://www.teraview.ca/en/help/
- group: operate
  title: ''
  type: HelpCenter
  url: https://teranetcommercialsolutions.zendesk.com/hc/en-ca
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teraview.ca/en/teraview-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.teraview.ca/en/become-a-teraview-user/
- group: start
  title: ''
  type: Login
  url: https://www.teraviewereg.ca/TvApp/Login.jsp?language=en
- group: start
  title: ''
  type: GettingStarted
  url: https://www.teraview.ca/en/teraview-training-environment/
- group: learn
  title: ''
  type: Training
  url: https://www.teraview.ca/en/teraview-video-guides/
- group: other
  title: ''
  type: SystemRequirements
  url: https://www.teraview.ca/en/system-requirements/
- group: other
  title: ''
  type: Policies
  url: https://www.teraview.ca/en/policies/
- group: other
  title: ''
  type: Accessibility
  url: https://www.teranet.ca/accessibility/
- group: company
  title: ''
  type: Careers
  url: https://www.teranet.ca/careers/
created: '2026-07-26'
description: 'Teranet Inc. is the private operator of Ontario''s Electronic Land Registration System (ELRS) and the POLARIS land records database under a long-running concession with the Government of Ontario, and is the exclusive service provider for Manitoba''s Land Titles System and Personal Property Registry. Founded in 1991, headquartered in Toronto and wholly owned by OMERS, Teranet sits at the base of the Canadian property value chain: it holds the authoritative title, parcel, writ and instrument record and resells it as commercial products — Teraview, OnLand, Teranet eXpress, GeoWarehouse, PurView, Teranet Xchange, DataConnect/ValueProtect AVM, TeraIntelligence — plus the Teranet-National Bank House Price Index. Its API posture is licensed access only. Teranet Connect is genuinely described by Teranet as an API (XML and web services over POLARIS and the Writs database), but it is licensed to legal-software vendors through an account manager, with no public documentation, no published
  base URL, no self-serve signup and no developer portal; Teranet''s own support site states plainly that GeoWarehouse has no open API. No RESO certification was found — Teranet is a land registry, not an MLS — and the public record it stewards is sold back rather than published as open data.'
image: https://www.teranet.ca/wp-content/uploads/2021/12/cropped-teranet_favicon_512_512-192x192.png
layout: provider
modified: '2026-07-26'
name: Teranet
nav: Providers
network: true
overview: 'Teranet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Canada, Land Registry, Title, and Conveyancing.


  Teranet''s developer surface includes authentication, changelog, sandbox, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 27.4
  delta: -4.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 77.8
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 31.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Teranet Authentication
  slug: teranet-authentication
  summary_line: proprietary-account/hardware-otp · 4 schemes
- kind: domain-security
  name: Teranet Domain Security
  slug: teranet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teranet
tags:
- Real Estate
- Canada
- Land Registry
- Title
- Conveyancing
- Property Data
- Valuation
- AVM
- PropTech
- Government
- Geospatial
website: https://www.teranet.ca/
---
