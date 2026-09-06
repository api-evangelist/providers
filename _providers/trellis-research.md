---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST Data API (V2, May 2024) for programmatic access to U.S. state and federal trial court data — Search (Boolean/query over Cases, Documents, Rulings with filtering and sorting), Rulings, Judges, Usa
  name: Trellis Trial Court Data API
  slug: trellis-trial-court-data-api
artifact_total: 5
asyncapis:
- description: ''
  name: Trellis Research Webhooks
  slug: trellis-research-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://trellis.law/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.trellis.law/trellis-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.trellis.law/
- group: docs
  title: ''
  type: APIReference
  url: https://support.trellis.law/trellis-api
- group: company
  title: ''
  type: Blog
  url: https://blog.trellis.law/
- group: operate
  title: ''
  type: Support
  url: https://support.trellis.law/
- group: start
  title: ''
  type: SignUp
  url: https://trellis.law/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trellis.law/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trellis.law/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trellis.law/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trellis-research-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trellis-research-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trellis-research-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trellis-research-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trellis-research-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trellis-research-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trellis-research-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trellis-research-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trellis-research-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trellis-research-domain-security.yml
created: '2026-07-17'
description: Trellis (trellis.law) is an AI-powered state and federal court research and litigation analytics platform built by litigators for legal teams. It aggregates the most extensive U.S. trial court data available — State Trial, Federal, District, Appellate, Supreme Court, and Bankruptcy cases across all 50 states plus DC — and exposes it through Smart Search, a REST Data API (V2, with federal and PACER integration), and a remote OAuth-secured MCP server. Capabilities include case/docket search, document retrieval, tentative rulings, verdict records, judge and firm analytics, party and expert search, case/topic alerts, and webhook notifications for docket refreshes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trellis-research.png
layout: provider
mcp_servers:
- description: Official remote MCP server from Trellis (trellis.law) exposing litigation research tools over U.S. state, federal, appellate, supreme, and bankruptcy court data — case search, document retrieval, tent
  name: Trellis Law MCP
  slug: trellis-law-mcp
modified: '2026-07-21'
name: Trellis Research
nav: Providers
network: true
overview: 'Trellis Research publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Research, Court Records, and Litigation Analytics.


  The Trellis Research catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trellis Research''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, changelog, and 13 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 39.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trellis-research/refs/heads/main/screenshots/trellis-research-2026-08-17T082432.png
security:
- kind: authentication
  name: Trellis Research Authentication
  slug: trellis-research-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Trellis Research Domain Security
  slug: trellis-research-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trellis-research
tags:
- Company
- Legal
- Legal Research
- Court Records
- Litigation Analytics
- Judicial Analytics
- Legal Data
- MCP
website: https://trellis.law/
---
