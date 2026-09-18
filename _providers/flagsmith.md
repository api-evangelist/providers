---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · 14-day trial on paid tiers
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Flagsmith Agentic Access
  operation_count: 35
  slug: flagsmith-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 2
apis:
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: The Flagsmith Flags API is the public-facing REST API that client-side and server-side SDKs use to retrieve feature flag values and remote configuration for environments and users. It uses a non-secre
  name: Flagsmith Flags API
  slug: flags-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage environments within a project. Environments represent deployment stages such as development, staging, and production.
  name: flagsmith Environments API
  slug: flagsmith-environments-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage feature flags within a project. Features can be toggled on or off and can have remote configuration values.
  name: flagsmith Features API
  slug: flagsmith-features-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage user identities within an environment. Identities represent individual users and their associated traits.
  name: flagsmith Identities API
  slug: flagsmith-identities-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage organisations within Flagsmith. Organisations are the top-level container for projects, users, and billing.
  name: flagsmith Organisations API
  slug: flagsmith-organisations-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage projects within an organisation. Projects contain environments and feature flags.
  name: flagsmith Projects API
  slug: flagsmith-projects-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage segments within a project. Segments define groups of users based on traits and rules for targeted flag delivery.
  name: flagsmith Segments API
  slug: flagsmith-segments-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Manage organisation users and their permissions within Flagsmith.
  name: flagsmith Users API
  slug: flagsmith-users-api
- baseURL: https://api.flagsmith.com/api/v1
  baseurl_source: declared
  description: Configure webhooks for environments and organisations to receive notifications about flag changes and audit log events.
  name: flagsmith Webhooks API
  slug: flagsmith-webhooks-api
artifact_total: 35
asyncapis:
- description: Flagsmith provides two types of webhooks for receiving event notifications. Environment webhooks automatically send flag evaluations for identified users whenever an identity's flags are evaluated via
  name: Flagsmith Webhook Events
  slug: flagsmith-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flagsmith Admin API
  slug: open-flagsmith-admin-api
- collection_type: open
  name: Flagsmith Admin Environments API
  slug: open-flagsmith-environments-api
- collection_type: open
  name: Flagsmith Admin Environments Features API
  slug: open-flagsmith-features-api
- collection_type: open
  name: Flagsmith Admin Environments Flags API
  slug: open-flagsmith-flags-api
- collection_type: open
  name: Flagsmith Admin Environments Identities API
  slug: open-flagsmith-identities-api
- collection_type: open
  name: Flagsmith Admin Environments Organisations API
  slug: open-flagsmith-organisations-api
- collection_type: open
  name: Flagsmith Admin Environments Projects API
  slug: open-flagsmith-projects-api
- collection_type: open
  name: Flagsmith Admin Environments Segments API
  slug: open-flagsmith-segments-api
- collection_type: open
  name: Flagsmith Admin Environments Users API
  slug: open-flagsmith-users-api
