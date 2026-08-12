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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Edinburgh Agentic Access
  operation_count: 20
  slug: university-of-edinburgh-agentic-access
  summary_line: 20 operations
api_count: 10
apis:
- description: Public OAI-PMH metadata harvesting endpoint for Edinburgh DataShare, exposing Dublin Core and other metadata formats for the University's research-data repository.
  name: Edinburgh DataShare OAI-PMH
  slug: datashare-oai
- description: Public OAI-PMH endpoint for the University's Pure research information system, surfaced publicly via Edinburgh Research Explorer. Supports harvesting of research-output metadata in multiple formats. P
  name: Edinburgh Research Explorer (Pure) OAI-PMH
  slug: pure-oai
- description: 'The University''s internal Enterprise APIs programme delivers Student Records, Timetabling and Staff APIs to support service integration. Documentation sits behind University SSO (Shibboleth/SAML) and '
  name: Enterprise APIs Programme (gated)
  slug: enterprise-apis
- description: Binary files attached to items
  name: University of Edinburgh Bitstreams API
  slug: university-of-edinburgh-bitstreams-api
- description: Collections of items
  name: University of Edinburgh Collections API
  slug: university-of-edinburgh-collections-api
- description: Top-level and nested communities
  name: University of Edinburgh Communities API
  slug: university-of-edinburgh-communities-api
- description: Community/collection tree
  name: University of Edinburgh Hierarchy API
  slug: university-of-edinburgh-hierarchy-api
- description: Repository items and their metadata/bitstreams
  name: University of Edinburgh Items API
  slug: university-of-edinburgh-items-api
- description: Metadata schema and field registry
  name: University of Edinburgh Registries API
  slug: university-of-edinburgh-registries-api
- description: Service status
  name: University of Edinburgh Status API
  slug: university-of-edinburgh-status-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-edinburgh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-edinburgh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ed.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uoe-is-apps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-edinburgh/
- group: auth
  title: ''
  type: Authentication
  url: https://idp.ed.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-edinburgh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-edinburgh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-edinburgh-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Edinburgh is a public research university in Scotland, United Kingdom, founded in 1582 and ranked #20 in the QS World University Rankings 2025. Its public developer/API footprint is centred on open research infrastructure: the Edinburgh DataShare research-data repository (a DSpace instance exposing a public REST API and OAI-PMH endpoint) and Edinburgh Research Explorer / Pure (research information system with a public OAI-PMH harvesting endpoint; SOAP/REST web services are gated). The University also runs an internal Enterprise APIs programme (Student Records, Timetabling, Staff) that is documented behind SSO and not publicly accessible.'
examples:
- key_count: 2
  name: University Of Edinburgh Getcommunity Example
  slug: university-of-edinburgh-getCommunity-example
- key_count: 2
  name: University Of Edinburgh Getitem Example
  slug: university-of-edinburgh-getItem-example
finops:
- name: University Of Edinburgh Finops
  service_category: Education
  slug: university-of-edinburgh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-edinburgh.png
json_schemas:
- name: Edinburgh DataShare Bitstream
  property_count: 16
  slug: university-of-edinburgh-bitstream
- name: Edinburgh DataShare Collection
  property_count: 16
  slug: university-of-edinburgh-collection
- name: Edinburgh DataShare Community
  property_count: 15
  slug: university-of-edinburgh-community
- name: Edinburgh DataShare Item
  property_count: 12
  slug: university-of-edinburgh-item
json_structures:
- name: University Of Edinburgh Community Structure
  property_count: 10
  slug: university-of-edinburgh-community-structure
- name: University Of Edinburgh Item Structure
  property_count: 8
  slug: university-of-edinburgh-item-structure
jsonld:
- class_count: 4
  name: University Of Edinburgh Context
  property_count: 5
  slug: university-of-edinburgh-context
layout: provider
modified: '2026-06-03'
name: University of Edinburgh
nav: Providers
network: true
overview: 'University of Edinburgh publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bitstreams API, Collections API, Communities API, and 4 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Edinburgh catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Edinburgh''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: University Of Edinburgh Plans Pricing
  plan_count: 2
  slug: university-of-edinburgh-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: University Of Edinburgh Rate Limits
  slug: university-of-edinburgh-rate-limits
rules:
- name: University of Edinburgh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-edinburgh-jsonschema-spectral-rules
- name: University of Edinburgh API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: university-of-edinburgh-rules
score:
  band: thin
  composite: 39.0
  delta: -0.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-edinburgh/refs/heads/main/screenshots/university-of-edinburgh-2026-06-20T200145.png
security:
- kind: domain-security
  name: University Of Edinburgh Domain Security
  slug: university-of-edinburgh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-edinburgh
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Repository
- OAI-PMH
- United Kingdom
- Scotland
website: https://www.ed.ac.uk/
---
