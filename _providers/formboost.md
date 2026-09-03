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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Single public unauthenticated HTTP endpoint (POST https://formboost.app/f/{alias}) that accepts JSON or form-encoded submissions. Returns 202 to JSON clients and 302 to HTML form posts. Discovery via '
  name: Formboost Form Submission API
  slug: formboost-form-submission-api
artifact_total: 8
asyncapis:
- description: ''
  name: Formboost Webhooks
  slug: formboost-webhooks
common:
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
  title: ''
  type: LLMsTxt
  url: llms/formboost-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/formboost-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/formboost-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/formboost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formboost-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formboost-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/formboost-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/formboost-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/formboost-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/formboost-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/formboost-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/formboost-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/formboost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formboost-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/formboost-packages.yml
created: '2026-09-02'
description: Form-backend-as-a-service with a single unauthenticated HTTP POST submission endpoint for any frontend or static site. Submissions land in an inbox and searchable dashboard and can fan out to Google Sheets, email, Slack, Discord, Telegram, Zapier, n8n, and webhooks. No backend code, server, or database required.
image: https://formboost.app/og.png
layout: provider
modified: '2026-09-02'
name: Formboost
nav: Providers
network: true
overview: 'Formboost publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include forms, form-backend, html-forms, serverless, and static-sites.


  The Formboost catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Formboost''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Formboost Plans Pricing
  plan_count: 4
  slug: formboost-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Formboost Rate Limits
  slug: formboost-rate-limits
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 86.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- forms
- form-backend
- html-forms
- serverless
- static-sites
- react
- nextjs
- vue
- webhooks
- no-code
- developer-tools
- spam-filtering
website: https://dashboard.formboost.app
---
