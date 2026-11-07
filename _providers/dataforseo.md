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
    error_semantics: documented
    event_surface_described: true
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
  score: 61.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 257
  human_in_the_loop: 3
  name: Dataforseo Agentic Access
  operation_count: 554
  slug: dataforseo-agentic-access
  summary_line: 554 operations · 257 acting · 3 human-in-the-loop
api_count: 12
apis:
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The AiOptimization API from DataForSEO — 44 operation(s) for aioptimization.
  name: DataForSEO AiOptimization API
  phrasing_intents:
  - id: ChatGptLlmScraperLocations
    intent: List locations for the ChatGPT scraper
    question: Which locations can I target when scraping ChatGPT search results?
  - id: ChatGptLlmScraperLocationsCountry
    intent: List ChatGPT scraper locations in a country
    question: Which ChatGPT scraper locations exist within one specific country?
  - id: ChatGptLlmScraperLanguages
    intent: List languages for the ChatGPT scraper
    question: What languages does the ChatGPT LLM scraper support?
  - id: ChatGptLlmScraperTaskPost
    intent: Queue a ChatGPT search scraping task
    question: How do I queue a ChatGPT search scrape to collect later instead of waiting live?
  - id: ChatGptLlmScraperTasksReady
    intent: List completed ChatGPT scraper tasks
    question: Which of my queued ChatGPT scraper tasks are finished but not yet collected?
  - id: ChatGptLlmScraperTaskGetAdvanced
    intent: Get structured results of a ChatGPT scrape
    question: How do I fetch the parsed, structured output of a ChatGPT scraper task I queued?
  - id: ChatGptLlmScraperTaskGetHtml
    intent: Get raw HTML of a queued ChatGPT scrape
    question: Can I download the raw HTML page of a ChatGPT scraper task I already queued?
  - id: ChatGptLlmScraperLiveAdvanced
    intent: Scrape ChatGPT search results live
    question: Can I get structured ChatGPT search results immediately in one call?
  phrasing_ops: 44
  slug: dataforseo-aioptimization-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The Appendix API from DataForSEO — 4 operation(s) for appendix.
  name: DataForSEO Appendix API
  phrasing_intents:
  - id: UserData
    intent: Check account usage, prices and spending
    question: How much have I spent on my DataForSEO account so far?
  - id: Errors
    intent: List possible API error codes
    question: What do the internal error codes and status messages returned by the API mean?
  - id: WebhookResend
    intent: Resend task webhooks
    question: Can I get pingbacks or postbacks re-sent for tasks whose webhook I missed?
  - id: AppendixStatus
    intent: Check the status of all APIs and endpoints
    question: Is any API or endpoint currently down or degraded?
  phrasing_ops: 4
  slug: dataforseo-appendix-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The Backlinks API from DataForSEO — 24 operation(s) for backlinks.
  name: DataForSEO Backlinks API
  phrasing_intents:
  - id: BacklinksIdList
    intent: List IDs of Backlinks tasks in a time period
    question: Can I get the IDs of every Backlinks task I created during a given time window?
  - id: BacklinksErrors
    intent: List Backlinks tasks that failed recently
    question: Which of my Backlinks API calls returned an error in the past seven days?
  - id: BacklinksAvailableFilters
    intent: List filters usable in Backlinks requests
    question: What fields can I filter and sort on when pulling backlink data?
  - id: Index
    intent: Get the size of the backlinks database
    question: How many backlinks, domains and pages does the DataForSEO index hold right now?
  - id: SummaryLive
    intent: Get a backlink profile overview for a target
    question: What does the overall backlink profile of a domain look like at a glance?
  - id: HistoryLive
    intent: Get historical backlink data for a domain
    question: How many backlinks did my domain have back in 2019 compared with today?
  - id: BacklinksLive
    intent: List the backlinks pointing to a target
    question: Which individual links point to my website?
  - id: AnchorsLive
    intent: Analyze anchor texts linking to a site
    question: What anchor text do other sites use when they link to me?
  phrasing_ops: 24
  slug: dataforseo-backlinks-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The BusinessData API from DataForSEO — 55 operation(s) for businessdata.
  name: DataForSEO BusinessData API
  phrasing_intents:
  - id: BusinessDataIdList
    intent: List IDs of Business Data tasks in a time period
    question: Can I get the IDs of every Business Data task I created in a given time window?
  - id: BusinessDataErrors
    intent: List Business Data tasks that failed recently
    question: Which of my Business Data tasks returned an error in the past seven days?
  - id: BusinessListingsLocations
    intent: List locations for the Business Listings search
    question: Which locations can I search in the Google Maps business listings database?
  - id: BusinessListingsCategories
    intent: List top business categories by business count
    question: What are the most common business categories in the listings database?
  - id: BusinessListingsAvailableFilters
    intent: List filters usable in Business Listings search
    question: What fields can I filter on when searching business listings?
  - id: BusinessListingsSearchLive
    intent: Search Google Maps business listings by category
    question: Which businesses are listed on Google Maps in a given category near a location?
  - id: BusinessListingsCategoriesAggregationLive
    intent: Count businesses per group of related categories
    question: How many businesses fall into each group of related categories in an area?
  - id: BusinessDataGoogleLocations
    intent: List Google locations for business data tasks
    question: Which Google locations can I target for business profile and review tasks?
  phrasing_ops: 55
  slug: dataforseo-businessdata-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The DataforseoLabs API from DataForSEO — 47 operation(s) for dataforseolabs.
  name: DataForSEO DataforseoLabs API
  phrasing_intents:
  - id: DataforseoLabsIdList
    intent: List Labs task IDs for a time period
    question: Can I get the IDs of every DataForSEO Labs task I created within a date range?
  - id: Status
    intent: Check when Labs data was last updated
    question: When was the Labs keyword database last refreshed for Google, Bing and Amazon?
  - id: DataforseoLabsErrors
    intent: List Labs tasks that failed recently
    question: Which of my Labs API tasks returned errors over the past 7 days?
  - id: AvailableFilters
    intent: List filters usable in Labs endpoints
    question: What filter fields and operators can I use in Labs API requests?
  - id: LocationsAndLanguages
    intent: List locations and languages supported by Labs
    question: Which countries and languages does the Labs API support for Google, Bing and Amazon?
  - id: Categories
    intent: List Google product and service categories
    question: What is the full list of Google product and service categories used in Labs?
  - id: GoogleAvailableHistory
    intent: List dates available for domain category metrics
    question: Which dates can I use as first_date and second_date when comparing domain metrics by category?
  - id: GoogleKeywordsForSiteLive
    intent: Find keywords relevant to a website
    question: Can I get a list of keywords relevant to a domain with search volume and CPC?
  phrasing_ops: 47
  slug: dataforseo-dataforseolabs-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The DomainAnalytics API from DataForSEO — 14 operation(s) for domainanalytics.
  name: DataForSEO DomainAnalytics API
  phrasing_intents:
  - id: DomainAnalyticsIdList
    intent: List my Domain Analytics task IDs for a period
    question: Can I see the IDs of all Domain Analytics tasks I created in a time range?
  - id: DomainAnalyticsErrors
    intent: List Domain Analytics tasks that failed
    question: Which Domain Analytics tasks returned errors in the past 7 days?
  - id: TechnologiesAvailableFilters
    intent: List filters for technology lookups
    question: What filters can I apply when searching domains by technology?
  - id: TechnologiesLocations
    intent: List locations for technology data
    question: Which countries can I segment technology usage data by?
  - id: TechnologiesLanguages
    intent: List languages for technology data
    question: Which website languages can I segment technology usage by?
  - id: TechnologiesTechnologies
    intent: List all detectable web technologies
    question: Which web technologies can be detected, grouped by category?
  - id: TechnologiesAggregationTechnologiesLive
    intent: Find technologies commonly used together
    question: What other technologies do sites running a given e-commerce platform usually use too?
  - id: TechnologiesTechnologiesSummaryLive
    intent: Count domains using a technology by country
    question: How many domains use a given technology, broken down by country and language?
  phrasing_ops: 14
  slug: dataforseo-domainanalytics-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The KeywordsData API from DataForSEO — 70 operation(s) for keywordsdata.
  name: DataForSEO KeywordsData API
  phrasing_intents:
  - id: KeywordsDataIdList
    intent: List my Keywords Data task IDs for a period
    question: Can I see the IDs of every Keywords Data task I created in a given time window?
  - id: KeywordsDataErrors
    intent: List Keywords Data tasks that failed
    question: Which of my Keywords Data tasks returned an error in the past 7 days?
  - id: GoogleAdsStatus
    intent: Check if Google updated last month's keyword data
    question: Has Google released last month's keyword search volume data yet?
  - id: GoogleAdsLocations
    intent: List locations for Google Ads keyword data
    question: Which countries, regions and cities can I target when pulling Google Ads keyword data?
  - id: GoogleAdsLocationsCountry
    intent: List Google Ads keyword locations in one country
    question: Which cities and regions inside a single country are available for Google Ads keyword data?
  - id: GoogleAdsLanguages
    intent: List languages for Google Ads keyword data
    question: What languages can I request Google Ads keyword volume in?
  - id: GoogleAdsSearchVolumeTaskPost
    intent: Queue a Google Ads search volume task
    question: Can I submit a batch of keywords for Google Ads search volume and collect the results later?
  - id: GoogleAdsSearchVolumeTasksReady
    intent: List finished Google Ads search volume tasks
    question: Which of my queued Google Ads search volume tasks have finished but haven't been collected?
  phrasing_ops: 70
  slug: dataforseo-keywordsdata-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The Merchant API from DataForSEO — 32 operation(s) for merchant.
  name: DataForSEO Merchant API
  phrasing_intents:
  - id: MerchantIdList
    intent: List my Merchant task IDs for a period
    question: Can I see the IDs of all the shopping data tasks I created in a date range?
  - id: MerchantErrors
    intent: List Merchant tasks that failed
    question: Which of my Merchant API tasks returned errors in the last 7 days?
  - id: MerchantGoogleLanguages
    intent: List Google Shopping languages
    question: What languages are supported for Google Shopping results?
  - id: MerchantGoogleLocations
    intent: List Google Shopping locations
    question: Which locations can I pull Google Shopping data for?
  - id: MerchantGoogleLocationsCountry
    intent: List Google Shopping locations in a country
    question: Which Google Shopping cities and regions are available within one country?
  - id: GoogleProductsTaskPost
    intent: Queue a Google Shopping product search
    question: Can I queue a search that lists the products Google Shopping shows for a query?
  - id: GoogleProductsTasksReady
    intent: List finished Google Shopping product tasks
    question: Which Google Shopping product search tasks have completed but not been collected?
  - id: MerchantTasksReady
    intent: List finished Merchant tasks across all types
    question: Which Merchant tasks of any kind, Google or Amazon, are completed and waiting to be collected?
  phrasing_ops: 32
  slug: dataforseo-merchant-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The OnPage API from DataForSEO — 30 operation(s) for onpage.
  name: DataForSEO OnPage API
  phrasing_intents:
  - id: OnPageIdList
    intent: List On-Page task IDs for a time period
    question: Can I get the IDs of every site crawl task I created within a date range?
  - id: OnPageErrors
    intent: List On-Page tasks that failed recently
    question: Which of my site audit tasks returned errors in the past 7 days?
  - id: ForceStop
    intent: Force stop a running website crawl
    question: Can I stop a website crawl that's still running?
  - id: OnPageAvailableFilters
    intent: List filters and thresholds for On-Page
    question: What filters and performance thresholds can I use with On-Page audit results?
  - id: TaskPost
    intent: Start a website crawl and audit
    question: How do I start an SEO audit that crawls my whole website?
  - id: OnPageTasksReady
    intent: List completed site crawl tasks
    question: Which of my site crawls have finished but haven't been collected yet?
  - id: Summary
    intent: Get the audit summary of a crawled site
    question: What's the overall health and list of issues for a site I crawled?
  - id: Pages
    intent: List crawled pages with their checks
    question: Which crawled pages failed on-page checks like missing titles or slow load?
  phrasing_ops: 30
  slug: dataforseo-onpage-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The Serp API from DataForSEO — 181 operation(s) for serp.
  name: DataForSEO Serp API
  phrasing_intents:
  - id: IdList
    intent: List IDs of SERP tasks created in a period
    question: Can I get every SERP task ID I created during a given time window, including unfinished ones?
  - id: Errors
    intent: List SERP tasks that failed recently
    question: Which of my SERP API tasks returned an error in the past seven days?
  - id: Screenshot
    intent: Capture a screenshot of a search results page
    question: Can I get an image snapshot of what a search results page actually looked like?
  - id: AiSummary
    intent: Summarize a SERP with an AI prompt
    question: Can an AI write a summary of everything that shows up on a search results page?
  - id: GoogleLocations
    intent: List locations supported for Google SERPs
    question: Which cities and regions can I target when pulling Google search results?
  - id: GoogleLocationsCountry
    intent: List Google SERP locations in one country
    question: Can I narrow the Google SERP location list to a single country?
  - id: GoogleLanguages
    intent: List languages supported for Google SERPs
    question: What languages can I request Google search results in?
  - id: GoogleOrganicTaskPost
    intent: Queue a Google organic search task
    question: How do I schedule a Google organic results check for a keyword and collect it later?
  phrasing_ops: 181
  slug: dataforseo-serp-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The App Data API from DataForSEO — 42 operation(s) for app data.
  name: DataForSEO App Data API
  phrasing_intents:
  - id: AppDataIdList
    intent: List IDs of App Data tasks in a time period
    question: Can I get the IDs of every App Data task I created in a given time window?
  - id: AppDataErrors
    intent: List App Data tasks that failed recently
    question: Which of my App Data tasks returned an error in the past seven days?
  - id: GoogleCategories
    intent: List Google Play app categories
    question: What app categories exist on Google Play for app data tasks?
  - id: AppDataGoogleLocations
    intent: List Google locations supported for app data
    question: Which Google Play locations can I target for app data tasks?
  - id: AppDataGoogleLocationsCountry
    intent: List Google Play app locations in one country
    question: Which Google Play app data locations are available within a single country?
  - id: AppDataGoogleLanguages
    intent: List Google languages supported for app data
    question: Which languages can I set when pulling Google Play app data?
  - id: GoogleAppSearchesTaskPost
    intent: Queue a Google Play app keyword search
    question: Which apps rank on Google Play for a given keyword?
  - id: GoogleAppSearchesTasksReady
    intent: List finished Google Play app search tasks
    question: Which of my Google Play app search tasks are done but not collected yet?
  phrasing_ops: 42
  slug: dataforseo-app-data-api
