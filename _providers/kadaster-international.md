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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/kadaster-international/well-known/kadaster-international-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kadaster-international-www-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.ncsc.nl/dienstverlening/kwetsbaarheid-melden-cvd
- group: design
  href: https://artifacts.apis.io/kadaster-international/conformance/kadaster-international-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kadaster-international-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kadaster-international/well-known/kadaster-international-formulieren-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kadaster-international-formulieren-security.txt
- group: agent
  href: https://artifacts.apis.io/kadaster-international/well-known/kadaster-international-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kadaster-international-well-known.yml
- group: other
  href: https://artifacts.apis.io/kadaster-international/hosts/kadaster-international-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kadaster-international-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kadaster.nl/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kadaster.nl/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kadaster
- group: auth
  href: https://artifacts.apis.io/kadaster-international/security/kadaster-international-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kadaster-international-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kadaster-international/security/kadaster-international-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kadaster-international-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kadaster.nl
created: '2026-10-23'
description: Kadaster International (Kadaster) is the Dutch national land registry and mapping agency. It provides authoritative information on property ownership, land use, cadastral data, and geographic information for the Netherlands. The organization offers public datasets, APIs, and services for developers, businesses, and citizens to access real‑estate, geospatial, and statistical data for planning, analysis, and compliance purposes.
layout: provider
modified: '2026-10-23'
name: Kadaster International
nav: Providers
network: true
overview: 'Kadaster International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Land Registry, Geospatial, Real Estate, Government, and Netherlands.


  Kadaster International''s developer surface includes documentation and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kadaster International Domain Security
  slug: kadaster-international-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kadaster International Vulnerability Disclosure
  slug: kadaster-international-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kadaster-international
tags:
- Land Registry
- Geospatial
- Real Estate
- Government
- Netherlands
website: https://www.kadaster.nl
---
