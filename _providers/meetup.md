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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
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
overview: 'Meetup publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Events, Community, Groups, Meetups, and Social.


  Meetup''s developer surface includes engineering blog, terms of service, privacy policy, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 91
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 43.2
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
- Events
- Community
- Groups
- Meetups
- Social
- GraphQL
---
