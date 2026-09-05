---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 1
apis:
- description: A POST-only REST API for programmatically writing data into Marin. Five bulk endpoints — /campaigns, /groups, /keywords, /ads and /strategies — accept a JSON body containing a single "data" array of r
  name: Marin API
  slug: marin-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.marinsoftware.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marinsoftware.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.marinsoftware.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.marinsoftware.com/
- group: start
  title: ''
  type: Login
  url: https://one.marinsoftware.com
- group: start
  title: ''
  type: SignUp
  url: https://www.marinsoftware.com/marinone-free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marinsoftware.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marinsoftware.com/legal/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marin-software-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://support.marinsoftware.com/en_US/Managing_Campaigns/api
- group: docs
  title: ''
  type: APIReference
  url: https://support.marinsoftware.com/en_US/bulk-actions/marin-api
- group: operate
  title: ''
  type: Support
  url: https://support.marinsoftware.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/marin-software-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marin-software-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marin-software-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marin-software-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marin-software-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marin-software-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marin-software-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/marin-software-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marin-software-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.marinsoftware.com/legal/data-processing-addendum
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marin-software-llms.txt
created: '2026-07-17'
description: Marin Software is a performance marketing and digital advertising management platform used by e-commerce brands, agencies, and enterprise marketers to plan, automate, and optimize paid media at scale across paid search, paid social, retail media, and app advertising channels. Its product line includes MarinOne (campaign management and automation), Marin Connect (marketing data collection and unification), Marin Ascend (cross-channel optimization), Marin for Agencies, and managed services. Marin publishes a POST-only REST write API — the Marin API, at https://api.marinsoftware.com/open-api version 0.1 — that pushes campaigns, groups, keywords, ads and strategies into the platform using HTTP Basic auth, documented only in the help center, plus a Marin Social API whose reference link no longer resolves. There is no OpenAPI, no SDK, no changelog and no status page, and the developer documentation portal has been decommissioned. Marin Software has been acquired by Zax Capital, which
  the company announces on its own homepage.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marin-software.png
layout: provider
modified: '2026-08-12'
name: Marin Software
nav: Providers
network: true
overview: 'Marin Software publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MarTech, Advertising, Marketing, and Performance Marketing.


  Marin Software''s developer surface includes pricing, engineering blog, signup flow, documentation, API reference, support, authentication, and 16 more developer resources.'
plans:
- name: Marin Software Plans Pricing
  plan_count: 3
  slug: marin-software-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Marin Software Rate Limits
  slug: marin-software-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 31.4
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marin-software/refs/heads/main/screenshots/marin-software-2026-07-25T230152.png
security:
- kind: authentication
  name: Marin Software Authentication
  slug: marin-software-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Marin Software Domain Security
  slug: marin-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marin-software
tags:
- Company
- MarTech
- Advertising
- Marketing
- Performance Marketing
- Digital Advertising
- Paid Search
- Paid Social
- Retail Media
- Campaign Management
- Bid Management
- Bulk Upload
website: https://www.marinsoftware.com/
---
