---
access_model:
  confidence: high
  label: Paid · Sales-assisted onboarding · API access granted on request
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Customeros Agentic Access
  operation_count: 57
  slug: customeros-agentic-access
  summary_line: 57 operations · 30 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: 'Key-authenticated REST surface for the customeros.ai cloud, published as six OpenAPI 3.0.1 documents (one per tag) plus the source Swagger 2.0 in github.com/customeros/customeros. All six declare the '
  name: CustomerOS REST API
  slug: customeros-customerbase-rest-api
- description: '34-operation REST API for outbound sequencing — flows, sequences, steps (email, LinkedIn or manual), senders with warming state and daily send limits, sending schedules, opt-out and analytics config, '
  name: CustomerOS Flow API
  slug: customeros-flow-api
- description: Client-side JavaScript tracker that captures page views and custom events, exposes window.cos.identify() for attaching identity and properties, and matches visitor IPs to companies. Since the 2025-09-
  name: CustomerOS Website Tracker
  slug: customeros-website-tracker
- description: Single GraphQL endpoint served by the open-source customer-os-api (Go, gqlgen) covering organizations, contacts, opportunities, contracts, invoices, interactions and timeline events. The repository mo
  name: CustomerOS GraphQL API
  slug: customeros-graphql-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-billing
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-customerbase
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-domains
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-enrich
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-flow-api
- collection_type: open
  name: CustomerOS GraphQL API
  slug: open-customeros-graphql-api
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-outreach
- collection_type: open
  name: CustomerOS API
  slug: open-customeros-verify
- collection_type: open
  name: CustomerOS GraphQL API
  slug: open-customeros
common:
- group: company
  title: ''
  type: Website
  url: https://customeros.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.customeros.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.customeros.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://customeros.ai/gtm-guides
- group: commercial
  title: ''
  type: Pricing
  url: https://customeros.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.customeros.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://customeros.ai/standard-agreement/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://customeros.ai/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customeros
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customeros
- group: operate
  title: ''
  type: StatusPage
  url: https://status.customeros.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.customeros.ai/security-and-compliance
- group: operate
  title: ''
  type: ChangeLog
  url: https://customeros.ai/updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/customeros-changelog.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/customeros-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/customeros-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/customeros-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/customeros-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/customeros-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customeros-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/customeros-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/customeros-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/customeros-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/customeros-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/customeros-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/customeros-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/customeros-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/customeros-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/customeros-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customeros-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/customeros-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/customeros-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/customeros-finops.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-customerbase-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-enrich-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-verify-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-domains-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-billing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-outreach-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-flow-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customeros-graphql-api-overlay.yaml
created: '2026-06-20'
description: CustomerOS (formerly Openline) is a London-based revenue-intelligence platform for B2B go-to-market teams. It identifies anonymous website visitors, scores them against an ideal customer profile, infers buying stage from page engagement, and attributes content and ad spend to real pipeline. The developer surface spans a first-party JavaScript website tracker installed behind a customer-owned reverse-proxy CNAME, a set of key-authenticated REST APIs published as OpenAPI in the company monorepo (CustomerBASE contacts and organizations, person and organization enrichment, email verification and IP intelligence, Mailstack sending domains and mailboxes, billing invoices, outreach tracking), a 34-operation Flow API for outbound sequencing, and the open-source customer-os-api GraphQL server that predates the pivot. CustomerOS also runs a live anonymous MCP server and serves an A2A agent card from its documentation host.
finops:
- name: Customeros Finops
  service_category: Customer Relationship Management
  slug: customeros-finops
graphqls:
- description: Representative GraphQL schema for the [CustomerOS](https://customeros.ai/) (formerly Openline)
  name: CustomerOS GraphQL Schema
  slug: customeros-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customeros.png
layout: provider
mcp_servers:
- description: ''
  name: customeros-mcp.yml
  slug: customeros-mcpyml
modified: '2026-08-13'
name: CustomerOS
nav: Providers
network: true
overview: 'CustomerOS publishes 3 APIs on the [APIs.io](https://apis.io/) network: REST API, Flow API, and GraphQL API. Tagged areas include CRM, Revenue, Go-To-Market, Lead Intelligence, and Visitor Identification.


  CustomerOS''s developer surface includes documentation, getting-started guide, engineering blog, pricing, changelog, authentication, and 37 more developer resources.'
plans:
- name: Customeros Plans Pricing
  plan_count: 2
  slug: customeros-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Customeros Rate Limits
  slug: customeros-rate-limits
score:
  band: developing
  composite: 50.2
  delta: -6.5
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 16.7
    contract_quality: 54.2
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/customeros/refs/heads/main/screenshots/customeros-2026-06-20T175351.png
security:
- kind: authentication
  name: Customeros Authentication
  slug: customeros-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Customeros Domain Security
  slug: customeros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Customeros Trust Center
  slug: customeros-trust-center
  summary_line: CASA Type 2
slug: customeros
tags:
- CRM
- Revenue
- Go-To-Market
- Lead Intelligence
- Visitor Identification
- Attribution
- Email Verification
- Enrichment
- GraphQL
- Open Source
website: https://customeros.ai
---
