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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Evermuse Agentic Access
  operation_count: 3
  slug: evermuse-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.evermuse.com
  baseurl_source: declared
  description: Send data to Evermuse
  name: Evermuse Ingestion API
  slug: evermuse-ingestion-api
artifact_total: 14
collections:
- collection_type: open
  name: Evermuse ingestion API
  slug: open-evermuse-ingestion-api
common:
- group: commercial
  href: https://artifacts.apis.io/evermuse/plans/evermuse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/evermuse-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/evermuse/overlays/evermuse-ingest-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/evermuse-ingest-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://evermuse.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evermuse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evermuse.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evermuse.com/api-reference/index
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evermuse.com/
- group: company
  title: ''
  type: Blog
  url: https://www.evermuse.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.evermuse.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evermuse.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.evermuse.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evermuse.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evermuse.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://evermuse.checkly-status-page.com/
- group: operate
  href: https://artifacts.apis.io/evermuse/changelog/evermuse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/evermuse-changelog.yml
- group: design
  href: https://artifacts.apis.io/evermuse/lifecycle/evermuse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/evermuse-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/evermuse/authentication/evermuse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/evermuse-authentication.yml
- group: auth
  href: https://artifacts.apis.io/evermuse/scopes/evermuse-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/evermuse-scopes.yml
- group: design
  href: https://artifacts.apis.io/evermuse/conventions/evermuse-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/evermuse-conventions.yml
- group: design
  href: https://artifacts.apis.io/evermuse/conventions/evermuse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/evermuse-conventions.yml
- group: agent
  href: https://artifacts.apis.io/evermuse/mcp/evermuse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/evermuse-mcp.yml
- group: agent
  href: https://artifacts.apis.io/evermuse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/evermuse/well-known/evermuse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evermuse-well-known.yml
- group: design
  href: https://artifacts.apis.io/evermuse/conformance/evermuse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evermuse-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.evermuse.com/security
- group: auth
  href: https://artifacts.apis.io/evermuse/security/evermuse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/evermuse-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.evermuse.com/security
- group: auth
  href: https://artifacts.apis.io/evermuse/security/evermuse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/evermuse-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/evermuse/security/evermuse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evermuse-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/evermuse/agentic-access/evermuse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evermuse-agentic-access.yml
created: '2026-07-17'
description: Evermuse is an AI advisor for product teams that turns every customer signal — sales and success calls, support conversations, meeting notes, emails, surveys, and reviews — into code-ready, well-researched feature specifications. Its Ingestion API accepts records wrapped in a canonical Integration Envelope (JSON or NDJSON), validates, normalizes, deduplicates, and stores them in the Evermuse Data Lake for AI analysis into user needs, feature requests, and prioritized opportunities. Evermuse also publishes a hosted, OAuth 2.1-protected Model Context Protocol (MCP) server that plugs Claude, ChatGPT, Cursor, and other agents directly into a workspace's real customer evidence and live roadmap.
finops:
- has_sources: true
  method: derived
  name: Evermuse Finops
  primary_unit: month, billed annually
  service_category: ''
  slug: evermuse-finops
  template: false
image: https://www.evermuse.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.evermuse.com.
  name: Evermuse MCP Server
  slug: evermuse-mcp-yml
modified: '2026-07-19'
name: Evermuse
nav: Providers
network: true
overview: 'Evermuse publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Ingestion API. Tagged areas include Company, Product Management, Customer Feedback, Voice of Customer, and Artificial Intelligence.


  Evermuse''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Evermuse Plans Pricing
  plan_count: 4
  slug: evermuse-plans-pricing
- name: Evermuse Price Estimates
  plan_count: 0
  slug: evermuse-price-estimates
random_paper: 12
scopes:
- name: Evermuse Scopes
  scope_count: 3
  slug: evermuse-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 51.6
    developer_ergonomics: 58.9
    discoverability: 65.0
    operational_transparency: 42.1
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/evermuse/evermuse-2026-07-25T213734.png
security:
- kind: authentication
  name: Evermuse Authentication
  slug: evermuse-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Evermuse Domain Security
  slug: evermuse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Evermuse Vulnerability Disclosure
  slug: evermuse-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Evermuse Trust Center
  slug: evermuse-trust-center
  summary_line: SOC 2, GDPR
skill_count: 2
skills:
- name: Ingest records and track the batch
  slug: evermuse-ingest-and-track
- name: Audit recent ingestion batches
  slug: evermuse-list-batches
slug: evermuse
tags:
- Company
- Product Management
- Customer Feedback
- Voice of Customer
- Artificial Intelligence
- Data Ingestion
- Product Analytics
- MCP
- Developer Tools
website: https://evermuse.com
---
