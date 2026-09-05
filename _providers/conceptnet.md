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
  band: agent-ready
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
    error_semantics: verified
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
  score: 29.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Conceptnet Agentic Access
  operation_count: 9
  slug: conceptnet-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The ConceptNet REST API exposes the full ConceptNet 5 knowledge graph via JSON-LD endpoints. Consumers can look up concept nodes by language and term, query edges by relation type, retrieve semantical
  name: ConceptNet REST API
  slug: conceptnet-rest-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: Look up concept nodes in the knowledge graph
  name: ConceptNet Concepts API
  slug: conceptnet-concepts-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: Access individual edge (assertion) records
  name: ConceptNet Edges API
  slug: conceptnet-edges-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: Complex multi-parameter edge queries
  name: ConceptNet Query API
  slug: conceptnet-query-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: Browse edges grouped by relation type
  name: ConceptNet Relations API
  slug: conceptnet-relations-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: Semantic similarity and relatedness using Numberbatch embeddings
  name: ConceptNet Similarity API
  slug: conceptnet-similarity-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: Access provenance and source information
  name: ConceptNet Sources API
  slug: conceptnet-sources-api
- baseURL: https://api.conceptnet.io
  baseurl_source: declared
  description: URI normalization and text standardization
  name: ConceptNet Utilities API
  slug: conceptnet-utilities-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ConceptNet REST Concepts API
  slug: open-conceptnet-concepts-api
- collection_type: open
  name: ConceptNet REST Concepts Edges API
  slug: open-conceptnet-edges-api
- collection_type: open
  name: ConceptNet REST Concepts Query API
  slug: open-conceptnet-query-api
- collection_type: open
  name: ConceptNet REST Concepts Relations API
  slug: open-conceptnet-relations-api
- collection_type: open
  name: ConceptNet REST Concepts Similarity API
  slug: open-conceptnet-similarity-api
- collection_type: open
  name: ConceptNet REST Concepts Sources API
  slug: open-conceptnet-sources-api
- collection_type: open
  name: ConceptNet REST Concepts Utilities API
  slug: open-conceptnet-utilities-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/commonsense/conceptnet5/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conceptnet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conceptnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conceptnet.io
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/commonsense/conceptnet5/wiki/API
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/commonsense/conceptnet5/wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commonsense
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/commonsense/conceptnet5
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by-sa/4.0/
- group: other
  title: ''
  type: Downloads
  url: https://github.com/commonsense/conceptnet5/wiki/Downloads
- group: operate
  title: ''
  type: FAQ
  url: https://github.com/commonsense/conceptnet5/wiki/FAQ
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/conceptnet-users
- group: commercial
  title: ''
  type: Plans
  url: plans/conceptnet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conceptnet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/conceptnet-finops.yml
created: '2026-06-13'
description: ConceptNet is a freely available multilingual knowledge graph that gives computers access to common-sense knowledge. It represents over 13 million links between concepts across 100+ languages, drawing from crowd-sourced resources (Open Mind Common Sense, Wiktionary), expert-created resources (WordNet, JMDict), and games with a purpose (Verbosity, nadya.jp). The public REST API provides JSON-LD responses and receives over 50,000 daily hits. ConceptNet also powers Numberbatch, a set of multilingual word embeddings aligned across languages that outperform word2vec, GloVe, and fastText on standard benchmarks.
examples:
- key_count: 4
  name: Get Concept Node
  slug: get-concept-node
- key_count: 4
  name: Get Related Concepts
  slug: get-related-concepts
- key_count: 4
  name: Get Relatedness
  slug: get-relatedness
- key_count: 4
  name: Normalize Uri
  slug: normalize-uri
- key_count: 4
  name: Query Edges
  slug: query-edges
finops:
- name: Conceptnet Finops
  service_category: ''
  slug: conceptnet-finops
image: https://conceptnet.io/img/conceptnet-logo.png
json_schemas:
- name: ConceptNet Concept Node
  property_count: 4
  slug: concept-node
- name: ConceptNet Edge
  property_count: 9
  slug: edge
- name: ConceptNet Relatedness Result
  property_count: 4
  slug: relatedness
layout: provider
modified: '2026-06-13'
name: ConceptNet
nav: Providers
network: true
overview: 'ConceptNet publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Concepts API, Edges API, Query API, and 4 more. Tagged areas include Knowledge Graph, NLP, Semantic Web, Common Sense, and Multilingual.


  The ConceptNet catalog on APIs.io includes 1 Spectral governance ruleset.


  ConceptNet''s developer surface includes documentation, getting-started guide, FAQ, support, and 11 more developer resources.'
plans:
- name: Conceptnet Plans Pricing
  plan_count: 2
  slug: conceptnet-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Conceptnet Rate Limits
  slug: conceptnet-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ConceptNet API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: conceptnet-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 53.7
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conceptnet/refs/heads/main/screenshots/conceptnet-2026-06-20T174840.png
security:
- kind: domain-security
  name: Conceptnet Domain Security
  slug: conceptnet-domain-security
  summary_line: TLSv1.2
slug: conceptnet
tags:
- Knowledge Graph
- NLP
- Semantic Web
- Common Sense
- Multilingual
- Word Embeddings
- Linked Data
- Open Data
website: https://conceptnet.io
---
