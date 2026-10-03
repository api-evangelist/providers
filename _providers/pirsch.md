---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Pirsch Agentic Access
  operation_count: 97
  slug: pirsch-agentic-access
  summary_line: 97 operations · 54 acting
api_count: 1
apis:
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Manage shareable access links for dashboard visibility
  name: Pirsch Access Links API
  phrasing_intents:
  - id: listAccessLinks
    intent: List shareable access links for a domain
    question: Which shareable dashboard access links exist for my site?
  - id: createAccessLink
    intent: Create a shareable access link to a dashboard
    question: How do I give a client read access to my Pirsch dashboard without an account?
  - id: updateAccessLink
    intent: Change an access link's description or expiry
    question: Can I extend the expiry date of an access link I already shared?
  - id: deleteAccessLink
    intent: Revoke a shareable access link
    question: How can I revoke a dashboard link I shared with someone?
  phrasing_ops: 4
  slug: pirsch-access-links-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Obtain access tokens using OAuth2 client credentials
  name: Pirsch Authentication API
  phrasing_intents:
  - id: getToken
    intent: Obtain an API access token
    question: How do I get a bearer token for the Pirsch API from my client credentials?
  phrasing_ops: 1
  slug: pirsch-authentication-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Manage OAuth2 and access-key API clients
  name: Pirsch Clients API
  phrasing_intents:
  - id: listClients
    intent: List the API clients on a domain
    question: Which API clients and access tokens are set up for my site?
  - id: createClient
    intent: Create an API client for a domain
    question: How do I create an OAuth client so my server can send data to Pirsch?
  - id: deleteClient
    intent: Delete an API client
    question: How do I revoke an API client's access to my analytics?
  phrasing_ops: 3
  slug: pirsch-clients-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Define and manage conversion goals with path patterns or events
  name: Pirsch Conversion Goals API
  phrasing_intents:
  - id: listConversionGoals
    intent: List a domain's conversion goals
    question: Which conversion goals have I configured for my site?
  - id: createConversionGoal
    intent: Create a conversion goal
    question: How do I track a conversion when visitors reach my thank-you page?
  - id: updateConversionGoal
    intent: Edit an existing conversion goal
    question: How do I change the path pattern on a conversion goal I already created?
  - id: deleteConversionGoal
    intent: Delete a conversion goal
    question: How can I remove a conversion goal I no longer need?
  - id: testGoalRegex
    intent: Test a goal regex against a sample path
    question: Can I check whether my goal's regex matches a URL before saving it?
  phrasing_ops: 5
  slug: pirsch-conversion-goals-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Manage tracked domains and their configuration
  name: Pirsch Domains API
  phrasing_intents:
  - id: listDomains
    intent: List the domains I can access
    question: Which websites do I have access to in Pirsch?
  - id: createDomain
    intent: Add a website for tracking
    question: How do I start tracking a new website?
  - id: deleteDomain
    intent: Permanently delete a domain and its data
    question: How do I stop tracking a site and erase all its analytics?
  - id: updateDomainHostname
    intent: Change a domain's hostname
    question: My site moved to a new hostname. How do I update it?
  - id: updateDomainSubdomain
    intent: Change a domain's dashboard subdomain
    question: Can I rename the dashboard subdomain for one of my sites?
  - id: updateDomainTimezone
    intent: Change a domain's reporting timezone
    question: How do I make my site's statistics use my local timezone?
  - id: updateDomainSettings
    intent: Update a domain's settings
    question: Where do I change the general settings of an existing domain?
  - id: listAlternativeDomains
    intent: List a domain's alternative hostnames
    question: Which extra hostnames are counted toward my site's statistics?
  phrasing_ops: 11
  slug: pirsch-domains-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Schedule and manage recurring email analytics reports
  name: Pirsch Email Reports API
  phrasing_intents:
  - id: listEmailReports
    intent: List scheduled email reports for a domain
    question: Which scheduled email reports are set up for my site?
  - id: createEmailReport
    intent: Schedule an analytics email report
    question: How do I get my site's statistics emailed to my team every week?
  - id: updateEmailReport
    intent: Change an email report's schedule
    question: Can I change an existing email report from weekly to monthly?
  - id: deleteEmailReport
    intent: Cancel a scheduled email report
    question: How do I stop an analytics email report from being sent?
  phrasing_ops: 4
  slug: pirsch-email-reports-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Define and manage multi-step conversion funnels
  name: Pirsch Funnels API
  phrasing_intents:
  - id: listFunnels
    intent: List a domain's funnels
    question: Which funnels have I defined for my site?
  - id: createOrUpdateFunnel
    intent: Create or edit a funnel's steps
    question: How do I build a signup funnel from landing page to confirmation?
  - id: deleteFunnel
    intent: Delete a funnel
    question: How can I remove a funnel I no longer use?
  phrasing_ops: 3
  slug: pirsch-funnels-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Manage domain members, roles, and invitations
  name: Pirsch Members API
  phrasing_intents:
  - id: listMembers
    intent: List members of a domain or organization
    question: Who has access to my site's analytics?
  - id: inviteMembers
    intent: Invite people by email to a domain
    question: How do I invite my colleagues to view my site's statistics?
  - id: updateMember
    intent: Change a member's role
    question: How do I make a teammate an admin on my site?
  - id: removeMember
    intent: Remove a member's access
    question: How do I take away a former employee's access to my dashboard?
  - id: listInvitations
    intent: List pending invitations
    question: Which invitations are still pending for my site?
  - id: acceptInvitation
    intent: Accept an invitation
    question: How do I accept an invitation someone sent me to their site?
  - id: deleteInvitation
    intent: Withdraw a pending invitation
    question: How do I cancel an invitation I sent to the wrong email?
  phrasing_ops: 7
  slug: pirsch-members-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Create and manage UTM-enriched short links
  name: Pirsch Short Links API
  phrasing_intents:
  - id: listShortLinks
    intent: List a domain's short links
    question: Which short links have I created for my site?
  - id: createOrUpdateShortLink
    intent: Create or edit a tracked short link
    question: How do I make a short link with UTM campaign tags for a newsletter?
  - id: deleteShortLink
    intent: Delete a short link
    question: How can I remove a short link I no longer want to work?
  phrasing_ops: 3
  slug: pirsch-short-links-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Query analytics statistics by date range and filter criteria
  name: Pirsch Statistics API
  phrasing_intents:
  - id: getTotalStatistics
    intent: Get total visitors, views and bounces
    question: How many visitors and page views did my site get last month?
  - id: getVisitorStatistics
    intent: Chart visitors over time
    question: How did my daily visitor count change over the last quarter?
  - id: getPageStatistics
    intent: Get traffic broken down by page
    question: Which pages on my site got the most visitors?
  - id: getHostnameStatistics
    intent: Get traffic broken down by hostname
    question: How is traffic split between my site's different hostnames?
  - id: getReferrerStatistics
    intent: See which referrers send traffic
    question: Which websites are sending me the most visitors?
  - id: getChannelStatistics
    intent: Get traffic by channel
    question: How much of my traffic comes from search versus social versus direct?
  - id: getUtmSourceStatistics
    intent: Get visitors by UTM source
    question: Which utm_source values brought the most visitors?
  - id: getUtmMediumStatistics
    intent: Get visitors by UTM medium
    question: Which utm_medium, like email or cpc, drove the most traffic?
  phrasing_ops: 28
  slug: pirsch-statistics-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Send page views, events, and session keep-alive signals
  name: Pirsch Tracking API
  phrasing_intents:
  - id: sendPageView
    intent: Record a single page view server-side
    question: How do I track page views from my backend instead of a JavaScript snippet?
  - id: sendPageViewBatch
    intent: Record many page views in one request
    question: Can I send a backlog of page views in one request?
  - id: sendEvent
    intent: Record a custom event
    question: How do I track a button click or signup as a custom event?
  - id: sendEventBatch
    intent: Record many custom events at once
    question: Can I send multiple custom events in a single call?
  - id: keepSessionAlive
    intent: Extend a visitor's session
    question: How do I keep a visitor's session from timing out while they stay on a page?
  - id: keepSessionAliveBatch
    intent: Extend many visitor sessions at once
    question: Can I extend several visitor sessions in one request?
  phrasing_ops: 6
  slug: pirsch-tracking-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Filter traffic and configure spike/warning notifications
  name: Pirsch Traffic Management API
  phrasing_intents:
  - id: listTrafficFilters
    intent: List a domain's traffic filters
    question: Which traffic filters are excluding visits from my site's stats?
  - id: createOrUpdateTrafficFilter
    intent: Create or edit a traffic filter
    question: How do I exclude my office IP from my analytics?
  - id: deleteTrafficFilter
    intent: Delete a traffic filter
    question: How do I stop excluding traffic that a filter currently blocks?
  - id: toggleSpikeNotifications
    intent: Turn traffic spike alerts on or off
    question: Can I get notified when my site suddenly gets a traffic spike?
  - id: configureSpikeNotifications
    intent: Set the traffic spike alert threshold
    question: What counts as a spike, and can I set the threshold myself?
  - id: toggleTrafficWarnings
    intent: Turn no-traffic warnings on or off
    question: Can I be warned if my site stops receiving traffic?
  - id: configureTrafficWarnings
    intent: Set days without traffic before a warning
    question: How many days without traffic should pass before I'm warned?
  phrasing_ops: 7
  slug: pirsch-traffic-management-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Manage the authenticated user account
  name: Pirsch User API
  phrasing_intents:
  - id: getUser
    intent: Get my account details
    question: What account information does Pirsch have on me?
  - id: updateUserName
    intent: Change my full name
    question: How do I change the name shown on my account?
  - id: updateUserEmail
    intent: Change my account email address
    question: How do I move my account to a new email address?
  - id: updateUserPassword
    intent: Change my password
    question: How do I change my account password?
  - id: updateUserLanguage
    intent: Change my interface language
    question: Can I switch the dashboard interface to German?
  - id: updateUserFilter
    intent: Change my default dashboard time range
    question: Can the dashboard open on the last 30 days by default?
  - id: getUserNews
    intent: Get release news and announcements
    question: What's new in the latest product releases?
  - id: markNewsRead
    intent: Mark news items as read
    question: How do I dismiss announcements I've already read?
  phrasing_ops: 9
  slug: pirsch-user-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Save and manage custom analytics views
  name: Pirsch Views API
  phrasing_intents:
  - id: listViews
    intent: List saved analytics views
    question: Which saved dashboard views do I have for my site?
  - id: createOrUpdateView
    intent: Save or edit an analytics view
    question: How do I save a dashboard view for a fixed date range?
  - id: deleteView
    intent: Delete a saved view
    question: How can I remove a saved view I no longer use?
  phrasing_ops: 3
  slug: pirsch-views-api
