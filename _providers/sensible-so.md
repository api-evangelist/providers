---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Sensible So Agentic Access
  operation_count: 32
  slug: sensible-so-agentic-access
  summary_line: 32 operations · 19 acting
api_count: 4
apis:
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: The Configuration API from sensible-so — 4 operation(s) for configuration.
  name: sensible-so Configuration API
  slug: sensible-so-configuration-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: Classify documents by type
  name: sensible-so Document API
  slug: sensible-so-document-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: The Document type API from sensible-so — 2 operation(s) for document type.
  name: sensible-so Document type API
  slug: sensible-so-document-type-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: Convert extracted document data to spreadsheet
  name: sensible-so Get Excel from documents API
  slug: sensible-so-get-excel-from-documents-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: Extract data from multiple documents bundled into single PDF files
  name: sensible-so Portfolio API
  slug: sensible-so-portfolio-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: The Reference document API from sensible-so — 4 operation(s) for reference document.
  name: sensible-so Reference document API
  slug: sensible-so-reference-document-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: spec
  description: Retrieve data extracted asynchronously from documents
  name: sensible-so Retrieve extractions API
  slug: sensible-so-retrieve-extractions-api
arazzos:
- description: Classify a document to discover its best-fit document type, then submit an asynchronous extraction against that type.
  name: Sensible Classify Then Extract
  slug: sensible-so-classify-then-extract-workflow
- description: List the version history of a configuration, then fetch one specific version of that configuration in full.
  name: Sensible Config Versions Then Get By Version
  slug: sensible-so-config-versions-then-get-by-version-workflow
- description: Create a new document type and then add a SenseML configuration to it in one pass.
  name: Sensible Create Document Type And Configuration
  slug: sensible-so-create-document-type-and-configuration-workflow
- description: Register a reference document in a document type, then list the type's reference documents to confirm registration.
  name: Sensible Create Reference Document And List
  slug: sensible-so-create-reference-document-and-list-workflow
- description: Kick off an asynchronous extraction from a document URL with a chosen config, poll until it completes, then read the parsed results.
  name: Sensible Extract From URL And Poll
  slug: sensible-so-extract-from-url-and-poll-workflow
- description: Asynchronously extract a document from a URL, poll until complete, then export the extraction as a CSV file.
  name: Sensible Extract From URL Poll Then CSV
  slug: sensible-so-extract-from-url-poll-then-csv-workflow
- description: Pull all standardized text from a reference document, then list the document type's reference documents.
  name: Sensible Extract Reference Text Then List
  slug: sensible-so-extract-reference-text-then-list-workflow
- description: Fetch a document type by id and then enumerate the configurations defined inside it.
  name: Sensible Get Document Type Then List Configurations
  slug: sensible-so-get-document-type-then-list-configurations-workflow
- description: List the configurations in a document type, then fetch the full stringified JSON of one named configuration.
  name: Sensible List Configurations Then Get
  slug: sensible-so-list-configurations-then-get-workflow
- description: Confirm a document type exists in the account before submitting an asynchronous extraction against it.
  name: Sensible List Document Types Then Extract
  slug: sensible-so-list-document-types-then-extract-workflow
- description: List recent extractions with filters, then retrieve the full result of the most recent matching extraction.
  name: Sensible List Extractions Then Retrieve
  slug: sensible-so-list-extractions-then-retrieve-workflow
- description: Segment and extract a multi-document portfolio at a URL, then poll until every sub-document extraction completes.
  name: Sensible Portfolio Extract From URL And Poll
  slug: sensible-so-portfolio-extract-from-url-and-poll-workflow
- description: Generate a Sensible-signed upload URL for a multi-document portfolio, then poll the portfolio extraction to completion.
  name: Sensible Portfolio Upload URL And Poll
  slug: sensible-so-portfolio-upload-url-and-poll-workflow
- description: Synchronously extract a document, then convert that extraction to a downloadable Excel spreadsheet.
  name: Sensible Sync Extract Then Spreadsheet
  slug: sensible-so-sync-extract-then-spreadsheet-workflow
- description: Generate a Sensible-signed upload URL for a document type, then poll the extraction id until results are ready.
  name: Sensible Upload URL Extract And Poll
  slug: sensible-so-upload-url-extract-and-poll-workflow
