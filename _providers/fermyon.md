---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.fermyon.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.akamai.com/products/akamai-functions — a different registrable domain (fermyon.com -> akamai.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Fermyon Agentic Access
  operation_count: 62
  slug: fermyon-agentic-access
  summary_line: 62 operations · 38 acting
api_count: 1
apis:
- description: Fermyon Wasm Functions is a multi-tenant, hosted, globally distributed engine for serverless functions running on Akamai Cloud. Developers author functions with the Spin Framework and deploy them to a
  name: Fermyon Wasm Functions
  slug: fermyon
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The accounts API from Fermyon — 1 operation(s) for accounts.
  name: Fermyon accounts API
  slug: fermyon-accounts-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The apps API from Fermyon — 6 operation(s) for apps.
  name: Fermyon apps API
  slug: fermyon-apps-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The auth-tokens API from Fermyon — 2 operation(s) for auth-tokens.
  name: Fermyon auth-tokens API
  slug: fermyon-auth-tokens-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The channels API from Fermyon — 6 operation(s) for channels.
  name: Fermyon channels API
  slug: fermyon-channels-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The custom-domains API from Fermyon — 1 operation(s) for custom-domains.
  name: Fermyon custom-domains API
  slug: fermyon-custom-domains-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The device-codes API from Fermyon — 3 operation(s) for device-codes.
  name: Fermyon device-codes API
  slug: fermyon-device-codes-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The key-value-pairs API from Fermyon — 1 operation(s) for key-value-pairs.
  name: Fermyon key-value-pairs API
  slug: fermyon-key-value-pairs-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The key-value-stores API from Fermyon — 4 operation(s) for key-value-stores.
  name: Fermyon key-value-stores API
  slug: fermyon-key-value-stores-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The oci API from Fermyon — 4 operation(s) for oci.
  name: Fermyon oci API
  slug: fermyon-oci-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The payments API from Fermyon — 3 operation(s) for payments.
  name: Fermyon payments API
  slug: fermyon-payments-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The personal-access-tokens API from Fermyon — 2 operation(s) for personal-access-tokens.
  name: Fermyon personal-access-tokens API
  slug: fermyon-personal-access-tokens-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The revisions API from Fermyon — 1 operation(s) for revisions.
  name: Fermyon revisions API
  slug: fermyon-revisions-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The sql-databases API from Fermyon — 5 operation(s) for sql-databases.
  name: Fermyon sql-databases API
  slug: fermyon-sql-databases-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: spec
  description: The variable-pairs API from Fermyon — 1 operation(s) for variable-pairs.
  name: Fermyon variable-pairs API
  slug: fermyon-variable-pairs-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fermyon Cloud accounts API
  slug: open-fermyon-accounts-api
- collection_type: open
  name: Fermyon Cloud accounts apps API
  slug: open-fermyon-apps-api
- collection_type: open
  name: Fermyon Cloud accounts auth-tokens API
  slug: open-fermyon-auth-tokens-api
- collection_type: open
  name: Fermyon Cloud accounts channels API
  slug: open-fermyon-channels-api
- collection_type: open
  name: Fermyon Cloud accounts custom-domains API
  slug: open-fermyon-custom-domains-api
- collection_type: open
  name: Fermyon Cloud accounts device-codes API
  slug: open-fermyon-device-codes-api
- collection_type: open
  name: Fermyon Cloud accounts key-value-pairs API
  slug: open-fermyon-key-value-pairs-api
- collection_type: open
  name: Fermyon Cloud accounts key-value-stores API
  slug: open-fermyon-key-value-stores-api
- collection_type: open
  name: Fermyon Cloud accounts oci API
  slug: open-fermyon-oci-api
- collection_type: open
  name: Fermyon Cloud accounts payments API
  slug: open-fermyon-payments-api
- collection_type: open
  name: Fermyon Cloud accounts personal-access-tokens API
  slug: open-fermyon-personal-access-tokens-api
- collection_type: open
  name: Fermyon Cloud accounts revisions API
  slug: open-fermyon-revisions-api
- collection_type: open
  name: Fermyon Cloud accounts sql-databases API
  slug: open-fermyon-sql-databases-api
- collection_type: open
  name: Fermyon Cloud accounts variable-pairs API
  slug: open-fermyon-variable-pairs-api
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
random_paper: 12
rate_limits:
- limit_count: 5
  name: Fermyon Rate Limits
  slug: fermyon-rate-limits
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 1.6
    developer_ergonomics: 39.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
