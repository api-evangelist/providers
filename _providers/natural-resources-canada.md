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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/security/natural-resources-canada-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/natural-resources-canada-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/well-known/natural-resources-canada-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/natural-resources-canada-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/well-known/natural-resources-canada-ressources-naturelles-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/natural-resources-canada-ressources-naturelles-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/well-known/natural-resources-canada-digital-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/natural-resources-canada-digital-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/well-known/natural-resources-canada-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/natural-resources-canada-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/hosts/natural-resources-canada-hosts.yml
  title: ''
  type: Hosts
  url: hosts/natural-resources-canada-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/vendors/natural-resources-canada-vendors.yml
  title: ''
  type: Vendors
  url: vendors/natural-resources-canada-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://natural-resources.canada.ca/corporate/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canada.ca/en/transparency/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://natural-resources.canada.ca/corporate/plans-performance-reports
- group: company
  title: ''
  type: Newsroom
  url: https://www.canada.ca/en/news/advanced-news-search/news-results.html?typ=newsreleases&dprtmnt=naturalresourcescanada&start=&end=
- group: company
  title: ''
  type: Blog
  url: https://blog.canada.ca/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/security/natural-resources-canada-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/natural-resources-canada-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/natural-resources-canada/refs/heads/main/security/natural-resources-canada-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/natural-resources-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://natural-resources.canada.ca/
coverage:
  checked: '2026-10-13'
  detail: The provider's main site returns HTML but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://natural-resources.canada.ca/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Natural Resources Canada (NRCan) is the federal department responsible for the sustainable development, management and use of Canada’s natural resources, including energy, minerals, forests, and water. It provides data, research, tools, and services to support industry, government, and the public in making informed decisions about resource stewardship, environmental protection, and economic growth. NRCan’s digital platforms offer APIs for accessing geospatial data, energy statistics, forest resources, and more, enabling developers to integrate authoritative Canadian resource information into applications and analyses.
layout: provider
modified: '2026-10-13'
name: Natural Resources Canada
nav: Providers
network: true
overview: 'Natural Resources Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Natural-Resources, Canada, and Environment.


  Natural Resources Canada''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Natural Resources Canada Domain Security
  slug: natural-resources-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Natural Resources Canada Vulnerability Disclosure
  slug: natural-resources-canada-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: natural-resources-canada
tags:
- Company
- Government
- Natural-Resources
- Canada
- Environment
website: https://natural-resources.canada.ca/
---
