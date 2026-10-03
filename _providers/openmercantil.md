---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 61
  human_in_the_loop: 2
  name: Openmercantil Agentic Access
  operation_count: 210
  slug: openmercantil-agentic-access
  summary_line: 210 operations · 61 acting · 2 human-in-the-loop
api_count: 3
apis:
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: 'Account API credential management: list, create, rotate and revoke opaque omk_* API keys. Secrets are returned once and recoverable only via an identical Idempotency-Key replay inside 24 hours.'
  name: OpenMercantil API Credentials API
  phrasing_intents:
  - id: listUserApiCredentials
    intent: List my API credentials
    question: Which API keys does my OpenMercantil account have and what scopes do they carry?
  - id: createUserApiCredential
    intent: Create an API credential
    question: How do I generate a new API key for my account?
  - id: rotateUserApiCredential
    intent: Rotate an API credential
    question: How do I replace a leaked API key with a fresh token?
  - id: revokeUserApiCredential
    intent: Revoke an API credential
    question: How do I permanently disable one of my API keys?
  phrasing_ops: 4
  slug: openmercantil-api-credentials-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Session-bound Stripe checkout, invoices and portal contracts. External actions are bounded, idempotent and never exposed through the public MCP.
  name: OpenMercantil Billing API
  phrasing_intents:
  - id: postDonationCheckout
    intent: Start a one-time donation checkout
    question: Can I make a one-off donation to support OpenMercantil?
  - id: postCreditsCheckout
    intent: Buy a credit pack
    question: How do I buy more credits for company reports?
  - id: postSubscriptionCheckout
    intent: Start a subscription checkout
    question: How do I subscribe to a paid plan?
  - id: getBillingInvoices
    intent: List my invoices and subscription
    question: Where can I see my past invoices?
  - id: getBillingPortal
    intent: Open my billing portal by redirect
    question: Can I be redirected straight to my Stripe billing portal?
  - id: postBillingPortal
    intent: Create a billing portal session as JSON
    question: How do I get a Stripe customer portal URL returned as JSON?
  - id: postLegacyBillingPortal
    intent: Create a portal session via the legacy route
    question: Does the old /api/v1/portal route still create a customer portal session?
  - id: receiveStripeWebhook
    intent: Receive a signed Stripe event
    question: Where does Stripe deliver its signed events for OpenMercantil billing?
  phrasing_ops: 8
  slug: openmercantil-billing-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Daily BORME publications, multi-source timeline and registry events
  name: OpenMercantil BORME API
  phrasing_intents:
  - id: getCompanyBySlugEvents
    intent: List a company's BORME events by year
    question: How do I page through the BORME registry events published about one Spanish company?
  - id: getCompanyBySlugTimeline
    intent: Get a company's multi-source timeline
    question: Can I see one chronological timeline for a company combining BORME acts and public procurement records?
  - id: getDailyByDate
    intent: Get the BORME daily summary grouped by province
    question: Which BORME acts were published on a given day, broken down by province and act type?
  - id: getLegacyDailySummaryByDate
    intent: Get a BORME daily summary via the legacy route
    question: Does the old summary/date route still return the BORME daily summary?
  - id: getEmpresaBySlugFacts
    intent: Get structured BORME facts for a company
    question: Which appointments, removals and capital changes has BORME published for a company?
  - id: getLegacyCompanyBySlugFacts
    intent: Get company BORME facts via the legacy English route
    question: Is the old English company/facts route still available for extracted BORME facts?
  phrasing_ops: 6
  slug: openmercantil-borme-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Company reports and registry events
  name: OpenMercantil Companies API
  phrasing_intents:
  - id: getCompanyBySlug
    intent: Get a Spanish company's registry report
    question: What does OpenMercantil's structured report on a Spanish company include?
  - id: compareCompanies
    intent: Compare two companies side by side
    question: Can I compare two Spanish companies side by side in one request?
  - id: listPublicCompanyDownloads
    intent: List the public company dataset downloads
    question: Which bulk company datasets can I download for free?
  - id: getCompanyBySlugEvents
    intent: List a company's BORME events by year
    question: How do I see every BORME registry event published for a company?
  - id: getCompanyBySlugTimeline
    intent: Get a company's combined multi-source timeline
    question: Can I get one chronological timeline mixing a company's BORME acts and procurement notices?
  - id: getCompanyBySlugOfficers
    intent: List a company's current and past officers
    question: Who are the directors and administrators of a Spanish company?
  - id: getCompanyBySlugContracts
    intent: List procurement notices linked to a company
    question: Which public procurement notices is a Spanish company linked to?
  - id: getCompanyBySlugProcurement
    intent: Get a company's procurement via the alias route
    question: Is there a /procurement alias that returns the same payload as a company's contracts route?
  phrasing_ops: 34
  slug: openmercantil-companies-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Bulk exports (CSV / JSON / aggregated stats)
  name: OpenMercantil Datasets API
  phrasing_intents:
  - id: listPublicCompanyDownloads
    intent: List the public company dataset downloads
    question: Which bulk company datasets can I download for free?
  - id: getCcaaStatsJson
    intent: Get company totals by autonomous community
    question: How many companies are registered in each Spanish autonomous community?
  - id: getLegacyCcaaStats
    intent: Get CCAA aggregates via the legacy alias
    question: Does the old suffix-less /ccaa/stats route still work?
  - id: getSectoresStatsJson
    intent: Get company totals by CNAE sector as JSON
    question: How many companies are there in each CNAE sector section?
  - id: getLegacySectoresStats
    intent: Get sector aggregates via the legacy alias
    question: Does the deprecated suffix-less /sectores/stats route still return data?
  - id: getSectoresStatsCsv
    intent: Download CNAE sector aggregates as CSV
    question: Can I download the per-sector statistics as a CSV file?
  - id: getContractsTopCompanies
    intent: Rank corporate suppliers via top-companies route
    question: Which companies top the contracts top-companies ranking by award procedures?
  - id: getContractsTopPersons
    intent: Rank persons by procurement-signing companies
    question: Is there a ranking of people linked to companies that win public contracts?
  phrasing_ops: 13
  slug: openmercantil-datasets-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Corporate and person-to-company relationship graphs. Every emitted record retains the source-specific terms authorized by the active public source catalog; no blanket relicensing applies.
  name: OpenMercantil Graph API
  phrasing_intents:
  - id: getGrafoBySlug
    intent: Get a company's corporate parent/child graph
    question: Who are a company's parent and subsidiary entities?
  - id: getGrafoPersonaBySlug
    intent: Get the companies linked to a person
    question: Which companies is a person connected to in BORME?
  - id: getCompanyBySlugNetwork
    intent: Get a company's documentary network
    question: Is the company documentary network projection available yet?
  phrasing_ops: 3
  slug: openmercantil-graph-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Public read-only connector catalog. Never exposes credentials, OAuth tokens, webhook secrets or operator actions.
  name: OpenMercantil Integrations API
  phrasing_intents:
  - id: receiveStripeWebhook
    intent: Receive a signed Stripe event
    question: Where does Stripe deliver its signed events for OpenMercantil billing?
  - id: listIntegrations
    intent: List public data-source integrations
    question: Which public data sources are integrated and legally allowed for reuse?
  - id: getIntegration
    intent: Get one integration's legal and transport status
    question: Is a specific data source integration legally cleared and technically available?
  phrasing_ops: 3
  slug: openmercantil-integrations-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: 'Spanish mercantile-law layer (derecho mercantil): legislation corpus + article texts + act→norm bridge. Distributes the consolidated BOE legal corpus structured by OpenMercantil so LLMs and agents can'
  name: OpenMercantil Legal API
  phrasing_intents:
  - id: createCompanyLegalReport
    intent: Generate a redacted legal report on a company
    question: How do I order a legal report on a Spanish company with my credits?
  - id: getLegalNorms
    intent: List core Spanish mercantile-law norms
    question: Which Spanish commercial laws and codes are covered?
  - id: getLegacyLegalNorms
    intent: List law norms via the singular legacy alias
    question: Does the deprecated singular /legal/norm route still list all norms?
  - id: getLegalNormBySlug
    intent: Get one mercantile-law norm and its key articles
    question: What are the key articles of a Spanish commercial law?
  - id: getLegalArticleByNormByN
    intent: Read the consolidated text of a law article
    question: Can I read the consolidated text of one article of a Spanish law?
  - id: getLegalActMap
    intent: Map every BORME act type to its governing law
    question: Which law governs each type of BORME registry act?
  - id: getLegalActMapByActo
    intent: Find the law governing one BORME act type
    question: Which law and articles govern a capital increase or an appointment in BORME?
  phrasing_ops: 7
  slug: openmercantil-legal-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Documentary mentions of natural persons in BORME (officer roles). Persons treated as documentary mentions only — no DNI, no contact data, no scoring.
  name: OpenMercantil Persons API
  phrasing_intents:
  - id: getCompanyBySlugOfficers
    intent: List a company's current and past officers
    question: Who are the directors and administrators of a Spanish company?
  - id: getPersonaBySlug
    intent: Get documentary registry mentions of a person
    question: In which BORME publications is a person mentioned?
  - id: getLegacyPersonBySlug
    intent: Get person mentions via the legacy English route
    question: Does the deprecated English person route still return registry mentions?
  - id: getPersonSearch
    intent: Search registry mentions of people by name
    question: How do I find a person by name in company registry records?
  - id: getPersonaBySlugContracts
    intent: Get procurement linked to a person
    question: Can I see public contracts connected to a specific person?
  phrasing_ops: 5
  slug: openmercantil-persons-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Public procurement awards (PLACSP) and grants (BDNS)
  name: OpenMercantil Public Procurement API
  phrasing_intents:
  - id: getCompanyBySlugContracts
    intent: List procurement notices linked to a company
    question: Which public procurement notices is a Spanish company linked to?
  - id: getCompanyBySlugProcurement
    intent: Get a company's procurement via the alias route
    question: Is there a /procurement alias that returns the same payload as a company's contracts route?
  - id: getCompanyBySlugGrants
    intent: List public grants awarded to a company
    question: Which BDNS public subsidies has a Spanish company been awarded?
  - id: getPersonaBySlugContracts
    intent: Get procurement linked to a person
    question: Can I see public contracts connected to a specific person?
  - id: getCompanyBySlugTed
    intent: List EU TED notices linked to a company
    question: Which EU Tenders Electronic Daily notices mention a Spanish company's NIF?
  - id: getContractsTopCompanies
    intent: Rank corporate suppliers via top-companies route
    question: Which companies top the contracts top-companies ranking by award procedures?
  - id: getContractsTopPersons
    intent: Rank persons by procurement-signing companies
    question: Is there a ranking of people linked to companies that win public contracts?
  - id: getContractsTopCompaniesCsv
    intent: Download the top-companies ranking as CSV
    question: Can I download the ranking of top procurement suppliers as a CSV?
  phrasing_ops: 13
  slug: openmercantil-public-procurement-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Company and person search endpoints
  name: OpenMercantil Search API
  phrasing_intents:
  - id: getSearch
    intent: Search Spanish companies by name or CIF
    question: How do I find a Spanish company by its name or CIF tax ID?
  - id: getPersonSearch
    intent: Search registry mentions of a person's name
    question: Where is a person's name mentioned in Spanish registry publications?
  phrasing_ops: 2
  slug: openmercantil-search-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: CNAE sector aggregates, ratios and company listings
  name: OpenMercantil Sectors API
  phrasing_intents:
  - id: getSectorByCnaeCompanies
    intent: List companies in a CNAE sector with filters
    question: Which Spanish companies operate in a given CNAE activity code?
  - id: getSectorByCnaeRatios
    intent: Get Banco de España ratios for a CNAE division
    question: What are the Banco de España Central de Balances ratios by year for a two-digit CNAE division?
  - id: getCnaeTree
    intent: Browse the CNAE activity code hierarchy
    question: What does the full CNAE-2009 activity classification hierarchy look like?
  - id: getCnaeByCode
    intent: Look up a CNAE code
    question: What activity does a given CNAE code stand for?
  - id: getSectorCompanies
    intent: List companies in a sector (v1.1 route)
    question: Is there a simpler v1.1 route that just lists companies under a sector code with a limit?
  - id: getSectorRatios
    intent: Get sector financial ratios (v1.1 route)
    question: Where is the v1.1 endpoint for a sector's aggregated financial ratios?
  - id: getSectorStats
    intent: Get company counts and growth across sectors
    question: Which CNAE sectors have the most companies and the fastest growth?
  - id: getSectorStatsCsv
    intent: Download sector statistics as CSV
    question: Can I download the sector aggregate statistics as a CSV file?
  phrasing_ops: 8
  slug: openmercantil-sectors-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Source catalog metadata, freshness and integration status
  name: OpenMercantil Sources API
  phrasing_intents:
  - id: getSourcesFreshness
    intent: See how fresh each public data source is
    question: How recent is the data from each public source OpenMercantil publishes?
  - id: getSourcesStatus
    intent: Get public metadata about the data sources
    question: Which public sources are in the catalog and what data date do they carry?
  - id: getCompanyGrants
    intent: List public grants a company received
    question: Has this Spanish company received any public subsidies or grants?
  - id: getCompanySanctions
    intent: Check a company for sanctions hits
    question: Is this company on any sanctions list or fined by a competition authority?
  - id: getCompanyCnmv
    intent: Get a company's CNMV securities records
    question: What does the Spanish securities regulator CNMV have on file for a company?
  phrasing_ops: 5
  slug: openmercantil-sources-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Customer-support writes. Anonymous creation requires explicit privacy consent; replies require an authenticated owner session and CSRF. Ticket data is never exposed through the public MCP.
  name: OpenMercantil Support API
  phrasing_intents:
  - id: createSupportTicket
    intent: Open a customer-support ticket
    question: How do I contact OpenMercantil support?
  - id: replySupportTicket
    intent: Reply to one of my support tickets
    question: How do I add a reply to a support ticket I opened?
  phrasing_ops: 2
  slug: openmercantil-support-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Service health and metadata
  name: OpenMercantil System API
  phrasing_intents:
  - id: getHealth
    intent: Check service health and BORME freshness
    question: Is the OpenMercantil service up right now?
  - id: getStats
    intent: Get counts of published companies
    question: How many Spanish legal entities are published in the dataset?
  phrasing_ops: 2
  slug: openmercantil-system-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Authenticated Panel Pro endpoints — segments, lists, notes, tags, exports, audit. Requires session cookie (browser) and X-CSRF-Token header for mutations.
  name: OpenMercantil User API
  phrasing_intents:
  - id: getUserMe
    intent: Get my account profile and plan
    question: Which plan tier is my OpenMercantil account on?
  - id: getUserOrganization
    intent: Get my organization, seats and members
    question: Which team members and seats does my organization have?
  - id: createUserOrganization
    intent: Create an organization
    question: Can I set up a team organization on a MAX or Enterprise plan?
  - id: updateUserOrganization
    intent: Rename my organization
    question: How do I change the name of my organization?
  - id: createUserOrganizationInvite
    intent: Invite someone to my organization
    question: How do I invite a colleague to join my organization?
  - id: resendUserOrganizationInvite
    intent: Resend an organization invitation
    question: My colleague lost their invite email; can I send the organization invitation again?
  - id: deleteUserOrganizationInvite
    intent: Cancel a pending organization invitation
    question: How do I withdraw an invitation that hasn't been accepted yet?
  - id: updateUserOrganizationMember
    intent: Change a team member's role
    question: How do I promote a team member to admin?
  phrasing_ops: 65
  slug: openmercantil-user-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: 'Account outbound webhooks: register, update, rotate the HMAC signing secret and delete event subscriptions. Three subscribable event types; deliveries are signed and fail closed on unknown events.'
  name: OpenMercantil Webhooks API
  phrasing_intents:
  - id: listUserWebhooks
    intent: List my outbound webhooks
    question: Which webhooks have I set up on my account?
  - id: createUserWebhook
    intent: Create an outbound webhook
    question: How do I get notified at my own URL when registry events happen?
  - id: updateUserWebhook
    intent: Update an outbound webhook
    question: Can I change the URL or events of an existing webhook?
  - id: deleteUserWebhook
    intent: Delete an outbound webhook
    question: How do I remove a webhook I no longer need?
  - id: rotateUserWebhookSecret
    intent: Rotate a webhook signing secret
    question: How do I rotate the signing secret of a webhook?
  phrasing_ops: 5
  slug: openmercantil-webhooks-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Public procurement (PLACSP) rankings
  name: OpenMercantil Contracts API
  phrasing_intents:
  - id: getPersonContracts
    intent: List public contracts linked to a person
    question: Which public procurement contracts is a person associated with?
  - id: getTopCompaniesByContracts
    intent: Rank companies by public contract volume
    question: Which companies win the most public contracts?
  - id: getTopCompaniesByContractsCsv
    intent: Download the company contracts ranking as CSV
    question: Can I download the top companies by contracts as a CSV?
  - id: getTopPersonsByContracts
    intent: Rank persons by public contract volume
    question: Which people are linked to the most public procurement contracts?
  - id: getTopPersonsByContractsCsv
    intent: Download the persons contracts ranking as CSV
    question: Can I export the persons-by-contracts ranking to a spreadsheet?
  phrasing_ops: 5
  slug: openmercantil-contracts-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Daily BORME summary feeds
  name: OpenMercantil Daily API
  phrasing_intents:
  - id: getDaily
    intent: Get the BORME daily summary for a date
    question: What was published in the Spanish mercantile registry gazette (BORME) on a given day?
  - id: getSummaryForDate
    intent: Get a cross-source public-record summary for a date
    question: Is there a consolidated summary of public records for one day across BORME and the other integrated sources?
  phrasing_ops: 2
  slug: openmercantil-daily-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Bulk and per-resource export endpoints
  name: OpenMercantil Export API
  phrasing_intents:
  - id: exportCompany
    intent: Export a company report
    question: Can I download a full report on one company as JSON or CSV?
  - id: exportEvents
    intent: Bulk export BORME events for a year
    question: How do I bulk download all BORME events for a year?
  - id: getSectorStatsCsv
    intent: Download sector statistics as CSV
    question: Can I get the aggregate CNAE sector statistics as a CSV file?
  - id: getTopCompaniesByContractsCsv
    intent: Download top companies by public contracts as CSV
    question: Which companies win the most public contracts, as a CSV?
  - id: getTopPersonsByContractsCsv
    intent: Download top persons by public contracts as CSV
    question: Which people are linked to the most public contracts, as a downloadable CSV?
  phrasing_ops: 5
  slug: openmercantil-export-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Geolocation enrichment
  name: OpenMercantil Geocode API
  phrasing_intents:
  - id: geocodeCompany
    intent: Geocode a company's registered address
    question: Can I get latitude and longitude for a company's registered address?
  phrasing_ops: 1
  slug: openmercantil-geocode-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Company relationship network and embargoes
  name: OpenMercantil Network API
  phrasing_intents:
  - id: getCompanyNetwork
    intent: Get a company's officer and shareholder network
    question: Who are the officers and shareholders connected to a company?
  - id: getCompanyEmbargoes
    intent: List embargoes recorded against a company
    question: Have any seizures been recorded against a company?
  phrasing_ops: 2
  slug: openmercantil-network-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Documentary risk signals from public sources (AEPD, CNMC, concursos, AEAT moroso, CENDOJ)
  name: OpenMercantil Risk Signals API
  phrasing_intents:
  - id: getCompanyBySlugSanctions
    intent: Check a company against sanctions data
    question: Is a Spanish company on any sanctions list?
  - id: getCompanyBySlugRiskSignals
    intent: Get documentary risk signals for a company
    question: What risk signals are published for a Spanish company?
  - id: getCompanyBySlugAeatMoroso
    intent: Check if a company is on the AEAT debtor list
    question: Does a Spanish company appear on the tax agency's list of debtors?
  - id: getCompanyBySlugEmbargoes
    intent: List embargo mentions for a company
    question: Has a Spanish company had assets seized or embargoed according to public registries?
  phrasing_ops: 4
  slug: openmercantil-risk-signals-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Company score, trust score and activity timeseries
  name: OpenMercantil Score API
  phrasing_intents:
  - id: getCompanyScore
    intent: Get a company's composite score
    question: What is the OpenMercantil composite score for a Spanish company?
  - id: getCompanyActivity
    intent: Get a company's registry activity over time
    question: How active has a company been in the mercantile registry over time?
  - id: getCompanyTrustScore
    intent: Get a company's trust score
    question: How trustworthy does a company look once registry, procurement and sanctions signals are combined?
  phrasing_ops: 3
  slug: openmercantil-score-api
