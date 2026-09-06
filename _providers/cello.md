---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cello Agentic Access
  operation_count: 6
  slug: cello-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.cello.so
  baseurl_source: declared
  description: The Events API from Cello — 1 operation(s) for events.
  name: Cello Events API
  slug: cello-events-api
- baseURL: https://api.cello.so
  baseurl_source: declared
  description: The New Users API from Cello — 1 operation(s) for new users.
  name: Cello New Users API
  slug: cello-new-users-api
- baseURL: https://api.cello.so
  baseurl_source: declared
  description: The Referral Codes API from Cello — 2 operation(s) for referral codes.
  name: Cello Referral Codes API
  slug: cello-referral-codes-api
- baseURL: https://api.cello.so
  baseurl_source: declared
  description: The Referrers API from Cello — 1 operation(s) for referrers.
  name: Cello Referrers API
  slug: cello-referrers-api
- baseURL: https://api.cello.so
  baseurl_source: declared
  description: The Token API from Cello — 1 operation(s) for token.
  name: Cello Token API
  slug: cello-token-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cello Events API
  slug: open-cello-events-api
- collection_type: open
  name: Cello Events New Users API
  slug: open-cello-new-users-api
- collection_type: open
  name: Cello Events Referral Codes API
  slug: open-cello-referral-codes-api
- collection_type: open
  name: Cello Events Referrers API
  slug: open-cello-referrers-api
- collection_type: open
  name: Cello Events Token API
  slug: open-cello-token-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cello-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cello-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cello-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cello-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cello.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cello.so
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cello.so/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cello.so/integration-overview
- group: operate
  title: ''
  type: Support
  url: https://docs.cello.so/guides/support/faqs
- group: company
  title: ''
  type: Blog
  url: https://cello.so/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getcello
- group: commercial
  title: ''
  type: Pricing
  url: https://cello.so/pricing/
- group: start
  title: ''
  type: Login
  url: https://portal.cello.so
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cello.so/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cello.so/privacy-policy/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cello-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cello-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cello-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cello-packages.yml
- group: design
  title: ''
  type: Components
  url: components/cello-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cello-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cello-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cello-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cello-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cello-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cello-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cello-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cello.so/privacy-policy/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cello-track-referral-conversion.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cello-fetch-and-reward-referee.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cello-referral-integration.md
- group: other
  title: ''
  type: AgentCard
  url: a2a/cello-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cello-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cello-scopes.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cello-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cello-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cello-rate-limits.yml
created: '2026-07-17'
description: Cello is an all-in-one, AI-powered referral platform for SaaS companies. It lets product teams embed in-product user referrals and run partner/affiliate programs with a few lines of code, then automates attribution, campaigns, notifications, fraud detection, and cross-border payouts. Cello ships an embeddable Referral Component and Attribution JS SDK for web plus native iOS, Android, Flutter, and React Native SDKs, a REST API for tokens, referral-code validation, events, and new-user rewards, a Growth Portal for analytics, and an official hosted MCP server exposing developer and growth-manager tools. Customers include Typeform, Miro, Descript, Pleo, and SmallPDF. Backed by HV Capital.
image: https://cello.so/wp-content/uploads/2022/12/Group-174900-1.png
layout: provider
mcp_servers:
- description: ''
  name: Cello MCP Server
  slug: cello-mcp-server
modified: '2026-08-13'
name: Cello
nav: Providers
network: true
overview: 'Cello publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Events API, New Users API, Referral Codes API, and 2 more. Tagged areas include Company, Referral Marketing, Affiliate Marketing, Growth, and Software-as-a-Service.


  Cello''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Cello Plans Pricing
  plan_count: 7
  slug: cello-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Cello Rate Limits
  slug: cello-rate-limits
scopes:
- name: Cello Scopes
  scope_count: 0
  slug: cello-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 49.9
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cello/refs/heads/main/screenshots/cello-2026-07-25T204908.png
security:
- kind: authentication
  name: Cello Authentication
  slug: cello-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Cello Domain Security
  slug: cello-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cello
tags:
- Company
- Referral Marketing
- Affiliate Marketing
- Growth
- Software-as-a-Service
- Attribution
- Partner Programs
- Ai Enterprise Software
website: https://docs.cello.so
---
