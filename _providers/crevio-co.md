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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 296
  human_in_the_loop: 8
  name: Crevio Co Agentic Access
  operation_count: 529
  slug: crevio-co-agentic-access
  summary_line: 529 operations · 296 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Per-user access checks for gated resources
  name: Crevio Access API
  slug: crevio-co-access-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Current account information
  name: Crevio Account API
  slug: crevio-co-account-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Paid advertising — campaigns, ad groups, ads, audiences, targeting, leads, conversions, and reports across Meta, Google, TikTok, LinkedIn, Pinterest, and X.
  name: Crevio Ads API
  slug: crevio-co-ads-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Who the agent's inbox answers
  name: Crevio Allowed Senders API
  slug: crevio-co-allowed-senders-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Account-wide business analytics
  name: Crevio Analytics API
  slug: crevio-co-analytics-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Human-in-the-loop approvals for gated actions
  name: Crevio Approvals API
  slug: crevio-co-approvals-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Download files that runs and scripts produced
  name: Crevio Artifacts API
  slug: crevio-co-artifacts-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: AI audio generation
  name: Crevio Audio API
  slug: crevio-co-audio-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Hosted billing pages for your customers
  name: Crevio Billing Portal API
  slug: crevio-co-billing-portal-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Blog post categories
  name: Crevio Blog Categories API
  slug: crevio-co-blogcategories-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Blog content management
  name: Crevio Blog Posts API
  slug: crevio-co-blogposts-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Reservations made against event types.
  name: Crevio Bookings API
  slug: crevio-co-bookings-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Named bot identities (persona, skills, toolsets) chats and tasks can run as
  name: Crevio Bots API
  slug: crevio-co-bots-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: One-to-many email sending
  name: Crevio Broadcasts API
  slug: crevio-co-broadcasts-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Outbound phone calls placed by the account's agent
  name: Crevio Calls API
  slug: crevio-co-calls-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Course chapters
  name: Crevio Chapters API
  slug: crevio-co-chapters-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Delegate work to the Crevio agent and read its replies
  name: Crevio Chats API
  slug: crevio-co-chats-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Account-wide checkout settings
  name: Crevio Checkout Configuration API
  slug: crevio-co-checkoutconfiguration-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Shareable checkout links
  name: Crevio Checkout Links API
  slug: crevio-co-checkoutlinks-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Checkout session management
  name: Crevio Checkouts API
  slug: crevio-co-checkouts-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Third-party app connections (connect, list, execute)
  name: Crevio Connections API
  slug: crevio-co-connections-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Customer relationship management
  name: Crevio Customers API
  slug: crevio-co-customers-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: 'Included business data: search the tool catalog, then run a tool (website/SEO, people, companies, local businesses, social, e-commerce, finance, jobs, reviews, ads, real estate, news, apps, travel, we'
  name: Crevio Data API
  slug: crevio-co-data-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Site deployments and build logs
  name: Crevio Deployments API
  slug: crevio-co-deployments-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Discount code management
  name: Crevio Discounts API
  slug: crevio-co-discounts-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Custom web domains for your sites.
  name: Crevio Domains API
  slug: crevio-co-domains-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Inboxes, threads, messages, drafts and delivery events
  name: Crevio Email API
  slug: crevio-co-email-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Addresses no send path will deliver to
  name: Crevio Email Suppressions API
  slug: crevio-co-email-suppressions-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Events an account can subscribe to
  name: Crevio Events API
  slug: crevio-co-events-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Scheduled sessions of an event experience
  name: Crevio Event Sessions API
  slug: crevio-co-eventsessions-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Digital experiences (courses, communities, downloads)
  name: Crevio Experiences API
  slug: crevio-co-experiences-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: File uploads and external media management
  name: Crevio Files API
  slug: crevio-co-files-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Documents generated for a formation
  name: Crevio Formation Documents API
  slug: crevio-co-formationdocuments-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Whitelabel business formation via doola Partner API
  name: Crevio Formations API
  slug: crevio-co-formations-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Hosted forms that capture leads and submissions
  name: Crevio Forms API
  slug: crevio-co-forms-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Form submission management
  name: Crevio Form Submissions API
  slug: crevio-co-formsubmissions-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Posts inside a forum experience
  name: Crevio Forum Posts API
  slug: crevio-co-forumposts-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: AI image generation, editing and stock search
  name: Crevio Images API
  slug: crevio-co-images-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Invoice creation, payment, and lifecycle management
  name: Crevio Invoices API
  slug: crevio-co-invoices-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Long-running asynchronous jobs
  name: Crevio Jobs API
  slug: crevio-co-jobs-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Find, verify and enrich business leads (Hunter.io-backed).
  name: Crevio Leads API
  slug: crevio-co-leads-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Terms, privacy and refund pages for the storefront
  name: Crevio Legal Pages API
  slug: crevio-co-legalpages-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Lessons inside a course chapter
  name: Crevio Lessons API
  slug: crevio-co-lessons-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Links inside a link-in-bio experience
  name: Crevio Link Items API
  slug: crevio-co-linkitems-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Account activity log
  name: Crevio Logs API
  slug: crevio-co-logs-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Current user profile
  name: Crevio Me API
  slug: crevio-co-me-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Order history and details
  name: Crevio Orders API
  slug: crevio-co-orders-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Self-contained HTML pages hosted at a stable link
  name: Crevio Pages API
  slug: crevio-co-pages-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Recorded consent to place calls to a number
  name: Crevio Phone Consents API
  slug: crevio-co-phone-consents-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Phone numbers provisioned for the account
  name: Crevio Phone Numbers API
  slug: crevio-co-phone-numbers-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Do-not-call entries
  name: Crevio Phone Suppressions API
  slug: crevio-co-phone-suppressions-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: The plans Crevio sells, their credit tiers, prices and limits.
  name: Crevio Plans API
  slug: crevio-co-plans-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Product pricing tiers
  name: Crevio Price Variants API
  slug: crevio-co-pricevariants-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Digital product catalog
  name: Crevio Products API
  slug: crevio-co-products-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Refund management
  name: Crevio Refunds API
  slug: crevio-co-refunds-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Product reviews
  name: Crevio Reviews API
  slug: crevio-co-reviews-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Reusable availability schedules that back event types.
  name: Crevio Schedules API
  slug: crevio-co-schedules-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Run JavaScript on the account's computer, without an agent turn
  name: Crevio Script Runs API
  slug: crevio-co-scriptruns-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Account-level environment variables shared across the account's sites
  name: Crevio Secrets API
  slug: crevio-co-secrets-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Timed email series people move through one step at a time
  name: Crevio Sequences API
  slug: crevio-co-sequences-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: AI-built sites — storefronts and web apps
  name: Crevio Sites API
  slug: crevio-co-sites-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: AI skills marketplace — search the catalog and install or uninstall skills for your account's agent.
  name: Crevio Skills API
  slug: crevio-co-skills-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Texting new leads and past customers until they answer. The email counterpart is Sequences.
  name: Crevio SMS follow-ups API
  slug: crevio-co-sms-follow-ups-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Texts on business phone lines.
  name: Crevio SMS messages API
  slug: crevio-co-sms-messages-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Social media management (accounts, posts, media).
  name: Crevio Socials API
  slug: crevio-co-socials-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: API and account status
  name: Crevio Status API
  slug: crevio-co-status-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Subscription lifecycle management (cancel, pause, resume)
  name: Crevio Subscriptions API
  slug: crevio-co-subscriptions-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Customer tags
  name: Crevio Tags API
  slug: crevio-co-tags-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Individual execution records for AI tasks.
  name: Crevio Task Runs API
  slug: crevio-co-taskruns-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: AI tasks — scheduled or event-triggered agentic work (cron, interval, once, immediate, event).
  name: Crevio Tasks API
  slug: crevio-co-tasks-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Members, roles, credit limits and invitations
  name: Crevio Team API
  slug: crevio-co-team-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Discussion topics inside a forum experience
  name: Crevio Topics API
  slug: crevio-co-topics-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Credit usage and transaction history
  name: Crevio Usage API
  slug: crevio-co-usage-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Users of the account
  name: Crevio Users API
  slug: crevio-co-users-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: AI video generation
  name: Crevio Video API
  slug: crevio-co-video-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Buyers waiting for approval on price variants that require it.
  name: Crevio Waitlist Entries API
  slug: crevio-co-waitlist-entries-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Web search & scraping (search, read, map, crawl, extract, research), backed by Firecrawl.
  name: Crevio Web API
  slug: crevio-co-web-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: API key management
  name: Crevio API Keys API
  slug: crevio-co-api-keys-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Third-party event sources that trigger tasks
  name: Crevio Event Sources API
  slug: crevio-co-event-sources-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Bookable services customers can schedule time on.
  name: Crevio Event Types API
  slug: crevio-co-event-types-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Order line items
  name: Crevio Order Items API
  slug: crevio-co-order-items-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Webhook endpoint management
  name: Crevio Webhook Endpoints API
  slug: crevio-co-webhook-endpoints-api
