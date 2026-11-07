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
  - scopes
  - security
  trial: true
  try_now: true
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Sp Global Agentic Access
  operation_count: 79
  slug: sp-global-agentic-access
  summary_line: 79 operations · 13 acting
api_count: 5
apis:
- baseURL: https://kfinance.kensho.com
  baseurl_source: declared
  description: REST API and Model Context Protocol server exposing S&P Capital IQ Financials, Market Data, Business Relationships, Earnings Call Transcripts, Company Intelligence, M&A Transactions, and Global Securi
  name: S&P Global LLM-Ready API (kFinance)
  phrasing_intents:
  - id: auditors_create
    intent: Look up a company's financial auditors
    question: Who audits this company's financial statements?
  phrasing_ops: 1
  slug: kensho-llm-ready-api
- baseURL: https://extract.kensho.com
  baseurl_source: declared
  description: 'Transforms unstructured PDF and image documents into machine-readable JSON, identifying titles, subtitles, paragraphs, tables, and footers in natural reading order. Optional OCR and Figure Extraction '
  name: Kensho Extract API
  phrasing_intents:
  - id: postV3Extractions
    intent: Submit a document directly for structured extraction
    question: How do I send a PDF straight to Kensho Extract and get its titles, paragraphs and tables back?
  - id: postV3ExtractionsUploadUrl
    intent: Get a pre-signed URL to upload a document for extraction
    question: Can I get a pre-signed upload link instead of attaching my document to the extraction request?
  - id: putV3ExtractionsUploadComplete
    intent: Start extraction after uploading to the pre-signed URL
    question: Why hasn't extraction started even though my file finished uploading to the pre-signed link?
  - id: getV3ExtractionsByRequestId
    intent: Retrieve the extracted document for a request
    question: Where do I fetch the structured output once my document has been extracted?
  - id: getV3ExtractionsDownloadUrlByRequestId
    intent: Get a download link for an extracted document
    question: Is there a file download link for a finished extraction rather than the inline response?
  phrasing_ops: 5
  slug: kensho-extract-api
- baseURL: https://nerd.kensho.com
  baseurl_source: declared
  description: Named-Entity Recognition and Disambiguation REST service linking text mentions to S&P Capital IQ company identifiers and to Wikimedia entities (people, places, events). Supports asynchronous batch ann
  name: Kensho NERD API
  phrasing_intents:
  - id: api_annotations_async_post
    intent: Submit text for asynchronous entity annotation
    question: How do I send a document's text to NERD and have entities linked to Capital IQ or Wikimedia?
  - id: api_annotations_async_put
    intent: Start annotating an uploaded text file
    question: I uploaded a text file through an upload URL - how do I tell NERD to start annotating it?
  - id: api_annotations_async_get
    intent: Fetch results of an entity annotation job
    question: Where can I pick up the entity annotations once my NERD job finishes?
  - id: api_annotations_async_delete
    intent: Delete the results of an annotation job
    question: Can I remove stored annotation results after I've downloaded them?
  phrasing_ops: 4
  slug: kensho-nerd-api
