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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/eox-it-services-gmbh/hosts/eox-it-services-gmbh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eox-it-services-gmbh-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eox.at/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eox.at/privacy-notice/
- group: other
  title: ''
  type: Leadership
  url: https://www.eox.at/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eox-a
- group: auth
  href: https://artifacts.apis.io/eox-it-services-gmbh/security/eox-it-services-gmbh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eox-it-services-gmbh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.eox.at
coverage:
  checked: '2026-10-26'
  detail: No public API documentation or machine-readable contracts were found for EOX IT Services GmbH.
  evidence:
  - status: 0
    url: https://api.eox.at/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: EOX IT Services GmbH provides IT consulting, cloud solutions, and digital transformation services based in Austria. The company focuses on delivering tailored technology strategies, managed services, and support for enterprises seeking to modernize their infrastructure. Through a portfolio that includes system integration, cybersecurity, and data analytics, EOX helps clients optimize operations and accelerate innovation.
image: https://eox.at/eox-twitter.jpg
layout: provider
modified: '2026-10-26'
name: EOX IT Services GmbH
nav: Providers
network: true
overview: EOX IT Services GmbH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IT Services, Cloud Solutions, Digital Transformation, and Consulting.
random_paper: 2
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eox It Services Gmbh Domain Security
  slug: eox-it-services-gmbh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eox-it-services-gmbh
tags:
- Company
- IT Services
- Cloud Solutions
- Digital Transformation
- Consulting
website: http://www.eox.at
---
