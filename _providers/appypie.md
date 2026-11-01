---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/appypie/plans/appypie-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appypie-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.appypie.com/security
- group: auth
  href: https://artifacts.apis.io/appypie/authentication/appypie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appypie-authentication.yml
- group: agent
  href: https://artifacts.apis.io/appypie/llms/appypie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appypie-llms.txt
- group: other
  href: https://artifacts.apis.io/appypie/hosts/appypie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appypie-hosts.yml
- group: other
  href: https://artifacts.apis.io/appypie/vendors/appypie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appypie-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.appypie.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.appypie.com/
- group: auth
  href: https://artifacts.apis.io/appypie/security/appypie-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appypie-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/appypie/security/appypie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appypie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appypie.com/
- group: company
  title: ''
  type: Blog
  url: https://www.appypie.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appypie.com/app-builder/pricing-plan
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appypie.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appypie.com/privacy-policy
coverage:
  checked: '2026-10-20'
  detail: No public developer program or API documentation was found on the developer subdomain.
  evidence:
  - status: 200
    url: https://developer.appypieautomate.ai/
  reason: no-developer-program
  state: none
created: '2026-10-19'
description: Appy Pie LLP provides a no‑code AI‑powered app builder platform that lets users create native mobile apps, websites, and AI‑driven applications from simple text prompts. The service offers a wide range of modules such as payments, bookings, chat, analytics, and e‑commerce, enabling rapid deployment to Android, iOS, and web stores without writing code. It serves businesses of all sizes, offering free trials, enterprise plans, and a patented AI backend for app generation.
image: https://images.appypie.com/wp-content/uploads/2023/07/12141920/appy-pie-no-code-ai-platform.png
layout: provider
modified: '2026-10-19'
name: Appy Pie LLP
nav: Providers
network: true
overview: 'Appy Pie LLP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include No-Code, Artificial Intelligence, App Builder, Mobile App, and Web App.


  Appy Pie LLP''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Appypie Plans Pricing
  plan_count: 4
  slug: appypie-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Appypie Authentication
  slug: appypie-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Appypie Domain Security
  slug: appypie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Appypie Trust Center
  slug: appypie-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, FIPS 140
slug: appypie
tags:
- No-Code
- Artificial Intelligence
- App Builder
- Mobile App
- Web App
website: https://appypie.com/
---
