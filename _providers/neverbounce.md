---
access_model:
  confidence: high
  label: Self-serve signup with published per-credit pricing
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - authentication
  - plans/neverbounce-plans-pricing.yml
  - https://www.neverbounce.com/pricing
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Neverbounce Agentic Access
  operation_count: 10
  slug: neverbounce-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: RESTful JSON API for email verification. Provides single email verification (`/single/check`), bulk job verification (`/jobs/create`, `/jobs/parse`, `/jobs/start`, `/jobs/status`, `/jobs/results`, `/j
  name: NeverBounce API v4
  slug: v4-api
- baseURL: https://api.neverbounce.com/v4
  baseurl_source: declared
  description: Account credit balances and job counts by state.
  name: NeverBounce Account API
  slug: neverbounce-account-api
- baseURL: https://api.neverbounce.com/v4
  baseurl_source: declared
  description: Bulk list verification jobs — create, parse, start, status, results, search, delete, download.
  name: NeverBounce Jobs API
  slug: neverbounce-jobs-api
- baseURL: https://api.neverbounce.com/v4
  baseurl_source: declared
  description: Real-time verification of a single email address.
  name: NeverBounce Single API
  slug: neverbounce-single-api
- baseURL: https://api.neverbounce.com/v4
  baseurl_source: declared
  description: 'Proof of Engagement. Server-side confirmation that a verification produced by the browser JavaScript widget genuinely came from NeverBounce, using the transaction_id and confirmation_token the widget '
  name: NeverBounce POE API
  slug: neverbounce-poe-api
artifact_total: 22
asyncapis:
- description: ''
  name: Neverbounce Webhooks
  slug: neverbounce-webhooks
collections:
- collection_type: open
  name: NeverBounce API v4 Account API
  slug: open-neverbounce-account-api
- collection_type: open
  name: NeverBounce API v4 Account Jobs API
  slug: open-neverbounce-jobs-api
- collection_type: open
  name: NeverBounce API v4 Account Single API
  slug: open-neverbounce-single-api
- collection_type: open
  name: NeverBounce API v4
  slug: open-neverbounce
common:
- group: agent
  href: https://artifacts.apis.io/neverbounce/agentic-access/neverbounce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/neverbounce-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/neverbounce/security/neverbounce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neverbounce-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/neverbounce/authentication/neverbounce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/neverbounce-authentication.yml
- group: build
  href: https://artifacts.apis.io/neverbounce/packages/neverbounce-packages.yml
  title: ''
  type: Packages
  url: packages/neverbounce-packages.yml
- group: build
  href: https://artifacts.apis.io/neverbounce/packages/neverbounce-packages.yml
  title: ''
  type: SDKs
  url: packages/neverbounce-packages.yml
- group: build
  href: https://artifacts.apis.io/neverbounce/cli/neverbounce-cli.yml
  title: ''
  type: CLI
  url: cli/neverbounce-cli.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/components/neverbounce-components.yml
  title: ''
  type: Components
  url: components/neverbounce-components.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/conventions/neverbounce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/neverbounce-conventions.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/errors/neverbounce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/neverbounce-problem-types.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/data-model/neverbounce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/neverbounce-data-model.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/conformance/neverbounce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/neverbounce-conformance.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/lifecycle/neverbounce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/neverbounce-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/neverbounce/lifecycle/neverbounce-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/neverbounce-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.neverbounce.com
- group: operate
  href: https://artifacts.apis.io/neverbounce/changelog/neverbounce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/neverbounce-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/neverbounce/plans/neverbounce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neverbounce-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/neverbounce/rate-limits/neverbounce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/neverbounce-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/neverbounce/asyncapi/neverbounce-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/neverbounce-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/neverbounce/mcp/neverbounce-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/neverbounce-mcp.yml
- group: build
  href: https://artifacts.apis.io/neverbounce/mcp/neverbounce-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/neverbounce-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/neverbounce/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/neverbounce/llms/neverbounce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neverbounce-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.neverbounce.com/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neverbounce
- group: company
  title: ''
  type: Website
  url: https://www.neverbounce.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.neverbounce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.neverbounce.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.neverbounce.com/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.neverbounce.com/docs/api-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NeverBounce
- group: commercial
  title: ''
  type: Pricing
  url: https://www.neverbounce.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.neverbounce.com/register
- group: operate
  title: ''
  type: Support
  url: https://www.neverbounce.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.neverbounce.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neverbounce.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoominfo.com/legal/privacy-policy
created: '2026-05-11'
description: NeverBounce is an email verification and list cleaning service — a ZoomInfo company — that validates individual email addresses in real time and cleans bulk lists by checking syntax, mailbox existence, role addresses, disposable addresses, catch-all domains, and deliverability to reduce bounce rates for marketing, sales, and transactional senders. The NeverBounce v4 REST API at https://api.neverbounce.com/v4.2/ provides ten published operations covering single email checks (/single/check), bulk list jobs (create, parse, start, status, results, search, delete, download), account credit info, and the Proof-of-Engagement confirmation used by the browser widget, with JSON responses over HTTPS. Authentication uses a per-integration API key (format `secret_xxxx...`) passed as the `key` parameter in the query string or request body; `public_` keys drive the JavaScript widget and cannot call the standard API. Application errors — including authentication failure and throttling — are
  returned with an HTTP 200 and a `status` field rather than a 4xx, which is the defining runtime quirk of this API.
finops:
- has_sources: true
  method: derived
  name: Neverbounce Finops
  primary_unit: 1,000 credits
  service_category: ''
  slug: neverbounce-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neverbounce.png
layout: provider
mcp_servers:
- description: Remote MCP server at developers.neverbounce.com.
  name: NeverBounce Developer Docs MCP
  slug: neverbounce-developer-docs-mcp
modified: '2026-08-13'
name: NeverBounce
nav: Providers
network: true
overview: 'NeverBounce publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Jobs API, Single API, and 2 more. Tagged areas include Email Verification, Email Hygiene, Deliverability, Marketing, and List Cleaning.


  The NeverBounce catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  NeverBounce''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, pricing, and 29 more developer resources.'
plans:
- name: Neverbounce Plans Pricing
  plan_count: 3
  slug: neverbounce-plans-pricing
- name: Neverbounce Price Estimates
  plan_count: 0
  slug: neverbounce-price-estimates
random_paper: 4
rate_limits:
- limit_count: 6
  name: Neverbounce Rate Limits
  slug: neverbounce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: NeverBounce API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: neverbounce-rules
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 52.8
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
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
screenshot: https://apis.io/screenshots/neverbounce/neverbounce-2026-06-20T190221.png
security:
- kind: authentication
  name: Neverbounce Authentication
  slug: neverbounce-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Neverbounce Domain Security
  slug: neverbounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: neverbounce-check-credits-and-usage
  slug: neverbounce-check-credits-and-usage
- name: neverbounce-verify-a-list
  slug: neverbounce-verify-a-list
- name: neverbounce-verify-single-email
  slug: neverbounce-verify-single-email
slug: neverbounce
tags:
- Email Verification
- Email Hygiene
- Deliverability
- Marketing
- List Cleaning
- Data Quality
- ZoomInfo
- Email
website: https://www.neverbounce.com
---