- baseURL: https://openmercantil.es
  baseurl_source: spec
  description: Aggregate statistics by region and sector
  name: OpenMercantil Stats API
  phrasing_intents:
  - id: getSectorStats
    intent: Get company statistics by sector
    question: How many companies are there per CNAE sector and how fast are they growing?
  - id: getSectorStatsCsv
    intent: Download sector statistics as CSV
    question: Can I download sector statistics as a CSV file?
  - id: getCcaaStats
    intent: Get company statistics by autonomous community
    question: How many companies are there in each Spanish autonomous community?
  phrasing_ops: 3
  slug: openmercantil-stats-api
artifact_total: 61
asyncapis:
- description: ''
  name: Openmercantil Webhooks
  slug: openmercantil-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenMercantil Public Billing API
  slug: open-openmercantil-billing-api
- collection_type: open
  name: OpenMercantil Public Billing Companies API
  slug: open-openmercantil-companies-api
- collection_type: open
  name: OpenMercantil Public Billing Contracts API
  slug: open-openmercantil-contracts-api
- collection_type: open
  name: OpenMercantil Public Billing Daily API
  slug: open-openmercantil-daily-api
- collection_type: open
  name: OpenMercantil Public Billing Export API
  slug: open-openmercantil-export-api
- collection_type: open
  name: OpenMercantil Public Billing Geocode API
  slug: open-openmercantil-geocode-api