- baseURL: https://scribe.kensho.com
  baseurl_source: declared
  description: Asynchronous audio and video transcription REST API. POST a media file to start a transcription job, then poll the transcription ID for completion. Optimised for finance and business audio (earnings c
  name: Kensho Scribe Batch API v2
  phrasing_intents:
  - id: queryTranscription
    intent: Check a v1 transcription job's result
    question: Is my v1 transcription job still pending or finished?
  - id: startTranscription
    intent: Upload a file to the v1 transcription service
    question: How do I upload an MP3 directly to the v1 transcription endpoint?
  - id: deleteTranscription
    intent: Delete a v1 transcription job's data
    question: Can I delete all stored data for a v1 transcription job?
  - id: postApiV2Transcription
    intent: Start a transcription of audio or video
    question: Can I transcribe a recording hosted at a URL and get a callback when done?
  - id: headApiV2TranscriptionByTranscriptionId
    intent: Check if a transcript is ready to download
    question: Is my transcript ready to download yet?
  - id: downloadTranscription
    intent: Download a finished transcript
    question: Where do I download the transcript once my transcription completes?
  - id: deleteApiV2TranscriptionByTranscriptionId
    intent: Delete all data for a transcription
    question: Can I make sure a transcription's data is wiped from the system?
  phrasing_ops: 7
  slug: kensho-scribe-batch-v2-api
- baseURL: wss://scribe.kensho.com/ws
  baseurl_source: declared
  description: Real-time streaming transcription over a WebSocket at wss://scribe.kensho.com/ws. Clients send an Authenticate message with a Kensho OIDC access token, then StartTranscription with an audio_format (RA
  name: Kensho Scribe Real Time API
  slug: kensho-scribe-realtime-api
- baseURL: https://scribe.kensho.com
  baseurl_source: declared
  description: Legacy v1 batch transcription endpoint (POST /api/v1/transcription). Superseded by the v2 batch API which decouples submission from result retrieval. Documented here for customers on the v1 contract.
  name: Kensho Scribe Batch API v1
  phrasing_intents:
  - id: queryTranscription
    intent: Check a v1 transcription job's result
    question: Is my v1 transcription job still pending or finished?
  - id: startTranscription
    intent: Upload a file to the v1 transcription service
    question: How do I upload an MP3 directly to the v1 transcription endpoint?
  - id: deleteTranscription
    intent: Delete a v1 transcription job's data
    question: Can I delete all stored data for a v1 transcription job?
  - id: postApiV2Transcription
    intent: Start a transcription of audio or video
    question: Can I transcribe a recording hosted at a URL and get a callback when done?
  - id: headApiV2TranscriptionByTranscriptionId
    intent: Check if a transcript is ready to download
    question: Is my transcript ready to download yet?
  - id: downloadTranscription
    intent: Download a finished transcript
    question: Where do I download the transcript once my transcription completes?
  - id: deleteApiV2TranscriptionByTranscriptionId
    intent: Delete all data for a transcription
    question: Can I make sure a transcription's data is wiped from the system?
  phrasing_ops: 7
  slug: kensho-scribe-batch-v1-api
- description: Data retrieval service that translates natural-language queries into structured retrieval tasks across S&P Global AI-ready datasets. Returns answers with source citations linking back to the underlyin
  name: Kensho Grounding Agent (Alpha)
  slug: kensho-grounding-agent
- description: 'Flagship desktop and API platform for S&P Global Market Intelligence — company fundamentals, ownership, transactions, estimates, news, screening, charting, and Office plug-ins. The Capital IQ Pro API '
  name: S&P Capital IQ Pro
  slug: sp-capital-iq-pro
- description: Data and analytics catalog spanning S&P Global business units (Market Intelligence, Ratings, Commodity Insights/Platts, Mobility, Sustainable1, Indices, Dow Jones) plus third-party vendors. Distributi
  name: S&P Global Marketplace
  slug: sp-marketplace
- description: Comprehensive financial data API providing access to fundamental data, industry-specific and segment data, valuations and pricing, S&P Global Credit Ratings and Research, and reference and terms and c
  name: S&P Capital IQ Market Intelligence API
  slug: market-intelligence
- description: API providing programmatic access to the S&P Global Marketplace catalog of premium fundamental and alternative datasets. Enables discovery and integration of datasets available on the marketplace plat
  name: S&P Global Marketplace Catalog API
  slug: marketplace-catalog
- baseURL: https://kfinance.kensho.com
  baseurl_source: declared
  description: The Funding Rounds API from S&P Global — 2 operation(s) for funding rounds.
  name: S&P Global Funding Rounds API
  phrasing_intents:
  - id: fundingrounds_investor_retrieve
    intent: List funding rounds a company invested in
    question: Which funding rounds has this investor participated in?
  - id: fundingrounds_target_retrieve
    intent: List funding rounds a company raised
    question: What funding rounds has this startup raised?
  phrasing_ops: 2
  slug: sp-global-funding-rounds-api
artifact_total: 226
asyncapis:
- description: Real-time streaming transcription WebSocket API from Kensho Technologies (a wholly-owned S&P Global subsidiary). Companion to the Kensho Scribe v2 batch REST API. Streams uncompressed PCM audio chunks
  name: Kensho Scribe Real Time API
  slug: kensho-scribe-realtime-asyncapi
collections:
- collection_type: postman
  name: Kensho Extract API
  slug: postman-kensho-extract
- collection_type: postman
  name: LLM-ready API
  slug: postman-kensho-llmready
- collection_type: postman
  name: NERD Service API
  slug: postman-kensho-nerd
- collection_type: postman
  name: Scribe Batch API
  slug: postman-kensho-scribe-batch-v1
- collection_type: postman
  name: Scribe Batch API
  slug: postman-kensho-scribe-batch-v2
- collection_type: postman
  name: Kensho Extract annotations-async API
  slug: postman-sp-global-annotations-async-api
- collection_type: postman
  name: Kensho Extract annotations-async Auditors API
  slug: postman-sp-global-auditors-api
- collection_type: postman
  name: Kensho Extract annotations-async Ciqpro API
  slug: postman-sp-global-ciqpro-api
- collection_type: postman
  name: Kensho Extract annotations-async Company Groups API
  slug: postman-sp-global-company-groups-api
- collection_type: postman
  name: Kensho Extract annotations-async Competitors API
  slug: postman-sp-global-competitors-api
- collection_type: postman
  name: Kensho Extract annotations-async Cusip API
  slug: postman-sp-global-cusip-api
- collection_type: postman
  name: Kensho Extract annotations-async Earnings API
  slug: postman-sp-global-earnings-api
- collection_type: postman
  name: Kensho Extract annotations-async Estimates API
  slug: postman-sp-global-estimates-api
- collection_type: postman
  name: Kensho Extract annotations-async Extractions API
  slug: postman-sp-global-extractions-api
- collection_type: postman
  name: Kensho Extract annotations-async Fundinground API
  slug: postman-sp-global-fundinground-api
- collection_type: postman
  name: Kensho Extract annotations-async Fundingrounds API
  slug: postman-sp-global-fundingrounds-api
- collection_type: postman
  name: Kensho Extract annotations-async Id API
  slug: postman-sp-global-id-api
- collection_type: postman
  name: Kensho Extract annotations-async Ids API
  slug: postman-sp-global-ids-api
- collection_type: postman
  name: Kensho Extract annotations-async Info API
  slug: postman-sp-global-info-api
- collection_type: postman
  name: Kensho Extract annotations-async Isin API
  slug: postman-sp-global-isin-api
- collection_type: postman
  name: Kensho Extract annotations-async Latest API
  slug: postman-sp-global-latest-api
- collection_type: postman
  name: Kensho Extract annotations-async Line Item API
  slug: postman-sp-global-line-item-api
- collection_type: postman
  name: Kensho Extract annotations-async Market Cap API
  slug: postman-sp-global-market-cap-api
- collection_type: postman
  name: Kensho Extract annotations-async Merger API
  slug: postman-sp-global-merger-api
- collection_type: postman
  name: Kensho Extract annotations-async Mergers API
  slug: postman-sp-global-mergers-api
- collection_type: postman
  name: Kensho Extract annotations-async Price Chart API
  slug: postman-sp-global-price-chart-api
- collection_type: postman
  name: Kensho Extract annotations-async Pricing API
  slug: postman-sp-global-pricing-api
- collection_type: postman
  name: Kensho Extract annotations-async Relationship API
  slug: postman-sp-global-relationship-api
- collection_type: postman
  name: Kensho Extract annotations-async Securities API
  slug: postman-sp-global-securities-api
- collection_type: postman
  name: Kensho Extract annotations-async Segments API
  slug: postman-sp-global-segments-api
- collection_type: postman
  name: Kensho Extract annotations-async Statements API
  slug: postman-sp-global-statements-api
- collection_type: postman
  name: Kensho Extract annotations-async Ticker Groups API
  slug: postman-sp-global-ticker-groups-api
- collection_type: postman
  name: Kensho Extract annotations-async Trading Item Groups API
  slug: postman-sp-global-trading-item-groups-api
- collection_type: postman
  name: Kensho Extract annotations-async Trading Items API
  slug: postman-sp-global-trading-items-api
- collection_type: postman
  name: Kensho Extract annotations-async Transcript API
  slug: postman-sp-global-transcript-api
- collection_type: postman
  name: Kensho Extract annotations-async Transcription API
  slug: postman-sp-global-transcription-api
- collection_type: postman
  name: Kensho Extract annotations-async upload-url API
  slug: postman-sp-global-upload-url-api
- collection_type: postman
  name: Kensho Extract annotations-async user-info API
  slug: postman-sp-global-user-info-api
- collection_type: postman
  name: Kensho Extract annotations-async Users API
  slug: postman-sp-global-users-api
- collection_type: open
  name: Kensho Extract API
  slug: open-kensho-extract
- collection_type: open
  name: LLM-ready API
  slug: open-kensho-llmready
- collection_type: open
  name: NERD Service API
  slug: open-kensho-nerd
- collection_type: open
  name: Scribe Batch API
  slug: open-kensho-scribe-batch-v1
- collection_type: open
  name: Scribe Batch API
  slug: open-kensho-scribe-batch-v2
- collection_type: open
  name: Kensho Extract annotations-async API
  slug: open-sp-global-annotations-async-api
- collection_type: open
  name: Kensho Extract annotations-async Auditors API
  slug: open-sp-global-auditors-api
- collection_type: open
  name: Kensho Extract annotations-async Ciqpro API
  slug: open-sp-global-ciqpro-api
- collection_type: open
  name: Kensho Extract annotations-async Company Groups API
  slug: open-sp-global-company-groups-api
- collection_type: open
  name: Kensho Extract annotations-async Competitors API
  slug: open-sp-global-competitors-api
- collection_type: open
  name: Kensho Extract annotations-async Cusip API
  slug: open-sp-global-cusip-api
- collection_type: open
  name: Kensho Extract annotations-async Earnings API
  slug: open-sp-global-earnings-api
- collection_type: open
  name: Kensho Extract annotations-async Estimates API
  slug: open-sp-global-estimates-api
- collection_type: open
  name: Kensho Extract annotations-async Extractions API
  slug: open-sp-global-extractions-api
- collection_type: open
  name: Kensho Extract annotations-async Fundinground API
  slug: open-sp-global-fundinground-api
- collection_type: open
  name: Kensho Extract annotations-async Fundingrounds API
  slug: open-sp-global-fundingrounds-api
- collection_type: open
  name: Kensho Extract annotations-async Id API
  slug: open-sp-global-id-api
- collection_type: open
  name: Kensho Extract annotations-async Ids API
  slug: open-sp-global-ids-api
- collection_type: open
  name: Kensho Extract annotations-async Info API
  slug: open-sp-global-info-api
- collection_type: open
  name: Kensho Extract annotations-async Isin API
  slug: open-sp-global-isin-api
- collection_type: open
  name: Kensho Extract annotations-async Latest API
  slug: open-sp-global-latest-api
- collection_type: open
  name: Kensho Extract annotations-async Line Item API
  slug: open-sp-global-line-item-api
- collection_type: open
  name: Kensho Extract annotations-async Market Cap API
  slug: open-sp-global-market-cap-api
- collection_type: open
  name: Kensho Extract annotations-async Merger API
  slug: open-sp-global-merger-api
- collection_type: open
  name: Kensho Extract annotations-async Mergers API
  slug: open-sp-global-mergers-api
- collection_type: open
  name: Kensho Extract annotations-async Price Chart API
  slug: open-sp-global-price-chart-api
- collection_type: open
  name: Kensho Extract annotations-async Pricing API
  slug: open-sp-global-pricing-api
- collection_type: open
  name: Kensho Extract annotations-async Relationship API
  slug: open-sp-global-relationship-api
- collection_type: open
  name: Kensho Extract annotations-async Securities API
  slug: open-sp-global-securities-api
- collection_type: open
  name: Kensho Extract annotations-async Segments API
  slug: open-sp-global-segments-api
- collection_type: open
  name: Kensho Extract annotations-async Statements API
  slug: open-sp-global-statements-api
- collection_type: open
  name: Kensho Extract annotations-async Ticker Groups API
  slug: open-sp-global-ticker-groups-api
- collection_type: open
  name: Kensho Extract annotations-async Trading Item Groups API
  slug: open-sp-global-trading-item-groups-api
- collection_type: open
  name: Kensho Extract annotations-async Trading Items API
  slug: open-sp-global-trading-items-api
- collection_type: open
  name: Kensho Extract annotations-async Transcript API
  slug: open-sp-global-transcript-api
- collection_type: open
  name: Kensho Extract annotations-async Transcription API
  slug: open-sp-global-transcription-api
- collection_type: open
  name: Kensho Extract annotations-async upload-url API
  slug: open-sp-global-upload-url-api
- collection_type: open
  name: Kensho Extract annotations-async user-info API
  slug: open-sp-global-user-info-api
- collection_type: open
  name: Kensho Extract annotations-async Users API
  slug: open-sp-global-users-api
common:
- group: other
  href: https://artifacts.apis.io/sp-global/capabilities/sp-global-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sp-global-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sp-global/overview
- group: agent
  href: https://artifacts.apis.io/sp-global/agentic-access/sp-global-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sp-global-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sp-global/security/sp-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sp-global-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sp-global/authentication/sp-global-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sp-global-authentication.yml
- group: start
  title: S&P Global Developer Portal (root)
  type: Portal
  url: https://developer.spglobal.com
- group: docs
  title: Kensho Documentation (canonical S&P Global API docs)
  type: Documentation
  url: https://docs.kensho.com
- group: other
  title: S&P Global Marketplace
  type: Marketplace
  url: https://www.marketplace.spglobal.com
- group: auth
  title: OIDC / OAuth 2.0 with keypair or refresh-token grants
  type: Authentication
  url: https://docs.kensho.com/authentication
- group: build
  title: kensho-kfinance Python library
  type: SDKs
  url: https://pypi.org/project/kensho-kfinance/
- group: build
  title: kFinance Python library source
  type: SDKs
  url: https://github.com/kensho-technologies/kfinance
- group: build
  title: S&P Global Plugin (Claude Cowork skills)
  type: SDKs
  url: https://github.com/kensho-technologies/spglobal-agent-skills
- group: build
  title: LLM-ready API example notebooks
  type: CodeExamples
  url: https://github.com/kensho-technologies/llm-ready-api-examples
- group: build
  title: Kensho Technologies GitHub organization (S&P Global AI subsidiary)
  type: GitHub
  url: https://github.com/kensho-technologies
- group: build
  title: SP-Global GitHub organization (currently no public repos)
  type: GitHub
  url: https://github.com/SP-Global
- group: company
  title: S&P Global Research & Insights
  type: Blog
  url: https://www.spglobal.com/en/research-insights
- group: company
  title: Kensho Blog
  type: Blog
  url: https://kensho.com/blog
- group: commercial
  href: https://artifacts.apis.io/sp-global/plans/sp-global-plans-pricing.yml
  title: S&P Global / Kensho API Plans (API Commons Plans 0.1)
  type: Plans
  url: plans/sp-global-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sp-global/rate-limits/sp-global-rate-limits.yml
  title: S&P Global / Kensho API Rate Limits (API Commons Rate Limits 0.1)
  type: RateLimits
  url: rate-limits/sp-global-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sp-global/finops/sp-global-finops.yml
  title: S&P Global / Kensho API FinOps mapping (FOCUS aligned)
  type: FinOps
  url: finops/sp-global-finops.yml
- group: design
  href: https://artifacts.apis.io/sp-global/json-ld/sp-global-context.jsonld
  title: S&P Global JSON-LD context
  type: JSONLD
  url: json-ld/sp-global-context.jsonld
- group: docs
  href: https://artifacts.apis.io/sp-global/json-schema/kensho-llmready-company-info-schema.json
  title: LLM-ready API Company Info JSON Schema
  type: JSONSchema
  url: json-schema/kensho-llmready-company-info-schema.json
- group: docs
  href: https://artifacts.apis.io/sp-global/json-schema/kensho-extract-extraction-schema.json
  title: Kensho Extract Extraction JSON Schema
  type: JSONSchema
  url: json-schema/kensho-extract-extraction-schema.json
- group: docs
  href: https://artifacts.apis.io/sp-global/json-schema/kensho-nerd-annotation-schema.json
  title: Kensho NERD Annotation JSON Schema
  type: JSONSchema
  url: json-schema/kensho-nerd-annotation-schema.json
- group: design
  href: https://artifacts.apis.io/sp-global/vocabulary/sp-global-vocabulary.yml
  title: S&P Global vocabulary
  type: Vocabulary
  url: vocabulary/sp-global-vocabulary.yml
- group: other
  title: ''
  type: Subsidiaries
  url: ''
- group: build
  href: https://artifacts.apis.io/sp-global/packages/sp-global-packages.yml
  title: First-party packages (kensho-kfinance on PyPI)
  type: Packages
  url: packages/sp-global-packages.yml
- group: agent
  href: https://artifacts.apis.io/sp-global/well-known/sp-global-well-known.yml
  title: Well-known probe index (RFC 8414 + RFC 9728 metadata on kfinance.kensho.com)
  type: WellKnown
  url: well-known/sp-global-well-known.yml
- group: agent
  href: https://artifacts.apis.io/sp-global/mcp/sp-global-mcp.yml
  title: Hosted kFinance MCP server manifest (https://kfinance.kensho.com/integrations/mcp)
  type: MCPServer
  url: mcp/sp-global-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sp-global/llms/sp-global-llms.txt
  title: Generated llms.txt for the S&P Global / Kensho API surface
  type: LLMsTxt
  url: llms/sp-global-llms.txt
- group: auth
  href: https://artifacts.apis.io/sp-global/scopes/sp-global-scopes.yml
  title: OAuth scopes (from live RFC 8414 metadata)
  type: OAuthScopes
  url: scopes/sp-global-scopes.yml
- group: design
  href: https://artifacts.apis.io/sp-global/conformance/sp-global-conformance.yml
  title: Standards conformance (OAuth2/OIDC/PKCE/MCP/RFC 8414/9728)
  type: Conformance
  url: conformance/sp-global-conformance.yml
- group: design
  href: https://artifacts.apis.io/sp-global/errors/sp-global-problem-types.yml
  title: Error catalog derived from OpenAPI 4xx/5xx responses
  type: ErrorCatalog
  url: errors/sp-global-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sp-global/lifecycle/sp-global-lifecycle.yml
  title: Versioning, supersession, and status-page lifecycle profile
  type: Lifecycle
  url: lifecycle/sp-global-lifecycle.yml
- group: operate
  title: Kensho status page (Atlassian Statuspage)
  type: StatusPage
  url: https://status.kensho.com
- group: operate
  href: https://artifacts.apis.io/sp-global/changelog/sp-global-changelog.yml
  title: kensho-kfinance changelog (semver, current 7.0.2)
  type: ChangeLog
  url: changelog/sp-global-changelog.yml
- group: design
  href: https://artifacts.apis.io/sp-global/conventions/sp-global-conventions.yml
  title: Cross-cutting API conventions (auth, batching, async jobs, errors)
  type: Conventions
  url: conventions/sp-global-conventions.yml
- group: design
  href: https://artifacts.apis.io/sp-global/data-model/sp-global-data-model.yml
  title: Capital IQ identification-triple entity graph
  type: DataModel
  url: data-model/sp-global-data-model.yml
- group: agent
  href: https://artifacts.apis.io/sp-global/skills/_index.yml
  title: S&P Global Plugin Agent Skills (provider-published, saved verbatim)
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/sp-global/collections/kensho-llmready.postman_collection.json
  title: Postman collection for the LLM-Ready API (repo artifact)
  type: PostmanCollection
  url: collections/kensho-llmready.postman_collection.json
- group: build
  href: https://artifacts.apis.io/sp-global/examples/kensho-llmready-get-company-information-example.json
  title: ''
  type: Examples
  url: examples/kensho-llmready-get-company-information-example.json
- group: build
  href: https://artifacts.apis.io/sp-global/examples/kensho-llmready-get-financial-statement-example.json
  title: ''
  type: Examples
  url: examples/kensho-llmready-get-financial-statement-example.json
- group: build
  href: https://artifacts.apis.io/sp-global/examples/kensho-extract-post-v3-extractions-example.json
  title: ''
  type: Examples
  url: examples/kensho-extract-post-v3-extractions-example.json
- group: start
  title: S&P Global Marketplace sign-up
  type: SignUp
  url: https://www.marketplace.spglobal.com/en/sign-up
- group: operate
  title: S&P Global Market Intelligence contact
  type: Support
  url: https://www.spglobal.com/market-intelligence/en/contact-us
- group: commercial
  title: S&P Global Corporate Privacy Policy
  type: PrivacyPolicy
  url: https://www.spglobal.com/en/privacy/privacy-policy-english
- group: commercial
  title: S&P Global Terms of Use
  type: TermsOfService
  url: https://www.spglobal.com/en/terms-of-use
- group: company
  title: ''
  type: Website
  url: https://www.spglobal.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spglobal.com/commodityinsights/api/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.spglobal.com/en/research-insights/articles
created: '2026-05-23'
description: S&P Global (NYSE SPGI) is the parent of S&P Global Ratings, S&P Global Market Intelligence, S&P Dow Jones Indices, S&P Global Commodity Insights (Platts), S&P Global Mobility, and S&P Global Sustainable1. Its public developer surface is anchored by Kensho Technologies (a wholly-owned S&P Global AI subsidiary) which ships REST APIs for the S&P Global LLM-ready API (kFinance), Extract, NERD, Scribe, and the Grounding Agent, plus the S&P Capital IQ Pro and Marketplace data products distributed through the S&P Global Marketplace.
examples:
- key_count: 6
  name: Kensho Extract Get V3 Extractions Download Url Request Id Example
  slug: kensho-extract-get-v3-extractions-download-url-request-id-example
- key_count: 6
  name: Kensho Extract Get V3 Extractions Request Id Example
  slug: kensho-extract-get-v3-extractions-request-id-example
- key_count: 6
  name: Kensho Extract Post V3 Extractions Example
  slug: kensho-extract-post-v3-extractions-example
- key_count: 6
  name: Kensho Extract Post V3 Extractions Upload Url Example
  slug: kensho-extract-post-v3-extractions-upload-url-example
- key_count: 6
  name: Kensho Extract Put V3 Extractions Upload Complete Example
  slug: kensho-extract-put-v3-extractions-upload-complete-example
- key_count: 6
  name: Kensho Llmready Auditors Create Example
  slug: kensho-llmready-auditors-create-example
- key_count: 6
  name: Kensho Llmready Ciqpro Retrieve Example
  slug: kensho-llmready-ciqpro-retrieve-example
- key_count: 6
  name: Kensho Llmready Cusip To Identification Triple Example
  slug: kensho-llmready-cusip-to-identification-triple-example
- key_count: 6
  name: Kensho Llmready Fundinground Info Advisors Investor Retrieve Example
  slug: kensho-llmready-fundinground-info-advisors-investor-retrieve-example
- key_count: 6
  name: Kensho Llmready Fundinground Info Advisors Target Retrieve Example
  slug: kensho-llmready-fundinground-info-advisors-target-retrieve-example
- key_count: 6
  name: Kensho Llmready Fundinground Info Retrieve Example
  slug: kensho-llmready-fundinground-info-retrieve-example
- key_count: 6
  name: Kensho Llmready Fundingrounds Investor Retrieve Example
  slug: kensho-llmready-fundingrounds-investor-retrieve-example
- key_count: 6
  name: Kensho Llmready Fundingrounds Target Retrieve Example
  slug: kensho-llmready-fundingrounds-target-retrieve-example
- key_count: 6
  name: Kensho Llmready Get Analyst Recommendations Example
  slug: kensho-llmready-get-analyst-recommendations-example
- key_count: 6
  name: Kensho Llmready Get Companies By Business Relationships Example
  slug: kensho-llmready-get-companies-by-business-relationships-example
- key_count: 6
  name: Kensho Llmready Get Companies By Gics Code Example
  slug: kensho-llmready-get-companies-by-gics-code-example
- key_count: 6
  name: Kensho Llmready Get Companies By Industry Code Example
  slug: kensho-llmready-get-companies-by-industry-code-example
- key_count: 6
  name: Kensho Llmready Get Companies By Location Example
  slug: kensho-llmready-get-companies-by-location-example
- key_count: 6
  name: Kensho Llmready Get Companies By Simple Industry Example
  slug: kensho-llmready-get-companies-by-simple-industry-example
- key_count: 6
  name: Kensho Llmready Get Company Information Example
  slug: kensho-llmready-get-company-information-example
- key_count: 6
  name: Kensho Llmready Get Competitors From Company 2 Example
  slug: kensho-llmready-get-competitors-from-company-2-example
- key_count: 6
  name: Kensho Llmready Get Competitors From Company Example
  slug: kensho-llmready-get-competitors-from-company-example
- key_count: 6
  name: Kensho Llmready Get Consensus Target Price Example
  slug: kensho-llmready-get-consensus-target-price-example
- key_count: 6
  name: Kensho Llmready Get Cusip Example
  slug: kensho-llmready-get-cusip-example
- key_count: 6
  name: Kensho Llmready Get Earnings Calls Dates Example
  slug: kensho-llmready-get-earnings-calls-dates-example
- key_count: 6
  name: Kensho Llmready Get Earnings Calls Example
  slug: kensho-llmready-get-earnings-calls-example
- key_count: 6
  name: Kensho Llmready Get Estimates Example
  slug: kensho-llmready-get-estimates-example
- key_count: 6
  name: Kensho Llmready Get Financial Line Item 2 Example
  slug: kensho-llmready-get-financial-line-item-2-example
- key_count: 6
  name: Kensho Llmready Get Financial Line Item Example
  slug: kensho-llmready-get-financial-line-item-example
- key_count: 6
  name: Kensho Llmready Get Financial Statement 2 Example
  slug: kensho-llmready-get-financial-statement-2-example
- key_count: 6
  name: Kensho Llmready Get Financial Statement Example
  slug: kensho-llmready-get-financial-statement-example
- key_count: 6
  name: Kensho Llmready Get Historical Metadata Example
  slug: kensho-llmready-get-historical-metadata-example
- key_count: 6
  name: Kensho Llmready Get Isin Example
  slug: kensho-llmready-get-isin-example
- key_count: 6
  name: Kensho Llmready Get Latest Date Example
  slug: kensho-llmready-get-latest-date-example
- key_count: 6
  name: Kensho Llmready Get Market Caps Example
  slug: kensho-llmready-get-market-caps-example
- key_count: 6
  name: Kensho Llmready Get Price Chart Example
  slug: kensho-llmready-get-price-chart-example
- key_count: 6
  name: Kensho Llmready Get Primary Security Example
  slug: kensho-llmready-get-primary-security-example
- key_count: 6
  name: Kensho Llmready Get Primary Trading Item Example
  slug: kensho-llmready-get-primary-trading-item-example
- key_count: 6
  name: Kensho Llmready Get Raw Transcript Example
  slug: kensho-llmready-get-raw-transcript-example
- key_count: 6
  name: Kensho Llmready Get Securities Example
  slug: kensho-llmready-get-securities-example
- key_count: 6
  name: Kensho Llmready Get Segments 2 Example
  slug: kensho-llmready-get-segments-2-example
- key_count: 6
  name: Kensho Llmready Get Segments Example
  slug: kensho-llmready-get-segments-example
- key_count: 6
  name: Kensho Llmready Get Stock Prices Example
  slug: kensho-llmready-get-stock-prices-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Business Relationships Example
  slug: kensho-llmready-get-tickers-by-business-relationships-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Combined Filters Example
  slug: kensho-llmready-get-tickers-by-combined-filters-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Exchange Code Example
  slug: kensho-llmready-get-tickers-by-exchange-code-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Gics Code Example
  slug: kensho-llmready-get-tickers-by-gics-code-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Industry Code Example
  slug: kensho-llmready-get-tickers-by-industry-code-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Location 2 Example
  slug: kensho-llmready-get-tickers-by-location-2-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Location Example
  slug: kensho-llmready-get-tickers-by-location-example
- key_count: 6
  name: Kensho Llmready Get Tickers By Simple Industry Example
  slug: kensho-llmready-get-tickers-by-simple-industry-example
- key_count: 6
  name: Kensho Llmready Get Trading Items By Exchange Code Example
  slug: kensho-llmready-get-trading-items-by-exchange-code-example
- key_count: 6
  name: Kensho Llmready Get Trading Items Example
  slug: kensho-llmready-get-trading-items-example
- key_count: 6
  name: Kensho Llmready Get Transcript Example
  slug: kensho-llmready-get-transcript-example
- key_count: 6
  name: Kensho Llmready Info Descriptions Retrieve Example
  slug: kensho-llmready-info-descriptions-retrieve-example
- key_count: 6
  name: Kensho Llmready Info Names Retrieve Example
  slug: kensho-llmready-info-names-retrieve-example
- key_count: 6
  name: Kensho Llmready Isin To Identification Triple Example
  slug: kensho-llmready-isin-to-identification-triple-example
- key_count: 6
  name: Kensho Llmready Merger Info Advisors Retrieve Example
  slug: kensho-llmready-merger-info-advisors-retrieve-example
- key_count: 6
  name: Kensho Llmready Merger Info Retrieve Example
  slug: kensho-llmready-merger-info-retrieve-example
- key_count: 6
  name: Kensho Llmready Mergers Retrieve Example
  slug: kensho-llmready-mergers-retrieve-example
- key_count: 6
  name: Kensho Llmready Refresh Access Token 2 Example
  slug: kensho-llmready-refresh-access-token-2-example
- key_count: 6
  name: Kensho Llmready Refresh Access Token Example
  slug: kensho-llmready-refresh-access-token-example
- key_count: 6
  name: Kensho Llmready Ticker To Identification Triple 2 Example
  slug: kensho-llmready-ticker-to-identification-triple-2-example
- key_count: 6
  name: Kensho Llmready Ticker To Identification Triple Example
  slug: kensho-llmready-ticker-to-identification-triple-example
- key_count: 6
  name: Kensho Llmready Unified Identification Triple Example
  slug: kensho-llmready-unified-identification-triple-example
- key_count: 6
  name: Kensho Llmready Users Permissions Retrieve Example
  slug: kensho-llmready-users-permissions-retrieve-example
- key_count: 6
  name: Kensho Nerd Api Annotations Async Delete Example
  slug: kensho-nerd-api-annotations-async-delete-example
- key_count: 6
  name: Kensho Nerd Api Annotations Async Get Example
  slug: kensho-nerd-api-annotations-async-get-example
- key_count: 6
  name: Kensho Nerd Api Annotations Async Post Example
  slug: kensho-nerd-api-annotations-async-post-example
- key_count: 6
  name: Kensho Nerd Api Annotations Async Put Example
  slug: kensho-nerd-api-annotations-async-put-example
- key_count: 6
  name: Kensho Nerd Api Annotations Upload Url Example
  slug: kensho-nerd-api-annotations-upload-url-example
- key_count: 6
  name: Kensho Nerd Me Get Example
  slug: kensho-nerd-me-get-example
- key_count: 6
  name: Kensho Scribe V2 Deletetranscription Example
  slug: kensho-scribe-v2-deletetranscription-example
- key_count: 6
  name: Kensho Scribe V2 Downloadtranscription Example
  slug: kensho-scribe-v2-downloadtranscription-example
- key_count: 6
  name: Kensho Scribe V2 Starttranscription Example
  slug: kensho-scribe-v2-starttranscription-example
features:
- 5 public REST OpenAPI surfaces (LLM-ready, Extract, NERD, Scribe v1 batch, Scribe v2 batch)
- 71 documented REST endpoints across the 5 specs (60 LLM-ready, 5 Extract, 3 NERD, 1 Scribe v1, 2 Scribe v2)
- MCP server for the LLM-ready API with stdio, SSE, and streamable-http transports
- Claude Cowork plugin shipping tearsheets, funding digests, and earnings preview skills
- kensho-kfinance Python SDK on PyPI with LangChain/OpenAI/Anthropic/Gemini examples
- OIDC authentication with keypair (production) or refresh token (development) flows
- Distribution via Snowflake and Databricks marketplace shares in addition to direct REST
- Capital IQ database back-end powering financial entity disambiguation across products
- Real-time WebSocket transcription companion to the Scribe batch APIs
- Grounding Agent (Alpha) for retrieval-with-citations over AI-ready datasets
finops:
- has_sources: false
  method: generated
  name: Sp Global Finops
  primary_unit: ''
  service_category: ''
  slug: sp-global-finops
  template: true
image: https://www.spglobal.com/spglobal-corporate-identity/spglobal-logo.svg
integrations:
- description: First-class Claude Desktop, Claude Cowork, and Claude Code MCP integrations including the S&P Global Plugin.
  name: Claude (Anthropic)
- description: MCP connector documented under llmreadyapi/mcp/third-party/chatgpt; code-generation and function-calling notebooks for OpenAI models.
  name: ChatGPT (OpenAI)
- description: Documented MCP third-party integration path for enterprise Copilot deployments.
  name: Microsoft Copilot Studio
- description: Documented MCP integration for AWS-hosted GenAI workflows.
  name: Amazon QuickSuite
- description: MCP integration plus Databricks marketplace shares for AI-ready data distribution.
  name: Databricks
- description: MCP integration in beta for Mistral-hosted agents.
  name: Mistral (Beta)
- description: Function-calling notebooks under llm-ready-api-examples wrap kFinance tools as LangChain tools across OpenAI, Anthropic, and Google Gemini providers.
  name: LangChain
- description: Distribution channel for S&P Global Marketplace datasets via Snowflake data sharing.
  name: Snowflake Marketplace
json_schemas:
- name: Kensho Extract Extraction
  property_count: 3
  slug: kensho-extract-extraction
- name: Kensho LLM-ready API Analyst Recommendation
  property_count: 2
  slug: kensho-llmready-analyst-recommendation
- name: Kensho LLM-ready API Auditor
  property_count: 2
  slug: kensho-llmready-auditor
- name: Kensho LLM-ready API Company Info
  property_count: 13
  slug: kensho-llmready-company-info
- name: Kensho LLM-ready API Cusip
  property_count: 1
  slug: kensho-llmready-cusip
- name: Kensho LLM-ready API Earnings
  property_count: 3
  slug: kensho-llmready-earnings
- name: Kensho LLM-ready API Estimate
  property_count: 3
  slug: kensho-llmready-estimate
- name: Kensho NERD Annotation
  property_count: 4
  slug: kensho-nerd-annotation
- name: Kensho Scribe Transcription
  property_count: 5
  slug: kensho-scribe-transcription
json_structures:
- name: Kensho Extract Extraction Structure
  property_count: 0
  slug: kensho-extract-extraction-structure
- name: Kensho Llmready Analyst Recommendation Structure
  property_count: 0
  slug: kensho-llmready-analyst-recommendation-structure
- name: Kensho Llmready Auditor Structure
  property_count: 0
  slug: kensho-llmready-auditor-structure
- name: Kensho Llmready Company Info Structure
  property_count: 0
  slug: kensho-llmready-company-info-structure
- name: Kensho Llmready Cusip Structure
  property_count: 0
  slug: kensho-llmready-cusip-structure
- name: Kensho Llmready Earnings Structure
  property_count: 0
  slug: kensho-llmready-earnings-structure
- name: Kensho Llmready Estimate Structure
  property_count: 0
  slug: kensho-llmready-estimate-structure
- name: Kensho Nerd Annotation Structure
  property_count: 0
  slug: kensho-nerd-annotation-structure
- name: Kensho Scribe Transcription Structure
  property_count: 0
  slug: kensho-scribe-transcription-structure
jsonld:
- class_count: 20
  name: Sp Global Context
  property_count: 67
  slug: sp-global-context
layout: provider
mcp_servers:
- description: ''
  name: kFinance MCP server (stdio, SSE, streamable-http transports)
  slug: kfinance-mcp-server-stdio-sse-streamable-http-transports
- description: 'Hosted (remote) MCP server for the S&P Global LLM-Ready API (kFinance), operated by Kensho. Documented first-class integrations: Claude (Desktop/Cowork/Code), ChatGPT, Microsoft Copilot Studio, Amazon'
  name: Hosted kFinance MCP server manifest (https://kfinance.kensho.com/integrations/mcp)
  slug: spglobal-kfinance
modified: '2026-07-22'
name: S&P Global
nav: Providers
network: true
overview: 'S&P Global publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including LLM-Ready API (kFinance), Kensho Extract API, Kensho NERD API, and 9 more. Tagged areas include Capital IQ, Commodity Insights, Credit Ratings, Document Extraction, and ESG.


  The S&P Global catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  S&P Global''s developer surface includes authentication, developer portal, documentation, code examples, GitHub presence, engineering blog, changelog, and 42 more developer resources.'
plans:
- name: Sp Global Plans Pricing
  plan_count: 7
  slug: sp-global-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sp Global Rate Limits
  slug: sp-global-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: S&P Global — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: sp-global-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: S&P Global — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: sp-global-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: S&P Global API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 7
  slug: sp-global-rules
scopes:
- name: Sp Global Scopes
  scope_count: 2
  slug: sp-global-scopes
  summary_line: 2 scopes · authorizationCode/refresh_token
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 45.5
    contract_quality: 68.4
    developer_ergonomics: 89.3
    discoverability: 71.7
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sp-global/sp-global-2026-06-20T194233.png
security:
- kind: authentication
  name: Sp Global Authentication
  slug: sp-global-authentication
  summary_line: http/oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Sp Global Domain Security
  slug: sp-global-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 4
skills:
- name: earnings-preview-single
  slug: sp-global-earnings-preview-beta
- name: funding-digest
  slug: sp-global-funding-digest
- name: sp-capital-iq-excel-pro
  slug: sp-global-sp-capital-iq-excel-pro
- name: tear-sheet
  slug: sp-global-tear-sheet
slug: sp-global
tags:
- Capital IQ
- Commodity Insights
- Credit Ratings
- Document Extraction
- ESG
- Financial Data
- Index Data
- LLM
- MCP
- Market Intelligence
- Mobility
- Named Entity Recognition
- Speech-to-Text
- Real-Time
use_cases:
- description: Ground LLM-generated investment notes, tearsheets, and earnings previews in live S&P Capital IQ data via the LLM-ready API and the S&P Global Claude Cowork plugin.
  name: AI Equity Research
- description: Pull merger, acquisition, advisor, and funding-round details for deal sourcing, target screening, and competitive intelligence.
  name: M&A and Funding Intelligence
- description: Retrieve consensus, estimates, calendar dates, and transcripts for earnings preview generation and post-call analysis.
  name: Earnings and Estimates Workflows
- description: Convert PDF filings, decks, and research into structured JSON with Kensho Extract for downstream RAG and analytics pipelines.
  name: Document Intelligence
- description: Use Kensho NERD to disambiguate company and security mentions in news, filings, and chat to canonical Capital IQ IDs.
  name: Entity Linking for Financial Text
- description: Transcribe finance and business audio with Kensho Scribe v2 batch and real-time APIs, including Human-in-the-Loop review for highest accuracy.
  name: Earnings Call Transcription
- description: Build chatbots and analyst assistants that return cited answers from S&P Global datasets via the Grounding Agent.
  name: Grounded Conversational Analytics
website: https://www.spglobal.com
---
