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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.bloomon.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.bloomon.co.uk/blog
- group: operate
  title: ''
  type: Support
  url: https://www.bloomon.co.uk/help/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bloomon.co.uk/help/
- group: start
  title: ''
  type: SignUp
  url: https://www.bloomon.co.uk/register
- group: start
  title: ''
  type: Login
  url: https://www.bloomon.co.uk/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomon.co.uk/about-bloomon/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomon.co.uk/about-bloomon/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomon-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloomon-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.bloomon.co.uk/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomon-domain-security.yml
created: '2026-07-17'
description: Bloomon is a flower and gift delivery service that lets customers order one-off bouquets or sign up for a recurring flower subscription delivered on a chosen cadence. It offers seasonal hand-tied and letterbox arrangements, gifting options, gift vouchers, and add-ons, with delivery across the United Kingdom and other European markets. Bloomon is part of the Bloom & Wild Group (confirmed via its published .well-known/security.txt, which points to bloomandwild.com). The company operates a consumer-facing e-commerce and subscription website rather than a public developer API; this API Evangelist profile therefore captures its web, security, and discovery surface rather than a machine-readable API.
image: https://www.bloomon.co.uk/assets/branded-icons/logo.svg
layout: provider
modified: '2026-07-18'
name: Bloomon
nav: Providers
network: true
overview: 'Bloomon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Flowers, Flower Delivery, and Subscription.


  Bloomon''s developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomon/refs/heads/main/screenshots/bloomon-2026-07-25T203414.png
security:
- kind: domain-security
  name: Bloomon Domain Security
  slug: bloomon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomon Vulnerability Disclosure
  slug: bloomon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomon
tags:
- Company
- Consumer
- Flowers
- Flower Delivery
- Subscription
- E-Commerce
- Gifting
- Retail
- Bloom & Wild Group
website: https://www.bloomon.co.uk/
---
