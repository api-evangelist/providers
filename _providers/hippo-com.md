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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hippo-com-trust-center.yml
- group: auth
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
created: '2026-05-25'
description: 'Hippo is a US homeowners insurance carrier headquartered in Palo Alto, California, operating as the insurance subsidiary of Hippo Holdings Inc. (NYSE: HIPO). Founded in 2015, Hippo modernizes home insurance with instant online quotes — typically under sixty seconds — and a smart home oriented approach that pairs policies with proactive home maintenance guidance through the Hippo Home mobile app, DIY checklists, home health scoring, and partnerships with smart device makers. The company writes homeowners, condo, landlord, flood, auto, and pet policies and operates as both a direct-to-consumer brand and an MGA distributing through a network of 70+ carrier partners, including Bamboo, Stillwater, Nationwide, American Integrity, Liberty Mutual, and Progressive. Hippo''s underwriting capacity is anchored by its wholly-owned admitted carrier, Spinnaker Insurance Company, acquired in 2020. Hippo serves 500K+ homeowners across the United States, with concentrated presence in Texas,
  California, Arizona, Colorado, Missouri, Ohio, South Carolina, Tennessee, and Virginia. There is no publicly documented developer API, SDK, or open-source release for Hippo or Spinnaker; the GitHub organization hippoinsurance exists but has no public repositories, and the api.hippo.com hostname is not exposed to the public internet. Integrations with smart home device partners, agents, and MGA carriers are handled through private partner channels rather than an open developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hippo-com.png
layout: provider
modified: '2026-08-08'
name: Hippo
nav: Providers
network: true
overview: 'Hippo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Home Insurance, Homeowners Insurance, Smart Home, and Insurtech.


  Hippo''s developer surface includes engineering blog, FAQ, legal docs, GitHub presence, and 25 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.5
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 7.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
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
- Homeowners Insurance
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
website: https://www.hippo.com
---