- baseURL: https://api.dataforseo.com
  baseurl_source: declared
  description: The Content Analysis API from DataForSEO — 11 operation(s) for content analysis.
  name: DataForSEO Content Analysis API
  phrasing_intents:
  - id: ContentAnalysisIdList
    intent: List my Content Analysis task IDs for a period
    question: Can I see the IDs of all Content Analysis tasks I created in a time window?
  - id: ContentAnalysisAvailableFilters
    intent: List filters for content analysis
    question: What filters can I apply to citation and sentiment queries?
  - id: Locations
    intent: List locations for content analysis
    question: Which locations can I scope content citation data to?
  - id: Languages
    intent: List languages for content analysis
    question: Which languages are covered for content citation analysis?
  - id: ContentAnalysisCategories
    intent: List content categories
    question: Which product and service categories can I analyze citations for?
  - id: SearchLive
    intent: Find detailed citations of a keyword
    question: Where on the web is my brand or keyword being mentioned?
  - id: ContentAnalysisSummaryLive
    intent: Summarize citations of a keyword
    question: What's the overall picture of mentions for a keyword, without listing each one?
  - id: SentimentAnalysisLive
    intent: Analyze sentiment of keyword citations
    question: Are mentions of my brand mostly positive or negative?
  phrasing_ops: 11
  slug: dataforseo-content-analysis-api
