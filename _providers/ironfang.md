---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 108
  human_in_the_loop: 3
  name: Ironfang Agentic Access
  operation_count: 230
  slug: ironfang-agentic-access
  summary_line: 230 operations · 108 acting · 3 human-in-the-loop
api_count: 7
apis:
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: Usage against quota.
  name: Ironfang Account API
  slug: ironfang-account-api
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: Up to 100 renders submitted, and refused, together.
  name: Ironfang Batches API
  slug: ironfang-batches-api
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: Where a finished job goes - a signed webhook, or your own S3 bucket.
  name: Ironfang Destinations API
  slug: ironfang-destinations-api
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: The Jobs API from Ironfang — 4 operation(s) for jobs.
  name: Ironfang Jobs API
  slug: ironfang-jobs-api
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: Turn a URL or HTML into an image, PDF or video.
  name: Ironfang Render API
  slug: ironfang-render-api
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: Shareable render URLs that need no API key.
  name: Ironfang Signed URLs API
  slug: ironfang-signed-urls-api
- baseURL: https://api.ironfang.com/render
  baseurl_source: declared
  description: Stored HTML with `{{variable}}` placeholders, rendered on demand.
  name: Ironfang Templates API
  slug: ironfang-templates-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Stored screenshots and other captured artifacts.
  name: Ironfang Audit Artifacts API
  slug: ironfang-audit-artifacts-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Audit runs, their pages and evidence.
  name: Ironfang Audit Audits API
  slug: ironfang-audit-audits-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: The account event stream.
  name: Ironfang Audit Events API
  slug: ironfang-audit-events-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Where exports are delivered.
  name: Ironfang Audit Export Destinations API
  slug: ironfang-audit-exportdestinations-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Evidence bundle exports.
  name: Ironfang Audit Exports API
  slug: ironfang-audit-exports-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Findings raised by audits.
  name: Ironfang Audit Findings API
  slug: ironfang-audit-findings-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Scheduled re-audits of a site.
  name: Ironfang Audit Monitors API
  slug: ironfang-audit-monitors-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: How the organisation is notified.
  name: Ironfang Audit Notification Preferences API
  slug: ironfang-audit-notificationpreferences-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Notifications raised for the organisation.
  name: Ironfang Audit Notifications API
  slug: ironfang-audit-notifications-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Per-page observations and comparisons.
  name: Ironfang Audit Page Observations API
  slug: ironfang-audit-pageobservations-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Pages within an audit.
  name: Ironfang Audit Pages API
  slug: ironfang-audit-pages-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Quoted, fixed-price extensions of hosted evidence retention.
  name: Ironfang Audit Retention API
  slug: ironfang-audit-retention-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Installable rule packs.
  name: Ironfang Audit Rule Packs API
  slug: ironfang-audit-rulepacks-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Rules and their revisions.
  name: Ironfang Audit Rules API
  slug: ironfang-audit-rules-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Sites under audit.
  name: Ironfang Audit Sites API
  slug: ironfang-audit-sites-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: This month's metered use, capacity and hosted evidence.
  name: Ironfang Audit Usage API
  slug: ironfang-audit-usage-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Public verification of evidence bundles.
  name: Ironfang Audit Verify API
  slug: ironfang-audit-verify-api
