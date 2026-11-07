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
agent_readiness:
  band: human-only
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Account management operations
  name: Fusebit Accounts API
  slug: fusebit-accounts-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Boundary management operations
  name: Fusebit Boundaries API
  slug: fusebit-boundaries-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Client management operations
  name: Fusebit Clients API
  slug: fusebit-clients-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Management for external credentials
  name: Fusebit Connector API
  slug: fusebit-connector-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The Connector/Tags API from Fusebit — 3 operation(s) for connector/tags.
  name: Fusebit Connector/Tags API
  slug: fusebit-connector-tags-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Function management operations
  name: Fusebit Functions API
  slug: fusebit-functions-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: A managed credential for a remote service, on behalf of a customer
  name: Fusebit Identity API
  slug: fusebit-identity-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The Identity/Tags API from Fusebit — 3 operation(s) for identity/tags.
  name: Fusebit Identity/Tags API
  slug: fusebit-identity-tags-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: A fully configured integration for a customer
  name: Fusebit Install API
  slug: fusebit-install-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The Install/Tags API from Fusebit — 4 operation(s) for install/tags.
  name: Fusebit Install/Tags API
  slug: fusebit-install-tags-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The logic necessary to integrate between two services
  name: Fusebit Integration API
  slug: fusebit-integration-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The Integration/Tags API from Fusebit — 3 operation(s) for integration/tags.
  name: Fusebit Integration/Tags API
  slug: fusebit-integration-tags-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Issuer management operations
  name: Fusebit Issuers API
  slug: fusebit-issuers-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The Registry API from Fusebit — 1 operation(s) for registry.
  name: Fusebit Registry API
  slug: fusebit-registry-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: An active configuration phase for a customer
  name: Fusebit Session API
  slug: fusebit-session-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: The Storage API from Fusebit — 3 operation(s) for storage.
  name: Fusebit Storage API
  slug: fusebit-storage-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: Subscription management operations
  name: Fusebit Subscriptions API
  slug: fusebit-subscriptions-api
- baseURL: https://api.us-west-1.on.fusebit.io
  baseurl_source: declared
  description: User management operations
  name: Fusebit Users API
  slug: fusebit-users-api
artifact_total: 24
common:
- group: commercial
  href: https://artifacts.apis.io/fusebit/finops/fusebit-finops.yml
  title: ''
  type: FinOps
  url: finops/fusebit-finops.yml
- group: other
  href: https://artifacts.apis.io/fusebit/capabilities/fusebit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fusebit-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://fusebit.io
- group: other
  href: https://artifacts.apis.io/fusebit/overlays/fusebit-core-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fusebit-core-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fusebit/overlays/fusebit-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fusebit-integrations-overlay.yaml
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
  href: https://artifacts.apis.io/fusebit/changelog/fusebit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fusebit-changelog.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/fivequarters/q5
- group: auth
  href: https://artifacts.apis.io/fusebit/authentication/fusebit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fusebit-authentication.yml
- group: design
  href: https://artifacts.apis.io/fusebit/conventions/fusebit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fusebit-conventions.yml
- group: design
  href: https://artifacts.apis.io/fusebit/errors/fusebit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fusebit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fusebit/data-model/fusebit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fusebit-data-model.yml
- group: design
  href: https://artifacts.apis.io/fusebit/lifecycle/fusebit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fusebit-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fusebit/conformance/fusebit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fusebit-conformance.yml
- group: build
  href: https://artifacts.apis.io/fusebit/packages/fusebit-packages.yml
  title: ''
  type: Packages
  url: packages/fusebit-packages.yml
- group: build
  href: https://artifacts.apis.io/fusebit/packages/fusebit-packages.yml
  title: ''
  type: SDKs
  url: packages/fusebit-packages.yml
- group: build
  href: https://artifacts.apis.io/fusebit/cli/fusebit-cli.yml
  title: ''
  type: CLI
  url: cli/fusebit-cli.yml
- group: design
  href: https://artifacts.apis.io/fusebit/components/fusebit-components.yml
  title: ''
  type: Components
  url: components/fusebit-components.yml
- group: agent
  href: https://artifacts.apis.io/fusebit/llms/fusebit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fusebit-llms.txt
- group: operate
  href: https://artifacts.apis.io/fusebit/rate-limits/fusebit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fusebit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fusebit/plans/fusebit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fusebit-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/fusebit/security/fusebit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fusebit-domain-security.yml
created: '2026-03-27'
description: 'Fusebit was a code-first, developer-facing embedded integration platform (embedded iPaaS) founded in Seattle in 2019, letting SaaS teams build, deploy and run third-party integrations inside their own products using serverless functions, managed OAuth connectors and an embeddable browser IDE. The company was acquired and the platform is retired: as of 2026-09-10 the domain fusebit.io is still registered but publishes no DNS A record, so the API, the developer documentation, the management portal and the asset CDN all fail to resolve. What survives is substantial and first-party — two published OpenAPI 3.0 contracts covering 89 operations, four dated release-note streams served from Fusebit''s own GitHub Pages, 101 npm packages under the @fusebit and @fusebit-int scopes, and 35 public repositories across the fusebit and fivequarters GitHub organizations. This profile is a historical record of a retired API, not a callable surface.'
finops:
- has_sources: false
  method: generated
  name: Fusebit Finops
  primary_unit: request
  service_category: API
  slug: fusebit-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fusebit.png
layout: provider
modified: '2026-09-16'
name: Fusebit
nav: Providers
network: true
overview: 'Fusebit publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Boundaries API, Clients API, and 15 more. Tagged areas include Developer Tools, Embedded iPaaS, Integration, Serverless, and OAuth.


  The Fusebit catalog on APIs.io includes 1 Spectral governance ruleset.


  Fusebit''s developer surface includes changelog, authentication, CLI, and 21 more developer resources.'
plans:
- name: Fusebit Plans Pricing
  plan_count: 0
  slug: fusebit-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Fusebit Rate Limits
  slug: fusebit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Fusebit API Rules
  rule_count: 67
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 8
  slug: fusebit-rules
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Defunct
- Authentication
website: https://fusebit.io
---