- collection_type: open
  name: OpenMercantil Public Billing Network API
  slug: open-openmercantil-network-api
- collection_type: open
  name: OpenMercantil Public Billing Persons API
  slug: open-openmercantil-persons-api
- collection_type: open
  name: OpenMercantil Public Billing Score API
  slug: open-openmercantil-score-api
- collection_type: open
  name: OpenMercantil Public Billing Search API
  slug: open-openmercantil-search-api
- collection_type: open
  name: OpenMercantil Public Billing Sectors API
  slug: open-openmercantil-sectors-api
- collection_type: open
  name: OpenMercantil Public Billing Sources API
  slug: open-openmercantil-sources-api
- collection_type: open
  name: OpenMercantil Public Billing Stats API
  slug: open-openmercantil-stats-api
- collection_type: open
  name: OpenMercantil Public Billing System API
  slug: open-openmercantil-system-api
- collection_type: open
  name: OpenMercantil Public API
  slug: open-openmercantil
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/overlays/openmercantil-risk-signals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openmercantil-risk-signals-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/agentic-access/openmercantil-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openmercantil-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/security/openmercantil-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openmercantil-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/authentication/openmercantil-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openmercantil-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openmercantil.es/
- group: docs
  title: ''
  type: Documentation
  url: https://openmercantil.es/api/documentacion
