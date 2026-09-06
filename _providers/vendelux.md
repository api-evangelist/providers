---
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendelux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vendelux.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://vendelux.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vendelux.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vendelux.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://vendelux.com/help
- group: company
  title: ''
  type: Blog
  url: https://vendelux.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://developers.vendelux.com/feed/
- group: start
  title: ''
  type: Login
  url: https://vendelux.com/app/events/search
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vendelux
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.vendelux.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/vendelux-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vendelux-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vendelux-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vendelux-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendelux-llms.txt
coverage:
  checked: '2026-09-02'
  detail: 'Vendelux ships an end-user event-marketing web app and nothing else: developers.vendelux.com is an engineering hiring blog rather than a developer portal, api.vendelux.com resolves but its origin 502s on every path, the public GitHub org has zero repositories, no `vendelux` package exists on npm/PyPI/RubyGems/crates.io/Packagist, and the only programmatic surface sold is Vendelux acting as the OAuth client into a customer''s Salesforce or HubSpot tenant.'
  evidence:
  - status: 502
    url: https://api.vendelux.com/openapi.json
  - status: 404
    url: https://developers.vendelux.com/openapi.json
  - status: 404
    url: https://vendelux.com/llms.txt
  - status: 200
    url: https://github.com/Vendelux
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Vendelux is an AI-native event marketing and B2B event intelligence platform that helps go-to-market teams decide which conferences and trade shows to attend, pre-book qualified meetings before an event starts, and attribute pipeline back to specific events. It maintains a proprietary database of 250,000+ global B2B events, enriched from first-party conference-organizer feeds and monitoring of 185,000+ sources, and pushes attendee, lead and ROI data into customer CRMs. Product surfaces are Event Discovery, Meetings, Segments/List Builder and CRM Integration (Salesforce and HubSpot). Founded in 2021 by Alex Reynolds and Stefan Deeran, headquartered in New York City, and backed by FirstMark Capital, Cervin Ventures, Tenacity Ventures and Tri-Valley Ventures. Vendelux publishes no public developer API: as of this profile its programmatic surface consists of OAuth connections Vendelux makes INTO a customer''s Salesforce or HubSpot tenant, not an API, SDK, webhook catalog or machine-readable
  contract it exposes to developers.'
image: https://vendelux.com/wp-content/themes/astra-child/assets/images/logo.svg
layout: provider
modified: '2026-09-02'
name: Vendelux
nav: Providers
network: true
overview: 'Vendelux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Event Intelligence, Event Marketing, B2B Events, Marketing Intelligence, and Sales Intelligence.


  Vendelux''s developer surface includes pricing, support, engineering blog, and 13 more developer resources.'
plans:
- name: Vendelux Plans Pricing
  plan_count: 3
  slug: vendelux-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Vendelux Rate Limits
  slug: vendelux-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Vendelux Domain Security
  slug: vendelux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vendelux Trust Center
  slug: vendelux-trust-center
  summary_line: trust center published
slug: vendelux
tags:
- Event Intelligence
- Event Marketing
- B2B Events
- Marketing Intelligence
- Sales Intelligence
- Event Data
- CRM Integration
- Demand Generation
- Field Marketing
- Conference Data
- Company
website: https://vendelux.com/
---
