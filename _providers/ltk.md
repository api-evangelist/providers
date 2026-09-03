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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: LTK's partner/affiliate API served from the rewardStyle Developer Portal, secured with OAuth2 (client-credentials token endpoint at /oauth/token). The full API reference and specification are gated be
  name: rewardStyle Developer Portal
  slug: rewardstyle-developer-portal
artifact_total: 6
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rewardStyle
- group: company
  title: ''
  type: Blog
  url: https://company.shopltk.com/us/creatorsuccess/creator-blog
- group: build
  title: ''
  type: Packages
  url: packages/ltk-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ltk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ltk-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ltk-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ltk-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: The rewardStyle Developer Portal at api.rewardstyle.com answers HTTP 200 with a sign-in form for every documentation path (/docs, /documentation, /openapi, /swagger, /api/v1), so the API reference and specification are only visible after partner registration; the OAuth2 token endpoint is the only part of the API that can be verified anonymously.
  evidence:
  - status: 200
    url: https://api.rewardstyle.com/docs
  - status: 400
    url: https://api.rewardstyle.com/oauth/token
  - status: 404
    url: https://api.rewardstyle.com/.well-known/openid-configuration
  - status: 404
    url: https://github.com/rewardStyle/api.rewardstyle.com
  reason: partner-login
  state: gated
created: '2026-07-17'
description: LTK (formerly rewardStyle / LIKEtoKNOW.it) is a creator commerce platform that connects shoppers, content creators, and brands, driving more than $6B in annual sales. Founded in 2011 by Amber and Baxter Box and headquartered in Dallas, LTK operates a shoppable-content network spanning 44M+ monthly shoppers, 1M+ brands, and 8,000+ integrated retailers, and has generated nearly 1,100 creator millionaires. For brand and affiliate partners, LTK exposes a partner API through the rewardStyle Developer Portal at api.rewardstyle.com, secured with OAuth2 and gated behind partner registration. This profile enriches the LTK company record with its verifiable public developer, security, and identity surface.
image: https://company.shopltk.com/hubfs/LinkedInLTKlogo1-1.jpg
layout: provider
modified: '2026-08-13'
name: LTK
nav: Providers
network: true
overview: 'LTK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Creator Commerce, Affiliates, and E-Commerce.


  LTK''s developer surface includes signup flow, support, authentication, engineering blog, and 16 more developer resources.'
plans:
- name: Ltk Plans Pricing
  plan_count: 0
  slug: ltk-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Ltk Rate Limits
  slug: ltk-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 23.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Affiliates
- E-Commerce
- Influencer Marketing
- Retail
- Shopping
website: https://company.shopltk.com/
---
