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
- description: BoardClic provides a SaaS platform for board management and governance. Documentation is hosted at the Help Center but no machine‑readable contract was found.
  name: BoardClic API
  slug: boardclic-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boardclic/refs/heads/main/well-known/boardclic-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boardclic-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boardclic/refs/heads/main/well-known/boardclic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boardclic-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boardclic/refs/heads/main/hosts/boardclic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boardclic-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://boardclic.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BoardClic
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boardclic/refs/heads/main/security/boardclic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardclic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boardclic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://boardclic.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://boardclic.com/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://boardclic.com/demo-request
- group: operate
  title: ''
  type: Support
  url: https://boardclic.com/contact
- group: company
  title: ''
  type: Blog
  url: https://boardclic.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://boardclic.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boardclic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boardclic.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://boardclic.com/demo-request
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://boardclic.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: BoardClic provides a digital platform that enables boards and private equity firms to conduct board, CEO, management and committee reviews, generate governance scores, and receive data‑driven insights. The service includes advisory modules, document analysis with secure digital signing, and AI‑enhanced assessments such as ESG maturity. It is used by over 600 boards worldwide to improve board performance and alignment.
image: https://framerusercontent.com/assets/tMFSHAvDh7sRL98KRr0wNQbG46c.png
layout: provider
modified: '2026-10-15'
name: BoardClic
nav: Providers
network: true
overview: 'BoardClic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Boards, Governance, Artificial Intelligence, Analytics, and Software-as-a-Service.


  BoardClic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boardclic Domain Security
  slug: boardclic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boardclic
tags:
- Boards
- Governance
- Artificial Intelligence
- Analytics
- Software-as-a-Service
website: https://boardclic.com/
---
