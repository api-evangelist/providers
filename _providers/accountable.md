---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL_template: https://{node}
  baseurl_source: spec_template
  description: Net asset value per share feeds.
  name: Accountable NAV API
  slug: accountable-nav-api
- baseURL_template: https://{node}
  baseurl_source: spec_template
  description: Collateral and reserve breakdown feeds.
  name: Accountable Proof of Reserves API
  slug: accountable-proof-of-reserves-api
- baseURL_template: https://{node}
  baseurl_source: spec_template
  description: On-chain redemption rate feeds.
  name: Accountable Redemption API
  slug: accountable-redemption-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Accountable / Proof of Reserves Feeds NAV API
  slug: open-accountable-nav-api
- collection_type: open
  name: Accountable NAV / Feeds Proof of Reserves API
  slug: open-accountable-proof-of-reserves-api
- collection_type: open
  name: Accountable NAV / Proof of Reserves Feeds Redemption API
  slug: open-accountable-redemption-api
common:
- group: company
  title: ''
  type: Website
  url: https://accountable.capital/
created: '2026-07-17'
description: 'Accountable is a company surfaced as a portfolio company of pantera-capital and added to the API Evangelist network as a stub for enrichment. Sector: crypto. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accountable.png
layout: provider
modified: '2026-07-17'
name: Accountable
nav: Providers
network: true
overview: 'Accountable publishes 3 APIs on the [APIs.io](https://apis.io/) network: NAV API, Proof of Reserves API, and Redemption API. Tagged areas include Company and Crypto.'
random_paper: 19
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 11.6
    developer_ergonomics: 0.0
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  provenance:
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
slug: accountable
tags:
- Company
- Crypto
website: https://accountable.capital/
---
