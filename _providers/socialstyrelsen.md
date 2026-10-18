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
  score: 10.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Public information and statistical data services provided by Socialstyrelsen. No public developer program or API documented.
  name: Socialstyrelsen API
  slug: socialstyrelsen-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/socialstyrelsen/refs/heads/main/well-known/socialstyrelsen-utbildning-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/socialstyrelsen-utbildning-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/socialstyrelsen/refs/heads/main/well-known/socialstyrelsen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/socialstyrelsen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/socialstyrelsen/refs/heads/main/hosts/socialstyrelsen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialstyrelsen-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.socialstyrelsen.se/statistik-och-data/register/
- group: company
  title: ''
  type: Newsroom
  url: https://www.socialstyrelsen.se/om-socialstyrelsen/pressrum/press/tandvard/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/socialstyrelsen/refs/heads/main/security/socialstyrelsen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialstyrelsen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.socialstyrelsen.se/
coverage:
  checked: '2026-10-12'
  detail: The agency provides public information but does not offer a developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.socialstyrelsen.se/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Socialstyrelsen, the National Board of Health and Welfare of Sweden, is a governmental authority responsible for developing and supervising health and social care policies, regulations, and guidelines. It provides extensive public information, statistical data, and professional resources across areas such as child and youth health, cancer, mental health, elder care, and medical education. The agency also publishes standards, recommendations, and support tools for healthcare professionals and the public.
image: https://www.socialstyrelsen.se/contentassets/0b589a3b07a543e9b695abaa69908dd9/socialstyrelsen-logotyp-delning-1200x628.jpg?w=1200&h=630&format=jpg&mode=crop
layout: provider
modified: '2026-10-12'
name: Socialstyrelsen (National Board of Health and Welfare)
nav: Providers
network: true
overview: 'Socialstyrelsen (National Board of Health and Welfare) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Health, Sweden, PublicPolicy, and Healthcare.


  Socialstyrelsen (National Board of Health and Welfare)''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Socialstyrelsen Domain Security
  slug: socialstyrelsen-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: socialstyrelsen
tags:
- Government
- Health
- Sweden
- PublicPolicy
- Healthcare
website: https://www.socialstyrelsen.se/
---
