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
  href: https://artifacts.apis.io/recurate/vendors/recurate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recurate-vendors.yml
- group: other
  href: https://artifacts.apis.io/recurate/hosts/recurate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recurate-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trove.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trove.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://trove.com/news/
- group: company
  title: ''
  type: Blog
  url: https://trove.com/resources/blog
- group: company
  title: ''
  type: Website
  url: https://www.recurate.com/
- group: auth
  href: https://artifacts.apis.io/recurate/security/recurate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recurate-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: Access to Recurate's API specification is blocked by a 403 response, indicating authentication is required.
  evidence:
  - status: 403
    url: https://api.trove.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Recurate was originally founded as a SaaS platform focused on automating recurring billing and subscription management for businesses. Backed by Gradient Ventures, the company aimed to simplify payment orchestration, invoicing, and revenue recognition through a developer-friendly API. However, the public website https://www.recurate.com now redirects to https://trove.com, suggesting the brand has been rebranded, acquired, or otherwise discontinued. No dedicated documentation, developer portal, or API reference is currently discoverable on the redirected site. This profile reflects the limited publicly available information as of the assessment date.
image: https://trove.com/wp-content/uploads/2022/06/Trove-Logo.svg
layout: provider
modified: '2026-10-29'
name: Recurate
nav: Providers
network: true
overview: 'Recurate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include FinTech, Payments, Subscription, SaaS, and Venture-backed.


  Recurate''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Recurate Domain Security
  slug: recurate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: recurate
tags:
- FinTech
- Payments
- Subscription
- SaaS
- Venture-backed
website: https://www.recurate.com/
---
