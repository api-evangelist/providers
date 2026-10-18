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
  href: https://raw.githubusercontent.com/api-evangelist/compumatrix/refs/heads/main/hosts/compumatrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compumatrix-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.compumatrix.com/sign-in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/compumatrix
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compumatrix/refs/heads/main/security/compumatrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compumatrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.compumatrix.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.compumatrix.com/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.compumatrix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.compumatrix.com/privacy
coverage:
  checked: '2026-10-10'
  detail: The provider's site returns HTML for typical OpenAPI URLs, offering no machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.compumatrix.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Compumatrix is a global web technologies and financial technology company founded in November 2006, based in Las Vegas, Nevada. It offers a social networking platform with a revenue sharing program, virtual prepaid cards, and a decentralized exchange. The company provides web development, mobile apps, CRM, ERP, and digital marketing services, aiming to empower entrepreneurs and individuals to earn online income through its platform.
layout: provider
modified: '2026-10-10'
name: Compumatrix
nav: Providers
network: true
overview: 'Compumatrix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WebTechnology, Fintech, SocialNetworking, and Entrepreneurship.


  Compumatrix''s developer surface includes documentation and 7 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compumatrix Domain Security
  slug: compumatrix-domain-security
  summary_line: TLSv1.3
slug: compumatrix
tags:
- Company
- WebTechnology
- Fintech
- SocialNetworking
- Entrepreneurship
website: https://www.compumatrix.com
---
