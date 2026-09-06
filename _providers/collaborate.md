---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://collaborate.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.webex.com/ — a different registrable domain (collaborate.com -> webex.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: company
  title: ''
  type: Website
  url: http://collaborate.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collaborate-domain-security.yml
created: '2026-07-17'
description: 'Collaborate.com was a mobile-first team collaboration service — unified document sharing, task management and team messaging across iPhone, iPod Touch, Android and the web, with integrations into Box, Dropbox and Google Drive. It was a service of Boston-based Kibits Corp, founded in 2011 by Matt Cutler (CEO) and David Greenstein (CTO), and was backed by GV (Google Ventures), Charles River Ventures, General Catalyst, SOS Ventures, Commonwealth Capital Ventures and Launch Capital. The company exited via acquisition by Cisco (December 2013), and its collaboration technology was folded into Cisco''s communications portfolio. The company no longer operates independently: collaborate.com is now a MarkMonitor-managed redirect that sends plain-HTTP traffic to https://www.webex.com/ and serves nothing over HTTPS. There is no developer portal, documentation, SDK, package, webhook or API surface to catalog — the asterisk in GV''s portfolio listing marks the exit.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/collaborate.png
layout: provider
modified: '2026-07-20'
name: Collaborate *
nav: Providers
network: true
overview: Collaborate * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Collaboration, Team Messaging, and File Sharing.
random_paper: 5
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/collaborate/refs/heads/main/screenshots/collaborate-2026-07-25T210041.png
security:
- kind: domain-security
  name: Collaborate Domain Security
  slug: collaborate-domain-security
  summary_line: HSTS
slug: collaborate
tags:
- Company
- Enterprise
- Collaboration
- Team Messaging
- File Sharing
- Task Management
- Mobile
- Acquired
website: http://collaborate.com
---
