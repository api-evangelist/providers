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
    agent_skills: derived
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
  score: 20.7
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Fermyon Agentic Access
  operation_count: 62
  slug: fermyon-agentic-access
  summary_line: 62 operations · 38 acting
api_count: 2
apis:
- description: Fermyon Wasm Functions is a multi-tenant, hosted, globally distributed engine for serverless functions running on Akamai Cloud. Developers author functions with the Spin Framework and deploy them to a
  name: Fermyon Wasm Functions
  slug: fermyon
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The accounts API from Fermyon — 1 operation(s) for accounts.
  name: Fermyon accounts API
  slug: fermyon-accounts-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The apps API from Fermyon — 6 operation(s) for apps.
  name: Fermyon apps API
  slug: fermyon-apps-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The auth-tokens API from Fermyon — 2 operation(s) for auth-tokens.
  name: Fermyon auth-tokens API
  slug: fermyon-auth-tokens-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The channels API from Fermyon — 6 operation(s) for channels.
  name: Fermyon channels API
  slug: fermyon-channels-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The custom-domains API from Fermyon — 1 operation(s) for custom-domains.
  name: Fermyon custom-domains API
  slug: fermyon-custom-domains-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The device-codes API from Fermyon — 3 operation(s) for device-codes.
  name: Fermyon device-codes API
  slug: fermyon-device-codes-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The key-value-pairs API from Fermyon — 1 operation(s) for key-value-pairs.
  name: Fermyon key-value-pairs API
  slug: fermyon-key-value-pairs-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The key-value-stores API from Fermyon — 4 operation(s) for key-value-stores.
  name: Fermyon key-value-stores API
  slug: fermyon-key-value-stores-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The oci API from Fermyon — 4 operation(s) for oci.
  name: Fermyon oci API
  slug: fermyon-oci-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The payments API from Fermyon — 3 operation(s) for payments.
  name: Fermyon payments API
  slug: fermyon-payments-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The personal-access-tokens API from Fermyon — 2 operation(s) for personal-access-tokens.
  name: Fermyon personal-access-tokens API
  slug: fermyon-personal-access-tokens-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The revisions API from Fermyon — 1 operation(s) for revisions.
  name: Fermyon revisions API
  slug: fermyon-revisions-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
  description: The sql-databases API from Fermyon — 5 operation(s) for sql-databases.
  name: Fermyon sql-databases API
  slug: fermyon-sql-databases-api
- baseURL: https://cloud.fermyon.com
  baseurl_source: declared
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
- group: build
  title: ''
  type: Packages
  url: packages/fermyon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fermyon-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fermyon-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fermyon-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fermyon-security.txt
- group: auth
  title: ''
  type: Security
  url: security/fermyon-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fermyon-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fermyon-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fermyon-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fermyon-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fermyon-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fermyon-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fermyon-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fermyon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fermyon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fermyon-finops.yml
- group: build
  title: ''
  type: Postman
  url: collections/fermyon.postman_collection.json
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fermyon.com/cloud/rest-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fermyon.com/
- group: start
  title: ''
  type: Quickstart
  url: https://developer.fermyon.com/cloud/quickstart
- group: operate
  title: ''
  type: Support
  url: https://developer.fermyon.com/cloud/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fermyon.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.fermyon.com/?signup
- group: start
  title: ''
  type: Login
  url: https://cloud.fermyon.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fermyon.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fermyon.com/privacy-policy
created: '2025-02-08'
description: Fermyon Wasm Functions is a multi-tenant, hosted, globally distributed engine for serverless functions running on Akamai Cloud, the most distributed cloud network. Fermyon is the company behind the Spin Framework and SpinKube, providing tools and runtimes for building and operating WebAssembly-based serverless applications.
finops:
- name: Fermyon Finops
  service_category: API
  slug: fermyon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fermyon.png
layout: provider
modified: '2026-09-09'
name: Fermyon
nav: Providers
network: true
overview: 'Fermyon publishes 14 APIs on the [APIs.io](https://apis.io/) network, including accounts API, apps API, auth-tokens API, and 11 more. Tagged areas include Compute, Functions, WebAssembly, Serverless, and Edge Computing.


  Fermyon''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, CLI, changelog, and 31 more developer resources.'
plans:
- name: Fermyon Plans Pricing
  plan_count: 4
  slug: fermyon-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 15
  name: Fermyon Rate Limits
  slug: fermyon-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.6
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 1.6
    developer_ergonomics: 67.3
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 17.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
- Edge Computing
- Serverless Functions
- Spin
- Developer Tools
website: https://www.fermyon.com/
---