- baseURL: https://api.pirsch.io/api/v1
  baseurl_source: declared
  description: Configure webhooks for event-driven integrations
  name: Pirsch Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List a domain's webhooks
    question: Which webhooks are configured for my site?
  - id: createOrUpdateWebhook
    intent: Create or edit a webhook
    question: How do I get a webhook call when an event happens on my site?
  - id: deleteWebhook
    intent: Delete a webhook
    question: How do I stop a webhook from firing?
  phrasing_ops: 3
  slug: pirsch-webhooks-api
artifact_total: 49
asyncapis:
- description: ''
  name: Pirsch Webhooks
  slug: pirsch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pirsch Access Links API
  slug: open-pirsch-access-links-api
- collection_type: open
  name: Pirsch Access Links Authentication API
  slug: open-pirsch-authentication-api
- collection_type: open
  name: Pirsch Access Links Clients API
  slug: open-pirsch-clients-api
- collection_type: open
  name: Pirsch Access Links Conversion Goals API
  slug: open-pirsch-conversion-goals-api
- collection_type: open
  name: Pirsch Access Links Domains API
  slug: open-pirsch-domains-api
- collection_type: open
  name: Pirsch Access Links Email Reports API
  slug: open-pirsch-email-reports-api
- collection_type: open
  name: Pirsch Access Links Funnels API
  slug: open-pirsch-funnels-api
