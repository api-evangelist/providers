---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'The partner-facing Flix API, published through the Flix Developer Portal. Documentation covers API references, getting-started guides, changelogs and example Postman collections for Flix distribution '
  name: Flix API
  slug: flix-api
- description: First-party GTFS Schedule feeds published by FlixMobility Tech GmbH covering the FlixBus and FlixTrain networks. Three anonymous, unauthenticated regional archives are served from gtfs.gis.flix.tech —
  name: Flix GTFS Schedule Feeds
  slug: flix-gtfs-schedule-feeds
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flixbus-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flixbus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flixbus-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flixbus-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flixbus-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flixbus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flixbus-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/flixbus-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flixbus-llms.txt
- group: company
  title: ''
  type: Website
  url: https://global.flixbus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.flixbus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.api.flixbus.com/
- group: start
  title: ''
  type: SignUp
  url: https://global.flixbus.com/company/partners/affiliate-partners
- group: operate
  title: ''
  type: Support
  url: https://help.flixbus.com/
- group: company
  title: ''
  type: Blog
  url: https://corporate.flix.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flix-tech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://global.flixbus.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.flixbus.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://global.flixbus.com/responsible-disclosure
created: '2026-08-04'
description: 'FlixBus is the long-distance coach brand of Flix SE (formerly FlixMobility), a Munich-headquartered mobility provider that also operates FlixTrain in Europe and Greyhound in North America. Flix runs an asset-light model: it owns the brand, network planning, pricing, distribution and technology while regional bus partners operate the vehicles. Its technology surface is split in two. A partner-facing Flix API is published through the Flix Developer Portal at developer.api.flixbus.com — a Redocly-based catalogue of API references, getting-started guides, changelogs and downloadable Postman collections — but the portal is gated behind Microsoft Entra ID (Azure AD) sign-in and the underlying gateway at global.api.flixbus.com rejects anonymous requests, so no machine-readable OpenAPI is reachable without a distribution-partner agreement (requested via online-distribution@flixbus.com). Publicly and anonymously, Flix does publish schedule data as first-party GTFS Schedule feeds for
  Europe, the United States and Great Britain from gtfs.gis.flix.tech, refreshed regularly and licensed ODbL-1.0 through national open-data portals.'
image: https://cdn-cf.cms.flixbus.com/drupal-assets/ogimage/flixbus.png
layout: provider
modified: '2026-08-04'
name: FlixBus
nav: Providers
network: true
overview: 'FlixBus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Travel, Mobility, and Bus.


  FlixBus'' developer surface includes authentication, documentation, signup flow, support, engineering blog, and 14 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 28.6
  delta: -2.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 30.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flixbus/refs/heads/main/screenshots/flixbus-2026-08-07T165346.png
security:
- kind: authentication
  name: Flixbus Authentication
  slug: flixbus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Flixbus Domain Security
  slug: flixbus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Flixbus Vulnerability Disclosure
  slug: flixbus-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: flixbus
tags:
- Company
- Transportation
- Travel
- Mobility
- Bus
- Rail
- Ticketing
- GTFS
- Open Data
- Distribution
website: https://global.flixbus.com/
---