- baseURL: https://api.crevio.co/v1
  baseurl_source: declared
  description: Webhook event delivery history
  name: Crevio Webhook Events API
  slug: crevio-co-webhook-events-api
artifact_total: 102
asyncapis:
- description: ''
  name: Crevio Co Webhooks
  slug: crevio-co-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://crevio.co/docs/introduction/getting-started
- group: agent
  href: https://artifacts.apis.io/crevio-co/agentic-access/crevio-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crevio-co-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/crevio-co/rate-limits/crevio-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crevio-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crevio-co/plans/crevio-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crevio-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/rules/crevio-co-rules.yml
  title: ''
  type: Spectral
  url: rules/crevio-co-rules.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/json-ld/crevio-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crevio-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/crevio-co/vocabulary/crevio-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crevio-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crevio-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/asyncapi/crevio-co-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/crevio-co-webhooks.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/data-model/crevio-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crevio-co-data-model.yml
- group: operate
  href: https://artifacts.apis.io/crevio-co/changelog/crevio-co-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crevio-co-changelog.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/conventions/crevio-co-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/crevio-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/conventions/crevio-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crevio-co-conventions.yml
- group: auth
  href: https://artifacts.apis.io/crevio-co/authentication/crevio-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crevio-co-authentication.yml
- group: operate
  href: https://artifacts.apis.io/crevio-co/lifecycle/crevio-co-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/crevio-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/lifecycle/crevio-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crevio-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/errors/crevio-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crevio-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crevio-co/conformance/crevio-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crevio-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crevio-co/llms/crevio-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crevio-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/crevio-co/well-known/crevio-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crevio-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/crevio-co/hosts/crevio-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crevio-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/crevio-co/vendors/crevio-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crevio-co-vendors.yml
