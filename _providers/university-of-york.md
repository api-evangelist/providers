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
  name: University Of York Agentic Access
  operation_count: 2
  slug: university-of-york-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: YorSearch is the University of York library discovery service, built on the Ex Libris Primo platform with an Alma library services backend (view id 44YORK-NUI). Primo exposes programmatic discovery vi
  name: YorSearch Library Discovery (Ex Libris Primo)
  slug: yorsearch-primo
- description: The Oai2 API from University of York — 1 operation(s) for oai2.
  name: University of York Oai2 API
  slug: university-of-york-oai2-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: White Rose eTheses Online (OAI-PMH 2.0) Oai2 API
  slug: open-university-of-york-oai2-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-york-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-york-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.york.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/university-of-york
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/uniofyork/
- group: operate
  title: ''
  type: Status
  url: https://status.york.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-york-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-york-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-york-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-york-vocabulary.yml
- group: design
  title: ''
  type: x-rules
  url: rules/university-of-york-rules.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-york-context.jsonld
created: '2026-06-03'
description: 'The University of York is a public research university in York, United Kingdom, ranked #184 in the QS World University Rankings 2025 and a member of the Russell Group. The university does not operate a dedicated public developer portal with documented, self-service APIs. Its confirmed programmatic surface is largely standards-based and library/research oriented: OAI-PMH metadata harvesting via the shared White Rose Research Online and White Rose eTheses Online EPrints repositories, and an Ex Libris Primo/Alma library discovery layer (YorSearch). The institution maintains a verified GitHub organization focused on internal faculty/IT engineering tooling rather than externally published APIs.'
examples:
- key_count: 3
  name: University Of York Getrecord Example
  slug: university-of-york-getrecord-example
- key_count: 3
  name: University Of York Identify Example
  slug: university-of-york-identify-example
finops:
- name: University Of York Finops
  service_category: Education
  slug: university-of-york-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-york.png
json_schemas:
- name: OAI-PMH Record (White Rose / EPrints)
  property_count: 2
  slug: university-of-york-oai-record
json_structures:
- name: University Of York Oai Record Structure
  property_count: 2
  slug: university-of-york-oai-record-structure
jsonld:
- class_count: 12
  name: University Of York Context
  property_count: 6
  slug: university-of-york-context
layout: provider
modified: '2026-06-03'
name: University of York
nav: Providers
network: true
overview: 'University of York publishes 1 API on the [APIs.io](https://apis.io/) network: Oai2 API. Tagged areas include Education, Higher Education, University, United Kingdom, and Research.


  The University of York catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of York''s developer surface includes GitHub presence, status page, and 11 more developer resources.'
plans:
- name: University Of York Plans Pricing
  plan_count: 2
  slug: university-of-york-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: University Of York Rate Limits
  slug: university-of-york-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of York API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-york-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of York API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: university-of-york-rules
score:
  band: thin
  composite: 29.6
  delta: -7.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 57.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 36.9
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
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-york/refs/heads/main/screenshots/university-of-york-2026-06-20T200333.png
security:
- kind: domain-security
  name: University Of York Domain Security
  slug: university-of-york-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-york
tags:
- Education
- Higher Education
- University
- United Kingdom
- Research
- Library
- Open Access
- OAI-PMH
website: https://www.york.ac.uk/
---
