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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yesgraph-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/yesgraph-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yesgraph-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yesgraph-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/yesgraph-lifecycle.yml
- group: company
  title: ''
  type: Website
  url: https://www.yesgraph.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yesgraph
created: '2026-07-17'
description: YesGraph was a San Francisco startup (YC W13) that provided a referral and contact-recommendation API. Its HTTP API and SDKs let mobile and web apps upload a user's address book and receive a machine-learning ranked list of which contacts a user should invite, powering smarter invite and referral flows. Founded by Ivan Kirigin (ex-Dropbox, ex-Facebook), YesGraph worked with companies including Airbnb, Atlassian, Gusto and Hired. In 2017 the team and its social-graph technology joined Lyft to strengthen Lyft's in-house referral program, and the public YesGraph API was deactivated on August 31, 2017. This profile documents the historical developer surface; the API is retired and no longer accepting traffic.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yesgraph.png
layout: provider
modified: '2026-07-21'
name: YesGraph
nav: Providers
network: true
overview: YesGraph is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Referrals, Recommendations, Contacts, and Social Graph.
random_paper: 6
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 7.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yesgraph/refs/heads/main/screenshots/yesgraph-2026-09-02T171243.png
security:
- kind: domain-security
  name: Yesgraph Domain Security
  slug: yesgraph-domain-security
  summary_line: no transport/DNS hardening detected
slug: yesgraph
tags:
- Company
- Referrals
- Recommendations
- Contacts
- Social Graph
- Growth
- Machine-Learning
- Invitations
website: https://www.yesgraph.com/
---
