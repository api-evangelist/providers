---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Science Museum Group Agentic Access
  operation_count: 7
  slug: science-museum-group-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://collection.sciencemuseumgroup.org.uk
  baseurl_source: declared
  description: Documents, archives, and written records in the collection
  name: Science Museum Group Documents API
  slug: science-museum-group-documents-api
- baseURL: https://collection.sciencemuseumgroup.org.uk
  baseurl_source: declared
  description: Scientific instruments, industrial artifacts, and cultural items in the collection
  name: Science Museum Group Objects API
  slug: science-museum-group-objects-api
- baseURL: https://collection.sciencemuseumgroup.org.uk
  baseurl_source: declared
  description: People associated with the museum collections including makers, scientists, and historical figures
  name: Science Museum Group People API
  slug: science-museum-group-people-api
- baseURL: https://collection.sciencemuseumgroup.org.uk
  baseurl_source: declared
  description: Full-text and filtered search across all collection types
  name: Science Museum Group Search API
  slug: science-museum-group-search-api
artifact_total: 21
collections:
- collection_type: open
  name: Science Museum Group Collection API
  slug: open-science-museum-group-collection
- collection_type: open
  name: Science Museum Group Collection Documents API
  slug: open-science-museum-group-documents-api
- collection_type: open
  name: Science Museum Group Collection Documents Objects API
  slug: open-science-museum-group-objects-api
- collection_type: open
  name: Science Museum Group Collection Documents People API
  slug: open-science-museum-group-people-api
- collection_type: open
  name: Science Museum Group Collection Documents Search API
  slug: open-science-museum-group-search-api
common:
- group: commercial
  href: https://artifacts.apis.io/science-museum-group/plans/science-museum-group-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/science-museum-group-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/science-museum-group/rate-limits/science-museum-group-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/science-museum-group-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/science-museum-group/finops/science-museum-group-finops.yml
  title: ''
  type: FinOps
  url: finops/science-museum-group-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.sciencemuseumgroup.org.uk/feed/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TheScienceMuseum/collectionsonline-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/TheScienceMuseum/collectionsonline-api/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/science-museum-group/agentic-access/science-museum-group-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/science-museum-group-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/science-museum-group/security/science-museum-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/science-museum-group-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sciencemuseumgroup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheScienceMuseum
- group: company
  title: ''
  type: Website
  url: https://www.sciencemuseumgroup.org.uk/
- group: start
  title: ''
  type: Collections Portal
  url: https://collection.sciencemuseumgroup.org.uk
created: '2026-05-02'
description: 'The Science Museum Group operates five UK science and technology museums: the Science Museum (London), the Science and Industry Museum (Manchester), the National Railway Museum (York), the National Science and Media Museum (Bradford), and Locomotion (Shildon). The group provides an open Collection API giving developers programmatic access to over 7 million objects, people, and documents in the museum collections via a JSONAPI-compliant REST interface. The API is free to use and supports searching, filtering, and retrieval of collection items with rich metadata, images, and curatorial notes.'
examples:
- key_count: 3
  name: Science Museum Group Get Object Example
  slug: science-museum-group-get-object-example
- key_count: 3
  name: Science Museum Group Search Objects Example
  slug: science-museum-group-search-objects-example
finops:
- has_sources: false
  method: generated
  name: Science Museum Group Finops
  primary_unit: request
  service_category: API
  slug: science-museum-group-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/science-museum-group.png
json_schemas:
- name: Science Museum Group Collection Object
  property_count: 5
  slug: science-museum-group-collection-object
json_structures:
- name: Science Museum Group Collection Object Structure
  property_count: 0
  slug: science-museum-group-collection-object-structure
jsonld:
- class_count: 23
  name: Science Museum Group Context
  property_count: 19
  slug: science-museum-group-context
layout: provider
modified: '2026-10-06'
name: Science Museum Group
nav: Providers
network: true
overview: 'Science Museum Group publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documents API, Objects API, People API, and 1 more. Tagged areas include Museums, Collection, Cultural Heritage, Open Data, and Science.


  The Science Museum Group catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Science Museum Group Plans Pricing
  plan_count: 3
  slug: science-museum-group-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Science Museum Group Rate Limits
  slug: science-museum-group-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Science Museum Group — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: science-museum-group-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Science Museum Group API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: science-museum-group-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 68.4
    catalog_earned_first_party: 0.0
    catalog_gap: 46.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 60.6
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/science-museum-group/science-museum-group-2026-06-20T193534.png
security:
- kind: domain-security
  name: Science Museum Group Domain Security
  slug: science-museum-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: science-museum-group
tags:
- Museums
- Collection
- Cultural Heritage
- Open Data
- Science
- Technology
- United Kingdom
website: https://www.sciencemuseumgroup.org.uk/
---
