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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pseg-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/pseg-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pseg-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.pseg.com/
- group: company
  title: ''
  type: Website
  url: https://www.psegliny.com/
- group: company
  title: ''
  type: About
  url: https://corporate.pseg.com/
- group: company
  title: ''
  type: Blog
  url: https://corporate.pseg.com/newsroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pseg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PSEGLI
- group: start
  title: ''
  type: Login
  url: https://nj.myaccount.pseg.com/user/login
- group: operate
  title: ''
  type: Support
  url: https://nj.myaccount.pseg.com/customersupport
- group: operate
  title: ''
  type: Support
  url: https://www.psegliny.com/en/myaccount/customersupport
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corporate.pseg.com/websitetermsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corporate.pseg.com/websitetermsandconditions
- group: other
  title: ''
  type: Rates
  url: https://nj.pseg.com/aboutpseg/regulatorypage/electrictariffs
- group: docs
  title: ''
  type: Documentation
  url: https://www.psegliny.com/myaccount/serviceandrates/mysmartenergy
- group: docs
  title: ''
  type: Documentation
  url: https://nj.myaccount.pseg.com/myservicepublic/smartmeters
created: '2026-07-27'
description: 'Public Service Enterprise Group (PSEG) is a diversified energy holding company headquartered in Newark, New Jersey. Its regulated utility subsidiary Public Service Electric and Gas (PSE&G) is New Jersey''s largest electric and gas distribution utility, and PSEG Long Island operates the transmission and distribution system on behalf of the Long Island Power Authority. PSEG sits squarely in the utility-retailer tier of the United States energy value chain — it meters, bills, and serves end customers, and it sells generation into the PJM wholesale market rather than publishing that market''s data itself. Its API posture is honestly closed. There is no developer portal: developer., developers., api., docs., and data.pseg.com do not resolve, and /developers, /api, and /docs on pseg.com return the site''s soft-404 page. Green Button is present only as a file: PSEG Long Island''s MySmartEnergy FAQ states customers can "download data information in CSV or Green Button (.XML) format,"
  which is Download My Data behind a customer login, not Connect My Data. There is no documented programmatic third-party access to customer usage data — in the New Jersey BPU AMI docket PSE&G described manual secondary-user sharing, a Letter of Authorization with spreadsheets emailed back, and EDI for BPU-licensed suppliers. Grid data is equally closed: the PSE&G NJ and PSEG Long Island outage maps are vendor-hosted KUBRA StormCenter applications with no published data API. Open market data for this territory comes from PJM and the EIA, not from PSEG.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pseg.png
layout: provider
modified: '2026-07-27'
name: PSEG
nav: Providers
network: true
overview: 'PSEG is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Utilities, Electricity, and Gas.


  PSEG''s developer surface includes engineering blog, support, documentation, and 14 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 6.1
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Pseg Domain Security
  slug: pseg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pseg
tags:
- Energy
- United States
- Utilities
- Electricity
- Gas
- Smart Metering
- Green Button
- Grid
- New Jersey
website: https://www.pseg.com/
---