artifact_total: 79
collections:
- collection_type: postman
  name: Sensible Classification API
  slug: postman-sensible-classification-api
- collection_type: postman
  name: Sensible Document Types and Configurations API
  slug: postman-sensible-document-types-api
- collection_type: postman
  name: Sensible Extractions API
  slug: postman-sensible-extractions-api
- collection_type: postman
  name: Sensible Reference Documents API
  slug: postman-sensible-reference-documents-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sensible Classification API
  slug: open-sensible-classification-api
- collection_type: open
  name: Sensible Document Types and Configurations API
  slug: open-sensible-document-types-api
- collection_type: open
  name: Sensible Extractions API
  slug: open-sensible-extractions-api
- collection_type: open
  name: Sensible Reference Documents API
  slug: open-sensible-reference-documents-api
- collection_type: open
  name: Sensible Classification Configuration API
  slug: open-sensible-so-configuration-api
- collection_type: open
  name: Sensible Classification Configuration Document API
  slug: open-sensible-so-document-api
- collection_type: open
  name: Sensible Classification Configuration Document type API
  slug: open-sensible-so-document-type-api
- collection_type: open
  name: Sensible Classification Configuration Get Excel from documents API
  slug: open-sensible-so-get-excel-from-documents-api
- collection_type: open
  name: Sensible Classification Configuration Portfolio API
  slug: open-sensible-so-portfolio-api
- collection_type: open
  name: Sensible Classification Configuration Reference document API
  slug: open-sensible-so-reference-document-api
- collection_type: open
  name: Sensible Classification Configuration Retrieve extractions API
  slug: open-sensible-so-retrieve-extractions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sensible-so-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sensible-so-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sensible-so-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensible-so-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sensible-so-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sensible-so/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-classify-then-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-config-versions-then-get-by-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-create-document-type-and-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-create-reference-document-and-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-extract-from-url-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-extract-from-url-poll-then-csv-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-extract-reference-text-then-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-get-document-type-then-list-configurations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-list-configurations-then-get-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-list-document-types-then-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-list-extractions-then-retrieve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-portfolio-extract-from-url-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-portfolio-upload-url-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-sync-extract-then-spreadsheet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sensible-so-upload-url-extract-and-poll-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.sensible.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensible.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensible.so/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sensible.so/changelog
- group: auth
  title: ''
  type: Authentication
  url: https://docs.sensible.so/reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sensible.so/docs/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sensible.so/docs/api-tutorial
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensible.so/llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://sensible.statuspage.io
- group: start
  title: ''
  type: Signup
  url: https://app.sensible.so/register
- group: other
  title: ''
  type: Account
  url: https://app.sensible.so/account
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sensible.so/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensible.so/reference/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.sensible.so/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sensible-hq
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sensible-hq/sensible-api-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sensible-hq/sensible-api-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sensible-hq/sensible-code-examples
- group: build
  title: ''
  type: Examples
  url: https://github.com/sensible-hq/sensible-configuration-library
- group: build
  title: ''
  type: Examples
  url: https://github.com/sensible-hq/sensible-sample-documents
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/16839934-45339059-3fec-4c31-a891-9a12a3e1c22b
- group: commercial
  title: ''
  type: Plans
  url: plans/sensible-so-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sensible-so-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sensible-so-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sensible-so-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sensible-so-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sensible.so/blog
created: '2026-05-25T00:00:00.000Z'
description: Sensible is a document-automation API platform that extracts structured data from PDFs, images, spreadsheets, and emails using a hybrid of deterministic layout-based methods and LLM-based query methods. SenseML, Sensible's config language, lets engineers declare what to pull and where. The platform ships with 150+ open-source pre-built configurations across financial services, insurance, logistics, real estate, and healthcare. Sensible exposes sync and async extraction, classification, portfolio segmentation, CSV/Excel export, human review, coverage statistics, configuration versioning, and webhook delivery, all behind a bearer-auth REST surface plus a Postman collection, an MCP server, and Python / JavaScript SDKs.
examples:
- key_count: 3
  name: Sensible So Classify Async Example
  slug: sensible-so-classify-async-example
- key_count: 2
  name: Sensible So Create Document Type Example
  slug: sensible-so-create-document-type-example
- key_count: 3
  name: Sensible So Extract From Url Example
  slug: sensible-so-extract-from-url-example
