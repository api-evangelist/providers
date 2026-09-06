---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveprofile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://liveprofile.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liveprofile
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveprofile.com
created: '2026-07-17'
description: LiveProfile is a cross-platform mobile messaging and chat product ("Stay connected with people and things that matter. Chat securely and express yourself freely."). It was originally backed by Lightspeed Venture Partners and is surfaced in the API Evangelist network as a portfolio-derived company profile. As of this enrichment pass, liveprofile.com is an invite-only relaunch teaser ("The New LiveProfile") running a waitlist, with apps advertised for Android, iPhone & iPad, and Mac/PC. The company maintains a public GitHub organization and a BetterUptime status page, but publishes no public API surface, developer documentation, OpenAPI, or SDKs at this time — so this profile carries identity and operational signals only, awaiting a real developer/API surface.
image: https://liveprofile.com/images/favicon-196x196.png
layout: provider
modified: '2026-07-20'
name: Liveprofile
nav: Providers
network: true
overview: Liveprofile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, Chat, Communications, and Mobile.
random_paper: 9
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liveprofile/refs/heads/main/screenshots/liveprofile-2026-07-25T225357.png
security:
- kind: domain-security
  name: Liveprofile Domain Security
  slug: liveprofile-domain-security
  summary_line: TLSv1.3
slug: liveprofile
tags:
- Company
- Messaging
- Chat
- Communications
- Mobile
- Consumer
website: https://liveprofile.com
---
