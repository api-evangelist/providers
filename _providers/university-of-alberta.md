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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Alberta Agentic Access
  operation_count: 2
  slug: university-of-alberta-agentic-access
  summary_line: 2 operations
api_count: 4
apis:
- description: Published University of Alberta collections and datasets on Borealis are harvestable via the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH), allowing other repositories and discov
  name: University of Alberta Borealis OAI-PMH Metadata Harvesting
  slug: borealis-oai-pmh
- description: The Info API from University of Alberta — 1 operation(s) for info.
  name: University of Alberta Info API
  slug: university-of-alberta-info-api
- description: The Search API from University of Alberta — 1 operation(s) for search.
  name: University of Alberta Search API
  slug: university-of-alberta-search-api
- description: The University of Alberta Library publishes open-source code through its GitHub organization (ualbertalib), including tools that interact with repository and digital-asset platform APIs (for example D
  name: University of Alberta Library Open Source (GitHub)
  slug: library-open-source
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: University of Alberta Research Data (Borealis Dataverse) Info API
  slug: open-university-of-alberta-info-api
- collection_type: open
  name: University of Alberta Research Data (Borealis Dataverse) Info Search API
  slug: open-university-of-alberta-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-alberta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-alberta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-alberta-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ualberta.ca/
- group: start
  title: Placeholder / pre-launch API site
  type: DeveloperPortal
  url: https://api.ualberta.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ualbertalib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-alberta/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-alberta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-alberta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-alberta-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Alberta is a public research university in Edmonton, Alberta, Canada, ranked #67 in the QS World University Rankings 2025. Its public, documented developer/API footprint is modest and decentralized: the central api.ualberta.ca site is a placeholder noting that the institution is "currently working to improve the way data is cataloged, shared, and governed," with no self-service developer portal yet. The strongest confirmed programmatic access is research data via the Borealis (Canadian Dataverse) repository, which exposes the University of Alberta research data collection through a REST Native/Search API and an OAI-PMH metadata endpoint. The University of Alberta Library also maintains an active open-source GitHub organization (ualbertalib). Course catalogue and Bear Tracks remain web-only with no official public API.'
examples:
- key_count: 2
  name: University Of Alberta Search Example
  slug: university-of-alberta-search-example
- key_count: 2
  name: University Of Alberta Version Example
  slug: university-of-alberta-version-example
finops:
- name: University Of Alberta Finops
  service_category: Education
  slug: university-of-alberta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-alberta.png
json_schemas:
- name: BorealisSearchItem
  property_count: 28
  slug: university-of-alberta-search-item
- name: BorealisSearchResponse
  property_count: 2
  slug: university-of-alberta-search-response
json_structures:
- name: University Of Alberta Search Item Structure
  property_count: 25
  slug: university-of-alberta-search-item-structure
jsonld:
- class_count: 15
  name: University Of Alberta Context
  property_count: 12
  slug: university-of-alberta-context
layout: provider
modified: '2026-07-25'
name: University of Alberta
nav: Providers
network: true
overview: 'University of Alberta publishes 2 APIs on the [APIs.io](https://apis.io/) network: Info API and Search API. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Alberta catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Alberta''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: University Of Alberta Plans Pricing
  plan_count: 2
  slug: university-of-alberta-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Alberta Rate Limits
  slug: university-of-alberta-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Alberta API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-alberta-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: University of Alberta API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: university-of-alberta-rules
score:
  band: thin
  composite: 38.6
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: University Of Alberta Authentication
  slug: university-of-alberta-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Alberta Domain Security
  slug: university-of-alberta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-alberta
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Library
- Canada
website: https://www.ualberta.ca/
---
