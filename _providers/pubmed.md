---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pubmed Agentic Access
  operation_count: 9
  slug: pubmed-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 10
apis:
- description: The PMC Open Access API provides citation data, license information, and download links for Open Access articles in PubMed Central. Supports filtering by date and license type, returning FTP and HTTPS
  name: PubMed Central OA API
  slug: pubmed-central-oa-api
- description: The PMC OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting) API enables systematic harvesting of metadata for all PMC archive items and full text for licensed content. Follows the OAI-
  name: PMC OAI-PMH API
  slug: pmc-oai-pmh-api
- description: The BioC API provides full text retrieval of PubMed Central Open Access articles in BioC XML or JSON format, optimized for natural language processing (NLP) and text mining applications. Supports arti
  name: PMC BioC API
  slug: pmc-bioc-api
- description: The PMC ID Converter API translates between different article identifier formats including PubMed IDs (PMIDs), PubMed Central IDs (PMCIDs), Digital Object Identifiers (DOIs), and manuscript IDs. Essen
  name: PMC ID Converter API
  slug: pmc-id-converter-api
- description: Operations for managing sets of records on the Entrez History server
  name: PubMed History API
  slug: pubmed-history-api
- description: Operations for retrieving database metadata and information
  name: PubMed Info API
  slug: pubmed-info-api
- description: Operations for finding linked records between databases
  name: PubMed Links API
  slug: pubmed-links-api
- description: Operations for retrieving records from Entrez databases
  name: PubMed Retrieval API
  slug: pubmed-retrieval-api
- description: Operations for searching Entrez databases
  name: PubMed Search API
  slug: pubmed-search-api
- description: Operations for retrieving document summaries
  name: PubMed Summary API
  slug: pubmed-summary-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCBI Entrez E-utilities History API
  slug: open-pubmed-history-api
- collection_type: open
  name: NCBI Entrez E-utilities History Info API
  slug: open-pubmed-info-api
- collection_type: open
  name: NCBI Entrez E-utilities History Links API
  slug: open-pubmed-links-api
- collection_type: open
  name: NCBI Entrez E-utilities History Retrieval API
  slug: open-pubmed-retrieval-api
- collection_type: open
  name: NCBI Entrez E-utilities History Search API
  slug: open-pubmed-search-api
- collection_type: open
  name: NCBI Entrez E-utilities History Summary API
  slug: open-pubmed-summary-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pubmed-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pubmed-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pubmed-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://ncbiinsights.ncbi.nlm.nih.gov/feed/
created: '2026-06-13'
description: NCBI PubMed is the primary biomedical literature database providing free access to over 35 million citations and abstracts from life science journals and online books. The Entrez Programming Utilities (E-utilities) REST API enables programmatic searching, retrieval, and linking of citations, article metadata, abstracts, full-text links, and MeSH terms across PubMed and 38 other NCBI databases.
examples:
- key_count: 4
  name: Efetch Abstracts
  slug: efetch-abstracts
- key_count: 4
  name: Elink Related Articles
  slug: elink-related-articles
- key_count: 3
  name: Esearch Pubmed
  slug: esearch-pubmed
- key_count: 3
  name: Esummary Pubmed
  slug: esummary-pubmed
finops:
- name: Entrez Eutils
  service_category: ''
  slug: entrez-eutils
image: https://www.ncbi.nlm.nih.gov/coreutils/img/ncbilogo.png
json_schemas:
- name: ESearch Response
  property_count: 2
  slug: esearch-response
- name: PubMed Article
  property_count: 23
  slug: pubmed-article
jsonld:
- class_count: 0
  name: Pubmed Article Example Context
  property_count: 0
  slug: pubmed-article-example
- class_count: 4
  name: Pubmed Context
  property_count: 30
  slug: pubmed-context
layout: provider
modified: '2026-06-13'
name: PubMed
nav: Providers
network: true
overview: 'PubMed publishes 6 APIs on the [APIs.io](https://apis.io/) network, including History API, Info API, Links API, and 3 more. Tagged areas include Biomedical, Life Science, Research, Literature, and Citations.


  The PubMed catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  PubMed''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Entrez Eutils
  plan_count: 2
  slug: entrez-eutils
random_paper: 7
rate_limits:
- limit_count: 0
  name: Entrez Eutils
  slug: entrez-eutils
rules:
- effective_rule_count: 6
  extends: []
  name: PubMed API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: pubmed-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 57.8
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pubmed/refs/heads/main/screenshots/pubmed-2026-06-20T192246.png
security:
- kind: authentication
  name: Pubmed Authentication
  slug: pubmed-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pubmed Domain Security
  slug: pubmed-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pubmed
tags:
- Biomedical
- Life Science
- Research
- Literature
- Citations
- abstracts
- Mesh
- Genomics
- PubMed
- NCBI
---