- baseURL: https://api.ironfang.com/audit
  baseurl_source: declared
  description: Webhook endpoints and deliveries.
  name: Ironfang Audit Webhooks API
  slug: ironfang-audit-webhooks-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Ironfang Finance usage as the organisation's billing account meters it, beside Finance's own content-free record. Payment, limits and invoices belong to the account at /billing/v1.
  name: Ironfang Finance E-Invoicing Billing API
  slug: ironfang-finance-billing-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Destinations subscribe to future terminal validation/generation operations in their organisation.
  name: Ironfang Finance E-Invoicing Deliveries API
  slug: ironfang-finance-deliveries-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Deterministic JSON-to-UBL generation, validated before success.
  name: Ironfang Finance E-Invoicing Generation API
  slug: ironfang-finance-generation-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Authenticated durable validation and generation jobs and ordered batches.
  name: Ironfang Finance E-Invoicing Jobs API
  slug: ironfang-finance-jobs-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Safe readable PDFs of retained successfully validated generation results.
  name: Ironfang Finance E-Invoicing Rendering API
  slug: ironfang-finance-rendering-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Signed validation observations and independent report integrity verification.
  name: Ironfang Finance E-Invoicing Reports API
  slug: ironfang-finance-reports-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Authenticated retained validation and generation results.
  name: Ironfang Finance E-Invoicing Results API
  slug: ironfang-finance-results-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: The immutable ruleset registry validation results are pinned to.
  name: Ironfang Finance E-Invoicing Rulesets API
  slug: ironfang-finance-rulesets-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: PHIVE validation of UBL Invoice and CreditNote XML with structured findings.
  name: Ironfang Finance E-Invoicing Validation API
  slug: ironfang-finance-validation-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Webhook and S3 deliveries of V1 and V2 events together.
  name: Ironfang Finance E-Invoicing V2 Deliveries API
  slug: ironfang-finance-v2-deliveries-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Durable validation jobs and batches, V1 and V2 together.
  name: Ironfang Finance E-Invoicing V2 Jobs API
  slug: ironfang-finance-v2-jobs-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Signed reports of retained results, and their verification.
  name: Ironfang Finance E-Invoicing V2 Reports API
  slug: ironfang-finance-v2-reports-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Retained results, V1 and V2 together.
  name: Ironfang Finance E-Invoicing V2 Results API
  slug: ironfang-finance-v2-results-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: The immutable releases a validation can name.
  name: Ironfang Finance E-Invoicing V2 Rulesets API
  slug: ironfang-finance-v2-rulesets-api
- baseURL: https://api.ironfang.com/finance
  baseurl_source: declared
  description: Validate one invoice, XML or PDF.
  name: Ironfang Finance E-Invoicing V2 Validation API
  slug: ironfang-finance-v2-validation-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: Outbound connectors that forward a run's callbacks to fixed local routes.
  name: Ironfang Rig Connectors API
  slug: ironfang-rig-connectors-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: The run timeline.
  name: Ironfang Rig Events API
  slug: ironfang-rig-events-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: Bundles, receipts and the keys they are signed with.
  name: Ironfang Rig Evidence API
  slug: ironfang-rig-evidence-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: Deterministic interference armed on a run's resources.
  name: Ironfang Rig Faults API
  slug: ironfang-rig-faults-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: Persistent containers for one application or product.
  name: Ironfang Rig Projects API
  slug: ironfang-rig-projects-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: The external identities a run receives.
  name: Ironfang Rig Resources API
  slug: ironfang-rig-resources-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: Disposable executions of a suite version.
  name: Ironfang Rig Runs API
  slug: ironfang-rig-runs-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: Persistent, versioned test definitions.
  name: Ironfang Rig Suites API
  slug: ironfang-rig-suites-api
- baseURL: https://api.ironfang.com/rig
  baseurl_source: declared
  description: What the organisation has used, and the deployment's fixed facts.
  name: Ironfang Rig Usage API
  slug: ironfang-rig-usage-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: What this deployment can do and the limits it applies.
  name: Ironfang Analytics Capabilities API
  slug: ironfang-analytics-capabilities-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: Totals of where visitors click, how far they scroll, how long each part of a page is on screen and where the pointer goes, across the recorded visits to one page. Computed from recordings, so they kee
  name: Ironfang Analytics Heatmaps API
  slug: ironfang-analytics-heatmaps-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: The public collection key a site's install snippet carries.
  name: Ironfang Analytics Keys API
  slug: ironfang-analytics-keys-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: The origins a site's recorder may send from and their DNS verification.
  name: Ironfang Analytics Origins API
  slug: ironfang-analytics-origins-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: 'Recordings of one tab within a session: search, what the visitor''s browser reported, the batches to play them back from, live viewing and deletion. Every recording keeps the visitor''s IP address and f'
  name: Ironfang Analytics Recordings API
  slug: ironfang-analytics-recordings-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: 'One browser''s visit to one site: every tab, from the first page until thirty minutes pass without the visitor doing anything, or twelve hours from its start. A session holds its pages, its events and '
  name: Ironfang Analytics Sessions API
  slug: ironfang-analytics-sessions-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: Instrumented websites and their capture configuration.
  name: Ironfang Analytics Sites API
  slug: ironfang-analytics-sites-api
- baseURL: https://api.ironfang.com/analytics
  baseurl_source: declared
  description: This month's recordings as the organisation's billing account counts them, and whether new recordings are being admitted.
  name: Ironfang Analytics Usage API
  slug: ironfang-analytics-usage-api
- baseURL: https://api.ironfang.com/security
  baseurl_source: declared
  description: What happened in the organisation's Security account.
  name: Ironfang Security Activity API
  slug: ironfang-security-activity-api
