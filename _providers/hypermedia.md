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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 27
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering hypermedia-driven APIs, HATEOAS, and the formats, link relations, and specifications that make APIs discoverable and self-describing. Hypermedia APIs use links, link relations, and embedded controls inside their responses so that clients can navigate an API graph at runtime rather than relying on hard-coded URI structures. This collection covers hypermedia formats including HAL, JSON:API, Siren, Collection+JSON, JSON-LD, Hydra, ALPS, UBER, Mason, and Verbose; the standards bodies that define web linking (IETF, W3C) including RFC 5988/8288 Web Linking and RFC 9264 api-catalog; provider APIs that demonstrably ship HATEOAS responses such as OpenProject, Reverb, MBTA, Patreon, Teamtailor, and Drupal JSON:API; and the spec libraries and frameworks (Spring HATEOAS, Spring Data REST, Apicurio) that implement hypermedia patterns.
examples:
- key_count: 5
  name: Hypermedia Hal Resource Example
  slug: hypermedia-hal-resource-example
- key_count: 10
  name: Hypermedia Link Relation Example
  slug: hypermedia-link-relation-example
features:
- description: Hypermedia APIs include in-response links and link relations so clients can discover available state transitions at runtime rather than hard-coding URI templates against documentation.
  name: HATEOAS Navigation
- description: Established formats such as HAL, JSON:API, Siren, Collection+JSON, Hydra, ALPS, UBER, Mason, and Verbose provide structured ways to embed links, actions, and metadata inside API responses.
  name: Standardized Hypermedia Formats
- description: RFC 5988 and RFC 8288 define the HTTP Link header and the Web Linking model, including the IANA Link Relations registry that gives shared meaning to rel values across APIs.
  name: Web Linking via Link Headers
- description: JSON-LD, Hydra, schema.org, and the broader RDF stack extend hypermedia with shared vocabularies, enabling semantic interoperability between APIs, search engines, and knowledge graphs.
  name: Linked Data and Semantic Hypermedia
- description: RFC 9264 api-catalog, APIs.json, and similar discovery documents act as hypermedia entry points that link a host to its APIs, OpenAPI specs, terms of service, and policies.
  name: Self-Describing API Catalogs
- description: Frameworks like Spring HATEOAS, Spring Data REST, and Apicurio provide implementation support for emitting HAL, HAL-FORMS, JSON:API, and Collection+JSON responses from server code.
  name: Hypermedia Frameworks and Libraries
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: A minimal hypermedia format for JSON and XML that embeds _links and _embedded resources, widely used by APIs such as OpenProject, Reverb, and Spring Data REST.
  name: HAL (Hypertext Application Language)
- description: A specification for building APIs in JSON that standardizes resource objects, relationships, includes, filtering, sorting, and pagination, used by Patreon, MBTA, Teamtailor, and Drupal.
  name: JSON:API
- description: A hypermedia specification for representing entities, their classes, properties, actions, and links, designed for rich, action-oriented hypermedia clients.
  name: Siren
- description: A JSON-based hypermedia format from Mike Amundsen for representing collections of items with queries and templates for write operations.
  name: Collection+JSON
- description: JSON-LD provides a JSON syntax for Linked Data; Hydra extends it with a vocabulary for describing hypermedia-driven Web APIs including operations, classes, and supported properties.
  name: JSON-LD and Hydra
- description: A profile description format for documenting semantic descriptors and state transitions independent of any single media type.
  name: ALPS (Application-Level Profile Semantics)
- description: IETF specifications defining the HTTP Link header and a model for typed web links, along with the IANA Link Relations registry shared across hypermedia formats.
  name: Web Linking (RFC 5988 / RFC 8288)
- description: A library for building hypermedia-driven REST APIs in Spring, supporting HAL, HAL-FORMS, Collection+JSON, and UBER, with first-class integration into Spring Data REST.
  name: Spring HATEOAS
json_schemas:
- name: HALResource
  property_count: 2
  slug: hypermedia-hal-resource
- name: LinkRelation
  property_count: 11
  slug: hypermedia-link-relation
json_structures:
- name: Hypermedia Hal Resource Structure
  property_count: 2
  slug: hypermedia-hal-resource-structure
- name: Hypermedia Link Relation Structure
  property_count: 11
  slug: hypermedia-link-relation-structure
jsonld:
- class_count: 6
  name: Hypermedia Context
  property_count: 17
  slug: hypermedia-context
layout: provider
modified: '2026-05-19'
name: Hypermedia
nav: Providers
network: true
overview: 'Hypermedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hypermedia, HATEOAS, HAL, JSON:API, and Link Headers.


  The Hypermedia catalog on APIs.io includes 1 JSON-LD context.


  Hypermedia''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: hypermedia
tags:
- Hypermedia
- HATEOAS
- HAL
- JSON:API
- Link Headers
- Link Relations
- Siren
- Collection+JSON
- Linked Data
- JSON-LD
- Hydra
- ALPS
use_cases:
- description: HATEOAS-based APIs allow servers to evolve URI structures, add new affordances, and deprecate endpoints over time while clients continue to navigate by link relations rather than hard-coded paths.
  name: Evolvable Long-Lived APIs
- description: OpenProject exposes work packages, projects, users, and attachments through a HAL+JSON hypermedia API where every resource embeds links to related resources and available actions.
  name: Domain-Driven Project Management APIs
- description: Patreon, MBTA, Teamtailor, and Drupal expose their resources via JSON:API, providing a consistent specification for fetching, including related resources, filtering, sorting, and pagination across very different domains.
  name: Standardized CRUD via JSON:API
- description: Schema.org and JSON-LD allow APIs and websites to publish machine-readable Linked Data that search engines, agents, and aggregators can consume without bespoke parsers.
  name: Semantic Search and Structured Data
- description: APIs.json and RFC 9264 api-catalog documents act as hypermedia entry points that let crawlers, tooling, and AI agents discover an organization's APIs, specifications, and policies from a single well-known URL.
  name: API Discovery and Catalogs
- description: Approaches like htmx, hyperview, and Hypermedia Systems return HTML fragments and hypermedia controls directly to the client, simplifying applications by treating HTML itself as the hypermedia format.
  name: Hypermedia-Driven Web Apps
website: https://apievangelist.com
---
