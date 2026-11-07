---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 85
  human_in_the_loop: 1
  name: Switstack Agentic Access
  operation_count: 125
  slug: switstack-agentic-access
  summary_line: 125 operations · 85 acting · 1 human-in-the-loop
api_count: 3
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
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/switstack/capabilities/switstack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/switstack-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/switstack/overlays/switstack-switcloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/switstack-switcloud-overlay.yaml
- group: other
  href: https://artifacts.apis.io/switstack/overlays/switstack-swittest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/switstack-swittest-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/switstack/agentic-access/switstack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/switstack-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/switstack/scopes/switstack-scopes.yml
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
  href: https://artifacts.apis.io/switstack/authentication/switstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/switstack-authentication.yml
- group: design
  href: https://artifacts.apis.io/switstack/conventions/switstack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/switstack-conventions.yml
- group: design
  href: https://artifacts.apis.io/switstack/errors/switstack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/switstack-problem-types.yml
- group: design
  href: https://artifacts.apis.io/switstack/data-model/switstack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/switstack-data-model.yml
- group: design
  href: https://artifacts.apis.io/switstack/lifecycle/switstack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/switstack-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/switstack/conformance/switstack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/switstack-conformance.yml
- group: build
  href: https://artifacts.apis.io/switstack/packages/switstack-packages.yml
  title: ''
  type: Packages
  url: packages/switstack-packages.yml
- group: build
  href: https://artifacts.apis.io/switstack/packages/switstack-packages.yml
  title: ''
  type: SDKs
  url: packages/switstack-packages.yml
- group: build
  href: https://artifacts.apis.io/switstack/cli/switstack-cli.yml
  title: ''
  type: CLI
  url: cli/switstack-cli.yml
- group: start
  href: https://artifacts.apis.io/switstack/sandbox/switstack-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/switstack-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/switstack/plans/switstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/switstack-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/switstack/rate-limits/switstack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/switstack-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/switstack/llms/switstack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/switstack-llms.txt
- group: agent
  href: https://artifacts.apis.io/switstack/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/switstack/security/switstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/switstack-domain-security.yml
- group: build
  href: https://artifacts.apis.io/switstack/examples/switstack-code-samples.yml
  title: ''
  type: Examples
  url: examples/switstack-code-samples.yml
- group: build
  title: ''
  type: Examples
  url: https://docs.switstack.io/switcloud/examples/
- group: design
  href: https://artifacts.apis.io/switstack/arazzo/switstack-onboard-a-terminal.yml
  title: ''
  type: Arazzo
  url: arazzo/switstack-onboard-a-terminal.yml
- group: design
  href: https://artifacts.apis.io/switstack/arazzo/switstack-take-a-payment.yml
  title: ''
  type: Arazzo
  url: arazzo/switstack-take-a-payment.yml
- group: design
  href: https://artifacts.apis.io/switstack/arazzo/switstack-run-a-test-suite.yml
  title: ''
  type: Arazzo
  url: arazzo/switstack-run-a-test-suite.yml
created: '2026-08-17'
description: 'Switstack is a payment infrastructure company building software-defined EMV acceptance for physical retail. It ships three products: switstack moka, a source-available EMV Level 2 kernel stack with brand Letters of Compliance; Switcloud, a hosted "universal compliance infrastructure" that abstracts EMV L2 execution and centralizes estate (organization/merchant/store/POI) and EMV configuration (CAPK, BIN, CRL, kernel parameter) management behind a REST API; and Swittest, a managed EMV functional test-automation service for labs and developers certifying card-present applications. The platform is terminal-agnostic and L2-stack agnostic — one L3 application runs across Android COTS tap-to-pay devices and PCI-PTS terminals via a GLA adapter layer — and Switstack supplies pre-certified PCI MPoC software and service components to shrink certification scope.'
finops:
- has_sources: true
  method: derived
  name: Switstack Finops
  primary_unit: ''
  service_category: ''
  slug: switstack-finops
  template: true
image: https://cdn.prod.website-files.com/677bdd3fa1a7f9a1d8e76d2e/67879a394c57fb7c99783259_switstack_meta.png
layout: provider
modified: '2026-08-17'
name: Switstack
nav: Providers
network: true
overview: 'Switstack publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, BOM API, Config API, and 5 more. Tagged areas include Company, Fintech Insurtech, Payments, EMV, and emv-level-2.


  The Switstack catalog on APIs.io includes 1 Spectral governance ruleset.


  Switstack''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 29 more developer resources.'
plans:
- name: Switstack Plans Pricing
  plan_count: 0
  slug: switstack-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Switstack Rate Limits
  slug: switstack-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Switstack API Rules
  rule_count: 53
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 6
  slug: switstack-rules
scopes:
- name: Switstack Scopes
  scope_count: 0
  slug: switstack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 31.8
    contract_quality: 44.3
    developer_ergonomics: 80.4
    discoverability: 71.4
    operational_transparency: 2.6
  previous_composite: 41.1
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
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/switstack/switstack-2026-09-02T161419.png
security:
- kind: authentication
  name: Switstack Authentication
  slug: switstack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Switstack Domain Security
  slug: switstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: Authenticate against a Switstack API
  slug: switstack-authenticate
- name: Build a Switcloud merchant estate
  slug: switstack-build-the-estate
- name: Configure EMV for a Switcloud terminal
  slug: switstack-configure-emv-for-a-terminal
- name: Create and reconcile a Switcloud payment
  slug: switstack-create-a-payment
- name: Run EMV tests with Swittest
  slug: switstack-run-emv-tests
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
