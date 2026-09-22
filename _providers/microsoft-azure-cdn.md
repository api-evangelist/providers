---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 78
  human_in_the_loop: 2
  name: Microsoft Azure Cdn Agentic Access
  operation_count: 122
  slug: microsoft-azure-cdn-agentic-access
  summary_line: 122 operations · 78 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The contract Microsoft publishes for the Microsoft.Cdn resource provider, harvested verbatim from Azure/azure-rest-api-specs at api-version 2026-07-01. Swagger 2.0, 73 paths, 115 operations, 387 defin
  name: Azure CDN Management API (Microsoft.Cdn)
  slug: microsoft-azure-cdn-management-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: microsoft-azure-cdn Operations API
  slug: microsoft-azure-cdn-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Profiles operations
  name: microsoft-azure-cdn Profiles API
  slug: microsoft-azure-cdn-profiles-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure CDN REST Operations API
  slug: open-microsoft-azure-cdn-operations-api
- collection_type: open
  name: Azure CDN REST Operations Profiles API
  slug: open-microsoft-azure-cdn-profiles-api
- collection_type: open
  name: Azure CDN REST API
  slug: open-microsoft-azure-cdn
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/security/microsoft-azure-cdn-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-cdn-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/security/microsoft-azure-cdn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-cdn-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/agentic-access/microsoft-azure-cdn-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cdn-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/security/microsoft-azure-cdn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cdn-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/authentication/microsoft-azure-cdn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cdn-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/scopes/microsoft-azure-cdn-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-cdn-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/rest/api/cdn/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/frontdoor/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/cdn/profiles
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/frontdoor/create-front-door-portal
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/lifecycle/microsoft-azure-cdn-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-azure-cdn-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/lifecycle/microsoft-azure-cdn-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-cdn-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/changelog/microsoft-azure-cdn-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-cdn-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/cli/microsoft-azure-cdn-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-cdn-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/packages/microsoft-azure-cdn-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-cdn-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/packages/microsoft-azure-cdn-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-cdn-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/conventions/microsoft-azure-cdn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-cdn-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/conventions/microsoft-azure-cdn-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-cdn-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/conformance/microsoft-azure-cdn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-cdn-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/security/microsoft-azure-cdn-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-cdn-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/well-known/microsoft-azure-cdn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-cdn-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/well-known/microsoft-azure-cdn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-cdn-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/mcp/microsoft-azure-cdn-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-cdn-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/mcp/microsoft-azure-cdn-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-cdn-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/llms/microsoft-azure-cdn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-cdn-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/errors/microsoft-azure-cdn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-cdn-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/data-model/microsoft-azure-cdn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-cdn-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/plans/microsoft-azure-cdn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-cdn-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/rate-limits/microsoft-azure-cdn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-cdn-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/finops/microsoft-azure-cdn-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-cdn-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/examples/microsoft-azure-cdn-examples.yml
  title: ''
  type: Examples
  url: examples/microsoft-azure-cdn-examples.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/overlays/microsoft-azure-cdn-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-cdn-management-overlay.yaml
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
created: '2026-03-13'
description: 'Azure Content Delivery Network (CDN) caches static web content at strategically placed edge locations to deliver it to users with maximum throughput and minimum latency. The product is operated through the Microsoft.Cdn Azure Resource Manager resource provider, a 115-operation REST contract on management.azure.com that manages CDN profiles, delivery endpoints, origins, origin groups, custom domains and web application firewall policies, and that also serves the Azure Front Door Standard and Premium resource family. Authentication is Microsoft Entra ID OAuth 2.0 with authorization decided by Azure RBAC. Azure CDN Standard from Microsoft (classic) is on a published retirement path: it stopped accepting new instances in 2025 and retires on 30 September 2027, with Microsoft directing customers to Azure Front Door and shipping a validate/migrate/commit API path for the move.'
finops:
- name: Microsoft Azure Cdn Finops
  service_category: API
  slug: microsoft-azure-cdn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cdn.png
layout: provider
mcp_servers:
- description: ''
  name: Microsoft Azure Cdn MCP Server
  slug: microsoft-azure-cdn-mcp-server
modified: '2026-09-17'
name: Microsoft Azure Cdn
nav: Providers
network: true
overview: 'Microsoft Azure Cdn publishes 3 APIs on the [APIs.io](https://apis.io/) network: Azure CDN Management API (Microsoft.Cdn), microsoft-azure-cdn Operations API, and microsoft-azure-cdn Profiles API. Tagged areas include CDN, Edge, Caching, Cloud Infrastructure, and Networking.


  Microsoft Azure Cdn''s developer surface includes authentication, developer portal, pricing, support, engineering blog, documentation, API reference, and 38 more developer resources.'
plans:
- name: Microsoft Azure Cdn Plans Pricing
  plan_count: 3
  slug: microsoft-azure-cdn-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Microsoft Azure Cdn Rate Limits
  slug: microsoft-azure-cdn-rate-limits
scopes:
- name: Microsoft Azure Cdn Scopes
  scope_count: 2
  slug: microsoft-azure-cdn-scopes
  summary_line: 2 scopes · implicit
score:
  band: exemplar
  composite: 68.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cdn/refs/heads/main/screenshots/microsoft-azure-cdn-2026-06-20T185404.png
security:
- kind: authentication
  name: Microsoft Azure Cdn Authentication
  slug: microsoft-azure-cdn-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cdn Domain Security
  slug: microsoft-azure-cdn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Cdn Vulnerability Disclosure
  slug: microsoft-azure-cdn-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Cdn Trust Center
  slug: microsoft-azure-cdn-trust-center
  summary_line: GDPR
slug: microsoft-azure-cdn
tags:
- CDN
- Edge
- Caching
- Cloud Infrastructure
- Networking
- Web Performance
- Azure
- Content Delivery
- Web Application Firewall
website: https://www.microsoft.com/
---
