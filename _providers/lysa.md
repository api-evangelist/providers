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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Lysa platform (no machine-readable spec discovered)
  name: Lysa API
  slug: lysa-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/security/lysa-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lysa-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/llms/lysa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lysa-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/well-known/lysa-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lysa-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/well-known/lysa-lysa-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lysa-lysa-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/well-known/lysa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lysa-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/hosts/lysa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lysa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/vendors/lysa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lysa-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/security/lysa-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lysa-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lysa/refs/heads/main/security/lysa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lysa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lysa.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lysa.se/help-center
- group: start
  title: ''
  type: SignUp
  url: https://signup.lysa.se
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lysa.se/legal-information?document=legal%2Fse%2Fsv%2Fpersonuppgiftspolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lysa.se/legal-information?document=legal%2Fse%2Fsv%2Fsa-skyddas-dina-pengar
- group: company
  title: ''
  type: Blog
  url: https://www.lysa.se/newsroom
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on any discovered host.
  evidence:
  - status: 404
    url: https://api.lysa.se/openapi.json
  - status: 404
    url: https://api.lysa.se/openapi.yaml
  - status: 404
    url: https://api.lysa.se/v1/openapi.json
  - status: 404
    url: https://api.lysa.se/api-docs
  - status: 404
    url: https://api.lysa.se/docs
  - status: 404
    url: https://api.lysa.se/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Lysa is a Swedish fintech company offering automated investment and savings services. It provides a digital platform where users can open accounts, invest in diversified portfolios, and benefit from automatic rebalancing and tax optimization. The service emphasizes low fees, transparency, and a user-friendly experience, aiming to make investing accessible to a broad audience. Lysa also offers pension transfers, savings accounts, and financial education resources.
image: https://lysa.se/lysa-og-se.jpg
layout: provider
modified: '2026-10-15'
name: Lysa
nav: Providers
network: true
overview: 'Lysa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Investment, savings, Automation, and Sweden.


  Lysa''s developer surface includes documentation, signup flow, engineering blog, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lysa Domain Security
  slug: lysa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lysa Vulnerability Disclosure
  slug: lysa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lysa
tags:
- Fintech
- Investment
- savings
- Automation
- Sweden
- Company
website: https://www.lysa.se/
---
