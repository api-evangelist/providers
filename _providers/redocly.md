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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-04'
api_count: 12
apis:
- description: Redocly Realm is the comprehensive API lifecycle management platform that unifies Redoc, Revel, and Reef into a single integrated product. Realm includes API documentation, mock servers, linting, cata
  name: Redocly Realm
  slug: redocly-realm
- description: Redocly Reunite is the Git-connected collaboration and deployment surface for Realm. It prepares, deploys, and hosts documentation projects and mock servers and ships a content editor, pull requests a
  name: Redocly Reunite
  slug: redocly-reunite
- description: Redocly Revel is the external developer hub product. It renders Markdown, Markdoc, and React pages with multi-product and localization capabilities, enabling organizations to create polished developer
  name: Redocly Revel
  slug: redocly-revel
- description: 'Redocly Reef is the internal API platform — a service catalog and governance product that organizes, aids discovery, and monitors APIs throughout their lifecycle. Reef includes Catalog for organizing '
  name: Redocly Reef
  slug: redocly-reef
- description: 'Redoc is the open-source engine that renders API reference documentation from OpenAPI definitions with a three-panel layout known for clarity and usability. Supports OpenAPI 3.2, 3.1, 3.0 and OpenAPI '
  name: Redocly Redoc
  slug: redocly-redoc
- description: Redocly CLI is an open-source command-line tool for working with OpenAPI descriptions, developer portals, and other API lifecycle operations. Supports linting, validation, bundling, splitting, and dec
  name: Redocly CLI
  slug: redocly-cli
- description: Respect Monitoring is Redocly's continuous, API-aware monitoring product powered by OpenAPI Arazzo workflows. Rather than uptime checking, it validates that API responses conform to specifications — e
  name: Redocly Respect Monitoring
  slug: redocly-respect
- description: Arazzo is the OpenAPI Initiative's specification for describing multi-step API workflows; Redocly is a primary tooling vendor with first-class Arazzo support across Redocly CLI (lint, validate, genera
  name: Arazzo Specification (Redocly Tooling)
  slug: redocly-arazzo
- baseURL: https://redocly.com
  baseurl_source: declared
  description: 'The Search API is the machine-readable query surface of any Realm project: POST /_search returns documentation and API-reference matches and POST /_search-facets returns facet aggregations. It is the '
  name: Redocly Realm Search API
  slug: redocly-search-api
- baseURL: https://redocly.com/mcp
  baseurl_source: declared
  description: 'The Docs MCP server is Realm''s Model Context Protocol endpoint, generated automatically from a project''s documentation and OpenAPI descriptions and served at /mcp on the project root. Redocly runs it '
  name: Redocly Docs MCP Server
  slug: redocly-docs-mcp
- baseURL: https://{host}/api
  baseurl_source: declared
  description: 'Scout is Redocly''s API-discovery service: it crawls connected Git remotes, tracks pull requests and runs jobs that find hidden, duplicate and undocumented APIs, then pushes what it finds into a Reunit'
  name: Redocly Scout API
  slug: redocly-scout
- baseURL: http://{host}
  baseurl_source: declared
  description: 'The Scout agent is the self-hosted worker half of Scout, deployed inside the customer''s own infrastructure (Redocly documents an AWS ECS task definition). Its API is small and operational: a health ch'
  name: Redocly Scout Agent API
  slug: redocly-scout-agent
artifact_total: 31
asyncapis:
- description: ''
  name: Redocly Webhooks
  slug: redocly-webhooks
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/redocly-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redocly-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redocly-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://redocly.com/docs
- group: other
  title: ''
  type: Customers
  url: https://redocly.com/customers
- group: commercial
  title: ''
  type: Pricing
  url: https://redocly.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://redocly.com/blog
- group: learn
  title: ''
  type: Webinars
  url: https://redocly.com/webinars
- group: auth
  title: ''
  type: Security
  url: https://redocly.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redocly.com/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://redocly.com/sla
- group: build
  title: ''
  type: CLI
  url: https://redocly.com/redocly-cli
- group: company
  title: ''
  type: About
  url: https://redocly.com/about
- group: operate
  title: ''
  type: Support
  url: https://redocly.com/contact-us
- group: other
  title: ''
  type: Products
  url: https://redocly.com/products
- group: start
  title: ''
  type: Login
  url: https://auth.cloud.redocly.com/login
- group: start
  title: ''
  type: Signup
  url: https://redocly.com/billing/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redocly.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redocly.com/subscription-agreement
- group: company
  title: ''
  type: Careers
  url: https://redocly.com/careers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Redocly
- group: other
  title: ''
  type: X
  url: https://twitter.com/Redocly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redocly
