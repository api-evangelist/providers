---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 102
  human_in_the_loop: 0
  name: Explorium Agentic Access
  operation_count: 127
  slug: explorium-agentic-access
  summary_line: 127 operations · 102 acting
api_count: 2
apis:
- description: 'Native remote Model Context Protocol server exposing the AgentSource data as 11 agent tools - match-business, fetch-businesses, fetch-businesses- statistics, fetch-businesses-events, enrich-business, '
  name: Explorium AgentSource MCP Server
  slug: explorium-agentsource-mcp-server
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, stat, autocomplete, and event/enrollment operations over the Explorium business dataset (v1).
  name: Explorium Businesses API
  phrasing_intents:
  - id: match_businesses
    intent: Match company names or domains to business IDs
    question: How do I turn a list of company names and websites into business IDs?
  - id: fetch_businesses
    intent: Search businesses by country, size and revenue
    question: Can I find companies filtered by country, employee count and revenue?
  - id: fetch_businesses_events
    intent: Fetch events for businesses
    question: What recent events, like hiring or funding news, happened at these companies?
  - id: businesses_autocomplete
    intent: Autocomplete business filter values
    question: What valid values can I use for a business search field, like industry?
  - id: fetch_stats
    intent: Count businesses matching filters
    question: How many companies match my filters before I pull them?
  - id: get_businesses_enrollments
    intent: List my business event enrollments
    question: Which companies am I currently monitoring for events?
  - id: add_businesses_enrollments
    intent: Enroll businesses for event monitoring
    question: How do I start monitoring a set of companies for events?
  - id: delete_businesses_enrollments
    intent: Remove a business event enrollment
    question: How do I stop monitoring companies for events?
  phrasing_ops: 9
  slug: explorium-businesses-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Inspect the shared credit pool that meters all Explorium API usage, including the credit menu and consumption aggregation (v1).
  name: Explorium Credits API
  phrasing_intents:
  - id: get_credits_menu_partner_id
    intent: Get the credits price menu for a partner
    question: How many credits does each enrichment cost for my partner account?
  - id: get_active_credits_summary
    intent: Show my active credits balance
    question: How many credits do I have left?
  - id: get_credit_aggregation
    intent: Report credit usage over a date range
    question: How many credits did I spend between two dates?
  phrasing_ops: 3
  slug: explorium-credits-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, stat, autocomplete, and event/enrollment operations over the Explorium prospect dataset (v1).
  name: Explorium Prospects API
  phrasing_intents:
  - id: match_prospects
    intent: Match people to prospect IDs
    question: How do I turn names, emails or LinkedIn URLs into prospect IDs?
  - id: fetch_prospects
    intent: Search prospects by role, seniority and company
    question: Can I find people by job title, seniority and the company they work for?
  - id: prospect_fetch_stats
    intent: Count prospects matching filters
    question: How many people match my persona filters before I export them?
  - id: fetch_prospects_events
    intent: Fetch events for prospects
    question: What job changes or other events happened for these people recently?
  - id: prospects_autocomplete
    intent: Autocomplete prospect filter values
    question: What values can I use for a people search field like job title?
  - id: get_prospects_enrollments
    intent: List my prospect event enrollments
    question: Which people am I currently monitoring for events?
  - id: add_prospects_enrollments
    intent: Enroll prospects for event monitoring
    question: How do I start tracking a set of people for job changes and other events?
  - id: delete_prospects_enrollments
    intent: Remove a prospect event enrollment
    question: How do I stop tracking people for events?
  phrasing_ops: 9
  slug: explorium-prospects-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Register, retrieve, delete, and connectivity-test the webhook endpoints that receive Explorium business and prospect event notifications (v1).
  name: Explorium Webhooks API
  phrasing_intents:
  - id: add_webhook
    intent: Register a webhook for event enrollments
    question: How do I get enrollment events pushed to my own URL?
  - id: get_webhook
    intent: Get a partner's webhook
    question: Which URL are my event notifications being sent to?
  - id: delete_webhook
    intent: Delete a partner's webhook
    question: How do I stop event notifications going to my webhook?
  - id: check_webhook_connectivity
    intent: Test webhook connectivity
    question: Can I verify my webhook endpoint is reachable before events start?
  phrasing_ops: 4
  slug: explorium-webhooks-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Submit any v2 company or people enrichment — plus AI research — as an asynchronous job over an uploaded entity-ID dataset.
  name: Explorium Async Enrichment Jobs API
  phrasing_intents:
  - id: v2_businesses_bombora_intent_job
    intent: Start a background job for Bombora intent on a list
    question: Can I pull Bombora intent signals for an entire uploaded company list in the background?
  - id: v2_businesses_company_hierarchies_job
    intent: Start a background job for company hierarchies
    question: How do I map parent companies and subsidiaries for a whole list of accounts at once?
  - id: v2_businesses_company_ratings_by_employees_job
    intent: Start a background job for employee ratings
    question: Can I get employee review ratings for hundreds of companies without waiting on each one?
  - id: v2_businesses_company_website_keywords_job
    intent: Start a background website keyword scan on a list
    question: Can I check which companies in a large list mention certain keywords on their websites?
  - id: v2_businesses_financial_indicators_job
    intent: Start a background job for financial indicators
    question: How can I get financial metrics like revenue for a big account list asynchronously?
  - id: v2_businesses_firmographics_job
    intent: Start a background firmographics job for a list
    question: Can I enrich industry, size and location for an uploaded company list in the background?
  - id: v2_businesses_funding_and_acquisition_job
    intent: Start a background job for funding and M&A data
    question: Which companies on my list raised money or were acquired, using a queued job?
  - id: v2_businesses_linkedin_posts_job
    intent: Start a background job for company LinkedIn posts
    question: Can I collect recent LinkedIn posts from every company in a list as a background job?
  phrasing_ops: 22
  slug: explorium-asyncenrichmentjobs-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: List, poll, and cancel the asynchronous enrichment jobs that back batch runs of up to 10,000 records (v2).
  name: Explorium Async Jobs API
  phrasing_intents:
  - id: v2_jobs
    intent: List my async enrichment jobs
    question: Which enrichment jobs have I started, and which are still running?
  - id: v2_job_status
    intent: Check the status of an async job
    question: How do I know when a background enrichment job has finished?
  - id: v2_job_cancel
    intent: Cancel an async job
    question: Can I stop a background enrichment job that's still running?
  phrasing_ops: 3
  slug: explorium-asyncjobs-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Bulk (multi-record) versions of every v1 company enrichment, processing up to 50 business IDs per request.
  name: Explorium Bulk Business Enrichments API
  phrasing_intents:
  - id: businesses_bombora_intent_bulk_enrich
    intent: Get Bombora intent for many businesses
    question: Can I fetch Bombora intent signals for a batch of company IDs in one request?
  - id: businesses_company_hierarchies_bulk_enrich
    intent: Get corporate hierarchies for many businesses
    question: How do I see the parent companies and subsidiaries of several businesses at once?
  - id: businesses_company_ratings_by_employees_bulk_enrich
    intent: Get employee ratings for many businesses
    question: What do employees rate these companies, looked up together?
  - id: businesses_company_website_keywords_bulk_enrich
    intent: Search many company websites for keywords
    question: Do any of these companies mention specific keywords on their websites?
  - id: businesses_financial_indicators_bulk_enrich
    intent: Get financial indicators for many businesses
    question: Can I get financial metrics for a batch of companies in a single request?
  - id: businesses_firmographics_bulk_enrich
    intent: Get firmographics for many businesses
    question: How do I get industry, size and location for several companies at once?
  - id: businesses_funding_and_acquisition_bulk_enrich
    intent: Get funding and acquisitions for many businesses
    question: Which of these companies have raised funding or made acquisitions?
  - id: businesses_linkedin_posts_bulk_enrich
    intent: Get LinkedIn posts for many businesses
    question: Can I fetch recent company LinkedIn posts for a batch of businesses?
  phrasing_ops: 17
  slug: explorium-bulkbusinessenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: 'Single-record company enrichments (v1): firmographics, technographics, webstack, website traffic and changes, financial indicators, funding and acquisition, workforce trends, company hierarchies, rati'
  name: Explorium Business Enrichments API
  phrasing_intents:
  - id: businesses_bombora_intent_enrich
    intent: Get Bombora intent for one business
    question: What topics is this company showing Bombora buying intent for?
  - id: businesses_company_hierarchies_enrich
    intent: Get the corporate hierarchy of a business
    question: Who is the parent company of this business, and what subsidiaries does it have?
  - id: businesses_company_ratings_by_employees_enrich
    intent: Get employee ratings for a business
    question: How do employees rate working at this company?
  - id: businesses_company_website_keywords_enrich
    intent: Search a company's website for keywords
    question: Does this company mention particular keywords on its website?
  - id: businesses_financial_indicators_enrich
    intent: Get financial indicators for a business
    question: What are the key financial metrics for this company?
  - id: businesses_firmographics_enrich
    intent: Get firmographics for a business
    question: What industry is this company in, how big is it and where is it based?
  - id: businesses_funding_and_acquisition_enrich
    intent: Get funding and acquisitions for a business
    question: How much funding has this company raised, and has it acquired anyone?
  - id: businesses_linkedin_posts_enrich
    intent: Get LinkedIn posts for a business
    question: What has this company posted on LinkedIn recently?
  phrasing_ops: 17
  slug: explorium-businessenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Run a customer-specific custom enrichment, single-record or in bulk, by custom enrichment ID.
  name: Explorium Custom Enrichments API
  phrasing_intents:
  - id: enrich_with_custom_enrichment
    intent: Run a custom enrichment on one business
    question: Can I apply my own custom enrichment to a single company?
  - id: bulk_enrich_with_custom_enrichment
    intent: Run a custom enrichment on many businesses
    question: Can I run a custom enrichment across a batch of companies in one request?
  phrasing_ops: 2
  slug: explorium-customenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Upload an entity-ID dataset that asynchronous v2 enrichment jobs run against.
  name: Explorium Entity ID Datasets API
  phrasing_intents:
  - id: v2_entity_id_lists_upload
    intent: Upload a file of entity IDs as a dataset
    question: How do I upload a list of business or prospect IDs to use in async jobs?
  phrasing_ops: 1
  slug: explorium-entityiddatasets-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Bulk (multi-record) versions of the v1 people enrichments, processing up to 50 prospect IDs per request.
  name: Explorium Prospects Bulk Enrichments API
  phrasing_intents:
  - id: prospects_contacts_information_bulk_enrich
    intent: Get contact details for many prospects
    question: Can I get emails and phone numbers for a batch of people at once?
  - id: prospects_linkedin_posts_bulk_enrich
    intent: Get LinkedIn posts for many prospects
    question: What have these people posted on LinkedIn recently?
  - id: prospects_profiles_bulk_enrich
    intent: Get professional profiles for many prospects
    question: Can I enrich job titles and work history for several people in one request?
  phrasing_ops: 3
  slug: explorium-prospectsbulkenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: 'Single-record people enrichments (v1): contact information, professional profiles, and LinkedIn posts for a matched prospect.'
  name: Explorium Prospects Enrichments API
  phrasing_intents:
  - id: prospects_contacts_information_enrich
    intent: Get contact details for a prospect
    question: What's this person's email address and phone number?
  - id: prospects_linkedin_posts_enrich
    intent: Get LinkedIn posts for a prospect
    question: What has this person been posting on LinkedIn?
  - id: prospects_profiles_enrich
    intent: Get a prospect's professional profile
    question: What is this person's current job title and work history?
  phrasing_ops: 3
  slug: explorium-prospectsenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Resolve free-text input to the standardized filter values the v2 search API accepts.
  name: Explorium V2 Autocomplete API
  phrasing_intents:
  - id: v2_autocomplete
    intent: Autocomplete search filter values
    question: What values are valid for a search field like industry or job title?
  phrasing_ops: 1
  slug: explorium-v2autocomplete-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Synchronous v2 company enrichments — the same seventeen attribute families as v1, on the unified v2 request shape.
  name: Explorium V2 Business Enrichments API
  phrasing_intents:
  - id: v2_businesses_bombora_intent_enrich
    intent: Get Bombora intent for businesses (v2)
    question: Which of my accounts are showing Bombora intent surges right now?
  - id: v2_businesses_company_hierarchies_enrich
    intent: Get corporate hierarchies for businesses (v2)
    question: Who owns these companies, and what subsidiaries sit under them?
  - id: v2_businesses_company_ratings_by_employees_enrich
    intent: Get employee ratings for businesses (v2)
    question: How do employees rate working at these companies?
  - id: v2_businesses_company_website_keywords_enrich
    intent: Search company websites for keywords (v2)
    question: Do these companies mention my keywords anywhere on their websites?
  - id: v2_businesses_financial_indicators_enrich
    intent: Get financial indicators for businesses (v2)
    question: What are the financial metrics for these companies?
  - id: v2_businesses_firmographics_enrich
    intent: Get firmographics for businesses (v2)
    question: What industry, headcount and location do these companies have?
  - id: v2_businesses_funding_and_acquisition_enrich
    intent: Get funding and acquisitions for businesses (v2)
    question: Have these companies raised money or bought other companies?
  - id: v2_businesses_linkedin_posts_enrich
    intent: Get LinkedIn posts for businesses (v2)
    question: What are these companies posting on their LinkedIn pages?
  phrasing_ops: 17
  slug: explorium-v2businessenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, and stat over the company dataset on the v2 (beta) surface, where bulk and single input share one endpoint.
  name: Explorium V2 Businesses API
  phrasing_intents:
  - id: v2_businesses_match
    intent: Match companies to business IDs (v2)
    question: How do I resolve company names and domains to business IDs in v2?
  - id: v2_businesses_fetch
    intent: Search businesses by filters (v2)
    question: Which companies match my target country, size and industry?
  - id: v2_businesses_stats
    intent: Count businesses matching filters (v2)
    question: How many companies fall into my target segment?
  phrasing_ops: 3
  slug: explorium-v2businesses-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Credit balance and consumption aggregation on the v2 (beta) surface.
  name: Explorium V2 Credits API
  phrasing_intents:
  - id: v2_credits_get
    intent: Show my active credits balance (v2)
    question: How many credits remain on my account?
  - id: v2_credits_aggregation
    intent: Report credit usage over a date range (v2)
    question: How many credits did I use over a given period?
  phrasing_ops: 2
  slug: explorium-v2credits-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: 'Synchronous v2 people enrichments: contact information, professional profiles, and LinkedIn posts.'
  name: Explorium V2 Prospect Enrichments API
  phrasing_intents:
  - id: v2_prospects_contact_information_enrich
    intent: Get contact details for prospects (v2)
    question: What are the emails and phone numbers for these people?
  - id: v2_prospects_linkedin_posts_enrich
    intent: Get LinkedIn posts for prospects (v2)
    question: What have these people shared on LinkedIn recently?
  - id: v2_prospects_profiles_enrich
    intent: Get professional profiles for prospects (v2)
    question: What are these people's job titles and career histories?
  phrasing_ops: 3
  slug: explorium-v2prospectenrichments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Match, fetch, and stat over the people dataset on the v2 (beta) surface.
  name: Explorium V2 Prospects API
  phrasing_intents:
  - id: v2_prospects_match
    intent: Match people to prospect IDs (v2)
    question: How do I resolve names, emails or LinkedIn URLs to prospect IDs in v2?
  - id: v2_prospects_fetch
    intent: Search prospects by filters (v2)
    question: Which people match my target job titles and seniority?
  - id: v2_prospects_stats
    intent: Count prospects matching filters (v2)
    question: How many people match my persona filters?
  phrasing_ops: 3
  slug: explorium-v2prospects-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Run a custom, AI-powered research task over a list of businesses or prospects using a natural-language query or prompt template, grounded in real-time web data (beta).
  name: Explorium V2 Research API
  phrasing_intents:
  - id: v2_businesses_research_enrich
    intent: Research companies with a custom question
    question: Can I ask a custom research question about specific companies and get answers back?
  - id: v2_prospects_research_enrich
    intent: Research people with a custom question
    question: Can I ask a custom research question about specific people?
  phrasing_ops: 2
  slug: explorium-v2research-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: Report the deployed version of the Explorium AgentSource service.
  name: Explorium Version API
  phrasing_intents:
  - id: version
    intent: Get the API version
    question: Which version of the API is currently deployed?
  phrasing_ops: 1
  slug: explorium-version-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: The V2Enrollments API from Explorium — 4 operation(s) for v2enrollments.
  name: Explorium V2Enrollments API
  slug: explorium-v2enrollments-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: The V2Webhooks API from Explorium — 4 operation(s) for v2webhooks.
  name: Explorium V2Webhooks API
  slug: explorium-v2webhooks-api
