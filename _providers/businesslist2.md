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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/businesslist2/refs/heads/main/hosts/businesslist2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/businesslist2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/businesslist2/refs/heads/main/vendors/businesslist2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/businesslist2-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nobul
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/businesslist2/refs/heads/main/security/businesslist2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/businesslist2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nobul.com
- group: docs
  title: ''
  type: Documentation
  url: https://nobul.com/page/about-us.html
- group: start
  title: ''
  type: GettingStarted
  url: https://nobul.com/page/how-it-works.html
- group: company
  title: ''
  type: Blog
  url: https://nobul.com/page/blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nobul.com/page/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nobul.com/page/privacy-policy.html
coverage:
  checked: '2026-10-06'
  detail: Businesslist2 is a real‑estate marketplace without a public developer API.
  evidence:
  - status: 200
    url: https://nobul.com
  reason: not-a-software-company
  state: none
created: '2026-10-06'
description: Businesslist2, also known as nobul, is a technology-driven real estate marketplace that enables agents from any brokerage to compete for consumer business. Founded in 2017 and headquartered in West Palm Beach, FL, US, the company leverages software and artificial intelligence to facilitate pre-IPO share investments through platforms like EquityZen. It offers a platform for buying and selling shares of private companies, aiming to democratize access to private market investments.
layout: provider
modified: '2026-10-06'
name: Businesslist2
nav: Providers
network: true
overview: 'Businesslist2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Marketplace, Artificial Intelligence, Pre-IPO, and Investment.


  Businesslist2''s developer surface includes documentation, getting-started guide, engineering blog, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Businesslist2 Domain Security
  slug: businesslist2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: businesslist2
tags:
- Real Estate
- Marketplace
- Artificial Intelligence
- Pre-IPO
- Investment
website: https://nobul.com
---
