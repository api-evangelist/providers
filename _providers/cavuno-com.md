---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 229
  human_in_the_loop: 16
  name: Cavuno Com Agentic Access
  operation_count: 392
  slug: cavuno-com-agentic-access
  summary_line: 392 operations · 229 acting · 16 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Report a problem an AI agent hit with the API, CLI, MCP server or SDK (Agent Feedback Protocol v0.1).
  name: Cavuno Agent feedback API
  slug: cavuno-com-agent-feedback-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Typed Board homepage analytics: overview metrics and traffic tables.'
  name: Cavuno Analytics API
  slug: cavuno-com-analytics-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Read your account audit-log entries.
  name: Cavuno Audit logs API
  slug: cavuno-com-audit-logs-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Named Backfill rules, company sources, and aggregate progress for collecting jobs into a Board.
  name: Cavuno Backfill API
  slug: cavuno-com-backfill-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Your account's platform subscription, entitlements, checkout, upgrade, and Stripe Connect status.
  name: Cavuno Billing API
  slug: cavuno-com-billing-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete blog authors.
  name: Cavuno Blog authors API
  slug: cavuno-com-blog-authors-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, publish, and delete blog posts, and run batched post operations.
  name: Cavuno Blog posts API
  slug: cavuno-com-blog-posts-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete blog tags.
  name: Cavuno Blog tags API
  slug: cavuno-com-blog-tags-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Candidates registered on your board: list, view, delete.'
  name: Cavuno Candidates API
  slug: cavuno-com-candidates-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete job categories, and manage their aliases.
  name: Cavuno Categories API
  slug: cavuno-com-categories-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete companies attached to jobs.
  name: Cavuno Companies API
  slug: cavuno-com-companies-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Coupons and promotion codes on your connected Stripe account.
  name: Cavuno Coupons API
  slug: cavuno-com-coupons-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: XML feeds of your published jobs for job aggregators (Indeed, Jooble, Careerjet, Jora, Jobrapido, or a custom format), and the Cavuno distribution opt-in.
  name: Cavuno Distribution API
  slug: cavuno-com-distribution-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Add, list, remove, and verify custom domains and email sender domains, and manage the development origins where sign-in may complete while you test a self-hosted frontend.
  name: Cavuno Domains API
  slug: cavuno-com-domains-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Customize the subject, preview text, and body of the emails your board sends.
  name: Cavuno Email templates API
  slug: cavuno-com-email-templates-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Employer job-posting subscriptions on your board.
  name: Cavuno Employer subscriptions API
  slug: cavuno-com-employer-subscriptions-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Employers on your board: list, view, company claims, and memberships.'
  name: Cavuno Employers API
  slug: cavuno-com-employers-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Bulk job imports: upload, map fields, confirm, and track progress.'
  name: Cavuno Imports API
  slug: cavuno-com-imports-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Read and answer the support conversations your board receives, and manage inbox settings.
  name: Cavuno Inbox API
  slug: cavuno-com-inbox-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Search-indexing and analytics-reporting integrations.
  name: Cavuno Integrations API
  slug: cavuno-com-integrations-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, renew, and accept account invitations.
  name: Cavuno Invitations API
  slug: cavuno-com-invitations-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Recurring XML job feeds pulled from a URL on a schedule: connect, map fields, re-detect, and track runs.'
  name: Cavuno Job feeds API
  slug: cavuno-com-job-feeds-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and publish jobs.
  name: Cavuno Jobs API
  slug: cavuno-com-jobs-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Read marketing-email consent decisions off the board user records, and withdraw on request.
  name: Cavuno Marketing permissions API
  slug: cavuno-com-marketing-permissions-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete job markets, and manage their aliases.
  name: Cavuno Markets API
  slug: cavuno-com-markets-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Upload and manage logos and other binary assets.
  name: Cavuno Media API
  slug: cavuno-com-media-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: List, update, suspend, and remove team members, and read roles and permissions.
  name: Cavuno Members API
  slug: cavuno-com-members-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Track long-running asynchronous operations.
  name: Cavuno Operations API
  slug: cavuno-com-operations-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Current operator identity: Board binding, actor type, live role, and effective permissions/scopes.'
  name: Cavuno Operator API
  slug: cavuno-com-operator-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Intro copy on category and location pages: retrieve, set, and delete.'
  name: Cavuno Page content API
  slug: cavuno-com-page-content-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Candidate-access paywall configuration, offers, and subscription state.
  name: Cavuno Paywall API
  slug: cavuno-com-paywall-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Job-posting plans sold on your board: create, publish, price, and features.'
  name: Cavuno Plans API
  slug: cavuno-com-plans-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete board redirect rules.
  name: Cavuno Redirects API
  slug: cavuno-com-redirects-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Reference values accepted by the remote-permit and remote-timezone job fields.
  name: Cavuno Remote taxonomies API
  slug: cavuno-com-remote-taxonomies-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Contact-led employer pricing cards: create, reorder, publish, hide, and archive.'
  name: Cavuno Sales-led plans API
  slug: cavuno-com-sales-led-plans-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Read and update your board settings.
  name: Cavuno Settings API
  slug: cavuno-com-settings-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Create, list, update, and delete job skills, and manage their aliases.
  name: Cavuno Skills API
  slug: cavuno-com-skills-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Job-alert subscribers: list, export, un/resubscribe, and import.'
  name: Cavuno Subscribers API
  slug: cavuno-com-subscribers-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: 'Unified billing ledger: job-posting orders and employer-subscription transactions.'
  name: Cavuno Transactions API
  slug: cavuno-com-transactions-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Your account's actionable product capacity (used, limit, remaining).
  name: Cavuno Usage API
  slug: cavuno-com-usage-api