- baseURL: https://api.explorium.ai
  baseurl_source: declared
  description: The Health Check API from Explorium — 2 operation(s) for health check.
  name: Explorium Health Check API
  phrasing_intents:
  - id: healthcheck
    intent: Check that the service is up
    question: Is the enrichment service up and responding?
  - id: healthcheck_bytes
    intent: Run a healthcheck returning a sized payload
    question: Can I test the API's response with a payload of a specific size?
  phrasing_ops: 2
  slug: explorium-health-check-api
artifact_total: 50
asyncapis:
- description: ''
  name: Explorium Webhooks
  slug: explorium-webhooks
collections:
- collection_type: open
  name: Explorium AgentSource Business Enrichments API
  slug: open-explorium-business-enrichments-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Businesses API
  slug: open-explorium-businesses-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Credits API
  slug: open-explorium-credits-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Events API
  slug: open-explorium-events-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Prospect Enrichments API
  slug: open-explorium-prospect-enrichments-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Prospects API
  slug: open-explorium-prospects-api
- collection_type: open
  name: Explorium AgentSource Business Enrichments Webhooks API
  slug: open-explorium-webhooks-api
- collection_type: open
  name: Explorium AgentSource API
  slug: open-explorium
common:
- group: company
  title: ''
  type: Blog
  url: https://www.explorium.ai/blog/news-and-updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.explorium.ai/blog/category/news-and-updates/feed/
