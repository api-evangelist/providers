---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zumba-fitness-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zumba-fitness-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.zumba.com/
created: '2026-07-17'
description: Zumba Fitness is a company surfaced as a portfolio company of insight-partners and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zumba-fitness.png
layout: provider
modified: '2026-07-17'
name: Zumba Fitness
nav: Providers
network: true
overview: Zumba Fitness is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
scopes:
- name: Zumba Fitness Scopes
  scope_count: 0
  slug: zumba-fitness-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 6.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zumba-fitness/refs/heads/main/screenshots/zumba-fitness-2026-09-02T171857.png
security:
- kind: authentication
  name: Zumba Fitness Authentication
  slug: zumba-fitness-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zumba Fitness Domain Security
  slug: zumba-fitness-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zumba Fitness Vulnerability Disclosure
  slug: zumba-fitness-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zumba-fitness
tags:
- Company
website: http://www.zumba.com/
---
