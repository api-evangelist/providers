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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schoolsfirst-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.schoolsfirstfcu.org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/schoolsfirst-federal-credit-union
- group: company
  title: ''
  type: Blog
  url: https://www.schoolsfirstfcu.org/about-us/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.schoolsfirstfcu.org/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.schoolsfirstfcu.org/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.schoolsfirstfcu.org/join/become-a-member/how-to-join/
- group: start
  title: ''
  type: Login
  url: https://online.schoolsfirstfcu.org/member-login/login
created: '2026-07-23'
description: 'SchoolsFirst Federal Credit Union is a federally chartered, member-owned credit union headquartered in Tustin, California, serving educators and their families. Founded in 1934 as Orange County Teachers Credit Union, it is the largest credit union in California and one of the largest in the United States, with roughly $31.9 billion in assets, over 1.4 million members, and about 70 branches. It offers savings, checking, loans, mortgages, credit cards, and investment services. Like most US credit unions, SchoolsFirst runs no first-party public developer program: probes of developer.schoolsfirstfcu.org fail to resolve and /developers returns 404, and its api.schoolsfirstfcu.org host is the member online-banking login backend, not a documented API. Consumer-permissioned data access is available only through open-finance aggregators (Plaid, Finicity, MX, Akoya) rather than a direct API. No public FDX participation or CFPB Section 1033 data-access posture is documented at this time.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: SchoolsFirst FCU
nav: Providers
network: true
overview: 'SchoolsFirst FCU is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Credit Union, and Open Finance.


  SchoolsFirst FCU''s developer surface includes engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.4
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Schoolsfirst Domain Security
  slug: schoolsfirst-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: schoolsfirst
tags:
- Financial-Services
- Banking
- United States
- Credit Union
- Open Finance
- Data Aggregation
website: https://www.schoolsfirstfcu.org
---
