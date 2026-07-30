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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Newcastle Agentic Access
  operation_count: 6
  slug: newcastle-agentic-access
  summary_line: 6 operations
api_count: 8
apis:
- description: Search and Data API for Newcastle University's Digitised Objects Repository, providing programmatic access to metadata and digitised materials from the university's collections.
  name: Digitised Objects Repository Search and Data API
  slug: digitised-objects
- description: API for the Eighteenth-Century Political Participation and Electoral Culture (ECPPEC) research project, providing access to historical British electoral datasets including pollbook records and electio
  name: ECPPEC Electoral Data API
  slug: ecppec
- description: Newcastle University's institutional research data repository, powered by Figshare, for documenting, archiving and publishing datasets and code. Programmatic access is available through the underlying
  name: data.ncl Research Data Repository (Figshare)
  slug: data-ncl
- description: Newcastle University's EPrints-based repositories (institutional outputs at eprints.ncl.ac.uk and electronic theses at theses.ncl.ac.uk) expose metadata harvesting via the standard EPrints OAI-PMH int
  name: EPrints Institutional Repository (OAI-PMH)
  slug: eprints
- description: An entity ordinarily describes a spatial location, such as a room in a building, or a pole in the street. In some circumstances, an entity may be a mobile piece of equipment, such as those used for va
  name: Newcastle University Entity API
  slug: newcastle-entity-api
- description: A feed is a representation of a measurement or parametrisation, usually a metric, for example the observed temperature.
  name: Newcastle University Feed API
  slug: newcastle-feed-api
- description: The Summary API from Newcastle University — 1 operation(s) for summary.
  name: Newcastle University Summary API
  slug: newcastle-summary-api
- description: There may be more than one timeseries associated with a feed, provided for convenience. Ordinarily there will be a plain timeseries, representing raw data from the device. In some cases, there may the
  name: Newcastle University Timeseries API
  slug: newcastle-timeseries-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/newcastle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newcastle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ncl.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/newcastleuniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/newcastle-university
- group: company
  title: ''
  type: Twitter
  url: https://x.com/UniofNewcastle
- group: commercial
  title: ''
  type: Plans
  url: plans/newcastle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newcastle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/newcastle-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Newcastle University is a public research university in Newcastle upon Tyne, United Kingdom, ranked #129 in the QS World University Rankings 2025. Its public developer and API footprint centers on research and open-data initiatives rather than a single central developer portal. Confirmed public APIs include the Newcastle Urban Observatory REST API (one of the UK''s largest open urban-sensing platforms, with an OpenAPI specification), the Digitised Objects Repository Search and Data API, and the ECPPEC electoral history research API. The university also operates a verified GitHub organization and a Figshare-powered research data repository (data.ncl), and runs EPrints-based institutional and thesis repositories that expose OAI-PMH.'
examples:
- key_count: 2
  name: Newcastle Entity List Example
  slug: newcastle-entity-list-example
- key_count: 3
  name: Newcastle Timeseries Entry Example
  slug: newcastle-timeseries-entry-example
finops:
- name: Newcastle Finops
  service_category: Education
  slug: newcastle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newcastle.png
json_schemas:
- name: Entity
  property_count: 5
  slug: newcastle-entity
- name: EntitySummary
  property_count: 3
  slug: newcastle-entitysummary
- name: Feed
  property_count: 8
  slug: newcastle-feed
- name: Timeseries
  property_count: 8
  slug: newcastle-timeseries
- name: TimeseriesEntry
  property_count: 6
  slug: newcastle-timeseriesentry
json_structures:
- name: Newcastle Entity Structure
  property_count: 5
  slug: newcastle-entity-structure
- name: Newcastle Feed Structure
  property_count: 8
  slug: newcastle-feed-structure
- name: Newcastle Timeseries Structure
  property_count: 8
  slug: newcastle-timeseries-structure
- name: Newcastle Timeseriesentry Structure
  property_count: 6
  slug: newcastle-timeseriesentry-structure
jsonld:
- class_count: 3
  name: Newcastle Context
  property_count: 8
  slug: newcastle-context
layout: provider
modified: '2026-06-03'
name: Newcastle University
nav: Providers
network: true
overview: 'Newcastle University publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entity API, Feed API, Summary API, and 1 more. Tagged areas include Education, Higher Education, University, United Kingdom, and Open Data.


  The Newcastle University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Newcastle University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Newcastle Plans Pricing
  plan_count: 2
  slug: newcastle-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Newcastle Rate Limits
  slug: newcastle-rate-limits
rules:
- name: Newcastle University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: newcastle-jsonschema-spectral-rules
- name: Newcastle University API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: newcastle-rules
score:
  band: thin
  composite: 35.7
  delta: -4.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.1
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 40.1
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
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newcastle/refs/heads/main/screenshots/newcastle-2026-06-20T190237.png
security:
- kind: domain-security
  name: Newcastle Domain Security
  slug: newcastle-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: newcastle
tags:
- Education
- Higher Education
- University
- United Kingdom
- Open Data
- Research Data
- Smart Cities
- Digital Library
website: https://www.ncl.ac.uk/
---