artifact_total: 52
asyncapis:
- description: ''
  name: Dataforseo Webhooks
  slug: dataforseo-webhooks
collections:
- collection_type: open
  name: DataForSEO AiOptimization API
  slug: open-dataforseo-aioptimization-api
- collection_type: open
  name: DataForSEO AiOptimization AppData API
  slug: open-dataforseo-appdata-api
- collection_type: open
  name: DataForSEO AiOptimization Appendix API
  slug: open-dataforseo-appendix-api
- collection_type: open
  name: DataForSEO AiOptimization Backlinks API
  slug: open-dataforseo-backlinks-api
- collection_type: open
  name: DataForSEO AiOptimization BusinessData API
  slug: open-dataforseo-businessdata-api
- collection_type: open
  name: DataForSEO AiOptimization ContentAnalysis API
  slug: open-dataforseo-contentanalysis-api
- collection_type: open
  name: DataForSEO AiOptimization DataforseoLabs API
  slug: open-dataforseo-dataforseolabs-api
- collection_type: open
  name: DataForSEO AiOptimization DomainAnalytics API
  slug: open-dataforseo-domainanalytics-api
- collection_type: open
  name: DataForSEO AiOptimization KeywordsData API
  slug: open-dataforseo-keywordsdata-api
- collection_type: open
  name: DataForSEO AiOptimization Merchant API
  slug: open-dataforseo-merchant-api
