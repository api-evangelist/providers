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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/sasken-communications/hosts/sasken-communications-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sasken-communications-hosts.yml
- group: other
  href: https://artifacts.apis.io/sasken-communications/vendors/sasken-communications-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sasken-communications-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sasken.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sasken.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sasken.com/insights/success-stories/pricing-elasticity-analysis
- group: company
  title: ''
  type: Newsroom
  url: https://www.sasken.com/news
- group: company
  title: ''
  type: Blog
  url: https://blog.sasken.com
- group: auth
  href: https://artifacts.apis.io/sasken-communications/security/sasken-communications-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sasken-communications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sasken.com/
coverage:
  checked: '2026-10-26'
  detail: No public developer portal or API documentation was found on the company website.
  evidence:
  - status: 200
    url: https://www.sasken.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Sasken Communications provides integrated communication solutions, including network infrastructure, IoT connectivity, and managed services for enterprises. Founded with a focus on innovation, the company leverages advanced technologies to deliver reliable, scalable, and secure communication platforms that enable digital transformation across industries.
layout: provider
modified: '2026-10-26'
name: Sasken Communications
nav: Providers
network: true
overview: 'Sasken Communications is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, IoT, Enterprise, and Network.


  Sasken Communications'' developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sasken Communications Domain Security
  slug: sasken-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sasken-communications
tags:
- Company
- Communications
- IoT
- Enterprise
- Network
website: https://www.sasken.com/
---
