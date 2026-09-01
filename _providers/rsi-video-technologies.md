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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rsi-video-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://videofied.com/
coverage:
  checked: '2026-08-17'
  detail: videofied.com is no longer a company site - it is a bare Azure App Service redirector (serving the Azure wildcard *.azurewebsites.net certificate, which does not even match the hostname) that 301s the brand's old marketing paths into resideo.com and honeywellhome.com and 404s everything else, while www.videofied.com and rsivideotech.com return NXDOMAIN and rsivideo.com is a parked lander; Honeywell bought RSI Video Technologies in March 2016 and the Videofied line now belongs to Resideo, so there is no RSI-operated developer surface left to read.
  evidence:
  - status: 200
    url: https://videofied.com/
  - status: 404
    url: https://videofied.com/.well-known/security.txt
  - status: 404
    url: https://videofied.com/openapi.json
  - status: 200
    url: https://videofied.com/us/frontel-receiver-software/
  - status: 200
    url: https://rsivideo.com/
  reason: defunct
  state: none
created: '2026-08-17'
description: 'RSI Video Technologies was a St. Paul, Minnesota maker of wireless, battery-powered intrusion detection devices with built-in cameras, sold worldwide under the Videofied brand, together with the Frontel receiver software that delivered alarm events and short video clips to professional central monitoring stations. Honeywell acquired the company for approximately USD 123 million in March 2016, and the Videofied product line moved to Resideo Technologies when Honeywell spun out its Homes business in 2018. RSI Video Technologies no longer operates as an independent company: its own domains either do not resolve or redirect into Resideo and Honeywell Home marketing pages, and it publishes no developer program, documentation or machine-readable API contract of its own. Any current developer surface for Videofied hardware belongs to Resideo and is profiled separately in the API Evangelist network as resideo-technologies.'
layout: provider
modified: '2026-08-17'
name: RSI Video Technologies
nav: Providers
network: true
overview: RSI Video Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Intrusion Detection, Video Verification, and Alarm Monitoring.
random_paper: 17
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Rsi Video Technologies Domain Security
  slug: rsi-video-technologies-domain-security
  summary_line: DMARC
slug: rsi-video-technologies
tags:
- Company
- Security
- Intrusion Detection
- Video Verification
- Alarm Monitoring
- Central Station Monitoring
- Hardware
- Acquired
website: https://videofied.com/
---
