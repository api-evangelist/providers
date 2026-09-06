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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Read (and timeline-write) access to Crossbeam Ecosystem Intelligence — partners, populations, reports/overlaps, and real-time signals — via a versioned REST API secured with OAuth 2.0. Requires an Aut
  name: Crossbeam Partner API
  slug: crossbeam-partner-api
artifact_total: 11
asyncapis:
- description: ''
  name: Crossbeam Signals Webhooks
  slug: crossbeam-signals-webhooks
collections:
- collection_type: postman
  name: Crossbeam Partner API
  slug: postman-crossbeam-partner-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/crossbeam-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crossbeam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.crossbeam.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.crossbeam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.crossbeam.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.crossbeam.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.crossbeam.com/en/articles/4677142-rest-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.crossbeam.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.crossbeam.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.crossbeam.com/resources/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.crossbeam.com/resources/product-updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getcrossbeam
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crossbeam.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.crossbeam.com/register
- group: start
  title: ''
  type: Login
  url: https://app.crossbeam.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crossbeam.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crossbeam.com/legal/crossbeam-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crossbeam.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/crossbeam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crossbeam-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crossbeam-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crossbeam-signals-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crossbeam-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crossbeam-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/crossbeam-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.crossbeam.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/crossbeam-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crossbeam-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crossbeam-changelog.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crossbeam-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crossbeam-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/crossbeam-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crossbeam-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crossbeam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crossbeam-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crossbeam-problem-types.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossbeam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.crossbeam.com/legal/responsible-disclosure
- group: build
  title: ''
  type: Postman
  url: https://developers.crossbeam.com/
created: '2026-07-17'
description: 'Crossbeam is the leading Ecosystem-Led Growth (ELG) platform: a secure data-collaboration network that lets companies compare CRM data with their partners to uncover shared customers, overlapping prospects, and co-selling opportunities without exposing sensitive records. It turns partner-sourced overlaps, populations, and real-time signals into "Ecosystem Intelligence" that flows into GTM tools and AI agents. Crossbeam exposes this data through a REST Partner API (OAuth 2.0), real-time Signals webhooks, a remote MCP server, and in-app AI Chat, backed by SOC 2 Type II, GDPR, CCPA, and PCI DSS compliance.'
image: https://cdn.prod.website-files.com/66955639e4d4a6eebd7168b9/67659cb901d6d8f4eb2bd567_crossbeam_opengraph.avif
layout: provider
mcp_servers:
- description: ''
  name: Crossbeam MCP Server
  slug: crossbeam-mcp-server
modified: '2026-08-14'
name: Crossbeam
nav: Providers
network: true
overview: 'Crossbeam publishes 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Company, Ecosystem-Led Growth, Partnerships, Account Mapping, and Co-Selling.


  The Crossbeam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crossbeam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 33 more developer resources.'
plans:
- name: Crossbeam Plans Pricing
  plan_count: 4
  slug: crossbeam-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Crossbeam Rate Limits
  slug: crossbeam-rate-limits
scopes:
- name: Crossbeam Scopes
  scope_count: 6
  slug: crossbeam-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 59.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crossbeam/refs/heads/main/screenshots/crossbeam-2026-07-25T210753.png
security:
- kind: authentication
  name: Crossbeam Authentication
  slug: crossbeam-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Crossbeam Domain Security
  slug: crossbeam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crossbeam Vulnerability Disclosure
  slug: crossbeam-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Crossbeam Trust Center
  slug: crossbeam-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: crossbeam
tags:
- Company
- Ecosystem-Led Growth
- Partnerships
- Account Mapping
- Co-Selling
- Data Collaboration
- Sales Intelligence
- CRM
- Webhook
- MCP
website: http://www.crossbeam.com/
---
