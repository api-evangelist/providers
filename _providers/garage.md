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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/garage-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/garage-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.shopgarage.com/
- group: company
  title: ''
  type: Blog
  url: https://www.shopgarage.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.withgarage.com/
- group: operate
  title: ''
  type: Support
  url: https://www.shopgarage.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.shopgarage.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shopgarage.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopgarage.com/policies/privacy-policy
created: '2026-07-17'
description: Garage (Garage Technologies, Inc.) is America's online marketplace for buying and selling specialized vehicles and equipment — fire trucks, ambulances, and heavy-duty municipal apparatus. The platform helps fire departments, EMS services, municipalities, and dealers list surplus equipment and buy what they need in seconds, bundling AI-powered appraisals, virtual inspections, live auctions, payments, freight, financing, and warranties into one consumer marketplace. Garage raised $13.5M and is backed by Initialized Capital. It operates a public consumer web marketplace (shopgarage.com / withgarage.com); no public developer API program was found during enrichment.
image: https://www.shopgarage.com/og-homepage.jpg
layout: provider
modified: '2026-07-19'
name: Garage
nav: Providers
network: true
overview: 'Garage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Emergency Vehicles, and Fire Trucks.


  Garage''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/garage/refs/heads/main/screenshots/garage-2026-07-25T215447.png
security:
- kind: domain-security
  name: Garage Domain Security
  slug: garage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: garage
tags:
- Company
- Consumer
- Marketplace
- Emergency Vehicles
- Fire Trucks
- Ambulances
- Municipal Equipment
- Government Surplus
website: https://www.shopgarage.com/
---
