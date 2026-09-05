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
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The account-based marketing platform API behind Terminus (now the DemandScience ABM Platform). The API host api.terminusplatform.com is live and answers every anonymous request with HTTP 401 "Authenti
  name: Terminus ABM Platform API
  slug: terminus-abm-platform-api
- description: A dedicated service that streamlines management of users and employee signature data inside an Email Experiences (Signature Ads, formerly Sigstr) account. Employee data delivered to the API endpoint c
  name: Employee Automation API
  slug: employee-automation-api
- description: 'Email verification API — single-address real-time validation and asynchronous CSV batch verification, sold as Intelligent Verification. OWNERSHIP: this API is served from api.lastbounce.com rather tha'
  name: Verify API
  slug: verify-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://demandscience.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.terminus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.demandscience.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.demandscience.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.demandscienceplatform.com/
- group: company
  title: ''
  type: Blog
  url: https://demandscience.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demandscience.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demandscience.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demandscience
- group: auth
  title: ''
  type: Authentication
  url: authentication/terminus-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terminus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.demandscience.com/hc/en-us/articles/46047614705811-Chat-Experiences-Deprecation-December-31-2025
- group: design
  title: ''
  type: Conformance
  url: conformance/terminus-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terminus-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/terminus-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terminus-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://support.demandscience.com/hc/en-us/sections/38485678357267-API-Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://support.demandscience.com/hc/en-us/sections/201012678-Getting-Started-with-DemandScience
- group: commercial
  title: ''
  type: Pricing
  url: https://demandscience.com/faq/pricing-fit-commercial/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetTerminus
- group: build
  title: ''
  type: Packages
  url: packages/terminus-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/terminus-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terminus-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terminus-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/terminus-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/terminus-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/terminus-sandbox.yml
created: '2026-08-05'
description: 'Terminus is an account-based marketing (ABM) platform covering account-based advertising, web personalization, email-signature marketing (Sigstr), conversational chat (Ramble) and revenue measurement (BrightFunnel). Terminus merged into DemandScience on 2024-11-12; terminus.com now 301-redirects to demandscience.com and the product runs as the DemandScience ABM Platform at app.demandscienceplatform.com. Terminus-branded infrastructure is still in production — api.terminusplatform.com, email.terminusplatform.com (Email Experiences / Signature Ads), terminus.bound360.com (Web Experiences) and *.terminus.services — and the API reference is published on a Redocly developer portal at developer.terminus.com. Platform API access is issued through a support ticket, and every path on the developer portal and the API host requires credentials. A third API is publicly documented: the Verify API (formerly Lastbounce, sold as Intelligent Verification) at api.lastbounce.com, whose endpoints,
  x-api-key header, error envelope and result-code vocabulary are all published in the DemandScience Help Center — as prose and cURL, with no OpenAPI served anywhere. No plans or price points are published, no rate limits are documented, and there is no first-party SDK in any registry for any of the three APIs.'
image: https://demandscience.com/wp-content/uploads/2023/05/cropped-favicon-192x192.png
layout: provider
modified: '2026-08-12'
name: Terminus
nav: Providers
network: true
overview: 'Terminus publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Account Based Marketing, Marketing, Advertising, and Sales.


  Terminus'' developer surface includes documentation, support, engineering blog, authentication, API reference, getting-started guide, pricing, and 20 more developer resources.'
plans:
- name: Terminus Plans Pricing
  plan_count: 0
  slug: terminus-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Terminus Rate Limits
  slug: terminus-rate-limits
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 31.1
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terminus/refs/heads/main/screenshots/terminus-2026-09-02T163148.png
security:
- kind: authentication
  name: Terminus Authentication
  slug: terminus-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Terminus Domain Security
  slug: terminus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Terminus Trust Center
  slug: terminus-trust-center
  summary_line: trust center published
slug: terminus
tags:
- Company
- Account Based Marketing
- Marketing
- Advertising
- Sales
- B2B
- Analytics
- Email
- Email Verification
- Data Quality
website: https://demandscience.com/
---