- baseURL: https://api.ironfang.com/security
  baseurl_source: declared
  description: Domains the organisation has added, their ownership verification and authorisation.
  name: Ironfang Security Domains API
  slug: ironfang-security-domains-api
- baseURL: https://api.ironfang.com/security
  baseurl_source: declared
  description: Normalised findings, their evidence, status and rechecks.
  name: Ironfang Security Findings API
  slug: ironfang-security-findings-api
- baseURL: https://api.ironfang.com/security
  baseurl_source: declared
  description: External Security Check runs and their results.
  name: Ironfang Security Scans API
  slug: ironfang-security-scans-api
- baseURL: https://api.ironfang.com/security
  baseurl_source: declared
  description: Whether Security is available, and the limits that apply.
  name: Ironfang Security Service API
  slug: ironfang-security-service-api
artifact_total: 90
asyncapis:
- description: ''
  name: Ironfang Webhooks
  slug: ironfang-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://ironfang.com/articles
- group: company
  title: ''
  type: BlogRSS
  url: https://ironfang.com/articles/feed.xml
- group: other
  href: https://artifacts.apis.io/ironfang/capabilities/ironfang-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ironfang-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ironfang/agentic-access/ironfang-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ironfang-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ironfang/rules/ironfang-rules.yml
  title: ''
  type: Spectral
  url: rules/ironfang-rules.yml
- group: design
  href: https://artifacts.apis.io/ironfang/json-ld/ironfang-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ironfang-context.jsonld
- group: design
  href: https://artifacts.apis.io/ironfang/vocabulary/ironfang-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ironfang-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/ironfang/lifecycle/ironfang-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ironfang-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/ironfang/hosts/ironfang-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ironfang-hosts.yml
- group: other
  href: https://artifacts.apis.io/ironfang/vendors/ironfang-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ironfang-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://ironfang.com/audit/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://ironfang.com/render/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://ironfang.com/changelog
- group: other
  href: https://artifacts.apis.io/ironfang/overlays/ironfang-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ironfang-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ironfang/mcp/ironfang-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ironfang-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.ironfang.com/mcp
- group: company
  title: ''
  type: Website
  url: https://www.ironfang.com/
- group: auth
  href: https://artifacts.apis.io/ironfang/security/ironfang-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ironfang-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ironfang/authentication/ironfang-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ironfang-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ironfang/scopes/ironfang-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ironfang-scopes.yml
- group: design
  href: https://artifacts.apis.io/ironfang/conventions/ironfang-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ironfang-conventions.yml
- group: design
  href: https://artifacts.apis.io/ironfang/conventions/ironfang-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ironfang-conventions.yml
- group: build
  href: https://artifacts.apis.io/ironfang/packages/ironfang-packages.yml
  title: ''
  type: Packages
  url: packages/ironfang-packages.yml
- group: build
  href: https://artifacts.apis.io/ironfang/packages/ironfang-packages.yml
  title: ''
  type: SDKs
  url: packages/ironfang-packages.yml
- group: build
  href: https://artifacts.apis.io/ironfang/cli/ironfang-cli.yml
  title: ''
  type: CLI
  url: cli/ironfang-cli.yml
- group: agent
  href: https://artifacts.apis.io/ironfang/well-known/ironfang-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ironfang-well-known.yml
- group: design
  href: https://artifacts.apis.io/ironfang/conformance/ironfang-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ironfang-conformance.yml
- group: design
  href: https://artifacts.apis.io/ironfang/lifecycle/ironfang-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ironfang-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ironfang.com
- group: start
  href: https://artifacts.apis.io/ironfang/sandbox/ironfang-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ironfang-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/ironfang/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/ironfang/plans/ironfang-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ironfang-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ironfang/rate-limits/ironfang-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ironfang-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ironfang.com/render
- group: start
  title: ''
  type: GettingStarted
  url: https://ironfang.com/render/guides
- group: operate
  title: ''
  type: Support
  url: https://ironfang.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ironfang-ltd
- group: commercial
  title: ''
  type: Pricing
  url: https://ironfang.com/render
- group: start
  title: ''
  type: SignUp
  url: https://id.ironfang.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ironfang.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ironfang.com/legal/privacy
