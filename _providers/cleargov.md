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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleargov/refs/heads/main/llms/cleargov-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleargov-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleargov/refs/heads/main/hosts/cleargov-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleargov-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cleargov.com/rc/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleargov/refs/heads/main/security/cleargov-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleargov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleargov.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cleargov.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://cleargov.com/docs
- group: company
  title: ''
  type: Blog
  url: https://cleargov.com/rc?type=a
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleargov.com/assets/ClearGov.com-Terms-of-Service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleargov.com/assets/ClearGov-Privacy-Policy-2026-w-printable-version.pdf
- group: start
  title: ''
  type: SignUp
  url: https://cleargov.com/sign-in
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://cleargov.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: ClearGov provides a cloud‑based financial engagement platform for local governments, enabling transparent budgeting, strategic planning, capital project tracking, and public reporting. Their tools help municipalities build trust through clear financial storytelling, interactive dashboards, and citizen engagement features, serving over 2,000 public finance teams nationwide.
image: https://cleargov.com/assets/2w1wm7vX-ClearGov-Logo.svg
layout: provider
modified: '2026-10-08'
name: ClearGov
nav: Providers
network: true
overview: 'ClearGov is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Software-as-a-Service, Government, and Transparency.


  ClearGov''s developer surface includes documentation, engineering blog, signup flow, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleargov Domain Security
  slug: cleargov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleargov
tags:
- Company
- Finance
- Software-as-a-Service
- Government
- Transparency
website: https://cleargov.com/
---
