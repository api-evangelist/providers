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
api_count: 1
apis:
- description: 'Undocumented private HTTP/JSON API at api.rightwayhealthcare.com that backs the Rightway member mobile apps (iOS/Android) and the member web app at member.rightwayhealthcare.com. The host is publicly '
  name: Rightway Member API
  slug: member-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rightway-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rightway-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rightway-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rightway-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.rightwayhealthcare.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rightwayhealthcare.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.rightwayhealthcare.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.rightwayhealthcare.com/members/get-help
- group: start
  title: ''
  type: Login
  url: https://member.rightwayhealthcare.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rightwayhealthcare.com/terms-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rightwayhealthcare.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.rightwayhealthcare.com/compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rightwayhealthcare.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/roadmaphealthcare
- group: company
  title: ''
  type: Careers
  url: https://www.rightwayhealthcare.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.rightwayhealthcare.com/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rightway-healthcare
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/rightway_stock/
created: '2026-08-02'
description: Rightway Healthcare is a New York-based healthcare navigation and pharmacy benefit management (PBM) company founded by Jordan Feldman and Dr. Theodore Feldman. It pairs a clinical care-navigation service — licensed pharmacists, nurses and care guides reachable by phone and in-app — with a fully transparent, 100% pass-through PBM that earns revenue from a single administrative fee rather than rebate spread. Rightway serves employers, health systems and public-sector plans covering roughly three million members, with named clients including Tyson Foods, TikTok and Zoom, and ships member-facing iOS, Android and web apps backed by a private mobile API. The company is HITRUST CSF certified and SOC 2 attested. It publishes no public developer program, API documentation or machine-readable API contract as of this profiling pass.
image: https://cdn.sanity.io/images/c67aqxu5/production/8ebd5e736e6fed503510282e4032d6a90c9041e5-2400x1260.png
layout: provider
modified: '2026-08-02'
name: Rightway
nav: Providers
network: true
overview: 'Rightway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmacy Benefits, PBM, and Care Navigation.


  Rightway''s developer surface includes engineering blog, support, and 16 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Rightway Domain Security
  slug: rightway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rightway
tags:
- Company
- Healthcare
- Pharmacy Benefits
- PBM
- Care Navigation
- Health Insurance
- Employee Benefits
- Digital Health
- HIPAA
website: https://www.rightwayhealthcare.com/
---
