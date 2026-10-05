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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asian-credit-fund/refs/heads/main/hosts/asian-credit-fund-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asian-credit-fund-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asian-credit-fund/refs/heads/main/security/asian-credit-fund-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asian-credit-fund-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asiancreditfund.com
- group: docs
  title: ''
  type: Documentation
  url: https://asiancreditfund.com/en/about-acf
- group: company
  title: ''
  type: About
  url: https://asiancreditfund.com/en/about-acf
- group: other
  title: ''
  type: ESG
  url: https://asiancreditfund.com/en/sd-esg-en
- group: company
  title: ''
  type: Careers
  url: https://asiancreditfund.com/en/career
coverage:
  checked: 2026-09-26
  detail: The provider's website is static HTML with no machine‑readable API specification discovered.
  evidence:
  - status: 200
    url: https://asiancreditfund.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Asian Credit Fund (ACF) is a Kazakh microfinance organization founded in 1997, providing microloans and non‑financial services to individuals and small businesses. Regulated by the National Bank of Kazakhstan, ACF aims to promote financial inclusion and sustainable development, offering ESG‑focused products and transparent reporting through annual and audit reports.
image: https://asiancreditfund.com/wp-content/uploads/2022/01/ACF-logo-25-anniversary.webp
layout: provider
modified: '2026-09-26'
name: Asian Credit Fund
nav: Providers
network: true
overview: 'Asian Credit Fund is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Microfinance, Kazakhstan, ESG, and Financial Inclusion.


  Asian Credit Fund''s developer surface includes documentation and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asian Credit Fund Domain Security
  slug: asian-credit-fund-domain-security
  summary_line: TLSv1.3
slug: asian-credit-fund
tags:
- Company
- Microfinance
- Kazakhstan
- ESG
- Financial Inclusion
website: https://asiancreditfund.com
---
