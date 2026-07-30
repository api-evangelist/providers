---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/becu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.becu.org/
- group: start
  title: ''
  type: Login
  url: https://onlinebanking.becu.org/BECUBankingWeb/Login.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.becu.org/online-privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.becu.org/website-terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.becu.org/support/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.becu.org/blog
created: '2026-07-23'
description: BECU (Boeing Employees' Credit Union) is a member-owned, not-for-profit state-chartered credit union founded in 1935 and headquartered in Tukwila, Washington (NMLS ID 490518). Originally serving Boeing employees, it is today one of the largest credit unions in the United States, offering consumer and business deposit accounts, lending, mortgages, and investment services across the Pacific Northwest and nationally through digital channels. Like the vast majority of US credit unions, BECU exposes no public first-party developer API or developer portal; its digital banking runs on established core and fintech vendors (FIS, LPL/Client Point, ICE/Ellie Mae for mortgage), and consumer-permissioned data access for third-party fintech apps is intermediated through data aggregators rather than a documented, self-serve BECU API. US open finance is voluntary and fragmented, and no mandated open-banking API contract applies here; the CFPB Section 1033 Personal Financial Data Rights rule
  is the emerging framework that will shape BECU's future data-access posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T12:00:00Z'
name: BECU
nav: Providers
network: true
overview: 'BECU is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Credit Union, and Open Finance.


  BECU''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.8
  delta: -3.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/becu/refs/heads/main/screenshots/becu-2026-07-25T202614.png
security:
- kind: domain-security
  name: Becu Domain Security
  slug: becu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: becu
tags:
- Financial Services
- Banking
- United States
- Credit Union
- Open Finance
- Data Aggregation
- CFPB 1033
website: https://www.becu.org/
---
