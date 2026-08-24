---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.6
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.creditgenie.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.creditgenie.com
- group: operate
  title: ''
  type: Support
  url: https://creditgenie.zendesk.com/hc/en-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creditgenie.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creditgenie.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CreditGenie
- group: auth
  title: ''
  type: Security
  url: https://creditgenie.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/credit-genie-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/credit-genie-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/credit-genie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credit-genie-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credit-genie-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/credit-genie_stock/
coverage:
  checked: '2026-08-11'
  detail: Credit Genie ships only the consumer Cash Boost / Money Manager mobile app — there is no developer subdomain at all (api., developer. and docs.creditgenie.com return NXDOMAIN), the marketing host 404s /openapi.json, /swagger.json, /api-docs and /llms.txt, the first-party GitHub org github.com/CreditGenie holds zero public repositories, and the only machine-readable document the company serves anywhere is its RFC 9116 security.txt.
  evidence:
  - status: 0
    url: https://api.creditgenie.com/openapi.json
  - status: 404
    url: https://www.creditgenie.com/openapi.json
  - status: 404
    url: https://www.creditgenie.com/llms.txt
  - status: 404
    url: https://creditgenie.com/.well-known/api-catalog
  - status: 200
    url: https://creditgenie.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'Credit Genie is a consumer fintech operated by Creditly Corp. (Wilmington, Delaware, founded 2019) that runs a mobile-first money app for people living between paychecks. Its Cash Boost product advances $10-$150 with no interest and no hard credit check, funded against a linked bank account rather than a credit score, while Money Manager layers spending tracking, cash-flow prediction and subscription detection on top of that same bank connection. A Line of Credit product and AskGenie, an AI financial assistant, are in early access. Creditly Corp. is registered with the California DFPI under the CCFPL (registration 04-CCFPL-1956127-3514680) and has raised roughly $21M from Fortress Investment Group, Khosla Ventures, Sutter Hill Ventures, Tippet Venture Partners and Gabriel Investments. Credit Genie is a direct-to-consumer app company: it publishes no public API, developer portal, or machine-readable contract of any kind.'
image: https://creditgenie.com/images/app-logo.png
layout: provider
modified: '2026-08-11'
name: Credit Genie
nav: Providers
network: true
overview: 'Credit Genie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Consumer Finance, and Lending.


  Credit Genie''s developer surface includes signup flow, support, and 11 more developer resources.'
plans:
- name: Credit Genie Plans Pricing
  plan_count: 0
  slug: credit-genie-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Credit Genie Rate Limits
  slug: credit-genie-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Credit Genie Domain Security
  slug: credit-genie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Credit Genie Vulnerability Disclosure
  slug: credit-genie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: credit-genie
tags:
- Company
- Financial-Services
- Fintech
- Consumer Finance
- Lending
- Cash Advance
- Personal Finance
- Mobile Application
website: https://www.creditgenie.com/
---
