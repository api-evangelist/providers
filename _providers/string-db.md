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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for accessing protein-protein interaction networks, functional enrichment results, homology data, and annotation information from the STRING database. Supports multiple output formats includi
  name: STRING REST API
  slug: string-rest-api
artifact_total: 14
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
overview: 'STRING publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Bioinformatics, Proteins, Genomics, Life Sciences, and Research.


  The STRING catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: STRING API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: string-db-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.9
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.2
    developer_ergonomics: 6.5
    discoverability: 70.4
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 38.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
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