- key_count: 2
  name: Sensible So Extract Sync Example
  slug: sensible-so-extract-sync-example
- key_count: 2
  name: Sensible So List Extractions Example
  slug: sensible-so-list-extractions-example
features:
- Hybrid extraction combining layout-based methods (label, region, box, paragraph, fixed_table, row, column, intersection, regex) with LLM-based methods (query_group, list, nlp_table)
- SenseML configuration language with version control (draft, development, production) and environment promotion
- 150+ pre-built configurations in the open-source sensible-configuration-library covering common document types (1040, W-2, 1099, ACORD forms, loss runs, bank statements, rate confirmations)
- Synchronous extraction `/extract/{document_type}` (testing) and asynchronous extraction `/extract_from_url`, `/generate_upload_url` (production)
- Portfolio extractions — segment a packaged PDF into multiple document types and extract each automatically
- Webhook delivery on extraction COMPLETE or human review APPROVED
- Document classification (sync + async) into account-defined document types
- Confidence scoring and fallback configs for LLM-based methods
- Computer vision-enhanced table detection and automatic + selective OCR (handwriting supported)
- Document splitting and fingerprinting for multi-document PDFs
- CSV and Excel output endpoints (`/generate_csv`, `/generate_excel`) for one or many extractions
- Daily coverage statistics per configuration (`/extractions/statistics`) for tuning and FinOps attribution
- Reference documents ("goldens") for layout tuning and fingerprinting
- Human review workflow with magic-link account auth tokens for non-account reviewers
- Validations (warning / error severity) declared inside the document-type schema
- Per-document pricing (linear, no token volatility) — Growth $499/mo (750 docs), Scale $1,499/mo (3,200 docs), Enterprise custom
- Bearer API key authentication; per-second concurrency limits scale by plan (1 → 10 → 25+)
- Python and JavaScript/TypeScript SDKs, Salesforce and QuickBooks integration examples
- Postman collection (16839934-45339059-3fec-4c31-a891-9a12a3e1c22b) for hands-on exploration
- Zapier app for Airtable, Slack, Google Sheets integrations
- Remote MCP server at https://docs.sensible.so/mcp for AI editors (Cursor, Windsurf, Claude Desktop)
- HIPAA on Enterprise; SOC 2 Type II
finops:
- name: Sensible So Finops
  service_category: Document Processing
  slug: sensible-so-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensible-so.png
json_schemas:
- name: SensibleDocumentType
  property_count: 8
  slug: sensible-so-document-type
- name: SensibleExtraction
  property_count: 13
  slug: sensible-so-extraction
jsonld:
- class_count: 0
  name: Sensible So Context
  property_count: 6
  slug: sensible-so-context
layout: provider
mcp_servers:
- description: ''
  name: Sensible MCP Endpoint
  slug: sensible-mcp-endpoint
modified: '2026-05-25'
name: Sensible
nav: Providers
network: true
overview: 'Sensible publishes 7 APIs on the [APIs.io](https://apis.io/) network, including sensible-so Configuration API, sensible-so Document API, sensible-so Document type API, and 4 more.


  The Sensible catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sensible''s developer surface includes authentication, developer portal, documentation, changelog, getting-started guide, signup flow, pricing, and 41 more developer resources.'
plans:
- name: Sensible So Plans Pricing
  plan_count: 4
  slug: sensible-so-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Sensible So Rate Limits
  slug: sensible-so-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sensible API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sensible-so-jsonschema-spectral-rules
- effective_rule_count: 12
  extends: []
  name: Sensible API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 3
  slug: sensible-so-rules
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 80.3
    catalog_earned_first_party: 0.0
    catalog_gap: 34.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 25.0
    contract_quality: 71.1
    developer_ergonomics: 66.7
    discoverability: 55.6
    governance: 25.0
    operational_transparency: 68.4
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensible-so/refs/heads/main/screenshots/sensible-so-2026-06-20T193703.png
security:
- kind: authentication
  name: Sensible So Authentication
  slug: sensible-so-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sensible So Domain Security
  slug: sensible-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sensible So Vulnerability Disclosure
  slug: sensible-so-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Sensible So Trust Center
  slug: sensible-so-trust-center
  summary_line: SOC 2, HIPAA
slug: sensible-so
website: https://www.sensible.so
---
