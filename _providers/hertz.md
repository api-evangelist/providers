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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-15'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hertz/refs/heads/main/security/hertz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hertz-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hertz/refs/heads/main/llms/hertz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hertz-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hertz
- group: company
  title: ''
  type: Website
  url: https://www.hertz.com
- group: operate
  title: ''
  type: Support
  url: https://www.hertz.com/supporthub/
- group: company
  title: ''
  type: Blog
  url: https://www.hertz.com/us/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hertz.com/rentacar/navigation/templates/legalView.jsp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hertz.com/rentacar/privacypolicy/index.jsp?targetPage=privacyPolicyView.jsp
coverage:
  checked: '2026-09-13'
  detail: Hertz's own Travel Agent "GDS Tools" page hands integrators quick-reference guides for Amadeus, Galileo by Travelport, SABRE Travel Network and Worldspan instead of publishing an API reference, and the only developer-shaped hostname, developers.hertz.com, is a dangling Akamai CNAME whose certificate does not match the name.
  evidence:
  - status: 200
    url: https://www.hertz.com/rentacar/misc/index.jsp?targetPage=GDSindex_TA.jsp
  - status: 0
    url: https://developers.hertz.com/
  - status: 404
    url: https://api.hertz.com/openapi.json
  - status: 403
    url: https://api.hertz.io/openapi.json
  - status: 404
    url: https://www.hertz.com/.well-known/api-catalog
  reason: marketplace-only
  state: gated
created: '2026-03-21'
description: 'The Hertz Corporation is a global vehicle rental company operating the Hertz, Dollar and Thrifty brands from airport and neighbourhood locations in roughly 160 countries, renting cars, vans and trucks to leisure, corporate, government and rideshare customers and running the Hertz Gold Plus Rewards loyalty programme. Hertz publishes no public developer programme: probing on 2026-09-13 found no developer portal, no OpenAPI or other machine-readable contract, no SDKs, no first-party MCP server and no /.well-known/ discovery documents on any Hertz host. Third-party integrators reach Hertz rates and availability through the global distribution systems — Amadeus, Sabre and Travelport — which Hertz''s own Travel Agent GDS Tools page directs them to, rather than through a first-party API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hertz.png
layout: provider
modified: '2026-09-13'
name: Hertz
nav: Providers
network: true
overview: 'Hertz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Car Rental, Vehicle Rental, Travel, and Mobility.


  Hertz''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hertz Domain Security
  slug: hertz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hertz
tags:
- Fortune 500
- Car Rental
- Vehicle Rental
- Travel
- Mobility
- Transportation
- Fleet Management
website: https://www.hertz.com
---
