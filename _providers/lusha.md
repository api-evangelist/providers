---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · API keys gated to Scale plan
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.1
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Lusha Agentic Access
  operation_count: 58
  slug: lusha-agentic-access
  summary_line: 58 operations · 38 acting
api_count: 2
apis:
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Find contacts or companies from known identifiers — contact id, LinkedIn URL, email or name + company; company id, name or domain — and return a non-PII preview with `has` and `canReveal` fields descr
  name: Lusha Search API
  phrasing_intents:
  - id: searchContacts
    intent: Preview contacts by identifier
    question: How do I check whether Lusha knows a person before spending credits?
  - id: searchCompanies
    intent: Preview companies by identifier
    question: How do I check what data exists for a company before enriching it?
  phrasing_ops: 2
  slug: lusha-search-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: 'Reveal full contact and company profiles by Lusha id, with an explicit `reveal` list controlling which fields are unlocked and charged, and optional waterfall fall-through to enabled third-party data '
  name: Lusha Enrich API
  phrasing_intents:
  - id: enrichContacts
    intent: Reveal emails and phones for found contacts
    question: How do I unlock the email and phone number for contacts I already searched?
  - id: enrichCompanies
    intent: Reveal full firmographics for found companies
    question: How do I get revenue, funding and technologies for companies I already searched?
  phrasing_ops: 2
  slug: lusha-enrich-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Resolve an identifier and return the fully revealed contact or company record in a single call, collapsing the two-phase search-then-enrich pattern where the caller has already decided to spend credit
  name: Lusha Search & Enrich API
  phrasing_intents:
  - id: searchAndEnrichContacts
    intent: Find and reveal contacts in one call
    question: Can I find a person and get their email and phone in a single request?
  - id: searchAndEnrichCompanies
    intent: Find and reveal companies in one call
    question: Can I look up a company and get its full firmographics in a single call?
  phrasing_ops: 2
  slug: lusha-search-enrich-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Filter-based search across Lusha's contact and company database — job title, seniority, department, location, company size, revenue, industry, technology and intent — with paged results and a dedupe s
  name: Lusha Prospecting API
  phrasing_intents:
  - id: prospectingContacts
    intent: Find contacts matching my ideal customer profile
    question: How do I find VPs of sales in the US at mid-size software companies?
  - id: prospectingCompanies
    intent: Find companies matching my target market
    question: How do I find companies of a certain size and industry that use a given technology?
  phrasing_ops: 2
  slug: lusha-prospecting-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: AI-powered similarity search that expands a seed list of contacts or companies into comparable profiles, with exclusion lists, a dedupe session id and optional persistence into a Lusha table.
  name: Lusha Lookalikes API
  phrasing_intents:
  - id: getContactLookalikes
    intent: Find people similar to seed contacts
    question: How do I find more people like my best customers' buyers?
  - id: getCompanyLookalikes
    intent: Find companies similar to seed accounts
    question: How do I find more companies like my best customers?
  - id: postV3LookalikeContacts
    intent: Find lookalike contacts (older endpoint)
    question: Is there an older lookalike contacts endpoint without table saving?
  - id: postV3LookalikeCompanies
    intent: Find lookalike companies (older endpoint)
    question: Is there an older lookalike companies endpoint without table saving?
  phrasing_ops: 4
  slug: lusha-lookalike-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Persona classification over a fixed set of up to 25 named accounts — labels each returned contact decision_maker, potential_champion or end_user with a relevance score. Released 2026-08-12 as the repl
  name: Lusha Buying Group API
  phrasing_intents:
  - id: getContactsBuyingGroup
    intent: Find the buying group at target companies
    question: Who are the decision makers and champions at a company I want to sell to?
  phrasing_ops: 1
  slug: lusha-buying-group-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Real-world activity data for contacts and companies — promotions and job changes on the contact side; headcount movement, hiring surges, web traffic, IT spend, news classes and LinkedIn activity inten
  name: Lusha Signals API
  phrasing_intents:
  - id: getContactSignals
    intent: Get job changes and promotions for contacts
    question: Which of my contacts recently got promoted or changed companies?
  - id: getCompanySignals
    intent: Get hiring, news and growth signals for companies
    question: Which of my target accounts are hiring or in the news?
  - id: getContactSignalTypes
    intent: List contact signal types
    question: What kinds of signals does Lusha track for people?
  - id: getCompanySignalTypes
    intent: List company signal types
    question: What kinds of signals are tracked for companies?
  - id: getCompanySignalFilters
    intent: List company signal filter types
    question: What filters can I apply to company signals, like news event type?
  - id: getCompanySignalFilterValues
    intent: Get values for one company signal filter
    question: What news event types can I filter company signals by?
  - id: getCompanySignalScores
    intent: Score companies by buying signal activity
    question: Which of my accounts show the most active buying signals?
  - id: getContactSignalScores
    intent: Score contacts by buying signal activity
    question: Which of my contacts have the strongest buying signals right now?
  phrasing_ops: 13
  slug: lusha-signals-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Companies ranked by website-visit signals for domains you track, filtered by score band, visitor country, session counts, unique visitors, high-intent pageviews and recency.
  name: Lusha Website Visitors API
  phrasing_intents:
  - id: getWebsiteVisits
    intent: See which companies visited my website
    question: Which companies have been visiting my website?
  phrasing_ops: 1
  slug: lusha-website-visits-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Filter discovery for prospecting — enumerates the available filter types and the valid values for each, so callers never guess industry labels, seniority ids or technology names. Charges no credits.
  name: Lusha Filters API
  phrasing_intents:
  - id: getContactFilterTypes
    intent: List contact prospecting filter types
    question: What kinds of filters can I use when prospecting for contacts?
  - id: getContactFilterValues
    intent: Get valid values for one contact filter
    question: What values are valid for the contact seniority or departments filter?
  - id: getCompanyFilterTypes
    intent: List company prospecting filter types
    question: What kinds of filters can I use when prospecting for companies?
  - id: getCompanyFilterValues
    intent: Get valid values for one company filter
    question: What values are valid for the company revenue or size filter?
  phrasing_ops: 4
  slug: lusha-filters-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Persist, organise and enrich contacts in reusable tables with dynamic columns — create, list, read, update, delete tables; add and remove up to 500 entity ids per call; run enrichment columns over a s
  name: Lusha Contacts Tables API
  phrasing_intents:
  - id: createContactsTable
    intent: Create a contacts table
    question: How do I start a new people list table in Lusha?
  - id: listContactsTables
    intent: List contacts tables
    question: Which contacts tables are mine or shared with my account?
  - id: getContactsTable
    intent: Get a contacts table and its status
    question: Has my contacts table finished processing yet?
  - id: updateContactsTable
    intent: Rename, archive or reassign a contacts table
    question: How do I rename a contacts table?
  - id: deleteContactsTable
    intent: Delete a contacts table
    question: How do I permanently delete a contacts table?
  - id: getContactsTableEntities
    intent: Read the rows of a contacts table
    question: How do I export the people and column values from a contacts table?
  - id: addContactsTableEntities
    intent: Add contacts to a table
    question: How do I add more people to an existing contacts table?
  - id: removeContactsTableEntities
    intent: Remove contacts from a table
    question: How do I take specific people out of a contacts table?
  phrasing_ops: 11
  slug: lusha-contacts-tables-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: The company-side twin of Contacts Tables — persist and enrich company working sets in tables with dynamic columns, capped at 50,000 entities per table and 500 tables per account.
  name: Lusha Companies Tables API
  phrasing_intents:
  - id: createCompaniesTable
    intent: Create a companies table
    question: How do I start a new account list table in Lusha?
  - id: listCompaniesTables
    intent: List companies tables
    question: Which companies tables do I own or have shared with me?
  - id: getCompaniesTable
    intent: Get a companies table and its status
    question: Is my companies table still processing?
  - id: updateCompaniesTable
    intent: Rename, archive or reassign a companies table
    question: How do I rename a companies table?
  - id: deleteCompaniesTable
    intent: Delete a companies table
    question: How do I permanently delete a companies table?
  - id: getCompaniesTableEntities
    intent: Read the rows of a companies table
    question: How do I export the rows and column values from a companies table?
  - id: addCompaniesTableEntities
    intent: Add companies to a table
    question: How do I add more companies to an existing table?
  - id: removeCompaniesTableEntities
    intent: Remove companies from a table
    question: How do I take specific companies out of a table without deleting the table?
  phrasing_ops: 11
  slug: lusha-companies-tables-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Subscription management for real-time signal callbacks — bulk create and delete up to 25 items per request, account-level HMAC-SHA256 secret with rotation, delivery test, contact opt-out notifications
  name: Lusha Webhooks API
  phrasing_intents:
  - id: createSubscription
    intent: Subscribe a webhook to signal events
    question: How do I get real-time signal notifications sent to my server?
  - id: listSubscriptions
    intent: List webhook subscriptions
    question: Which webhook subscriptions do I have set up?
  - id: getSubscriptionById
    intent: Get one webhook subscription
    question: How do I see the settings of one webhook subscription?
  - id: updateSubscription
    intent: Change or reactivate a webhook subscription
    question: How do I change the URL a webhook subscription posts to?
  - id: testSubscription
    intent: Send a test event to a webhook
    question: How do I check my webhook endpoint works before going live?
  - id: deleteSubscriptions
    intent: Delete webhook subscriptions
    question: How do I delete several webhook subscriptions at once?
  - id: getAuditLogs
    intent: View webhook delivery logs
    question: Why did my webhook deliveries fail?
  - id: getAuditLogStats
    intent: Get webhook delivery statistics
    question: What's my webhook delivery success rate?
  phrasing_ops: 11
  slug: lusha-webhooks-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Credit balance, plan information, per-action credit pricing and the live rate-limit tiers for the minute, hourly and daily windows.
  name: Lusha Account API
  phrasing_intents:
  - id: getAccountUsage
    intent: Check credits, rate limits and plan
    question: How many Lusha credits do I have left this billing cycle?
  phrasing_ops: 1
  slug: lusha-account-api
