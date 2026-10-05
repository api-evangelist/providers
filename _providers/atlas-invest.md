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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlas-invest/refs/heads/main/well-known/atlas-invest-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlas-invest-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-invest/refs/heads/main/hosts/atlas-invest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-invest-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-invest/refs/heads/main/vendors/atlas-invest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlas-invest-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlas-invest/refs/heads/main/security/atlas-invest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-invest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlas-invest.co
- group: company
  title: ''
  type: Blog
  url: https://atlas-invest.co/blog
- group: docs
  title: ''
  type: Documentation
  url: https://atlas-invest.co/about-us/
- group: docs
  title: ''
  type: APIReference
  url: https://atlas-invest.co/about-us/
- group: operate
  title: ''
  type: Support
  url: https://atlas-invest.co/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlas-invest.co/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlas-invest.co/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/atlas-invest/workspace/atlas-invest
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlas-invest
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract found on discovered hosts.
  evidence:
  - status: 200
    url: https://backoffice.atlas-invest.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atlas Invest is an AI‑powered bridge lending platform that provides commercial real‑estate bridge loans and private credit solutions. Leveraging proprietary AI, deep industry expertise, and institutional capital, it connects brokers, borrowers, and investors to streamline deal flow, accelerate underwriting, and deliver transparent, fast financing for multifamily and mixed‑use properties across the United States.
layout: provider
modified: '2026-09-26'
name: Atlas Invest
nav: Providers
network: true
overview: 'Atlas Invest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Bridge Lending, Real Estate, and Artificial Intelligence.


  Atlas Invest''s developer surface includes engineering blog, documentation, API reference, support, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlas Invest Domain Security
  slug: atlas-invest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlas-invest
tags:
- Company
- Fintech
- Bridge Lending
- Real Estate
- Artificial Intelligence
- Private Credit
website: https://atlas-invest.co
---
