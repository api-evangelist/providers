---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 89
  human_in_the_loop: 2
  name: Switstack Agentic Access
  operation_count: 128
  slug: switstack-agentic-access
  summary_line: 128 operations · 89 acting · 2 human-in-the-loop
api_count: 4
apis:
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Auth API from Switstack — 3 operation(s) for auth.
  name: Switstack Auth API
  slug: switstack-auth-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The BOM API from Switstack — 6 operation(s) for bom.
  name: Switstack BOM API
  slug: switstack-bom-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Config API from Switstack — 29 operation(s) for config.
  name: Switstack Config API
  slug: switstack-config-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Parser API from Switstack — 4 operation(s) for parser.
  name: Switstack Parser API
  slug: switstack-parser-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Payment API from Switstack — 4 operation(s) for payment.
  name: Switstack Payment API
  slug: switstack-payment-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Suite API from Switstack — 2 operation(s) for suite.
  name: Switstack Suite API
  slug: switstack-suite-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Test API from Switstack — 5 operation(s) for test.
  name: Switstack Test API
  slug: switstack-test-api
- baseURL: https://switcloud.switstack.io/
  baseurl_source: declared
  description: The Validation API from Switstack — 6 operation(s) for validation.
  name: Switstack Validation API
  slug: switstack-validation-api
arazzos:
- description: Authenticate, build the Merchant -> Store -> POI estate, assemble a minimum EMV configuration, and bundle it into the POIConfig a terminal fetches at runtime. This is steps 1 and 2 of the Switcloud ge
  name: Onboard a Switcloud terminal
  slug: switstack-onboard-a-terminal
- description: Authenticate, discover a suite, inspect a test and its scope, validate a custom suite, then run a selection and consume the Server-Sent Events stream. Every operationId is verified verbatim against op
  name: Verify and run a Swittest EMV test suite
  slug: switstack-run-a-test-suite
- description: 'The backend half of a Switcloud card-present transaction: authenticate as a basic/machine user, create a Payment against a POI and POIConfig, wait for the on-device leg, then read the completed transa'
  name: Take a Switcloud payment and reconcile it
  slug: switstack-take-a-payment
artifact_total: 17
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/switstack-switcloud-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/switstack-swittest-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/switstack-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/switstack-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.switstack.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.switstack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.switstack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.switstack.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.switstack.io/switcloud/getting_started/
- group: company
  title: ''
  type: Blog
  url: https://www.switstack.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.switstack.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/switstack
- group: operate
  title: ''
  type: Support
  url: https://github.com/switstack/switstack-issues
- group: start
  title: ''
  type: SignUp
  url: https://www.switstack.io/get-started
- group: commercial
  title: ''
  type: License
  url: https://docs.switstack.io/moka/license/
- group: auth
  title: ''
  type: Authentication
  url: authentication/switstack-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/switstack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/switstack-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/switstack-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/switstack-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/switstack-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/switstack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/switstack-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/switstack-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/switstack-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/switstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/switstack-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/switstack-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/switstack-domain-security.yml
- group: build
  title: ''
  type: Examples
  url: examples/switstack-code-samples.yml
- group: build
  title: ''
  type: Examples
  url: https://docs.switstack.io/switcloud/examples/
- group: design
  title: ''
  type: Arazzo
  url: arazzo/switstack-onboard-a-terminal.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/switstack-take-a-payment.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/switstack-run-a-test-suite.yml
created: '2026-08-17'
description: 'Switstack is a payment infrastructure company building software-defined EMV acceptance for physical retail. It ships three products: switstack moka, a source-available EMV Level 2 kernel stack with brand Letters of Compliance; Switcloud, a hosted "universal compliance infrastructure" that abstracts EMV L2 execution and centralizes estate (organization/merchant/store/POI) and EMV configuration (CAPK, BIN, CRL, kernel parameter) management behind a REST API; and Swittest, a managed EMV functional test-automation service for labs and developers certifying card-present applications. The platform is terminal-agnostic and L2-stack agnostic — one L3 application runs across Android COTS tap-to-pay devices and PCI-PTS terminals via a GLA adapter layer — and Switstack supplies pre-certified PCI MPoC software and service components to shrink certification scope.'
image: https://cdn.prod.website-files.com/677bdd3fa1a7f9a1d8e76d2e/67879a394c57fb7c99783259_switstack_meta.png
layout: provider
modified: '2026-08-17'
name: Switstack
nav: Providers
network: true
overview: 'Switstack publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, BOM API, Config API, and 5 more. Tagged areas include Company, Fintech Insurtech, Payments, EMV, and emv-level-2.


  Switstack''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 28 more developer resources.'
plans:
- name: Switstack Plans Pricing
  plan_count: 0
  slug: switstack-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Switstack Rate Limits
  slug: switstack-rate-limits
scopes:
- name: Switstack Scopes
  scope_count: 0
  slug: switstack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 80.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/switstack/refs/heads/main/screenshots/switstack-2026-09-02T161419.png
security:
- kind: authentication
  name: Switstack Authentication
  slug: switstack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Switstack Domain Security
  slug: switstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: switstack
tags:
- Company
- Fintech Insurtech
- Payments
- EMV
- emv-level-2
- Card Present
- Point-of-Sale
- SoftPOS
- Tap to Pay
- Payment Terminals
- In-Store Payments
- pci-mpoc
- certification-testing
- Retail Payments
- estate-management
website: https://www.switstack.io/
---
