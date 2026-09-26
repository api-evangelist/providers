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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-09-25'
api_count: 5
apis:
- description: Auto-generated GraphQL API endpoint for each headless channel in Xperience by Kentico. Supports querying content items with filtering, sorting, pagination, linked items, language variants, taxonomy ta
  name: Kentico Headless GraphQL API
  slug: kentico-headless-graphql-api
- description: Built-in REST service for reading, creating, updating, and deleting pages and CMS objects within Xperience by Kentico. Requests use HTTP Basic authentication with Base64-encoded credentials or hash pa
  name: Kentico Management REST API
  slug: kentico-management-rest-api
- description: Server-side .NET API for content item queries, object queries, file system operations, and database access within Xperience by Kentico applications. Includes ContentRetriever API, ObjectQuery API, Fil
  name: Kentico .NET Content API
  slug: kentico-dotnet-content-api
- description: HTTP API for the Kentico SaaS control plane. Uploads a deployment ZIP package to an Xperience Portal project environment so CI/CD pipelines can deploy without using the Portal UI. Authenticated with a
  name: Xperience Portal API
  slug: kentico-xperience-portal-api
- description: Preview REST management API exposed by an Xperience by Kentico application at the kentico-api/management path once the Kentico.Xperience.ManagementApi package is installed and AddKenticoManagementApi(
  name: Xperience by Kentico Management API
  slug: kentico-management-api
artifact_total: 14
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/security/kentico-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kentico-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/security/kentico-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kentico-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/security/kentico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kentico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kentico.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kentico.com/documentation/developers-and-admins/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Kentico
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kenticosoftware
- group: company
  title: ''
  type: Blog
  url: https://www.kentico.com/discover/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kentico.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xperience-portal.com
- group: other
  title: ''
  type: X
  url: https://x.com/kentico
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/plans/kentico-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kentico-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/rate-limits/kentico-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kentico-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/finops/kentico-finops.yml
  title: ''
  type: FinOps
  url: finops/kentico-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/mcp/kentico-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kentico-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/llms/kentico-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kentico-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/packages/kentico-packages.yml
  title: ''
  type: Packages
  url: packages/kentico-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/packages/kentico-packages.yml
  title: ''
  type: SDKs
  url: packages/kentico-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/cli/kentico-cli.yml
  title: ''
  type: CLI
  url: cli/kentico-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/components/kentico-components.yml
  title: ''
  type: Components
  url: components/kentico-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/well-known/kentico-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kentico-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/well-known/kentico-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kentico-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.kentico.com/vulnerability-disclosure-program
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/authentication/kentico-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kentico-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/conventions/kentico-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kentico-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/errors/kentico-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kentico-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/lifecycle/kentico-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kentico-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.kentico.com/documentation/developers-and-admins/installation/support-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/changelog/kentico-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kentico-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/conformance/kentico-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kentico-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kentico.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/data-model/kentico-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kentico-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/sandbox/kentico-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kentico-sandbox.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kentico.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-reference.kentico.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kentico.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.kentico.com/customers/supportcenter
- group: operate
  title: ''
  type: Community
  url: https://community.kentico.com
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.kentico.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kentico
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kentico.com/end-user-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kentico.com/privacy-policy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/kentico
created: '2026-06-13'
description: Kentico is an enterprise .NET CMS and digital experience platform offering REST and GraphQL APIs for managing web content, e-commerce, digital marketing, and personalization. Xperience by Kentico provides headless channel GraphQL endpoints auto-generated per channel, a content item .NET API, file storage APIs supporting Azure Blob and Amazon S3, and a management REST service for CRUD operations on CMS objects. The platform supports ASP.NET Core with channel-based licensing covering website, email, and headless channels.
finops:
- name: Kentico Finops
  service_category: ''
  slug: kentico-finops
graphqls:
- description: Xperience by Kentico provides a per-channel headless GraphQL API whose schema is **auto-generated** at runtime from the content types configured in each headless channel. There is no single static sch
  name: Kentico Xperience GraphQL API
  slug: kentico-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kentico.png
layout: provider
mcp_servers:
- description: ''
  name: Kentico MCP Server
  slug: kentico-mcp-server
modified: '2026-08-13'
name: Kentico
nav: Providers
network: true
overview: 'Kentico publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, Digital Experience Platform, GraphQL, and REST.


  Kentico''s developer surface includes documentation, engineering blog, pricing, CLI, authentication, changelog, sandbox, and 37 more developer resources.'
plans:
- name: Kentico Plans Pricing
  plan_count: 5
  slug: kentico-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Kentico Rate Limits
  slug: kentico-rate-limits
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 34.0
    developer_ergonomics: 82.1
    discoverability: 80.0
    operational_transparency: 52.6
  previous_composite: 60.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/screenshots/kentico-2026-06-20T183955.png
security:
- kind: authentication
  name: Kentico Authentication
  slug: kentico-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Kentico Domain Security
  slug: kentico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kentico Vulnerability Disclosure
  slug: kentico-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kentico Trust Center
  slug: kentico-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: kentico
tags:
- CMS
- Content Management
- Digital Experience Platform
- GraphQL
- REST
- .NET
- Headless
- E-Commerce
- Digital Marketing
- Personalization
website: https://www.kentico.com
---
