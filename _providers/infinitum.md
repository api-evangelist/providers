---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: An HTTP/JSON API over Infinitum's Motor Selection Tool (MST) and Fan Selection Tool (FST), documented by Infinitum for third-party integration with BMS, design software and internal tools. Infinitum's
  name: Infinitum Selection Tools API
  slug: infinitum-selection-tools-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infinitum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goinfinitum.com/
- group: operate
  title: ''
  type: Support
  url: https://support.goinfinitum.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://goinfinitum.com/resources/infinitum-blog/
- group: start
  title: ''
  type: SignUp
  url: https://mst.goinfinitum.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goinfinitum.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goinfinitum.com/terms/
- group: design
  title: ''
  type: Conformance
  url: conformance/infinitum-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infinitum-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/infinitum-plans-pricing.yml
coverage:
  checked: '2026-08-23'
  detail: Infinitum documents a Motor/Fan Selection Tool JSON API and names three endpoints, but the reference at https://mst.goinfinitum.com/docs/api 307-redirects to a sign-in and the company's own support article states that detailed API documentation requires a signed NDA and a case-by-case commercial agreement, so endpoint URLs, schemas and credentials are issued only to contracted customers.
  evidence:
  - status: 307
    url: https://mst.goinfinitum.com/docs/api
  - status: 200
    url: https://support.goinfinitum.com/hc/en-us/articles/52467614888851-Fan-Selection-Tool-FST-External-Integration-with-Third-Party-Applications
  - status: 404
    url: https://goinfinitum.com/openapi.json
  - status: 404
    url: https://goinfinitum.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-23'
description: 'Infinitum (formerly Infinitum Electric) is an Austin, Texas motor manufacturer, founded in 2016 by Ben Schuler, that builds the Aircore EC+ family of air-core printed-circuit-board (PCB) stator electric motors along with integrated fan and pump systems, Active Front End (AFE) drives, power generation packages and off-road traction motors for data centers, commercial and industrial buildings, water and wastewater treatment, agriculture and mobility. Its software surface is operator tooling rather than a developer platform: the I-con motor control application for commissioning, monitoring and diagnostics, a browser-based Motor Selection Tool (MST) and Fan Selection Tool (FST), an IoT kit for telemetry, and BACnet, Modbus and analog/digital field integration on the motor itself. Infinitum does document an HTTP API for the selection tools - fan selection, motor selection and fan chart endpoints - but the reference is served behind an account sign-in and the company states that
  detailed API documentation and advanced integration require a signed NDA and a commercial agreement, so no public contract is reachable.'
image: https://goinfinitum.com/wp-content/uploads/2022/08/cropped-InfinitumLogo-Color-Horz-RGB-425.png
layout: provider
modified: '2026-08-23'
name: Infinitum
nav: Providers
network: true
overview: 'Infinitum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Motors, Manufacturing, Industrial Automation, and Building Automation.


  Infinitum''s developer surface includes support, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Infinitum Plans Pricing
  plan_count: 0
  slug: infinitum-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Infinitum Domain Security
  slug: infinitum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infinitum
tags:
- Company
- Electric Motors
- Manufacturing
- Industrial Automation
- Building Automation
- Data Centers
- HVAC
- Energy Efficiency
- Internet of Things
- Hardware
website: https://goinfinitum.com/
---
