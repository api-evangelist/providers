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
- description: Clerq provides a next‑generation bank payments platform with developer tools and sandbox environments.
  name: Clerq API
  slug: clerq-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clerq/refs/heads/main/well-known/clerq-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clerq-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clerq/refs/heads/main/well-known/clerq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clerq-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clerq/refs/heads/main/hosts/clerq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clerq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clerq/refs/heads/main/vendors/clerq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clerq-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clerq.io/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.clerq.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clerq.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clerq.io/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.clerq.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clerq.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clerq/refs/heads/main/security/clerq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clerq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clerq.io/
coverage:
  checked: '2026-10-09'
  detail: API spec at https://api.clerq.io/openopenapi.json requires authentication, returning 401 Unauthorized.
  evidence:
  - status: 401
    url: https://api.clerq.io/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Clerq provides a next‑generation bank payments platform that enables businesses to accept low‑cost, guaranteed payments directly from customers’ bank accounts, both online and in‑store. By integrating with over 5,000 banks, Clerc reduces card processing fees by up to 75 % and offers chargeback guarantees, helping merchants increase conversion and cut costs. The platform serves sectors such as automotive, powersports, and e‑commerce, offering developer tools, sandbox environments, and comprehensive documentation.
image: https://cdn.prod.website-files.com/676951a41dbbf55924fcf5bc/676ac6bea62814a1d991a40e_Frame%201321315344%20(1).png
layout: provider
modified: '2026-10-08'
name: Clerq
nav: Providers
network: true
overview: 'Clerq is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Fintech, Banking, and B2B.


  Clerq''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Clerq Domain Security
  slug: clerq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clerq
tags:
- Payments
- Fintech
- Banking
- B2B
website: https://www.clerq.io/
---
