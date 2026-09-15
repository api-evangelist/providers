---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-09-14'
api_count: 2
apis:
- description: Programmatic access to Featureflip — projects, environments, feature flags, variations, targeting, segments, and SDK keys. Bearer-token auth (ffp_ personal / ffs_ service tokens).
  name: Management API
  slug: management-api
- description: High-performance feature flag evaluation service for SDKs, with client and SDK endpoints for evaluation, identify, streaming, flags, and events.
  name: Evaluation API
  slug: evaluation-api
- description: Documentation for the @featureflip/mcp server, a local stdio process run via npx that calls the Management API on your behalf using a bearer token.
  name: MCP Server (local)
  slug: mcp-server-local
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://featureflip.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/authentication/featureflip-authentication.yml
  title: ''
  type: Authentication
  url: authentication/featureflip-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/security/featureflip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/featureflip-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/packages/featureflip-packages.yml
  title: ''
  type: Packages
  url: packages/featureflip-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/packages/featureflip-packages.yml
  title: ''
  type: SDKs
  url: packages/featureflip-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/conventions/featureflip-conventions.yml
  title: ''
  type: Conventions
  url: conventions/featureflip-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/conventions/featureflip-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/featureflip-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/rate-limits/featureflip-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/featureflip-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/plans/featureflip-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/featureflip-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/changelog/featureflip-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/featureflip-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/lifecycle/featureflip-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/featureflip-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/errors/featureflip-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/featureflip-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/data-model/featureflip-data-model.yml
  title: ''
  type: DataModel
  url: data-model/featureflip-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/conformance/featureflip-conformance.yml
  title: ''
  type: Conformance
  url: conformance/featureflip-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/featureflip/refs/heads/main/rules/featureflip-spectral.yaml
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
layout: provider
mcp_servers:
- description: Local Model Context Protocol server that lets AI agents (Claude Code, Cursor, etc.) manage Featureflip flags by calling the Management API on the caller's behalf. It manages flag configuration; it doe
  name: Featureflip MCP Server
  slug: featureflip-mcp-server
modified: '2026-09-13'
name: Featureflip
nav: Providers
network: true
overview: 'Featureflip publishes 2 APIs on the [APIs.io](https://apis.io/) network: Management API and Evaluation API. Tagged areas include Feature Flags, Feature Management, feature flag cleanup, Progressive Delivery, and Experimentation.


  The Featureflip catalog on APIs.io includes 1 Spectral governance ruleset.


  Featureflip''s developer surface includes authentication, changelog, documentation, getting-started guide, pricing, engineering blog, support, and 19 more developer resources.'
plans:
- name: Featureflip Plans Pricing
  plan_count: 4
  slug: featureflip-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Featureflip Rate Limits
  slug: featureflip-rate-limits
rules:
- effective_rule_count: 41
  extends:
  - spectral:oas
  name: Featureflip API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: featureflip-spectral
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 33.3
    contract_quality: 33.3
    developer_ergonomics: 66.1
    discoverability: 72.2
    operational_transparency: 21.1
  previous_composite: 50.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Featureflip Authentication
  slug: featureflip-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Featureflip Domain Security
  slug: featureflip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
