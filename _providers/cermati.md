---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: This is the documentation of Cermati Protect Generic Insurance API
  name: Cermati Protect Generic Insurance API
  slug: cermati-protect-generic-insurance-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cermati/refs/heads/main/vendors/cermati-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cermati-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cermati/refs/heads/main/llms/cermati-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cermati-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cermati/refs/heads/main/hosts/cermati-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cermati-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cermati.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cermati.com/pages/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cermati.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cermatiprotect.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cermati
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cermati/refs/heads/main/security/cermati-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cermati-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cermati.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cermati.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cermati (PT Agregasi Cermat Indonesia) is a fintech aggregator offering a platform for loans, credit cards, insurance, investments and gold products in Indonesia. It provides consumers with information and access to thousands of financial products, and offers API access to product data for developers. Registered with OJK, it operates via its website https://www.cermati.com and mobile app.
image: https://next-static.cermati.com/marketplace/static/images/open-graph/cermati-og.jpg
layout: provider
modified: '2026-10-07'
name: Cermati
nav: Providers
network: true
overview: 'Cermati is listed with 1 API on the [APIs.io](https://apis.io/) network: Protect Generic Insurance API. Tagged areas include Fintech, Loans, Credit Cards, Insurance, and Investment.


  Cermati''s developer surface includes documentation and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 30.0
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cermati Domain Security
  slug: cermati-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cermati
tags:
- Fintech
- Loans
- Credit Cards
- Insurance
- Investment
- Indonesia
website: https://www.cermati.com/
---