- collection_type: open
  name: DataForSEO AiOptimization OnPage API
  slug: open-dataforseo-onpage-api
- collection_type: open
  name: DataForSEO AiOptimization Serp API
  slug: open-dataforseo-serp-api
common:
- group: other
  href: https://artifacts.apis.io/dataforseo/overlays/dataforseo-appdata-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dataforseo-appdata-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dataforseo/overlays/dataforseo-contentanalysis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dataforseo-contentanalysis-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dataforseo/capabilities/dataforseo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dataforseo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/dataforseo/agentic-access/dataforseo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dataforseo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dataforseo/security/dataforseo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataforseo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dataforseo/authentication/dataforseo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataforseo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://dataforseo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dataforseo.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dataforseo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dataforseo
- group: company
  title: ''
  type: Blog
  url: https://dataforseo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dataforseo.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dataforseo.com
- group: other
  title: ''
  type: X
  url: https://x.com/dataforseo
- group: commercial
  href: https://artifacts.apis.io/dataforseo/plans/dataforseo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataforseo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dataforseo/rate-limits/dataforseo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dataforseo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dataforseo/finops/dataforseo-finops.yml
  title: ''
  type: FinOps
  url: finops/dataforseo-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dataforseo.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dataforseo.com/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://dataforseo.com/blog/a-kickstart-guide-to-using-dataforseo-apis
