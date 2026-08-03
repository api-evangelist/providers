---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 146
  human_in_the_loop: 0
  name: Pryon Agentic Access
  operation_count: 276
  slug: pryon-agentic-access
  summary_line: 276 operations · 146 acting
api_count: 8
apis:
- description: The Pryon Platform administrative API — organizations, teams, members, knowledge collections and knowledge domains, content and content groups, connectors, subjects, regression tests, messages, analyt
  name: Pryon Admin API
  slug: pryon-admin-api
- description: The Pryon Retrieval Engine API — create and continue retrievals over a knowledge collection (REST, WebSocket and server-sent events), fetch content, content groups, extracts, summaries and content ima
  name: Pryon Retrieval API
  slug: pryon-retrieval-api
- description: The Pryon Generative Engine API — OpenAI-compatible chat completions and model listing, query guardrails (toxicity and prompt-injection classification), query routing, query rewriting for multi-turn c
  name: Pryon Generative API
  slug: pryon-generative-api
- description: Create, list, retrieve and delete knowledge collections for an organization, resolve the active knowledge domain behind a collection, and decommission knowledge domain versions.
  name: Pryon Knowledge Collections API
  slug: pryon-knowledge-collections-api
- description: Conversational exchange over a Pryon collection — start or continue a conversation, review the exchange request and response cycle, and stream ExchangeEvent messages as data-only server-sent events.
  name: Pryon Exchange API
  slug: pryon-exchange-api
- description: Ratings, rating reviews, approvals and verified answers across extractive exchanges, generative exchanges and generative retrievals — the human-in-the-loop surface that curates what a Pryon collection
  name: Pryon Feedback API
  slug: pryon-feedback-api
- description: The contract a customer implements to connect any content repository that has no prebuilt Pryon connector — discover content sources with pagination, download content data in parts, return content met
  name: Pryon Universal Connector API
  slug: pryon-universal-connector-api
- description: Define, list, update and delete user-defined metadata fields and field values at the organization and collection level, and list the collections that use a given metadata field — the filters that narr
  name: Pryon User-Defined Metadata API
  slug: pryon-user-defined-metadata-api
artifact_total: 14
asyncapis:
- description: ''
  name: Pryon Events
  slug: pryon-events
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/pryon-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.pryon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pryon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pryon.com/docs/about-pryon
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pryon.com/reference/api-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pryon.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/pryon-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pryon.com/resources/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.pryon.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pryon-AI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pryon.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pryon.com/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.pryon.com/acceptable-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.pryon.com/about/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pryon.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pryon-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pryon-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/pryon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pryon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pryon-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pryon-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pryon-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/pryon-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/pryon-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pryon-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pryon-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pryon-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pryon-tool-crosswalk.yml
- group: other
  title: ''
  type: Events
  url: asyncapi/pryon-events.yml
created: '2026-08-02'
description: Pryon is a Raleigh, North Carolina enterprise AI company founded in 2017 by Igor Jablokov that provides a retrieval-augmented generation (RAG) platform for regulated and security-conscious organizations. The Pryon RAG Suite couples an Ingestion Engine (filetype handling, layout analysis, OCR/HTR, table structure recognition and semantic segmentation), a Retrieval Engine (vast search, query canonicalization, query classification, metadata filtering, verified answers) and a Generative Engine (chat completions, guardrails, query rewriting, answer summarization) behind a single set of REST APIs. Symphony, its low-code orchestration builder, composes those engines into custom RAG and agentic workflows. Content is ingested through prebuilt connectors for SharePoint, Salesforce, Amazon S3, Azure Blob Storage, Google Cloud Storage, NFS and a Universal Connector, and the platform is deployed in Pryon SaaS, customer VPC, on-premises and air-gapped environments. All 276 published operations
  are documented at docs.pryon.com, which also serves an llms.txt index for agents.
image: https://cdn.prod.website-files.com/65cbae0a3956181cf7a74c75/672bde6da9f2a2dc6e54b6fa_fav-icon-pryon-wht-bg.png
layout: provider
mcp_servers:
- description: ''
  name: pryon-mcp.yml
  slug: pryon-mcpyml
modified: '2026-08-02'
name: Pryon
nav: Providers
network: true
overview: 'Pryon publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Retrieval API, Generative API, and 5 more. Tagged areas include Artificial Intelligence, Retrieval Augmented Generation, Enterprise Search, Knowledge Management, and Generative AI.


  The Pryon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pryon''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, changelog, and 23 more developer resources.'
random_paper: 93
score:
  band: developing
  composite: 47.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 57.8
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Pryon Authentication
  slug: pryon-authentication
  summary_line: oauth2/apiKey · 1 scheme
- kind: domain-security
  name: Pryon Domain Security
  slug: pryon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pryon Trust Center
  slug: pryon-trust-center
  summary_line: SOC 2
slug: pryon
tags:
- Artificial Intelligence
- Retrieval Augmented Generation
- Enterprise Search
- Knowledge Management
- Generative AI
- Document Ingestion
- Content Connectors
- Agents
- Machine Learning
- Company
website: https://www.pryon.com/
---
