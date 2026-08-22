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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lancaster Agentic Access
  operation_count: 1
  slug: lancaster-agentic-access
  summary_line: 1 operation
api_count: 3
apis:
- description: Open-source AWS serverless application maintained by Lancaster University Library that listens for Ex Libris Alma webhook events and forwards them to backend SNS topics. Reference code for integrating
  name: Lancaster Library Alma Webhook Handler
  slug: alma-webhook-handler
- description: Library user, fine, loan, and renewal services exposed via Ex Libris Alma/Primo web services (getUser, getUserCash, getUserLoans, renewUserLoans) that power the iLancaster mobile app and student porta
  name: Lancaster Library Services (Ex Libris Alma/Primo)
  slug: library-services
- description: The Oai2 API from Lancaster University — 1 operation(s) for oai2.
  name: Lancaster University Oai2 API
  slug: lancaster-oai2-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lancaster EPrints OAI-PMH 2.0 Interface Oai2 API
  slug: open-lancaster-oai2-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lancaster-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lancaster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lancaster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lancaster.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lancaster-university
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lulibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/lancaster-university/
- group: other
  title: ''
  type: Repository
  url: https://eprints.lancs.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/lancaster-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lancaster-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lancaster-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Lancaster University is a collegiate public research university in Lancaster, United Kingdom, ranked #141 in the QS World University Rankings 2025. Its public, machine-accessible developer footprint is modest and centered on research and library systems: the Lancaster EPrints institutional repository exposes a live OAI-PMH 2.0 interface for harvesting metadata, the Lancaster University Library maintains open-source integration code on GitHub (including an Ex Libris Alma webhook handler and Pure metadata tooling), and library services such as loans and fines are surfaced through Ex Libris Alma/Primo web services that back the iLancaster mobile app. There is no single public, self-service API developer portal; most service APIs are internal or gated.'
examples:
- key_count: 2
  name: Lancaster Getrecord Example
  slug: lancaster-getrecord-example
- key_count: 2
  name: Lancaster Identify Example
  slug: lancaster-identify-example
finops:
- name: Lancaster Finops
  service_category: Education
  slug: lancaster-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lancaster.png
json_schemas:
- name: Lancaster EPrints OAI Identify
  property_count: 7
  slug: lancaster-identify
- name: Lancaster EPrints OAI Record
  property_count: 2
  slug: lancaster-record
json_structures:
- name: Lancaster Record Structure
  property_count: 2
  slug: lancaster-record-structure
jsonld:
- class_count: 18
  name: Lancaster Context
  property_count: 3
  slug: lancaster-context
layout: provider
modified: '2026-06-03'
name: Lancaster University
nav: Providers
network: true
overview: 'Lancaster University publishes 1 API on the [APIs.io](https://apis.io/) network: Oai2 API. Tagged areas include Education, Higher Education, University, United Kingdom, and Research.


  The Lancaster University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lancaster University''s developer surface includes GitHub presence and 11 more developer resources.'
plans:
- name: Lancaster Plans Pricing
  plan_count: 2
  slug: lancaster-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Lancaster Rate Limits
  slug: lancaster-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lancaster University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lancaster-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Lancaster University API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: lancaster-rules
score:
  band: thin
  composite: 32.3
  delta: -5.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.4
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 37.5
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
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lancaster/refs/heads/main/screenshots/lancaster-2026-06-20T184256.png
security:
- kind: domain-security
  name: Lancaster Domain Security
  slug: lancaster-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lancaster Vulnerability Disclosure
  slug: lancaster-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lancaster
tags:
- Education
- Higher Education
- University
- United Kingdom
- Research
- Library
- Open Data
website: https://www.lancaster.ac.uk/
---
