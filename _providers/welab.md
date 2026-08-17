---
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: WeLab Bank's Open API programme, published under the Hong Kong Monetary Authority Open API Framework and linked as "Open API" from the welab.bank site footer. The developer portal at portal-sandbox.we
  name: WeLab Bank Open API
  slug: welab-bank-open-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/welab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.welab.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal-sandbox.welab.bank/
- group: operate
  title: ''
  type: Support
  url: https://www.welab.bank/en/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.welab.bank/en/support/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.welab.bank/en/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.welab.bank/en/newsroom/
- group: company
  title: ''
  type: About
  url: https://www.welab.bank/en/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.welab.bank/en/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.welab.bank/en/legal/privacy-policy/
- group: auth
  title: ''
  type: RegulatoryDisclosures
  url: https://www.welab.bank/en/legal/regulatory-disclosures/
- group: auth
  title: ''
  type: SecurityTips
  url: https://www.welab.bank/en/legal/security-tips/
- group: company
  title: ''
  type: Careers
  url: https://www.welab.co/en/careers/
- group: auth
  title: ''
  type: Authentication
  url: authentication/welab-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/welab-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/welab-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/welab-llms.txt
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/welab-stock
coverage:
  checked: '2026-08-05'
  detail: WeLab Bank's own footer "Open API" link goes to portal-sandbox.welab.bank, a registered-third-party-service-provider portal that answers every non-interactive client with a Cloudflare 403, and its sandbox gateway api-sandbox.welab.bank refuses anonymous requests at the TLS layer with HTTP 400 "No required SSL certificate was sent" — so the account balance/status/transaction contract cannot be read without a WeLab-issued client certificate.
  evidence:
  - status: 400
    url: https://api-sandbox.welab.bank/
  - status: 403
    url: https://portal-sandbox.welab.bank/
  - status: 200
    url: https://www.welab.bank/en/legal/maintenance-schedule/
  reason: partner-login
  state: gated
created: '2026-08-05'
description: 'WeLab is a Hong Kong-headquartered fintech group founded in 2013 (incorporated November 2012 as WeLend) by Simon Loong, Kelly Wong and Frances Kang, operating consumer lending, digital banking and payments businesses across Hong Kong, mainland China and Indonesia. Its brands include WeLend (Hong Kong online lending), WeLab Digital and Taoxinji (mainland China), WeLab Pay, Tianmian Lab, and two licensed digital banks — WeLab Bank Limited, one of Hong Kong''s virtual banks licensed by the Hong Kong Monetary Authority in April 2019 and launched to the public in July 2020, and Bank Saqu (formerly Bank Jasa Jakarta) in Indonesia. WeLab Bank is the group''s API-bearing entity: under the HKMA Open API Framework it publishes an "Open API" developer portal for registered third-party service providers, backed by dedicated production and sandbox API gateways that require a client certificate (mutual TLS) before any request is served. Investors across its funding rounds include Sequoia
  Capital, Alibaba Entrepreneurs Fund, Credit Suisse and Allianz.'
image: https://www.welab.bank/uploads/We_Lab_Bank_logo_en_b54140e004.png
layout: provider
modified: '2026-08-05'
name: WeLab
nav: Providers
network: true
overview: 'WeLab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include fintech, digital-banking, virtual-bank, open-banking, and hong-kong.


  WeLab''s developer surface includes support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 76
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Welab Authentication
  slug: welab-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Welab Domain Security
  slug: welab-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: welab
tags:
- fintech
- digital-banking
- virtual-bank
- open-banking
- hong-kong
- indonesia
- consumer-lending
- payments
- hkma-open-api
- financial-services
website: https://www.welab.co/
---
