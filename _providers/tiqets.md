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
- description: The Tiqets Supplier API allows supply partners to integrate booking systems with Tiqets.
  name: Tiqets Supplier API
  slug: tiqets-supplier-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/well-known/tiqets-tiqets-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tiqets-tiqets-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.tiqets.com/en/responsible-disclosure/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/llms/tiqets-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tiqets-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/well-known/tiqets-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tiqets-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/well-known/tiqets-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tiqets-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/well-known/tiqets-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tiqets-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/hosts/tiqets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tiqets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/vendors/tiqets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tiqets-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/packages/tiqets-packages.yml
  title: ''
  type: SDKs
  url: packages/tiqets-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/packages/tiqets-packages.yml
  title: ''
  type: Packages
  url: packages/tiqets-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiqets.com/en/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://support.tiqets.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiqets.com/en/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.tiqets.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tiqets
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/security/tiqets-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tiqets-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiqets/refs/heads/main/security/tiqets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tiqets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tiqets.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://suppliers.tiqets.com/mcp
  - status: 403
    url: https://support.tiqets.com/mcp
  - status: 403
    url: https://partners.tiqets.com/mcp
  - status: 200
    url: https://tiqets.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Tiqets is a global ticketing platform that allows travelers to discover, book, and instantly receive tickets for museums, attractions, theme parks, and activities worldwide. By partnering with cultural institutions and tour operators, Tiqets provides a seamless digital experience, offering mobile tickets, skip‑the‑line access, and multilingual support. The service aims to simplify travel planning and enhance on‑site experiences for millions of users each year, leveraging a robust API for partners to integrate ticketing capabilities into their own applications and platforms.
layout: provider
modified: '2026-10-12'
name: Tiqets
nav: Providers
network: true
overview: 'Tiqets is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Ticketing, and Marketplace.


  Tiqets'' developer surface includes support, engineering blog, and 16 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 51.8
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: unknown
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
  name: Tiqets Domain Security
  slug: tiqets-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tiqets Vulnerability Disclosure
  slug: tiqets-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tiqets
tags:
- Company
- Travel
- Ticketing
- Marketplace
website: https://tiqets.com/
---