- collection_type: open
  name: Pirsch Access Links Members API
  slug: open-pirsch-members-api
- collection_type: open
  name: Pirsch Access Links Short Links API
  slug: open-pirsch-short-links-api
- collection_type: open
  name: Pirsch Access Links Statistics API
  slug: open-pirsch-statistics-api
- collection_type: open
  name: Pirsch Access Links Tracking API
  slug: open-pirsch-tracking-api
- collection_type: open
  name: Pirsch Access Links Traffic Management API
  slug: open-pirsch-traffic-management-api
- collection_type: open
  name: Pirsch Access Links User API
  slug: open-pirsch-user-api
- collection_type: open
  name: Pirsch Access Links Views API
  slug: open-pirsch-views-api
- collection_type: open
  name: Pirsch Access Links Webhooks API
  slug: open-pirsch-webhooks-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/agentic-access/pirsch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pirsch-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/security/pirsch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pirsch-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/authentication/pirsch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pirsch-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pirsch.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pirsch.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pirsch-analytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/emvi-software-gmbh-pirsch-analytics/
- group: company
  title: ''
  type: Blog
  url: https://pirsch.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pirsch.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/PirschAnalytics
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/plans/pirsch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pirsch-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/rate-limits/pirsch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pirsch-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/finops/pirsch-finops.yml
  title: ''
  type: FinOps
  url: finops/pirsch-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pirsch.io/api-sdks/api-v1
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pirsch.io/api-sdks/api-v1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pirsch.io/get-started/frontend-integration
- group: operate
  title: ''
  type: Support
  url: https://forum.pirsch.io
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.pirsch.io/faq
- group: start
  title: ''
  type: Console
  url: https://pirsch.pirsch.io
