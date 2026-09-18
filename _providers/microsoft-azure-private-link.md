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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Private Link Agentic Access
  operation_count: 7
  slug: microsoft-azure-private-link-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: microsoft-azure-private-link Operations API
  slug: microsoft-azure-private-link-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Private Endpoints operations
  name: microsoft-azure-private-link Private Endpoints API
  slug: microsoft-azure-private-link-private-endpoints-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Private Link REST Operations API
  slug: open-microsoft-azure-private-link-operations-api
- collection_type: open
  name: Azure Private Link REST Operations Private Endpoints API
  slug: open-microsoft-azure-private-link-private-endpoints-api
- collection_type: open
  name: Azure Private Link REST API
  slug: open-microsoft-azure-private-link
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/private-link/private-link-overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/private-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal
- group: start
  title: ''
  type: Quickstart
  url: https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/azurenetworkingblog
- group: operate
  title: ''
  type: Roadmap
  url: https://azure.microsoft.com/en-us/updates/?category=networking
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/private-link/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/plans/microsoft-azure-private-link-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-private-link-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
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
  url: https://azure.microsoft.com/en-us/support/options/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/agentic-access/microsoft-azure-private-link-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-private-link-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/authentication/microsoft-azure-private-link-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-private-link-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/scopes/microsoft-azure-private-link-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-private-link-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/conventions/microsoft-azure-private-link-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-private-link-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/conventions/microsoft-azure-private-link-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-private-link-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/errors/microsoft-azure-private-link-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-private-link-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/rate-limits/microsoft-azure-private-link-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-private-link-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/data-model/microsoft-azure-private-link-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-private-link-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/lifecycle/microsoft-azure-private-link-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-private-link-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  title: ''
  type: Deprecation
  url: https://azure.microsoft.com/en-us/updates/?updateType=retirements
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/changelog/microsoft-azure-private-link-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-private-link-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/packages/microsoft-azure-private-link-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-private-link-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/packages/microsoft-azure-private-link-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-private-link-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/cli/microsoft-azure-private-link-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-private-link-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/llms/microsoft-azure-private-link-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-private-link-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/conformance/microsoft-azure-private-link-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-private-link-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/security/microsoft-azure-private-link-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-private-link-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/cvd
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/security/microsoft-azure-private-link-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-private-link-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/well-known/microsoft-azure-private-link-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-private-link-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/well-known/microsoft-azure-private-link-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-private-link-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/security/microsoft-azure-private-link-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-private-link-domain-security.yml
created: '2026-05-04'
description: 'Microsoft Azure Private Link gives a virtual network a private IP address onto an Azure PaaS service, a partner service, or a service the customer publishes themselves, so traffic reaches it across the Microsoft backbone and never traverses the public internet. It has two sides. A consumer creates a private endpoint pointing at a target resource id and attaches a private DNS zone group so the service''s own hostname resolves to that private address. A producer publishes a private link service in front of a Standard Load Balancer, hands out an opaque alias, and approves or rejects the connections that arrive — including connections from other tenants. Both sides are managed through the Azure Resource Manager REST API at management.azure.com, which Microsoft publishes as Swagger 2.0 in its azure-rest-api-specs repository: 24 operations at api-version 2025-03-01, OAuth2 bearer only, with no API key and no anonymous surface.'
finops:
- name: Microsoft Azure Private Link Finops
  service_category: API
  slug: microsoft-azure-private-link-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-private-link.png
layout: provider
modified: '2026-09-17'
name: Microsoft Azure Private Link
nav: Providers
network: true
overview: 'Microsoft Azure Private Link publishes 2 APIs on the [APIs.io](https://apis.io/) network: microsoft-azure-private-link Operations API and microsoft-azure-private-link Private Endpoints API. Tagged areas include Networking, Private Connectivity, Cloud Infrastructure, Virtual Networks, and DNS.


  Microsoft Azure Private Link''s developer surface includes developer portal, documentation, API reference, getting-started guide, quickstart, engineering blog, pricing, and 34 more developer resources.'
plans:
- name: Microsoft Azure Private Link Plans Pricing
  plan_count: 0
  slug: microsoft-azure-private-link-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Microsoft Azure Private Link Rate Limits
  slug: microsoft-azure-private-link-rate-limits
scopes:
- name: Microsoft Azure Private Link Scopes
  scope_count: 1
  slug: microsoft-azure-private-link-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.5
  facets:
    access_clarity: 68.4
    contract_governance: 4.5
    contract_quality: 45.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 89.5
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/screenshots/microsoft-azure-private-link-2026-06-20T185432.png
security:
- kind: authentication
  name: Microsoft Azure Private Link Authentication
  slug: microsoft-azure-private-link-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Private Link Domain Security
  slug: microsoft-azure-private-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Private Link Vulnerability Disclosure
  slug: microsoft-azure-private-link-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Private Link Trust Center
  slug: microsoft-azure-private-link-trust-center
  summary_line: GDPR
slug: microsoft-azure-private-link
tags:
- Networking
- Private Connectivity
- Cloud Infrastructure
- Virtual Networks
- DNS
- Security
- Azure Resource Manager
- Infrastructure-as-a-Service
website: https://www.microsoft.com/
---