- group: other
  href: https://artifacts.apis.io/explorium/capabilities/explorium-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/explorium-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/explorium/security/explorium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/explorium-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/explorium/agentic-access/explorium-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/explorium-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/explorium/authentication/explorium-authentication.yml
  title: ''
  type: Authentication
  url: authentication/explorium-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/explorium-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/explorium-ai
- group: company
  title: ''
  type: Website
  url: https://www.explorium.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.explorium.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.explorium.ai/mcp-docs/agentsource-mcp
- group: commercial
  href: https://artifacts.apis.io/explorium/plans/explorium-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/explorium-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/explorium/rate-limits/explorium-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/explorium-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/explorium/finops/explorium-finops.yml
  title: ''
  type: FinOps
  url: finops/explorium-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.explorium.ai/blog/
- group: docs
  href: https://artifacts.apis.io/explorium/openapi/_original/explorium-agentsource-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/explorium-agentsource-openapi.json
- group: other
  href: https://artifacts.apis.io/explorium/overlays/explorium-agentsource-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/explorium-agentsource-overlay.yaml
- group: build
  href: https://artifacts.apis.io/explorium/packages/explorium-packages.yml
  title: ''
  type: Packages
  url: packages/explorium-packages.yml
- group: agent
  href: https://artifacts.apis.io/explorium/well-known/explorium-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/explorium-well-known.yml
