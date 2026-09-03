---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resortpass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.resortpass.com/
- group: company
  title: ''
  type: Blog
  url: https://www.resortpass.com/blog
- group: operate
  title: ''
  type: Support
  url: https://kb.resortpass.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.resortpass.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.resortpass.com/privacy-policy
created: '2026-07-17'
description: ResortPass is a consumer travel and hospitality marketplace that lets people book hotel and resort day passes — pool access, spa treatments, cabanas, fitness centers, and day rooms — at over 2,000 hotels without an overnight stay, starting around $25. Guests search by city and date, book a pass, and enjoy resort amenities for the day, while partner hotels monetize otherwise-idle amenity capacity. Surfaced as a portfolio company of CRV and added to the API Evangelist network. No public developer API, API documentation, or developer portal was found during enrichment; the company operates a consumer web/mobile booking product and a hotel partner program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resortpass.png
layout: provider
modified: '2026-07-20'
name: ResortPass
nav: Providers
network: true
overview: 'ResortPass is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Travel, Hospitality, and Hotels.


  ResortPass'' developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resortpass/refs/heads/main/screenshots/resortpass-2026-09-02T153551.png
security:
- kind: domain-security
  name: Resortpass Domain Security
  slug: resortpass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resortpass
tags:
- Company
- Consumer
- Travel
- Hospitality
- Hotels
- Booking
- Marketplace
- Leisure
website: https://www.resortpass.com/
---
