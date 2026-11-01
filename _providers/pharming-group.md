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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.pharming.com/security-policy
- group: auth
  href: https://artifacts.apis.io/pharming-group/well-known/pharming-group-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pharming-group-security.txt
- group: agent
  href: https://artifacts.apis.io/pharming-group/well-known/pharming-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pharming-group-well-known.yml
- group: other
  href: https://artifacts.apis.io/pharming-group/hosts/pharming-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pharming-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/pharming-group/vendors/pharming-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pharming-group-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pharming.com/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://www.pharming.com/our-news/sign-up-for-pharming-s-egm-2020-webinar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pharming.com/privacy-center
- group: auth
  href: https://artifacts.apis.io/pharming-group/security/pharming-group-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pharming-group-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pharming-group/security/pharming-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pharming-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pharming.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.pharming.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Pharming Group is a biotechnology company focused on developing innovative RNA‑based therapeutics and vaccines. Founded in 2003, the firm leverages cutting‑edge mRNA technology to create treatments for rare genetic diseases and infectious diseases. With a portfolio that includes several pre‑clinical programs and partnerships with major pharmaceutical players, Pharming Group aims to transform the landscape of precision medicine through scalable, safe, and effective RNA solutions. The company operates globally, with research facilities in the United States and Europe, and maintains a strong commitment to scientific excellence and patient‑centric innovation.
layout: provider
modified: '2026-10-23'
name: Pharming Group
nav: Providers
network: true
overview: 'Pharming Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, RNA Therapeutics, Pharma, and Innovation.


  Pharming Group''s developer surface includes signup flow and 10 more developer resources.'
random_paper: 16
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
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pharming Group Domain Security
  slug: pharming-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pharming Group Vulnerability Disclosure
  slug: pharming-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pharming-group
tags:
- Company
- Biotechnology
- RNA Therapeutics
- Pharma
- Innovation
website: https://www.pharming.com/
---
