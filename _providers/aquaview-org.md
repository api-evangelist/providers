---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aquaview-org/well-known/aquaview-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aquaview-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/aquaview-org/hosts/aquaview-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquaview-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/aquaview-org/vendors/aquaview-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquaview-org-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aquaview.org/
- group: start
  title: ''
  type: Login
  url: https://aquaview.org/login
- group: auth
  href: https://artifacts.apis.io/aquaview-org/security/aquaview-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquaview-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aquaview.org/
- group: docs
  title: ''
  type: Documentation
  url: https://aquaview.org/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.aquaview.org
- group: company
  title: ''
  type: Blog
  url: https://aquaview.org/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aquaview.org/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aquaview.org/terms-of-service
created: '2026-11-01'
description: AQUAVIEW provides a multi‑cloud enterprise data platform that unifies data ingestion, cataloging, and secure access across public clouds and on‑premises environments. It offers a STAC‑based catalog, high‑availability services, and APIs for discovering and managing environmental and operational datasets, enabling researchers and enterprises to accelerate product development and data‑driven insights.
image: https://aquaview.org/uploads/mainview-enterprise.jpeg
layout: provider
modified: '2026-11-01'
name: AQUAVIEW
nav: Providers
network: true
overview: 'AQUAVIEW is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Platform, Cloud, Enterprise, Environmental Data, and STAC.


  AQUAVIEW''s developer surface includes documentation, API reference, engineering blog, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 18.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquaview Org Domain Security
  slug: aquaview-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aquaview-org
tags:
- Data Platform
- Cloud
- Enterprise
- Environmental Data
- STAC
website: https://aquaview.org/
---
