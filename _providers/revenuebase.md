---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Revenuebase Agentic Access
  operation_count: 10
  slug: revenuebase-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.revenuebase.ai
  baseurl_source: declared
  description: The Account API from RevenueBase — 2 operation(s) for account.
  name: RevenueBase Account API
  slug: revenuebase-account-api
- baseURL: https://api.revenuebase.ai
  baseurl_source: declared
  description: The Email API from RevenueBase — 2 operation(s) for email.
  name: RevenueBase Email API
  slug: revenuebase-email-api
- baseURL: https://api.revenuebase.ai
  baseurl_source: declared
  description: The Jobs API from RevenueBase — 4 operation(s) for jobs.
  name: RevenueBase Jobs API
  slug: revenuebase-jobs-api
- baseURL: https://api.revenuebase.ai
  baseurl_source: declared
  description: The Organization API from RevenueBase — 2 operation(s) for organization.
  name: RevenueBase Organization API
  slug: revenuebase-organization-api
- baseURL: https://api.revenuebase.ai
  baseurl_source: declared
  description: The health API from RevenueBase — 2 operation(s) for health.
  name: RevenueBase Health API
  slug: revenuebase-health-api
- baseURL: https://api.revenuebase.ai
  baseurl_source: declared
  description: The Contact API from RevenueBase — 1 operation(s) for contact.
  name: RevenueBase Contact API
  slug: revenuebase-contact-api
artifact_total: 22
collections:
- collection_type: open
  name: Revenuebase API v2 Account API
  slug: open-revenuebase-account-api
- collection_type: open
  name: Revenuebase API v2 Account Email API
  slug: open-revenuebase-email-api
- collection_type: open
  name: Revenuebase API v2 Account Jobs API
  slug: open-revenuebase-jobs-api
- collection_type: open
  name: Revenuebase API v2 Account Organization API
  slug: open-revenuebase-organization-api
common:
- group: other
  href: https://artifacts.apis.io/revenuebase/capabilities/revenuebase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/revenuebase-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/revenuebase/agentic-access/revenuebase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/revenuebase-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://revenuebase.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.revenuebase.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revenuebase.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.revenuebase.ai/api-reference/v2/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.revenuebase.ai/docs/getting-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.revenuebase.ai/api-reference/v2/make-first-call
- group: auth
  href: https://artifacts.apis.io/revenuebase/authentication/revenuebase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revenuebase-authentication.yml
- group: auth
  href: https://artifacts.apis.io/revenuebase/security/revenuebase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revenuebase-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/revenuebase/openapi/_original/revenuebase-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/revenuebase-openapi.json
- group: other
  href: https://artifacts.apis.io/revenuebase/overlays/revenuebase-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/revenuebase-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/revenuebase/mcp/revenuebase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/revenuebase-mcp.yml
- group: design
  href: https://artifacts.apis.io/revenuebase/errors/revenuebase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/revenuebase-problem-types.yml
- group: design
  href: https://artifacts.apis.io/revenuebase/conventions/revenuebase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/revenuebase-conventions.yml
- group: design
  href: https://artifacts.apis.io/revenuebase/conformance/revenuebase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/revenuebase-conformance.yml
- group: design
  href: https://artifacts.apis.io/revenuebase/lifecycle/revenuebase-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/revenuebase-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/revenuebase/lifecycle/revenuebase-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/revenuebase-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revenuebase.ai/
- group: operate
  href: https://artifacts.apis.io/revenuebase/changelog/revenuebase-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/revenuebase-changelog.yml
- group: design
  href: https://artifacts.apis.io/revenuebase/data-model/revenuebase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/revenuebase-data-model.yml
- group: build
  href: https://artifacts.apis.io/revenuebase/packages/revenuebase-packages.yml
  title: ''
  type: Packages
  url: packages/revenuebase-packages.yml
- group: build
  href: https://artifacts.apis.io/revenuebase/packages/revenuebase-packages.yml
  title: ''
  type: SDKs
  url: packages/revenuebase-packages.yml
- group: agent
  href: https://artifacts.apis.io/revenuebase/well-known/revenuebase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/revenuebase-well-known.yml
