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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bankbazaar/refs/heads/main/llms/bankbazaar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankbazaar-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bankbazaar/refs/heads/main/hosts/bankbazaar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankbazaar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bankbazaar/refs/heads/main/vendors/bankbazaar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankbazaar-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankbazaar.com/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://blog.bankbazaar.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bankbazaar
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankbazaar/refs/heads/main/security/bankbazaar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankbazaar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankbazaar.com
coverage:
  checked: '2026-09-27'
  detail: API spec endpoints return 403 Access Denied, no public OpenAPI or GraphQL schema is available.
  evidence:
  - status: 403
    url: https://api.bankbazaar.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: BankBazaar is India’s Largest FinTech Co-Branded Credit Card issuer & Online Platform for Free Credit Score with over 60 Million Registered Users. It offers credit card comparison, loan services, and financial products through its digital platform.
image: https://www.bankbazaar.com/images/social-share-og.webp
layout: provider
modified: '2026-09-27'
name: Bankbazaar
nav: Providers
network: true
overview: 'Bankbazaar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Credit Cards, Loans, India, and Financial Services.


  Bankbazaar''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bankbazaar Domain Security
  slug: bankbazaar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bankbazaar
tags:
- Fintech
- Credit Cards
- Loans
- India
- Financial Services
website: https://www.bankbazaar.com
---
