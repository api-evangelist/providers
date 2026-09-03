---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 6
apis:
- description: Public SPARQL 1.1 query endpoint backed by OpenLink Virtuoso over the DBpedia knowledge graph derived from Wikipedia. Supports up to 10,000 result rows, 120-second query timeout, and 100 requests/seco
  name: DBpedia SPARQL Endpoint
  slug: sparql
- description: 'REST API for entity retrieval and auto-complete over the DBpedia knowledge graph. Resolves plain-text keywords to DBpedia resource URIs. Supports keyword search (/api/search) and prefix/auto-complete '
  name: DBpedia Lookup Service
  slug: lookup
- description: REST API for automatic annotation and entity linking of natural language text to DBpedia resources. Accepts text via HTTP GET or POST and returns mentions linked to DBpedia URIs. Supports multi-langua
  name: DBpedia Spotlight
  slug: spotlight
- description: 'HTTP Linked Data access to DBpedia resources via content negotiation. Dereference any DBpedia entity URI (http://dbpedia.org/resource/{EntityName}) using an Accept header to retrieve RDF descriptions '
  name: DBpedia Linked Data
  slug: linked-data
- description: Real-time SPARQL endpoint and Linked Data access over continuously updated DBpedia data derived from near-real-time Wikipedia edits. SPARQL endpoint at http://live.dbpedia.org/sparql. Provides 19 type
  name: DBpedia Live
  slug: live
- description: Data cataloging, versioning, and publishing platform for DBpedia and community datasets. Exposes a SPARQL API for querying RDF metadata and a Search API for discovering published datasets. Data metada
  name: DBpedia Databus
  slug: databus
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dbpedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dbpedia.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dbpedia.org/resources/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dbpedia
- group: operate
  title: ''
  type: Forums
  url: https://forum.dbpedia.org/
- group: company
  title: ''
  type: Blog
  url: https://www.dbpedia.org/blog/
- group: commercial
  title: ''
  type: Plans
  url: plans/dbpedia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dbpedia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dbpedia-finops.yml
created: '2026-06-13'
description: DBpedia is a community project that extracts structured data from Wikipedia and publishes it as Linked Open Data on the Web. It provides a SPARQL endpoint, a Lookup Service for entity resolution, a Spotlight API for text annotation, a Live endpoint for real-time Wikipedia data, and Linked Data access via HTTP content negotiation — forming a queryable cross-linked knowledge graph of Wikipedia-derived facts.
finops:
- name: Dbpedia Finops
  service_category: Data and Analytics
  slug: dbpedia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dbpedia.png
layout: provider
modified: '2026-06-13'
name: DBpedia
nav: Providers
network: true
overview: 'DBpedia publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Linked Data, Knowledge Graph, SPARQL, Semantic Web, and Wikipedia.


  DBpedia''s developer surface includes documentation, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: Dbpedia Plans Pricing
  plan_count: 2
  slug: dbpedia-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 7
  name: Dbpedia Rate Limits
  slug: dbpedia-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dbpedia/refs/heads/main/screenshots/dbpedia-2026-06-20T175737.png
security:
- kind: domain-security
  name: Dbpedia Domain Security
  slug: dbpedia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dbpedia
tags:
- Linked Data
- Knowledge Graph
- SPARQL
- Semantic Web
- Wikipedia
- Open Data
- Entity Linking
- RDF
- Ontology
website: https://www.dbpedia.org/
---
