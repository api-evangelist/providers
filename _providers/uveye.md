---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Uveye Agentic Access
  operation_count: 8
  slug: uveye-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.uveye.dev/v1
  baseurl_source: declared
  description: Appraisal / quote data derived from an inspection.
  name: UVeye Appraisal API
  slug: uveye-appraisal-api
- baseURL: https://api.uveye.dev/v1
  baseurl_source: declared
  description: Retrieve vehicle inspection data and the most recent inspections for a site or site group.
  name: UVeye Inspections API
  slug: uveye-inspections-api
- baseURL: https://api.uveye.dev/v1
  baseurl_source: declared
  description: Inspection imagery.
  name: UVeye Media API
  slug: uveye-media-api
- baseURL: https://api.uveye.dev/v1
  baseurl_source: declared
  description: Submit dealer inventory for merchandising and mark vehicles sold.
  name: UVeye Merchandise API
  slug: uveye-merchandise-api
- baseURL: https://api.uveye.dev/v1
  baseurl_source: declared
  description: Generate and record customer-facing public inspection links.
  name: UVeye Public Links API
  slug: uveye-public-links-api
artifact_total: 18
asyncapis:
- description: ''
  name: Uveye Merchandise Webhooks
  slug: uveye-merchandise-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UVeye Public API v1 Appraisal API
  slug: open-uveye-appraisal-api
- collection_type: open
  name: UVeye Public API v1 Inspections API
  slug: open-uveye-inspections-api
- collection_type: open
  name: UVeye Public API v1 Media API
  slug: open-uveye-media-api
- collection_type: open
  name: UVeye Public API v1 Merchandise API
  slug: open-uveye-merchandise-api
- collection_type: open
  name: UVeye Public API v1 Public Links API
  slug: open-uveye-public-links-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uveye-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/uveye-public-api-v1-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uveye-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uveye-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uveye.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.v1.uveye.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://api.v1.uveye.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://api.v1.uveye.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.v1.uveye.dev/
- group: build
  title: ''
  type: Postman
  url: https://api.v1.uveye.dev/
- group: operate
  title: ''
  type: Support
  url: https://uveye.com/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://uveye.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://uveye.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UVeye
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uveye.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uveye.com/terms-and-conditions/
- group: start
  title: ''
  type: SignUp
  url: https://us.backoffice.uveye.app/
- group: auth
  title: ''
  type: TrustCenter
  url: security/uveye-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.uveye.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.uveye.com/
- group: company
  title: ''
  type: Careers
  url: https://uveye.com/careers/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uveye-merchandise-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uveye-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uveye-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/uveye-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uveye-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uveye-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uveye-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uveye-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uveye-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/uveye-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uveye-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uveye-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uveye-vulnerability-disclosure.yml
created: '2026-08-02'
description: 'UVeye builds AI-powered automated vehicle inspection systems — "the MRI for cars" — that drive a vehicle through a scanning lane and produce a full condition report in seconds. Four scanning modules cover the vehicle: Artemis (tires and tread), Helios (undercarriage), Atlas (exterior body damage) and Apollo (interior). The systems are deployed across dealership service lanes, fleet and leasing depots, auctions and remarketing lots, rental returns, OEM manufacturing and logistics/PDI ports. UVeye exposes the resulting inspection data to third parties through the UVeye Public API v1 — inspection detail lookups by VIN, license plate, inspection id or barcode, latest-inspection discovery by site or site group, customer-facing public inspection links, appraisal/quote data, inspection imagery, and a Merchandise surface that ingests dealer inventory and pushes rendered multi-angle imagery back over a signed webhook. Headquartered in Teaneck, New Jersey with offices in Norcross GA,
  Tel Aviv and London.'
image: https://uveye.com/favicon.ico
layout: provider
modified: '2026-08-02'
name: UVeye
nav: Providers
network: true
overview: 'UVeye publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Appraisal API, Inspections API, Media API, and 2 more. Tagged areas include Automotive, Vehicle Inspection, Artificial Intelligence, Computer-Vision, and Dealerships.


  The UVeye catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  UVeye''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 28 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 3
  name: Uveye Rate Limits
  slug: uveye-rate-limits
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 66.8
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uveye/refs/heads/main/screenshots/uveye-2026-08-17T082702.png
security:
- kind: authentication
  name: Uveye Authentication
  slug: uveye-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Uveye Domain Security
  slug: uveye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uveye Vulnerability Disclosure
  slug: uveye-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Uveye Trust Center
  slug: uveye-trust-center
  summary_line: SOC 2, ISO 27001
slug: uveye
tags:
- Automotive
- Vehicle Inspection
- Artificial Intelligence
- Computer-Vision
- Dealerships
- Fleet Management
- Auctions and Remarketing
- Automotive Retail
- Inspection Data
- Company
website: https://uveye.com/
---
