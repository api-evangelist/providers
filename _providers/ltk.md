---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 15.3
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: LTK's partner/affiliate API served from the rewardStyle Developer Portal, secured with OAuth2 (client-credentials token endpoint at /oauth/token). The full API reference and specification are gated be
  name: rewardStyle Developer Portal
  slug: rewardstyle-developer-portal
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ltk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://company.shopltk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.rewardstyle.com/
- group: start
  title: ''
  type: SignUp
  url: https://api.rewardstyle.com/register
- group: operate
  title: ''
  type: Support
  url: https://company.shopltk.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://company.shopltk.com/ltk-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://company.shopltk.com/ltk-privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/ltk-authentication.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ltk-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ltk-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ltk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://shopltk.com/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ltk-llms.txt
created: '2026-07-17'
description: LTK (formerly rewardStyle / LIKEtoKNOW.it) is a creator commerce platform that connects shoppers, content creators, and brands, driving more than $6B in annual sales. Founded in 2011 by Amber and Baxter Box and headquartered in Dallas, LTK operates a shoppable-content network spanning 44M+ monthly shoppers, 1M+ brands, and 8,000+ integrated retailers, and has generated nearly 1,100 creator millionaires. For brand and affiliate partners, LTK exposes a partner API through the rewardStyle Developer Portal at api.rewardstyle.com, secured with OAuth2 and gated behind partner registration. This profile enriches the LTK company record with its verifiable public developer, security, and identity surface.
image: https://company.shopltk.com/
layout: provider
modified: '2026-07-20'
name: LTK
nav: Providers
network: true
overview: 'LTK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Creator Commerce, Affiliate, and E-Commerce.


  LTK''s developer surface includes signup flow, support, authentication, and 10 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ltk/refs/heads/main/screenshots/ltk-2026-07-25T225629.png
security:
- kind: authentication
  name: Ltk Authentication
  slug: ltk-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ltk Domain Security
  slug: ltk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ltk Vulnerability Disclosure
  slug: ltk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ltk
tags:
- Company
- Consumer
- Creator Commerce
- Affiliate
- E-Commerce
- Influencer Marketing
- Retail
- Shopping
website: https://company.shopltk.com/
---
