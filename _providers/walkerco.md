---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://walkerandcompany.com'', ''status'': 301, ''note'': ''declared website redirects to https://getbevel.com/ — a different registrable domain (walkerandcompany.com -> getbevel.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/procter-and-gamble/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/walkerco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.pg.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walkerco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://walkerandcompany.com
- group: company
  title: ''
  type: Website
  url: https://getbevel.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getbevel.com
- group: start
  title: ''
  type: Login
  url: https://getbevel.com/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WalkerAndCoBrandsInc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getbevel.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getbevel.com/policies/terms-of-service
- group: agent
  title: ''
  type: WellKnown
  url: well-known/walkerco-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/walkerco-security.txt
created: '2026-07-17'
description: Walker & Company Brands (WalkerCo) is a health and beauty company founded by Tristan Walker that designs grooming and personal-care products for people of color. Its flagship brand, Bevel, sells shaving systems, razors, skin, hair, and beard-care products direct-to-consumer, and the company also operates the FORM hair-care line. Walker & Company was acquired by Procter & Gamble in 2018 and its storefronts run on Shopify. The company does not publish a public developer API or developer portal; its programmatic surface is limited to the Shopify-provided Customer Account OAuth/OIDC endpoints on the Bevel storefront and an internal-tooling GitHub organization. This profile was surfaced as a 500 Global portfolio company and enriched from public web sources.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walkerco.png
layout: provider
modified: '2026-07-21'
name: WalkerCo
nav: Providers
network: true
overview: WalkerCo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health and Beauty, Consumer Products, E-Commerce, and Grooming.
random_paper: 16
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walkerco/refs/heads/main/screenshots/walkerco-2026-09-02T170407.png
security:
- kind: domain-security
  name: Walkerco Domain Security
  slug: walkerco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Walkerco Vulnerability Disclosure
  slug: walkerco-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: walkerco
tags:
- Company
- Health and Beauty
- Consumer Products
- E-Commerce
- Grooming
- Personal Care
- Shopify
- Direct to Consumer
website: https://walkerandcompany.com
---