- group: build
  href: https://artifacts.apis.io/crevio-co/packages/crevio-co-packages.yml
  title: ''
  type: SDKs
  url: packages/crevio-co-packages.yml
- group: build
  href: https://artifacts.apis.io/crevio-co/packages/crevio-co-packages.yml
  title: ''
  type: Packages
  url: packages/crevio-co-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://crevio.co/security
- group: start
  title: ''
  type: Login
  url: https://crevio.co/users/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/creviolabs
- group: operate
  title: ''
  type: ChangeLog
  url: https://crevio.co/docs/changelog
- group: auth
  href: https://artifacts.apis.io/crevio-co/security/crevio-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crevio-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crevio.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crevio.co/docs
- group: docs
  title: ''
  type: Documentation
  url: https://crevio.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://crevio.co/docs/developer/api-reference/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://crevio.co/contact
- group: company
  title: ''
  type: Blog
  url: https://crevio.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://crevio.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crevio.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crevio.co/legal/privacy-policy
created: '2026-11-04'
description: 'Crevio is an AI-powered platform that runs your business. You describe what you want to sell — Crevio builds, launches, and grows it. Not AI as a feature. AI as the foundation. You create. We run the business. Crevio runs your small business with AI: website, customers, payments, and marketing, all handled for you.'
image: https://crevio.co/og_image.png
json_schemas:
- name: AiTaskRequest
  property_count: 25
  slug: crevio-co-ai-task-request
- name: AiTaskRun
  property_count: 32
  slug: crevio-co-ai-task-run
- name: AiTask
  property_count: 39
  slug: crevio-co-ai-task
- name: EmailSequenceRequest
  property_count: 9
  slug: crevio-co-email-sequence-request
- name: EmailSequence
  property_count: 14
  slug: crevio-co-email-sequence
- name: FormRequest
  property_count: 13
  slug: crevio-co-form-request
jsonld:
- class_count: 120
  name: Crevio Co Context
  property_count: 473
  slug: crevio-co-context
layout: provider
modified: '2026-11-04'
name: Crevio
nav: Providers
network: true
overview: 'Crevio publishes 83 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Account API, Ads API, and 80 more. Tagged areas include Business Formation, Website Builder, Payments, and CRM.


  The Crevio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Crevio''s developer surface includes getting-started guide, changelog, authentication, documentation, API reference, support, engineering blog, and 31 more developer resources.'
plans:
- name: Crevio Co Plans Pricing
  plan_count: 3
  slug: crevio-co-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Crevio Co Rate Limits
  slug: crevio-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 119
  extends:
  - spectral:oas
  name: Crevio API Rules
  rule_count: 78
  severity_counts:
    error: 65
    hint: 0
    info: 3
    warn: 10
  slug: crevio-co-rules
score:
  band: exemplar
  composite: 67.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 74.3
    developer_ergonomics: 66.1
    discoverability: 57.1
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 83
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crevio Co Authentication
  slug: crevio-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Crevio Co Domain Security
  slug: crevio-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: crevio-co-checkout-flow
  slug: crevio-co-checkout-flow
- name: crevio-co-invoice-creation-and-void
  slug: crevio-co-invoice-creation-and-void
- name: crevio-co-list-and-get-customer
  slug: crevio-co-list-and-get-customer
- name: crevio-co-manage-subscription
  slug: crevio-co-manage-subscription
- name: crevio-co-refund-processing
  slug: crevio-co-refund-processing
slug: crevio-co
tags:
- Business Formation
- Website Builder
- Payments
- CRM
website: https://crevio.co/
---
