---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-08'
api_count: 2
apis:
- description: 'The Adaptive Client API is a sixteen-operation REST API under /api/v3/client that exposes an Adaptive workspace to external systems: list users, resources, endpoints, authorizations, scripts and teams'
  name: Adaptive Client API
  slug: adaptive-automation-technologies-client-api
- description: Adaptive ships a built-in Model Context Protocol server that lets AI agents — Claude, Cursor, VS Code and other MCP clients — work with an Adaptive workspace. Interactive clients connect to https://<w
  name: Adaptive MCP Server
  slug: adaptive-automation-technologies-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Adaptive Automation Technologies Webhooks
  slug: adaptive-automation-technologies-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://adaptive.live/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.adaptive.live/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.adaptive.live/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.adaptive.live/developer-guide/adaptive-api
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.adaptive.live/install/cloud-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adaptive-scale
- group: company
  title: ''
  type: Blog
  url: https://adaptive.live/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adaptive.live/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.adaptive.live/
- group: operate
  title: ''
  type: Support
  url: https://documentation.adaptive.live/overview/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adaptive.live/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptive.live/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/adaptive-automation-technologies-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptive-automation-technologies-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/adaptive-automation-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adaptive-automation-technologies-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/adaptive-automation-technologies-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adaptive-automation-technologies-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adaptive-automation-technologies-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptive-automation-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/adaptive-automation-technologies-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/adaptive-automation-technologies-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adaptive-automation-technologies-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-automation-technologies-domain-security.yml
created: '2026-09-07'
description: 'Adaptive Automation Technologies, Inc. — trading as Adaptive (adaptive.live) — builds a privileged access management and data security platform that brokers credential-less, fully audited access to databases, Kubernetes clusters, virtual machines, cloud accounts, network appliances and internal web services for both human operators and autonomous AI agents. The platform is sold as three surfaces: Bastion/Stratos (just-in-time infrastructure and browser access with SSO and MFA), Exo (a secure agent harness with a tools/MCP registry, scoped networking and guardrails), and a shared trust layer covering authorization, audit, data masking, database activity monitoring, discovery and classification, and compliance reporting. Adaptive exposes a documented sixteen-operation REST Client API at /api/v3/client, a built-in remote MCP server secured by OAuth with RFC 7591 dynamic client registration, a cross-platform CLI, and first-party Terraform and Pulumi providers. It runs as managed
  cloud on app.adaptive.live or self-hosted on Kubernetes, Docker or an air-gapped VM.'
image: https://adaptive.live/og/adaptive.png
layout: provider
mcp_servers:
- description: Adaptive ships a first-party, built-in remote MCP server as part of the platform — it is not a separate download. Every Adaptive deployment (managed cloud or self-hosted) exposes it on its own workspa
  name: Adaptive Automation Technologies MCP Server
  slug: adaptive-automation-technologies-mcp-server
modified: '2026-09-07'
name: Adaptive Automation Technologies
nav: Providers
network: true
overview: 'Adaptive Automation Technologies publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Privileged Access Management, Identity and Access Management, and Data Security.


  The Adaptive Automation Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adaptive Automation Technologies'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 17 more developer resources.'
plans:
- name: Adaptive Automation Technologies Plans Pricing
  plan_count: 0
  slug: adaptive-automation-technologies-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Adaptive Automation Technologies Rate Limits
  slug: adaptive-automation-technologies-rate-limits
scopes:
- name: Adaptive Automation Technologies Scopes
  scope_count: 0
  slug: adaptive-automation-technologies-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 50.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adaptive Automation Technologies Authentication
  slug: adaptive-automation-technologies-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Adaptive Automation Technologies Domain Security
  slug: adaptive-automation-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Adaptive Automation Technologies Trust Center
  slug: adaptive-automation-technologies-trust-center
  summary_line: SOC 2 Type II
slug: adaptive-automation-technologies
tags:
- Company
- Security
- Privileged Access Management
- Identity and Access Management
- Data Security
- Agents
- Model Context Protocol
- Infrastructure
- Databases
- Kubernetes
- Compliance
- Audit
website: https://adaptive.live/
---
