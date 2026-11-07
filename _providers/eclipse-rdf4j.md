---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Eclipse Rdf4J Agentic Access
  operation_count: 20
  slug: eclipse-rdf4j-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 1
apis:
- baseURL: http://localhost:8080/rdf4j-server
  baseurl_source: declared
  description: Manage namespace prefix declarations.
  name: Eclipse RDF4J Namespaces API
  slug: eclipse-rdf4j-namespaces-api
- baseURL: http://localhost:8080/rdf4j-server
  baseurl_source: declared
  description: Protocol version of the server.
  name: Eclipse RDF4J Protocol API
  slug: eclipse-rdf4j-protocol-api
- baseURL: http://localhost:8080/rdf4j-server
  baseurl_source: declared
  description: Manage and inspect RDF repositories.
  name: Eclipse RDF4J Repositories API
  slug: eclipse-rdf4j-repositories-api
- baseURL: http://localhost:8080/rdf4j-server
  baseurl_source: declared
  description: Group multiple operations in an atomic transaction.
  name: Eclipse RDF4J Transactions API
  slug: eclipse-rdf4j-transactions-api
- baseURL: http://localhost:8080/rdf4j-server
  baseurl_source: declared
  description: The [SPARQL 1.1 Graph Store HTTP Protocol](https://www.w3.org/TR/sparql11-http-rdf-update/) is supported on a per-repository basis. The functionality is accessible at the /repositories/<ID>/rdf-graphs
  name: Eclipse RDF4J Graph Store API
  slug: eclipse-rdf4j-graph-store-api
- baseURL: http://localhost:8080/rdf4j-server
  baseurl_source: declared
  description: SPARQL Query and Update execution
  name: Eclipse RDF4J SPARQL API
  slug: eclipse-rdf4j-sparql-api
artifact_total: 20
collections:
- collection_type: open
  name: RDF4J Server REST Contexts API
  slug: open-eclipse-rdf4j-contexts-api
- collection_type: open
  name: RDF4J Server REST Contexts Namespaces API
  slug: open-eclipse-rdf4j-namespaces-api
- collection_type: open
  name: RDF4J Server REST Contexts Protocol API
  slug: open-eclipse-rdf4j-protocol-api
- collection_type: open
  name: RDF4J Server REST Contexts Repositories API
  slug: open-eclipse-rdf4j-repositories-api
- collection_type: open
  name: RDF4J Server REST Contexts Size API
  slug: open-eclipse-rdf4j-size-api
- collection_type: open
  name: RDF4J Server REST Contexts Statements API
  slug: open-eclipse-rdf4j-statements-api
- collection_type: open
  name: RDF4J Server REST Contexts Transactions API
  slug: open-eclipse-rdf4j-transactions-api
- collection_type: open
  name: RDF4J Server REST API
  slug: open-rdf4j-server-rest-api
common:
- group: commercial
  href: https://artifacts.apis.io/eclipse-rdf4j/plans/eclipse-rdf4j-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eclipse-rdf4j-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/eclipse-rdf4j/rate-limits/eclipse-rdf4j-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eclipse-rdf4j-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/eclipse-rdf4j/finops/eclipse-rdf4j-finops.yml
  title: ''
  type: FinOps
  url: finops/eclipse-rdf4j-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.rdf4j.org/
- group: operate
  title: ''
  type: Releases
  url: https://github.com/eclipse/rdf4j/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/eclipse-rdf4j/rdf4j/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/eclipse-rdf4j/rdf4j/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/eclipse-rdf4j/rdf4j/blob/main/CONTRIBUTING.md
- group: agent
  href: https://artifacts.apis.io/eclipse-rdf4j/agentic-access/eclipse-rdf4j-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eclipse-rdf4j-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/eclipse-rdf4j/security/eclipse-rdf4j-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eclipse-rdf4j-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://rdf4j.org/documentation/programming/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://rdf4j.org/documentation/
- group: learn
  title: ''
  type: Tutorials
  url: https://rdf4j.org/documentation/tutorials/
- group: operate
  title: ''
  type: ChangeLog
  url: https://rdf4j.org/release-notes/
- group: operate
  title: ''
  type: Issues
  url: https://github.com/eclipse/rdf4j/issues
- group: operate
  title: ''
  type: Support
  url: https://github.com/eclipse/rdf4j/discussions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eclipse/rdf4j
- group: commercial
  title: ''
  type: License
  url: https://github.com/eclipse/rdf4j/blob/main/LICENSE.md
- group: company
  title: ''
  type: Blog
  url: https://rdf4j.org/index.xml
created: '2024-01-01'
description: Eclipse RDF4J is a powerful open-source Java framework for processing and handling RDF data. It supports creating, parsing, scalable storage, reasoning, and querying with RDF and Linked Data, and ships with an HTTP server (RDF4J Server) and a web-based Workbench. The framework offers an easy-to-use Java API and SPARQL 1.1 support, and integrates with leading RDF database solutions.
finops:
- has_sources: false
  method: generated
  name: Eclipse Rdf4J Finops
  primary_unit: request
  service_category: API
  slug: eclipse-rdf4j-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eclipse-rdf4j.png
layout: provider
modified: '2026-05-19'
name: Eclipse RDF4J
nav: Providers
network: true
overview: 'Eclipse RDF4J publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Namespaces API, Protocol API, Repositories API, and 3 more. Tagged areas include Eclipse Foundation, Java, Linked Data, Open Source, and RDF.


  The Eclipse RDF4J catalog on APIs.io includes 1 Spectral governance ruleset.


  Eclipse RDF4J''s developer surface includes getting-started guide, documentation, changelog, support, engineering blog, and 14 more developer resources.'
plans:
- name: Eclipse Rdf4J Plans Pricing
  plan_count: 3
  slug: eclipse-rdf4j-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Eclipse Rdf4J Rate Limits
  slug: eclipse-rdf4j-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Eclipse RDF4J API Rules
  rule_count: 46
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 7
  slug: eclipse-rdf4j-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 39.1
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 24.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 42.9
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/eclipse-rdf4j/eclipse-rdf4j-2026-06-20T180427.png
security:
- kind: domain-security
  name: Eclipse Rdf4J Domain Security
  slug: eclipse-rdf4j-domain-security
  summary_line: TLSv1.3
slug: eclipse-rdf4j
tags:
- Eclipse Foundation
- Java
- Linked Data
- Open Source
- RDF
- Semantic Web
- SPARQL
- Triple Store
website: https://www.rdf4j.org/
---