- group: other
  title: ''
  type: APIsJSON
  url: https://openmercantil.es/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://openmercantil.es/precios
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openmercantil.es/terminos-de-uso
- group: operate
  title: ''
  type: Support
  url: https://openmercantil.es/soporte
- group: other
  title: ''
  type: Downloads
  url: https://openmercantil.es/descargas
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PabloCirre
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/json-schema/openmercantil-company-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/openmercantil-company-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/json-schema/openmercantil-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/openmercantil-event-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/json-structure/openmercantil-company-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/openmercantil-company-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/json-ld/openmercantil-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/openmercantil-context.jsonld
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/examples/openmercantil-search-companies-example.json
  title: ''
  type: Examples
  url: examples/openmercantil-search-companies-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/examples/openmercantil-get-company-example.json
  title: ''
  type: Examples
  url: examples/openmercantil-get-company-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/examples/openmercantil-get-company-events-example.json
  title: ''
  type: Examples
  url: examples/openmercantil-get-company-events-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/examples/openmercantil-health-example.json
  title: ''
  type: Examples
  url: examples/openmercantil-health-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/rules/openmercantil-rules.yml
  title: ''
  type: SpectralRuleset
  url: rules/openmercantil-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/vocabulary/openmercantil-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openmercantil-vocabulary.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/plans/openmercantil-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openmercantil-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/rate-limits/openmercantil-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openmercantil-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/finops/openmercantil-finops.yml
  title: ''
  type: FinOps
  url: finops/openmercantil-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://openmercantil.es/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/packages/openmercantil-packages.yml
  title: ''
  type: Packages
  url: packages/openmercantil-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/conventions/openmercantil-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openmercantil-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/conventions/openmercantil-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/openmercantil-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/errors/openmercantil-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openmercantil-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/lifecycle/openmercantil-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openmercantil-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://openmercantil.es/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/lifecycle/openmercantil-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/openmercantil-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/changelog/openmercantil-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openmercantil-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/conformance/openmercantil-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openmercantil-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/conformance/openmercantil-conformance.yml
  title: ''
  type: Compliance
  url: conformance/openmercantil-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/scopes/openmercantil-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/openmercantil-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/security/openmercantil-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/openmercantil-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/security/openmercantil-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/openmercantil-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/security/openmercantil-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/openmercantil-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/data-model/openmercantil-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openmercantil-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/asyncapi/openmercantil-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/openmercantil-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/llms/openmercantil-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openmercantil-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openmercantil.es/api
