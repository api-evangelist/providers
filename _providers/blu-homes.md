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
  score: 6.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blu-homes/refs/heads/main/llms/blu-homes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blu-homes-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blu-homes/refs/heads/main/well-known/blu-homes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blu-homes-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blu-homes/refs/heads/main/hosts/blu-homes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blu-homes-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blu-homes/refs/heads/main/vendors/blu-homes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blu-homes-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dvele.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dvele.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.dvele.com/press/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dvele.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.dvele.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dvele
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blu-homes/refs/heads/main/security/blu-homes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blu-homes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dvele.com/blu-homes/modern-modular-homes
coverage:
  checked: '2026-09-29'
  detail: Developer portal at https://www.dvele.com/developers returns HTML pages without machine‑readable OpenAPI or other contracts.
  evidence:
  - status: 200
    url: https://www.dvele.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blu Homes, originally a modular home builder, has been acquired by Dvele and now operates under the Dvele brand. The company focuses on sustainable, precision-engineered homes with low environmental impact, offering modern modular designs, advanced manufacturing, and health‑centric living spaces. Through Dvele, Blu Homes continues to provide innovative, energy‑efficient housing solutions for developers and homeowners seeking high‑quality, customizable homes.
layout: provider
modified: '2026-09-29'
name: Blu Homes
nav: Providers
network: true
overview: 'Blu Homes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Modular Homes, Sustainable Housing, Real Estate, and Dvele.


  Blu Homes'' developer surface includes engineering blog and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blu Homes Domain Security
  slug: blu-homes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blu-homes
tags:
- Company
- Modular Homes
- Sustainable Housing
- Real Estate
- Dvele
website: https://www.dvele.com/blu-homes/modern-modular-homes
---