created: '2026-09-02'
description: Ironfang Render is the rendering API from Ironfang Ltd, a UK software company that builds and operates self-service developer APIs. It turns a URL or a block of raw HTML into screenshots, PDFs, templated images, QR codes, captioned video clips and scrolling site previews over plain HTTPS and JSON, with no browser fleet for the customer to run. The v1 REST API is described by a published OpenAPI 3.1 contract covering 33 operations across synchronous rendering, reusable HTML templates, signed render URLs, durable asynchronous jobs, batches of up to 100, and webhook or S3-compatible delivery destinations. A remote MCP server at mcp.ironfang.com exposes the same core to AI assistants over OAuth 2.1 with a per-connection credit budget, and an llms.txt, a TypeScript and Python SDK, a CLI and an n8n node round out the surface. Plans are hard-capped rather than metered into overage, cache hits are free, and failed renders are refunded. Ironfang's own apis.json lists five more product
  APIs on the same account, portal and key format, each with its own published OpenAPI 3.1 contract under api.ironfang.com, for Audit (website evidence), Finance (e-invoice validation and generation, v1 and v2), Rig (disposable integration test environments), Analytics (session replay) and Security (external security checks).
finops:
- has_sources: true
  method: derived
  name: Ironfang Finops
  primary_unit: 1,000 output seconds
  service_category: ''
  slug: ironfang-finops
  template: false
image: https://ironfang.com/logo-wolf-white.svg
json_schemas:
- name: ClipRequest
  property_count: 8
  slug: ironfang-clip-request
- name: JobDelivery
  property_count: 3
  slug: ironfang-job-delivery
- name: PdfRequest
  property_count: 21
  slug: ironfang-pdf-request
- name: QrRequest
  property_count: 13
  slug: ironfang-qr-request
- name: RenderTemplateRequest
  property_count: 14
  slug: ironfang-render-template-request
- name: ScreenshotRequest
  property_count: 26
  slug: ironfang-screenshot-request
- name: SignRequest
  property_count: 8
  slug: ironfang-sign-request
- name: SignedUrl
  property_count: 2
  slug: ironfang-signed-url
- name: SitePreviewRequest
  property_count: 19
  slug: ironfang-site-preview-request
- name: TemplateInput
  property_count: 4
  slug: ironfang-template-input
- name: Template
  property_count: 7
  slug: ironfang-template
- name: Usage
  property_count: 9
  slug: ironfang-usage
jsonld:
- class_count: 13
  name: Ironfang Context
  property_count: 67
  slug: ironfang-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ironfang.uk over HTTP requiring OAuth; 18 tools listed.
  name: Ironfang MCP Server
  slug: ironfang
- description: ''
  name: Ironfang MCP Server
  slug: mcp
modified: '2026-10-06'
name: Ironfang
nav: Providers
network: true
overview: 'Ironfang publishes 62 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batches API, Destinations API, and 59 more. Tagged areas include Developer Tools, Screenshots, website screenshot, HTML to PDF, and PDF API.


  The Ironfang catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ironfang''s developer surface includes engineering blog, documentation, changelog, authentication, CLI, sandbox, getting-started guide, and 34 more developer resources.'
plans:
- name: Ironfang Plans Pricing
  plan_count: 7
  slug: ironfang-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Ironfang Rate Limits
  slug: ironfang-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Ironfang API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 2
  slug: ironfang-rules
scopes:
- name: Ironfang Scopes
  scope_count: 10
  slug: ironfang-scopes
  summary_line: 10 scopes
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 92.8
    catalog_earned_first_party: 24.0
    catalog_gap: 22.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 61.8
    contract_governance: 35.6
    contract_quality: 79.8
    developer_ergonomics: 57.7
    discoverability: 80.0
    operational_transparency: 61.8
  previous_composite: 80.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 91.9
      total: 62
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/ironfang/ironfang-2026-10-11T105859.png
security:
- kind: authentication
  name: Ironfang Authentication
  slug: ironfang-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ironfang Domain Security
  slug: ironfang-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: ironfang-clean-authenticated-capture
  slug: ironfang-clean-authenticated-capture
- name: ironfang-durable-render-jobs
  slug: ironfang-durable-render-jobs
- name: ironfang-og-image-pipeline
  slug: ironfang-og-image-pipeline
- name: ironfang-signed-webhook-delivery
  slug: ironfang-signed-webhook-delivery
slug: ironfang
tags:
- Developer Tools
- Screenshots
- website screenshot
- HTML to PDF
- PDF API
- Image API
- OG Image API
- QR Code API
- Website-to-Video
- Rendering Infrastructure
- MCP
- UK-hosted
website: https://www.ironfang.com/
---
