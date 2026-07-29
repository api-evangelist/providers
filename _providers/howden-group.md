---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.howdengroup.com/uk-en
- group: company
  title: ''
  type: About
  url: https://www.howdengroup.com/uk-en/about-us
- group: start
  title: ''
  type: Portal
  url: https://parentportal.howdengroup.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/howden-broking-insurance
- group: company
  title: ''
  type: Blog
  url: https://www.howdengroup.com/uk-en/news-insights
- group: operate
  title: ''
  type: Support
  url: https://www.howdengroup.com/uk-en/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.howdengroup.com/howden-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.howdengroup.com/howden-privacy-data-protection-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.howdengroup.com/cookie-policy
- group: other
  title: ''
  type: Complaints
  url: https://www.howdengroup.com/complaints-procedure
- group: company
  title: ''
  type: Careers
  url: https://www.howdengroup.com/uk-en/careers
- group: auth
  title: ''
  type: Security
  url: https://www.howdengroup.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/howden-group-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/howden-group-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/howden-group-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/howden-group-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/howden-group-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/howden-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/howden-group-domain-security.yml
created: '2026-07-25'
description: 'Howden Group Holdings is a London-headquartered, employee-owned international insurance intermediary founded in 1994, operating across retail insurance broking (Howden), specialty and reinsurance broking (Howden Re / Howden Specialty), and managing general agency underwriting (DUAL). Its home market is the United Kingdom and the Lloyd''s of London subscription market, with lines of business spanning property and casualty, specialty, credit and political risk, marine, cyber, employee benefits, and reinsurance. Howden''s API posture is partner-gated and honestly recorded as such: no developer subdomain resolves (developer/developers/docs/api.howdengroup.com all fail DNS) and no /developers, /api or /partners path exists on howdengroup.com. What Howden does operate is real but private broker-to-carrier integration — HowdenCAP''s Tepfin X structured credit placement application holds direct bilateral APIs with insurers (Allianz Trade, AXA XL, Mosaic), and in July 2025 Howden went
  live with ACORD GRLC digital accounting and invoicing standards over ACORD Solutions Group''s ADEPT gateway with retail insurer partner Hiscox. None of that surface is self-serve, documented publicly, or accompanied by a downloadable OpenAPI definition. The only public web surfaces are marketing pages and login walls. Howden does publish two real machine-readable web artifacts — an RFC 9116 security.txt at www.howdengroup.com naming security@howdengrp.com, and an llms.txt overview blurb mirrored across the Howden Re and DUAL brands — plus a robots.txt Content-Signal directive permitting AI training, search and AI input use of its public content.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Howden Group
nav: Providers
network: true
overview: 'Howden Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Broker, Insurance Broking, and Reinsurance.


  Howden Group''s developer surface includes developer portal, engineering blog, support, and 16 more developer resources.'
random_paper: 32
score:
  band: emerging
  composite: 20.1
  delta: -1.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 21.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/howden-group/refs/heads/main/screenshots/howden-group-2026-07-25T221536.png
security:
- kind: domain-security
  name: Howden Group Domain Security
  slug: howden-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Howden Group Vulnerability Disclosure
  slug: howden-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: howden-group
tags:
- Insurance
- United Kingdom
- Broker
- Insurance Broking
- Reinsurance
- Specialty Insurance
- Managing General Agent
- Employee Benefits
- Credit Insurance
- London Market
- ACORD
- Partner Gated
website: https://www.howdengroup.com/uk-en
---
