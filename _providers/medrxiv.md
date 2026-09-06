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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Medrxiv Agentic Access
  operation_count: 5
  slug: medrxiv-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.medrxiv.org
  baseurl_source: declared
  description: Retrieve preprint metadata by date interval or DOI
  name: medRxiv Details API
  slug: medrxiv-details-api
- baseURL: https://api.medrxiv.org
  baseurl_source: declared
  description: Retrieve publication records linking preprints to published articles
  name: medRxiv Publications API
  slug: medrxiv-publications-api
- baseURL: https://api.medrxiv.org
  baseurl_source: declared
  description: Retrieve usage statistics for preprints
  name: medRxiv Usage API
  slug: medrxiv-usage-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: medRxiv REST Details API
  slug: open-medrxiv-details-api
- collection_type: open
  name: medRxiv REST Details Publications API
  slug: open-medrxiv-publications-api
- collection_type: open
  name: medRxiv REST Details Usage API
  slug: open-medrxiv-usage-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/medrxiv-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medrxiv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medrxiv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.medrxiv.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medrxiv.org/about-medrxiv
- group: company
  title: ''
  type: About
  url: https://www.medrxiv.org/about-medrxiv
- group: company
  title: ''
  type: Blog
  url: https://connect.medrxiv.org/medrxiv_xml.php?subject=all
created: '2026-06-13'
description: Cold Spring Harbor Laboratory preprint server for health sciences providing a REST API for searching and accessing medical and clinical research preprints before peer review. The API enables programmatic access to preprint metadata, publication information, and usage statistics for health science papers posted to medRxiv.
examples:
- key_count: 4
  name: Get Preprint By Doi
  slug: get-preprint-by-doi
- key_count: 4
  name: Get Preprints By Date Range
  slug: get-preprints-by-date-range
- key_count: 4
  name: Get Publication Records
  slug: get-publication-records
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medrxiv.png
json_schemas:
- name: PreprintDetail
  property_count: 14
  slug: preprint-detail
- name: PublicationRecord
  property_count: 12
  slug: publication-record
layout: provider
modified: '2026-06-13'
name: medRxiv
nav: Providers
network: true
overview: 'medRxiv publishes 3 APIs on the [APIs.io](https://apis.io/) network: Details API, Publications API, and Usage API. Tagged areas include Health Sciences, Preprints, Research, Open Access, and Medical Research.


  The medRxiv catalog on APIs.io includes 1 Spectral governance ruleset.


  medRxiv''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 11
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: medRxiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: medrxiv-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 66.3
    catalog_earned_first_party: 0.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 60.5
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 0.0
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medrxiv/refs/heads/main/screenshots/medrxiv-2026-06-20T185122.png
security:
- kind: domain-security
  name: Medrxiv Domain Security
  slug: medrxiv-domain-security
  summary_line: TLSv1.3
slug: medrxiv
tags:
- Health Sciences
- Preprints
- Research
- Open Access
- Medical Research
- Clinical Research
- Scientific Publications
website: https://www.medrxiv.org/
---
