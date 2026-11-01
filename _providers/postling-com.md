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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/postling-com/hosts/postling-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postling-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postling.com/privacy/
- group: auth
  href: https://artifacts.apis.io/postling-com/security/postling-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postling-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postling.com
coverage:
  checked: '2026-10-21'
  detail: The provider operates a marketing and finance blog with no public API documented.
  evidence:
  - status: 200
    url: https://postling.com
  reason: not-a-software-company
  state: none
created: '2026-10-21'
description: Waffl, operating under the postling.com domain, runs a marketing, business and finance blog offering articles on making money, side hustles, investing, crypto, and entrepreneurship. The site provides guides, tips, and insights for readers looking to grow wealth, start businesses, and navigate financial topics. Content includes how‑to tutorials, market analyses, and personal finance strategies, positioning Waffl as a resource for financial education and marketing advice.
layout: provider
modified: '2026-10-21'
name: Waffl
nav: Providers
network: true
overview: Waffl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Finance, Business, and Entrepreneurship.
random_paper: 20
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Postling Com Domain Security
  slug: postling-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postling-com
tags:
- Company
- Marketing
- Finance
- Business
- Entrepreneurship
website: https://postling.com
---