- baseURL: https://api.cavuno.com/v1
  baseurl_source: declared
  description: Configure Board-owned outbound webhook endpoints, inspect delivery history, and replay completed deliveries.
  name: Cavuno Webhooks API
  slug: cavuno-com-webhooks-api
artifact_total: 60
asyncapis:
- description: ''
  name: Cavuno Com Webhooks
  slug: cavuno-com-webhooks
common:
- group: start
  title: ''
  type: SignUp
  url: https://cavuno.com/auth/sign-up
- group: agent
  href: https://artifacts.apis.io/cavuno-com/agentic-access/cavuno-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cavuno-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cavuno-com/plans/cavuno-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cavuno-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/rules/cavuno-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cavuno-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/json-ld/cavuno-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cavuno-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cavuno-com/vocabulary/cavuno-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cavuno-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cavuno-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/asyncapi/cavuno-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cavuno-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/data-model/cavuno-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cavuno-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cavuno-com/changelog/cavuno-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cavuno-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/conventions/cavuno-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cavuno-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cavuno.com/security
- group: auth
  href: https://artifacts.apis.io/cavuno-com/authentication/cavuno-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cavuno-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/lifecycle/cavuno-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cavuno-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/errors/cavuno-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cavuno-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cavuno-com/conformance/cavuno-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cavuno-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cavuno-com/llms/cavuno-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cavuno-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cavuno-com/well-known/cavuno-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cavuno-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cavuno-com/hosts/cavuno-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cavuno-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cavuno-com/vendors/cavuno-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cavuno-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cavuno.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://cavuno.com/security
- group: build
  title: ''
  type: SDKs
  url: https://cavuno.com/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cavuno.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wollemiahq
- group: operate
  title: ''
  type: ChangeLog
  url: https://cavuno.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://cavuno.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://cavuno.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/cavuno-com/security/cavuno-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cavuno-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cavuno-com/security/cavuno-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cavuno-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cavuno-com/security/cavuno-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cavuno-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cavuno.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cavuno.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cavuno.com/docs#getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://cavuno.com/pricing
created: '2026-11-04'
description: Create an AI‑powered job board for your association, publication, community, or business. Cavuno lets you customize the board, automatically add relevant jobs, and grow your platform with ease. It offers a flexible, modern solution for managing job listings and engaging audiences.
image: https://cavuno.com/api/marketing/og/dashboard?page=home&v=3
json_schemas:
- name: CreateJobBody
  property_count: 34
  slug: cavuno-com-create-job-body
- name: Job
  property_count: 45
  slug: cavuno-com-job
- name: JobSummary
  property_count: 28
  slug: cavuno-com-job-summary
- name: PatchSettingsBody
  property_count: 66
  slug: cavuno-com-patch-settings-body
- name: SearchConsoleComparisonResponse
  property_count: 9
  slug: cavuno-com-search-console-comparison-response
- name: UpdateJobBody
  property_count: 31
  slug: cavuno-com-update-job-body
jsonld:
- class_count: 120
  name: Cavuno Com Context
  property_count: 283
  slug: cavuno-com-context
layout: provider
modified: '2026-11-04'
name: Cavuno
nav: Providers
network: true
overview: 'Cavuno publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent feedback API, Analytics API, Audit logs API, and 38 more. Tagged areas include Job Board Software, Artificial Intelligence, Community Platforms, and Monetization.


  The Cavuno catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cavuno''s developer surface includes signup flow, changelog, authentication, engineering blog, API reference, documentation, getting-started guide, and 28 more developer resources.'
plans:
- name: Cavuno Com Plans Pricing
  plan_count: 6
  slug: cavuno-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Cavuno API Rules
  rule_count: 60
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 14
  slug: cavuno-com-rules
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 72.1
    developer_ergonomics: 36.3
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
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
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cavuno Com Authentication
  slug: cavuno-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cavuno Com Domain Security
  slug: cavuno-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cavuno Com Vulnerability Disclosure
  slug: cavuno-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cavuno Com Trust Center
  slug: cavuno-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 4
skills:
- name: cavuno-com-create-and-test-webhook-endpoint
  slug: cavuno-com-create-and-test-webhook-endpoint
- name: cavuno-com-create-company
  slug: cavuno-com-create-company
- name: cavuno-com-manage-employer-membership-invites
  slug: cavuno-com-manage-employer-membership-invites
- name: cavuno-com-refund-transaction
  slug: cavuno-com-refund-transaction
slug: cavuno-com
tags:
- Job Board Software
- Artificial Intelligence
- Community Platforms
- Monetization
website: https://cavuno.com/
---
