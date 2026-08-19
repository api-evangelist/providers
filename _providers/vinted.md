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
    consent_identity: true
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
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vinted-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.vinted.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vinted-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vinted-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vinted-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vinted-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.vinted.com
- group: operate
  title: ''
  type: Support
  url: https://www.vinted.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vinted.com/terms_and_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vinted.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://company.vinted.com/en/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vinted
created: '2026-07-17'
description: Vinted is a European consumer-to-consumer (C2C) online marketplace for buying and selling secondhand clothes, shoes, accessories, and other lifestyle items, operating across web and mobile apps in dozens of markets. Founded in Vilnius, Lithuania, it is one of Europe's largest secondhand fashion platforms and is backed by Accel, Insight Partners, and Lightspeed Venture Partners. Vinted does not publish a public developer API, SDKs, or a developer portal; this API Evangelist profile captures the company's public identity, legal, and security (security.txt / domain-security) surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vinted.png
layout: provider
modified: '2026-07-21'
name: Vinted
nav: Providers
network: true
overview: 'Vinted is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Ecommerce, and Secondhand.


  Vinted''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 12.4
  delta: -0.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Vinted Domain Security
  slug: vinted-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vinted Vulnerability Disclosure
  slug: vinted-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vinted
tags:
- Company
- Consumer
- Marketplace
- Ecommerce
- Secondhand
- Fashion
- C2C
- Europe
website: https://www.vinted.com
---
