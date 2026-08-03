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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 76
  human_in_the_loop: 0
  name: University Of Vienna Agentic Access
  operation_count: 145
  slug: university-of-vienna-agentic-access
  summary_line: 145 operations · 76 acting
api_count: 16
apis:
- description: OAI-PMH metadata harvesting interface for the PHAIDRA repository, used by aggregators such as OpenAIRE, Europeana, BASE, OAPEN, EBSCO and Primo. Supports the oai_dc (Dublin Core) and oai_openaire meta
  name: PHAIDRA OAI-PMH Endpoint
  slug: phaidra-oai-pmh
- description: The pan-European Higher Education Institutions (HEI) API, operated by the European University Foundation, publishes structured institutional data for the University of Vienna in JSON:API format, inclu
  name: HEI API (University of Vienna record)
  slug: hei-api
- description: Requests for transforming and validating datastreams
  name: University of Vienna datastream API
  slug: university-of-vienna-datastream-api
- description: Requests related to users, user groups and organisation structure
  name: University of Vienna directory API
  slug: university-of-vienna-directory-api
- description: Requests to the imageserver
  name: University of Vienna imageserver API
  slug: university-of-vienna-imageserver-api
- description: Requests for manipulating object lists
  name: University of Vienna lists API
  slug: university-of-vienna-lists-api
- description: The misc API from University of Vienna — 7 operation(s) for misc.
  name: University of Vienna misc API
  slug: university-of-vienna-misc-api
- description: Look at the [OAI-PMH protocol](https://www.openarchives.org/pmh) used in this endpoint
  name: University of Vienna oai-pmh API
  slug: university-of-vienna-oai-pmh-api
- description: Additional requests for the manipulation of digital objects
  name: University of Vienna object-advanced API
  slug: university-of-vienna-object-advanced-api
- description: Most important requests you'll need to manage digital objects in PHAIDRA
  name: University of Vienna object-basics API
  slug: university-of-vienna-object-basics-api
- description: Requests for adding and removing object relationships
  name: University of Vienna relationships API
  slug: university-of-vienna-relationships-api
- description: The search API from University of Vienna — 1 operation(s) for search.
  name: University of Vienna search API
  slug: university-of-vienna-search-api
- description: Session management
  name: University of Vienna session API
  slug: university-of-vienna-session-api
- description: The stats API from University of Vienna — 4 operation(s) for stats.
  name: University of Vienna stats API
  slug: university-of-vienna-stats-api
- description: Requests for managing metadata templates
  name: University of Vienna templates API
  slug: university-of-vienna-templates-api
- description: Requests for controlled vocabularies
  name: University of Vienna vocabularies API
  slug: university-of-vienna-vocabularies-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-vienna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-vienna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-vienna-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.univie.ac.at/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/univienna/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-vienna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-vienna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-vienna-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Vienna (Universität Wien), founded in 1365, is Austria''s largest university and ranks #78 in the QS World University Rankings 2025. Its public, programmatically accessible footprint centers on research and scholarly infrastructure rather than a unified developer portal: PHAIDRA, the university''s institutional repository, exposes a documented REST(ish) API and an OAI-PMH metadata harvesting endpoint, and the institution''s structured data is also published through the pan-European HEI API. Course, library discovery (u:find / u:search) and student-information systems are public web services but do not publish open developer documentation. No central, branded API developer portal or official GitHub organization was confirmed.'
examples:
- key_count: 3
  name: University Of Vienna Object Info Example
  slug: university-of-vienna-object-info-example
- key_count: 3
  name: University Of Vienna Search Select Example
  slug: university-of-vienna-search-select-example
finops:
- name: University Of Vienna Finops
  service_category: Education
  slug: university-of-vienna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-vienna.png
json_schemas:
- name: PHAIDRA Solr Index Document
  property_count: 29
  slug: university-of-vienna-index
- name: PHAIDRA Object Info
  property_count: 30
  slug: university-of-vienna-object-info
json_structures:
- name: University Of Vienna Index Structure
  property_count: 29
  slug: university-of-vienna-index-structure
- name: University Of Vienna Object Info Structure
  property_count: 30
  slug: university-of-vienna-object-info-structure
jsonld:
- class_count: 28
  name: University Of Vienna Context
  property_count: 0
  slug: university-of-vienna-context
layout: provider
modified: '2026-06-03'
name: University of Vienna
nav: Providers
network: true
overview: 'University of Vienna publishes 14 APIs on the [APIs.io](https://apis.io/) network, including datastream API, directory API, imageserver API, and 11 more. Tagged areas include Education, Higher Education, University, Research, and Repository.


  The University of Vienna catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Vienna''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: University Of Vienna Plans Pricing
  plan_count: 2
  slug: university-of-vienna-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 1
  name: University Of Vienna Rate Limits
  slug: university-of-vienna-rate-limits
rules:
- name: University of Vienna API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-vienna-jsonschema-spectral-rules
- name: University of Vienna API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: university-of-vienna-rules
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-vienna/refs/heads/main/screenshots/university-of-vienna-2026-06-20T200302.png
security:
- kind: authentication
  name: University Of Vienna Authentication
  slug: university-of-vienna-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: University Of Vienna Domain Security
  slug: university-of-vienna-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-vienna
tags:
- Education
- Higher Education
- University
- Research
- Repository
- Open Data
- Austria
- Europe
website: https://www.univie.ac.at/en/
---
