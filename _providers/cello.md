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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.9
  scored_at: '2026-11-06'
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
artifact_total: 23
collections:
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
- group: company
  title: ''
  type: BlogRSS
  url: https://cello.so/feed/
- group: company
  title: ''
  type: Website
  url: https://www.cello.so/
- group: other
  href: https://artifacts.apis.io/cello/overlays/cello-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cello-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/cello/security/cello-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cello-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cello/agentic-access/cello-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cello-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cello/authentication/cello-authentication.yml
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
  href: https://artifacts.apis.io/cello/mcp/cello-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cello-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cello/llms/cello-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cello-llms.txt
- group: build
  href: https://artifacts.apis.io/cello/packages/cello-packages.yml
  title: ''
  type: Packages
  url: packages/cello-packages.yml
- group: build
  href: https://artifacts.apis.io/cello/packages/cello-packages.yml
  title: ''
  type: SDKs
  url: packages/cello-packages.yml
- group: design
  href: https://artifacts.apis.io/cello/components/cello-components.yml
  title: ''
  type: Components
  url: components/cello-components.yml
- group: start
  href: https://artifacts.apis.io/cello/sandbox/cello-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cello-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/cello/changelog/cello-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cello-changelog.yml
- group: design
  href: https://artifacts.apis.io/cello/lifecycle/cello-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cello-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cello/conventions/cello-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cello-conventions.yml
- group: design
  href: https://artifacts.apis.io/cello/errors/cello-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cello-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cello/data-model/cello-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cello-data-model.yml
- group: design
  href: https://artifacts.apis.io/cello/conformance/cello-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cello-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cello.so/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/cello/skills/cello-track-referral-conversion.md
  title: ''
  type: AgentSkill
  url: skills/cello-track-referral-conversion.md
- group: agent
  href: https://artifacts.apis.io/cello/skills/cello-fetch-and-reward-referee.md
  title: ''
  type: AgentSkill
  url: skills/cello-fetch-and-reward-referee.md
- group: agent
  href: https://artifacts.apis.io/cello/skills/cello-referral-integration.md
  title: ''
  type: AgentSkill
  url: skills/cello-referral-integration.md
- group: other
  href: https://artifacts.apis.io/cello/a2a/cello-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cello-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cello/well-known/cello-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cello-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cello/scopes/cello-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cello-scopes.yml
- group: build
  href: https://artifacts.apis.io/cello/mcp/cello-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cello-tool-crosswalk.yml
- group: commercial
  href: https://artifacts.apis.io/cello/plans/cello-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cello-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cello/rate-limits/cello-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cello-rate-limits.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@cello.so
created: '2026-07-17'
description: Cello is an all-in-one, AI-powered referral platform for SaaS companies. It lets product teams embed in-product user referrals and run partner/affiliate programs with a few lines of code, then automates attribution, campaigns, notifications, fraud detection, and cross-border payouts. Cello ships an embeddable Referral Component and Attribution JS SDK for web plus native iOS, Android, Flutter, and React Native SDKs, a REST API for tokens, referral-code validation, events, and new-user rewards, a Growth Portal for analytics, and an official hosted MCP server exposing developer and growth-manager tools. Customers include Typeform, Miro, Descript, Pleo, and SmallPDF. Backed by HV Capital.
finops:
- has_sources: true
  method: derived
  name: Cello Finops
  primary_unit: subscription
  service_category: ''
  slug: cello-finops
  template: false
image: https://cello.so/wp-content/uploads/2022/12/Group-174900-1.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cello.so over HTTP requiring OAuth; 8 tools listed.
  name: Cello MCP Server
  slug: cello
modified: '2026-10-06'
name: Cello
nav: Providers
network: true
overview: 'Cello publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, New Users API, Referral Codes API, and 2 more. Tagged areas include Company, Referral Marketing, Affiliate Marketing, Growth, and Software-as-a-Service.


  The Cello catalog on APIs.io includes 1 Spectral governance ruleset.


  Cello''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Cello Plans Pricing
  plan_count: 8
  slug: cello-plans-pricing
- name: Cello Price Estimates
  plan_count: 0
  slug: cello-price-estimates
random_paper: 23
rate_limits:
- limit_count: 0
  name: Cello Rate Limits
  slug: cello-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Cello API Rules
  rule_count: 58
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 2
  slug: cello-rules
scopes:
- name: Cello Scopes
  scope_count: 2
  slug: cello-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 51.1
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 62.2
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
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cello/cello-2026-07-25T204908.png
security:
- kind: authentication
  name: Cello Authentication
  slug: cello-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Cello Domain Security
  slug: cello-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Fetch a share link and check referee reward eligibility
  slug: cello-fetch-and-reward-referee
- name: Cello
  slug: cello-referral-integration
- name: Track a referral conversion with Cello
  slug: cello-track-referral-conversion
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
- A2A
website: https://www.cello.so/
---
