---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The eGifter API is a powerful tool that allows developers to integrate digital gifting capabilities into their applications and websites. With this API, users can easily send personalized gift cards f
  name: eGifter API
  slug: egifter
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/egifter-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eGifter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/egifter
- group: company
  title: ''
  type: Blog
  url: https://corporate.egifter.com/powered-by-egifter/
- group: operate
  title: ''
  type: FAQ
  url: https://support.egifter.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.egifter.com/privacy/
created: '2025-02-08'
description: eGifter is a digital gift card platform that allows people to easily send and receive gift cards for a wide variety of retailers and brands. Users can choose from hundreds of options including popular stores, restaurants, and entertainment venues. Whether it's for a birthday, holiday, or just to show appreciation, eGifter makes it simple to find the perfect gift for any occasion.
finops:
- name: Egifter Finops
  service_category: API
  slug: egifter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/egifter.png
layout: provider
modified: '2026-07-25'
name: eGifter
nav: Providers
network: true
overview: 'eGifter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gift Cards.


  eGifter''s developer surface includes engineering blog, FAQ, and 4 more developer resources.'
plans:
- name: Egifter Plans Pricing
  plan_count: 3
  slug: egifter-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Egifter Rate Limits
  slug: egifter-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/egifter/refs/heads/main/screenshots/egifter-2026-07-25T212954.png
security:
- kind: domain-security
  name: Egifter Domain Security
  slug: egifter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: egifter
tags:
- Gift Cards
---
