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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.8
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: The APIs.json specification defines a machine-readable JSON or YAML format for describing API operations. Unlike OpenAPI which describes the technical interface of a single API, APIs.json describes th
  name: APIs.json Specification
  slug: apis-json-specification
artifact_total: 41
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/apis-json/api-json/blob/develop/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/security/apis-json-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apis-json-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apisjson.org
- group: docs
  title: Reserved property types
  type: Documentation
  url: https://apisjson.org/properties/
- group: company
  title: ''
  type: Blog
  url: https://apisjson.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apis-json
- group: build
  title: Specification Repository
  type: GitHubRepository
  url: https://github.com/apis-json/api-json
- group: build
  title: Website
  type: GitHubRepository
  url: https://github.com/apis-json/apis-json-website
- group: build
  title: Artisanal APIs.json Examples
  type: GitHubRepository
  url: https://github.com/apis-json/artisanal
- group: build
  title: Backstage Integration
  type: GitHubRepository
  url: https://github.com/apis-json/backstage
- group: operate
  title: ''
  type: Support
  url: https://github.com/apis-json/api-json/issues
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/rules/apis-json-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/vocabulary/apis-json-vocabulary.yaml
- group: docs
  title: Reserved property type reference
  type: APIReference
  url: https://apisjson.org/properties/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apis-json/api-json/issues
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/changelog/apis-json-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apis-json-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/lifecycle/apis-json-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apis-json-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/conformance/apis-json-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apis-json-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/conventions/apis-json-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apis-json-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/data-model/apis-json-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apis-json-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/packages/apis-json-packages.yml
  title: ''
  type: Packages
  url: packages/apis-json-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/llms/apis-json-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apis-json-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/rate-limits/apis-json-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apis-json-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/plans/apis-json-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apis-json-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/examples/apis-json-complete-example.json
  title: Complete worked example
  type: Examples
  url: examples/apis-json-complete-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/examples/apis-json-minimal-example.json
  title: Minimal worked example
  type: Examples
  url: examples/apis-json-minimal-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/json-structure/apis-json-structure-0.20-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/apis-json-structure-0.20-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/json-ld/apis-json-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apis-json-context.jsonld
created: '2026-03-26'
description: APIs.json is an open, machine-readable specification that API providers can use to describe their API operations, similar to how websites use sitemap.xml. The format provides a lightweight means for individuals and organizations to document the location of their APIs, associated descriptions, human and machine-readable specifications, and ancillary information such as licensing, maintainers, and terms of service. It was created by Kin Lane and Steven Willmott in May 2014 and is maintained as an open IETF-style draft. The current stable version is 0.23, published August 19, 2026, following a rapid 2026 release sequence (0.19 through 0.23) that added the prompts, rules and workflows collections in 0.21 and registered roughly seventy new property types in 0.22 and 0.23 by measured adoption across 26,866 published indexes. APIs.json files can be placed at the root of any domain as /apis.json or /apis.yml for automated discovery. The specification defines root-level fields (name,
  description, url, apis, common), API-level fields (aid, humanURL, baseURL, tags, properties), and a comprehensive list of property types covering documentation, authentication, licensing, support, and governance. It is the foundation for the APIs.io search engine and API Commons initiative.
examples:
- key_count: 16
  name: Apis Json Complete Example
  slug: apis-json-complete-example
- key_count: 13
  name: Apis Json Minimal Example
  slug: apis-json-minimal-example
features:
- description: Provides a machine-readable format for documenting API operations beyond just the technical interface, covering documentation, pricing, authentication, terms of service, support, and governance.
  name: Machine-Readable API Operations
- description: APIs.json files can be placed at /apis.json or /apis.yml at the root of any domain, enabling automated discovery by search engines and robots without prior knowledge of the API provider.
  name: Domain Root Discovery
- description: Defines a comprehensive enumerated set of property types (OpenAPI, Documentation, Authentication, Pricing, Support, etc.) enabling consistent machine-readable indexing of API operations.
  name: Property Type System
- description: Supports federated API directories through include references, allowing a root APIs.json to reference other APIs.json files on different servers or domains.
  name: Federation via Include
- description: A single APIs.json file can document multiple APIs in the apis array, with shared properties in the common section, enabling organization-wide API catalogs.
  name: Multiple API Collections
- description: Defines authoritative (same DNS domain) and non-authoritative entries, with conflict resolution rules giving priority to the most specific authoritative entry.
  name: Authority and Non-Authority
- description: Supports overlay specifications that can modify or extend existing APIs.json entries, enabling provider-agnostic enrichment of API metadata.
  name: Overlay Support
- description: Maintained as a versioned specification from 0.11 through current 0.23, with full version history and diff comparisons available on GitHub and apisjson.org. Every draft ever published is still retained at its original URL, so an index written against an older version keeps a live normative reference.
  name: Version History
