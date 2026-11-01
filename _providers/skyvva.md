---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SKYVVA provides a native Salesforce integration platform with a REST API documented in the SKYVVA Help Center.
  name: SKYVVA API
  slug: skyvva-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/skyvva/plans/skyvva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skyvva-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/skyvva/changelog/skyvva-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/skyvva-changelog.yml
- group: auth
  href: https://artifacts.apis.io/skyvva/authentication/skyvva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skyvva-authentication.yml
- group: agent
  href: https://artifacts.apis.io/skyvva/llms/skyvva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skyvva-llms.txt
- group: other
  href: https://artifacts.apis.io/skyvva/hosts/skyvva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skyvva-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skyvva.com/en/legal-notice.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skyvva.com/en/privacy-policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://skyvva.com/en/pricing.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.skyvva.com/articles/4-alerting-setup.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.skyvva.com/
- group: auth
  href: https://artifacts.apis.io/skyvva/security/skyvva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skyvva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skyvva.com/
created: '2026-10-21'
description: SKYVVA provides a native Salesforce integration platform that connects Salesforce with SAP, ERP, databases, and cloud applications without middleware. It offers real-time monitoring, data mapping, and a free proof‑of‑concept, targeting enterprises seeking seamless data flow between Salesforce and back‑office systems. The solution is cloud‑based, supports German and English languages, and emphasizes low‑code configuration and secure data handling.
image: https://skyvva.com/images/skyvva-og-1200x630.png
layout: provider
modified: '2026-10-21'
name: SKYVVA
nav: Providers
network: true
overview: 'SKYVVA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Salesforce, ERP, and Middleware-free.


  SKYVVA''s developer surface includes changelog, authentication, pricing, getting-started guide, documentation, and 7 more developer resources.'
plans:
- name: Skyvva Plans Pricing
  plan_count: 1
  slug: skyvva-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Skyvva Authentication
  slug: skyvva-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Skyvva Domain Security
  slug: skyvva-domain-security
  summary_line: TLSv1.3
slug: skyvva
tags:
- Company
- Integration
- Salesforce
- ERP
- Middleware-free
website: https://skyvva.com/
---
