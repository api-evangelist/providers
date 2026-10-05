---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.2
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Snov Io Agentic Access
  operation_count: 65
  slug: snov-io-agentic-access
  summary_line: 65 operations · 32 acting
api_count: 1
apis:
- description: Verify the deliverability and validity of up to 10 email addresses per request using a two-step async API. Returns validity status, MX record checks, and disposable email detection results.
  name: Snov.io Email Verification API
  slug: snovio-email-verification-api
- description: Create, update, delete, and manage multi-channel outreach campaigns programmatically. Supports email step content management, recipient management, campaign state changes, and full analytics reporting
  name: Snov.io Campaigns API
  slug: snovio-campaigns-api
- description: Add, search, and manage prospect records and lists within Snov.io. Supports custom fields, list creation, CRM pipeline management, and do-not-email suppression list operations.
  name: Snov.io Prospect Management API
  slug: snovio-prospect-management-api
- description: Create and manage email warm-up campaigns to improve deliverability scores. Supports full CRUD operations on warm-up campaigns and provides statistical reporting on warm-up progress.
  name: Snov.io Email Warm-up API
  slug: snovio-email-warm-up-api
- description: Subscribe to real-time event notifications from the Snov.io platform. Supports listing, creating, updating, and deleting webhook subscriptions for automated event-driven integrations.
  name: Snov.io Webhooks API
  slug: snovio-webhooks-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: OAuth 2.0 token management
  name: Snov.io Authentication API
  phrasing_intents:
  - id: getAccessToken
    intent: Get an API access token
    question: How do I get a bearer token for the Snov.io API using my client ID and secret?
  phrasing_ops: 1
  slug: snov-io-authentication-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Create and manage multi-channel outreach campaigns
  name: Snov.io Campaigns API
  phrasing_intents:
  - id: listCampaigns
    intent: List my outreach campaigns
    question: Which outreach campaigns do I have set up in Snov.io?
  - id: createCampaign
    intent: Create an outreach campaign
    question: How do I create a new multi-channel outreach campaign?
  - id: getCampaign
    intent: Get a campaign's details
    question: What settings does one specific campaign have?
  - id: updateCampaign
    intent: Update an existing campaign's settings
    question: Can I rename a campaign I already created?
  - id: deleteCampaign
    intent: Delete a campaign
    question: How do I permanently remove a campaign?
  - id: changeCampaignState
    intent: Start, pause or stop a campaign
    question: Can I pause a running campaign and resume it later?
  - id: listEmailSchedules
    intent: List email send schedules
    question: What send schedules are available for my campaign emails?
  - id: createEmailStepContent
    intent: Add an email step to a campaign
    question: Can I add a follow-up email step to a campaign through the API?
  phrasing_ops: 24
  slug: snov-io-campaigns-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: CRM pipeline and stage management
  name: Snov.io CRM Pipeline API
  phrasing_intents:
  - id: listPipelines
    intent: List CRM pipelines
    question: What sales pipelines are set up in my Snov.io CRM?
  - id: listPipelineStages
    intent: List CRM pipeline stages
    question: What stages does my sales pipeline have?
  phrasing_ops: 2
  slug: snov-io-crm-pipeline-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Search for company information and email addresses by domain
  name: Snov.io Domain Search API
  phrasing_intents:
  - id: startDomainSearch
    intent: Start a company domain search
    question: How do I look up what Snov.io knows about a company domain?
  - id: getDomainSearchResult
    intent: Get company domain search results
    question: Where do I get the results of a domain search I already started?
  - id: startDomainProspectSearch
    intent: Find prospects at a company domain
    question: Can I find people who work at a company by its domain?
  - id: getDomainProspectSearchResult
    intent: Get domain prospect search results
    question: Where do I collect the prospect profiles from a domain prospect search?
  - id: startDomainEmailsSearch
    intent: Find all email addresses at a domain
    question: Can I get every email address associated with a company domain?
  - id: getDomainEmailsSearchResult
    intent: Get domain email addresses search results
    question: Where are the email addresses from my domain emails search?
  - id: startGenericContactsSearch
    intent: Find generic contact addresses at a domain
    question: Can I find a company's info@ or support@ style addresses?
  - id: getGenericContactsSearchResult
    intent: Get generic contacts search results
    question: Where do I get the info@ and support@ addresses my search found?
  phrasing_ops: 9
  slug: snov-io-domain-search-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Manage sender email accounts
  name: Snov.io Email Accounts API
  phrasing_intents:
  - id: listEmailAccounts
    intent: List connected sender email accounts
    question: Which sender mailboxes have I connected?
  - id: addEmailAccount
    intent: Connect a sender email account
    question: How do I connect a new mailbox for sending campaigns using SMTP?
  - id: updateEmailAccount
    intent: Update a sender email account
    question: Can I change the signature on a sender account I already connected?
  - id: checkSenderStatus
    intent: Check a sender account's connection status
    question: Why is my sender mailbox not sending — is its SMTP or IMAP connection broken?
  phrasing_ops: 4
  slug: snov-io-email-accounts-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Find email addresses by name, LinkedIn, or domain
  name: Snov.io Email Finder API
  phrasing_intents:
  - id: startFindEmailsByName
    intent: Find emails from a person's name and domain
    question: Can I find someone's email if I know their name and company domain?
  - id: getFindEmailsByNameResult
    intent: Get find-emails-by-name results
    question: Where do I pick up the emails found from names and domains?
  - id: startFindDomainByCompanyName
    intent: Find company domains from company names
    question: I only have company names — can I find their website domains?
  - id: getFindDomainByCompanyNameResult
    intent: Get company-name-to-domain results
    question: Where do I get the domains found for my company names?
  - id: startLinkedInProfileEnrichment
    intent: Enrich LinkedIn profiles by URL
    question: Can I get contact details from a list of LinkedIn profile URLs?
  - id: getLinkedInProfileEnrichmentResult
    intent: Get LinkedIn profile enrichment results
    question: Where are the enriched LinkedIn profiles I requested?
  - id: getProfileByEmail
    intent: Enrich a person's profile from an email
    question: Can I find out who's behind an email address — name, job, company?
  phrasing_ops: 7
  slug: snov-io-email-finder-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Verify email deliverability and validity
  name: Snov.io Email Verification API
  phrasing_intents:
  - id: startEmailVerification
    intent: Verify a batch of email addresses
    question: How do I check whether email addresses are valid before sending?
  - id: getEmailVerificationResult
    intent: Get email verification results
    question: Where do I see which emails passed verification?
  phrasing_ops: 2
  slug: snov-io-email-verification-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Manage email warm-up campaigns for improved deliverability
  name: Snov.io Email Warm-up API
  phrasing_intents:
  - id: listWarmUpCampaigns
    intent: List email warm-up campaigns
    question: Which mailboxes do I have warm-up running for?
  - id: createWarmUpCampaign
    intent: Start warming up a sender mailbox
    question: How do I warm up a new mailbox to improve deliverability?
  - id: getWarmUpCampaign
    intent: Get a warm-up campaign's details
    question: What settings is a particular warm-up campaign using?
  - id: updateWarmUpCampaign
    intent: Change a warm-up campaign's settings
    question: Can I pause a warm-up or make it run without an end date?
  phrasing_ops: 4
  slug: snov-io-email-warm-up-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Manage prospect records and lists
  name: Snov.io Prospects API
  phrasing_intents:
  - id: addProspect
    intent: Add a prospect to a list
    question: How do I add a new contact to one of my prospect lists?
  - id: findProspectById
    intent: Look up a prospect by ID
    question: Can I fetch a prospect record if I have its ID?
  - id: findProspectByEmail
    intent: Look up a saved prospect by email
    question: Is this email address already saved as a prospect in my lists?
  - id: getProspectCustomFields
    intent: List prospect custom fields
    question: What custom fields are defined for my prospects?
  - id: listProspectLists
    intent: List prospect lists
    question: Which prospect lists do I have?
  - id: viewProspectsInList
    intent: View the prospects in a list
    question: Who is in a specific prospect list?
  - id: createProspectList
    intent: Create a prospect list
    question: How do I create a new list to organize prospects?
  phrasing_ops: 7
  slug: snov-io-prospects-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: User account management
  name: Snov.io User API
  phrasing_intents:
  - id: getUserBalance
    intent: Check my credit balance
    question: How many Snov.io credits do I have left?
  phrasing_ops: 1
  slug: snov-io-user-api