- group: operate
  title: ''
  type: Support
  url: https://dataforseo.com/help-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dataforseo
- group: start
  title: ''
  type: SignUp
  url: https://app.dataforseo.com/register
- group: start
  title: ''
  type: Login
  url: https://app.dataforseo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataforseo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataforseo.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/55275669/2sBXwmRYr2
- group: operate
  title: ''
  type: ChangeLog
  url: https://dataforseo.com/updates
- group: auth
  title: ''
  type: Compliance
  url: https://dataforseo.com/wp-content/uploads/2021/12/27001_DATAFORSEO-.pdf
- group: build
  href: https://artifacts.apis.io/dataforseo/packages/dataforseo-packages.yml
  title: ''
  type: Packages
  url: packages/dataforseo-packages.yml
- group: build
  href: https://artifacts.apis.io/dataforseo/packages/dataforseo-packages.yml
  title: ''
  type: SDKs
  url: packages/dataforseo-packages.yml
- group: agent
  href: https://artifacts.apis.io/dataforseo/well-known/dataforseo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataforseo-well-known.yml
- group: agent
  href: https://artifacts.apis.io/dataforseo/mcp/dataforseo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dataforseo-mcp.yml
- group: build
  href: https://artifacts.apis.io/dataforseo/mcp/dataforseo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dataforseo-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dataforseo/llms/dataforseo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataforseo-llms.txt
- group: design
  href: https://artifacts.apis.io/dataforseo/conformance/dataforseo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataforseo-conformance.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/errors/dataforseo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataforseo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/lifecycle/dataforseo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dataforseo-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/dataforseo/scopes/dataforseo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dataforseo-scopes.yml
- group: start
  href: https://artifacts.apis.io/dataforseo/sandbox/dataforseo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dataforseo-sandbox.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/conventions/dataforseo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dataforseo-conventions.yml
- group: operate
  href: https://artifacts.apis.io/dataforseo/changelog/dataforseo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dataforseo-changelog.yml
- group: build
  href: https://artifacts.apis.io/dataforseo/cli/dataforseo-cli.yml
  title: ''
  type: CLI
  url: cli/dataforseo-cli.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/data-model/dataforseo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dataforseo-data-model.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/asyncapi/dataforseo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dataforseo-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/dataforseo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/vocabulary/dataforseo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataforseo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/rules/dataforseo-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/dataforseo-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/dataforseo/json-ld/dataforseo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dataforseo-context.jsonld
