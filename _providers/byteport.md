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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API to copy, move, pull, share, and list files across connected storage providers (Amazon S3, Google Drive, Dropbox, Box and more) using the DART acceleration protocol. Bearer API-key auth over h
  name: Byteport API
  slug: byteport-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/byteport-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.byteport.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.byteport.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.byteport.com/api-reference
- group: company
  title: ''
  type: Website
  url: https://byteport.com
- group: commercial
  title: ''
  type: Pricing
  url: https://byteport.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.byteport.io
- group: start
  title: ''
  type: Login
  url: https://app.byteport.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://byteport.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://byteport.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://byteport.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbyteport
- group: auth
  title: ''
  type: Authentication
  url: authentication/byteport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/byteport-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/byteport-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/byteport-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/byteport-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/byteport-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/byteport-llms.txt
created: '2026-07-17'
description: Byteport is a San Francisco-based file transfer acceleration company (Y Combinator W2026) that moves large datasets across the internet using DART (Dynamic Accelerated Record Transfer), a proprietary protocol the company reports as typically 10x faster than TCP and up to 1000-1500x faster over unreliable cellular or satellite links. The Byteport API lets developers copy, move, pull, share, and list files across connected storage providers such as Amazon S3, Google Drive, Dropbox, and Box at scales from 1GB to 100TB with zero network configuration, targeting robotics, satellite, AI/ML, SaaS data-distribution, and defense workloads.
image: https://github.com/getbyteport.png
layout: provider
modified: '2026-07-18'
name: Byteport
nav: Providers
network: true
overview: 'Byteport publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, File Transfer, Data Transfer, Acceleration, and Cloud Storage.


  Byteport''s developer surface includes documentation, API reference, pricing, signup flow, support, authentication, and 13 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 23.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/byteport/refs/heads/main/screenshots/byteport-2026-07-25T204142.png
security:
- kind: authentication
  name: Byteport Authentication
  slug: byteport-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Byteport Domain Security
  slug: byteport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: byteport
tags:
- Company
- File Transfer
- Data Transfer
- Acceleration
- Cloud Storage
- Robotics
- Artificial Intelligence
- Satellite
- Infrastructure
- Y Combinator
website: https://byteport.com
---
