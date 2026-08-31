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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Microsoft Linkedin Agentic Access
  operation_count: 17
  slug: microsoft-linkedin-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- description: The LinkedIn Marketing API enables programmatic management of LinkedIn advertising campaigns, audience targeting, creative assets, and performance reporting. Developers can create sponsored content, m
  name: LinkedIn Marketing API
  slug: marketing-api
- description: 'The LinkedIn Consumer API provides access to member profiles, sign-in with LinkedIn, and content sharing capabilities. Developers can implement social sign-on, retrieve basic profile information, and '
  name: LinkedIn Consumer API
  slug: consumer-api
- description: The LinkedIn Talent Solutions API provides access to recruiting and talent management capabilities. It enables integration with applicant tracking systems, job posting management, candidate search, an
  name: LinkedIn Talent Solutions API
  slug: talent-solutions-api
- description: Manage ad accounts
  name: Microsoft LinkedIn AdAccounts API
  slug: microsoft-linkedin-adaccounts-api
- description: Manage ad account user permissions
  name: Microsoft LinkedIn AdAccountUsers API
  slug: microsoft-linkedin-adaccountusers-api
- description: Manage campaign groups
  name: Microsoft LinkedIn AdCampaignGroups API
  slug: microsoft-linkedin-adcampaigngroups-api
- description: Manage campaigns
  name: Microsoft LinkedIn AdCampaigns API
  slug: microsoft-linkedin-adcampaigns-api
- description: Manage creatives
  name: Microsoft LinkedIn AdCreatives API
  slug: microsoft-linkedin-adcreatives-api
artifact_total: 26
asyncapis:
- description: ''
  name: Microsoft Linkedin Webhooks
  slug: microsoft-linkedin-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LinkedIn Marketing AdAccounts API
  slug: open-microsoft-linkedin-adaccounts-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdAccountUsers API
  slug: open-microsoft-linkedin-adaccountusers-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdCampaignGroups API
  slug: open-microsoft-linkedin-adcampaigngroups-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdCampaigns API
  slug: open-microsoft-linkedin-adcampaigns-api
- collection_type: open
  name: LinkedIn Marketing AdAccounts AdCreatives API
  slug: open-microsoft-linkedin-adcreatives-api
- collection_type: open
  name: LinkedIn Marketing API
  slug: open-microsoft-linkedin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-linkedin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-linkedin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-linkedin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-linkedin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-linkedin-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkedin
- group: start
  title: ''
  type: Portal
  url: https://developer.linkedin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linkedin.com/legal/l/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linkedin.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.linkedin.com/help/linkedin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.linkedin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/linkedin/shared/references/v2/object-types
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/linkedin/marketing/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://www.linkedin.com/developers/apps/new
- group: company
  title: ''
  type: Blog
  url: https://www.linkedin.com/developers/news
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-marketing-solutions-versioned-apis/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://www.linkedin-apistatus.com/
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-linkedin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/microsoft-linkedin-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-linkedin-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-linkedin-security.txt
- group: auth
  title: ''
  type: Security
  url: security/microsoft-linkedin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-linkedin-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/microsoft-linkedin-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-linkedin-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-linkedin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-linkedin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-linkedin-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-linkedin-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-linkedin-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-linkedin-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-linkedin-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-linkedin-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-linkedin-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-linkedin-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-linkedin-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-linkedin-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-linkedin-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/microsoft-linkedin-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/microsoft-linkedin-finops.yml
created: '2024-01-01'
description: LinkedIn, owned by Microsoft, operates a versioned Rest.li API platform covering advertising and marketing, company page and community management, talent and recruiting, sales navigation, learning, and consumer sign-in. The versioned Marketing surface lives under https://api.linkedin.com/rest/ and requires a Linkedin-Version YYYYMM header on every call, with each monthly version supported for a minimum of twelve months before it is sunset. Authentication is OAuth 2.0, and Sign In with LinkedIn is a conformant OpenID Connect provider with a live discovery document. Access to the Marketing, Talent, Sales and Learning APIs is gated behind product approval and, in most cases, a commercial partner relationship; LinkedIn publishes no API pricing and no OpenAPI definitions of its own.
finops:
- name: Microsoft Linkedin Finops
  service_category: API
  slug: microsoft-linkedin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-linkedin.png
layout: provider
mcp_servers:
- description: LinkedIn publishes no MCP server. Every LinkedIn MCP server in circulation is community-built on top of either the public API or the unofficial Voyager endpoints. The tool list below is an API Evangel
  name: Microsoft LinkedIn MCP Server
  slug: microsoft-linkedin-mcp-server
modified: '2026-08-13'
name: Microsoft LinkedIn
nav: Providers
network: true
overview: 'Microsoft LinkedIn publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AdAccounts API, AdAccountUsers API, AdCampaignGroups API, and 2 more. Tagged areas include Marketing, Microsoft, Professional Networking, Recruiting, and Social Network.


  The Microsoft LinkedIn catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Microsoft LinkedIn''s developer surface includes authentication, developer portal, documentation, support, API reference, getting-started guide, signup flow, and 37 more developer resources.'
plans:
- name: Microsoft Linkedin Plans Pricing
  plan_count: 0
  slug: microsoft-linkedin-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Microsoft Linkedin Rate Limits
  slug: microsoft-linkedin-rate-limits
scopes:
- name: Microsoft Linkedin Scopes
  scope_count: 5
  slug: microsoft-linkedin-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 26
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 61.9
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-linkedin/refs/heads/main/screenshots/microsoft-linkedin-2026-06-20T185506.png
security:
- kind: authentication
  name: Microsoft Linkedin Authentication
  slug: microsoft-linkedin-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Linkedin Domain Security
  slug: microsoft-linkedin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Linkedin Vulnerability Disclosure
  slug: microsoft-linkedin-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Microsoft Linkedin Trust Center
  slug: microsoft-linkedin-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27018, ISO 22301, SOC 2 Type II, PCI DSS
slug: microsoft-linkedin
tags:
- Marketing
- Microsoft
- Professional Networking
- Recruiting
- Social Network
website: https://developer.linkedin.com/
---