- group: company
  title: ''
  type: About
  url: https://pirsch.io/about-us
- group: company
  title: ''
  type: News
  url: https://pirsch.io/news
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://pirsch.io/static/files/Data%20Processing%20Agreement%20-%20Pirsch%20Analytics.pdf
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/pirsch.bsky.social
- group: company
  title: ''
  type: Mastodon
  url: https://social.anoxinon.de/@pirsch
- group: other
  title: ''
  type: ProductHunt
  url: https://www.producthunt.com/products/pirsch-analytics
- group: start
  title: ''
  type: SignUp
  url: https://pirsch.io/signup
- group: start
  title: ''
  type: Login
  url: https://pirsch.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pirsch.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pirsch.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pirsch-analytics
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pirsch.io/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/changelog/pirsch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pirsch-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/packages/pirsch-packages.yml
  title: ''
  type: Packages
  url: packages/pirsch-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/packages/pirsch-packages.yml
  title: ''
  type: SDKs
  url: packages/pirsch-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/llms/pirsch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pirsch-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/conventions/pirsch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pirsch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/errors/pirsch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pirsch-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/lifecycle/pirsch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pirsch-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/conformance/pirsch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pirsch-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.pirsch.io/privacy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/data-model/pirsch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pirsch-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/components/pirsch-components.yml
  title: ''
  type: Components
  url: components/pirsch-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/asyncapi/pirsch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pirsch-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/mcp/pirsch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pirsch-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/vocabulary/pirsch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pirsch-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/json-ld/pirsch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pirsch-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/rules/pirsch-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/pirsch-jsonschema-spectral-rules.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/json-schema/pirsch-hit-request.json
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-hit-request.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/json-schema/pirsch-event-request.json
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-event-request.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/json-schema/pirsch-visitor-stats.json
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-visitor-stats.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/json-schema/pirsch-domain.json
  title: ''
  type: JSONSchema
  url: json-schema/pirsch-domain.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/examples/pirsch-hit-request-example.json
  title: ''
  type: Examples
  url: examples/pirsch-hit-request-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/examples/pirsch-event-request-example.json
  title: ''
  type: Examples
  url: examples/pirsch-event-request-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/examples/pirsch-token-request-example.json
  title: ''
  type: Examples
  url: examples/pirsch-token-request-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/examples/pirsch-token-response-example.json
  title: ''
  type: Examples
  url: examples/pirsch-token-response-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/examples/pirsch-visitor-stats-response-example.json
  title: ''
  type: Examples
  url: examples/pirsch-visitor-stats-response-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/examples/pirsch-domain-example.json
  title: ''
  type: Examples
  url: examples/pirsch-domain-example.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-access-links-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-access-links-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-authentication-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-clients-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-clients-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-conversion-goals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-conversion-goals-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-domains-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-domains-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-email-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-email-reports-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-funnels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-funnels-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-members-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-members-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-short-links-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-short-links-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-statistics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-statistics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-tracking-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-tracking-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-traffic-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-traffic-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-user-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-user-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-views-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-views-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/overlays/pirsch-webhooks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pirsch-webhooks-overlay.yaml
