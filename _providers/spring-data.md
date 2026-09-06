---
access_model:
  confidence: low
  label: Enterprise · Open access
  onboarding: open
  pricing: enterprise
  public: false
  source:
  - plans
  - security
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Spring Data Agentic Access
  operation_count: 14
  slug: spring-data-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: Simplifies the development of creating a JPA-based data access layer. Reduces boilerplate code and provides powerful query derivation, named queries, and specification-based querying on top of JPA/Hib
  name: Spring Data JPA
  slug: spring-data-jpa
- description: Provides a Spring-based programming model for MongoDB. Simplifies document operations, offers repository support, geo-spatial queries, GridFS, and full-text search integration with Spring's template p
  name: Spring Data MongoDB
  slug: spring-data-mongodb
- description: Easy configuration and access to Redis from Spring applications. Provides low-level and high-level abstractions for storing, reading, querying data. Supports both reactive and imperative programming m
  name: Spring Data Redis
  slug: spring-data-redis
- description: Provides Spring-based programming model and repository support for Apache Cassandra. Offers CassandraTemplate, repository abstraction, query derivation, and reactive programming support with Project R
  name: Spring Data Cassandra
  slug: spring-data-cassandra
- description: Spring-based programming model for Neo4j graph database. Provides repository support, object-graph mapping, Cypher query derivation, and reactive Neo4j integration with full Spring ecosystem compatibi
  name: Spring Data Neo4j
  slug: spring-data-neo4j
- description: Spring Data module for Elasticsearch search engine. Provides ElasticsearchTemplate, repository abstraction, index management, full-text search queries, and reactive Elasticsearch client support.
  name: Spring Data Elasticsearch
  slug: spring-data-elasticsearch
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Association API from Spring Data — 1 operation(s) for association.
  name: Spring Data Association API
  slug: spring-data-association-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Collection API from Spring Data — 1 operation(s) for collection.
  name: Spring Data Collection API
  slug: spring-data-collection-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Discovery API from Spring Data — 1 operation(s) for discovery.
  name: Spring Data Discovery API
  slug: spring-data-discovery-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Item API from Spring Data — 1 operation(s) for item.
  name: Spring Data Item API
  slug: spring-data-item-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Profile API from Spring Data — 2 operation(s) for profile.
  name: Spring Data Profile API
  slug: spring-data-profile-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Search API from Spring Data — 2 operation(s) for search.
  name: Spring Data Search API
  slug: spring-data-search-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spring Data REST Association API
  slug: open-spring-data-association-api
- collection_type: open
  name: Spring Data REST Association Collection API
  slug: open-spring-data-collection-api
- collection_type: open
  name: Spring Data REST Association Discovery API
  slug: open-spring-data-discovery-api
- collection_type: open
  name: Spring Data REST Association Item API
  slug: open-spring-data-item-api
- collection_type: open
  name: Spring Data REST Association Profile API
  slug: open-spring-data-profile-api
- collection_type: open
  name: Spring Data REST API
  slug: open-spring-data-rest
- collection_type: open
  name: Spring Data REST Association Search API
  slug: open-spring-data-search-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/spring-projects/spring-data-jpa/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/spring-projects/spring-data-jpa/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/spring-projects/spring-data-jpa/blob/main/SECURITY.adoc
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spring-projects/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spring-projects/spring-data-jpa/blob/main/CONTRIBUTING.adoc
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-data-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-data
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-projects
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-data
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/search?q=spring-data
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-projects/spring-data-commons/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/spring-projects/spring-data-commons/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/spring-projects/spring-data-commons/blob/main/CHANGELOG.adoc
created: '2024-01-15'
description: Spring Data's mission is to provide a familiar and consistent, Spring-based programming model for data access while still retaining the special traits of the underlying data store. It makes it easy to use data access technologies, relational and non-relational databases, map-reduce frameworks, and cloud-based data services. This is an umbrella project which contains many subprojects that are specific to a given database.
examples:
- key_count: 4
  name: Spring Data List Resources Example
  slug: spring-data-list-resources-example
finops:
- name: Spring Data Finops
  service_category: Developer Tools
  slug: spring-data-finops
image: https://spring.io/img/projects/spring-data.svg
json_schemas:
- name: Spring Data Paged Resource
  property_count: 3
  slug: spring-data-paged-resource
json_structures:
- name: Spring Data Hal Resource Structure
  property_count: 0
  slug: spring-data-hal-resource-structure
jsonld:
- class_count: 8
  name: Spring Data Context
  property_count: 16
  slug: spring-data-context
layout: provider
modified: '2026-05-19'
name: Spring Data
nav: Providers
network: true
overview: 'Spring Data publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Association API, Collection API, Discovery API, and 3 more. Tagged areas include Data Access, Database, Framework, Java, and JPA.


  The Spring Data catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Data''s developer surface includes engineering blog, Stack Overflow tag, release notes, changelog, and 13 more developer resources.'
plans:
- name: Spring Data Plans Pricing
  plan_count: 1
  slug: spring-data-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Spring Data Rate Limits
  slug: spring-data-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Spring Data API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: spring-data-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Spring Data API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: spring-data-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.5
    catalog_earned_first_party: 0.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 57.3
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 18.4
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-data/refs/heads/main/screenshots/spring-data-2026-06-20T194412.png
security:
- kind: domain-security
  name: Spring Data Domain Security
  slug: spring-data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Data Vulnerability Disclosure
  slug: spring-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-data
tags:
- Data Access
- Database
- Framework
- Java
- JPA
- MongoDB
- ORM
- Redis
- REST
- Spring
website: https://spring.io/projects/spring-data
---
