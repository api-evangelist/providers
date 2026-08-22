---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Amazon Kendra Agentic Access
  operation_count: 26
  slug: amazon-kendra-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 8
apis:
- description: Operations for managing data source connectors
  name: Amazon Kendra Data Sources API
  slug: amazon-kendra-data-sources-api
- description: Operations for managing documents in the index
  name: Amazon Kendra Documents API
  slug: amazon-kendra-documents-api
- description: Operations for managing search experiences
  name: Amazon Kendra Experience API
  slug: amazon-kendra-experience-api
- description: Operations for managing FAQ entries
  name: Amazon Kendra FAQs API
  slug: amazon-kendra-faqs-api
- description: Operations for creating and managing search indexes
  name: Amazon Kendra Indexes API
  slug: amazon-kendra-indexes-api
- description: Operations for querying the search index
  name: Amazon Kendra Queries API
  slug: amazon-kendra-queries-api
- description: Operations for query autocompletion
  name: Amazon Kendra Query Suggestions API
  slug: amazon-kendra-query-suggestions-api
- description: Operations for managing custom synonyms
  name: Amazon Kendra Thesaurus API
  slug: amazon-kendra-thesaurus-api
arazzos:
- description: Load an FAQ file from S3 into an index, wait until it is active, then query for FAQ-backed answers.
  name: Amazon Kendra Create FAQ and Query
  slug: amazon-kendra-create-faq-and-query-workflow
- description: Wait for an index to be active, create a hosted search experience on it, and confirm it via the experiences list.
  name: Amazon Kendra Create Search Experience
  slug: amazon-kendra-create-search-experience-workflow
- description: Load a custom synonym thesaurus from S3 into an index, wait until it is active, then run a synonym-aware query.
  name: Amazon Kendra Create Thesaurus and Query
  slug: amazon-kendra-create-thesaurus-and-query-workflow
- description: Directly upload documents into an index, wait until they finish indexing, then run a search query.
  name: Amazon Kendra Ingest Documents and Query
  slug: amazon-kendra-ingest-documents-and-query-workflow
- description: Create an index, wait until it is active, attach a data source, and kick off the first sync job.
  name: Amazon Kendra Provision Index and Start First Sync
  slug: amazon-kendra-provision-index-and-sync-workflow
- description: Generate type-ahead query suggestions for a partial query, then run a full search using the top suggestion.
  name: Amazon Kendra Query Suggestions then Search
  slug: amazon-kendra-query-suggestions-then-search-workflow
- description: Remove stale documents from an index, upload their refreshed versions, and wait until the new versions are indexed.
  name: Amazon Kendra Refresh Documents
  slug: amazon-kendra-refresh-documents-workflow
- description: Update a data source's sync schedule, trigger an immediate sync, and wait for that sync to succeed.
  name: Amazon Kendra Reschedule and Resync Data Source
  slug: amazon-kendra-reschedule-and-resync-data-source-workflow
- description: Look up an index by name, confirm it is active, and run a search query against it.
  name: Amazon Kendra Resolve Index by Name and Query
  slug: amazon-kendra-resolve-index-and-query-workflow
- description: Retrieve semantically relevant passages for a question and run a parallel ranked query to enrich a RAG context.
  name: Amazon Kendra Retrieve Passages for RAG
  slug: amazon-kendra-retrieve-passages-for-rag-workflow
- description: Start a data source sync job on an existing connector, wait for it to succeed, then query the refreshed index.
  name: Amazon Kendra Sync Data Source and Query
  slug: amazon-kendra-sync-data-source-and-query-workflow
- description: Delete a data source connector, confirm it is gone, then delete the index that owned it.
  name: Amazon Kendra Teardown Data Source and Index
  slug: amazon-kendra-teardown-data-source-and-index-workflow
artifact_total: 67
collections:
- collection_type: postman
  name: Amazon Kendra API
  slug: postman-amazon-kendra
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Kendra Data Sources API
  slug: open-amazon-kendra-data-sources-api
- collection_type: open
  name: Amazon Kendra Data Sources Documents API
  slug: open-amazon-kendra-documents-api
- collection_type: open
  name: Amazon Kendra Data Sources Experience API
  slug: open-amazon-kendra-experience-api
- collection_type: open
  name: Amazon Kendra Data Sources FAQs API
  slug: open-amazon-kendra-faqs-api
- collection_type: open
  name: Amazon Kendra Data Sources Indexes API
  slug: open-amazon-kendra-indexes-api
- collection_type: open
  name: Amazon Kendra Data Sources Queries API
  slug: open-amazon-kendra-queries-api
- collection_type: open
  name: Amazon Kendra Data Sources Query Suggestions API
  slug: open-amazon-kendra-query-suggestions-api
- collection_type: open
  name: Amazon Kendra Data Sources Thesaurus API
  slug: open-amazon-kendra-thesaurus-api
