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
api_count: 1
apis:
- description: API for Ottimate (formerly Plate IQ) providing accounts payable automation services.
  name: Ottimate API
  slug: ottimate-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/plateiq-com/llms/plateiq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plateiq-com-llms.txt
- group: other
  href: https://artifacts.apis.io/plateiq-com/hosts/plateiq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plateiq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/plateiq-com/vendors/plateiq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plateiq-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ottimate.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://ottimate.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ottimate.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://ottimate.com/news/
- group: start
  title: ''
  type: Login
  url: https://auth.plateiq.com/login/?next=/oauth/authorize/%3Fresponse_type%3Dcode%26client_id%3DJ2QJoYRFSVu4hLdK7tZpEfx3qPWNSrGaBJt1OB4X%26redirect_uri%3Dhttps%253A//dashboard.plateiq.com/accounts/login/%253Fnext%253D%25252F%26scope%3Daccounts.can_access_dashboard
- group: other
  title: ''
  type: Leadership
  url: https://ottimate.com/leadership/
- group: docs
  title: ''
  type: Documentation
  url: https://ottimate.com/guides/
- group: company
  title: ''
  type: Blog
  url: https://ottimate.com/blog/
- group: auth
  href: https://artifacts.apis.io/plateiq-com/security/plateiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plateiq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plateiq.com
coverage:
  checked: '2026-10-25'
  detail: Documentation pages are HTML with heavy JavaScript and no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://ottimate.com/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Ottimate, formerly Plate IQ, provides AI‑powered accounts payable automation for finance teams, offering invoice capture, coding, approval workflows, and direct vendor payments. The platform integrates with major ERP systems such as NetSuite, QuickBooks, Sage, and Microsoft Dynamics, delivering real‑time spend visibility, error reduction, and compliance support across industries like hospitality, healthcare, and retail.
image: https://ottimate.com/wp-content/uploads/2025/09/ottimate-cover-image.png
layout: provider
modified: '2026-10-25'
name: Paro
nav: Providers
network: true
overview: 'Paro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Automation, AI, and AP.


  Paro''s developer surface includes support, documentation, engineering blog, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.9
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
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Plateiq Com Domain Security
  slug: plateiq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plateiq-com
tags:
- Company
- Finance
- Automation
- AI
- AP
website: https://plateiq.com
---
