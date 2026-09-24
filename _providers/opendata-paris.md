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
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Provides access to Paris open data sets via the API console.
  name: Open Data API
  slug: open-data-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opendata-paris/refs/heads/main/security/opendata-paris-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/opendata-paris-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opendata-paris/refs/heads/main/well-known/opendata-paris-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/opendata-paris-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opendata-paris/refs/heads/main/well-known/opendata-paris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opendata-paris-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opendata-paris/refs/heads/main/security/opendata-paris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opendata-paris-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opendata-paris/refs/heads/main/security/opendata-paris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opendata-paris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.paris.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://opendata.paris.fr/api-console/explore/v2.1/
- group: docs
  title: ''
  type: APIReference
  url: https://opendata.paris.fr/api/explore/v2.1/swagger.json
- group: start
  title: ''
  type: GettingStarted
  url: https://opendata.paris.fr/pages/home/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opendata.paris.fr/terms/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opendata.paris.fr/terms/privacy-policy/
coverage:
  checked: 2026-09-21
  detail: API documentation provides only a Swagger UI without a downloadable OpenAPI spec.
  evidence:
  - status: 404
    url: https://opendata.paris.fr/api/explore/v2.1/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: Paris Open Data provides open public data from the City of Paris, offering datasets across themes such as administration, finance, culture, environment, mobility, and urban planning. The portal enables search, download, and reuse of data for citizens, developers, and researchers, fostering transparency and innovation.
layout: provider
modified: '2026-09-21'
name: Paris Open Data
nav: Providers
network: true
overview: 'Paris Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Data, Government, Transparency, and Paris.


  Paris Open Data''s developer surface includes documentation, API reference, getting-started guide, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.6
    operational_transparency: 10.5
  previous_composite: 19.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Opendata Paris Domain Security
  slug: opendata-paris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opendata Paris Vulnerability Disclosure
  slug: opendata-paris-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opendata-paris
tags:
- Company
- Open Data
- Government
- Transparency
- Paris
website: https://opendata.paris.fr/
---