- baseURL: https://api.snov.io
  baseurl_source: declared
  description: Real-time event webhook subscriptions
  name: Snov.io Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List webhook subscriptions
    question: Which webhooks are currently subscribed on my account?
  - id: addWebhook
    intent: Subscribe a webhook to an event
    question: How do I get real-time notifications when an event happens?
  - id: updateWebhook
    intent: Update a webhook subscription
    question: Can I change the URL of a webhook I already set up?
  - id: deleteWebhook
    intent: Delete a webhook subscription
    question: How do I stop receiving webhook notifications permanently?
  phrasing_ops: 4
  slug: snov-io-webhooks-api
- description: 'First-party remote Model Context Protocol server exposing 100+ Snov.io actions to AI assistants — prospect search and enrichment, list and folder management, email verification, Sales CRM (pipelines, '
  name: Snov.io Outreach MCP Server
  slug: snov-io-mcp-server
artifact_total: 46
asyncapis:
- description: ''
  name: Snov Io Webhooks
  slug: snov-io-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snov.io Authentication API
  slug: open-snov-io-authentication-api
- collection_type: open
  name: Snov.io Authentication Campaigns API
  slug: open-snov-io-campaigns-api
- collection_type: open
  name: Snov.io Authentication CRM Pipeline API
  slug: open-snov-io-crm-pipeline-api
