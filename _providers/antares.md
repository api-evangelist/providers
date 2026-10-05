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
  href: https://raw.githubusercontent.com/api-evangelist/antares/refs/heads/main/llms/antares-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/antares-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antares/refs/heads/main/hosts/antares-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antares-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antares/refs/heads/main/vendors/antares-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antares-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.antares.com/legal/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.antares.com/legal/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.antares.com/our-perspectives/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antares/refs/heads/main/security/antares-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antares-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.antares.com/
coverage:
  checked: 2026-09-25
  detail: Antares provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.antares.com
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Antares is a technology company that provides advanced data analytics and cloud-based solutions for financial services. The company focuses on delivering scalable platforms that enable real-time data processing, risk assessment, and market insights for institutional investors and traders. Antares aims to empower clients with customizable tools and APIs that integrate seamlessly into existing workflows, enhancing decision-making and operational efficiency.
image: https://www.antares.com/wp-content/uploads/2026/05/Antares-Capital_1200x675.webp
layout: provider
modified: '2026-09-25'
name: Antares
nav: Providers
network: true
overview: Antares is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Private Credit, Liquid Credit, Liquidity Solutions, Institutional Investors, and Insurance Companies.
random_paper: 2
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Antares Domain Security
  slug: antares-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antares
tags:
- Private Credit
- Liquid Credit
- Liquidity Solutions
- Institutional Investors
- Insurance Companies
- Financial Advisors
- Sponsors
- Alternative Credit
website: https://www.antares.com/
---