- group: other
  href: https://artifacts.apis.io/explorium/well-known/explorium-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/explorium-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/explorium/mcp/explorium-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/explorium-mcp.yml
- group: build
  href: https://artifacts.apis.io/explorium/mcp/explorium-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/explorium-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/explorium/a2a/explorium-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/explorium-a2a.yml
- group: agent
  href: https://artifacts.apis.io/explorium/llms/explorium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/explorium-llms.txt
- group: design
  href: https://artifacts.apis.io/explorium/conformance/explorium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/explorium-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.explorium.ai/data-security/
- group: auth
  href: https://artifacts.apis.io/explorium/security/explorium-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/explorium-trust-center.yml
- group: design
  href: https://artifacts.apis.io/explorium/errors/explorium-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/explorium-problem-types.yml
- group: design
  href: https://artifacts.apis.io/explorium/lifecycle/explorium-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/explorium-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/explorium/conventions/explorium-conventions.yml
  title: ''
  type: Conventions
  url: conventions/explorium-conventions.yml
- group: operate
  href: https://artifacts.apis.io/explorium/changelog/explorium-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/explorium-changelog.yml
- group: design
  href: https://artifacts.apis.io/explorium/data-model/explorium-data-model.yml
  title: ''
  type: DataModel
  url: data-model/explorium-data-model.yml
