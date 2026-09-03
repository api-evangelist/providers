---
access_model:
  confidence: high
  label: Free and open — no registration, no key, no scopes
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Newcastle Agentic Access
  operation_count: 6
  slug: newcastle-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- baseURL: https://api-dor.ncl.ac.uk
  baseurl_source: declared
  description: A single point-of-truth interface for searching, browsing and displaying the digitised objects held in Newcastle University Library's Special Collections. Eighteen operations across collections, digit
  name: Digitised Objects Repository Search and Data API
  slug: digitised-objects
- description: A GraphQL API over the Eighteenth-Century Political Participation and Electoral Culture research dataset — historical British elections, constituencies, candidates, poll books, voters, votes, occupati
  name: ECPPEC Electoral Data GraphQL API
  slug: ecppec
- description: An OAI-PMH 2.0 metadata harvesting interface over Newcastle University's electronic theses repository, running on DSpace 6.3. Supports oai_dc, dim and the uketd_dc profile used by the UK Electronic Th
  name: Newcastle University eTheses OAI-PMH Endpoint
  slug: etheses-oai
- description: 'Newcastle University''s institutional research data repository, operated for the university by Figshare on a Newcastle-branded custom domain. Programmatic access exists but runs entirely on Figshare''s '
  name: data.ncl Research Data Repository (Figshare tenancy)
  slug: data-ncl
- baseURL: https://api.usb.urbanobservatory.ac.uk/api/v2.0a
  baseurl_source: declared
  description: 'An entity ordinarily describes a spatial location, such as a room in a building or a pole in the street. In some circumstances an entity may be a mobile piece of equipment, in which case the location '
  name: Urban Observatory API (Urban Sciences Building) — Entity
  slug: urban-observatory-entity
- baseURL: https://api.usb.urbanobservatory.ac.uk/api/v2.0a
  baseurl_source: declared
  description: A feed is a representation of a measurement or parametrisation, usually a metric, for example the observed temperature.
  name: Urban Observatory API (Urban Sciences Building) — Feed
  slug: urban-observatory-feed
- baseURL: https://api.usb.urbanobservatory.ac.uk/api/v2.0a
  baseurl_source: declared
  description: A compact summary view over Urban Sciences Building entities and the feeds attached to them.
  name: Urban Observatory API (Urban Sciences Building) — Summary
  slug: urban-observatory-summary
- baseURL: https://api.usb.urbanobservatory.ac.uk/api/v2.0a
  baseurl_source: declared
  description: There may be more than one timeseries associated with a feed. Ordinarily there will be a plain timeseries representing raw data from the device; in some cases there may be additional timeseries repres
  name: Urban Observatory API (Urban Sciences Building) — Timeseries
  slug: urban-observatory-timeseries
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Urban Observatory API: Urban Sciences Building Entity API'
  slug: open-newcastle-entity-api
- collection_type: open
  name: 'Urban Observatory API: Urban Sciences Building Entity Feed API'
  slug: open-newcastle-feed-api
- collection_type: open
  name: 'Urban Observatory API: Urban Sciences Building Entity Summary API'
  slug: open-newcastle-summary-api
- collection_type: open
  name: 'Urban Observatory API: Urban Sciences Building Entity Timeseries API'
  slug: open-newcastle-timeseries-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.ncl.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newcastleuniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/newcastle-university
- group: company
  title: ''
  type: Twitter
  url: https://x.com/UniofNewcastle
- group: other
  title: ''
  type: IdentityFederation
  url: https://gateway.ncl.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.ncl.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://theses.ncl.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.ncl.ac.uk/undergraduate/degrees/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.ncl.ac.uk/library/special-collections/
- group: design
  title: ''
  type: x-conformance
  url: conformance/newcastle-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newcastle-authentication.yml
- group: auth
  title: ''
  type: x-scopes
  url: scopes/newcastle-scopes.yml
