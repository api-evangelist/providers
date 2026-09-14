---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 3
apis:
- description: Read-only GraphQL API serving a venue's activity schedules — classes, trainings, workshops, courses, events, retreats, camps, and educations — with venue, teacher, room, sport, and availability detail
  name: Eversports Provider API
  slug: eversports-provider-api
- description: GraphQL API for aggregator partners exposing venues, classes, sessions, and reservations, plus mutations to make, cancel, and check in reservations. Separate test and production hosts. Bearer auth, Re
  name: Eversports Aggregator API
  slug: eversports-aggregator-api
- description: Legacy JSON:API REST integration API used by aggregator and partner systems to manage users, venues, courts, and orders on the Eversports platform. Requests and responses follow the jsonapi.org format
  name: Eversports Integration API (v2)
  slug: eversports-integration-api-v2
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.eversports.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aggregator.eversports.io/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.eversportsmanager.com/what-is-the-provider-api
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.eversportsmanager.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eversport
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eversportsmanager.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.eversportsmanager.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.eversportsmanager.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eversportsmanager.com/gtc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eversportsmanager.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/eversports-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eversports-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eversports-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eversports-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eversports-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eversports-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eversports-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/eversports-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eversports-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eversports-domain-security.yml
created: '2026-07-17'
description: 'Eversports is a European sports and fitness platform that lets consumers discover and book classes, courts, and memberships across studios, gyms, and clubs, and gives those businesses a back-office management suite (Eversports Manager) for scheduling, bookings, payments, and customer management. Eversports Manager exposes two public GraphQL APIs: a read-only Provider API that serves a venue''s activity schedules (classes, trainings, workshops, courses, events, retreats, camps, educations) with venue, teacher, room, sport, and availability detail; and an Aggregator API that exposes venues, classes, sessions, and reservations plus mutations to make, cancel, and check in reservations for aggregator partners. Both APIs authenticate with a Bearer token issued by Eversports and use Relay-style cursor pagination.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eversports.png
layout: provider
modified: '2026-07-19'
name: Eversports
nav: Providers
network: true
overview: 'Eversports publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Fitness, Booking, and Scheduling.


  Eversports'' developer surface includes documentation, support, pricing, signup flow, authentication, sandbox, and 15 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/eversports/refs/heads/main/screenshots/eversports-2026-07-25T213739.png
security:
- kind: authentication
  name: Eversports Authentication
  slug: eversports-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eversports Domain Security
  slug: eversports-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: eversports
tags:
- Company
- Sports
- Fitness
- Booking
- Scheduling
- Wellness
- GraphQL
- Reservations
- Event
website: https://www.eversports.com
---