created: '2026-06-13'
description: DataForSEO is an SEO data platform offering REST APIs for SERP results, keyword data, backlink analysis, on-page audits, domain analytics, and competitor research across 100+ search engines. It provides pay-as-you-go access to structured SEO and digital marketing data for software developers, agencies, and enterprise teams.
finops:
- has_sources: true
  method: derived
  name: Dataforseo Finops
  primary_unit: task
  service_category: ''
  slug: dataforseo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dataforseo.png
json_schemas:
- name: DataForSEO Ai Optimization API Schemas
  property_count: 0
  slug: dataforseo-ai-optimization
- name: DataForSEO App Data API Schemas
  property_count: 0
  slug: dataforseo-app-data
- name: DataForSEO Appendix API Schemas
  property_count: 0
  slug: dataforseo-appendix
- name: DataForSEO Backlinks API Schemas
  property_count: 0
  slug: dataforseo-backlinks
- name: DataForSEO Business Data API Schemas
  property_count: 0
  slug: dataforseo-business-data
- name: DataForSEO Content Analysis API Schemas
  property_count: 0
  slug: dataforseo-content-analysis
- name: DataForSEO Domain Analytics API Schemas
  property_count: 0
  slug: dataforseo-domain-analytics
- name: DataForSEO Keywords Data API Schemas
  property_count: 0
  slug: dataforseo-keywords-data
- name: DataForSEO Labs API Schemas
  property_count: 0
  slug: dataforseo-labs
- name: DataForSEO Merchant API Schemas
  property_count: 0
  slug: dataforseo-merchant
- name: DataForSEO On Page API Schemas
  property_count: 0
  slug: dataforseo-on-page
- name: DataForSEO Serp API Schemas
  property_count: 0
  slug: dataforseo-serp
jsonld:
- class_count: 24
  name: Dataforseo Context
  property_count: 45
  slug: dataforseo-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.dataforseo.com over streamable HTTP requiring OAuth; 4 tools listed.
  name: DataForSEO MCP Server
  slug: dataforseo
modified: '2026-08-13'
name: DataForSEO
nav: Providers
network: true
overview: 'DataForSEO publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including AiOptimization API, Appendix API, Backlinks API, and 9 more. Tagged areas include SEO, SERP, Keywords, Backlinks, and Domain Analytics.


  The DataForSEO catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DataForSEO''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 42 more developer resources.'
plans:
- name: Dataforseo Plans Pricing
  plan_count: 11
  slug: dataforseo-plans-pricing
- name: Dataforseo Price Estimates
  plan_count: 0
  slug: dataforseo-price-estimates
random_paper: 8
rate_limits:
- limit_count: 0
  name: Dataforseo Rate Limits
  slug: dataforseo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: DataForSEO — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: dataforseo-jsonschema-spectral-rules
scopes:
- name: Dataforseo Scopes
  scope_count: 2
  slug: dataforseo-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.8
    catalog_earned_first_party: 12.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 41.7
    contract_quality: 72.3
    developer_ergonomics: 90.5
    discoverability: 80.0
    operational_transparency: 34.2
  previous_composite: 73.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
screenshot: https://apis.io/screenshots/dataforseo/dataforseo-2026-06-20T175648.png
security:
- kind: authentication
  name: Dataforseo Authentication
  slug: dataforseo-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Dataforseo Domain Security
  slug: dataforseo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: amazon-competitor-auditor
  slug: dataforseo-amazon-competitor-auditor
- name: dataforseo-onpage-site-audit
  slug: dataforseo-onpage-site-audit
- name: pricing-strategy
  slug: dataforseo-pricing-strategy
- name: dataforseo-serp-task-lifecycle
  slug: dataforseo-serp-task-lifecycle
slug: dataforseo
tags:
- SEO
- SERP
- Keywords
- Backlinks
- Domain Analytics
- On-Page SEO
- Competitor Research
- Search Engines
- Content Analysis
- E-Commerce
- App Store
- Business Data
- AI Optimization
- Social Media
website: https://dataforseo.com
---
