---
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ofgem-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ofgem-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ofgem.gov.uk/report-vulnerability
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ofgem-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ofgem-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ofgem-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ofgem-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ofgem-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ofgem-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ofgem.gov.uk/
- group: company
  title: ''
  type: About
  url: https://www.ofgem.gov.uk/about-us
- group: start
  title: ''
  type: Portal
  url: https://www.ofgem.gov.uk/news-and-insight/data/data-portal
- group: docs
  title: ''
  type: Documentation
  url: https://www.ofgem.gov.uk/news-and-insight/data
- group: docs
  title: ''
  type: Documentation
  url: https://www.ofgem.gov.uk/data/ofgem-data-upcoming-release-calendar
- group: docs
  title: ''
  type: Documentation
  url: https://www.ofgem.gov.uk/energy-regulation/technology-and-innovation/digitalisation
- group: docs
  title: ''
  type: Documentation
  url: https://www.ofgem.gov.uk/sites/default/files/2021-11/Data_Best_Practice_Guidance_v1.pdf
- group: start
  title: ''
  type: Registry
  url: https://epr.ofgem.gov.uk/
- group: start
  title: ''
  type: Registry
  url: https://rer.ofgem.gov.uk/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.ofgem.gov.uk/report-vulnerability
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.ofgem.gov.uk/.well-known/security.txt
- group: company
  title: ''
  type: News
  url: https://www.ofgem.gov.uk/news-and-insight
- group: company
  title: ''
  type: Blog
  url: https://www.ofgem.gov.uk/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ofgem.gov.uk/rss.xml
- group: other
  title: ''
  type: Publications
  url: https://www.ofgem.gov.uk/publications
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ofgem
- group: operate
  title: ''
  type: Support
  url: https://www.ofgem.gov.uk/about-us/get-in-touch/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ofgem.gov.uk/ofgem-privacy-policy
- group: other
  title: ''
  type: Cookies
  url: https://www.ofgem.gov.uk/cookies
- group: other
  title: ''
  type: Accessibility
  url: https://www.ofgem.gov.uk/website-accessibility
- group: other
  title: ''
  type: Consultations
  url: https://www.ofgem.gov.uk/consultations
- group: other
  title: ''
  type: Guidance
  url: https://www.ofgem.gov.uk/guidance/we-are-launching-our-new-data-exchange-service
created: '2026-07-27'
description: 'Ofgem, the Office of Gas and Electricity Markets, is the non-ministerial government department that regulates the gas and electricity markets of Great Britain (England, Scotland and Wales), drawing its powers from the Gas Act 1986, the Electricity Act 1989 and the Energy Act 2023. It licenses the companies that make, transport and sell energy, sets the price cap, runs the RIIO network price controls, administers environmental and social schemes such as the Renewables Obligation, REGO and Feed-in Tariffs on behalf of government, grants and supervises the Smart Meter Communication Licence held by the Smart DCC, and imposes the Data Best Practice licence obligation that requires network licensees to treat Energy System Data as presumed open. It sits above the value chain rather than in it - it holds no customers, no meters and no wires. Its own API posture is the plain finding: Ofgem publishes NO API of any kind. There is no developer portal, no api., docs., data. or developer.
  subdomain, no OpenAPI, no CKAN endpoint. Market data is genuinely open but delivered as chart images, CSV and XLSX file downloads from the Ofgem Data Portal; consumer data does not exist here at all, because Great Britain mandated the smart-meter INFRASTRUCTURE rather than a consumer data right, and no CDR-equivalent obligation binds either Ofgem or the suppliers it licenses. Ofgem''s two operational registers - the Electronic Public Register and the Renewable Electricity Register - are login-gated applications whose backends are undocumented and unpublished. Ofgem is therefore a regulator that demands open, discoverable, interoperable data from the industry it supervises while shipping none of it programmatically itself.'
image: https://www.ofgem.gov.uk/sites/default/files/styles/uncropped_large/public/2021-06/ofgem-logo.jpg
layout: provider
modified: '2026-07-27'
name: Ofgem
nav: Providers
network: true
overview: 'Ofgem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  Ofgem''s developer surface includes authentication, developer portal, documentation, product news, engineering blog, support, and 25 more developer resources.'
random_paper: 1
scopes:
- name: Ofgem Scopes
  scope_count: 5
  slug: ofgem-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 31.9
    developer_ergonomics: 38.1
    discoverability: 61.1
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 31.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 59.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ofgem/refs/heads/main/screenshots/ofgem-2026-08-07T190026.png
security:
- kind: authentication
  name: Ofgem Authentication
  slug: ofgem-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Ofgem Domain Security
  slug: ofgem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ofgem Vulnerability Disclosure
  slug: ofgem-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ofgem
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Energy Markets
- Regulator
- Smart Metering
- Open Data
- Energy Regulation
- Renewables
- Great Britain
website: https://www.ofgem.gov.uk/
---