- description: 'First-party hosted Model Context Protocol server exposing 22 Lusha tools over streamable HTTP. Authenticates with OAuth 2.1 (scope `mcp`, PKCE S256, dynamic client registration at auth.lusha.com) for '
  name: Lusha MCP Server
  slug: mcp
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: 'Manage your account and monitor usage. Use this endpoint to: - Monitor credit usage - Understand consumption patterns - Align API usage with plan limits - Support governance and production operations '
  name: Lusha Account Management API
  phrasing_intents:
  - id: getAccountUsageStats
    intent: Get API credit usage statistics
    question: How many API credits have I used and how many remain?
  phrasing_ops: 1
  slug: lusha-account-management-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Available filters for company searches
  name: Lusha Company Filters API
  phrasing_intents:
  - id: searchCompanyNames
    intent: Look up company names for filtering
    question: How do I find the exact company name to use in a prospecting filter?
  - id: getCompanyIndustries
    intent: List industries for company filters
    question: What industries can I filter companies by?
  - id: getCompanySizes
    intent: List company size ranges
    question: What employee size ranges can I filter companies by?
  - id: getCompanyRevenues
    intent: List company revenue ranges
    question: What revenue ranges can I filter companies by?
  - id: searchCompanyLocations
    intent: Look up company locations for filtering
    question: How do I find a company headquarters location to filter on?
  - id: getCompanySicCodes
    intent: List SIC codes for company filters
    question: Which SIC codes can I filter companies by?
  - id: getCompanyNaicsCodes
    intent: List NAICS codes for company filters
    question: Which NAICS codes can I filter companies by?
  - id: getCompanyIntentTopics
    intent: List buyer intent topics
    question: What buyer intent topics can I filter companies by?
  phrasing_ops: 9
  slug: lusha-company-filters-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: Available filters for contact searches
  name: Lusha Contact Filters API
  phrasing_intents:
  - id: getContactDepartments
    intent: List departments for contact filters
    question: What departments can I filter contacts by?
  - id: getContactSeniority
    intent: List seniority levels for contact filters
    question: What seniority levels can I filter contacts by?
  - id: getContactDataPoints
    intent: List contact data points to filter on
    question: Can I filter to contacts that have a phone number or email on file?
  - id: getContactCountries
    intent: List countries for contact filters
    question: Which countries can I filter contacts by?
  - id: searchContactLocations
    intent: Look up contact locations for filtering
    question: How do I find a city or state to filter contacts by?
  phrasing_ops: 5
  slug: lusha-contact-filters-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: '**What is enrichment?** Enrichment is the process of adding missing or updated data to existing contact or company records. Use enrichment to: - Complete CRM records - Improve outbound accuracy and de'
  name: Lusha Enrichment API
  phrasing_intents:
  - id: searchSingleContact
    intent: Find and enrich one person
    question: How do I get the email and phone for one person from their LinkedIn URL?
  - id: searchMultipleContacts
    intent: Enrich a batch of people at once
    question: How do I enrich a whole list of contacts in one request?
  - id: searchSingleCompanyV2
    intent: Look up one company
    question: How do I get company details from a website domain?
  - id: searchMultipleCompaniesV2
    intent: Look up a batch of companies at once
    question: How do I enrich a list of company domains in one call?
  phrasing_ops: 4
  slug: lusha-enrichment-api