- collection_type: open
  name: Snov.io Authentication Domain Search API
  slug: open-snov-io-domain-search-api
- collection_type: open
  name: Snov.io Authentication Email Accounts API
  slug: open-snov-io-email-accounts-api
- collection_type: open
  name: Snov.io Authentication Email Finder API
  slug: open-snov-io-email-finder-api
- collection_type: open
  name: Snov.io Authentication Email Verification API
  slug: open-snov-io-email-verification-api
- collection_type: open
  name: Snov.io Authentication Email Verifier API
  slug: open-snov-io-email-verifier-api
- collection_type: open
  name: Snov.io Authentication Email Warm-up API
  slug: open-snov-io-email-warm-up-api
- collection_type: open
  name: Snov.io Authentication Enrichment API
  slug: open-snov-io-enrichment-api
- collection_type: open
  name: Snov.io Authentication Prospects API
  slug: open-snov-io-prospects-api
- collection_type: open
  name: Snov.io Authentication Sender Accounts API
  slug: open-snov-io-sender-accounts-api
- collection_type: open
  name: Snov.io Authentication User API
  slug: open-snov-io-user-api
- collection_type: open
  name: Snov.io Authentication Warm-up API
  slug: open-snov-io-warm-up-api
- collection_type: open
  name: Snov.io Authentication Webhooks API
  slug: open-snov-io-webhooks-api
- collection_type: open
  name: Snov.io API
  slug: open-snov
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/capabilities/snov-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snov-io-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/agentic-access/snov-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snov-io-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/security/snov-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snov-io-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/authentication/snov-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snov-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://snov.io/
- group: docs
  title: ''
  type: Documentation
  url: https://snov.io/api
- group: other
  title: ''
  type: Knowledgebase
  url: https://snov.io/knowledgebase/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devsnovio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snovio
- group: company
  title: ''
  type: Blog
  url: https://snov.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://snov.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/snov_io
- group: auth
  title: ''
  type: Authentication
  url: https://snov.io/knowledgebase/how-to-use-snov-io-api/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/plans/snov-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snov-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/rate-limits/snov-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snov-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/finops/snov-io-finops.yml
  title: ''
  type: FinOps
  url: finops/snov-io-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/scopes/snov-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/snov-io-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/mcp/snov-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snov-io-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/mcp/snov-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snov-io-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/well-known/snov-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snov-io-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/packages/snov-io-packages.yml
  title: ''
  type: Packages
  url: packages/snov-io-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/llms/snov-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snov-io-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/conventions/snov-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snov-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/errors/snov-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snov-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/lifecycle/snov-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snov-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/conformance/snov-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snov-io-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/security/snov-io-trust-center.yml
  title: ''
  type: Compliance
  url: security/snov-io-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/security/snov-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/snov-io-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/data-model/snov-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snov-io-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/changelog/snov-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/snov-io-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/asyncapi/snov-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/snov-io-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/graphql/snov-io-graphql.md
  title: ''
  type: GraphQL
  url: graphql/snov-io-graphql.md
