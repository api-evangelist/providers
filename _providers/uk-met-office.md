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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.metoffice.gov.uk/about-us/legal/vulnerability-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/uk-met-office/well-known/uk-met-office-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uk-met-office-security.txt
- group: auth
  href: https://artifacts.apis.io/uk-met-office/well-known/uk-met-office-college-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uk-met-office-college-security.txt
- group: agent
  href: https://artifacts.apis.io/uk-met-office/well-known/uk-met-office-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uk-met-office-well-known.yml
- group: other
  href: https://artifacts.apis.io/uk-met-office/hosts/uk-met-office-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uk-met-office-hosts.yml
- group: other
  href: https://artifacts.apis.io/uk-met-office/vendors/uk-met-office-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uk-met-office-vendors.yml
- group: build
  href: https://artifacts.apis.io/uk-met-office/packages/uk-met-office-packages.yml
  title: ''
  type: SDKs
  url: packages/uk-met-office-packages.yml
- group: build
  href: https://artifacts.apis.io/uk-met-office/packages/uk-met-office-packages.yml
  title: ''
  type: Packages
  url: packages/uk-met-office-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metoffice.gov.uk/about-us/governance/public-weather-service/customer-group/terms-of-reference
- group: operate
  title: ''
  type: Support
  url: https://reference.metoffice.gov.uk/ui/help
- group: start
  title: ''
  type: SignUp
  url: https://www.metoffice.gov.uk/policies/registered-content
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metoffice.gov.uk/policies/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metoffice.gov.uk/policies/pricing-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.metoffice.gov.uk/research/news
- group: docs
  title: ''
  type: Documentation
  url: https://weather.metoffice.gov.uk/guides/rss
- group: company
  title: ''
  type: Blog
  url: https://www.metoffice.gov.uk/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MetOffice
- group: auth
  href: https://artifacts.apis.io/uk-met-office/security/uk-met-office-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/uk-met-office-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/uk-met-office/security/uk-met-office-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uk-met-office-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.metoffice.gov.uk/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.metoffice.gov.uk/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: The UK Met Office is the United Kingdom’s national weather service, providing weather and climate data, forecasts, warnings and scientific research. It offers public weather services, data APIs, and expertise to support businesses, government and the public in understanding and responding to weather and climate change impacts.
image: https://www.metoffice.gov.uk/api/images/file/LoughriggFellLakeDistrictjpg-1280x503.jpg
layout: provider
modified: '2026-10-23'
name: UK Met Office
nav: Providers
network: true
overview: 'UK Met Office is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Data, and Forecast.


  UK Met Office''s developer surface includes support, signup flow, pricing, documentation, engineering blog, and 15 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Uk Met Office Domain Security
  slug: uk-met-office-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uk Met Office Vulnerability Disclosure
  slug: uk-met-office-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: uk-met-office
tags:
- Company
- Weather
- Climate
- Data
- Forecast
website: https://www.metoffice.gov.uk/
---
