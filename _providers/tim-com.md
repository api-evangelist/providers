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
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: CAMARA-aligned API that returns the timestamp of the last SIM swap (or whether a swap occurred within a caller-supplied window) for a given TIM mobile number. Used by banks and fintechs as a signal ag
  name: TIM SIM Swap
  slug: tim-sim-swap
- description: CAMARA Number Verification API that authenticates a mobile device by silently confirming the MSISDN bound to the active mobile data session against the number asserted by the application. Eliminates t
  name: TIM Number Verification
  slug: tim-number-verification
- description: KYC Match API that compares customer-supplied attributes (name, tax ID, date of birth, address) against TIM's subscriber records and returns per-attribute match scores. Used during onboarding to valid
  name: TIM Know Your Customer - Match
  slug: tim-know-your-customer-match
- description: 'Given an IP address observed by a relying party, returns the TIM mobile number (MSISDN) currently associated with that radio session. Intended for banking and payment apps that need to bind an in-app '
  name: TIM IP to MSISDN
  slug: tim-ip-to-msisdn
- description: Given an IP address, returns the TIM fixed-line or mobile number associated with the session. Extends IP-to-MSISDN to cover both mobile and broadband subscribers for fraud and access-control use cases
  name: TIM IP to Number
  slug: tim-ip-to-number
- description: CAMARA Device Location verification API offered by TIM Brasil Open Gateway. Confirms whether a mobile device is physically within a supplied geographic area at request time, supporting geofenced authe
  name: TIM Device Location
  slug: tim-device-location
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tim-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tim-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gruppotim.it/en.html
- group: company
  title: ''
  type: Website
  url: https://www.tim.it
- group: company
  title: ''
  type: Website
  url: https://www.tim.com.br
- group: start
  title: ''
  type: Portal
  url: https://developer.tim.it
- group: start
  title: ''
  type: Portal
  url: https://www.tim.com.br/open-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tim.it/apis-developer
- group: other
  title: ''
  type: Standards
  url: https://camaraproject.org/
- group: company
  title: ''
  type: About
  url: https://www.gruppotim.it/en/group.html
- group: operate
  title: ''
  type: PressRelease
  url: https://www.tim.com.br/sobre-a-tim/sala-de-imprensa/press-releases/institucional/tim-lanca-novas-apis
- group: other
  title: ''
  type: Subsidiary
  url: https://www.tisparkle.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.noovle.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.telsy.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.olivetti.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.gruppotim.it/en/investors.html
- group: company
  title: ''
  type: Careers
  url: https://www.gruppotim.it/en/careers.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tim-official-page/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TIMnewsroom
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/TIM
created: '2026-05-25'
description: TIM S.p.A. (formerly Telecom Italia) is the incumbent Italian telecommunications operator headquartered in Rome and one of the largest telcos in Europe. The group operates fixed and mobile networks across Italy under the TIM Consumer and TIM Enterprise brands, runs TIM Brasil (the second-largest mobile operator in Brazil), and owns a portfolio of technology subsidiaries including Sparkle (international connectivity and quantum-safe infrastructure), Noovle (cloud), Telsy (cybersecurity), and Olivetti (IT services). TIM exposes its mobile network as a programmable platform through the developer.tim.it portal in Italy and through TIM Open Gateway in Brazil, both implementing CAMARA-standard network APIs (SIM Swap, Number Verification, Know Your Customer, IP-to-MSISDN, IP-to- Number, Device Location) jointly defined by the Linux Foundation, TM Forum, and GSMA. These APIs let banks, fintechs, insurers, retailers, and online services authenticate users, detect SIM-swap fraud, verify
  customer identity, and locate devices using TIM's mobile network as the trust anchor. As of late 2025 TIM Brasil reported 50 million Open Gateway API queries across its catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tim-com.png
layout: provider
modified: '2026-05-25'
name: TIM
nav: Providers
network: true
overview: 'TIM publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Telco, Mobile Network Operator, Network APIs, and CAMARA.


  TIM''s developer surface includes developer portal, documentation, YouTube channel, and 17 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.4
  delta: -2.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tim-com/refs/heads/main/screenshots/tim-com-2026-06-20T195400.png
security:
- kind: domain-security
  name: Tim Com Domain Security
  slug: tim-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tim Com Vulnerability Disclosure
  slug: tim-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tim-com
tags:
- Telecommunications
- Telco
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- GSMA
- SIM Swap
- Number Verification
- Know Your Customer
- Identity
- Anti-Fraud
- Italy
- Brazil
- 5G
website: https://www.gruppotim.it/en.html
---
