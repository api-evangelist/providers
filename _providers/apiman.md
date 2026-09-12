---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 76
  human_in_the_loop: 2
  name: Apiman Agentic Access
  operation_count: 177
  slug: apiman-agentic-access
  summary_line: 177 operations · 76 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Apiman is an open source API management platform with a developer portal, API gateway, and management UI supporting policies, plans, organizations, multi-tenancy, and extensible Java-based plugin arch
  name: Apiman
  slug: apiman
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Actions API from Apiman — 2 operation(s) for actions.
  name: Apiman Actions API
  slug: apiman-actions-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Blobs API from Apiman — 2 operation(s) for blobs.
  name: Apiman Blobs API
  slug: apiman-blobs-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Developers API from Apiman — 8 operation(s) for developers.
  name: Apiman Developers API
  slug: apiman-developers-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Devportal API from Apiman — 22 operation(s) for devportal.
  name: Apiman Devportal API
  slug: apiman-devportal-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Downloads API from Apiman — 1 operation(s) for downloads.
  name: Apiman Downloads API
  slug: apiman-downloads-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Events API from Apiman — 1 operation(s) for events.
  name: Apiman Events API
  slug: apiman-events-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Experimental API from Apiman — 22 operation(s) for experimental.
  name: Apiman Experimental API
  slug: apiman-experimental-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Gateways API from Apiman — 3 operation(s) for gateways.
  name: Apiman Gateways API
  slug: apiman-gateways-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Organizations API from Apiman — 57 operation(s) for organizations.
  name: Apiman Organizations API
  slug: apiman-organizations-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Plugins API from Apiman — 5 operation(s) for plugins.
  name: Apiman Plugins API
  slug: apiman-plugins-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Policy Definitions API from Apiman — 2 operation(s) for policy definitions.
  name: Apiman Policy Definitions API
  slug: apiman-policy-definitions-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Roles API from Apiman — 2 operation(s) for roles.
  name: Apiman Roles API
  slug: apiman-roles-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Search API from Apiman — 7 operation(s) for search.
  name: Apiman Search API
  slug: apiman-search-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The System API from Apiman — 3 operation(s) for system.
  name: Apiman System API
  slug: apiman-system-api
- baseURL: https://{apiman_host}/apiman
  baseurl_source: declared
  description: The Users API from Apiman — 13 operation(s) for users.
  name: Apiman Users API
  slug: apiman-users-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Manager REST Actions API
  slug: open-apiman-actions-api
- collection_type: open
  name: API Manager REST Actions Blobs API
  slug: open-apiman-blobs-api
- collection_type: open
  name: API Manager REST Actions Developers API
  slug: open-apiman-developers-api
- collection_type: open
  name: API Manager REST Actions Devportal API
  slug: open-apiman-devportal-api
- collection_type: open
  name: API Manager REST Actions Downloads API
  slug: open-apiman-downloads-api
- collection_type: open
  name: API Manager REST Actions Events API
  slug: open-apiman-events-api
- collection_type: open
  name: API Manager REST Actions Experimental API
  slug: open-apiman-experimental-api
- collection_type: open
  name: API Manager REST Actions Gateways API
  slug: open-apiman-gateways-api
- collection_type: open
  name: API Manager REST Actions Organizations API
  slug: open-apiman-organizations-api
- collection_type: open
  name: API Manager REST Actions Plugins API
  slug: open-apiman-plugins-api
- collection_type: open
  name: API Manager REST Actions Policy Definitions API
  slug: open-apiman-policy-definitions-api
- collection_type: open
  name: API Manager REST Actions Roles API
  slug: open-apiman-roles-api
- collection_type: open
  name: API Manager REST Actions Search API
  slug: open-apiman-search-api
- collection_type: open
  name: API Manager REST Actions System API
  slug: open-apiman-system-api
- collection_type: open
  name: API Manager REST Actions Users API
  slug: open-apiman-users-api