- group: docs
  title: ''
  type: APIReference
  url: https://snov.io/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://snov.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://snov.io/knowledgebase/how-to-use-snov-io-api/
- group: operate
  title: ''
  type: Support
  url: https://snov.io/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://snov.io/knowledgebase/
- group: start
  title: ''
  type: SignUp
  url: https://app.snov.io/register
- group: start
  title: ''
  type: Login
  url: https://app.snov.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snov.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snov.io/privacy-policy
- group: auth
  title: ''
  type: SecurityCenter
  url: https://snov.io/security-center
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://snov.io/release-notes
created: '2026-06-12'
description: Snov.io is a sales automation and lead generation platform serving over 300,000 companies across 180+ countries. The platform provides a REST API enabling developers to programmatically access email finding, domain search, email verification, drip campaign management, and LinkedIn prospect automation. Authentication uses OAuth 2.0 client credentials to obtain short-lived Bearer tokens, and all API operations consume credits from the account balance. The API covers the full sales outreach lifecycle from prospect discovery and contact enrichment through multi-channel campaign execution and CRM pipeline management. Snov.io also operates a first-party remote Model Context Protocol server at https://mcp.snov.io/mcp, documented as exposing more than 100 actions to AI assistants and gated by a separate OAuth authorization code flow with PKCE and dynamic client registration. The two surfaces are disjoint — campaigns, warm-up, sender accounts and webhooks are REST-only, while Sales CRM
  writes and all LinkedIn outreach actions are reachable only over MCP.
finops:
- name: Snov Io Finops
  service_category: ''
  slug: snov-io-finops
graphqls:
- description: Snov.io is a sales automation and lead generation platform serving over 300,000 companies across 180+ countries. Its REST API covers the full outreach lifecycle — prospect discovery, email finding, em
  name: Snov.io GraphQL Schema
  slug: snov-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snov-io.png
jsonld:
- class_count: 11
  name: Snov Io Context
  property_count: 28
  slug: snov-io-context
layout: provider
mcp_servers:
- description: Snov.io ships a first-party REMOTE Model Context Protocol server at https://mcp.snov.io/mcp. It is a hosted HTTP endpoint an MCP client POSTs to directly — there is no npx package, no stdio binary and
  name: Snov.io Outreach MCP Server
  slug: snov-io-outreach-mcp-server
modified: '2026-08-13'
name: Snov.io
nav: Providers
network: true
overview: 'Snov.io publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, CRM Pipeline API, and 14 more. Tagged areas include Sales Automation, Email Finder, Email Verification, Lead Generation, and Drip Campaigns.


  The Snov.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Snov.io''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 37 more developer resources.'
plans:
- name: Snov Io Plans Pricing
  plan_count: 7
  slug: snov-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Snov Io Rate Limits
  slug: snov-io-rate-limits
scopes:
- name: Snov Io Scopes
  scope_count: 1
  slug: snov-io-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 67.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 75.0
    catalog_earned_first_party: 24.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 69.3
    developer_ergonomics: 58.9
    discoverability: 68.3
    operational_transparency: 57.9
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/screenshots/snov-io-2026-06-20T194107.png
security:
- kind: authentication
  name: Snov Io Authentication
  slug: snov-io-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Snov Io Domain Security
  slug: snov-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Snov Io Trust Center
  slug: snov-io-trust-center
  summary_line: GDPR, LOA (Letter of Authorization), CCPA / Do Not Sell My Personal Information
slug: snov-io
tags:
- Sales Automation
- Email Finder
- Email Verification
- Lead Generation
- Drip Campaigns
- CRM
- LinkedIn Automation
- Prospect Management
- Data Enrichment
- Cold Email
website: https://snov.io/
---