- group: agent
  href: https://artifacts.apis.io/revenuebase/llms/revenuebase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/revenuebase-llms.txt
- group: agent
  href: https://artifacts.apis.io/revenuebase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/revenuebase/rate-limits/revenuebase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/revenuebase-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://revenuebase.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://revenuebase.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.revenuebase.ai/
- group: start
  title: ''
  type: Login
  url: https://app.revenuebase.ai/
- group: operate
  title: ''
  type: Support
  url: https://revenuebase.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revenuebase
- group: commercial
  title: ''
  type: TermsOfService
  url: https://revenuebase.ai/stc-01-14-2024
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revenuebase.ai/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenue-base/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/revenuebase
- group: other
  href: https://artifacts.apis.io/revenuebase/a2a/revenuebase-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/revenuebase-a2a.yml
- group: build
  href: https://artifacts.apis.io/revenuebase/mcp/revenuebase-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/revenuebase-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/revenuebase/skills/revenuebase-provider-skill.md
  title: ''
  type: AgentSkill
  url: skills/revenuebase-provider-skill.md
- group: commercial
  href: https://artifacts.apis.io/revenuebase/plans/revenuebase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/revenuebase-plans-pricing.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.revenuebase.ai/docs/release-notes
- group: operate
  title: ''
  type: Contact
  url: mailto:sales@revenuebase.ai
created: '2026-07-17'
description: RevenueBase is a B2B data infrastructure platform — "the trust layer for B2B data" — providing 400M+ continuously verified contacts (399M as of the August 2026 release notes) and 65M+ companies delivered via Snowflake, S3, Gigasheet, or a REST API. Core capabilities include real-time and batch email verification, deterministic and semantic company matching/resolution, organization discovery, and record enrichment, with data filterable by headcount, revenue, funding stage, industry, job title, seniority, geography, and tech stack. The v2 REST API authenticates with an API key in the x-key header and meters usage in credits. Originally surfaced as a Bessemer Venture Partners portfolio company and enriched into the API Evangelist network.
finops:
- has_sources: true
  method: derived
  name: Revenuebase Finops
  primary_unit: credit
  service_category: ''
  slug: revenuebase-finops
  template: false
image: https://cdn.prod.website-files.com/69aeeb63d4c5075af2fb954d/69dcb129729f9ab3c0816e26_RevenueBase-Favicon-32x32px.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.revenuebase.ai over HTTP; 3 tools listed.
  name: RevenueBase
  slug: revenuebase
modified: '2026-08-13'
name: RevenueBase
nav: Providers
network: true
overview: 'RevenueBase publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Email API, Jobs API, and 3 more. Tagged areas include Company, B2B Data, Data Enrichment, Email Verification, and Contact Data.


  The RevenueBase catalog on APIs.io includes 1 Spectral governance ruleset.


  RevenueBase''s developer surface includes documentation, API reference, getting-started guide, quickstart, authentication, changelog, engineering blog, and 36 more developer resources.'
plans:
- name: Revenuebase Plans Pricing
  plan_count: 10
  slug: revenuebase-plans-pricing
- name: Revenuebase Price Estimates
  plan_count: 0
  slug: revenuebase-price-estimates
random_paper: 21
rate_limits:
- limit_count: 2
  name: Revenuebase Rate Limits
  slug: revenuebase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: RevenueBase API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: revenuebase-rules
score:
  band: strong
  composite: 60.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 46.2
    developer_ergonomics: 71.4
    discoverability: 73.2
    operational_transparency: 55.3
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/revenuebase/revenuebase-2026-08-17T081544.png
security:
- kind: authentication
  name: Revenuebase Authentication
  slug: revenuebase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Revenuebase Domain Security
  slug: revenuebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Revenuebase
  slug: revenuebase-provider-skill
- name: revenuebase-resolve-organizations
  slug: revenuebase-resolve-organizations
- name: revenuebase-verify-emails
  slug: revenuebase-verify-emails
slug: revenuebase
tags:
- Company
- B2B Data
- Data Enrichment
- Email Verification
- Contact Data
- Company Data
- Lead Intelligence
- Sales Intelligence
- A2A
website: https://revenuebase.ai/
---
