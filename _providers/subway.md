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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/subway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.subway.com/
- group: company
  title: ''
  type: About
  url: https://www.subway.com/en-us/aboutus/ourstory
- group: company
  title: ''
  type: Newsroom
  url: https://www.subway.com/en-us/aboutus/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.subway.com/en-us/contactus/careers
- group: company
  title: Franchise Opportunities
  type: Partners
  url: https://www.mysubwaycareer.com/
- group: start
  title: Subway MyWay / MVP Rewards
  type: Signup
  url: https://www.subway.com/en-us/MyWayRewards/HowItWorks
- group: operate
  title: Subway App FAQs
  type: FAQ
  url: https://media.subway.com/sites/en-us/app/faqs/appfaqs.html
- group: commercial
  title: MyWay Rewards Terms of Use
  type: TermsOfService
  url: https://www.subway.com/en-us/legal/mywayrewardstermsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.subway.com/en-us/privacy/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/SUBWAY
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/subway
created: '2026-05-05'
description: One of the world's largest fast-food restaurant chains specializing in submarine sandwiches and salads. Operates over 36,000 locations in more than 100 countries through its franchise model. Subway has no public developer API or self-service developer portal; ordering, store locator, nutrition, and MyWay/MVP loyalty integrations are handled through internal systems and direct franchise/partner agreements.
features:
- description: Customers place pickup and delivery orders through subway.com and the Subway mobile app; no public ordering API is exposed to third-party developers.
  name: Online & Mobile Ordering
- description: Web and app store locator surfaces location, hours, and amenities for 36,000+ franchised restaurants worldwide. Location data is not available via a documented public API.
  name: Store Locator
- description: Nutritional and menu information is published on subway.com for consumers; there is no public menu/nutrition data API.
  name: Nutrition & Menu Information
- description: Consumer loyalty program (rebranded MVP Rewards) earning tokens and discount coupon rewards, managed through Subway-owned systems.
  name: MyWay / MVP Rewards Loyalty
- description: Stored-value Subway Card and digital gift card program governed by Subway card terms of use.
  name: Gift & Subway Cards
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subway.png
integrations:
- description: Delivery is offered through third-party marketplaces (e.g., DoorDash, Uber Eats, Grubhub) via direct commercial partnerships rather than a Subway public API.
  name: Third-Party Delivery
- description: In-app and online payments are processed through integrated payment providers within Subway's first-party systems.
  name: Payment Processing
layout: provider
modified: '2026-06-03'
name: Subway
nav: Providers
network: true
overview: 'Subway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fast Food, Restaurant, Food and Beverage, Quick Service Restaurant, and Loyalty.


  Subway''s developer surface includes signup flow, FAQ, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/subway/refs/heads/main/screenshots/subway-2026-06-20T194635.png
security:
- kind: domain-security
  name: Subway Domain Security
  slug: subway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: subway
tags:
- Fast Food
- Restaurant
- Food and Beverage
- Quick Service Restaurant
- Loyalty
use_cases:
- description: End users order food for pickup or delivery via Subway's first-party web and mobile experiences.
  name: Consumer Ordering
- description: Members accrue and redeem rewards through the MyWay/MVP Rewards program.
  name: Loyalty Engagement
- description: Franchisees access operational and point-of-sale systems through internal Subway platforms, not public APIs.
  name: Franchise Operations
website: https://www.subway.com/
---
