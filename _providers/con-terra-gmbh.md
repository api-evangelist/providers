---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Geospatial API platform offering services for public administration and enterprises. Documentation is available at the developer portal.
  name: Con Terra API
  slug: con-terra-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/con-terra-gmbh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.conterra.de/trust
- group: auth
  title: ''
  type: Security
  url: https://trust.conterra.de
- group: auth
  href: https://artifacts.apis.io/con-terra-gmbh/well-known/con-terra-gmbh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/con-terra-gmbh-security.txt
- group: agent
  href: https://artifacts.apis.io/con-terra-gmbh/well-known/con-terra-gmbh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/con-terra-gmbh-well-known.yml
- group: other
  href: https://artifacts.apis.io/con-terra-gmbh/hosts/con-terra-gmbh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/con-terra-gmbh-hosts.yml
- group: build
  href: https://artifacts.apis.io/con-terra-gmbh/packages/con-terra-gmbh-packages.yml
  title: ''
  type: SDKs
  url: packages/con-terra-gmbh-packages.yml
- group: build
  href: https://artifacts.apis.io/con-terra-gmbh/packages/con-terra-gmbh-packages.yml
  title: ''
  type: Packages
  url: packages/con-terra-gmbh-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.conterra.de/aktuelles/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.conterra.de/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conterra.de/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conterra
- group: auth
  href: https://artifacts.apis.io/con-terra-gmbh/security/con-terra-gmbh-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/con-terra-gmbh-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/con-terra-gmbh/security/con-terra-gmbh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/con-terra-gmbh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/con-terra-gmbh/security/con-terra-gmbh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/con-terra-gmbh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.conterra.de
coverage:
  checked: '2026-10-26'
  detail: The developer pages return 404 for common spec URLs and no OpenAPI, GraphQL, or AsyncAPI files are publicly available.
  evidence:
  - status: 404
    url: https://www.conterra.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: con terra GmbH is a German GeoIT integrator offering solutions and services around geodata, digital transformation, GeoAI, digital twins, and cloud-based data integration for public administration, infrastructure operators, and enterprises. The company connects geodata, expert information, and leading technologies to deliver tailored solutions, emphasizing innovation and sustainability in the geospatial domain.
layout: provider
modified: '2026-10-26'
name: con terra GmbH
nav: Providers
network: true
overview: 'con terra GmbH is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GeoIT, Data Integration, Digital Transformation, and Cloud.


  con terra GmbH''s developer surface includes documentation and 15 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 55.4
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Con Terra Gmbh Domain Security
  slug: con-terra-gmbh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Con Terra Gmbh Vulnerability Disclosure
  slug: con-terra-gmbh-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Con Terra Gmbh Trust Center
  slug: con-terra-gmbh-trust-center
  summary_line: ISO 27001
slug: con-terra-gmbh
tags:
- Company
- GeoIT
- Data Integration
- Digital Transformation
- Cloud
website: http://www.conterra.de
---