- group: docs
  title: ''
  type: APIReference
  url: https://openmercantil.es/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://openmercantil.es/api/documentacion
- group: docs
  title: ''
  type: OpenAPI
  url: https://openmercantil.es/openapi.json
- group: start
  title: ''
  type: SignUp
  url: https://openmercantil.es/mi-cuenta/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openmercantil.es/privacidad
- group: operate
  title: ''
  type: HelpCenter
  url: https://openmercantil.es/faq
created: '2026-05-09'
description: OpenMercantil is an independent public-data API for Spanish company intelligence. It indexes the Boletin Oficial del Registro Mercantil (BORME) and cross-references it with 80+ official public sources (BOE, CNMV, CNMC, AEAT, AEPD, PLACSP, TED EU, BDNS, OEPM, EPO, WIPO, CENDOJ, GLEIF, OpenSanctions, ICIJ and more) to expose company and person search, structured company reports, BORME registry event timelines, documentary officer mentions, CNAE sector navigation and ratios, daily BORME summaries, public-procurement notices and rankings, documentary risk signals, a corporate relationship graph, a Spanish mercantile-law corpus that bridges registry acts to the governing BOE norm, account-plane datasets and HMAC-signed outbound webhooks, and CSV/JSON bulk exports. The live OpenAPI 3.1 contract (v1.9.3) declares 118 paths and 139 operations. The public read plane is free and anonymous with no API key, rate-limited at 60 req/min and 200 req/day per IP, with paid Profesional, MAX and
  Enterprise tiers raising the quota. Derived data is CC BY 4.0 and every response carries its own source and attribution metadata. The project is informational and does not replace official Registro Mercantil certificates.