- group: design
  title: ''
  type: x-errors
  url: errors/newcastle-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/newcastle-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/newcastle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newcastle-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/newcastle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newcastle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/newcastle-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Newcastle University is a public research university in Newcastle upon Tyne, United Kingdom, and a member of the Russell Group. Its programmable footprint is genuinely its own but it is small, decentralised and unadvertised: there is no central developer portal, no API changelog, no status page and no developer support channel anywhere on ncl.ac.uk. What the institution actually operates and runs itself, verified live on 2026-08-30, is four things — the Urban Observatory API for the Urban Sciences Building (the largest open urban-sensing platform in the UK, on a domain Newcastle registered and serves from its own nameservers), the Library''s Digitised Objects Repository Search and Data API, which publishes its own OpenAPI at /info/open-api and serves 15,482 digitised objects from Special Collections, the ECPPEC eighteenth-century electoral GraphQL API with open introspection, and an OAI-PMH 2.0 endpoint over the eTheses repository. Alongside these it operates a Shibboleth SAML
  2.0 identity provider registered in the UK Access Management Federation with 168 service providers under ncl.ac.uk, which is by volume the institution''s largest machine-readable surface and is a login federation rather than a data API. Its research data repository, data.ncl, is a Figshare tenant: the data and the DOIs are Newcastle''s, the API contract is Figshare''s, and it is recorded here as a tenant relationship rather than credited to the university.'
examples:
- key_count: 4
  name: Newcastle Digitised Objects Collections Example
  slug: newcastle-digitised-objects-collections-example
- key_count: 4
  name: Newcastle Digitised Objects List Example
  slug: newcastle-digitised-objects-list-example
- key_count: 2
  name: Newcastle Ecppec Graphql Example
  slug: newcastle-ecppec-graphql-example
- key_count: 3
  name: Newcastle Entity List Example
  slug: newcastle-entity-list-example
- key_count: 4
  name: Newcastle Timeseries Entry Example
  slug: newcastle-timeseries-entry-example
finops:
- name: Newcastle Finops
  service_category: Education
  slug: newcastle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newcastle.png
json_schemas:
- name: DigitisedObject
  property_count: 5
  slug: newcastle-digitised-object
- name: Collection
  property_count: 3
  slug: newcastle-dor-collection
- name: DorError
  property_count: 1
  slug: newcastle-dor-error
- name: DorPagination
  property_count: 5
  slug: newcastle-dor-pagination
- name: Entity
  property_count: 5
  slug: newcastle-entity
- name: EntitySummary
  property_count: 3
  slug: newcastle-entitysummary
- name: Feed
  property_count: 8
  slug: newcastle-feed
- name: HateoasLinks
  property_count: 0
  slug: newcastle-hateoas-links
- name: Timeseries
  property_count: 8
  slug: newcastle-timeseries
- name: TimeseriesEntry
  property_count: 6
  slug: newcastle-timeseriesentry
json_structures:
- name: Newcastle Entity Structure
  property_count: 5
  slug: newcastle-entity-structure
- name: Newcastle Feed Structure
  property_count: 8
  slug: newcastle-feed-structure
- name: Newcastle Timeseries Structure
  property_count: 8
  slug: newcastle-timeseries-structure
- name: Newcastle Timeseriesentry Structure
  property_count: 6
  slug: newcastle-timeseriesentry-structure
jsonld:
- class_count: 3
  name: Newcastle Context
  property_count: 8
  slug: newcastle-context
layout: provider
modified: '2026-08-30'
name: Newcastle University
nav: Providers
network: true
overview: 'Newcastle University publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Digitised Objects Repository Search and Data API, Urban Observatory API (Urban Sciences Building) — Entity, Urban Observatory API (Urban Sciences Building) — Feed, and 2 more. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  The Newcastle University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Newcastle University''s developer surface includes authentication and 19 more developer resources.'
plans:
- name: Newcastle Plans Pricing
  plan_count: 2
  slug: newcastle-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Newcastle Rate Limits
  slug: newcastle-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Newcastle University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: newcastle-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Newcastle University API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: newcastle-rules
scopes:
- name: Newcastle Scopes
  scope_count: 0
  slug: newcastle-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 30.7
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newcastle/refs/heads/main/screenshots/newcastle-2026-06-20T190237.png
security:
- kind: authentication
  name: Newcastle Authentication
  slug: newcastle-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Newcastle Domain Security
  slug: newcastle-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: newcastle
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Research Data
- Open Data
- Digital Library
- Identity Federation
- Smart Cities
- Cultural Heritage
website: https://www.ncl.ac.uk/
---
