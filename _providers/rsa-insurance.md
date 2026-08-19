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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rsa-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rsainsurance.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.intactinsurance.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rsainsurance.co.uk/brokers-and-partners/tools-resources/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rsainsurance.co.uk/brokers-and-partners/faqs/
- group: start
  title: ''
  type: Portal
  url: https://www.rsaconnect.rsagroup.co.uk/portal/UKHome.aspx
- group: start
  title: ''
  type: Portal
  url: https://www.rsaonline.rsagroup.com/AWE/Container.aspx?CurrentWorkflow=Logon&CurrentStep=Login
- group: start
  title: ''
  type: Portal
  url: https://www.services1.rsagroup.co.uk/webappserver/midphase2public/
- group: start
  title: ''
  type: Portal
  url: https://www.connect.intactinsurance.co.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.rsainsurance.co.uk/contact/broker-support/
- group: operate
  title: ''
  type: Support
  url: https://www.intactinsurance.co.uk/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.intactinsurance.co.uk/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rsainsurance.co.uk/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rsainsurance.co.uk/terms-conditions/
- group: auth
  title: ''
  type: Compliance
  url: https://www.rsainsurance.co.uk/regulation/
- group: auth
  title: ''
  type: Authentication
  url: authentication/rsa-insurance-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rsa-insurance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rsa-insurance-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rsa-insurance-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rsa
- group: other
  title: ''
  type: X
  url: https://x.com/rsagroup
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/rsainsurance
created: '2026-07-25'
description: 'RSA Insurance is a British property and casualty insurer whose lineage runs back to the Sun Fire Office of 1710, making it one of the oldest general insurance brands in the United Kingdom. It writes commercial lines through intermediaries — property, liability, motor fleet, marine, construction, engineering and renewable energy, cyber, professional and financial lines, rail, and accident and health — alongside a residual personal lines book. RSA Insurance Group was acquired by Intact Financial Corporation in 2021, and on 6 October 2025 RSA and NIG formally rebranded to Intact Insurance across the UK, Ireland and Europe; rsainsurance.co.uk now survives as a legacy broker-tools site while corporate, investor, careers and news content has moved to intactinsurance.co.uk. RSA has no public developer portal and publishes no self-serve API. developer., developers., docs. and api. subdomains do not serve (wildcard DNS resolves but no TLS service answers), and /developers, /api, /developer,
  /partners, /integrations and /brokers all return HTTP 404. Every integration surface is broker-gated behind a user ID and password issued to registered intermediaries: RSA Connect (the "Connect Intermediary Website"), RSA Online for intermediated personal home and commercial trading, RSA Claims Online, an eFNOL commercial property claims form, the MID2 Motor Insurance Database portal, and the RSAred risk management customer portal. Machine-to-machine trading reaches RSA the way it reaches most UK carriers — through broker software houses (Acturis, Applied, Open GI, SSP, Bravo Digital Trader) and the Polaris imarket commercial e-trading hub, which lists Intact among its participating insurers and runs on Polaris Standards rather than an openly documented carrier API. No ACORD, AL3, ACORD XML, NGDS or IVANS reference appears anywhere on RSA''s public site, and no Lloyd''s PPL, Whitespace or Blueprint Two participation was found. This is a partner-gated carrier with no public API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: RSA Insurance
nav: Providers
network: true
overview: 'RSA Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Property and Casualty, Commercial Lines, and Carrier.


  RSA Insurance''s developer surface includes documentation, developer portal, support, engineering blog, authentication, YouTube channel, and 16 more developer resources.'
random_paper: 147
score:
  band: emerging
  composite: 25.2
  delta: 0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Rsa Insurance Authentication
  slug: rsa-insurance-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Rsa Insurance Domain Security
  slug: rsa-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rsa-insurance
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Commercial Lines
- Carrier
- Broker
- Claims
- Underwriting
- Partner Gated
website: https://www.rsainsurance.co.uk/
---
