---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rover.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rover-com
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.rover.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.rover.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/roverdotcom
- group: commercial
  title: ''
  type: Plans
  url: plans/rover-plans-pricing.yml
created: '2026-07-03'
description: 'Rover is the world''s largest online marketplace for pet care, connecting pet parents with sitters and dog walkers for boarding, house sitting, drop-in visits, doggy daycare, and dog walking. Founded in 2011 and headquartered in Seattle, Rover was a publicly traded company (Nasdaq: ROVR) until Blackstone completed its acquisition of Rover Group for approximately $2.3 billion on February 27, 2024, taking the company private and delisting its stock. As of this catalog entry, Rover does NOT publish a public, documented developer API or a developer portal. Its platform is a closed consumer/provider marketplace; the only outward-facing integration program is a marketing affiliate program offered through third-party affiliate networks (Impact, CJ, Rakuten, Skimlinks, ShareASale, etc.), not a data/booking API. Programmatic access to Rover data today is only available via unofficial third-party web scrapers (e.g. Apify), which are outside Rover''s supported surface. This entry is an
  honest stub documenting the absence of a public API; it should be revisited if Rover launches a partner or developer API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rover.png
layout: provider
modified: '2026-07-03'
name: Rover
nav: Providers
network: true
overview: 'Rover is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Care, Dog Walking, Pet Sitting, Marketplace, and Consumer.


  Rover''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Rover Plans Pricing
  plan_count: 5
  slug: rover-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rover/refs/heads/main/screenshots/rover-2026-09-02T154140.png
security:
- kind: domain-security
  name: Rover Domain Security
  slug: rover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rover
tags:
- Pet Care
- Dog Walking
- Pet Sitting
- Marketplace
- Consumer
- No Public API
- Stub
website: https://www.rover.com
---
