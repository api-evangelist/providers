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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Eclipse Rdf4J Agentic Access
  operation_count: 20
  slug: eclipse-rdf4j-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 1
apis:
- description: Inspect named graphs (contexts) in a repository.
  name: Eclipse RDF4J Contexts API
  slug: eclipse-rdf4j-contexts-api
- description: Manage namespace prefix declarations.
  name: Eclipse RDF4J Namespaces API
  slug: eclipse-rdf4j-namespaces-api
- description: Protocol version of the server.
  name: Eclipse RDF4J Protocol API
  slug: eclipse-rdf4j-protocol-api
- description: Manage and inspect RDF repositories.
  name: Eclipse RDF4J Repositories API
  slug: eclipse-rdf4j-repositories-api
- description: Get the number of statements in a repository.
  name: Eclipse RDF4J Size API
  slug: eclipse-rdf4j-size-api
- description: Read and modify the RDF statements in a repository.
  name: Eclipse RDF4J Statements API
  slug: eclipse-rdf4j-statements-api
- description: Group multiple operations in an atomic transaction.
  name: Eclipse RDF4J Transactions API
  slug: eclipse-rdf4j-transactions-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/eclipse-rdf4j-agentic-access.yml
- group: auth
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
- name: Eclipse Rdf4J Finops
  service_category: API
  slug: eclipse-rdf4j-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eclipse-rdf4j.png
layout: provider
modified: '2026-05-19'
name: Eclipse RDF4J
nav: Providers
network: true
overview: 'Eclipse RDF4J publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Contexts API, Namespaces API, Protocol API, and 4 more. Tagged areas include Eclipse Foundation, Java, Linked Data, Open-Source, and RDF.


  Eclipse RDF4J''s developer surface includes getting-started guide, documentation, changelog, support, engineering blog, and 10 more developer resources.'
plans:
- name: Eclipse Rdf4J Plans Pricing
  plan_count: 3
  slug: eclipse-rdf4j-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Eclipse Rdf4J Rate Limits
  slug: eclipse-rdf4j-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 43.6
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eclipse-rdf4j/refs/heads/main/screenshots/eclipse-rdf4j-2026-06-20T180427.png
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
- Open-Source
- RDF
- Semantic Web
- SPARQL
- Triple Store
---
