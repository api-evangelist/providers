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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Birmingham Agentic Access
  operation_count: 2
  slug: university-of-birmingham-agentic-access
  summary_line: 2 operations
api_count: 4
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) interface for UBIRA eData, the University's EPrints-based research data repository. Returns Dublin Core metadata for archived, DOI-a
  name: UBIRA eData OAI-PMH
  slug: edata-oai
- description: OAI-PMH metadata harvesting interface for the University of Birmingham eTheses EPrints repository, providing access to metadata for full-text electronic theses produced by research postgraduates. No a
  name: UBIRA eTheses OAI-PMH
  slug: etheses-oai
- description: OAI-PMH metadata harvesting interface for the University of Birmingham ePapers EPrints repository, holding open access working papers, technical reports and other grey literature. No authentication re
  name: ePapers OAI-PMH
  slug: epapers-oai
- description: The Constructions API from University of Birmingham — 2 operation(s) for constructions.
  name: University of Birmingham Constructions API
  slug: university-of-birmingham-constructions-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-birmingham-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-birmingham-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.birmingham.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/University-of-Birmingham
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-birmingham/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/unibirmingham
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-birmingham-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-birmingham-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-birmingham-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Birmingham is a public research university in Birmingham, United Kingdom, and a founding member of the Russell Group, ranked #94 in the QS World University Rankings 2025. Its public developer/API footprint is limited and decentralized: there is no central developer portal or published API program. Confirmed machine-readable interfaces are concentrated in the library/research-repository ecosystem (EPrints-based repositories exposing OAI-PMH endpoints) plus a small open research API from the English Constructicon linguistics project. The institutional GitHub organization exists but currently exposes no public repositories.'
examples:
- key_count: 9
  name: University Of Birmingham Getconstruction Example
  slug: university-of-birmingham-getConstruction-example
finops:
- name: University Of Birmingham Finops
  service_category: Education
  slug: university-of-birmingham-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-birmingham.png
json_schemas:
- name: Construction
  property_count: 9
  slug: university-of-birmingham-construction
json_structures:
- name: University Of Birmingham Construction Structure
  property_count: 9
  slug: university-of-birmingham-construction-structure
jsonld:
- class_count: 12
  name: University Of Birmingham Context
  property_count: 1
  slug: university-of-birmingham-context
layout: provider
modified: '2026-06-03'
name: University of Birmingham
nav: Providers
network: true
overview: 'University of Birmingham publishes 1 API on the [APIs.io](https://apis.io/) network: Constructions API. Tagged areas include Education, Higher Education, University, United Kingdom, and Research.


  The University of Birmingham catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Birmingham''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Birmingham Plans Pricing
  plan_count: 2
  slug: university-of-birmingham-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: University Of Birmingham Rate Limits
  slug: university-of-birmingham-rate-limits
rules:
- name: University of Birmingham API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-birmingham-jsonschema-spectral-rules
- name: University of Birmingham API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 2
  slug: university-of-birmingham-rules
score:
  band: thin
  composite: 36.3
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.9
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 36.8
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
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-birmingham/refs/heads/main/screenshots/university-of-birmingham-2026-06-20T200137.png
security:
- kind: domain-security
  name: University Of Birmingham Domain Security
  slug: university-of-birmingham-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-birmingham
tags:
- Education
- Higher Education
- University
- United Kingdom
- Research
- Open Data
- Library
- OAI-PMH
website: https://www.birmingham.ac.uk/
---