- baseURL: https://api.lusha.com
  baseurl_source: declared
  description: With Lusha's Prospecting API, you can query Lusha's extensive database based on specific criteria (such as job title, seniority, location, and more) to retrieve detailed contact and company informatio
  name: Lusha Prospecting - Search & Enrich API
  phrasing_intents:
  - id: searchProspectingContacts
    intent: Search contacts by prospecting filters
    question: How do I search for contacts with filters in the older prospecting flow?
  - id: enrichProspectingContacts
    intent: Enrich contacts from a prospecting search
    question: How do I reveal emails for contacts returned by a prospecting search?
  - id: searchProspectingCompanies
    intent: Search companies by prospecting filters
    question: Which accounts match my industry and size filters in step two of prospecting?
  - id: enrichProspectingCompanies
    intent: Enrich companies from a prospecting search
    question: How do I get full details for companies returned by a prospecting search?
  phrasing_ops: 4
  slug: lusha-prospecting-search-enrich-api
artifact_total: 44
asyncapis:
- description: ''
  name: Lusha Webhooks
  slug: lusha-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lusha API Documentation Account API
  slug: open-lusha-account-api
- collection_type: open
  name: Lusha API Documentation Buying Group API
  slug: open-lusha-buying-group-api
- collection_type: open
  name: Lusha API Documentation Companies Tables API
  slug: open-lusha-companies-tables-api