- collection_type: open
  name: Flagsmith Admin Environments Webhooks API
  slug: open-flagsmith-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://flagsmith.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/agentic-access/flagsmith-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flagsmith-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flagsmith-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/authentication/flagsmith-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flagsmith-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flagsmith
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flagsmith
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/json-ld/flagsmith-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flagsmith-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/json-schema/flagsmith-feature-flag-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/flagsmith-feature-flag-schema.json
- group: company
  title: ''
  type: Blog
  url: https://flagsmith.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flagsmith.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flagsmith.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flagsmith.com/integrating-with-flagsmith/flagsmith-api-overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flagsmith.com/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://docs.flagsmith.com/support/faq
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/hFhxNtXzgm
- group: commercial
  title: ''
  type: Pricing
  url: https://flagsmith.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.flagsmith.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flagsmith.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flagsmith.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/flagsmith/workspace/flagsmith/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flagsmith.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/changelog/flagsmith-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flagsmith-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/lifecycle/flagsmith-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/flagsmith-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/lifecycle/flagsmith-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flagsmith-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/packages/flagsmith-packages.yml
  title: ''
  type: Packages
  url: packages/flagsmith-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/packages/flagsmith-packages.yml
  title: ''
  type: SDKs
  url: packages/flagsmith-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/cli/flagsmith-cli.yml
  title: ''
  type: CLI
  url: cli/flagsmith-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/sandbox/flagsmith-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/flagsmith-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/mcp/flagsmith-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flagsmith-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/mcp/flagsmith-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/flagsmith-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/llms/flagsmith-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flagsmith-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/well-known/flagsmith-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flagsmith-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/scopes/flagsmith-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/flagsmith-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/conventions/flagsmith-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flagsmith-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/errors/flagsmith-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flagsmith-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/rate-limits/flagsmith-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flagsmith-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/plans/flagsmith-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flagsmith-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/data-model/flagsmith-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flagsmith-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/conformance/flagsmith-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flagsmith-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-trust-center.yml
  title: ''
  type: Compliance
  url: security/flagsmith-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flagsmith-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/flagsmith-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/security/flagsmith-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flagsmith-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/asyncapi/flagsmith-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/flagsmith-webhooks-asyncapi.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/finops/flagsmith-finops.yml
  title: ''
  type: FinOps
  url: finops/flagsmith-finops.yml
created: '2026-05-03'
description: 'Flagsmith is an open-source feature flag, remote configuration and experimentation platform built by Bullet Train Ltd. Teams use it to release features safely, run A/B and multivariate tests, and segment users without redeploying code, across web, mobile and server-side applications. It ships as a hosted cloud service on a global low-latency Edge API, as a private cloud deployment, or self-hosted on the customer''s own infrastructure, with the core product open source under BSD-3-Clause. Two public API surfaces back it: a non-secret SDK/Flags API for evaluating flags, and a 615-operation Management API that does everything the dashboard does. Flagsmith is OpenFeature compatible, publishes first-party SDKs for thirteen language ecosystems, and operates a remote MCP server exposing 54 tools to AI agents over OAuth.'
finops:
- name: Flagsmith Finops
  service_category: API
  slug: flagsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flagsmith.png
json_schemas:
- name: Flagsmith Feature Flag
  property_count: 12
  slug: flagsmith-feature-flag
jsonld:
- class_count: 0
  name: Flagsmith Context
  property_count: 9
  slug: flagsmith-context
layout: provider
mcp_servers:
- description: ''
  name: Flagsmith MCP Server
  slug: flagsmith-mcp-server
modified: '2026-09-17'
name: Flagsmith
nav: Providers
network: true
overview: 'Flagsmith publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Flags API, Environments API, Features API, and 6 more. Tagged areas include Feature Flags, Remote Config, Release Management, A/B Testing, and Experimentation.


  The Flagsmith catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Flagsmith''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 39 more developer resources.'
plans:
- name: Flagsmith Plans Pricing
  plan_count: 4
  slug: flagsmith-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Flagsmith Rate Limits
  slug: flagsmith-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Flagsmith API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: flagsmith-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Flagsmith API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: flagsmith-jsonschema-spectral-rules
scopes:
- name: Flagsmith Scopes
  scope_count: 0
  slug: flagsmith-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 80.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 73.5
    catalog_earned_first_party: 24.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 47.8
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 71.8
    developer_ergonomics: 85.1
    discoverability: 75.9
    operational_transparency: 92.1
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/screenshots/flagsmith-2026-06-20T181306.png
security:
- kind: authentication
  name: Flagsmith Authentication
  slug: flagsmith-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Flagsmith Domain Security
  slug: flagsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flagsmith Vulnerability Disclosure
  slug: flagsmith-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Flagsmith Trust Center
  slug: flagsmith-trust-center
  summary_line: read, note, how_to_verify
slug: flagsmith
tags:
- Feature Flags
- Remote Config
- Release Management
- A/B Testing
- Experimentation
- Segmentation
- Developer Tools
- DevOps
- Open-Source
- Software-as-a-Service
- MCP
- Agent Ready
website: https://flagsmith.com
---