examples:
- key_count: 2
  name: Openmercantil Get Company Events Example
  slug: openmercantil-get-company-events-example
- key_count: 2
  name: Openmercantil Get Company Example
  slug: openmercantil-get-company-example
- key_count: 2
  name: Openmercantil Health Example
  slug: openmercantil-health-example
- key_count: 2
  name: Openmercantil Search Companies Example
  slug: openmercantil-search-companies-example
finops:
- name: Openmercantil Finops
  service_category: Open Data / Public Records
  slug: openmercantil-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openmercantil.png
json_schemas:
- name: OpenMercantil Company
  property_count: 13
  slug: openmercantil-company
- name: OpenMercantil Company Event
  property_count: 5
  slug: openmercantil-event
json_structures:
- name: Openmercantil Company Structure
  property_count: 13
  slug: openmercantil-company-structure
jsonld:
- class_count: 31
  name: Openmercantil Context
  property_count: 2
  slug: openmercantil-context
layout: provider
modified: '2026-08-14'
name: OpenMercantil
nav: Providers
network: true
overview: 'OpenMercantil publishes 25 APIs on the [APIs.io](https://apis.io/) network, including API Credentials API, Billing API, BORME API, and 22 more. Tagged areas include BDNS, BORME, Business Registry, CIF, and CNAE.


  The OpenMercantil catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  OpenMercantil''s developer surface includes authentication, documentation, pricing, support, code examples, changelog, API reference, and 44 more developer resources.'
