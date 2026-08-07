---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-06'
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
artifact_total: 6
common:
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
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nift-well-known.yml
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
- group: design
  title: ''
  type: DataModel
  url: data-model/nift-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nift-domain-security.yml
created: '2026-07-17'
description: 'Nift is a customer-gifting and acquisition platform: businesses send "thank-you" gifts that let their own customers discover and try new brands, restaurants, and services, while the partnering brands gain new customers at the moment of gift selection. Proprietary AI matches each recipient to relevant gift options. For developers, Nift ships a partner integration surface: first-party SDKs (Web, iOS, Android, React Native) that embed the Nift gift-redemption "card flow" directly into a partner''s app, plus a server-side Partners API secured with OAuth 2.0 client credentials for looking up customer eligibility status and submitting GDPR-style customer deletion (anonymization) requests. Backed by Foundry Group.'
image: https://cdn.nift.me/assets/media_library/Nift-30-GiftCard-330af8982cf61d121b763521121a4025dd0f85b6010e361ebc736d0fa0d13d78.png
layout: provider
mcp_servers:
- description: ''
  name: nift-mcp.yml
  slug: nift-mcpyml
modified: '2026-07-20'
name: NIFT
nav: Providers
network: true
overview: 'NIFT publishes 1 API on the [APIs.io](https://apis.io/) network: Customers API. Tagged areas include Company, Marketing, Gifting, Customer Acquisition, and Loyalty.


  NIFT''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 94
scopes:
- name: Nift Scopes
  scope_count: 2
  slug: nift-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 43.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 68.2
    developer_ergonomics: 45.1
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Nift Authentication
  slug: nift-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nift Domain Security
  slug: nift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
