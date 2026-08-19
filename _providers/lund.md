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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lund Agentic Access
  operation_count: 2
  slug: lund-agentic-access
  summary_line: 2 operations
api_count: 5
apis:
- description: OAI-PMH 2.0 metadata-harvesting endpoint for fully or partially harvesting Lund University publication metadata (Identify, ListMetadataFormats, ListRecords). No authentication required.
  name: Lund University Publications OAI-PMH
  slug: lup-oai
- description: SRU 1.1 Search/Retrieve via URL service using CQL (Contextual Query Language) for querying the LUP publication database. Scan and explain operations are not supported; no authentication required.
  name: Lund University Publications SRU
  slug: lup-sru
- description: unAPI 1 discovery service for retrieving alternate metadata formats of LUP records. No authentication required.
  name: Lund University Publications unAPI
  slug: lup-unapi
- description: Public external interface to the LUCRIS research information system, built on Elsevier Pure, covering researchers, organisations, outputs, projects, datasets, and activities. Lund documents that LUCRI
  name: Lund University Research Portal (LUCRIS / Pure)
  slug: research-portal
- description: The Publication API from Lund University — 2 operation(s) for publication.
  name: Lund University Publication API
  slug: lund-publication-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lund University Publications (LUP) Search Publication API
  slug: open-lund-publication-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lund-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lund-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lund-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lunduniversity.lu.se/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lunduniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/lund-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lup.lub.lu.se/search/doc/api
- group: commercial
  title: ''
  type: Plans
  url: plans/lund-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lund-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lund-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Lund University is a public research university in Lund, Sweden, founded in 1666 and ranked #74 in the QS World University Rankings 2025. Its public developer and API footprint centers on the Lund University Libraries'' research-output and open-metadata services, principally Lund University Publications (LUP), which exposes a JSON Search API, OAI-PMH harvesting, SRU/CQL search, an unAPI discovery service, and RSS feeds. The Lund University Research Portal is an external interface to the LUCRIS research information system built on Elsevier Pure. Administrative, identity (SWAMID/SAML federation), and student-information systems exist but are gated behind institutional affiliation rather than openly self-service.'
examples:
- key_count: 5
  name: Lund Searchpublications Example
  slug: lund-searchpublications-example
finops:
- name: Lund Finops
  service_category: Education
  slug: lund-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lund.png
json_schemas:
- name: Publication
  property_count: 52
  slug: lund-publication
- name: SearchResult
  property_count: 5
  slug: lund-searchresult
json_structures:
- name: Lund Publication Structure
  property_count: 21
  slug: lund-publication-structure
jsonld:
- class_count: 29
  name: Lund Context
  property_count: 7
  slug: lund-context
layout: provider
modified: '2026-06-03'
name: Lund University
nav: Providers
network: true
overview: 'Lund University publishes 1 API on the [APIs.io](https://apis.io/) network: Publication API. Tagged areas include Education, Higher Education, University, Sweden, and Research.


  The Lund University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lund University''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: Lund Plans Pricing
  plan_count: 2
  slug: lund-plans-pricing
random_paper: 137
rate_limits:
- limit_count: 1
  name: Lund Rate Limits
  slug: lund-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lund University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lund-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Lund University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: lund-rules
score:
  band: thin
  composite: 36.5
  delta: -4.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 68.5
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lund/refs/heads/main/screenshots/lund-2026-06-20T184805.png
security:
- kind: domain-security
  name: Lund Domain Security
  slug: lund-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lund Vulnerability Disclosure
  slug: lund-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lund
tags:
- Education
- Higher Education
- University
- Sweden
- Research
- Library
- Open Data
- Publications
website: https://www.lunduniversity.lu.se/
---
