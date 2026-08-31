---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans/nift-plans-pricing.yml
  - https://github.com/nift-sdks/nift-flow-sdk-docs/blob/main/docs/sdk/customer-status-server.md
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nift Agentic Access
  operation_count: 2
  slug: nift-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Customer status and deletion operations for partners.
  name: NIFT Customers API
  slug: nift-customers-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nift Partners Customers API
  slug: open-nift-customers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nift-partners-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.gonift.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/nift-sdks/nift-flow-sdk-docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/nift-sdks/nift-flow-sdk-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/nift-sdks/nift-flow-sdk-docs/blob/main/docs/sdk/web.md#quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nift-sdks
- group: operate
  title: ''
  type: Support
  url: https://www.gonift.com/contact_us/
- group: company
  title: ''
  type: Blog
  url: https://www.gonift.com/business/newsroom/
- group: start
  title: ''
  type: SignUp
  url: https://www.gonift.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gonift.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gonift.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/nift-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nift-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nift-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/nift-packages.yml
- group: design
  title: ''
  type: Components
  url: components/nift-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nift-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nift-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nift-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nift-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/nift-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nift-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nift-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nift-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nift-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/nift-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nift-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nift-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gonift.com/business/vulnerability-disclosure-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/nift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nift-rate-limits.yml
created: '2026-07-17'
description: 'Nift is a customer-gifting and acquisition platform: businesses send "thank-you" gifts that let their own customers discover and try new brands, restaurants, and services, while the partnering brands gain new customers at the moment of gift selection. Proprietary AI matches each recipient to relevant gift options. For developers, Nift ships a partner integration surface: first-party SDKs (Web, iOS, Android, React Native) that embed the Nift gift-redemption "card flow" directly into a partner''s app, plus a server-side Partners API secured with OAuth 2.0 client credentials for looking up customer eligibility status and submitting GDPR-style customer deletion (anonymization) requests. Backed by Foundry Group.'
image: https://cdn.nift.me/assets/media_library/Nift-30-GiftCard-330af8982cf61d121b763521121a4025dd0f85b6010e361ebc736d0fa0d13d78.png
layout: provider
mcp_servers:
- description: ''
  name: NIFT MCP Server
  slug: nift-mcp-server
modified: '2026-08-13'
name: NIFT
nav: Providers
network: true
overview: 'NIFT publishes 1 API on the [APIs.io](https://apis.io/) network: Customers API. Tagged areas include Company, Marketing, Gifting, Customer Acquisition, and Loyalty.


  NIFT''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Nift Plans Pricing
  plan_count: 0
  slug: nift-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Nift Rate Limits
  slug: nift-rate-limits
scopes:
- name: Nift Scopes
  scope_count: 2
  slug: nift-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 15.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nift/refs/heads/main/screenshots/nift-2026-08-07T185254.png
security:
- kind: authentication
  name: Nift Authentication
  slug: nift-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nift Domain Security
  slug: nift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nift Vulnerability Disclosure
  slug: nift-vulnerability-disclosure
  summary_line: contact published
slug: nift
tags:
- Company
- Marketing
- Gifting
- Customer Acquisition
- Loyalty
- Rewards
- SDK
- Partners
website: https://www.gonift.com
---