created: '2026-06-13'
description: Pirsch is a privacy-first website analytics platform built and hosted in Germany. GDPR, CCPA, PECR, and Schrems II compliant, it tracks page views, sessions, custom events, conversion goals, funnels, and traffic sources without cookies or personal data storage. Developers access all data via a RESTful API with OAuth and access-key authentication, supported by official Go, JavaScript, and PHP SDKs.
examples:
- key_count: 16
  name: Pirsch Domain Example
  slug: pirsch-domain-example
- key_count: 8
  name: Pirsch Event Request Example
  slug: pirsch-event-request-example
- key_count: 10
  name: Pirsch Hit Request Example
  slug: pirsch-hit-request-example
- key_count: 2
  name: Pirsch Token Request Example
  slug: pirsch-token-request-example
- key_count: 2
  name: Pirsch Token Response Example
  slug: pirsch-token-response-example
finops:
- name: Pirsch Finops
  service_category: ''
  slug: pirsch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pirsch.png
json_schemas:
- name: Domain
  property_count: 16
  slug: pirsch-domain
- name: EventRequest
  property_count: 14
  slug: pirsch-event-request
- name: HitRequest
  property_count: 13
  slug: pirsch-hit-request
- name: VisitorStats
  property_count: 12
  slug: pirsch-visitor-stats
jsonld:
- class_count: 7
  name: Pirsch Context
  property_count: 63
  slug: pirsch-context
layout: provider
modified: '2026-08-13'
name: Pirsch
nav: Providers
network: true
overview: 'Pirsch publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Access Links API, Authentication API, Clients API, and 12 more. Tagged areas include Analytics, Web Analytics, Privacy, GDPR, and Cookie-Free.


  The Pirsch catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Pirsch''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 66 more developer resources.'
plans:
- name: Pirsch Plans Pricing
  plan_count: 3
  slug: pirsch-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Pirsch Rate Limits
  slug: pirsch-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pirsch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pirsch-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.8
    catalog_earned_first_party: 24.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 23.5
    contract_quality: 64.8
    developer_ergonomics: 66.1
    discoverability: 67.0
    operational_transparency: 57.9
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/screenshots/pirsch-2026-06-20T191730.png
security:
- kind: authentication
  name: Pirsch Authentication
  slug: pirsch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pirsch Domain Security
  slug: pirsch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pirsch
tags:
- Analytics
- Web Analytics
- Privacy
- GDPR
- Cookie-Free
- Page Views
- Sessions
- Event
- Conversion Goals
- Funnels
- Traffic Sources
website: https://pirsch.io
---
