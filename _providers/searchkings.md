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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/searchkings/security/searchkings-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/searchkings-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/searchkings/well-known/searchkings-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/searchkings-security.txt
- group: agent
  href: https://artifacts.apis.io/searchkings/well-known/searchkings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/searchkings-well-known.yml
- group: other
  href: https://artifacts.apis.io/searchkings/hosts/searchkings-hosts.yml
  title: ''
  type: Hosts
  url: hosts/searchkings-hosts.yml
- group: auth
  href: https://artifacts.apis.io/searchkings/security/searchkings-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/searchkings-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/searchkings/security/searchkings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/searchkings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://searchkings.com/
- group: company
  title: ''
  type: AboutUs
  url: https://searchkings.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://searchkings.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://searchkings.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://searchkings.com/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://searchkings.com/faqs/
coverage:
  checked: '2026-10-28'
  detail: Provider documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://searchkings.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: SearchKings provides AI‑enhanced Google Ads and digital marketing services for small and mid‑size businesses. Leveraging proprietary call‑intelligence and ChatGPT‑driven ad creation, they help clients generate leads, manage campaigns, and optimise spend across Google Ads, local services ads, eCommerce, and social platforms. Over 5,000 customers trust SearchKings for month‑to‑month, flat‑fee marketing solutions, with a $500 Google Ads credit for new sign‑ups and a focus on transparent reporting and AI‑powered performance.
layout: provider
modified: '2026-10-28'
name: SearchKings
nav: Providers
network: true
overview: 'SearchKings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, AI, and LeadGeneration.


  SearchKings'' developer surface includes FAQ and 11 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.5
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
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Searchkings Domain Security
  slug: searchkings-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Searchkings Vulnerability Disclosure
  slug: searchkings-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: searchkings
tags:
- Company
- Marketing
- Advertising
- AI
- LeadGeneration
website: https://searchkings.com/
---