- collection_type: open
  name: Lusha API Documentation Contacts Tables API
  slug: open-lusha-contacts-tables-api
- collection_type: open
  name: Lusha API Documentation Enrich API
  slug: open-lusha-enrich-api
- collection_type: open
  name: Lusha API Documentation Filters API
  slug: open-lusha-filters-api
- collection_type: open
  name: Lusha API Documentation Lookalikes API
  slug: open-lusha-lookalikes-api
- collection_type: open
  name: Lusha API Documentation Prospecting API
  slug: open-lusha-prospecting-api
- collection_type: open
  name: Lusha API Documentation Search API
  slug: open-lusha-search-api
- collection_type: open
  name: Lusha API Documentation Search & Enrich API
  slug: open-lusha-search-enrich-api
- collection_type: open
  name: Lusha API Documentation Signals API
  slug: open-lusha-signals-api
- collection_type: open
  name: Lusha API Documentation Webhooks API
  slug: open-lusha-webhooks-api
- collection_type: open
  name: Lusha API Documentation Website Visits API
  slug: open-lusha-website-visits-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/capabilities/lusha-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lusha-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.lusha.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lusha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lusha.com/apis/openapi
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lusha.com/apis/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lusha.com/guides/advanced-topics/new-getting-started
- group: operate
  title: ''
  type: Support
  url: https://info.lusha.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lusha.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lusha-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lushadata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lusha.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://dashboard.lusha.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lusha.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lusha.com/legal/privacy-notice/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lushateam/workspace/lusha-s-api/collection/28683568-fc849873-9ae1-47dd-8159-0d4deda04750
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.lusha.com/_spec/apis/@v3/openapi.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/mcp/lusha-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lusha-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/mcp/lusha-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lusha-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/agentic-access/lusha-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lusha-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/authentication/lusha-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lusha-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/scopes/lusha-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lusha-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/conventions/lusha-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lusha-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/errors/lusha-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lusha-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/data-model/lusha-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lusha-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/lifecycle/lusha-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lusha-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lusha.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.lusha.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/changelog/lusha-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lusha-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lusha.com/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/asyncapi/lusha-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lusha-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/conformance/lusha-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lusha-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lusha.com/trust-center
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/security/lusha-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lusha-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lusha.com/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/well-known/lusha-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lusha-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/security/lusha-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lusha-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/security/lusha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lusha-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/well-known/lusha-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lusha-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/packages/lusha-packages.yml
  title: ''
  type: Packages
  url: packages/lusha-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/sandbox/lusha-sandbox.yml
  title: ''
  type: Console
  url: sandbox/lusha-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/plans/lusha-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lusha-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/rate-limits/lusha-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lusha-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/finops/lusha-finops.yml
  title: ''
  type: FinOps
  url: finops/lusha-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/llms/lusha-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lusha-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.lusha.com/llms.txt
