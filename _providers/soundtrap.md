---
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soundtrap.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soundtrap.com/legal/privacy_world
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/soundtrap/refs/heads/main/llms/soundtrap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soundtrap-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/soundtrap/refs/heads/main/well-known/soundtrap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/soundtrap-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/soundtrap/refs/heads/main/hosts/soundtrap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soundtrap-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/soundtrap/refs/heads/main/vendors/soundtrap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soundtrap-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.soundtrap.com/legal/trust-center
- group: operate
  title: ''
  type: Support
  url: https://support.soundtrap.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soundtrap.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/soundtrap/refs/heads/main/security/soundtrap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soundtrap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soundtrap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.soundtrap.com/developers
- group: company
  title: ''
  type: Blog
  url: https://blog.soundtrap.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soundtrap.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.soundtrap.com/signup
coverage:
  checked: '2026-10-15'
  detail: Developer portal at https://www.soundtrap.com/developers is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.soundtrap.com/developers
  - status: 0
    url: https://api.soundtrap.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Soundtrap is an online music creation platform that lets users create, record, and collaborate on music projects directly in the browser. It offers a digital audio workstation with virtual instruments, loops, and effects, supporting both individual creators and educators. Users can share their tracks, collaborate in real-time, and access a library of royalty‑free sounds, making music production accessible without installing software.
image: https://static.soundtrap.com/payload-media/image/default-og-image.98381c1d.jpg
layout: provider
modified: '2026-10-15'
name: Soundtrap
nav: Providers
network: true
overview: 'Soundtrap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Collaboration, Education, Online-DAW, and Soundtrap.


  Soundtrap''s developer surface includes support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Soundtrap Domain Security
  slug: soundtrap-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: soundtrap
tags:
- Music
- Collaboration
- Education
- Online-DAW
- Soundtrap
website: https://soundtrap.com/
---
