---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.1
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: REST API v4 for managing business locations, syndicating listings to 80+ directories, aggregating and responding to reviews, running review campaigns, tracking local search rankings with grid-rank hea
  name: Synup API
  slug: synup-api
- description: First-party remote Model Context Protocol server enumerating 126 tools in its published tool table across six surfaces (Locations, Listings, Reviews, Rankings, Posts & Social, Account & Insights). Ten
  name: Synup MCP Server
  slug: synup-mcp
artifact_total: 12
asyncapis:
- description: ''
  name: Synup Webhooks
  slug: synup-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.synup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.synup.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.synup.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.synup.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.synup.com/synup-local-seo-api-getting-started-doc-824500
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/synup-api-openapi.yml
- group: design
  title: ''
  type: Webhooks
  url: openapi/synup-webhooks-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/synup-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/synup-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synup-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/synup-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/synup-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synup-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synup-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synup-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synup-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synup-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.synup.com/en/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/synup-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/synup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synup-packages.yml
- group: design
  title: ''
  type: Components
  url: components/synup-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/synup-api-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/synup-examples.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/synup-schemas.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/synup-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/synup-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synup-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/synup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/synup-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synup
- group: other
  title: ''
  type: X
  url: https://x.com/synupinc
- group: company
  title: ''
  type: Blog
  url: https://www.synup.com/en/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synup.com/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.synup.com/
- group: start
  title: ''
  type: Login
  url: https://local.synup.com/users/find_workspace
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synup.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synup.com/en/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.synup.com/
created: '2026-06-13'
description: Synup is a local marketing platform for agencies and multi-location brands, providing a REST API (v4) for managing business locations, syndicating listing data to 80+ directories including Google, Apple, Bing and Facebook, aggregating and responding to reviews across every connected platform, running SMS and email review campaigns, tracking local search rankings with grid-rank heatmaps, publishing local and social posts, and pulling unified profile analytics. The platform serves marketing agencies with white-label tooling covering listings sync, reputation management, social media, local SEO and reporting, and ships a first-party remote MCP server so AI agents can drive the same surface as the dashboard.
finops:
- name: Synup Finops
  service_category: ''
  slug: synup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synup.png
json_schemas:
- name: Synup API v4 component schemas
  property_count: 0
  slug: synup-schemas
jsonld:
- class_count: 33
  name: Synup Context
  property_count: 2
  slug: synup-context
layout: provider
mcp_servers:
- description: ''
  name: synup-mcp.yml
  slug: synup-mcpyml
modified: '2026-08-13'
name: Synup
nav: Providers
network: true
overview: 'Synup publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Local Marketing, Listings Management, Reputation Management, Local SEO, and Reviews.


  The Synup catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Synup''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, code examples, engineering blog, and 36 more developer resources.'
plans:
- name: Synup Plans Pricing
  plan_count: 3
  slug: synup-plans-pricing
random_paper: 128
rate_limits:
- limit_count: 0
  name: Synup Rate Limits
  slug: synup-rate-limits
scopes:
- name: Synup Scopes
  scope_count: 2
  slug: synup-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 61.3
  delta: -3.3
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 71.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 26.3
  previous_composite: 64.6
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synup/refs/heads/main/screenshots/synup-2026-06-20T194835.png
security:
- kind: authentication
  name: Synup Authentication
  slug: synup-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Synup Domain Security
  slug: synup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synup
tags:
- Local Marketing
- Listings Management
- Reputation Management
- Local SEO
- Reviews
- Social Media
- Analytics
- Business Listings
- Review Management
- Agency Software
website: https://www.synup.com/
---
