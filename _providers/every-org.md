---
access_model:
  confidence: high
  label: Free (non-commercial)
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.every.org/charity-api
  - plans/every-org-plans-pricing.yml
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Every.org API is a powerful tool that allows developers to access and interact with a wide range of charitable giving data. By integrating the API into their applications, developers can retrieve '
  name: Every.org API
  slug: every-org
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.every.org/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/every-org-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everydotorg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everydotorg
- group: operate
  title: ''
  type: Support
  url: https://support.every.org/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.every.org/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.every.org/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.every.org/charity-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.every.org/docs/endpoints/nonprofits
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.every.org/docs/intro
- group: commercial
  title: ''
  type: Pricing
  url: https://www.every.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.every.org/charity-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.every.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.every.org/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.every.org/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/every-org-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/every-org-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/every-org-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/every-org-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/every-org-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/every-org-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/every-org-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/every-org-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/every-org-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/every-org-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/every-org-packages.yml
- group: design
  title: ''
  type: Components
  url: components/every-org-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/every-org-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/every-org-llms.txt
created: '2025-03-01'
description: Every.org is a platform that empowers individuals to give back and support causes they care about. Users can create fundraising campaigns, donate to verified nonprofits, and track their impact through personalized giving dashboards. Every.org also partners with companies to facilitate workplace giving programs and corporate social responsibility initiatives.
finops:
- name: Every Org Finops
  service_category: API
  slug: every-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/every-org.png
layout: provider
modified: '2026-08-28'
name: Every.org
nav: Providers
network: true
overview: 'Every.org publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Charities, Donations, Fundraising, Non-Profit, and Philanthropy.


  Every.org''s developer surface includes support, engineering blog, API reference, getting-started guide, pricing, signup flow, changelog, and 22 more developer resources.'
plans:
- name: Every Org Plans Pricing
  plan_count: 2
  slug: every-org-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Every Org Rate Limits
  slug: every-org-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 38.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/every-org/refs/heads/main/screenshots/every-org-2026-06-20T180910.png
security:
- kind: authentication
  name: Every Org Authentication
  slug: every-org-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Every Org Domain Security
  slug: every-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: every-org
tags:
- Charities
- Donations
- Fundraising
- Non-Profit
- Philanthropy
- Webhook
- Giving
website: https://www.every.org/
---
