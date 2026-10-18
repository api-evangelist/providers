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
  href: https://raw.githubusercontent.com/api-evangelist/buyersight/refs/heads/main/hosts/buyersight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyersight-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buyersight/refs/heads/main/vendors/buyersight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buyersight-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.buyersight.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.buyersight.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://buyersight.io/price-in-sales-process/
- group: company
  title: ''
  type: Blog
  url: https://buyersight.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buyersight
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buyersight/refs/heads/main/security/buyersight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyersight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyersight.io
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://buyersight.io
  - status: 403
    url: https://equityzen.com/company/buyersight
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: BuyerSight provides an AI‑augmented outbound sales pipeline platform that combines automated prospecting, email deliverability management, and human sales expertise. It helps B2B companies increase qualified meetings, improve conversion rates, and reduce customer acquisition costs through AI‑driven recommendations and managed email infrastructure.
image: http://buyersight.io/wp-content/uploads/2025/05/Group-1686555974-1.svg
layout: provider
modified: '2026-10-06'
name: Buyersight
nav: Providers
network: true
overview: 'Buyersight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sales, Artificial Intelligence, Outbound, B2B, and Marketing.


  Buyersight''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
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
  name: Buyersight Domain Security
  slug: buyersight-domain-security
  summary_line: TLSv1.3
slug: buyersight
tags:
- Sales
- Artificial Intelligence
- Outbound
- B2B
- Marketing
website: https://buyersight.io
---
