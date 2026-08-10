---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Fermyon Agentic Access
  operation_count: 62
  slug: fermyon-agentic-access
  summary_line: 62 operations · 38 acting
api_count: 15
apis:
- description: Fermyon Wasm Functions is a multi-tenant, hosted, globally distributed engine for serverless functions running on Akamai Cloud. Developers author functions with the Spin Framework and deploy them to a
  name: Fermyon Wasm Functions
  slug: fermyon
- description: The accounts API from Fermyon — 1 operation(s) for accounts.
  name: Fermyon accounts API
  slug: fermyon-accounts-api
- description: The apps API from Fermyon — 6 operation(s) for apps.
  name: Fermyon apps API
  slug: fermyon-apps-api
- description: The auth-tokens API from Fermyon — 2 operation(s) for auth-tokens.
  name: Fermyon auth-tokens API
  slug: fermyon-auth-tokens-api
- description: The channels API from Fermyon — 6 operation(s) for channels.
  name: Fermyon channels API
  slug: fermyon-channels-api
- description: The custom-domains API from Fermyon — 1 operation(s) for custom-domains.
  name: Fermyon custom-domains API
  slug: fermyon-custom-domains-api
- description: The device-codes API from Fermyon — 3 operation(s) for device-codes.
  name: Fermyon device-codes API
  slug: fermyon-device-codes-api
- description: The key-value-pairs API from Fermyon — 1 operation(s) for key-value-pairs.
  name: Fermyon key-value-pairs API
  slug: fermyon-key-value-pairs-api
- description: The key-value-stores API from Fermyon — 4 operation(s) for key-value-stores.
  name: Fermyon key-value-stores API
  slug: fermyon-key-value-stores-api
- description: The oci API from Fermyon — 4 operation(s) for oci.
  name: Fermyon oci API
  slug: fermyon-oci-api
- description: The payments API from Fermyon — 3 operation(s) for payments.
  name: Fermyon payments API
  slug: fermyon-payments-api
- description: The personal-access-tokens API from Fermyon — 2 operation(s) for personal-access-tokens.
  name: Fermyon personal-access-tokens API
  slug: fermyon-personal-access-tokens-api
- description: The revisions API from Fermyon — 1 operation(s) for revisions.
  name: Fermyon revisions API
  slug: fermyon-revisions-api
- description: The sql-databases API from Fermyon — 5 operation(s) for sql-databases.
  name: Fermyon sql-databases API
  slug: fermyon-sql-databases-api
- description: The variable-pairs API from Fermyon — 1 operation(s) for variable-pairs.
  name: Fermyon variable-pairs API
  slug: fermyon-variable-pairs-api
artifact_total: 23
collections:
- collection_type: open
  name: Fermyon Cloud API
  slug: open-fermyon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fermyon-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fermyon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fermyon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fermyon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fermyon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fermyon
- group: start
  title: ''
  type: Portal
  url: https://developer.fermyon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fermyon.com/spin/v3/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fermyon.com/spin/v3/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.fermyon.com/blog/index
- group: company
  title: ''
  type: Website
  url: https://www.fermyon.com/
created: '2025-02-08'
description: Fermyon Wasm Functions is a multi-tenant, hosted, globally distributed engine for serverless functions running on Akamai Cloud, the most distributed cloud network. Fermyon is the company behind the Spin Framework and SpinKube, providing tools and runtimes for building and operating WebAssembly-based serverless applications.
finops:
- name: Fermyon Finops
  service_category: API
  slug: fermyon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fermyon.png
layout: provider
modified: '2026-04-28'
name: Fermyon
nav: Providers
network: true
overview: 'Fermyon publishes 14 APIs on the [APIs.io](https://apis.io/) network, including accounts API, apps API, auth-tokens API, and 11 more. Tagged areas include Compute, Functions, WebAssembly, and Serverless.


  Fermyon''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Fermyon Plans Pricing
  plan_count: 3
  slug: fermyon-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Fermyon Rate Limits
  slug: fermyon-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.5
    developer_ergonomics: 41.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fermyon/refs/heads/main/screenshots/fermyon-2026-06-20T181140.png
security:
- kind: authentication
  name: Fermyon Authentication
  slug: fermyon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fermyon Domain Security
  slug: fermyon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fermyon Vulnerability Disclosure
  slug: fermyon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fermyon
tags:
- Compute
- Functions
- WebAssembly
- Serverless
website: https://www.fermyon.com/
---
