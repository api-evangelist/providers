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
- group: company
  title: ''
  type: Website
  url: https://www.string-db.org/
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
