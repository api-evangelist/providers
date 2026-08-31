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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: OAuth 2.0 / OpenID Connect storefront surface for the SAIB & Co. mall on the Cafe24 Unified Commerce Platform (UCP). Advertised via the mall's live OpenID Connect discovery document; supports authoriz
  name: SAIB & Co. Cafe24 Storefront API
  slug: saib-co-cafe24-storefront-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://saibnco.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saibnco.com/member/agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saibnco.com/member/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://saibnco.com/board/faq2.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/saib-and-co-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saib-and-co-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/saib-and-co-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saib-and-co-domain-security.yml
created: '2026-07-17'
description: SAIB (Save & Co.) is a Seoul-based Korean intimate cosmetics and wellness brand focused on female empowerment, offering premium condoms and solid feminine cleansing products made with proprietary, health-conscious ingredients such as CranProB. The brand donates 10% of sales revenue to campaigns supporting gender equality and women's rights. SAIB sells direct-to-consumer through a Cafe24-hosted storefront (saibnco.com); its only programmatic surface is the Cafe24 Unified Commerce Platform (UCP) storefront, which exposes an OpenID Connect discovery document and an OAuth 2.0 / OIDC storefront API for this mall. Surfaced as a portfolio company of 500 Global and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saib-and-co.png
layout: provider
modified: '2026-07-21'
name: SAIB & Co.
nav: Providers
network: true
overview: 'SAIB & Co. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cosmetics, Consumer Goods, E-Commerce, and Wellness.


  SAIB & Co.''s developer surface includes support, authentication, and 6 more developer resources.'
random_paper: 14
scopes:
- name: Saib And Co Scopes
  scope_count: 6
  slug: saib-and-co-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Saib And Co Authentication
  slug: saib-and-co-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Saib And Co Domain Security
  slug: saib-and-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: saib-and-co
tags:
- Company
- Cosmetics
- Consumer Goods
- E-Commerce
- Wellness
- Retail
- Cafe24
- Authentication
website: https://saibnco.com
---
