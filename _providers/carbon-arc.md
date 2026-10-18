---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 27
  human_in_the_loop: 3
  name: Carbon Arc Agentic Access
  operation_count: 92
  slug: carbon-arc-agentic-access
  summary_line: 92 operations · 27 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Block API from Carbon Arc — 2 operation(s) for block.
  name: Carbon Arc Block API
  slug: carbon-arc-block-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Bucket Access API from Carbon Arc — 3 operation(s) for bucket access.
  name: Carbon Arc Bucket Access API
  slug: carbon-arc-bucket-access-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Catalog API from Carbon Arc — 11 operation(s) for catalog.
  name: Carbon Arc Catalog API
  slug: carbon-arc-catalog-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Clients API from Carbon Arc — 3 operation(s) for clients.
  name: Carbon Arc Clients API
  slug: carbon-arc-clients-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Data Library API from Carbon Arc — 9 operation(s) for data library.
  name: Carbon Arc Data Library API
  slug: carbon-arc-data-library-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Explore Use Cases API from Carbon Arc — 1 operation(s) for explore use cases.
  name: Carbon Arc Explore Use Cases API
  slug: carbon-arc-explore-use-cases-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Framework API from Carbon Arc — 14 operation(s) for framework.
  name: Carbon Arc Framework API
  slug: carbon-arc-framework-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Ontology API from Carbon Arc — 19 operation(s) for ontology.
  name: Carbon Arc Ontology API
  slug: carbon-arc-ontology-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Ontology Internal API from Carbon Arc — 2 operation(s) for ontology internal.
  name: Carbon Arc Ontology Internal API
  slug: carbon-arc-ontology-internal-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Polaris API from Carbon Arc — 8 operation(s) for polaris.
  name: Carbon Arc Polaris API
  slug: carbon-arc-polaris-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Prisms API from Carbon Arc — 2 operation(s) for prisms.
  name: Carbon Arc Prisms API
  slug: carbon-arc-prisms-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Public API from Carbon Arc — 3 operation(s) for public.
  name: Carbon Arc Public API
  slug: carbon-arc-public-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Research API from Carbon Arc — 1 operation(s) for research.
  name: Carbon Arc Research API
  slug: carbon-arc-research-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Tracking API from Carbon Arc — 1 operation(s) for tracking.
  name: Carbon Arc Tracking API
  slug: carbon-arc-tracking-api
- baseURL: https://api.carbonarc.co
  baseurl_source: declared
  description: The Transcripts API from Carbon Arc — 7 operation(s) for transcripts.
  name: Carbon Arc Transcripts API
  slug: carbon-arc-transcripts-api
artifact_total: 25
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/agentic-access/carbon-arc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carbon-arc-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/rules/carbon-arc-rules.yml
  title: ''
  type: Spectral
  url: rules/carbon-arc-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/json-ld/carbon-arc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carbon-arc-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/vocabulary/carbon-arc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carbon-arc-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/data-model/carbon-arc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carbon-arc-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/errors/carbon-arc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carbon-arc-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/conformance/carbon-arc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carbon-arc-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/hosts/carbon-arc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbon-arc-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/packages/carbon-arc-packages.yml
  title: ''
  type: SDKs
  url: packages/carbon-arc-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/packages/carbon-arc-packages.yml
  title: ''
  type: Packages
  url: packages/carbon-arc-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbon-arc/refs/heads/main/security/carbon-arc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbon-arc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbonarc.co
created: '2026-10-06'
description: Carbon Arc provides infrastructure for the AI economy, offering tools and services that enable developers to build, deploy, and scale AI applications. The platform includes APIs for model management, data pipelines, and monitoring, targeting enterprises and AI startups seeking robust, production‑grade solutions.
json_schemas:
- name: AdminAssetResponse
  property_count: 18
  slug: carbon-arc-admin-asset-response
- name: AssetDetailResponse
  property_count: 16
  slug: carbon-arc-asset-detail-response
- name: FrameworkMetadataResponse
  property_count: 14
  slug: carbon-arc-framework-metadata-response
- name: FrameworkOrderRead
  property_count: 16
  slug: carbon-arc-framework-order-read
- name: MaterializedPrism
  property_count: 12
  slug: carbon-arc-materialized-prism
- name: QueryJobResponse
  property_count: 12
  slug: carbon-arc-query-job-response
jsonld:
- class_count: 120
  name: Carbon Arc Context
  property_count: 287
  slug: carbon-arc-context
layout: provider
modified: '2026-10-06'
name: Carbon Arc
nav: Providers
network: true
overview: 'Carbon Arc publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Block API, Bucket Access API, Catalog API, and 12 more. Tagged areas include Artificial Intelligence, Infrastructure, Platform, MLOps, and Enterprise.


  The Carbon Arc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Carbon Arc API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: carbon-arc-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.8
    developer_ergonomics: 7.1
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 38.9
security:
- kind: domain-security
  name: Carbon Arc Domain Security
  slug: carbon-arc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-arc
tags:
- Artificial Intelligence
- Infrastructure
- Platform
- MLOps
- Enterprise
website: https://www.carbonarc.co
---
