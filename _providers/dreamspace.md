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
api_count: 1
apis:
- description: Experiment with AI models on an infinite canvas
  name: Dreamspace
  slug: dreamspace
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dreamspace/refs/heads/main/security/dreamspace-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dreamspace-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dreamspace/refs/heads/main/hosts/dreamspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamspace-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dreamspace/refs/heads/main/vendors/dreamspace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamspace-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.dreamspace.art/docs
- group: company
  title: ''
  type: Blog
  url: https://www.dreamspace.art/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dreamspace/refs/heads/main/security/dreamspace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamspace-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dreamspace/refs/heads/main/security/dreamspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamspace.art/
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.dreamspace.art/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Dreamspace.art is a creative platform that enables users to experiment with AI models on an infinite digital canvas. It offers tools for generating art, visualizing data, and building interactive AI‑driven experiences, all accessible via a web interface. The service showcases cutting‑edge generative AI capabilities, providing both hobbyists and developers a space to explore, prototype, and share AI‑generated creations in real time.
image: https://dreamspace.art/header.png
layout: provider
modified: '2026-10-16'
name: Dreamspace
nav: Providers
network: true
overview: 'Dreamspace is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Creative Platform, Generative Art, and Web.


  Dreamspace''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreamspace Domain Security
  slug: dreamspace-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dreamspace Vulnerability Disclosure
  slug: dreamspace-vulnerability-disclosure
  summary_line: no policy recorded
slug: dreamspace
tags:
- Company
- Artificial Intelligence
- Creative Platform
- Generative Art
- Web
website: https://dreamspace.art/
---
