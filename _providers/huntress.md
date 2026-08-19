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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Huntress Agentic Access
  operation_count: 92
  slug: huntress-agentic-access
  summary_line: 92 operations · 37 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Operations about Accounts
  name: Huntress Accounts API
  slug: huntress-accounts-api
- description: Operations about Actors
  name: Huntress Actor API
  slug: huntress-actor-api
- description: Operations about Agents
  name: Huntress Agents API
  slug: huntress-agents-api
- description: Operations about Escalations
  name: Huntress Escalations API
  slug: huntress-escalations-api
- description: Operations about External Recons
  name: Huntress External Recon API
  slug: huntress-external-recon-api
- description: Operations about Identities
  name: Huntress Identities API
  slug: huntress-identities-api
- description: Operations about Incident Reports
  name: Huntress Incident Reports API
  slug: huntress-incident-reports-api
- description: Operations about Invoices
  name: Huntress Invoices API
  slug: huntress-invoices-api
- description: Operations about Known VPNs
  name: Huntress Known VPNs API
  slug: huntress-known-vpns-api
- description: Operations about Organizations
  name: Huntress Organizations API
  slug: huntress-organizations-api
- description: Operations about Platform Actions
  name: Huntress Platform Actions API
  slug: huntress-platform-actions-api
- description: Operations for Reseller-level API credentials. These are mostly the same endpoints available in the rest of the API. However, the account ID is included in the URL, so that you can specify which accou
  name: Huntress Reseller API
  slug: huntress-reseller-api
- description: Query your SIEM logs programmatically using <a href="https://support.huntress.io/hc/en-us/articles/30113222043155-Searching-Logs-ESQL">ES|QL (Elasticsearch Query Language)</a>.
  name: Huntress SIEM API
  slug: huntress-siem-api
- description: Operations about Signals
  name: Huntress Signals API
  slug: huntress-signals-api
- description: Operations about Summary Reports
  name: Huntress Summary Reports API
  slug: huntress-summary-reports-api
- description: Operations about Unwanted Access Rules
  name: Huntress Unwanted Access Rules API
  slug: huntress-unwanted-access-rules-api
- description: Operations about Users
  name: Huntress Users API
  slug: huntress-users-api
artifact_total: 44
asyncapis:
- description: ''
  name: Huntress Webhooks
  slug: huntress-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Huntress API Reference Accounts API
  slug: open-huntress-accounts-api
- collection_type: open
  name: Huntress API Reference Accounts Actor API
  slug: open-huntress-actor-api
- collection_type: open
  name: Huntress API Reference Accounts Agents API
  slug: open-huntress-agents-api
- collection_type: open
  name: Huntress API Reference Accounts Escalations API
  slug: open-huntress-escalations-api
- collection_type: open
  name: Huntress API Reference Accounts External Recon API
  slug: open-huntress-external-recon-api
- collection_type: open
  name: Huntress API Reference Accounts Identities API
  slug: open-huntress-identities-api
- collection_type: open
  name: Huntress API Reference Accounts Incident Reports API
  slug: open-huntress-incident-reports-api
- collection_type: open
  name: Huntress API Reference Accounts Invoices API
  slug: open-huntress-invoices-api
- collection_type: open
  name: Huntress API Reference Accounts Known VPNs API
  slug: open-huntress-known-vpns-api
- collection_type: open
  name: Huntress API Reference Accounts Organizations API
  slug: open-huntress-organizations-api
- collection_type: open
  name: Huntress API Reference Accounts Platform Actions API
  slug: open-huntress-platform-actions-api
- collection_type: open
  name: Huntress API Reference Accounts Reseller API
  slug: open-huntress-reseller-api
- collection_type: open
  name: Huntress API Reference Accounts SIEM API
  slug: open-huntress-siem-api
- collection_type: open
  name: Huntress API Reference Accounts Signals API
  slug: open-huntress-signals-api
- collection_type: open
  name: Huntress API Reference Accounts Summary Reports API
  slug: open-huntress-summary-reports-api
- collection_type: open
  name: Huntress API Reference Accounts Unwanted Access Rules API
  slug: open-huntress-unwanted-access-rules-api
- collection_type: open
  name: Huntress API Reference Accounts Users API
  slug: open-huntress-users-api
- collection_type: open
  name: Huntress Webhooks
  slug: open-huntress-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.huntress.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.huntress.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.huntress.io/docs
- group: operate
  title: ''
  type: Support
  url: https://support.huntress.io
- group: company
  title: ''
  type: Blog
  url: https://www.huntress.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/huntresslabs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.huntress.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.huntress.com/start-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.huntress.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.huntress.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huntress.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/huntress-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/huntress-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/huntress-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/huntress-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/huntress-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/huntress-rest-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/huntress-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.huntress.com
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/huntress-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/huntress-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/huntress-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/huntress-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/huntress-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/huntress-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://support.huntress.io/hc/en-us/articles/24119617302291-Huntress-Vulnerability-Disclosure-Program-Terms-and-Conditions
- group: auth
  title: ''
  type: TrustCenter
  url: security/huntress-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/huntress-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huntress-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/huntress-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/huntress-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.huntress.com
created: '2026-07-17'
description: Huntress is a managed cybersecurity platform built for small and mid-sized businesses and the MSPs/MSSPs that serve them, pairing purpose-built software with a human-powered 24/7 Security Operations Center (SOC). Its products span Managed EDR (including macOS and Managed Microsoft Defender), Managed ITDR for Microsoft 365 identities, Managed SIEM, and Managed Security Awareness Training. The Huntress REST API (api.huntress.io/v1) gives partners programmatic access to accounts, organizations, agents, incident reports, remediations, escalations, platform actions, signals, external recon, billing and reseller subscriptions, plus a SIEM ES|QL query endpoint — secured with HTTP Basic API keys, cursor-paginated, with real-time webhooks and an official remote MCP server for AI agents.
image: https://huntresscdn.com/portal/assets/huntress_logo_wide_teal_small-34bc9ba6.png
layout: provider
mcp_servers:
- description: ''
  name: huntress-mcp.yml
  slug: huntress-mcpyml
modified: '2026-07-19'
name: Huntress
nav: Providers
network: true
overview: 'Huntress publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Actor API, Agents API, and 14 more. Tagged areas include Company, Security, Cybersecurity, Managed Detection and Response, and Endpoint Security.


  The Huntress catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Huntress'' developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 26 more developer resources.'
random_paper: 147
scopes:
- name: Huntress Scopes
  scope_count: 1
  slug: huntress-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.7
  delta: -2.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 64.9
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huntress/refs/heads/main/screenshots/huntress-2026-07-25T221735.png
security:
- kind: authentication
  name: Huntress Authentication
  slug: huntress-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Huntress Domain Security
  slug: huntress-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Huntress Vulnerability Disclosure
  slug: huntress-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Huntress Trust Center
  slug: huntress-trust-center
  summary_line: SOC 2, GDPR
slug: huntress
tags:
- Company
- Security
- Cybersecurity
- Managed Detection and Response
- Endpoint Security
- SOC
- SIEM
- Identity Threat Detection
- MSP
- Webhooks
website: https://www.huntress.com
---
