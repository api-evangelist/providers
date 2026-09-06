---
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for the Solsten assessment and persona platform. Documented operations cover listing users who completed an assessment (paged, 500 per page, one-hour cache), checking a single user's assessme
  name: Solsten API
  slug: solsten-api
artifact_total: 7
asyncapis:
- description: ''
  name: 12Traits Webhooks
  slug: 12traits-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://solsten.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.solsten.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.solsten.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.solsten.io/
- group: start
  title: ''
  type: Login
  url: https://dashboard.solsten.io/
- group: operate
  title: ''
  type: Support
  url: https://solsten.io/contact
- group: company
  title: ''
  type: Blog
  url: https://solsten.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/12traits
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solsten.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solsten.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/12traits-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/12traits-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/12traits-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/12traits-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/12traits-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/12traits-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/12traits-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/12traits-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/12traits-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/12traits-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/12traits-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/12traits-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/12traits-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/12traits-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/12traits-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://solsten.io/llms.txt
created: '2026-09-05'
description: Solsten (originally 12traits) is a Berlin- and Minneapolis-based psychological-AI company that builds audience intelligence for product, marketing and research teams, pairing validated psychographic measurement with behavioural telemetry to model how real people think, decide and engage. Its product suite spans Traits (assessment-driven psychographic personas for a company's real customers), Navigator (a library of 200,000+ pre-profiled audiences drawn from 2M+ questionnaire respondents) and Elaris (audience-aware generative content). The public developer surface is a small REST API at api.solsten.io covering assessment completion, per-user assessment status, segment/persona user lists and GDPR-style user-data deletion, plus a documented Microsoft Azure PlayFab webhook and a cloud-object-storage bulk ingestion contract for behavioural events and KPIs.
image: https://solsten.io/api/images/?path=2023/08/Solsten_avatar.png
layout: provider
modified: '2026-09-05'
name: Solsten
nav: Providers
network: true
overview: 'Solsten publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audience Intelligence, Psychographics, Consumer Insights, and Analytics.


  The Solsten catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Solsten''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: 12Traits Plans Pricing
  plan_count: 0
  slug: 12traits-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: 12Traits Rate Limits
  slug: 12traits-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 12Traits Authentication
  slug: 12traits-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 12Traits Domain Security
  slug: 12traits-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 12Traits Vulnerability Disclosure
  slug: 12traits-vulnerability-disclosure
  summary_line: Hackerone
slug: 12traits
tags:
- Company
- Audience Intelligence
- Psychographics
- Consumer Insights
- Analytics
- Artificial Intelligence
- Gaming
- Market Research
- Personalization
- Behavioral Data
website: https://solsten.io/
---
