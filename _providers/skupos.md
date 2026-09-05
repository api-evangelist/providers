---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.skupos.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.pdiessentials.com/ — a different registrable domain (skupos.com -> pdiessentials.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skupos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skupos.com/
- group: operate
  title: ''
  type: Support
  url: https://help.skupos.com/en/
- group: start
  title: ''
  type: Login
  url: https://go.skupos.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pdiessentials.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pdiessentials.com/skupos-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pdiessentials.com/skupos-privacy/
- group: company
  title: ''
  type: Partners
  url: https://www.pdiessentials.com/partners
- group: operate
  title: ''
  type: Contact
  url: https://www.pdiessentials.com/contact
created: '2026-07-17'
description: Skupos is a retail technology platform for the convenience store industry that connects independent c-store retailers, distributors, and consumer brands through a single data network. Its SaaS platform delivers scan-data automation, back-office and financial management, tobacco scan-data incentives, digital loyalty and funded promotions, and GasBuddy integration. Founded in 2016 and backed by Insight Partners, Skupos was acquired by PDI Technologies in 2023 and now operates as part of the PDI Essentials product suite. Skupos runs an authenticated production API at api.skupos.com but publishes no public API specification, developer portal, or client SDKs.
image: https://www.pdiessentials.com/_astro/logo-essentials.Rgnh57UP_ZhMMfU.webp
layout: provider
modified: '2026-07-21'
name: Skupos
nav: Providers
network: true
overview: 'Skupos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail Technology, Convenience Store, Scan Data, and Loyalty.


  Skupos'' developer surface includes support, pricing, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skupos/refs/heads/main/screenshots/skupos-2026-09-02T155749.png
security:
- kind: domain-security
  name: Skupos Domain Security
  slug: skupos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skupos
tags:
- Company
- Retail Technology
- Convenience Store
- Scan Data
- Loyalty
- Point-of-Sale
- Software-as-a-Service
- Consumer Packaged Goods
website: https://www.skupos.com/
---
