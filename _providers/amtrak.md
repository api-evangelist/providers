---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'Amtrak''s complete national timetable published as a static General Transit Feed Specification archive, served from content.amtrak.com with no registration, no API key, no click-through licence and no '
  name: Amtrak GTFS Schedule Feed
  slug: amtrak-gtfs-schedule-feed
artifact_total: 4
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/amtrak-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amtrak-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amtrak-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amtrak-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/amtrak-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amtrak-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amtrak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amtrak.com/
- group: company
  title: ''
  type: Newsroom
  url: https://media.amtrak.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://media.amtrak.com/rss/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://media.amtrak.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://media.amtrak.com/privacy-policy/
- group: start
  title: ''
  type: TravelAgentPortal
  url: https://portal.railagent.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Amtrak
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amtrak
created: '2026-07-28'
description: 'Amtrak (the National Railroad Passenger Corporation) is the federally chartered operator of the United States national intercity passenger rail network, headquartered in Washington, D.C. It runs the Northeast Corridor including Acela, the state-supported corridors, the long-distance network, and the Amtrak Thruway Connecting Service bus network, and its published GTFS feed covers 61 routes, 646 stops, 2,948 trips and 20 operating agencies across the United States and into Canada. In the distribution chain Amtrak sits as a GDS-intermediated supplier of its own inventory: its content reaches third-party booking tools through Travelport Universal API, through Sabre, Apollo and Worldspan on the RailAgent channel, and through rail aggregators including SilverRail, Travelfusion and RailKey Technologies, alongside its own amtrak.com, mobile app and call centre. Its API posture is honestly stated as one open-standard data feed and nothing else. The only machine-readable contract Amtrak
  publishes is a static GTFS schedule archive at content.amtrak.com, which is completely ungated - no key, no registration, no click-through - but which Amtrak advertises nowhere: there is no developer portal, no documentation page, no OpenAPI, no AsyncAPI, no GraphQL, and no published terms of use for the feed. Everything transactional is closed. The developer., docs., data. and partners. subdomains of amtrak.com do not resolve, developers.amtrak.com resolves only to a Microsoft Entra application proxy, api.amtrak.com answers 401 on every path from Akamai NetStorage, and www.amtrak.com returns 403 to every non-browser client, so no first-party terms of service could be retrieved programmatically. A developer who wants shopping, booking, payment, ticketing or servicing does not sign up; they are accredited through Travelport or an aggregator, complete an Amtrak test-case worksheet, pass a three-week UAT, and commit to supporting Amtrak refund fees and eVoucher issuance before production
  credentials are issued.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Amtrak GTFS Schedule Feed record schemas
  property_count: 8
  slug: amtrak-gtfs
layout: provider
modified: '2026-07-28'
name: Amtrak
nav: Providers
network: true
overview: 'Amtrak publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United States, Rail, Passenger Rail, and Transit.


  Amtrak''s developer surface includes authentication and 15 more developer resources.'
random_paper: 60
score:
  band: emerging
  composite: 23.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 9.7
    developer_ergonomics: 12.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 23.0
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amtrak/refs/heads/main/screenshots/amtrak-2026-08-07T161348.png
security:
- kind: authentication
  name: Amtrak Authentication
  slug: amtrak-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Amtrak Domain Security
  slug: amtrak-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: amtrak
tags:
- Travel
- United States
- Rail
- Passenger Rail
- Transit
- GTFS
- Open Data
- Booking
- Distribution
- GDS
- Corporate Travel
- Travel Agents
- Loyalty
website: https://www.amtrak.com/
---
