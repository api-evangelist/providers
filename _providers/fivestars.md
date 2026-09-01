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
    agentic_commerce: false
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sumup/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fivestars-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fivestars.com
- group: build
  title: ''
  type: Packages
  url: packages/fivestars-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fivestars-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fivestars-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fivestars.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fivestars-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/fivestars-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fivestars-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://help.fivestars.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fivestars
- group: start
  title: ''
  type: Login
  url: https://dashboard.fivestars.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fsweb.fivestars.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fsweb.fivestars.com/privacy/
coverage:
  checked: '2026-08-13'
  detail: Fivestars was fully absorbed into SumUp — fivestars.com 301s to sumup.com/en-us/loyalty-program/, api.fivestars.com resolves through SumUp's edge but 404s on every spec and .well-known path, developers.fivestars.com and docs.fivestars.com do not resolve, and the Wayback Machine holds no capture of a Fivestars developer portal at any point.
  evidence:
  - status: 301
    url: https://fivestars.com/
  - status: 404
    url: https://api.fivestars.com/openapi.json
  - status: 404
    url: https://www.fivestars.com/developers
  - status: 200
    url: https://status.fivestars.com/api/v2/summary.json
  reason: defunct
  state: none
created: '2026-07-17'
description: Fivestars was a customer loyalty, rewards, and payments platform for small and mid-sized brick-and-mortar merchants, founded in 2010 and headquartered in San Francisco. It combined an automated marketing engine, a customer loyalty and rewards program, and integrated card payments so local businesses could turn one-time shoppers into repeat customers. Fivestars was backed by Lightspeed Venture Partners, Menlo Ventures, and Y Combinator. The company was acquired by SumUp in 2021 and its product has since been folded into SumUp Connect (SumUp Loyalty); fivestars.com now redirects to SumUp's loyalty program. Fivestars publishes no public API, no developer portal and no machine-readable contract — api.fivestars.com resolves but returns 404 on every spec and well-known path, and developers.fivestars.com does not resolve. Fivestars-branded surfaces that remain live include the marketing site, merchant dashboard, help center and a public status page, plus one first-party iOS library
  (TapiSDK) for legacy cPay terminal integrators. This profile is retained in the API Evangelist network as a historical company record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fivestars.png
layout: provider
modified: '2026-08-13'
name: Fivestars
nav: Providers
network: true
overview: 'Fivestars is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loyalty, Rewards, Payments, and Point-of-Sale.


  Fivestars'' developer surface includes support and 14 more developer resources.'
plans:
- name: Fivestars Plans Pricing
  plan_count: 0
  slug: fivestars-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Fivestars Rate Limits
  slug: fivestars-rate-limits
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fivestars/refs/heads/main/screenshots/fivestars-2026-07-25T214648.png
security:
- kind: domain-security
  name: Fivestars Domain Security
  slug: fivestars-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fivestars
tags:
- Company
- Loyalty
- Rewards
- Payments
- Point-of-Sale
- Customer Engagement
- Marketing
- Small Business
website: https://fivestars.com
---
