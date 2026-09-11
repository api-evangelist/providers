---
access_model:
  confidence: low
  label: Pricing not published — provider retired
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - none
  trial: false
  try_now: false
api_count: 2
apis:
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: 'The Fusebit HTTP API managed and executed everything on the platform across two concurrent major versions on one host. v1 (Core, 49 operations) covered accounts, subscriptions, boundaries, serverless '
  name: Fusebit HTTP API
  slug: apis
artifact_total: 6
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fusebit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fusebit
- group: operate
  title: ''
  type: ChangeLog
  url: https://fivequarters.github.io/q5/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fusebit-changelog.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/fivequarters/q5
- group: auth
  title: ''
  type: Authentication
  url: authentication/fusebit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fusebit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fusebit-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fusebit-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fusebit-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fusebit-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/fusebit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fusebit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fusebit-cli.yml
- group: design
  title: ''
  type: Components
  url: components/fusebit-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fusebit-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fusebit-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fusebit-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fusebit-domain-security.yml
created: '2026-03-27'
description: 'Fusebit was a code-first, developer-facing embedded integration platform (embedded iPaaS) founded in Seattle in 2019, letting SaaS teams build, deploy and run third-party integrations inside their own products using serverless functions, managed OAuth connectors and an embeddable browser IDE. The company was acquired and the platform is retired: as of 2026-09-10 the domain fusebit.io is still registered but publishes no DNS A record, so the API, the developer documentation, the management portal and the asset CDN all fail to resolve. What survives is substantial and first-party — two published OpenAPI 3.0 contracts covering 89 operations, four dated release-note streams served from Fusebit''s own GitHub Pages, 101 npm packages under the @fusebit and @fusebit-int scopes, and 35 public repositories across the fusebit and fivequarters GitHub organizations. This profile is a historical record of a retired API, not a callable surface.'
finops:
- name: Fusebit Finops
  service_category: API
  slug: fusebit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fusebit.png
layout: provider
modified: '2026-09-10'
name: Fusebit
nav: Providers
network: true
overview: 'Fusebit publishes 1 API on the [APIs.io](https://apis.io/) network: HTTP API. Tagged areas include Developer Tools, Embedded iPaaS, Integration, Serverless, and OAuth.


  Fusebit''s developer surface includes changelog, authentication, CLI, and 16 more developer resources.'
plans:
- name: Fusebit Plans Pricing
  plan_count: 0
  slug: fusebit-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Fusebit Rate Limits
  slug: fusebit-rate-limits
security:
- kind: authentication
  name: Fusebit Authentication
  slug: fusebit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fusebit Domain Security
  slug: fusebit-domain-security
  summary_line: no transport/DNS hardening detected
slug: fusebit
tags:
- Developer Tools
- Embedded iPaaS
- Integration
- Serverless
- OAuth
- Acquired
---
