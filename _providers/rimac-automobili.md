---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.rimac-automobili.com/
- group: company
  title: ''
  type: About
  url: https://www.rimac-automobili.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.rimac-newsroom.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.rimac-automobili.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.rimac-automobili.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rimac-automobili.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rimac-automobili.com/legal-notice/
- group: auth
  title: ''
  type: Compliance
  url: https://www.rimac-automobili.com/legal-and-compliance-documents/
- group: company
  title: ''
  type: Careers
  url: https://www.rimac-group.com/careers/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rimac-automobili-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rimac-automobili-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rimac-automobili-llms.txt
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/rimac-automobili_stock/
coverage:
  checked: '2026-08-26'
  detail: Rimac Automobili builds electric hypercars and keeps its vehicle software entirely in-house — its connected-car backend is a private MQTT telemetry platform serving only Rimac's own owner apps, and the corporate site has no /developers or /api section at all (both return HTTP 404), no /.well-known/ document on any of seven Rimac hosts, and no OpenAPI at any API-host root.
  evidence:
  - status: 404
    url: https://www.rimac-automobili.com/developers
  - status: 404
    url: https://www.rimac-automobili.com/api
  - status: 404
    url: https://www.rimac-automobili.com/openapi.json
  - status: 404
    url: https://www.rimac-technology.com/openapi.json
  - status: 404
    url: https://www.rimac-automobili.com/.well-known/agent-card.json
  - status: 404
    url: https://www.rimac-automobili.com/.well-known/security.txt
  - status: 404
    url: https://www.rimac-automobili.com/llms.txt
  - status: 200
    url: https://www.rimac-automobili.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Rimac Automobili d.o.o. is a Croatian electric hypercar manufacturer and automotive technology company founded by Mate Rimac in 2009 and headquartered at the Rimac Campus in Kerestinec, near Zagreb. It designs and builds the Nevera and Nevera R all-electric hypercars, and develops the vehicle software, infotainment, connectivity and telemetry stack that runs them in-house. Since the 2021 formation of the Bugatti Rimac joint venture with Porsche, the group's component and OEM-supply business was carved out into the sister company Rimac Technology, while Rimac Automobili remains the vehicle brand. Rimac operates a private, customer-only connected-vehicle backend — an MQTT-based telemetry platform feeding first-party iOS and Android owner apps with location, charging, battery and driving-performance data, plus over-the-air update and remote command channels — but it publishes no public developer program, developer portal, API reference, or machine-readable API contract of any kind.
  This profile is maintained in the API Evangelist network for company and portfolio tracking.
image: https://cloudfront.rimac-automobili.com/wp-content/uploads/2023/07/18115344/7-HYPERGARAGE-2880x1920.jpg
layout: provider
modified: '2026-08-26'
name: Rimac Automobili
nav: Providers
network: true
overview: 'Rimac Automobili is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Electric Vehicles, Manufacturing, and Automotive Technology.


  Rimac Automobili''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Rimac Automobili Domain Security
  slug: rimac-automobili-domain-security
  summary_line: TLSv1.2 · DMARC
slug: rimac-automobili
tags:
- Company
- Automotive
- Electric Vehicles
- Manufacturing
- Automotive Technology
- Hypercars
- Connected Vehicles
- Telematics
- Croatia
- Mobility
website: https://www.rimac-automobili.com/
---
