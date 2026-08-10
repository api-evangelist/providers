---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accesshope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.myaccesshope.org/
- group: company
  title: ''
  type: About
  url: https://www.myaccesshope.org/about
- group: company
  title: ''
  type: Blog
  url: https://www.myaccesshope.org/blog
- group: company
  title: ''
  type: News
  url: https://www.myaccesshope.org/news
- group: operate
  title: ''
  type: PressReleases
  url: https://www.myaccesshope.org/press-releases
- group: company
  title: ''
  type: Careers
  url: https://www.myaccesshope.org/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.myaccesshope.org/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.myaccesshope.org/terms
- group: start
  title: ''
  type: Login
  url: https://app.myaccesshope.org/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accesshope
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/myaccesshope
- group: design
  title: ''
  type: Conformance
  url: conformance/accesshope-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.myaccesshope.org/press-releases/accesshope-wins-2024-fortress-cybersecurity-award
- group: auth
  title: ''
  type: TrustCenter
  url: security/accesshope-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accesshope-llms.txt
- group: company
  title: ''
  type: BlogRSS
  url: https://www.myaccesshope.org/blog/rss.xml
coverage:
  checked: '2026-08-06'
  detail: AccessHope onboards employer clients with a weekly eligibility file coordinated by an implementation team rather than an API; its only software surfaces are the credentialed member portal at app.myaccesshope.org (NextAuth credentials provider, robots.txt Disallow /) and a login-gated document portal at docs.myaccesshope.org, and there is no developer portal, API reference, spec, SDK or /.well-known/ document anywhere on the myaccesshope.org estate.
  evidence:
  - status: 404
    url: https://www.myaccesshope.org/developers
  - status: 404
    url: https://www.myaccesshope.org/api
  - status: 404
    url: https://www.myaccesshope.org/openapi.json
  - status: 404
    url: https://www.myaccesshope.org/.well-known/agent-card.json
  - status: 200
    url: https://app.myaccesshope.org/api/auth/providers
  - status: 200
    url: https://app.myaccesshope.org/robots.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'AccessHope is a Los Angeles-area health benefits company, founded in 2019 and wholly owned by City of Hope, that delivers remote cancer expertise as an employer-sponsored benefit. Its subspecialist teams review a member''s pathology, imaging, molecular testing and treatment plan against the latest evidence from a coalition of National Cancer Institute-designated Comprehensive Cancer Centers — City of Hope, Dana-Farber Cancer Institute, Emory Winship, Fred Hutch, Johns Hopkins Kimmel, Northwestern Medicine Lurie, and UT Southwestern Simmons — and return guidance to the member''s own local oncologist rather than moving the patient. AccessHope reports roughly 9 million covered members across 700+ employer and health-plan clients, including 70+ Fortune 500 companies. Delivery is business-to-business: employers, benefits consultants, health plans and navigation partners onboard through an eligibility file feed and an implementation-managed workflow, while members and clinical staff
  use credentialed web portals. AccessHope publishes no public developer program, API documentation, or machine-readable API contract.'
image: https://www.myaccesshope.org/hubfs/Logo.svg
layout: provider
modified: '2026-08-06'
name: AccessHope
nav: Providers
network: true
overview: 'AccessHope is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Cancer Care, and Employee Benefits.


  AccessHope''s developer surface includes engineering blog, product news, and 15 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 19.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accesshope/refs/heads/main/screenshots/accesshope-2026-08-07T160757.png
security:
- kind: domain-security
  name: Accesshope Domain Security
  slug: accesshope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accesshope Trust Center
  slug: accesshope-trust-center
  summary_line: HITRUST CSF r2, SOC 2 Type I, SOC 2 Type II
slug: accesshope
tags:
- Company
- Healthcare
- Oncology
- Cancer Care
- Employee Benefits
- Health Benefits
- Digital Health
- Telehealth
- Second Opinion
- Employer Health
website: https://www.myaccesshope.org/
---