- collection_type: open
  name: API Manager REST API
  slug: open-apiman
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apiman/apiman/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apiman/apiman/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apiman/apiman/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apiman/apiman/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apiman/apiman/blob/master/LICENSE
- group: operate
  title: ''
  type: Support
  url: https://www.apiman.io/support.html
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apiman-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apiman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apiman.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiman
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apiman/apiman
- group: company
  title: ''
  type: Blog
  url: https://www.apiman.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.apiman.io/apiman-docs/guides/latest/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.apiman.io/rest-api-docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apiman.io/apiman-docs/installation-guide/latest/quickstart.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.apiman.io/changelog.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apiman-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/apiman/apiman/blob/master/SECURITY.md
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apiman-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apiman-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apiman-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apiman-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apiman-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apiman-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/apiman-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/apiman-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apiman-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apiman-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apiman-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apiman-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apiman-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apiman-rate-limits.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/apiman/apiman
- group: operate
  title: ''
  type: Community
  url: https://github.com/orgs/apiman/discussions
created: '2026-03-25'
description: Apiman is an open source API management platform featuring a REST API, manager UI, and standalone developer portal with multi-tenancy, events, notifications, permissions, and approval workflows. It provides extensible API gateway capabilities through a simple Java plugin architecture with support for policies, plans, organizations, and client management.
examples:
- key_count: 8
  name: Apiman Api Example
  slug: apiman-api-example
- key_count: 7
  name: Apiman Plan Example
  slug: apiman-plan-example
features:
- description: Full REST API for managing organizations, APIs, plans, clients, and policies programmatically.
  name: REST API Manager
- description: Extensible API gateway that enforces policies at runtime for authentication, rate limiting, and transformation.
  name: API Gateway
- description: Standalone developer portal for API discovery, documentation, and self-service subscription management.
  name: Developer Portal
- description: Pluggable Java-based policy engine supporting rate limiting, quotas, IP whitelisting, authentication, and custom policies.
  name: Policy Engine
- description: Organization-based multi-tenancy allowing separate API management namespaces within a single platform.
  name: Multi-Tenancy
- description: Configurable approval workflows for API subscriptions with notification and event support.
  name: Approval Workflows
finops:
- name: Apiman Finops
  service_category: API
  slug: apiman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiman.png
json_schemas:
- name: Apiman API
  property_count: 8
  slug: apiman-api
- name: Apiman Plan
  property_count: 7
  slug: apiman-plan
json_structures:
- name: Apiman Api Structure
  property_count: 8
  slug: apiman-api-structure
- name: Apiman Plan Structure
  property_count: 7
  slug: apiman-plan-structure
jsonld:
- class_count: 11
  name: Apiman Context
  property_count: 1
  slug: apiman-context
layout: provider
modified: '2026-09-06'
name: Apiman
nav: Providers
network: true
overview: 'Apiman publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Blobs API, Developers API, and 12 more. Tagged areas include API Gateway, API Management, Developer Portal, Java, and Open-Source.


  The Apiman catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apiman''s developer surface includes support, engineering blog, documentation, API reference, getting-started guide, changelog, authentication, and 28 more developer resources.'
plans:
- name: Apiman Plans Pricing
  plan_count: 0
  slug: apiman-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Apiman Rate Limits
  slug: apiman-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apiman API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apiman-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 61.3
    catalog_earned_first_party: 0.0
    catalog_gap: 53.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 28.0
    contract_quality: 49.9
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/apiman/refs/heads/main/screenshots/apiman-2026-06-20T172245.png
security:
- kind: authentication
  name: Apiman Authentication
  slug: apiman-authentication
  summary_line: openIdConnect/http · 3 schemes
- kind: domain-security
  name: Apiman Domain Security
  slug: apiman-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Apiman Vulnerability Disclosure
  slug: apiman-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apiman
solutions:
- description: Free, Apache-licensed API management platform deployable on any JVM-based infrastructure.
  name: Open Source
- description: High-performance async API gateway implementation using Eclipse Vert.x.
  name: Vert.x Gateway
- description: Apiman overlay for WildFly/EAP application server deployments.
  name: WildFly Overlay
tags:
- API Gateway
- API Management
- Developer Portal
- Java
- Open-Source
- Policy Enforcement
- Self-Hosted
- Keycloak
use_cases:
- description: Deploy Apiman on-premise to manage APIs across internal services with full control over infrastructure.
  name: On-Premise API Management
- description: Provide developers with a self-service portal for discovering and subscribing to APIs.
  name: Developer Portal Hosting
- description: Enforce security, rate limiting, and transformation policies on API traffic through the gateway.
  name: API Policy Enforcement
- description: Use organizations and plans to provide isolated API management environments for multiple teams.
  name: Multi-Team API Governance
website: https://www.apiman.io
---
