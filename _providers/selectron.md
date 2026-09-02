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
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.selectron.ch/en/
- group: operate
  title: ''
  type: Support
  url: https://www.selectron.ch/en/services-and-support/contact-sales-and-support/
- group: start
  title: ''
  type: Login
  url: https://cockpit.selectron.ch/de/Account/Login?ReturnUrl=%2Fen%2FDownload
- group: company
  title: ''
  type: Blog
  url: https://www.selectron.ch/en/media/press-releases/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.selectron.ch/en/footer/general-terms-of-business/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.selectron.ch/en/footer/data-protection/
- group: auth
  title: ''
  type: Compliance
  url: https://www.selectron.ch/en/company/
- group: auth
  title: ''
  type: Security
  url: https://www.selectron.ch/en/services-and-support/cybersecurity-services/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/selectron-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/selectron-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/selectron-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/selectron-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/selectron-plans-pricing.yml
coverage:
  checked: '2026-08-17'
  detail: Selectron builds embedded rail control software that runs on its own on-vehicle hardware and ships its engineering toolchain (Symphony Suite) as licensed Windows desktop applications downloaded from the login-gated Cockpit portal — there is no web API, developer portal or machine-readable contract anywhere on selectron.ch, and api./developer./docs.selectron.ch do not resolve.
  evidence:
  - status: 404
    url: https://www.selectron.ch/openapi.json
  - status: 404
    url: https://www.selectron.ch/apis.json
  - status: 404
    url: https://www.selectron.ch/llms.txt
  - status: 404
    url: https://www.selectron.ch/.well-known/agent-card.json
  - status: 200
    url: https://www.selectron.ch/en/products-and-solutions-2026/software-and-tooling/
  - status: 200
    url: https://cockpit.selectron.ch/de/Account/Login
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Selectron Systems AG is a Swiss rail-vehicle automation and safety supplier founded in 1956 in Lyss, Switzerland, and part of the Knorr-Bremse Group since 2015. Its core business is the Train Control and Management System (TCMS): freely programmable safety controllers and vehicle control units, centralised and decentralised remote I/O (Smartio RIOM), driver-cab displays and HMIs, wheel-slide protection, Ethernet switches, routers, converters and train-bus gateways, plus a rail cybersecurity line (Security Gateway, Threat Detection Solution with Irdeto, PKI and Cyber Resilience Act services). Engineering tooling ships as the Symphony Suite (Maestro Designer, CAP1131, SIM1131, POUtest1131, TOP1131, WDLD1131, SAND) distributed through the login-gated Cockpit portal. Products are certified to ISO/TS 22163 (IRIS), EN 61508 SIL 3, EN 50129 SIL 2, EN 50128 SIL 2 and IEC 62443 SL 2. Selectron publishes no public web API, developer portal or machine-readable contract.'
image: https://www.selectron.ch/media/0000-selectron/0000-selectron-logos/navigationheader-selectronlogo.png
layout: provider
modified: '2026-08-17'
name: Selectron
nav: Providers
network: true
overview: 'Selectron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Rail, Railway, Transportation, and Industrial Automation.


  Selectron''s developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: Selectron Plans Pricing
  plan_count: 0
  slug: selectron-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 17.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Selectron Domain Security
  slug: selectron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Selectron Vulnerability Disclosure
  slug: selectron-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: selectron
tags:
- Company
- Rail
- Railway
- Transportation
- Industrial Automation
- Embedded Systems
- Train Control
- TCMS
- Cybersecurity
- Operational Technology
- Switzerland
website: https://www.selectron.ch/en/
---
