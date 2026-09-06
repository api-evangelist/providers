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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: TrueVault Safe is a REST API and secure datastore for sensitive personal data. Resources include Users, Groups (with policy-based Access Grid permissions), Vaults, BLOBs, Documents, Schemas, Search (f
  name: TrueVault Safe REST API
  slug: truevault-safe-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.truevault.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truevault.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.truevault.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.truevault.com/Overview.html
- group: operate
  title: ''
  type: Support
  url: https://www.truevault.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.truevault.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truevault
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truevault.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.truevault.com/register
- group: start
  title: ''
  type: Login
  url: https://console.truevault.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truevault.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.truevault.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.truevault.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/truevault-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/truevault-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truevault-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truevault-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truevault-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truevault-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/truevault-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truevault-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/truevault-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truevault-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truevault-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truevault-domain-security.yml
created: '2026-07-17'
description: TrueVault provides developer infrastructure for storing and managing sensitive personal data in a compliant way. Its original product, TrueVault Safe, is a HIPAA-oriented REST API and secure datastore that lets applications create Vaults and store encrypted Documents, BLOBs, Users, and Schemas, with group-based access control (the Access Grid), full-text and geospatial Search, transactional Email/SMS messaging, password-reset flows, and scoped access tokens. Authentication is via API keys or user access tokens passed in an HTTP Basic header. TrueVault's newer Polaris product is privacy-compliance software that helps ecommerce brands comply with US state privacy laws, the GDPR, and the CCPA. TrueVault is a Y Combinator-backed company.
image: https://github.com/truevault.png
layout: provider
modified: '2026-07-21'
name: TrueVault
nav: Providers
network: true
overview: 'TrueVault publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Privacy, Security, Compliance, and HIPAA.


  TrueVault''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 30.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truevault/refs/heads/main/screenshots/truevault-2026-09-02T164359.png
security:
- kind: authentication
  name: Truevault Authentication
  slug: truevault-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Truevault Domain Security
  slug: truevault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truevault
tags:
- Company
- Data Privacy
- Security
- Compliance
- HIPAA
- Data Storage
- Encryption
- Identity
- Privacy
- PII
website: https://console.truevault.com/
---