finops:
- name: Apis Json Finops
  service_category: API
  slug: apis-json-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apis-json.png
integrations:
- description: The APIs.io search engine is built entirely on the APIs.json specification, indexing submitted APIs.json files to power its API discovery and search capabilities.
  name: APIs.io
- description: API Commons uses APIs.json as its core metadata format for documenting API operations across the open API ecosystem.
  name: API Commons
- description: APIs.json references OpenAPI specifications as a core property type, linking machine-readable API interface descriptions to their operations metadata.
  name: OpenAPI
- description: APIs.json files can be imported into Spotify Backstage using the apis-json/backstage integration tool for enterprise developer portal use.
  name: Backstage
- description: Spectral rulesets can validate APIs.json files against the specification schema and enforce organizational governance rules for API operations.
  name: Spectral
- description: APIs.json supports AsyncAPI as a property type, allowing event-driven and message-based APIs to be documented alongside REST APIs in a single APIs.json file.
  name: AsyncAPI
json_schemas:
- name: A JSON Schema for apis.json, version 0.17
  property_count: 14
  slug: apis-json-schema-0.17
- name: JSON Schema for APIs.json 0.18
  property_count: 16
  slug: apis-json-schema-0.18
- name: JSON Schema for APIs.json 0.19
  property_count: 18
  slug: apis-json-schema-0.19
- name: JSON Schema for APIs.json 0.20
  property_count: 20
  slug: apis-json-schema-0.20
- name: JSON Schema for APIs.json 0.21
  property_count: 24
  slug: apis-json-schema-0.21
- name: JSON Schema for APIs.json 0.21
  property_count: 24
  slug: apis-json-schema-0.22
- name: JSON Schema for APIs.json 0.23
  property_count: 24
  slug: apis-json-schema-0.23
json_structures:
- name: Apis Json Structure 0.17 Structure
  property_count: 14
  slug: apis-json-structure-0.17-structure
- name: Apis Json Structure 0.18 Structure
  property_count: 16
  slug: apis-json-structure-0.18-structure
- name: Apis Json Structure 0.19 Structure
  property_count: 18
  slug: apis-json-structure-0.19-structure
- name: Apis Json Structure 0.20 Structure
  property_count: 20
  slug: apis-json-structure-0.20-structure
jsonld:
- class_count: 9
  name: Apis Json Context
  property_count: 26
  slug: apis-json-context
layout: provider
modified: '2026-09-14'
name: APIs.json
nav: Providers
network: true
overview: 'APIs.json publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Aggregation, API Cataloging, API Commons, API Discovery, and API Governance.


  The APIs.json catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  APIs.json''s developer surface includes documentation, engineering blog, support, API reference, changelog, code examples, and 22 more developer resources.'
plans:
- name: Apis Json Plans Pricing
  plan_count: 0
  slug: apis-json-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Apis Json Rate Limits
  slug: apis-json-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: APIs.json API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: apis-json-jsonschema-spectral-rules
- effective_rule_count: 34
  extends: []
  name: APIs.json API Rules
  rule_count: 34
  severity_counts:
    error: 15
    hint: 0
    info: 7
    warn: 12
  slug: apis-json-spectral-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 47.0
    contract_quality: 34.7
    developer_ergonomics: 23.8
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 30.6
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/screenshots/apis-json-2026-06-20T172256.png
security:
- kind: domain-security
  name: Apis Json Domain Security
  slug: apis-json-domain-security
  summary_line: TLSv1.3
slug: apis-json
tags:
- API Aggregation
- API Cataloging
- API Commons
- API Discovery
- API Governance
- API Operations
- Machine-Readable
- Specification
- Standards
use_cases:
- description: API providers publish APIs.json files at their domain root so that search engines like APIs.io can automatically discover and index all their APIs without manual submission.
  name: API Discovery
- description: Platform teams use APIs.json as a canonical machine-readable index of their API portfolio, enabling automated compliance checking of required operational properties like terms of service and authentication.
  name: API Governance
- description: Developer portals can be automatically generated from APIs.json files by reading the properties array and presenting documentation, OpenAPI specs, getting started guides, and other resources.
  name: API Portal Generation
- description: Organizations publish APIs.json files to participate in the API Commons initiative, making their APIs discoverable and accessible to a wider developer community.
  name: API Commons Participation
- description: Enterprises use APIs.json as the foundation for internal API catalogs, enabling discoverability of internal, partner, and public APIs using a consistent machine-readable format.
  name: Internal API Catalog
- description: Teams use the APIs.json Backstage integration to import API metadata from APIs.json files into Spotify Backstage for internal developer portal use.
  name: Backstage Integration
website: https://apisjson.org
---
