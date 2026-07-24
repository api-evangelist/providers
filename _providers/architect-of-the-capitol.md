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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Architect Of The Capitol Agentic Access
  operation_count: 8
  slug: architect-of-the-capitol-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: The Accessibility API from Architect of the Capitol — 1 operation(s) for accessibility.
  name: Architect of the Capitol Accessibility API
  slug: architect-of-the-capitol-accessibility-api
- description: The Art Collection API from Architect of the Capitol — 2 operation(s) for art collection.
  name: Architect of the Capitol Art Collection API
  slug: architect-of-the-capitol-art-collection-api
- description: The Buildings API from Architect of the Capitol — 2 operation(s) for buildings.
  name: Architect of the Capitol Buildings API
  slug: architect-of-the-capitol-buildings-api
- description: The Preservation API from Architect of the Capitol — 2 operation(s) for preservation.
  name: Architect of the Capitol Preservation API
  slug: architect-of-the-capitol-preservation-api
- description: The Visitor Information API from Architect of the Capitol — 1 operation(s) for visitor information.
  name: Architect of the Capitol Visitor Information API
  slug: architect-of-the-capitol-visitor-information-api
artifact_total: 50
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/architect-of-the-capitol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/architect-of-the-capitol-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/architect-of-the-capitol
- group: start
  title: ''
  type: Portal
  url: https://www.aoc.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aoc.gov/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/rules/aoc-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/vocabulary/aoc-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/json-ld/aoc-data-api-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.aoc.gov/explore-capitol-campus/blog
created: '2024-11-21'
description: The Architect of the Capitol (AOC) serves Congress and the Supreme Court as builder and steward of Capitol Hill's landmark buildings and grounds, preserving historic structures, monuments, art, and gardens across the Capitol campus.
examples:
- key_count: 2
  name: Aoc Data Api Accessibility Info Example
  slug: aoc-data-api-accessibility-info-example
- key_count: 2
  name: Aoc Data Api Artwork Example
  slug: aoc-data-api-artwork-example
- key_count: 2
  name: Aoc Data Api Artwork List Example
  slug: aoc-data-api-artwork-list-example
- key_count: 2
  name: Aoc Data Api Building Example
  slug: aoc-data-api-building-example
- key_count: 2
  name: Aoc Data Api Building List Example
  slug: aoc-data-api-building-list-example
- key_count: 2
  name: Aoc Data Api Coordinates Example
  slug: aoc-data-api-coordinates-example
- key_count: 2
  name: Aoc Data Api Preservation Project Example
  slug: aoc-data-api-preservation-project-example
- key_count: 2
  name: Aoc Data Api Preservation Project List Example
  slug: aoc-data-api-preservation-project-list-example
- key_count: 2
  name: Aoc Data Api Visitor Info Example
  slug: aoc-data-api-visitor-info-example
features:
- description: Information about the US Capitol, House and Senate office buildings, Library of Congress, and Supreme Court.
  name: Capitol Campus Buildings
- description: Access to the Capitol art collection catalog including paintings, sculptures, and historic artifacts.
  name: Art Collections
- description: Data on preservation and restoration projects across the Capitol campus.
  name: Historic Preservation Projects
- description: Accessibility features and visitor accommodations across Capitol campus facilities.
  name: Accessibility Information
- description: Management of congressional office space, hearing rooms, and support facilities.
  name: Congressional Facilities
finops:
- name: Architect Of The Capitol Finops
  service_category: API
  slug: architect-of-the-capitol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/architect-of-the-capitol.png
json_schemas:
- name: AccessibilityInfo
  property_count: 10
  slug: aoc-data-api-accessibility-info
- name: ArtworkList
  property_count: 4
  slug: aoc-data-api-artwork-list
- name: Artwork
  property_count: 12
  slug: aoc-data-api-artwork
- name: BuildingList
  property_count: 4
  slug: aoc-data-api-building-list
- name: Building
  property_count: 12
  slug: aoc-data-api-building
- name: Coordinates
  property_count: 2
  slug: aoc-data-api-coordinates
- name: PreservationProjectList
  property_count: 4
  slug: aoc-data-api-preservation-project-list
- name: PreservationProject
  property_count: 12
  slug: aoc-data-api-preservation-project
- name: VisitorInfo
  property_count: 3
  slug: aoc-data-api-visitor-info
json_structures:
- name: Aoc Data Api Accessibility Info Structure
  property_count: 10
  slug: aoc-data-api-accessibility-info-structure
- name: Aoc Data Api Artwork List Structure
  property_count: 4
  slug: aoc-data-api-artwork-list-structure
- name: Aoc Data Api Artwork Structure
  property_count: 12
  slug: aoc-data-api-artwork-structure
- name: Aoc Data Api Building List Structure
  property_count: 4
  slug: aoc-data-api-building-list-structure
- name: Aoc Data Api Building Structure
  property_count: 12
  slug: aoc-data-api-building-structure
- name: Aoc Data Api Coordinates Structure
  property_count: 2
  slug: aoc-data-api-coordinates-structure
- name: Aoc Data Api Preservation Project List Structure
  property_count: 4
  slug: aoc-data-api-preservation-project-list-structure
- name: Aoc Data Api Preservation Project Structure
  property_count: 12
  slug: aoc-data-api-preservation-project-structure
- name: Aoc Data Api Visitor Info Structure
  property_count: 3
  slug: aoc-data-api-visitor-info-structure
jsonld:
- class_count: 9
  name: Aoc Data Api Context
  property_count: 0
  slug: aoc-data-api-context
layout: provider
modified: '2026-04-19'
name: Architect of the Capitol
nav: Providers
network: true
overview: 'Architect of the Capitol publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accessibility API, Art Collection API, Buildings API, and 2 more. Tagged areas include Federal Government, Capitol Hill, Congress, Historic Preservation, and Government Services.


  The Architect of the Capitol catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Architect of the Capitol''s developer surface includes developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Architect Of The Capitol Plans Pricing
  plan_count: 3
  slug: architect-of-the-capitol-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Architect Of The Capitol Rate Limits
  slug: architect-of-the-capitol-rate-limits
rules:
- name: Architect of the Capitol API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 5
  slug: aoc-spectral-rules
- name: Architect of the Capitol API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: architect-of-the-capitol-jsonschema-spectral-rules
- name: Architect of the Capitol API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: architect-of-the-capitol-spectral-rules
score:
  band: thin
  composite: 42.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.9
    developer_ergonomics: 19.6
    discoverability: 87.5
    governance: 39.5
    operational_transparency: 31.6
  previous_composite: 42.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/screenshots/architect-of-the-capitol-2026-06-20T172408.png
security:
- kind: domain-security
  name: Architect Of The Capitol Domain Security
  slug: architect-of-the-capitol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: architect-of-the-capitol
tags:
- Federal Government
- Capitol Hill
- Congress
- Historic Preservation
- Government Services
use_cases:
- description: Provide Capitol campus visitor information including building access, tours, and facilities.
  name: Visitor Information
- description: Research the Capitol art collection for educational and historical purposes.
  name: Art Research
- description: Track preservation project status and outcomes for historic Capitol structures.
  name: Historic Preservation
- description: Support congressional staff with facilities management and space planning information.
  name: Congressional Services
website: https://www.aoc.gov/
---
