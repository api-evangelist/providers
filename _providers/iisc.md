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
  name: Iisc Agentic Access
  operation_count: 8
  slug: iisc-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: ePrints@IISc is the open-access institutional repository of IISc research publications, established in 2002 on EPrints software. It is OAI-compliant and exposes an OAI-PMH metadata-harvesting interfac
  name: ePrints@IISc OAI-PMH
  slug: eprints-oai
- description: The Bitstreams API from Indian Institute of Science Bangalore — 2 operation(s) for bitstreams.
  name: Indian Institute of Science Bangalore Bitstreams API
  slug: iisc-bitstreams-api
- description: The Collections API from Indian Institute of Science Bangalore — 2 operation(s) for collections.
  name: Indian Institute of Science Bangalore Collections API
  slug: iisc-collections-api
- description: The Communities API from Indian Institute of Science Bangalore — 2 operation(s) for communities.
  name: Indian Institute of Science Bangalore Communities API
  slug: iisc-communities-api
- description: The Items API from Indian Institute of Science Bangalore — 2 operation(s) for items.
  name: Indian Institute of Science Bangalore Items API
  slug: iisc-items-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams API
  slug: open-iisc-bitstreams-api
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams Collections API
  slug: open-iisc-collections-api
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams Communities API
  slug: open-iisc-communities-api
- collection_type: open
  name: ETD@IISc DSpace REST Bitstreams Items API
  slug: open-iisc-items-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iisc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iisc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iisc.ac.in/
- group: build
  title: ''
  type: Library
  url: https://library.iisc.ac.in/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/IISc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/indian-institute-of-science/
- group: commercial
  title: ''
  type: Plans
  url: plans/iisc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iisc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iisc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Indian Institute of Science (IISc) Bangalore is India''s premier research-intensive university, founded in 1909, and ranked #211 in the QS World University Rankings 2025. IISc does not operate a formal, centralized public developer portal. Its confirmable public machine-readable footprint is academic: the ePrints@IISc institutional repository (EPrints software) exposes an OAI-PMH metadata interface, and the DSpace-based ETD@IISc theses repository is likewise OAI-compliant. Individual labs and centres publish open source on GitHub (for example cni-iisc, csl-iisc, val-iisc), but there is no single official institutional GitHub org with public repositories or a documented REST API program.'
examples:
- key_count: 2
  name: Iisc Listcollections Example
  slug: iisc-listCollections-example
- key_count: 2
  name: Iisc Listcommunities Example
  slug: iisc-listCommunities-example
- key_count: 2
  name: Iisc Listitems Example
  slug: iisc-listItems-example
finops:
- name: Iisc Finops
  service_category: Education
  slug: iisc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iisc.png
json_schemas:
- name: ETD@IISc Bitstream
  property_count: 14
  slug: iisc-bitstream
- name: ETD@IISc Collection
  property_count: 16
  slug: iisc-collection
- name: ETD@IISc Community
  property_count: 15
  slug: iisc-community
- name: ETD@IISc Item
  property_count: 11
  slug: iisc-item
json_structures:
- name: Iisc Community Structure
  property_count: 10
  slug: iisc-community-structure
- name: Iisc Item Structure
  property_count: 10
  slug: iisc-item-structure
jsonld:
- class_count: 25
  name: Iisc Context
  property_count: 1
  slug: iisc-context
layout: provider
modified: '2026-06-03'
name: Indian Institute of Science Bangalore
nav: Providers
network: true
overview: 'Indian Institute of Science Bangalore publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bitstreams API, Collections API, Communities API, and 1 more. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Indian Institute of Science Bangalore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Indian Institute of Science Bangalore''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Iisc Plans Pricing
  plan_count: 2
  slug: iisc-plans-pricing
random_paper: 126
rate_limits:
- limit_count: 1
  name: Iisc Rate Limits
  slug: iisc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Indian Institute of Science Bangalore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: iisc-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Indian Institute of Science Bangalore API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: iisc-rules
score:
  band: thin
  composite: 30.7
  delta: -7.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 55.9
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/iisc/refs/heads/main/screenshots/iisc-2026-06-20T183226.png
security:
- kind: domain-security
  name: Iisc Domain Security
  slug: iisc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iisc
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- OAI-PMH
- India
website: https://iisc.ac.in/
---