- group: other
  title: ''
  type: Governance
  url: https://redocly.com/api-governance
- group: operate
  title: ''
  type: ChangeLog
  url: https://redocly.com/docs/realm/changelog
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://redocly.com/vulnerability-disclosure-policy
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://redocly.com/dpa
- group: docs
  title: ''
  type: Reference
  url: https://redocly.com/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/redocly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/redocly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/redocly-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://redocly.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/redocly-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redocly-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/redocly-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/redocly-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/redocly-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redocly-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/redocly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/redocly-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/redocly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redocly-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/redocly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redocly-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redocly-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/redocly-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/redocly-cli.yml
- group: design
  title: ''
  type: Components
  url: components/redocly-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/redocly-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/redocly-webhooks.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://redocly.com/roadmap
- group: start
  title: ''
  type: GettingStarted
  url: https://redocly.com/docs/realm/get-started
- group: start
  title: ''
  type: Quickstart
  url: https://redocly.com/docs/cli/quickstart
- group: learn
  title: ''
  type: Learn
  url: https://redocly.com/learn
- group: other
  title: ''
  type: SubProcessors
  url: https://redocly.com/sub-processors
created: '2026-01-05'
description: Redocly is a company that specializes in API documentation and governance tooling. Their platform helps organizations create, manage, and publish API documentation through Realm (the integrated lifecycle platform that unifies Redoc, Revel, and Reef), Reunite (Git-connected collaboration and deployment for docs/APIs), Revel (developer portal), Reef (internal API catalog and scorecard), and Redoc (open-source OpenAPI renderer). The Redocly CLI provides linting, bundling, splitting, decoration, and documentation generation for OpenAPI, AsyncAPI, and Arazzo specifications. Respect Monitoring adds continuous, Arazzo-powered API monitoring, and the Enterprise tier exposes MCP Servers and AI search for Realm portals — positioning Redocly's catalog as an AI substrate for agentic software.
examples:
- key_count: 2
  name: Redocly Cli Commands Example
  slug: redocly-cli-commands-example
- key_count: 3
  name: Redocly Config Example
  slug: redocly-config-example
- key_count: 3
  name: Redocly Lint Result Example
  slug: redocly-lint-result-example
finops:
- name: Redocly Finops
  service_category: API
  slug: redocly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redocly.png
json_schemas:
- name: Redocly Configuration
  property_count: 7
  slug: redocly-config
- name: Redocly Lint Result
  property_count: 3
  slug: redocly-lint-result
json_structures:
- name: Redocly Config Structure
  property_count: 0
  slug: redocly-config-structure
- name: Redocly Lint Result Structure
  property_count: 0
  slug: redocly-lint-result-structure
jsonld:
- class_count: 0
  name: Redocly Context
  property_count: 4
  slug: redocly-context
layout: provider
mcp_servers:
- description: 'Redocly ships a Docs MCP server as a Realm feature and runs it on its own documentation site. The endpoint answers anonymously: tools/list returns two real tools and resources/list returns the publish'
  name: Redocly Docs MCP Server
  slug: redocly-docs-mcp-server
modified: '2026-08-27'
name: Redocly
nav: Providers
network: true
overview: 'Redocly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Realm Search API, Docs MCP Server, Scout API, and 1 more. Tagged areas include Artificial Intelligence, API Catalog, API Documentation, Arazzo, and Developer Portal.


  The Redocly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Redocly''s developer surface includes authentication, documentation, pricing, engineering blog, CLI, support, signup flow, and 49 more developer resources.'
plans:
- name: Redocly Plans Pricing
  plan_count: 15
  slug: redocly-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 9
  name: Redocly Rate Limits
  slug: redocly-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Redocly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: redocly-jsonschema-spectral-rules
scopes:
- name: Redocly Scopes
  scope_count: 0
  slug: redocly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 85.3
    catalog_earned_first_party: 24.0
    catalog_gap: 29.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 43.2
    contract_quality: 65.4
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 43.2
    operational_transparency: 92.1
  previous_composite: 73.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redocly/refs/heads/main/screenshots/redocly-2026-06-20T192731.png
security:
- kind: authentication
  name: Redocly Authentication
  slug: redocly-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Redocly Domain Security
  slug: redocly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Redocly Vulnerability Disclosure
  slug: redocly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Redocly Trust Center
  slug: redocly-trust-center
  summary_line: SOC 2 Type II, CSA STAR / CAIQ v4, PCI DSS, GDPR / CCPA
slug: redocly
tags:
- Artificial Intelligence
- API Catalog
- API Documentation
- Arazzo
- Developer Portal
- Governance
- Linting
- MCP
- Monitoring
- OpenAPI
---