- group: start
  href: https://artifacts.apis.io/explorium/sandbox/explorium-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/explorium-sandbox.yml
- group: design
  href: https://artifacts.apis.io/explorium/asyncapi/explorium-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/explorium-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/explorium/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/explorium/skills/explorium-agentsource.md
  title: ''
  type: AgentSkill
  url: skills/explorium-agentsource.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.explorium.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.explorium.ai/reference/quick-starts/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.explorium.ai/reference/quick-starts/quick-starts
- group: auth
  title: ''
  type: Authentication
  url: https://www.explorium.ai/auth.md
- group: operate
  title: ''
  type: Support
  url: https://developers.explorium.ai/reference/support-help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.explorium.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.explorium.ai/sign-up/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.explorium.ai/explorium-website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.explorium.ai/privacy-policy/
- group: start
  title: ''
  type: Console
  url: https://www.explorium.ai/mcp-playground/
- group: operate
  title: ''
  type: Contact
  url: mailto:support@explorium.ai
created: '2026-07-11'
description: Explorium is the B2B data layer for AI agents and go-to-market systems. Its AgentSource platform is one external-data and enrichment API plus a hosted MCP server, resolving, fetching, enriching and monitoring a company dataset and a people dataset aggregated from 100+ external sources. The REST API at https://api.explorium.ai publishes an anonymous OpenAPI 3.1 description covering 127 operations across two parallel surfaces - v1 (stable) and v2 (beta) - spanning entity matching, filtered fetch with cursor pagination, market-sizing statistics, autocomplete, seventeen company enrichment families and three people enrichment families (single, bulk to 50, and asynchronous to 10,000), AI-powered research, eighteen business and prospect event types delivered over HMAC-signed webhooks, and a shared prepaid credit pool that meters every call. Authentication is an api_key header on REST and OAuth 2.0 on MCP. Explorium is unusually agent-forward at the discovery layer, serving an RFC 9727
  api-catalog, a conformant A2A agent card, an MCP server card, an ARD capability catalog, an agent-skills index and llms.txt from its own domain.
