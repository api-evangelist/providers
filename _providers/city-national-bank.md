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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/city-national-bank-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/city-national-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cnb.com/privacy-security.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/city-national-bank-llms.txt
- group: start
  title: ''
  type: Login
  url: https://www.cnb.com/personal-banking/online-banking.html
- group: company
  title: ''
  type: Website
  url: https://www.cnb.com/
- group: company
  title: ''
  type: About
  url: https://www.cnb.com/about-us.html
- group: company
  title: ''
  type: Blog
  url: https://www.cnb.com/personal-banking/insights.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cnb.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cnb.com/legal.html
- group: operate
  title: ''
  type: Support
  url: https://www.cnb.com/contact-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/city-national-bank
created: '2026-07-23'
description: 'City National Bank is a national bank chartered in the United States and a wholly owned subsidiary of Royal Bank of Canada (RBC) since 2015, headquartered in Los Angeles, California and known historically as "the bank to the stars" for its deep roots in the entertainment industry. With roughly $98 billion in assets, it is an FDIC-insured, super-regional institution offering personal, business, and private banking, wealth management, treasury management, and capital markets services, with industry expertise across entertainment, healthcare, real estate, technology, and law. City National operates as CN Bank in Florida. It runs NO first-party public developer portal or documented public API: developer.cnb.com and developers.cnb.com do not resolve and api.cnb.com returns 404. Consistent with the voluntary, fragmented US open-finance model, consumer-permissioned account data is reached through third-party aggregators (Plaid, MX, Finicity, Akoya) rather than a direct City National
  API. As a covered depository institution it falls under the emerging CFPB Section 1033 Personal Financial Data Rights rule, but no City-National-specific 1033 or FDX participation posture is publicly documented. Its Canadian parent RBC runs a separate developer portal (developer.rbc.com) under a different charter that does not expose City National Bank APIs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: City National Bank
nav: Providers
network: true
overview: 'City National Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Super-Regional Bank, and National Bank.


  City National Bank''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.2
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/city-national-bank/refs/heads/main/screenshots/city-national-bank-2026-07-25T205437.png
security:
- kind: domain-security
  name: City National Bank Domain Security
  slug: city-national-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: City National Bank Vulnerability Disclosure
  slug: city-national-bank-vulnerability-disclosure
  summary_line: Hackerone
slug: city-national-bank
tags:
- Financial-Services
- Banking
- United States
- Super-Regional Bank
- National Bank
- Private Banking
- Wealth Management
- Open Finance
- Data Aggregation
website: https://www.cnb.com/
---
