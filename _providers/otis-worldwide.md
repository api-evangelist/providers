---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developers.otis.com/signup
  - https://www.otis.com/documents/256045/119472397/OID_Robot-Prodivers_Datasheet_InDesign_WHQ_English_Final.pdf/215d5e99-fd88-5502-aa1a-078c8c3b3eff?t=1655310590825
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: 'Cloud-based or on-premise API for integrating service robots and third-party applications with Otis elevators. Otis''s own service-robot data sheet lists the available operations as: place a hall call,'
  name: Otis Integrated Dispatch (OID) API
  slug: otis-integrated-dispatch-oid-api
- description: API that moves elevator and escalator data into Building Management Systems (BMS), Building Automation Systems (BAS) and SCADA platforms — real-time equipment status, notifications and alerts, waiting
  name: Otis Building Management API
  slug: otis-building-management-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/otis-worldwide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.otis.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/otis_elevators
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.otis.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.otis.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.otis.com/Started
- group: start
  title: ''
  type: SignUp
  url: https://developers.otis.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.otis.com/en/us/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.otis.com/en/us/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.otis.com/en/us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.otis.com/en/us/privacy-policy
- group: operate
  title: ''
  type: Roadmap
  url: https://www.otis.com/documents/256045/119472397/OID_Robot-Prodivers_Datasheet_InDesign_WHQ_English_Final.pdf/215d5e99-fd88-5502-aa1a-078c8c3b3eff?t=1655310590825
- group: auth
  title: ''
  type: Authentication
  url: authentication/otis-worldwide-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/otis-worldwide-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/otis-worldwide-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/otis-worldwide-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/otis-worldwide-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/otis-worldwide-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/otis-worldwide-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/otis-worldwide-llms.txt
coverage:
  checked: '2026-08-28'
  detail: developers.otis.com is an Azure API Management developer portal whose anonymous API catalogue returns count 0 — the reference, and any machine-readable spec behind it, require a portal account plus a subscribed API product, and Otis's own BMS API Appendix limits the licence to sites where Otis holds the elevator maintenance contract.
  evidence:
  - status: 200
    url: https://apim-apip-prod-naa-7yxcbl5fhzara.management.azure-api.net/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/00000000-0000-0000-0000-000000000000/providers/Microsoft.ApiManagement/service/apim-apip-prod-naa-7yxcbl5fhzara/apis?api-version=2021-08-01
  - status: 404
    url: https://developers.otis.com/openapi.json
  - status: 404
    url: https://api.otis.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: 'Otis Worldwide is the world''s leading manufacturer, installer and servicer of elevators, escalators and moving walkways, serving customers in more than 200 countries and territories. Alongside the equipment business Otis runs a connected-building software portfolio — Otis ONE IoT remote monitoring, the Compass destination-entry dispatch platform, eCall and eView — and exposes it to integrators through the Otis Developer Portal at developers.otis.com. Two named API products sit behind that portal: the Otis Integrated Dispatch (OID) API, a secure-websocket, OAuth 2.0 client-credentials interface that lets service robots and third-party applications place hall, car and destination calls and read live car position, direction, load, door status and car mode; and the Building Management API, which streams elevator and escalator availability, traffic and maintenance data into BMS, BAS and SCADA platforms and accepts operational commands. Otis also publishes an eCall Pro API. The
  developer portal is an Azure API Management instance and its API catalogue is visible only to signed-in, subscribed developers, so no public OpenAPI, AsyncAPI or other machine-readable contract is reachable anonymously.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/otis-worldwide.png
layout: provider
modified: '2026-08-28'
name: Otis Worldwide
nav: Providers
network: true
overview: 'Otis Worldwide publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Elevators, Escalators, Building Management, Smart Buildings, and Internet of Things.


  Otis Worldwide''s developer surface includes API reference, getting-started guide, signup flow, support, engineering blog, authentication, sandbox, and 13 more developer resources.'
plans:
- name: Otis Worldwide Plans Pricing
  plan_count: 0
  slug: otis-worldwide-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Otis Worldwide Rate Limits
  slug: otis-worldwide-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.3
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Otis Worldwide Authentication
  slug: otis-worldwide-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Otis Worldwide Domain Security
  slug: otis-worldwide-domain-security
  summary_line: TLSv1.3 · DMARC
slug: otis-worldwide
tags:
- Elevators
- Escalators
- Building Management
- Smart Buildings
- Internet of Things
- Robotics
- Building Automation
- Elevator Dispatch
- Industrial
- Manufacturing
website: https://www.otis.com
---
