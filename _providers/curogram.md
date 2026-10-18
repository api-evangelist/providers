---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curogram/refs/heads/main/well-known/curogram-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curogram-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curogram/refs/heads/main/hosts/curogram-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curogram-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curogram/refs/heads/main/vendors/curogram-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curogram-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.curogram.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.curogram.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curogram.com/privacy
- group: start
  title: ''
  type: Login
  url: https://curogram.com/login
- group: company
  title: ''
  type: Blog
  url: https://curogram.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/curogram
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curogram/refs/heads/main/security/curogram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curogram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curogram.com
coverage:
  checked: '2026-10-12'
  detail: The provider's website offers no machine‑readable API specification and no documentation host was identified.
  evidence:
  - status: 200
    url: https://curogram.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curogram provides a HIPAA‑compliant, all‑in‑one communication platform for healthcare practices, offering secure two‑way texting, patient reminders, online forms, mass messaging, telemedicine, and integrated workflow automation to reduce phone calls, no‑shows, and staffing costs while improving patient engagement and online reputation.
image: https://curogram.com/hubfs/2024%20Website/Featured%20Images/6.png
layout: provider
modified: '2026-10-12'
name: Curogram
nav: Providers
network: true
overview: 'Curogram is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Text Messaging, Patient Engagement, Telehealth, EMR Integration, and Call Center.


  Curogram''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curogram Domain Security
  slug: curogram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curogram
tags:
- Text Messaging
- Patient Engagement
- Telehealth
- EMR Integration
- Call Center
- Healthcare Communication
- Practice Management
website: https://curogram.com
---
