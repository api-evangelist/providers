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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Leadspace Agentic Access
  operation_count: 9
  slug: leadspace-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 5
apis:
- description: OAuth 2.0 token issuance and refresh
  name: Leadspace Authorization API
  slug: leadspace-authorization-api
- description: Bulk account expansion into net-new contacts
  name: Leadspace Discovery API
  slug: leadspace-discovery-api
- description: Single and bulk person and company enrichment
  name: Leadspace Enrichment API
  slug: leadspace-enrichment-api
- description: Buyer-intent scoring and refresh
  name: Leadspace Intent API
  slug: leadspace-intent-api
- description: Polling for asynchronous discovery results
  name: Leadspace Results API
  slug: leadspace-results-api
artifact_total: 12
asyncapis:
- description: ''
  name: Leadspace Callbacks Webhooks
  slug: leadspace-callbacks-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leadspace-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.leadspace.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.leadspace.com/hc/en-us/categories/5940743388306-Developer-Guides
- group: docs
  title: ''
  type: Documentation
  url: https://support.leadspace.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://support.leadspace.com/hc/en-us/sections/201997649-API
- group: start
  title: ''
  type: GettingStarted
  url: https://support.leadspace.com/hc/en-us/categories/5778624503826-Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://support.leadspace.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.leadspace.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadspace
- group: start
  title: ''
  type: SignUp
  url: https://studio.leadspace.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leadspace.com/service-support-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leadspace.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadspace.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/leadspace-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leadspace-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leadspace-changelog.yml
- group: operate
  title: ''
  type: ChangeLogPage
  url: https://support.leadspace.com/hc/en-us/categories/7154652740626-Release-Notes
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadspace-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leadspace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leadspace-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/leadspace-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leadspace-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leadspace-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/leadspace-examples.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leadspace-callbacks-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leadspace-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://support.leadspace.com/hc/en-us/articles/360012276859-General-Statement-of-Information-Security-and-Privacy
- group: auth
  title: ''
  type: Security
  url: https://www.leadspace.com/report-a-vulnerability
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadspace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadspace-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leadspace-well-known.yml
- group: design
  title: ''
  type: Components
  url: components/leadspace-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leadspace-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leadspace-llms.txt
created: '2026-07-17'
description: Leadspace is a B2B GTM Data Intelligence Cloud and customer data platform that unifies buyer data, account data, and buying signals into the Leadspace Universal Graph. Its API-first enrichment service resolves partial person and company records into full profiles carrying firmographics (SIC, NAICS, industry, revenue, employee counts), corporate family-tree hierarchy, department sizes, funding and investor history, installed-base and website technology signals, weekly buyer-intent models sourced from Leadspace Intent and Bombora, and persona and predictive fit scores. Leadspace exposes single and bulk enrichment, contact discovery (account expansion), and an intent-only refresh API over a single gateway, alongside Leadspace Studio for segment building and SmartForms for real-time inbound web-form enrichment. It integrates with Salesforce, Marketo, Eloqua, and HubSpot. Leadspace is ISO 27001 certified and SOC 2 Type II audited.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadspace.png
layout: provider
mcp_servers:
- description: ''
  name: leadspace-mcp.yml
  slug: leadspace-mcpyml
modified: '2026-07-19'
name: Leadspace
nav: Providers
network: true
overview: 'Leadspace publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Discovery API, Enrichment API, and 2 more. Tagged areas include B2B Data, Customer Data Platform, Data Enrichment, Intent Data, and Sales Intelligence.


  The Leadspace catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leadspace''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 28 more developer resources.'
random_paper: 61
rate_limits:
- limit_count: 0
  name: Leadspace Rate Limits
  slug: leadspace-rate-limits
score:
  band: strong
  composite: 57.5
  delta: -0.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 71.7
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 58.4
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/screenshots/leadspace-2026-07-25T224715.png
security:
- kind: authentication
  name: Leadspace Authentication
  slug: leadspace-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Leadspace Domain Security
  slug: leadspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leadspace Vulnerability Disclosure
  slug: leadspace-vulnerability-disclosure
  summary_line: contact published
slug: leadspace
tags:
- B2B Data
- Customer Data Platform
- Data Enrichment
- Intent Data
- Sales Intelligence
- Account-Based Marketing
- Identity Resolution
- Firmographics
- Lead Scoring
- Company
website: https://www.leadspace.com/
---
