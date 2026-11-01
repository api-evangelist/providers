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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Single public unauthenticated HTTP endpoint (POST https://formboost.app/f/{alias}) that accepts JSON or form-encoded submissions. Returns 202 to JSON clients and 302 to HTML form posts. Discovery via '
  name: Formboost Form Submission API
  slug: formboost-form-submission-api
artifact_total: 10
asyncapis:
- description: ''
  name: Formboost Webhooks
  slug: formboost-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.formboost.app/
- group: docs
  title: ''
  type: Documentation
  url: https://formboost.app/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.formboost.app
- group: docs
  title: ''
  type: APIReference
  url: https://formboost.app/docs/api-reference-and-config
- group: start
  title: ''
  type: GettingStarted
  url: https://formboost.app/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://formboost.app/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://formboost.app/faq
- group: company
  title: ''
  type: Blog
  url: https://formboost.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/formboost
- group: commercial
  title: ''
  type: Pricing
  url: https://formboost.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.formboost.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://formboost.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://formboost.app/privacy
- group: auth
  title: ''
  type: Security
  url: https://formboost.app/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.formboost.app
- group: operate
  title: ''
  type: ChangeLog
  url: https://formboost.app/changelog
- group: agent
  href: https://artifacts.apis.io/formboost/llms/formboost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/formboost-llms.txt
- group: operate
  href: https://artifacts.apis.io/formboost/changelog/formboost-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/formboost-changelog.yml
- group: design
  href: https://artifacts.apis.io/formboost/lifecycle/formboost-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/formboost-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/formboost/plans/formboost-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/formboost-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/formboost/rate-limits/formboost-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/formboost-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/formboost/authentication/formboost-authentication.yml
  title: ''
  type: Authentication
  url: authentication/formboost-authentication.yml
- group: design
  href: https://artifacts.apis.io/formboost/conventions/formboost-conventions.yml
  title: ''
  type: Conventions
  url: conventions/formboost-conventions.yml
- group: design
  href: https://artifacts.apis.io/formboost/errors/formboost-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/formboost-problem-types.yml
- group: design
  href: https://artifacts.apis.io/formboost/asyncapi/formboost-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/formboost-webhooks.yml
- group: design
  href: https://artifacts.apis.io/formboost/conformance/formboost-conformance.yml
  title: ''
  type: Conformance
  url: conformance/formboost-conformance.yml
- group: auth
  href: https://artifacts.apis.io/formboost/conformance/formboost-conformance.yml
  title: ''
  type: Compliance
  url: conformance/formboost-conformance.yml
- group: auth
  href: https://artifacts.apis.io/formboost/security/formboost-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/formboost-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/formboost/security/formboost-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/formboost-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/formboost/security/formboost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/formboost-domain-security.yml
- group: build
  href: https://artifacts.apis.io/formboost/packages/formboost-packages.yml
  title: ''
  type: Packages
  url: packages/formboost-packages.yml
created: '2026-09-02'
description: Form-backend-as-a-service with a single unauthenticated HTTP POST submission endpoint for any frontend or static site. Submissions land in an inbox and searchable dashboard and can fan out to Google Sheets, email, Slack, Discord, Telegram, Zapier, n8n, and webhooks. No backend code, server, or database required.
finops:
- has_sources: true
  method: derived
  name: Formboost Finops
  primary_unit: subscription
  service_category: ''
  slug: formboost-finops
  template: false
image: https://formboost.app/og.png
layout: provider
modified: '2026-09-02'
name: Formboost
nav: Providers
network: true
overview: 'Formboost is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Forms, Form Backend, HTML Forms, Serverless, and Static Sites.


  The Formboost catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Formboost''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Formboost Plans Pricing
  plan_count: 4
  slug: formboost-plans-pricing
- name: Formboost Price Estimates
  plan_count: 0
  slug: formboost-price-estimates
random_paper: 3
rate_limits:
- limit_count: 5
  name: Formboost Rate Limits
  slug: formboost-rate-limits
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 64.3
    operational_transparency: 86.8
  previous_composite: 62.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/formboost/formboost-2026-10-11T104617.png
security:
- kind: authentication
  name: Formboost Authentication
  slug: formboost-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Formboost Domain Security
  slug: formboost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Formboost Vulnerability Disclosure
  slug: formboost-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Formboost Trust Center
  slug: formboost-trust-center
  summary_line: trust center published
slug: formboost
tags:
- Forms
- Form Backend
- HTML Forms
- Serverless
- Static Sites
- React
- Next.js
- Vue
- Webhook
- No-Code
- Developer Tools
- Spam Filtering
website: https://www.formboost.app/
---
