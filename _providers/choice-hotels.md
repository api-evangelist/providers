---
access_model:
  confidence: high
  label: No public developer program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/choice-hotels-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.choicehotels.com/
- group: other
  title: ''
  type: CorporateSite
  url: https://www.choicehotelsdevelopment.com/
- group: company
  title: ''
  type: Blog
  url: https://media.choicehotels.com/press-releases
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.choicehotels.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/choice-hotels-international/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Choice_Hotels
- group: start
  title: ''
  type: Login
  url: https://connect.choicehotels.com/
- group: start
  title: ''
  type: Login
  url: https://apps.choicecentral.com/ccweb/content/home.html
- group: company
  title: ''
  type: BlogRSS
  url: https://media.choicehotels.com/press-releases?pagetemplate=rss
- group: operate
  title: ''
  type: Support
  url: https://www.choicehotels.com/help
- group: operate
  title: ''
  type: Support
  url: https://choicehotels.service-now.com/hp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.choicehotels.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.choicehotels.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.choicehotels.com/legal/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/choice-hotels-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/choice-hotels-llms.txt
created: '2026-07-28'
description: 'Choice Hotels International (NYSE: CHH) is a United States hotel franchisor headquartered in North Bethesda, Maryland, operating 7,575 hotels with 656,825 rooms open across 49 states, the District of Columbia and 50 countries and territories as of December 31, 2025. Its brands include Comfort, Quality, Clarion, Sleep Inn, Econo Lodge, Rodeway Inn, MainStay Suites, Suburban Studios, WoodSpring Suites, Everhome Suites, Cambria Hotels, Ascend Hotel Collection and the Radisson Americas brands. Choice sits on the supply side of the travel distribution chain as a franchisor rather than an owner: its proprietary choiceEDGE central reservation system pushes rate, inventory and availability to ChoiceHotels.com, the Choice Privileges mobile apps, the global distribution systems (Sabre, Amadeus), the OTAs (Expedia, Booking.com) and metasearch (Kayak, Tripadvisor), while its proprietary choiceADVANTAGE property management system runs the majority of its franchised properties. API posture
  is honestly none-published — no public developer portal, no published API reference, no machine-readable contract, and no exit path. A TIBCO Mashery API gateway answers at api.choicehotels.com but every probed path returns ERR_596_SERVICE_NOT_FOUND, and developer.choicehotels.com is an unprovisioned Mashery CNAME returning 404 under a mashery.com certificate. All real integration is reached through gated franchisee and vendor channels (connect.choicehotels.com, choicecentral.com, the SkyTouch /CONNECT interface program) that require a commercial agreement.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/choice-hotels.png
layout: provider
modified: '2026-07-28'
name: Choice Hotels
nav: Providers
network: true
overview: 'Choice Hotels is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United States, Hospitality, Hotels, and Booking.


  Choice Hotels'' developer surface includes engineering blog, support, and 15 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.9
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Choice Hotels Domain Security
  slug: choice-hotels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Choice Hotels Vulnerability Disclosure
  slug: choice-hotels-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: choice-hotels
tags:
- Travel
- United States
- Hospitality
- Hotels
- Booking
- Reservations
- Distribution
- Franchising
- Loyalty
website: https://www.choicehotels.com/
---
