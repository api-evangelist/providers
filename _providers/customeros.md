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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Customeros Agentic Access
  operation_count: 57
  slug: customeros-agentic-access
  summary_line: 57 operations · 30 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Client-side JavaScript tracker that captures page views and custom events, exposes window.cos.identify() for attaching identity and properties, and matches visitor IPs to companies. Since the 2025-09-
  name: CustomerOS Website Tracker
  slug: customeros-website-tracker
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Billing API API from CustomerOS — 1 operation(s) for billing api.
  name: CustomerOS Billing API
  slug: customeros-billing-api-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The CustomerBASE API API from CustomerOS — 6 operation(s) for customerbase api.
  name: CustomerOS CustomerBASE API
  slug: customeros-customerbase-api-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Domains API from CustomerOS — 2 operation(s) for domains.
  name: CustomerOS Domains API
  slug: customeros-domains-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Email Verification API from CustomerOS — 4 operation(s) for email verification.
  name: CustomerOS Email Verification API
  slug: customeros-email-verification-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Enrichment API API from CustomerOS — 3 operation(s) for enrichment api.
  name: CustomerOS Enrichment API
  slug: customeros-enrichment-api-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Flows API from CustomerOS — 18 operation(s) for flows.
  name: CustomerOS Flows API
  slug: customeros-flows-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The IP Intelligence API from CustomerOS — 1 operation(s) for ip intelligence.
  name: CustomerOS IP Intelligence API
  slug: customeros-ip-intelligence-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Mailboxes API from CustomerOS — 1 operation(s) for mailboxes.
  name: CustomerOS Mailboxes API
  slug: customeros-mailboxes-api
- baseURL: https://api.customeros.ai
  baseurl_source: declared
  description: The Outreach API from CustomerOS — 1 operation(s) for outreach.
  name: CustomerOS Outreach API
  slug: customeros-outreach-api
- baseURL: https://{customer-reverse-proxy-domain}/analytics-0.1.js
  baseurl_source: declared
  description: Single GraphQL endpoint for all CustomerOS operations.
  name: CustomerOS Graph QL API
  slug: customeros-graph-ql-api
artifact_total: 35
collections:
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
- group: other
  href: https://artifacts.apis.io/customeros/capabilities/customeros-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/customeros-capability-edges.yml
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
  href: https://artifacts.apis.io/customeros/changelog/customeros-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/customeros-changelog.yml
- group: other
  href: https://artifacts.apis.io/customeros/a2a/customeros-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/customeros-a2a.yml
- group: agent
  href: https://artifacts.apis.io/customeros/mcp/customeros-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/customeros-mcp.yml
- group: build
  href: https://artifacts.apis.io/customeros/mcp/customeros-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/customeros-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/customeros/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/customeros/llms/customeros-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/customeros-llms.txt
- group: agent
  href: https://artifacts.apis.io/customeros/well-known/customeros-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/customeros-well-known.yml
- group: agent
  href: https://artifacts.apis.io/customeros/agentic-access/customeros-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/customeros-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/customeros/authentication/customeros-authentication.yml
  title: ''
  type: Authentication
  url: authentication/customeros-authentication.yml
- group: design
  href: https://artifacts.apis.io/customeros/conventions/customeros-conventions.yml
  title: ''
  type: Conventions
  url: conventions/customeros-conventions.yml
- group: design
  href: https://artifacts.apis.io/customeros/errors/customeros-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/customeros-problem-types.yml
- group: design
  href: https://artifacts.apis.io/customeros/lifecycle/customeros-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/customeros-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/customeros/conformance/customeros-conformance.yml
  title: ''
  type: Conformance
  url: conformance/customeros-conformance.yml
- group: design
  href: https://artifacts.apis.io/customeros/data-model/customeros-data-model.yml
  title: ''
  type: DataModel
  url: data-model/customeros-data-model.yml
- group: design
  href: https://artifacts.apis.io/customeros/components/customeros-components.yml
  title: ''
  type: Components
  url: components/customeros-components.yml
- group: build
  href: https://artifacts.apis.io/customeros/packages/customeros-packages.yml
  title: ''
  type: Packages
  url: packages/customeros-packages.yml
