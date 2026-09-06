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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Read-oriented JSON REST API exposing a Getro network's companies, jobs and contacts, plus shared reference collections (job functions, industry tags, locations). Bearer API-key auth, URI-path versioni
  name: Getro Network API v2
  slug: getro-network-api-v2
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://getro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getro.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getro.com/
- group: operate
  title: ''
  type: Support
  url: https://help.getro.com/
- group: company
  title: ''
  type: Blog
  url: https://www.getro.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getro.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.getro.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getro.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getro.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getro
- group: auth
  title: ''
  type: Authentication
  url: authentication/getro-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getro-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/getro-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getro-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getro-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/getro-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getro-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getro-domain-security.yml
created: '2026-07-17'
description: Getro provides talent and hiring software for venture-capital firms and professional communities. Its flagship product GetroJobs aggregates every open role across a network's companies into a single automatically-updated job board, while GetroConnect adds a relationship layer for warm introductions at scale — People Finder, Company Research, contact outreach and lightweight CRM. Getro exposes a Network API (v2), a read-oriented JSON REST API that lets a network programmatically page through its companies, jobs and contacts. The API is authenticated with a bearer API key, versioned in the URI path, rate limited to 30 requests per minute, and documented on the Getro developer portal. Getro was founded out of the Techstars community and is now part of Findem.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getro.png
layout: provider
modified: '2026-07-19'
name: Getro
nav: Providers
network: true
overview: 'Getro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job, Talent, Hiring, and Recruiting.


  Getro''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 13 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Getro Rate Limits
  slug: getro-rate-limits
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 28.7
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getro/refs/heads/main/screenshots/getro-2026-07-25T215739.png
security:
- kind: authentication
  name: Getro Authentication
  slug: getro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Getro Domain Security
  slug: getro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getro
tags:
- Company
- Job
- Talent
- Hiring
- Recruiting
- Job Board
- Venture Capital
- Networks
- CRM
website: https://getro.com/
---
