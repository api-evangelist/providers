---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: The Advance Passenger Information System (APIS) collects pre-arrival and pre-departure manifest data on all passengers and crew members flown or sailed into and out of the United States. The eAPIS web
  name: APIS / eAPIS
  slug: apis-eapis
- description: ACE is the U.S. Single Window through which the trade community reports imports and exports and CBP and Partner Government Agencies determine admissibility. Trade users access ACE via the ACE Secure D
  name: Automated Commercial Environment (ACE)
  slug: ace
- description: AES is the system through which exporters file Electronic Export Information (EEI) for goods leaving the United States. AES is integrated with ACE and supports both EDI filings and the AESDirect web f
  name: Automated Export System (AES)
  slug: aes
- description: The AESDirect WebLink Inquiry API allows authorized partners to programmatically query AESDirect filings. CBP provides separate certification (test) and production environments for the API. This is on
  name: AESDirect WebLink Inquiry API
  slug: aesdirect-weblink-inquiry-api
- description: ACAS requires inbound air carriers and other eligible parties to submit advance air cargo data to CBP for security risk-based screening prior to loading on aircraft destined for the United States. ACA
  name: Air Cargo Advance Screening (ACAS)
  slug: acas
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customs-and-border-protection-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/US-CBP
- group: company
  title: ''
  type: Website
  url: https://www.cbp.gov/
- group: other
  title: ''
  type: TradeAutomation
  url: https://www.cbp.gov/trade/automated
- group: other
  title: ''
  type: TradeOutreach
  url: https://www.cbp.gov/trade/stakeholder-engagement
- group: other
  title: ''
  type: ACEServiceDesk
  url: https://www.cbp.gov/contact/automated-broker-interface-service-desk
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.help.cbp.gov/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cbp.gov/newsroom
- group: other
  title: ''
  type: FOIA
  url: https://www.cbp.gov/site-policy-notices/foia
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbp.gov/site-policy-notices/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/CBP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-customs-and-border-protection/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/CustomsBorderProtect
- group: company
  title: ''
  type: Blog
  url: https://www.cbp.gov/rss.xml
created: '2024-12-03'
description: U.S. Customs and Border Protection (CBP) is the federal law enforcement agency within the Department of Homeland Security responsible for apprehending individuals attempting to enter the United States illegally, stemming the flow of illegal drugs and contraband, protecting agricultural and economic interests from harmful pests and diseases, protecting intellectual property, and regulating and facilitating international trade, collecting import duties, and enforcing U.S. trade laws. CBP's primary trade automation systems are the Automated Commercial Environment (ACE), the Automated Export System (AES), AESDirect, the Advance Passenger Information System (APIS / eAPIS), and the Air Cargo Advance Screening (ACAS) program. Trade integrations are predominantly delivered through Electronic Data Interchange (EDI) messaging via ACE, with a small set of CBP web services (e.g., the AESDirect WebLink Inquiry API) exposed for programmatic use.
finops:
- name: Customs And Border Protection Finops
  service_category: API
  slug: customs-and-border-protection-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customs-and-border-protection.png
layout: provider
modified: '2026-04-28'
name: Customs and Border Protection
nav: Providers
network: true
overview: 'Customs and Border Protection publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ACE, ACAS, AES, AESDirect, and APIS.


  Customs and Border Protection''s developer surface includes YouTube channel, engineering blog, and 12 more developer resources.'
plans:
- name: Customs And Border Protection Plans Pricing
  plan_count: 3
  slug: customs-and-border-protection-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Customs And Border Protection Rate Limits
  slug: customs-and-border-protection-rate-limits
score:
  band: emerging
  composite: 26.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customs-and-border-protection/refs/heads/main/screenshots/customs-and-border-protection-2026-06-20T175353.png
security:
- kind: domain-security
  name: Customs And Border Protection Domain Security
  slug: customs-and-border-protection-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: customs-and-border-protection
tags:
- ACE
- ACAS
- AES
- AESDirect
- APIS
- Borders
- Cargo
- CBP
- Customs
- Department of Homeland Security
- DHS
- EDI
- Exports
- Federal Government
- Imports
- International Trade
- Manifests
- Single Window
- Trade Compliance
website: https://www.cbp.gov/
---
