---
access_model:
  confidence: high
  label: No public API · Accredited travel agents only
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - agency-hub
  - travel-agent-main-agreement
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virgin-australia-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virgin-australia-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virgin-australia-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.virginaustralia.com/
- group: company
  title: ''
  type: About
  url: https://www.virginaustralia.com/au/en/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.virginaustralia.com/au/en/newsroom/
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.virginaustralia.com/au/en/travel-info/flying-with-us/agency-hub/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virginaustralia.com/au/en/travel-info/flying-with-us/agency-hub/travel-agent-main-agreement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virginaustralia.com/au/en/about-us/policies/legal/terms-of-use/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virginaustralia.com/au/en/about-us/policies/legal/terms-of-use/chatgpt-app/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.virginaustralia.com/au/en/about-us/policies/privacy/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.virginaustralia.com/au/en/about-us/policies/legal/conditions-of-carriage/
- group: start
  title: ''
  type: Onboarding
  url: https://www.virginaustralia.com/au/en/travel-info/flying-with-us/agency-hub/bsp-ticketing-authority-application/
- group: start
  title: ''
  type: Onboarding
  url: https://www.virginaustralia.com/au/en/travel-info/flying-with-us/agency-hub/application-for-virgin-australia-plating-authority-for-arc-agent/
- group: docs
  title: ''
  type: Documentation
  url: https://www.virginaustralia.com/au/en/fly-for-business/business-flyer/travel-trade/agent-faqs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.virginaustralia.com/au/en/travel-info/flying-with-us/agency-hub/policies-and-guides/
- group: start
  title: ''
  type: Login
  url: https://www.virginaustralia.com/au/en/travel-info/flying-with-us/agency-hub/agents-corporate-log-in/
- group: operate
  title: ''
  type: Support
  url: https://www.virginaustralia.com/au/en/help/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.virginaustralia.com/au/en/help/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virgin-australia
created: '2026-07-28'
description: 'Virgin Australia (IATA code VA, ASX:VGN) is Australia''s second-largest airline group, founded in 2000 and headquartered in Brisbane, operating a domestic and short-haul international network alongside charter and cargo services with more than 8,000 team members and the 13-million-member Velocity Frequent Flyer loyalty program. It sits on the airline side of a concentrated Australian duopoly with Qantas, and reaches travel agents and travel management companies almost entirely through GDS intermediation — Amadeus, Sabre and Travelport/Galileo — rather than through any direct machine interface of its own. Virgin Australia selected Sabre as its preferred NDC IT technology provider in October 2023 and renewed a multi-year Amadeus distribution agreement covering EDIFACT today and NDC in future, but as of July 2026 no Virgin Australia NDC endpoint, developer portal or API documentation is published anywhere on virginaustralia.com. Its API posture is honestly stated as none-published:
  developer.virginaustralia.com, developers., api., apis. and docs. subdomains do not resolve; /developers, /api, /api-docs, /openapi.json and /swagger.json all return 404; and the only partner surface is the Agency Hub, whose Travel Agent Main Agreement requires current IATA or ATIS accreditation, GDS access for BSP sales, and Virgin Australia''s absolute discretion to approve an account. The one genuinely public programmatic-adjacent surface is the Virgin Australia app in ChatGPT, launched 10 June 2026 for flight and Velocity Reward Seat search only — it cannot book, amend, cancel or take payment, and its underlying interface is not documented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Virgin Australia
nav: Providers
network: true
overview: 'Virgin Australia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Aviation, Airline, and Distribution.


  Virgin Australia''s developer surface includes engineering blog, privacy policy, legal docs, documentation, support, and 15 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 11.7
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virgin-australia/refs/heads/main/screenshots/virgin-australia-2026-09-02T170002.png
security:
- kind: domain-security
  name: Virgin Australia Domain Security
  slug: virgin-australia-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: virgin-australia
tags:
- Travel
- Australia
- Aviation
- Airline
- Distribution
- GDS
- NDC
- Booking
- Loyalty
- Corporate Travel
website: https://www.virginaustralia.com/
---
