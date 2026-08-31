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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
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
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Science Museum Group Agentic Access
  operation_count: 7
  slug: science-museum-group-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Documents, archives, and written records in the collection
  name: Science Museum Group Documents API
  slug: science-museum-group-documents-api
- description: Scientific instruments, industrial artifacts, and cultural items in the collection
  name: Science Museum Group Objects API
  slug: science-museum-group-objects-api
- description: People associated with the museum collections including makers, scientists, and historical figures
  name: Science Museum Group People API
  slug: science-museum-group-people-api
- description: Full-text and filtered search across all collection types
  name: Science Museum Group Search API
  slug: science-museum-group-search-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TheScienceMuseum/collectionsonline-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/TheScienceMuseum/collectionsonline-api/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/science-museum-group-agentic-access.yml
- group: auth
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
- name: Science Museum Group Finops
  service_category: API
  slug: science-museum-group-finops
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
modified: '2026-05-19'
name: Science Museum Group
nav: Providers
network: true
overview: 'Science Museum Group publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Objects API, People API, and 1 more. Tagged areas include Museums, Collection, Cultural Heritage, Open Data, and Science.


  The Science Museum Group catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Science Museum Group Plans Pricing
  plan_count: 3
  slug: science-museum-group-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Science Museum Group Rate Limits
  slug: science-museum-group-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Science Museum Group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: science-museum-group-jsonschema-spectral-rules
- effective_rule_count: 51
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
  composite: 27.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 33.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 66.5
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 0.0
  previous_composite: 27.5
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
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/screenshots/science-museum-group-2026-06-20T193534.png
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
