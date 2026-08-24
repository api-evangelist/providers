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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splash-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.splashfinancial.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/splash-financial_stock/
- group: company
  title: ''
  type: Blog
  url: https://www.splashfinancial.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.splashfinancial.com/about-us/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splashfinancial.com/disclaimers/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splashfinancial.com/disclaimers/online-privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://my.splashfinancial.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/splashfinancial
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splash-financial-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splash-financial-well-known.yml
coverage:
  checked: '2026-08-05'
  detail: Splash Financial markets its origination technology to credit unions and community banks, but the only route to it is the "fill out the form and we'll contact you" partnerships page — there is no developer portal, and the live API host api.splashfinancial.com (an AWS API Gateway) answers every unauthenticated path, including /openapi.json, with {"message":"Not Found"} while robots.txt disallows /api/ and /partner/.
  evidence:
  - status: 200
    url: https://www.splashfinancial.com/about-us/partnerships
  - status: 404
    url: https://api.splashfinancial.com/openapi.json
  - status: 200
    url: https://www.splashfinancial.com/robots.txt
  - status: 200
    url: https://www.splashfinancial.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: Splash Financial is a Cleveland, Ohio financial technology company and online lending marketplace, founded in 2013, that matches consumers with loan offers from a network of partner banks and credit unions rather than lending directly itself. The platform uses automated underwriting to prequalify borrowers and present competing offers across student loan refinancing, personal loans, debt consolidation, home equity lines of credit, in-school private student loans, and medical school loan refinancing. The company reports having helped more than 125,000 people refinance over $6 billion in loans. Splash also sells its origination technology to credit unions and community banks as a partner channel, but that integration is arranged through a business development contact form and no public developer portal, API reference, or machine-readable specification is published.
image: https://www.splashfinancial.com/favicon.ico
layout: provider
modified: '2026-08-05'
name: Splash Financial
nav: Providers
network: true
overview: 'Splash Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Lending, Student Loans, and Personal Loans.


  Splash Financial''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Splash Financial Domain Security
  slug: splash-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: splash-financial
tags:
- Company
- Financial-Services
- Lending
- Student Loans
- Personal Loans
- Marketplace
- Fintech
- Debt Consolidation
- Home Equity
website: https://www.splashfinancial.com/
---
