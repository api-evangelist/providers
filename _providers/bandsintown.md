---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bandsintown Agentic Access
  operation_count: 2
  slug: bandsintown-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://rest.bandsintown.com
  baseurl_source: declared
  description: The artist events API from Bandsintown — 1 operation(s) for artist events.
  name: Bandsintown artist events API
  slug: bandsintown-artist-events-api
- baseURL: https://rest.bandsintown.com
  baseurl_source: declared
  description: The artist information API from Bandsintown — 1 operation(s) for artist information.
  name: Bandsintown artist information API
  slug: bandsintown-artist-information-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bandsintown artist events API
  slug: open-bandsintown-artist-events-api
- collection_type: open
  name: Bandsintown artist events artist information API
  slug: open-bandsintown-artist-information-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bandsintown-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bandsintown-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bandsintown.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.artists.bandsintown.com/en/articles/9186477-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.artists.bandsintown.com/en/articles/7053475-what-is-the-bandsintown-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bandsintown
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bandsintown/api-gem
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bandsintown.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corp.bandsintown.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corp.bandsintown.com/privacy
- group: operate
  title: ''
  type: Contact
  url: mailto:API@bandsintown.com
- group: company
  title: ''
  type: Blog
  url: https://artists.bandsintown.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/bandsintown-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bandsintown-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bandsintown-finops.yml
created: '2026-05-28'
description: Bandsintown is a concert discovery platform that connects fans with live music events through a REST API for accessing artist event listings, venue information, and fan notification management. The platform serves as the largest database of upcoming concert listings and concert tickets, enabling artists, developers, and partners to display tour dates, retrieve artist metadata, filter events by date range, and drive fan engagement through RSVP and notification tracking. API access requires an app_id parameter obtained through the Bandsintown for Artists account settings or via a partnership request for broader integration use cases.
examples:
- key_count: 9
  name: Artist Data Example
  slug: artist-data-example
- key_count: 9
  name: Event Data Example
  slug: event-data-example
finops:
- name: Bandsintown Finops
  service_category: ''
  slug: bandsintown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bandsintown.png
json_schemas:
- name: ArtistData
  property_count: 9
  slug: artist-data
- name: EventData
  property_count: 9
  slug: event-data
- name: OfferData
  property_count: 3
  slug: offer-data
- name: VenueData
  property_count: 6
  slug: venue-data
jsonld:
- class_count: 8
  name: Bandsintown Context
  property_count: 19
  slug: bandsintown-context
layout: provider
modified: '2026-06-13'
name: Bandsintown
nav: Providers
network: true
overview: 'Bandsintown publishes 2 APIs on the [APIs.io](https://apis.io/) network: artist events API and artist information API. Tagged areas include Concerts, Live Music, Event, Artists, and Venues.


  The Bandsintown catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bandsintown''s developer surface includes documentation, getting-started guide, engineering blog, and 12 more developer resources.'
plans:
- name: Bandsintown Plans Pricing
  plan_count: 2
  slug: bandsintown-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Bandsintown Rate Limits
  slug: bandsintown-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bandsintown API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bandsintown-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 53.7
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 39.5
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bandsintown/refs/heads/main/screenshots/bandsintown-2026-06-20T172944.png
security:
- kind: domain-security
  name: Bandsintown Domain Security
  slug: bandsintown-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bandsintown
tags:
- Concerts
- Live Music
- Event
- Artists
- Venues
- Music Discovery
- tour dates
- Tickets
- fan notifications
- Entertainment
website: https://www.bandsintown.com/
---
