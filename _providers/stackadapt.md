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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: Read-only REST API for fetching reporting data across dimensions and metrics to analyze campaign performance. Write operations are deprecated; use the GraphQL API for write operations.
  name: StackAdapt REST API
  slug: rest-api
- description: Full-featured GraphQL API for creating and managing programmatic advertising campaigns, ad groups, creatives, targeting segments, pixel tracking, and performance reporting. The primary API for write o
  name: StackAdapt GraphQL API
  slug: graphql-api
- description: Server-to-server API for conversion tracking and audience generation without requiring website pixel installation.
  name: StackAdapt Pixel API
  slug: pixel-api
- description: API for secure data sharing and audience synchronization with third-party platforms and data partners.
  name: StackAdapt Data Taxonomy API
  slug: data-taxonomy-api
- description: Model Context Protocol server enabling AI agents (Claude, ChatGPT) to interact with the StackAdapt platform programmatically via the GraphQL API.
  name: StackAdapt MCP Server
  slug: mcp-server
artifact_total: 20
asyncapis:
- description: ''
  name: Stackadapt Webhooks
  slug: stackadapt-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/stackadapt/security/stackadapt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackadapt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stackadapt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackadapt.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/StackAdapt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackadapt
- group: company
  title: ''
  type: Blog
  url: https://www.stackadapt.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackadapt.com/plans-and-packages
- group: other
  title: ''
  type: X
  url: https://x.com/stackadapt
- group: commercial
  href: https://artifacts.apis.io/stackadapt/plans/stackadapt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackadapt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stackadapt/rate-limits/stackadapt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stackadapt-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stackadapt/finops/stackadapt-finops.yml
  title: ''
  type: FinOps
  url: finops/stackadapt-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StackAdapt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.stackadapt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stackadapt.com/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stackadapt.com/get-started-with-api
- group: start
  title: ''
  type: SignUp
  url: https://www.stackadapt.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://www.stackadapt.com/academy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stackadapt.com/legal-document-centre/api-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stackadapt.com/legal-document-centre/platform-and-services-privacy-policy
- group: agent
  href: https://artifacts.apis.io/stackadapt/llms/stackadapt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stackadapt-llms.txt
- group: agent
  href: https://artifacts.apis.io/stackadapt/mcp/stackadapt-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stackadapt-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stackadapt/well-known/stackadapt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stackadapt-well-known.yml
- group: build
  href: https://artifacts.apis.io/stackadapt/packages/stackadapt-packages.yml
  title: ''
  type: Packages
  url: packages/stackadapt-packages.yml
- group: build
  href: https://artifacts.apis.io/stackadapt/packages/stackadapt-packages.yml
  title: ''
  type: SDKs
  url: packages/stackadapt-packages.yml
- group: auth
  href: https://artifacts.apis.io/stackadapt/authentication/stackadapt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stackadapt-authentication.yml
- group: auth
  href: https://artifacts.apis.io/stackadapt/scopes/stackadapt-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/stackadapt-scopes.yml
- group: design
  href: https://artifacts.apis.io/stackadapt/conventions/stackadapt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stackadapt-conventions.yml
- group: design
  href: https://artifacts.apis.io/stackadapt/errors/stackadapt-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/stackadapt-error-codes.yml
- group: design
  href: https://artifacts.apis.io/stackadapt/lifecycle/stackadapt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stackadapt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.stackadapt.com/legal-document-centre/api-terms-and-conditions
- group: design
  href: https://artifacts.apis.io/stackadapt/conformance/stackadapt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stackadapt-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.stackadapt.com/trust-and-security-center
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.stackadapt.com/trust-and-security-center
- group: auth
  href: https://artifacts.apis.io/stackadapt/security/stackadapt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackadapt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.stackadapt.com/trust-and-security-center
- group: start
  href: https://artifacts.apis.io/stackadapt/sandbox/stackadapt-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stackadapt-sandbox.yml
- group: design
  href: https://artifacts.apis.io/stackadapt/components/stackadapt-components.yml
  title: ''
  type: Components
  url: components/stackadapt-components.yml
- group: design
  href: https://artifacts.apis.io/stackadapt/data-model/stackadapt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stackadapt-data-model.yml
- group: design
  href: https://artifacts.apis.io/stackadapt/asyncapi/stackadapt-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/stackadapt-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/stackadapt/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-13'
description: StackAdapt is an AI-powered programmatic advertising platform with REST and GraphQL APIs for managing campaigns, ad groups, creatives, targeting segments, pixel tracking, and performance reporting across native, display, video, connected TV, audio, and digital out-of-home channels.
finops:
- has_sources: true
  method: derived
  name: Stackadapt Finops
  primary_unit: ''
  service_category: ''
  slug: stackadapt-finops
  template: true
graphqls:
- description: StackAdapt is an AI-powered programmatic advertising platform (DSP) that provides a full-featured GraphQL API for creating and managing digital advertising campaigns across native, display, video, con
  name: StackAdapt GraphQL API
  slug: stackadapt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackadapt.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.stackadapt.com over HTTP requiring OAuth.
  name: StackAdapt MCP Server
  slug: stackadapt
modified: '2026-08-13'
name: StackAdapt
nav: Providers
network: true
overview: 'StackAdapt is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Programmatic Advertising, Digital Advertising, Campaign Management, AdTech, and DSP.


  The StackAdapt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StackAdapt''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, signup flow, support, and 33 more developer resources.'
plans:
- name: Stackadapt Plans Pricing
  plan_count: 5
  slug: stackadapt-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Stackadapt Rate Limits
  slug: stackadapt-rate-limits
scopes:
- name: Stackadapt Scopes
  scope_count: 2
  slug: stackadapt-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 73.2
    discoverability: 70.0
    operational_transparency: 31.6
  previous_composite: 63.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stackadapt/stackadapt-2026-06-20T194444.png
security:
- kind: authentication
  name: Stackadapt Authentication
  slug: stackadapt-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Stackadapt Domain Security
  slug: stackadapt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stackadapt Vulnerability Disclosure
  slug: stackadapt-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Stackadapt Trust Center
  slug: stackadapt-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, PCI DSS, ISO/IEC 27001:2022, NIST Cybersecurity Framework (CSF)
skill_count: 4
skills:
- name: Build StackAdapt audiences, pixels and event subscriptions
  slug: stackadapt-audiences-pixels-and-webhooks
- name: Connect an agent to StackAdapt over MCP
  slug: stackadapt-connect-agent-via-mcp
- name: Launch and control a StackAdapt campaign
  slug: stackadapt-launch-and-control-a-campaign
- name: Pull campaign performance from StackAdapt
  slug: stackadapt-pull-campaign-performance
slug: stackadapt
tags:
- Programmatic Advertising
- Digital Advertising
- Campaign Management
- AdTech
- DSP
- Native Advertising
- Display Advertising
- Video Advertising
- Connected TV
- Audience Targeting
- Real-Time Bidding
- Conversion Tracking
- Performance Reporting
website: https://www.stackadapt.com
---
