---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Demio Agentic Access
  operation_count: 7
  slug: demio-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 3
apis:
- description: Events, Event Sessions (Dates) and attendee registration. List and read Events, read a specific Session, and register a person for an Event to receive their unique join link.
  name: Demio Events API
  slug: demio-events-api
- description: Per-Session participation and attendance reporting — the participant list for an Event Session with attendance status and registration custom-field values.
  name: Demio Reports API
  slug: demio-reports-api
- description: Authorization verification. Confirms an account API key/secret pair is valid and reports whether it is a sandbox credential.
  name: Demio Intro API
  slug: demio-intro-api
artifact_total: 10
asyncapis:
- description: ''
  name: Demio Events
  slug: demio-events
collections:
- collection_type: open
  name: Public Demio API
  slug: open-demio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.demio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://publicdemioapi.docs.apiary.io
- group: docs
  title: ''
  type: Documentation
  url: https://publicdemioapi.docs.apiary.io
- group: docs
  title: ''
  type: APIReference
  url: https://publicdemioapi.docs.apiary.io
- group: start
  title: ''
  type: GettingStarted
  url: https://help.demio.com/en/articles/4544025-api-limitations
- group: operate
  title: ''
  type: Support
  url: https://help.demio.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.demio.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.demio.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meetdemio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.demio.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://my.demio.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banzai.io/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demio.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/demio-openapi.yml
- group: other
  title: ''
  type: APIBlueprint
  url: openapi/demio-api-blueprint-original.apib
- group: auth
  title: ''
  type: Authentication
  url: authentication/demio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/demio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/demio-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/demio-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/demio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/demio-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/demio-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/demio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/demio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/demio-components.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/demio-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demio-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demio-help-center-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/demio-openapi-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/demio-examples.yml
created: '2026-08-12'
description: 'Demio is a browser-based webinar and virtual-event platform built for B2B marketing and sales teams, operated by Banzai International, Inc. (NASDAQ: BNZI). It runs live, automated/evergreen, on-demand and series webinars with no attendee download, and pairs them with customizable registration pages, embeddable registration forms, in-session engagement tools (polls, handouts, featured actions, chat), recordings, Showcase event listings and post-webinar analytics. Its public developer surface is the Public Demio API — a key/secret authorized REST API at https://my.demio.com/api/v1 covering Events, Event Sessions (Dates), attendee registration with unique join links, and per-Session participation reporting. Demio documents the API as an Apiary API Blueprint, publishes burst rate limits and daily call quotas, runs a public Atlassian Statuspage, ships one first-party PHP SDK from its meetdemio GitHub organization, and offers a Zapier app with registration, join, no-show and event-update
  triggers for teams that do not want to call the API directly.'
image: https://cdn.prod.website-files.com/639df5c77a191c7268d2f9a2/63d939e13b301514d7b3dbab_60ee09e2a0845e4356fd7641_5a86d4765e69d200011f70a5_favicon-256.png
layout: provider
modified: '2026-08-12'
name: Demio
nav: Providers
network: true
overview: 'Demio publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, Reports API, and Intro API. Tagged areas include Company, Webinars, Virtual Events, Event Management, and Marketing.


  The Demio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Demio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Demio Plans Pricing
  plan_count: 4
  slug: demio-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Demio Rate Limits
  slug: demio-rate-limits
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 25.5
    developer_ergonomics: 60.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demio/refs/heads/main/screenshots/demio-2026-08-17T080854.png
security:
- kind: authentication
  name: Demio Authentication
  slug: demio-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Demio Domain Security
  slug: demio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: demio
tags:
- Company
- Webinars
- Virtual Events
- Event Management
- Marketing
- Marketing Technology
- Demand Generation
- Video
- Engagement Marketing
- Lead Generation
- Software-as-a-Service
website: https://www.demio.com
---