- group: other
  href: https://artifacts.apis.io/customeros/grpc/_index.yml
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: auth
  href: https://artifacts.apis.io/customeros/security/customeros-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/customeros-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/customeros/security/customeros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/customeros-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/customeros/plans/customeros-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/customeros-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/customeros/rate-limits/customeros-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/customeros-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/customeros/finops/customeros-finops.yml
  title: ''
  type: FinOps
  url: finops/customeros-finops.yml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-customerbase-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-customerbase-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-enrich-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-enrich-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-verify-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-verify-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-domains-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-domains-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-billing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-billing-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-outreach-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-outreach-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-flow-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-flow-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/customeros/overlays/customeros-graphql-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/customeros-graphql-api-overlay.yaml
- group: operate
  title: ''
  type: Support
  url: mailto:help@customeros.ai
created: '2026-06-20'
description: CustomerOS (formerly Openline) is a London-based revenue-intelligence platform for B2B go-to-market teams. It identifies anonymous website visitors, scores them against an ideal customer profile, infers buying stage from page engagement, and attributes content and ad spend to real pipeline. The developer surface spans a first-party JavaScript website tracker installed behind a customer-owned reverse-proxy CNAME, a set of key-authenticated REST APIs published as OpenAPI in the company monorepo (CustomerBASE contacts and organizations, person and organization enrichment, email verification and IP intelligence, Mailstack sending domains and mailboxes, billing invoices, outreach tracking), a 34-operation Flow API for outbound sequencing, and the open-source customer-os-api GraphQL server that predates the pivot. CustomerOS also runs a live anonymous MCP server and serves an A2A agent card from its documentation host.
finops:
- has_sources: true
  method: derived
  name: Customeros Finops
  primary_unit: subscription
  service_category: ''
  slug: customeros-finops
  template: false
graphqls:
- description: Representative GraphQL schema for the [CustomerOS](https://customeros.ai/) (formerly Openline)
  name: CustomerOS GraphQL Schema
  slug: customeros-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customeros.png
layout: provider
mcp_servers:
- description: CustomerOS runs a live, anonymous, remote MCP server on its documentation host. It is a DOCUMENTATION server (search + a read-only virtual filesystem over the docs pages and the published OpenAPI), no
  name: CustomerOS MCP Server
  slug: customer-os-docs
modified: '2026-08-13'
name: CustomerOS
nav: Providers
network: true
overview: 'CustomerOS publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, CustomerBASE API, Domains API, and 8 more. Tagged areas include CRM, Revenue, Go-To-Market, Lead Intelligence, and Visitor Identification.


  The CustomerOS catalog on APIs.io includes 1 Spectral governance ruleset.


  CustomerOS''s developer surface includes documentation, getting-started guide, engineering blog, pricing, changelog, authentication, support, and 38 more developer resources.'
plans:
- name: Customeros Plans Pricing
  plan_count: 2
  slug: customeros-plans-pricing
- name: Customeros Price Estimates
  plan_count: 0
  slug: customeros-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Customeros Rate Limits
  slug: customeros-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: CustomerOS API Rules
  rule_count: 54
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 11
  slug: customeros-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 55.5
    catalog_earned_first_party: 8.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 82.9
    contract_governance: 18.2
    contract_quality: 50.6
    developer_ergonomics: 42.3
    discoverability: 80.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/customeros/customeros-2026-06-20T175351.png
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
skill_count: 4
skills:
- name: customeros-build-outbound-flow
  slug: customeros-build-outbound-flow
- name: customeros-enrich-and-verify
  slug: customeros-enrich-and-verify
- name: customeros-manage-customerbase
  slug: customeros-manage-customerbase
- name: customeros-manage-mailstack-domains
  slug: customeros-manage-mailstack-domains
slug: customeros
tags:
- CRM
- Revenue
- Go-To-Market
- Lead Intelligence
- Visitor Identification
- Attribution
- Email Verification
- Data Enrichment
- GraphQL
- Open Source
- A2A
website: https://customeros.ai
---
