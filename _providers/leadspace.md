---
access_model:
  confidence: high
  label: Free tier, self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://www.leadspace.com/solutions/sidekick/pricing
  - https://www.leadspace.com/solutions/leadspace-mcp
  - plans/leadspace-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-09-14'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Leadspace Agentic Access
  operation_count: 9
  slug: leadspace-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 3
apis:
- baseURL: https://apigw.leadspace.com
  baseurl_source: declared
  description: OAuth 2.0 token issuance and refresh
  name: Leadspace Authorization API
  slug: leadspace-authorization-api
- baseURL: https://apigw.leadspace.com
  baseurl_source: declared
  description: Bulk account expansion into net-new contacts
  name: Leadspace Discovery API
  slug: leadspace-discovery-api
- baseURL: https://apigw.leadspace.com
  baseurl_source: declared
  description: Single and bulk person and company enrichment
  name: Leadspace Enrichment API
  slug: leadspace-enrichment-api
- baseURL: https://apigw.leadspace.com
  baseurl_source: declared
  description: Buyer-intent scoring and refresh
  name: Leadspace Intent API
  slug: leadspace-intent-api
- description: 'Hosted remote MCP server exposing the Leadspace GTM Data Intelligence Cloud to AI assistants as a custom connector — account intelligence, company and contact lookup, verified email and phone reveal, '
  name: Leadspace MCP
  slug: leadspace-mcp-server
- baseURL: https://apigw.leadspace.com
  baseurl_source: declared
  description: Polling for asynchronous discovery results
  name: Leadspace Results API
  slug: leadspace-results-api
artifact_total: 22
asyncapis:
- description: ''
  name: Leadspace Callbacks Webhooks
  slug: leadspace-callbacks-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Leadspace Discovery Authorization API
  slug: open-leadspace-authorization-api
- collection_type: open
  name: Leadspace Authorization Discovery API
  slug: open-leadspace-discovery-api
- collection_type: open
  name: Leadspace Discovery Authorization Enrichment API
  slug: open-leadspace-enrichment-api
- collection_type: open
  name: Leadspace Discovery Authorization Intent API
  slug: open-leadspace-intent-api
- collection_type: open
  name: Leadspace Discovery Authorization Results API
  slug: open-leadspace-results-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/overlays/leadspace-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leadspace-discovery-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/agentic-access/leadspace-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/lifecycle/leadspace-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/leadspace-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/lifecycle/leadspace-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leadspace-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/changelog/leadspace-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leadspace-changelog.yml
- group: operate
  title: ''
  type: ChangeLogPage
  url: https://support.leadspace.com/hc/en-us/categories/7154652740626-Release-Notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/authentication/leadspace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leadspace-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/conventions/leadspace-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leadspace-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/errors/leadspace-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leadspace-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/errors/leadspace-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/leadspace-error-codes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/rate-limits/leadspace-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leadspace-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/data-model/leadspace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leadspace-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/examples/leadspace-examples.yml
  title: ''
  type: Examples
  url: examples/leadspace-examples.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/asyncapi/leadspace-callbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/leadspace-callbacks-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/conformance/leadspace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leadspace-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.leadspace.com/platform/security-and-compliance
- group: auth
  title: ''
  type: Security
  url: https://www.leadspace.com/report-a-vulnerability
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/security/leadspace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadspace-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/security/leadspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leadspace-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/well-known/leadspace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leadspace-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/components/leadspace-components.yml
  title: ''
  type: Components
  url: components/leadspace-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/mcp/leadspace-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leadspace-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/mcp/leadspace-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/leadspace-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/scopes/leadspace-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leadspace-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/security/leadspace-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/leadspace-trust-center.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/plans/leadspace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leadspace-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leadspace.com/solutions/sidekick/pricing
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/packages/leadspace-packages.yml
  title: ''
  type: Packages
  url: packages/leadspace-packages.yml
- group: start
  title: ''
  type: Login
  url: https://skprod.leadspace.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/llms/leadspace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leadspace-llms.txt
created: '2026-07-17'
description: 'Leadspace is a B2B GTM Data Intelligence Cloud and customer data platform that unifies buyer data, account data, and buying signals into the Leadspace Universal Graph. Its API-first enrichment service resolves partial person and company records into full profiles carrying firmographics (SIC, NAICS, industry, revenue, employee counts), corporate family-tree hierarchy, department sizes, funding and investor history, installed-base and website technology signals, weekly buyer-intent models sourced from Leadspace Intent and Bombora, and persona and predictive fit scores. Leadspace exposes single and bulk enrichment, contact discovery (account expansion), and an intent-only refresh API over a single gateway, alongside Leadspace Studio for segment building and SmartForms for real-time inbound web-form enrichment. As of 2026 Leadspace also ships two self-serve agent-facing products that share one account: Leadspace Sidekick, a Chrome extension overlaying verified contact data and
  fit scoring on LinkedIn, and Leadspace MCP, a hosted remote Model Context Protocol server that plugs the same data graph into Claude, ChatGPT and any MCP-compatible client with per-user OAuth. It integrates with Salesforce, Marketo, Eloqua, and HubSpot. Leadspace is ISO 27001 certified and SOC 2 Type II audited.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadspace.png
layout: provider
mcp_servers:
- description: ''
  name: Leadspace MCP Server
  slug: leadspace-mcp-server
modified: '2026-08-13'
name: Leadspace
nav: Providers
network: true
overview: 'Leadspace publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Discovery API, Enrichment API, and 2 more. Tagged areas include MCP, AI Agents, B2B Data, Customer Data Platform, and Data Enrichment.


  The Leadspace catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leadspace''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 36 more developer resources.'
plans:
- name: Leadspace Plans Pricing
  plan_count: 4
  slug: leadspace-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Leadspace Rate Limits
  slug: leadspace-rate-limits
scopes:
- name: Leadspace Scopes
  scope_count: 4
  slug: leadspace-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 68.7
    developer_ergonomics: 58.9
    discoverability: 74.1
    operational_transparency: 73.7
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/leadspace/refs/heads/main/screenshots/leadspace-2026-07-25T224715.png
security:
- kind: authentication
  name: Leadspace Authentication
  slug: leadspace-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Leadspace Domain Security
  slug: leadspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leadspace Vulnerability Disclosure
  slug: leadspace-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Leadspace Trust Center
  slug: leadspace-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: leadspace
tags:
- MCP
- AI Agents
- B2B Data
- Customer Data Platform
- Data Enrichment
- Intent Data
- Sales Intelligence
- Account Based Marketing
- Identity Resolution
- Firmographics
- Lead Scoring
- Company
website: https://www.leadspace.com/
---
