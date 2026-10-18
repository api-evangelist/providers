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
- description: Provides modern banking solutions, including ATM-as-a-Service and digital banking platforms.
  name: NCR Atleos API
  slug: ncr-atleos-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ncr-atleos/refs/heads/main/hosts/ncr-atleos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ncr-atleos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ncr-atleos/refs/heads/main/vendors/ncr-atleos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ncr-atleos-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ncratleos.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.ncratleos.com/support
- group: auth
  title: ''
  type: Security
  url: https://www.ncratleos.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ncratleos.com/terms-and-conditions/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ncratleos.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.ncratleos.com/about-us/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.ncratleos.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ncr-atleos/refs/heads/main/security/ncr-atleos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ncr-atleos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ncratleos.com/
coverage:
  checked: '2026-10-13'
  detail: Developer portal https://portal.ncratleos.com/ returns HTTP 403, blocking access to API specifications.
  evidence:
  - status: 403
    url: https://portal.ncratleos.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-13'
description: NCR Atleos provides modern banking solutions, including ATM-as-a-Service, ATM network integration, and digital banking platforms. Their offerings span software, hardware, and consulting services aimed at transforming self‑service channels and improving operational efficiency for financial institutions.
image: https://cdn.prod.website-files.com/64a2be73942e1d57fed077f3/68c8563dffc324e53967f20e_Open%20Graph.jpg
layout: provider
modified: '2026-10-13'
name: NCR Atleos
nav: Providers
network: true
overview: 'NCR Atleos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, ATM, Software, and Services.


  NCR Atleos'' developer surface includes support and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ncr Atleos Domain Security
  slug: ncr-atleos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ncr-atleos
tags:
- Company
- Banking
- ATM
- Software
- Services
website: https://www.ncratleos.com/
---
