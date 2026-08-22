---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bucket Agentic Access
  operation_count: 12
  slug: bucket-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 2
apis:
- description: JSON-over-HTTP API browsers and backends use at runtime to fetch evaluated and enabled flags, and to send users, companies and feature-usage events. Publishable-key (client) or secret-key (server) bea
  name: Reflag Runtime API
  slug: reflag-runtime-api
- description: The Apps API from Bucket — 9 operation(s) for apps.
  name: Bucket Apps API
  slug: bucket-apps-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reflag Management Apps API
  slug: open-bucket-apps-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bucket-management-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bucket-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://reflag.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reflag.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reflag.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reflag.com/api/reflag-rest-api/reflag-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reflag.com/welcome/readme
- group: company
  title: ''
  type: Blog
  url: https://reflag.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://reflag.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://reflag.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.reflag.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.reflag.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reflag.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reflag.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reflagcom
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reflag.com
- group: auth
  title: ''
  type: Security
  url: https://reflag.com/legal/security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://reflag.com/security
- group: build
  title: ''
  type: Packages
  url: packages/bucket-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bucket-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bucket-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bucket-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bucket-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bucket-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bucket-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bucket-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bucket-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bucket-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/bucket-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bucket-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bucket-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bucket-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bucket (rebranded to Reflag in 2026, reflag.com) is a TypeScript-first feature management platform built for B2B SaaS teams. It provides feature flags with self-cleaning lifecycle automation, AI/agent integration via a hosted MCP server, strongly typed SDKs for React, React Native, Vue, Next.js, Node.js and the browser, OpenFeature providers, local flag evaluation for zero-latency and downtime protection, feature entitlements, in-app feedback collection, and deep integrations with Linear, Slack, GitHub, Datadog, Vercel and analytics tools. The platform exposes two APIs — a Runtime API for evaluating flags for users and companies at request time, and a Management API for programmatically managing apps, environments, flags and targeting rules from CI/CD. Backed by 500 Global and Creandum.
image: https://cdn.prod.website-files.com/68a872edf3df6064de547670/68b8414134c540f12c2928bc_reflag-dynamic-favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: bucket-mcp.yml
  slug: bucket-mcpyml
modified: '2026-07-18'
name: Bucket
nav: Providers
network: true
overview: 'Bucket publishes 1 API on the [APIs.io](https://apis.io/) network: Apps API. Tagged areas include Company, Feature Flags, Feature Management, Feature Flagging, and Developer Tools.


  Bucket''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, signup flow, and 26 more developer resources.'
random_paper: 8
score:
  band: strong
  composite: 55.1
  delta: -3.5
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 58.0
    developer_ergonomics: 68.5
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 28.9
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bucket/refs/heads/main/screenshots/bucket-2026-07-25T204024.png
security:
- kind: authentication
  name: Bucket Authentication
  slug: bucket-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bucket Domain Security
  slug: bucket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bucket Vulnerability Disclosure
  slug: bucket-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Bucket Trust Center
  slug: bucket-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: bucket
tags:
- Company
- Feature Flags
- Feature Management
- Feature Flagging
- Developer Tools
- SaaS
- Entitlements
- Experimentation
- MCP
- Agent Ready
website: https://reflag.com
---
