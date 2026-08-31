---
access_model:
  confidence: high
  label: Enterprise / contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://zefr.com/pricing
  - https://zefr.com/request-a-demo
  - https://suitability.zefr.com/
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zefr-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zefr-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zefr-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/zefr-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/zefr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zefr-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zefr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zefr-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/zefr-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zefr-llms.txt
- group: company
  title: ''
  type: Website
  url: https://zefr.com
- group: start
  title: ''
  type: Login
  url: https://suitability.zefr.com/
- group: operate
  title: ''
  type: Support
  url: https://zefr.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://zefr.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZEFR-INC
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zefr.com/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zefr.com/privacy-policy
- group: auth
  title: ''
  type: Trust
  url: https://trust.zefr.com/
coverage:
  checked: '2026-08-12'
  detail: Zefr runs live API infrastructure — api.zefr.com is a Google Apigee gateway that answers every anonymous request with a proprietary ApplicationNotFound fault — but publishes no developer portal, no API reference and no machine-readable contract; developer.zefr.com and docs.zefr.com do not resolve, the /support page renders the placeholder "Waiting on Content Entry...", and the only route to the platform is the "Request a Demo" form.
  evidence:
  - status: 404
    url: https://api.zefr.com/openapi.json
  - status: 0
    url: https://developer.zefr.com/
  - status: 0
    url: https://docs.zefr.com/
  - status: 200
    url: https://zefr.com/support
  - status: 404
    url: https://zefr.com/pricing
  - status: 200
    url: https://login.zefr.com/.well-known/openid-configuration
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'Zefr is an ad-tech content intelligence company that classifies social video, image, audio and text so advertisers can buy and measure media against brand safety and suitability standards. Its classification engine labels content across YouTube, Meta (Facebook and Instagram), TikTok, Snapchat, Google Ads and DV360 against the 4A''s and GARM frameworks, and its Brand Suitability Suite gives brands pre-bid controls and post-bid measurement from a single console. Zefr has no public developer program: production API infrastructure exists (api.zefr.com is a Google Apigee gateway, alongside api2.zefr.com and api-eu1.zefr.com) but no developer portal, API reference or machine-readable contract is published anywhere, and access runs through a demo request. The only machine-readable documents Zefr serves publicly are the OpenID Connect and OAuth 2.0 Authorization Server Metadata discovery documents on its Auth0 custom domain, login.zefr.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zefr.png
layout: provider
modified: '2026-08-12'
name: Zefr
nav: Providers
network: true
overview: 'Zefr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Adtech, Brand Safety, Brand Suitability, and Content Intelligence.


  Zefr''s developer surface includes authentication, support, engineering blog, and 15 more developer resources.'
plans:
- name: Zefr Plans Pricing
  plan_count: 0
  slug: zefr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Zefr Rate Limits
  slug: zefr-rate-limits
scopes:
- name: Zefr Scopes
  scope_count: 0
  slug: zefr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.4
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Zefr Authentication
  slug: zefr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zefr Domain Security
  slug: zefr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Zefr Trust Center
  slug: zefr-trust-center
  summary_line: read, published, note
slug: zefr
tags:
- Company
- Adtech
- Brand Safety
- Brand Suitability
- Content Intelligence
- Content Moderation
- Video
- Social-Media
- Advertising
- Media Measurement
- Machine-Learning
website: https://zefr.com
---
