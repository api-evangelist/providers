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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aps-com/refs/heads/main/hosts/aps-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aps-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aps-com/refs/heads/main/vendors/aps-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aps-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aps.com/en/Utility/Regulatory-and-Legal/Terms-of-Use
- group: operate
  title: ''
  type: Support
  url: https://www.aps.com/en/Utility/Help
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aps-com/refs/heads/main/security/aps-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aps-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aps.com
- group: start
  title: ''
  type: Login
  url: https://www.aps.com/en/Authorization/Login
- group: company
  title: ''
  type: Newsroom
  url: https://www.aps.com/en/About/Our-Company/Newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aps.com/en/Utility/Regulatory-and-Legal/Privacy-Policy
coverage:
  checked: '2026-10-13'
  detail: APS publishes no developer portal, API documentation or machine-readable contract. api.aps.com and developer.aps.com do not resolve; contract discovery across www, build, careers and marketplace found no OpenAPI, AsyncAPI or GraphQL (marketplace.aps.com/mcp answers 403 to every path, opaque). No Green Button Connect My Data program page exists in the sitemap (/Residential/Account/Green-Button 404s); customer data access is limited to logged-in usage downloads (Billing-and-Payment/Download-Usage) and EDI bill-file downloads (/en/EDI/EDI-Download-Bill-Files) for business accounts.
  evidence:
  - status: unresolved
    url: https://api.aps.com/
  - status: unresolved
    url: https://developer.aps.com/
  - status: 404
    url: https://www.aps.com/Residential/Account/Green-Button
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Arizona Public Service (APS) is Arizona's largest electric utility, a subsidiary of Pinnacle West Capital, serving residential and business customers across the state.
image: https://www.aps.com/-/media/APS/APSCOM-Images/About/Sustainability-and-Innovation/APSEmployeesLookingIntoDistanceSolarPanels033x.jpg?sc_lang=en
layout: provider
modified: '2026-10-13'
name: Arizona Public Service
nav: Providers
network: true
overview: 'Arizona Public Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, and Electricity.


  Arizona Public Service''s developer surface includes support and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 32.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aps Com Domain Security
  slug: aps-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aps-com
tags:
- Company
- Energy
- Utilities
- Electricity
website: https://www.aps.com
---
