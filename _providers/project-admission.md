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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://projectadmission.com/
- group: operate
  title: ''
  type: Support
  url: https://help.pa.exchange/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.pa.exchange/
- group: auth
  title: ''
  type: Security
  url: security/project-admission-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/project-admission-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/project-admission-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/project-admission-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/project-admission-well-known.yml
created: '2026-07-17'
description: Project Admission is a ticketing technology company serving the live event industry — professional sports teams, leagues, artists, theaters, and venues. It layers on top of existing ticketing systems such as SeatGeek, Ticketmaster, and AXS to expand opportunities around the ticket and capture more value before, during, and after an event. Its platform provides branded storefronts, multi-channel inventory management, bulk ticket distribution, split season-ticket ingestion, and fan-engagement tools including influencer and group-sales programs. Project Admission does not publicly expose a developer API, SDKs, or developer portal; this profile captures its verified public web and security surface. Surfaced as a portfolio company of Anthemis and Techstars and added to the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/project-admission.png
layout: provider
modified: '2026-07-20'
name: Project Admission
nav: Providers
network: true
overview: 'Project Admission is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Live Events, Sports, and Entertainment.


  Project Admission''s developer surface includes support and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 7.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/project-admission/refs/heads/main/screenshots/project-admission-2026-09-02T152128.png
security:
- kind: domain-security
  name: Project Admission Domain Security
  slug: project-admission-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Project Admission Vulnerability Disclosure
  slug: project-admission-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: project-admission
tags:
- Company
- Ticketing
- Live Events
- Sports
- Entertainment
- Venues
- Event Technology
website: https://projectadmission.com/
---
