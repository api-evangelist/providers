---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Documentation for the @featureflip/mcp server, a local stdio process run via npx that calls the Management API on your behalf using a bearer token.
  name: MCP Server (local)
  slug: mcp-server-local
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: Client SDK endpoints for browser-side feature flag evaluation. All endpoints require a valid Client SDK key passed via the Authorization header. Unlike server SDK endpoints, these evaluate flags serve
  name: Featureflip Client SDK API
  slug: featureflip-client-sdk-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: Environments within a resolved organization + project — one level deeper than ProjectsController. Every route here carries `{org}`, so ResolveTenantFilter has already resolved + access-checked it befo
  name: Featureflip Environments API
  slug: featureflip-environments-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: 'Feature flags within a resolved organization + project — mirrors EnvironmentsController''s resolve-then-dispatch shape one level deeper. `{project}` is resolved key-or-guid, scoped to the resolved org '
  name: Featureflip Feature Flags API
  slug: featureflip-feature-flags-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: 'The caller''s own identity. This route has no `{org}` segment, so ResolveTenantFilter is a pass-through here — the caller is read entirely from the authenticated principal (via GetCurrentUserQuery for '
  name: Featureflip Me API
  slug: featureflip-me-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: The caller's organizations. `List` has no `{org}` segment (pass-through tenant filter) and dispatches ListOrganizationsQuery, which already scopes to the caller's own memberships. `Get` carries `{org}
  name: Featureflip Organizations API
  slug: featureflip-organizations-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: Projects within a resolved organization. Every route here carries `{org}`, so ResolveTenantFilter has already resolved + access-checked it before any action runs — dispatched commands/queries always u
  name: Featureflip Projects API
  slug: featureflip-projects-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: SDK keys within a resolved organization + project + environment — one level deeper than EnvironmentsController. Every action resolves `{project}` (key-or-guid, scoped to the resolved org, with the ser
  name: Featureflip SDK Keys API
  slug: featureflip-sdk-keys-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: SDK endpoints for feature flag evaluation and configuration retrieval. All endpoints require a valid SDK key passed via the Authorization header.
  name: Featureflip Server SDK API
  slug: featureflip-server-sdk-api
- baseURL: https://api.featureflip.io
  baseurl_source: declared
  description: 'User segments within a resolved organization + project — mirrors EnvironmentsController''s resolve-then-dispatch shape one level deeper. `{project}` is resolved key-or-guid, scoped to the resolved org '
  name: Featureflip User Segments API
  slug: featureflip-user-segments-api
- baseURL: https://featureflip.io/docs/integrations/mcp/
  baseurl_source: declared
  description: 'Manage outbound webhook subscriptions: where configuration-change events are sent, which events and projects they cover, their signing secrets, and their delivery log.'
  name: Featureflip Webhooks API
  slug: featureflip-webhooks-api
artifact_total: 22
common:
- group: other
  href: https://artifacts.apis.io/featureflip/capabilities/featureflip-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/featureflip-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/featureflip/overlays/featureflip-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/featureflip-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/featureflip/overlays/featureflip-evaluation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/featureflip-evaluation-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://featureflip.io/
- group: auth
  href: https://artifacts.apis.io/featureflip/authentication/featureflip-authentication.yml
  title: ''
  type: Authentication
  url: authentication/featureflip-authentication.yml
- group: auth
  href: https://artifacts.apis.io/featureflip/security/featureflip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/featureflip-domain-security.yml
- group: build
  href: https://artifacts.apis.io/featureflip/packages/featureflip-packages.yml
  title: ''
  type: Packages
  url: packages/featureflip-packages.yml
- group: build
  href: https://artifacts.apis.io/featureflip/packages/featureflip-packages.yml
  title: ''
  type: SDKs
  url: packages/featureflip-packages.yml
- group: design
  href: https://artifacts.apis.io/featureflip/conventions/featureflip-conventions.yml
  title: ''
  type: Conventions
  url: conventions/featureflip-conventions.yml
- group: design
  href: https://artifacts.apis.io/featureflip/conventions/featureflip-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/featureflip-conventions.yml
- group: operate
  href: https://artifacts.apis.io/featureflip/rate-limits/featureflip-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/featureflip-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/featureflip/plans/featureflip-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/featureflip-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/featureflip/changelog/featureflip-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/featureflip-changelog.yml
- group: design
  href: https://artifacts.apis.io/featureflip/lifecycle/featureflip-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/featureflip-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/featureflip/errors/featureflip-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/featureflip-problem-types.yml
- group: design
  href: https://artifacts.apis.io/featureflip/data-model/featureflip-data-model.yml
  title: ''
  type: DataModel
  url: data-model/featureflip-data-model.yml
- group: design
  href: https://artifacts.apis.io/featureflip/conformance/featureflip-conformance.yml
  title: ''
  type: Conformance
  url: conformance/featureflip-conformance.yml
- group: agent
  href: https://artifacts.apis.io/featureflip/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/featureflip/rules/featureflip-spectral.yaml
  title: ''
  type: Rules
  url: rules/featureflip-spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://featureflip.io/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://featureflip.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://featureflip.io/docs/quickstart/javascript/
- group: commercial
  title: ''
  type: Pricing
  url: https://featureflip.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://featureflip.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://featureflip.io/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.featureflip.io/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canopy-labs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://featureflip.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://featureflip.io/privacy/
created: '2026-09-12'
description: Feature flag platform with automated dead-flag cleanup (via a GitHub Action), flat pricing, and API-first, agent-native surfaces. Exposes a Management REST API and a high-performance Evaluation API, both with public OpenAPI contracts, plus official SDKs for 13 languages, OpenFeature providers, a Terraform provider, and a local MCP server.
finops:
- has_sources: true
  method: derived
  name: Featureflip Finops
  primary_unit: subscription
  service_category: ''
  slug: featureflip-finops
  template: false
layout: provider
mcp_servers:
- description: Local Model Context Protocol server that lets AI agents (Claude Code, Cursor, etc.) manage Featureflip flags by calling the Management API on the caller's behalf. It manages flag configuration; it doe
  name: Featureflip MCP Server
  slug: featureflip-mcp-server
modified: '2026-09-13'
name: Featureflip
nav: Providers
network: true
overview: 'Featureflip publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Client SDK API, Environments API, Feature Flags API, and 8 more. Tagged areas include Feature Flags, Feature Management, feature flag cleanup, Progressive Delivery, and Experimentation.


  The Featureflip catalog on APIs.io includes 1 Spectral governance ruleset.


  Featureflip''s developer surface includes authentication, changelog, documentation, getting-started guide, pricing, engineering blog, support, and 22 more developer resources.'
plans:
- name: Featureflip Plans Pricing
  plan_count: 8
  slug: featureflip-plans-pricing
- name: Featureflip Price Estimates
  plan_count: 0
  slug: featureflip-price-estimates
random_paper: 23
rate_limits:
- limit_count: 0
  name: Featureflip Rate Limits
  slug: featureflip-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Featureflip — spectral rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: featureflip-spectral
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.3
    catalog_earned_first_party: 12.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 49.2
    developer_ergonomics: 66.1
    discoverability: 68.3
    operational_transparency: 18.4
  previous_composite: 51.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 42.1
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/featureflip/featureflip-2026-10-11T104418.png
security:
- kind: authentication
  name: Featureflip Authentication
  slug: featureflip-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Featureflip Domain Security
  slug: featureflip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: dead-flag-cleanup
  slug: featureflip-dead-flag-cleanup
- name: progressive-rollout
  slug: featureflip-progressive-rollout
- name: targeting-rule
  slug: featureflip-targeting-rule
slug: featureflip
tags:
- Feature Flags
- Feature Management
- feature flag cleanup
- Progressive Delivery
- Experimentation
- feature flags as code
- OpenFeature
- MCP
- Developer Tools
- DevOps/CI-CD
website: https://featureflip.io/
---
