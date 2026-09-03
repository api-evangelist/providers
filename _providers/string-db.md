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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 20.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Functional annotations and term lookup
  name: STRING Annotation API
  slug: string-db-annotation-api
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Functional enrichment analysis
  name: STRING Enrichment API
  slug: string-db-enrichment-api
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Protein homology and similarity scores
  name: STRING Homology API
  slug: string-db-homology-api
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Map protein names and synonyms to STRING identifiers
  name: STRING Identifiers API
  slug: string-db-identifiers-api
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Retrieve protein-protein interaction networks
  name: STRING Network API
  slug: string-db-network-api
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Utility endpoints (version, links, API key)
  name: STRING Utility API
  slug: string-db-utility-api
- baseURL: https://string-db.org
  baseurl_source: declared
  description: Values/Ranks GSEA-like enrichment (requires API key)
  name: STRING Valuesranks API
  slug: string-db-valuesranks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: STRING REST Annotation API
  slug: open-string-db-annotation-api
- collection_type: open
  name: STRING REST Enrichment API
  slug: open-string-db-enrichment-api
- collection_type: open
  name: STRING REST Homology API
  slug: open-string-db-homology-api
- collection_type: open
  name: STRING REST Identifiers API
  slug: open-string-db-identifiers-api
- collection_type: open
  name: STRING REST Network API
  slug: open-string-db-network-api
- collection_type: open
  name: STRING REST Utility API
  slug: open-string-db-utility-api
- collection_type: open
  name: STRING REST Valuesranks API
  slug: open-string-db-valuesranks-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/string-db-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://string-db.org/cgi/info?footer_active_subpage=cookies
- group: other
  title: ''
  type: Licensing
  url: https://string-db.org/cgi/access?footer_active_subpage=licensing
- group: docs
  title: ''
  type: UsageGuidelines
  url: https://string-db.org/cgi/access?footer_active_subpage=usage
- group: docs
  title: ''
  type: APIDocumentation
  url: https://string-db.org/help/api/
- group: other
  title: ''
  type: Downloads
  url: https://string-db.org/cgi/download
description: STRING is a protein-protein interaction network database providing scored associations between proteins across thousands of organisms. The REST API enables programmatic access to interaction scores, network visualizations, functional enrichment analysis, homology data, and protein annotations. STRING integrates data from genomic context, co-expression, text mining, biochemical and genetic experiments, and curated databases.
examples:
- key_count: 3
  name: Functional Enrichment
  slug: functional-enrichment
- key_count: 3
  name: Get Interaction Partners
  slug: get-interaction-partners
- key_count: 3
  name: Get String Ids
  slug: get-string-ids
- key_count: 3
  name: Ppi Enrichment
  slug: ppi-enrichment
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://string-db.org/images/logo/logo_medium.png
json_schemas:
- name: EnrichmentResult
  property_count: 10
  slug: enrichment-result
- name: Interaction
  property_count: 13
  slug: interaction
- name: StringIdMapping
  property_count: 6
  slug: string-id-mapping
jsonld:
- class_count: 0
  name: context Context
  property_count: 38
  slug: context
layout: provider
modified: 2026-06-13
name: STRING
nav: Providers
network: true
overview: 'STRING publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Annotation API, Enrichment API, Homology API, and 4 more. Tagged areas include Bioinformatics, Proteins, Genomics, Life Sciences, and Research.


  The STRING catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: STRING API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: string-db-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 57.5
    developer_ergonomics: 16.7
    discoverability: 70.4
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 36.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/string-db/refs/heads/main/screenshots/string-db-2026-06-20T194621.png
security:
- kind: domain-security
  name: String Db Domain Security
  slug: string-db-domain-security
  summary_line: TLSv1.3
slug: string-db
tags:
- Bioinformatics
- Proteins
- Genomics
- Life Sciences
- Research
- Open Data
website: https://string-db.org
---
