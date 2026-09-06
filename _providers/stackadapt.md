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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-05'
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
artifact_total: 16
asyncapis:
- description: ''
  name: Stackadapt Webhooks
  slug: stackadapt-webhooks
common:
- group: auth
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
  title: ''
  type: Plans
  url: plans/stackadapt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stackadapt-rate-limits.yml
- group: commercial
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
  title: ''
  type: LLMsTxt
  url: llms/stackadapt-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stackadapt-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stackadapt-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/stackadapt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stackadapt-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stackadapt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stackadapt-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stackadapt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stackadapt-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stackadapt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.stackadapt.com/legal-document-centre/api-terms-and-conditions
- group: design
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
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackadapt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.stackadapt.com/trust-and-security-center
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stackadapt-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/stackadapt-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stackadapt-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/stackadapt-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-13'
description: StackAdapt is an AI-powered programmatic advertising platform with REST and GraphQL APIs for managing campaigns, ad groups, creatives, targeting segments, pixel tracking, and performance reporting across native, display, video, connected TV, audio, and digital out-of-home channels.
finops:
- name: Stackadapt Finops
  service_category: ''
  slug: stackadapt-finops
graphqls:
- description: StackAdapt is an AI-powered programmatic advertising platform (DSP) that provides a full-featured GraphQL API for creating and managing digital advertising campaigns across native, display, video, con
  name: StackAdapt GraphQL API
  slug: stackadapt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackadapt.png
layout: provider
mcp_servers:
- description: ''
  name: StackAdapt MCP Server
  slug: stackadapt-mcp-server
modified: '2026-08-13'
name: StackAdapt
nav: Providers
network: true
overview: 'StackAdapt publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Programmatic Advertising, Digital Advertising, Campaign Management, AdTech, and DSP.


  The StackAdapt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StackAdapt''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, signup flow, support, and 33 more developer resources.'
plans:
- name: Stackadapt Plans Pricing
  plan_count: 5
  slug: stackadapt-plans-pricing
random_paper: 6
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
  composite: 62.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 62.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackadapt/refs/heads/main/screenshots/stackadapt-2026-06-20T194444.png
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
slug: stackadapt
tags:
- Programmatic Advertising
- Digital Advertising
- Campaign Management
- AdTech
- DSP
- Demand-Side Platform
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
