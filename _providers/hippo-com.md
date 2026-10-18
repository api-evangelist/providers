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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Direct-to-consumer homeowners quote, bind, and policy management. Quotes delivered in under 60 seconds. No public API; carrier partnerships are managed via First Connect.
  name: Hippo Consumer Quote & Bind
  provenance: unpublished
  slug: hippo-consumer
- description: Hippo Home is the consumer smart-home companion app for iOS and Android. Provides DIY maintenance checklists, seasonal guidance, and a home health score. No public API; integrations are sales-led.
  name: Hippo Home App
  provenance: unpublished
  slug: hippo-home
- description: First Connect, a Hippo subsidiary, is an API-first digital platform giving independent agents one-stop access to 100+ home, auto, cyber, small business, life, and specialty carriers and MGAs. The port
  name: First Connect (Independent Agent Platform)
  slug: first-connect
- description: Spinnaker is Hippo's affiliated specialty admitted carrier providing paper for MGAs and program administrators. Integrations are sales-led.
  name: Spinnaker Insurance (MGA Carrier Paper)
  slug: spinnaker
artifact_total: 9
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.hippo.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hippo-com/refs/heads/main/security/hippo-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hippo-com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hippo-com/refs/heads/main/security/hippo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hippo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hippo.com
- group: other
  title: ''
  type: Quote
  url: https://www.hippo.com
- group: other
  title: ''
  type: Claims
  url: https://www.hippo.com/claim
- group: other
  title: ''
  type: Account
  url: https://myhippo.com/account
- group: other
  title: ''
  type: Agents
  url: https://www.hippo.com/agents
- group: learn
  title: ''
  type: LearnCenter
  url: https://www.hippo.com/learn-center
- group: company
  title: ''
  type: Blog
  url: https://www.hippo.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://faq.hippo.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://www.hippo.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.hippo.com/careers
- group: commercial
  title: ''
  type: Legal
  url: https://www.hippo.com/legal-information
- group: auth
  title: ''
  type: Security
  url: https://trust.hippo.com
- group: company
  title: ''
  type: Investors
  url: https://investors.hippoholdings.com
- group: other
  title: ''
  type: Spinnaker
  url: https://www.spinnakerins.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hippoinsurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hippo-insurance
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HippoInsurance
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/HippoInsurance
- group: other
  title: ''
  type: Homeowners
  url: https://www.hippo.com/homeowners-insurance
- group: other
  title: ''
  type: Auto
  url: https://www.hippo.com/auto-insurance
- group: other
  title: ''
  type: Flood
  url: https://www.hippo.com/flood-insurance
- group: other
  title: ''
  type: Pet
  url: https://www.hippo.com/pet-insurance
- group: other
  title: ''
  type: Landlord
  url: https://www.hippo.com/landlord-insurance
- group: other
  title: ''
  type: HippoHomeApp
  url: https://www.hippo.com/hippo-home-app
- group: company
  title: ''
  type: About
  url: https://www.hippo.com/about-us
- group: other
  title: ''
  type: FirstConnect
  url: https://www.firstconnectinsurance.com
- group: company
  title: ''
  type: Newsroom
  url: https://investors.hippo.com/news-releases
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hippo-com/refs/heads/main/plans/hippo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hippo-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hippo-com/refs/heads/main/rate-limits/hippo-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hippo-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hippo-com/refs/heads/main/finops/hippo-com-finops.yml
  title: ''
  type: FinOps
  url: finops/hippo-com-finops.yml
created: '2026-05-25'
description: 'Hippo is a US homeowners insurance carrier headquartered in Palo Alto, California, operating as the insurance subsidiary of Hippo Holdings Inc. (NYSE: HIPO). Founded in 2015, Hippo modernizes home insurance with instant online quotes — typically under sixty seconds — and a smart home oriented approach that pairs policies with proactive home maintenance guidance through the Hippo Home mobile app, DIY checklists, home health scoring, and partnerships with smart device makers. The company writes homeowners, condo, landlord, flood, auto, and pet policies and operates as both a direct-to-consumer brand and an MGA distributing through a network of 70+ carrier partners, including Bamboo, Stillwater, Nationwide, American Integrity, Liberty Mutual, and Progressive. Hippo''s underwriting capacity is anchored by its wholly-owned admitted carrier, Spinnaker Insurance Company, acquired in 2020. Hippo serves 500K+ homeowners across the United States, with concentrated presence in Texas,
  California, Arizona, Colorado, Missouri, Ohio, South Carolina, Tennessee, and Virginia. There is no publicly documented developer API, SDK, or open-source release for Hippo or Spinnaker; the GitHub organization hippoinsurance exists but has no public repositories, and the api.hippo.com hostname is not exposed to the public internet. Integrations with smart home device partners, agents, and MGA carriers are handled through private partner channels rather than an open developer program.'
finops:
- has_sources: false
  method: generated
  name: Hippo Com Finops
  primary_unit: ''
  service_category: API
  slug: hippo-com-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hippo-com.png
layout: provider
modified: '2026-08-08'
name: Hippo
nav: Providers
network: true
overview: 'Hippo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Home Insurance, Smart Home, Insurtech, and Property Insurance.


  Hippo''s developer surface includes engineering blog, FAQ, legal docs, GitHub presence, and 29 more developer resources.'
plans:
- name: Hippo Com Plans Pricing
  plan_count: 1
  slug: hippo-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Hippo Com Rate Limits
  slug: hippo-com-rate-limits
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.7
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 63.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hippo-com/refs/heads/main/screenshots/hippo-com-2026-06-20T182748.png
security:
- kind: domain-security
  name: Hippo Com Domain Security
  slug: hippo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hippo Com Trust Center
  slug: hippo-com-trust-center
  summary_line: SOC 2, CSA STAR
slug: hippo-com
tags:
- Insurance
- Home Insurance
- Smart Home
- Insurtech
- Property Insurance
- Condo Insurance
- Landlord Insurance
- Flood Insurance
- MGA
- Carrier
- Claims
- Underwriting
- Mobile App
- Consumer
- Property and Casualty
website: https://www.hippo.com
---