plans:
- name: Openmercantil Plans Pricing
  plan_count: 4
  slug: openmercantil-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Openmercantil Rate Limits
  slug: openmercantil-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenMercantil API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openmercantil-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: OpenMercantil API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 4
  slug: openmercantil-rules
scopes:
- name: Openmercantil Scopes
  scope_count: 0
  slug: openmercantil-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 80.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 79.0
    catalog_earned_first_party: 24.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 70.8
    developer_ergonomics: 56.5
    discoverability: 69.6
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 80.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/screenshots/openmercantil-2026-06-20T191016.png
security:
- kind: authentication
  name: Openmercantil Authentication
  slug: openmercantil-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Openmercantil Domain Security
  slug: openmercantil-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Openmercantil Vulnerability Disclosure
  slug: openmercantil-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Openmercantil Trust Center
  slug: openmercantil-trust-center
  summary_line: trust center published
slug: openmercantil
tags:
- BDNS
- BORME
- Business Registry
- CIF
- CNAE
- CNMV
- CSV
- Company Data
- Company Search
- Corporate Registry
- DCAT-AP
- Daily Summary
- Geocoding
- JSON
- Legal Data
- Mercantile Law
- OEPM
- Open Data
- Open Government Data
- OpenAPI
- OpenSanctions
- PLACSP
- Public Procurement
- Public Records
- Public-Interest Data
- REST API
- Registry Timeline
- Risk Signals
- Sanctions
- Spain
- Spanish Companies
- Spanish Open Data
- Tenders
- Trust Score
- Webhook
website: https://openmercantil.es/
---
