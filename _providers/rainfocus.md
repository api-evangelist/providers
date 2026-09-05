---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The RainFocus RESTful integration API. Requests are dispatched against api.rainfocus.com and are keyed on an apiProfile identifier - a named API Profile configured per customer in the RainFocus Integr
  name: RainFocus Platform API
  slug: rainfocus-platform-api
- description: RainFocus Nexus MCP Profiles, announced 7 July 2026, is a first-party remote Model Context Protocol server that exposes live RainFocus event data to AI clients. The endpoint answers at https://api.rai
  name: RainFocus Nexus MCP Profiles
  slug: rainfocus-mcp
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.rainfocus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.rainfocus.com/secure-integrations
- group: operate
  title: ''
  type: Support
  url: https://help.rainfocus.com/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.rainfocus.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.rainfocus.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.rainfocus.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://www.rainfocus.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rainfocus.com/privacy-security/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rainfocus.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.rainfocus.com/privacy-security/vulnerability-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rainfocus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.rainfocus.com/privacy-security/
- group: auth
  title: ''
  type: Compliance
  url: conformance/rainfocus-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rainfocus-conformance.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rainfocus.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rainfocus-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rainfocus-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rainfocus-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/rainfocus-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rainfocus-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rainfocus-domain-security.yml
- group: commercial
  title: ''
  type: APITerms
  url: https://www.rainfocus.com/privacy-security/api-terms-and-conditions/
created: '2026-08-26'
description: 'RainFocus is a Lehi, Utah based enterprise event management and event marketing platform used by large B2B organizations to run conferences, roadshows, field-marketing programs, kickoffs and webinars from a single data-first system. The platform spans registration, call for papers, speaker enablement, sponsor and exhibitor activation, meetings management, on-site check-in and badge printing, a mobile app, and portfolio-level analytics, all anchored on a Global Attendee Profile. Its developer surface is delivered as a customer-provisioned "Integration Suite": RESTful APIs at api.rainfocus.com governed by named API Profiles with modular field mappings and OAuth (Global) client credentials, plus RainFocus Nexus MCP Profiles - an OAuth-secured remote Model Context Protocol server at api.rainfocus.com/mcp/ that lets AI agents read live session capacity, check-in status, attendee, exhibitor and session records and write back changes such as closing registration or updating speaker
  details, with per-event scoping and audit logging. No OpenAPI, GraphQL, AsyncAPI, WSDL or Protobuf contract is published to the public web; API and MCP reference material lives behind the RainFocus Help Center and the customer statement of work.'
image: https://www.rainfocus.com/assets/images/default-open-graph.jpg
layout: provider
mcp_servers:
- description: RainFocus Nexus MCP Profiles is a first-party, hosted, remote Model Context Protocol server for live event data. It was announced on 7 July 2026 and RainFocus describes it as "the first native MCP wit
  name: RainFocus MCP Server
  slug: rainfocus-mcp-server
modified: '2026-08-26'
name: RainFocus
nav: Providers
network: true
overview: 'RainFocus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Event, Event Management, Event Marketing, and Registration.


  RainFocus'' developer surface includes documentation, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Rainfocus Plans Pricing
  plan_count: 0
  slug: rainfocus-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rainfocus Rate Limits
  slug: rainfocus-rate-limits
scopes:
- name: Rainfocus Scopes
  scope_count: 0
  slug: rainfocus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 28.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rainfocus/refs/heads/main/screenshots/rainfocus-2026-09-02T152828.png
security:
- kind: authentication
  name: Rainfocus Authentication
  slug: rainfocus-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Rainfocus Domain Security
  slug: rainfocus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rainfocus Vulnerability Disclosure
  slug: rainfocus-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Rainfocus Trust Center
  slug: rainfocus-trust-center
  summary_line: SOC 2 (AICPA SOC), ISO/IEC 27001:2022, PCI DSS
slug: rainfocus
tags:
- Company
- Event
- Event Management
- Event Marketing
- Registration
- Conferences
- Webinars
- Marketing Technology
- Attendee Data
- MCP
- Agents
- Enterprise Software
- Software-as-a-Service
website: https://www.rainfocus.com/
---
