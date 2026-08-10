---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/koho-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/koho
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koho-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.koho.ca/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.koho.ca/security/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/koho-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/koho-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.koho.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/koho
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.koho.ca/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.koho.ca/legal/
- group: operate
  title: ''
  type: Support
  url: https://www.koho.ca/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.koho.ca/
- group: start
  title: ''
  type: SignUp
  url: https://web.koho.ca/register
created: '2026-07-23'
description: KOHO is a Canadian financial-technology company (neobank) founded in 2014 by Daniel Eberhard and headquartered in Vancouver, British Columbia, serving more than 2.5 million Canadians through a mobile-first money app. KOHO is not a chartered bank; it issues a KOHO Mastercard prepaid card through KOHO Financial Inc. and places customer balances in trust with CDIC-member institutions (its longstanding banking partner is Peoples Trust Company), while offering high-interest savings, cash back, credit building, Cover cash advances, and Pay Later. The company is in the final stages of pursuing a federal Schedule I banking licence, which would make it one of Canada's first new federally regulated banks in decades, and in May 2026 it joined the Interac e-Transfer network directly as a Participant under the broadened access for Payment Service Providers. On the open-finance front, KOHO exposes no first-party public developer API or portal; consumer account and transaction data access
  today is available only through third-party aggregators (Plaid and Flinks), consistent with Canada's voluntary, not-yet-operational Consumer-Driven Banking framework.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: KOHO
nav: Providers
network: true
overview: 'KOHO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Fintech, and Neobank.


  KOHO''s developer surface includes support, signup flow, and 12 more developer resources.'
random_paper: 85
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Koho Domain Security
  slug: koho-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Koho Vulnerability Disclosure
  slug: koho-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Koho Trust Center
  slug: koho-trust-center
  summary_line: SOC 2 Type 2, PCI DSS
slug: koho
tags:
- Financial Services
- Banking
- Canada
- Fintech
- Neobank
- Payments
- Interac
- Data Aggregation
- Consumer-Driven Banking
website: https://www.koho.ca/
---
