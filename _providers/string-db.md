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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Functional annotations and term lookup
  name: STRING Annotation API
  slug: string-db-annotation-api
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Functional enrichment analysis
  name: STRING Enrichment API
  slug: string-db-enrichment-api
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Protein homology and similarity scores
  name: STRING Homology API
  slug: string-db-homology-api
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Map protein names and synonyms to STRING identifiers
  name: STRING Identifiers API
  slug: string-db-identifiers-api
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Retrieve protein-protein interaction networks
  name: STRING Network API
  slug: string-db-network-api
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Utility endpoints (version, links, API key)
  name: STRING Utility API
  slug: string-db-utility-api
- baseURL: https://string-db.org
  baseurl_source: spec
  description: Values/Ranks GSEA-like enrichment (requires API key)
  name: STRING Valuesranks API
  slug: string-db-valuesranks-api
artifact_total: 29
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/string-db/refs/heads/main/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/string-db/refs/heads/main/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/string-db/refs/heads/main/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.string-db.org/blog/
- group: company
  title: ''
  type: Website
  url: https://www.string-db.org/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/string-db/refs/heads/main/security/string-db-domain-security.yml
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
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
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
mcp_servers:
- description: Remote MCP server at mcp.string-db.org over HTTP; 17 tools listed.
  name: STRING MCP Server
  slug: string-db
modified: '2026-10-06'
name: STRING
nav: Providers
network: true
overview: 'STRING publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Annotation API, Enrichment API, Homology API, and 4 more. Tagged areas include Bioinformatics, Proteins, Genomics, Life Sciences, and Research.


  The STRING catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  STRING''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: STRING — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: string-db-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.3
    catalog_earned_first_party: 0.0
    catalog_gap: 70.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 52.3
    developer_ergonomics: 19.0
    discoverability: 61.7
    operational_transparency: 5.3
  previous_composite: 32.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
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
website: https://www.string-db.org/
---
