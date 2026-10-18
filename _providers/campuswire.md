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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/campuswire/refs/heads/main/hosts/campuswire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/campuswire-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://campuswire.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://dev.campuswire.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/campuswire/refs/heads/main/security/campuswire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/campuswire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://campuswire.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://campuswire.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campuswire.com/terms
- group: company
  title: ''
  type: Blog
  url: https://medium.com/campuswire
- group: company
  title: ''
  type: About
  url: https://campuswire.com/about
coverage:
  checked: '2026-10-06'
  detail: No public developer documentation or API specification was found on campuswire.com or its API subdomains.
  evidence:
  - status: 404
    url: https://api.campuswire.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Campuswire provides an online platform that facilitates class communication, Q&A, chatrooms, and live video for higher education. It aims to improve teaching and learning by offering a modern forum, real‑time discussions, and integrated tools for professors and students, all free to use. The service supports course announcements, discussions, and collaborative learning experiences, positioning itself as a comprehensive alternative to traditional LMS forums.
image: https://static.campuswire.com/images/social-banner.png
layout: provider
modified: '2026-10-06'
name: Campuswire
nav: Providers
network: true
overview: 'Campuswire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Collaboration, Platform, LMS, and Communications.


  Campuswire''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Campuswire Domain Security
  slug: campuswire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: campuswire
tags:
- Education
- Collaboration
- Platform
- LMS
- Communications
website: https://campuswire.com
---