- collection_type: open
  name: Amazon Kendra API
  slug: open-amazon-kendra
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-kendra-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-kendra-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-kendra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-kendra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-kendra-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-kendra/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-create-faq-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-create-search-experience-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-create-thesaurus-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-ingest-documents-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-provision-index-and-sync-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-query-suggestions-then-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-refresh-documents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-reschedule-and-resync-data-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-resolve-index-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-retrieve-passages-for-rag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-sync-data-source-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-kendra-teardown-data-source-and-index-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/kendra/home
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/kendra/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/kendra/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kendra/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/kendra/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/kendra/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/kendra/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-kendra-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-kendra-vocabulary.yaml
created: '2024-01-15'
description: Amazon Kendra is an intelligent enterprise search service powered by machine learning that enables organizations to index and search across multiple data sources, delivering highly accurate and relevant answers to natural language queries.
examples:
- key_count: 6
  name: Amazon Kendra Data Source Example
  slug: amazon-kendra-data-source-example
- key_count: 6
  name: Amazon Kendra Faq Example
  slug: amazon-kendra-faq-example
- key_count: 7
  name: Amazon Kendra Index Example
  slug: amazon-kendra-index-example
- key_count: 4
  name: Amazon Kendra Query Result Example
  slug: amazon-kendra-query-result-example
features:
- description: ML-powered semantic search that understands natural language queries and context to return highly accurate answers from enterprise content.
  name: Intelligent Search
- description: Kendra Retriever API enables retrieval-augmented generation workflows with optimized passage chunking and ACL-based filtering for LLM integration.
  name: GenAI RAG Support
- description: Native connectors for Amazon S3, SharePoint, Salesforce, ServiceNow, Google Drive, Confluence, and many more data repositories.
  name: Data Source Connectors
- description: Fine-tune search results based on document freshness, authoritative sources, and custom synonyms without ML expertise.
  name: Relevance Tuning
- description: No-code visual interface to build, customize, and launch search applications with drag-and-drop components.
  name: Experience Builder
- description: Visibility into quality and usability metrics and user interaction patterns to identify content gaps.
  name: Search Analytics Dashboard
- description: Preprocessing capabilities for metadata enrichment, document classification, entity extraction, and AWS AI service integration.
  name: Custom Document Enrichment
- description: Learns from user interactions and feedback to promote preferred documents to the top of search results over time.
  name: Incremental Learning
finops:
- name: Amazon Kendra Finops
  service_category: API
  slug: amazon-kendra-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: DataSource
  property_count: 6
  slug: amazon-kendra-data-source
- name: Faq
  property_count: 6
  slug: amazon-kendra-faq
- name: Index
  property_count: 7
  slug: amazon-kendra-index
- name: QueryResult
  property_count: 4
  slug: amazon-kendra-query-result
json_structures:
- name: Amazon Kendra Data Source Structure
  property_count: 6
  slug: amazon-kendra-data-source-structure
- name: Amazon Kendra Faq Structure
  property_count: 6
  slug: amazon-kendra-faq-structure
- name: Amazon Kendra Index Structure
  property_count: 7
  slug: amazon-kendra-index-structure
- name: Amazon Kendra Query Result Structure
  property_count: 4
  slug: amazon-kendra-query-result-structure
jsonld:
- class_count: 4
  name: Amazon Kendra Context
  property_count: 16
  slug: amazon-kendra-context
layout: provider
modified: '2026-05-19'
name: Amazon Kendra
nav: Providers
network: true
overview: 'Amazon Kendra publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data Sources API, Documents API, Experience API, and 5 more. Tagged areas include AI, Enterprise Search, Knowledge Management, Machine Learning, and Natural Language.


  The Amazon Kendra catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Kendra''s developer surface includes authentication, engineering blog, support, developer console, CLI, developer portal, documentation, and 29 more developer resources.'
plans:
- name: Amazon Kendra Plans Pricing
  plan_count: 3
  slug: amazon-kendra-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Amazon Kendra Rate Limits
  slug: amazon-kendra-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Kendra API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-kendra-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon Kendra API Rules
  rule_count: 26
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 16
  slug: amazon-kendra-spectral-rules
score:
  band: strong
  composite: 61.7
  delta: -7.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 25.0
    contract_quality: 76.1
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-kendra/refs/heads/main/screenshots/amazon-kendra-2026-06-20T171715.png
security:
- kind: authentication
  name: Amazon Kendra Authentication
  slug: amazon-kendra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Kendra Domain Security
  slug: amazon-kendra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Kendra Vulnerability Disclosure
  slug: amazon-kendra-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Kendra Trust Center
  slug: amazon-kendra-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-kendra
tags:
- AI
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
use_cases:
- description: Help employees find accurate answers and data-driven insights across internal knowledge bases and document repositories.
  name: Employee Productivity
- description: Power self-service chatbots and agent-assist solutions for contact centers with intelligent search.
  name: Customer Service
- description: Integrate intelligent search and conversational AI into customer-facing applications via the Kendra API.
  name: SaaS Application Integration
- description: Use Kendra GenAI indices in Amazon Q Business and Amazon Bedrock knowledge bases to build RAG applications.
  name: Generative AI Applications
- description: Index and search across multiple heterogeneous data sources to create a unified knowledge search experience.
  name: Enterprise Knowledge Management
website: https://aws.amazon.com/kendra/
---
