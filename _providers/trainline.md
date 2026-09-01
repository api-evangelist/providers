---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Trainline Partner Solutions'' wholesale rail and coach distribution API, sold to travel sellers, OTAs, TMCs and corporate booking tools. Trainline publicly describes it as "a modern, intuitive RESTful '
  name: Trainline Global API
  slug: trainline-global-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/trainline-eu/stations/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/trainline-eu/stations/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/trainline-eu/stations/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trainline-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trainline-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.thetrainline.com/terms/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/trainline-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.thetrainline.com/terms/security
- group: design
  title: ''
  type: Conformance
  url: conformance/trainline-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trainline-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trainline-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trainline-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/trainline-packages.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trainline-station-identifiers.yml
- group: docs
  title: ''
  type: JsonSchema
  url: json-schema/trainline-station.json
- group: company
  title: ''
  type: Website
  url: https://www.thetrainline.com/
- group: company
  title: ''
  type: Website
  url: https://www.trainlinegroup.com/
- group: start
  title: ''
  type: Portal
  url: https://tps.thetrainline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tps.thetrainline.com/our-products/
- group: operate
  title: ''
  type: Support
  url: https://tps.thetrainline.com/partner-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thetrainline.com/terms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tps.thetrainline.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thetrainline.com/terms/privacy
- group: company
  title: ''
  type: Blog
  url: https://tps.thetrainline.com/blog-and-media/
- group: company
  title: ''
  type: Blog
  url: https://media.trainline.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trainline
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trainline-eu
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/trainline-eu/stations
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trainline
- group: company
  title: ''
  type: Twitter
  url: https://x.com/thetrainline
- group: operate
  title: ''
  type: Support
  url: https://support.thetrainline.com/en/support/home
- group: company
  title: ''
  type: Partners
  url: https://www.thetrainline.com/about-us/partnerships
- group: company
  title: ''
  type: Investors
  url: https://www.trainlinegroup.com/investors
created: '2026-07-28'
description: 'Trainline plc is Europe''s leading independent rail and coach ticket retailer and distribution platform, headquartered in London and listed on the London Stock Exchange, with the United Kingdom as its home market. It aggregates fares, inventory and real-time journey data from 270+ rail and coach carriers across more than 40 countries and resells that content through its own consumer app and website, through Trainline for Business, and — via Trainline Solutions / Trainline Partner Solutions — as wholesale distribution to other travel sellers through its Global API, Agent Tool and White Label products. In distribution terms Trainline is an aggregator-reseller sitting between the carriers and the traveller: rail has no GDS-equivalent oligopoly and no NDC, so Trainline is itself the intermediation layer, holding the carrier connections, the ticket-issuing accreditation and the settlement relationships that a competitor would otherwise have to rebuild carrier by carrier. Its API
  posture is honestly gated: the Global API is publicly described as "a modern, intuitive RESTful API" on tps.thetrainline.com but there is no developer portal, no public reference, no sandbox and no OpenAPI — access requires a commercial agreement reached through a sales conversation, and in Great Britain a retailer also needs Rail Delivery Group / Rail Settlement Plan third-party retailer accreditation and a bond. The one genuinely open artifact is the ODbL-licensed European station database Trainline publishes on GitHub, which maps its internal station ids to UIC codes, ATOC/CRS codes and carrier-specific ids.'
image: https://tps.thetrainline.com/apple-touch-icon.png
json_schemas:
- name: Trainline European Station
  property_count: 76
  slug: trainline-station
layout: provider
modified: '2026-07-28'
name: Trainline
nav: Providers
network: true
overview: 'Trainline publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Rail, United Kingdom, Europe, and Booking.


  Trainline''s developer surface includes developer portal, documentation, support, engineering blog, and 29 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 86.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 22.0
    operational_transparency: 13.2
  open_source:
    applies: true
    score: 25.0
  previous_composite: 22.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Trainline Domain Security
  slug: trainline-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trainline Vulnerability Disclosure
  slug: trainline-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Trainline Trust Center
  slug: trainline-trust-center
  summary_line: PCI DSS Level 1, ISO/IEC 27001, ISO 22301
slug: trainline
tags:
- Travel
- Rail
- United Kingdom
- Europe
- Booking
- Ticketing
- Distribution
- OTA
- Corporate Travel
website: https://www.thetrainline.com/
---
