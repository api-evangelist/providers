---
access_model:
  confidence: high
  label: Paid plans with a 14-day free trial
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.callrail.com/pricing
  - plans/callrail-plans-pricing.yml
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Callrail Agentic Access
  operation_count: 8
  slug: callrail-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: REST API providing programmatic access to CallRail accounts, companies, tracking numbers, calls, text messages, form submissions, users, tags, and integrations. Requests authenticate via the HTTP head
  name: CallRail v3 API
  slug: v3-api
- description: CallRail's hosted Model Context Protocol server. Connects a CallRail account directly to AI assistants (Claude.ai, Claude Desktop, ChatGPT) over OAuth 2.0, exposing 36 tools — 22 read tools across acc
  name: CallRail MCP Server
  slug: mcp
- baseURL: https://api.callrail.com/v3/
  baseurl_source: declared
  description: The Accounts API from CallRail — 2 operation(s) for accounts.
  name: CallRail Accounts API
  slug: callrail-accounts-api
- baseURL: https://api.callrail.com/v3/
  baseurl_source: declared
  description: The Calls API from CallRail — 6 operation(s) for calls, including summary and time series reporting.
  name: CallRail Calls API
  slug: callrail-calls-api
artifact_total: 17
asyncapis:
- description: ''
  name: Callrail Webhooks
  slug: callrail-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CallRail v3 Accounts API
  slug: open-callrail-accounts-api
- collection_type: open
  name: CallRail v3 Accounts Calls API
  slug: open-callrail-calls-api
- collection_type: open
  name: CallRail v3 API
  slug: open-callrail
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/callrail-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.callrail.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/callrail-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/callrail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.callrail.com/security/disclosure
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/callrail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/callrail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/callrail-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/callrail-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/callrail-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/callrail-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/callrail-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/callrail-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/callrail-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.callrail.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/callrail-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/callrail-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/callrail-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/callrail-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/callrail-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/callrail-packages.yml
- group: design
  title: ''
  type: Components
  url: components/callrail-components.yml
- group: company
  title: ''
  type: Website
  url: https://www.callrail.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.callrail.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.callrail.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.callrail.com/#api
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.callrail.com/#getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.callrail.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.callrail.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.callrail.com/authenticate
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.callrail.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.callrail.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.callrail.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://support.callrail.com/hc/en-us/community/topics
- group: company
  title: ''
  type: Blog
  url: https://www.callrail.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CallRail
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/callrail
created: '2026-05-11'
description: CallRail is a call tracking and conversation intelligence platform that attributes phone calls, texts, and form fills to marketing campaigns and applies AI-powered transcription, sentiment, and lead scoring to inbound conversations. The CallRail v3 API is a REST/JSON interface exposing accounts, companies, trackers, calls, texts, form submissions, and integrations. Authentication uses an account API key passed in the HTTP Authorization header against a base URL of https://api.callrail.com/v3/.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/callrail.png
layout: provider
mcp_servers:
- description: 'CallRail publishes a hosted Model Context Protocol server documented in the MCP section of the v3 API reference. It is a read-only interface by default (a separate set of write tools is also exposed) '
  name: CallRail MCP Server
  slug: callrail-mcp-server
modified: '2026-08-14'
name: CallRail
nav: Providers
network: true
overview: 'CallRail publishes 2 APIs on the [APIs.io](https://apis.io/) network: Accounts API and Calls API. Tagged areas include Call Tracking, Conversation Intelligence, Marketing Attribution, Lead Tracking, and Telephony.


  The CallRail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CallRail''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Callrail Plans Pricing
  plan_count: 4
  slug: callrail-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Callrail Rate Limits
  slug: callrail-rate-limits
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 60.4
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/callrail/refs/heads/main/screenshots/callrail-2026-06-20T173850.png
security:
- kind: authentication
  name: Callrail Authentication
  slug: callrail-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Callrail Domain Security
  slug: callrail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Callrail Vulnerability Disclosure
  slug: callrail-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Callrail Trust Center
  slug: callrail-trust-center
  summary_line: ISO 42001, SOC 2 Type II, HIPAA/HITECH, PCI, GDPR, CCPA
slug: callrail
tags:
- Call Tracking
- Conversation Intelligence
- Marketing Attribution
- Lead Tracking
- Telephony
- Analytics
- Form Tracking
website: https://www.callrail.com
---
