---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 8.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mr-cooper-group-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mrcooper.com/blog/feed/
- group: company
  title: ''
  type: Website
  url: https://www.mrcooper.com/
- group: company
  title: ''
  type: ParentCompanyWebsite
  url: https://www.rocketcompanies.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.rocketcompanies.com/home/default.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mrcooper/
- group: start
  title: ''
  type: Login
  url: https://www.mrcooper.com/login
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Acquisition
  url: ''
- group: other
  title: ''
  type: Subsidiaries
  url: ''
- group: other
  title: ''
  type: History
  url: ''
created: '2026-05-23'
description: 'Mr. Cooper Group (formerly Nationstar Mortgage, NASDAQ: COOP) was a Coppell, Texas-based mortgage servicer with roughly $1.5T in unpaid principal balance under servicing and more than 4 million customers. It was acquired by Rocket Companies (NYSE: RKT) in an all-stock transaction announced March 31, 2025 (initial value $9.4B) and closed October 1, 2025 (final value approximately $14.2B). Mr. Cooper now operates as a Rocket Companies subsidiary; the corporate site mrcoopergroup.com redirects to rocketcompanies.com and the COOP ticker has been delisted. The consumer brand Mr. Cooper continues at mrcooper.com as one of seven Rocket Companies operating businesses (Rocket Mortgage, Redfin, Mr. Cooper, Rocket Homes, Rocket Close, Rocket Money, Rocket Loans). Mr. Cooper does not publish a public developer API or developer portal.'
features:
- description: Servicing of residential mortgage loans for approximately 4.3 million customers across the United States, covering payment processing, escrow, customer service, and loss mitigation.
  name: Mortgage Servicing
- description: Origination of home purchase, refinance, cash-out refinance, and home equity loans, now powered by Rocket Mortgage following the acquisition.
  name: Mortgage Origination
- description: Second-lien home equity products allowing customers to access equity 'without losing the rate on your first mortgage'.
  name: Home Equity Loans
- description: Mr. Cooper consumer portal at mrcooper.com providing account access, payment, statements, escrow management, and loan lookup.
  name: Online Self-Service
- description: Mr. Cooper mobile app for iOS and Android offering account management, payments, and document access.
  name: Mobile App
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mr-cooper-group.png
integrations:
- description: Mr. Cooper consumer mortgage originations are now branded 'Homeownership Powered by Rocket Mortgage' following the acquisition; mrcooper.com explicitly notes the two are 'separate companies uniting under the same parent organization'.
  name: Rocket Mortgage
- description: GSE counterparty for conforming loan servicing, securitization, and subservicing.
  name: Fannie Mae
- description: GSE counterparty for conforming loan servicing and subservicing.
  name: Freddie Mac
- description: Issuer relationship for FHA, VA, and USDA-backed mortgage-backed securities.
  name: Ginnie Mae
layout: provider
modified: '2026-05-23'
name: Mr. Cooper Group
nav: Providers
network: true
overview: 'Mr. Cooper Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mortgage, Mortgage Servicing, Financial Services, Real Estate, and Consumer Finance.


  Mr. Cooper Group''s developer surface includes engineering blog, authentication, and 5 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.8
  delta: -1.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mr-cooper-group/refs/heads/main/screenshots/mr-cooper-group-2026-08-07T184416.png
security:
- kind: domain-security
  name: Mr Cooper Group Domain Security
  slug: mr-cooper-group-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: mr-cooper-group
tags:
- Mortgage
- Mortgage Servicing
- Financial Services
- Real Estate
- Consumer Finance
- Acquired
- Rocket Companies
use_cases:
- description: Servicing third-party-originated and GSE-owned residential mortgages at scale, including conforming, FHA, VA, and USDA loans.
  name: Residential Mortgage Servicing
- description: Subservicing arrangements for banks, credit unions, and mortgage investors that own loans but outsource servicing operations.
  name: Mortgage Subservicing
- description: Servicing of delinquent, non-performing, and re-performing loans through the Rushmore Servicing subsidiary.
  name: Specialty Servicing
- description: REO management, valuation, title, and field services historically delivered through the Xome subsidiary.
  name: Real Estate Services
website: https://www.mrcooper.com/
---