finops:
- has_sources: true
  method: derived
  name: Explorium Finops
  primary_unit: package
  service_category: ''
  slug: explorium-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/explorium.png
layout: provider
mcp_servers:
- description: ''
  name: Explorium MCP Server
  slug: mcp
modified: '2026-10-06'
name: Explorium
nav: Providers
network: true
overview: 'Explorium publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Businesses API, Credits API, Prospects API, and 21 more. Tagged areas include Data Enrichment, B2B Data, Company Data, Prospect Enrichment, and Firmographics.


  The Explorium catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Explorium''s developer surface includes engineering blog, authentication, documentation, changelog, sandbox, API reference, getting-started guide, and 40 more developer resources.'
plans:
- name: Explorium Plans Pricing
  plan_count: 6
  slug: explorium-plans-pricing
- name: Explorium Price Estimates
  plan_count: 0
  slug: explorium-price-estimates
random_paper: 13
rate_limits:
- limit_count: 6
  name: Explorium Rate Limits
  slug: explorium-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Explorium API Rules
  rule_count: 57
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 10
  slug: explorium-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 55.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 57.9
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
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
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/explorium/explorium-2026-07-25T213931.png
security:
- kind: authentication
  name: Explorium Authentication
  slug: explorium-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Explorium Domain Security
  slug: explorium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Explorium Vulnerability Disclosure
  slug: explorium-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Explorium Trust Center
  slug: explorium-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CCPA
skill_count: 6
skills:
- name: Explorium
  slug: explorium-agentsource
- name: Build a target account list with Explorium
  slug: explorium-build-a-target-account-list
- name: Find and enrich prospects with Explorium
  slug: explorium-find-and-enrich-prospects
- name: Match and enrich companies with Explorium
  slug: explorium-match-and-enrich-companies
- name: Monitor business and prospect events with Explorium
  slug: explorium-monitor-business-events
- name: Run a bulk enrichment job with Explorium
  slug: explorium-run-a-bulk-enrichment-job
slug: explorium
tags:
- Data Enrichment
- B2B Data
- Company Data
- Prospect Enrichment
- Firmographics
- Technographics
- Web Intelligence
- Reference Data
- AI Agents
- MCP
- Agent Readiness
- Sales Intelligence
- Business Events
- Webhook
- Market Intelligence
- A2A
website: https://www.explorium.ai
---
