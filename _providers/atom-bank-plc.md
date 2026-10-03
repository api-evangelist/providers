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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atom-bank-plc/refs/heads/main/well-known/atom-bank-plc-atombank-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atom-bank-plc-atombank-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atom-bank-plc/refs/heads/main/well-known/atom-bank-plc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atom-bank-plc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atom-bank-plc/refs/heads/main/hosts/atom-bank-plc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atom-bank-plc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atom-bank-plc/refs/heads/main/vendors/atom-bank-plc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atom-bank-plc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atombank.co.uk/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.atombank.co.uk/help/faqs/
- group: operate
  title: ''
  type: StatusPage
  url: https://atombank.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://www.atombank.co.uk/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.atombank.co.uk/newsroom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.atombank.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.atombank.co.uk/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atombank
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atom-bank-plc/refs/heads/main/security/atom-bank-plc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atom-bank-plc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atombank.co.uk/
coverage:
  checked: 2026-09-26
  detail: Developer portal requires login to access API documentation
  evidence:
  - status: 200
    url: https://portal.atombank.co.uk/
  reason: partner-login
  state: gated
created: '2026-09-26'
description: Atom Bank plc is a UK‑based digital‑only bank founded in 2014 and launched in 2016. It offers savings accounts, mortgages and business loans through a mobile‑first app, emphasizing speed, low fees and competitive rates. Regulated by the FCA and PRA with FSCS protection, Atom Bank focuses on technology‑driven banking experiences, biometric security and real‑time notifications. The bank serves personal and SME customers across the United Kingdom, providing products such as Cash ISAs, Instant Savers, Fixed Savers, mortgages and commercial loans.
image: https://eu-images.contentstack.com/v3/assets/bltdab5bf2080bb23ac/blt8988f6b1beda5123/69ef4ac36aa0d702ac086189/atom-bank-preview-purple-background.jpg
layout: provider
modified: '2026-09-26'
name: Atom Bank plc
nav: Providers
network: true
overview: 'Atom Bank plc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Digital Bank, United Kingdom, and Fintech.


  Atom Bank plc''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atom Bank Plc Domain Security
  slug: atom-bank-plc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atom-bank-plc
tags:
- Company
- Banking
- Digital Bank
- United Kingdom
- Fintech
website: https://www.atombank.co.uk/
---
