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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: A single-endpoint GraphQL API for accessing and managing Meetup community data including groups, events, members, tickets (RSVPs), venues, and photos. Supports querying, mutations for event creation a
  name: Meetup GraphQL API
  slug: meetup-graphql-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meetup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meetup-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.meetup.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.meetup.com/hc
- group: docs
  title: ''
  type: APIUserGuide
  url: https://help.meetup.com/hc/en-us/sections/41453323105549
- group: commercial
  title: ''
  type: Terms
  url: https://www.meetup.com/terms/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.meetup.com/privacy/
- group: build
  title: ''
  type: OAuthClients
  url: https://www.meetup.com/api/oauth/list/
created: '2026-06-13'
description: Meetup is a community event platform that connects people with shared interests through in-person and online group meetings. Its GraphQL API enables developers to access group events, members, RSVPs, venue information, and community activity data. The API is available as part of the Meetup Pro subscription and supports event creation, publishing workflows, RSVP management, photo uploads, and network-wide group and event search for Pro organizers.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: The Meetup GraphQL API is a single-endpoint API that provides access to Meetup's community platform data, including groups, events, members, RSVPs, venues, photos, and Pro network management. It is av
  name: Meetup GraphQL API
  slug: meetup-graphql
image: https://www.meetup.com/favicon.ico
layout: provider
modified: '2026-06-13'
name: Meetup
nav: Providers
network: true
overview: 'Meetup publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Event, Community, Group, Meetups, and Social.


  Meetup''s developer surface includes engineering blog, terms of service, privacy policy, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meetup/refs/heads/main/screenshots/meetup-2026-06-20T185133.png
security:
- kind: domain-security
  name: Meetup Domain Security
  slug: meetup-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meetup Vulnerability Disclosure
  slug: meetup-vulnerability-disclosure
  summary_line: disclosure policy published
slug: meetup
tags:
- Event
- Community
- Group
- Meetups
- Social
- GraphQL
---