created: '2026-05-08'
description: Lusha is a B2B sales-intelligence platform that sells verified contact and company data, buying signals and AI recommendations to revenue teams. Its v3 REST API at api.lusha.com exposes 58 operations across thirteen resource families — Search, Enrich, Search & Enrich, Prospecting, Lookalikes, Buying Group, Contacts Tables, Companies Tables, Signals, Website Visits, Filters, Webhooks and Account — behind a single `api_key` header credential, on a search-then-enrich pattern where previews are free of PII and reveals spend credits. Lusha also ships a first-party hosted MCP server at mcp.lusha.com with 22 tools, OAuth 2.1 discovery and official Claude, ChatGPT and Codex connectors, plus HMAC-signed webhooks for real-time signal delivery.
finops:
- name: Lusha Finops
  service_category: Sales Intelligence
  slug: lusha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lusha.png
layout: provider
mcp_servers:
- description: Lusha ships a first-party hosted MCP server at https://mcp.lusha.com plus a local stdio package on npm (@lusha-org/mcp) and a Gemini CLI extension. The hosted endpoint accepts either an OAuth authoriz
  name: Lusha MCP Server
  slug: lusha
modified: '2026-08-13'
name: Lusha
nav: Providers
network: true
overview: 'Lusha publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Search API, Enrich API, Search & Enrich API, and 16 more. Tagged areas include Sales Intelligence, B2B, Enrichment, Contact Data, and Prospecting.


  The Lusha catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lusha''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 39 more developer resources.'
plans:
- name: Lusha Plans Pricing
  plan_count: 4
  slug: lusha-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 13
  name: Lusha Rate Limits
  slug: lusha-rate-limits
scopes:
- name: Lusha Scopes
  scope_count: 1
  slug: lusha-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 72.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 62.0
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 86.8
  previous_composite: 72.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
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
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/lusha/refs/heads/main/screenshots/lusha-2026-06-20T184813.png
security:
- kind: authentication
  name: Lusha Authentication
  slug: lusha-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Lusha Domain Security
  slug: lusha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lusha Vulnerability Disclosure
  slug: lusha-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lusha Trust Center
  slug: lusha-trust-center
  summary_line: SOC 2 Type II
slug: lusha
tags:
- Sales Intelligence
- B2B
- Enrichment
- Contact Data
- Prospecting
- Intents
- Signals
- Lookalikes
- Webhook
- MCP
website: https://www.lusha.com/
---
