---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 83
  human_in_the_loop: 4
  name: Blindinsight Agentic Access
  operation_count: 127
  slug: blindinsight-agentic-access
  summary_line: 127 operations · 83 acting · 4 human-in-the-loop
api_count: 19
apis:
- description: The accounts API from BlindInsight — 10 operation(s) for accounts.
  name: BlindInsight accounts API
  slug: blindinsight-accounts-api
- description: The blindllm API from BlindInsight — 4 operation(s) for blindllm.
  name: BlindInsight blindllm API
  slug: blindinsight-blindllm-api
- description: The blindllm-queries API from BlindInsight — 2 operation(s) for blindllm-queries.
  name: BlindInsight blindllm-queries API
  slug: blindinsight-blindllm-queries-api
- description: The csrf API from BlindInsight — 1 operation(s) for csrf.
  name: BlindInsight csrf API
  slug: blindinsight-csrf-api
- description: The datasets API from BlindInsight — 3 operation(s) for datasets.
  name: BlindInsight datasets API
  slug: blindinsight-datasets-api
- description: The delete-jobs API from BlindInsight — 1 operation(s) for delete-jobs.
  name: BlindInsight delete-jobs API
  slug: blindinsight-delete-jobs-api
- description: The files API from BlindInsight — 2 operation(s) for files.
  name: BlindInsight files API
  slug: blindinsight-files-api
- description: The grants API from BlindInsight — 2 operation(s) for grants.
  name: BlindInsight grants API
  slug: blindinsight-grants-api
- description: The identities API from BlindInsight — 2 operation(s) for identities.
  name: BlindInsight identities API
  slug: blindinsight-identities-api
- description: The jobs API from BlindInsight — 2 operation(s) for jobs.
  name: BlindInsight jobs API
  slug: blindinsight-jobs-api
- description: The materials API from BlindInsight — 8 operation(s) for materials.
  name: BlindInsight materials API
  slug: blindinsight-materials-api
- description: The organizations API from BlindInsight — 15 operation(s) for organizations.
  name: BlindInsight organizations API
  slug: blindinsight-organizations-api
- description: The records API from BlindInsight — 5 operation(s) for records.
  name: BlindInsight records API
  slug: blindinsight-records-api
- description: The requests API from BlindInsight — 4 operation(s) for requests.
  name: BlindInsight requests API
  slug: blindinsight-requests-api
- description: The schemas API from BlindInsight — 4 operation(s) for schemas.
  name: BlindInsight schemas API
  slug: blindinsight-schemas-api
- description: The status API from BlindInsight — 1 operation(s) for status.
  name: BlindInsight status API
  slug: blindinsight-status-api
- description: The token API from BlindInsight — 3 operation(s) for token.
  name: BlindInsight token API
  slug: blindinsight-token-api
- description: The users API from BlindInsight — 4 operation(s) for users.
  name: BlindInsight users API
  slug: blindinsight-users-api
- description: The ws API from BlindInsight — 1 operation(s) for ws.
  name: BlindInsight ws API
  slug: blindinsight-ws-api
artifact_total: 24
asyncapis:
- description: Real-time progress channel for asynchronous Blind Insight ingest/upload jobs. After starting a batch upload (POST /api/jobs/upload/) or a large resumable file upload (POST /api/files/), clients receiv
  name: Blind Insight Jobs WebSocket
  slug: blindinsight-jobs-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blindinsight-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blindinsight-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blindinsight-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/blindinsight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blindinsight-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/blindinsight-cli.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blindinsight-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blindinsight-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blindinsight-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blindinsight-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/blindinsight-jobs-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blindinsight-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/blindinsight-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blindinsight-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blindinsight-llms.txt
- group: company
  title: ''
  type: Website
  url: https://blindinsight.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blindinsight.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blindinsight.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blindinsight.io/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blindinsight.io/getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://app.blindinsight.io/
- group: start
  title: ''
  type: Login
  url: https://app.blindinsight.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blind-insight
created: '2026-07-17'
description: BlindInsight (Blind Insight) is an end-to-end encrypted datastore and privacy-preserving data-analysis platform. It lets teams encrypt, ingest, search, and run machine learning and LLM queries over fully encrypted records without ever exposing plaintext, using a locally deployed Blind Proxy that transparently performs client-side encryption and decryption against the cloud REST API. The platform provides schema-constrained encrypted fields, searchable encryption, key sharing and keyring management, role- and team-based access grants, organization and user management, resumable batch ingestion, and a BlindLLM interface for prompting models over protected data — aimed at regulated, compliance-sensitive workloads.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blindinsight.png
layout: provider
mcp_servers:
- description: ''
  name: blindinsight-mcp.yml
  slug: blindinsight-mcpyml
modified: '2026-07-18'
name: BlindInsight
nav: Providers
network: true
overview: 'BlindInsight publishes 19 APIs on the [APIs.io](https://apis.io/) network, including accounts API, blindllm API, blindllm-queries API, and 16 more. Tagged areas include Company, Security, Encryption, Privacy, and Confidential Computing.


  The BlindInsight catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BlindInsight''s developer surface includes authentication, CLI, sandbox, documentation, API reference, getting-started guide, signup flow, and 17 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 61.2
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 44.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blindinsight/refs/heads/main/screenshots/blindinsight-2026-07-25T203316.png
security:
- kind: authentication
  name: Blindinsight Authentication
  slug: blindinsight-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Blindinsight Domain Security
  slug: blindinsight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blindinsight
tags:
- Company
- Security
- Encryption
- Privacy
- Confidential Computing
- Data
- Machine Learning
- Compliance
- Cryptography
website: https://blindinsight.io
---
