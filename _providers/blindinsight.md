---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 83
  human_in_the_loop: 4
  name: Blindinsight Agentic Access
  operation_count: 127
  slug: blindinsight-agentic-access
  summary_line: 127 operations · 83 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The accounts API from BlindInsight — 10 operation(s) for accounts.
  name: BlindInsight accounts API
  slug: blindinsight-accounts-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The blindllm API from BlindInsight — 4 operation(s) for blindllm.
  name: BlindInsight blindllm API
  slug: blindinsight-blindllm-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The blindllm-queries API from BlindInsight — 2 operation(s) for blindllm-queries.
  name: BlindInsight blindllm-queries API
  slug: blindinsight-blindllm-queries-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The csrf API from BlindInsight — 1 operation(s) for csrf.
  name: BlindInsight csrf API
  slug: blindinsight-csrf-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The datasets API from BlindInsight — 3 operation(s) for datasets.
  name: BlindInsight datasets API
  slug: blindinsight-datasets-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The delete-jobs API from BlindInsight — 1 operation(s) for delete-jobs.
  name: BlindInsight delete-jobs API
  slug: blindinsight-delete-jobs-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The files API from BlindInsight — 2 operation(s) for files.
  name: BlindInsight files API
  slug: blindinsight-files-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The grants API from BlindInsight — 2 operation(s) for grants.
  name: BlindInsight grants API
  slug: blindinsight-grants-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The identities API from BlindInsight — 2 operation(s) for identities.
  name: BlindInsight identities API
  slug: blindinsight-identities-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The jobs API from BlindInsight — 2 operation(s) for jobs.
  name: BlindInsight jobs API
  slug: blindinsight-jobs-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The materials API from BlindInsight — 8 operation(s) for materials.
  name: BlindInsight materials API
  slug: blindinsight-materials-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The organizations API from BlindInsight — 15 operation(s) for organizations.
  name: BlindInsight organizations API
  slug: blindinsight-organizations-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The records API from BlindInsight — 5 operation(s) for records.
  name: BlindInsight records API
  slug: blindinsight-records-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The requests API from BlindInsight — 4 operation(s) for requests.
  name: BlindInsight requests API
  slug: blindinsight-requests-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The schemas API from BlindInsight — 4 operation(s) for schemas.
  name: BlindInsight schemas API
  slug: blindinsight-schemas-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The status API from BlindInsight — 1 operation(s) for status.
  name: BlindInsight status API
  slug: blindinsight-status-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The token API from BlindInsight — 3 operation(s) for token.
  name: BlindInsight token API
  slug: blindinsight-token-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The users API from BlindInsight — 4 operation(s) for users.
  name: BlindInsight users API
  slug: blindinsight-users-api
- baseURL: https://api.app.blindinsight.io
  baseurl_source: declared
  description: The ws API from BlindInsight — 1 operation(s) for ws.
  name: BlindInsight ws API
  slug: blindinsight-ws-api
artifact_total: 43
asyncapis:
- description: Real-time progress channel for asynchronous Blind Insight ingest/upload jobs. After starting a batch upload (POST /api/jobs/upload/) or a large resumable file upload (POST /api/files/), clients receiv
  name: Blind Insight Jobs WebSocket
  slug: blindinsight-jobs-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blind Insight REST accounts API
  slug: open-blindinsight-accounts-api
- collection_type: open
  name: Blind Insight REST accounts blindllm API
  slug: open-blindinsight-blindllm-api
- collection_type: open
  name: Blind Insight REST accounts blindllm-queries API
  slug: open-blindinsight-blindllm-queries-api
- collection_type: open
  name: Blind Insight REST accounts csrf API
  slug: open-blindinsight-csrf-api
- collection_type: open
  name: Blind Insight REST accounts datasets API
  slug: open-blindinsight-datasets-api
- collection_type: open
  name: Blind Insight REST accounts delete-jobs API
  slug: open-blindinsight-delete-jobs-api
- collection_type: open
  name: Blind Insight REST accounts files API
  slug: open-blindinsight-files-api
- collection_type: open
  name: Blind Insight REST accounts grants API
  slug: open-blindinsight-grants-api
- collection_type: open
  name: Blind Insight REST accounts identities API
  slug: open-blindinsight-identities-api
- collection_type: open
  name: Blind Insight REST accounts jobs API
  slug: open-blindinsight-jobs-api
- collection_type: open
  name: Blind Insight REST accounts materials API
  slug: open-blindinsight-materials-api
- collection_type: open
  name: Blind Insight REST accounts organizations API
  slug: open-blindinsight-organizations-api
- collection_type: open
  name: Blind Insight REST accounts records API
  slug: open-blindinsight-records-api
- collection_type: open
  name: Blind Insight REST accounts requests API
  slug: open-blindinsight-requests-api
- collection_type: open
  name: Blind Insight REST accounts schemas API
  slug: open-blindinsight-schemas-api
- collection_type: open
  name: Blind Insight REST accounts status API
  slug: open-blindinsight-status-api
- collection_type: open
  name: Blind Insight REST accounts token API
  slug: open-blindinsight-token-api
- collection_type: open
  name: Blind Insight REST accounts users API
  slug: open-blindinsight-users-api
- collection_type: open
  name: Blind Insight REST accounts ws API
  slug: open-blindinsight-ws-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/blindinsight-openapi-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: BlindInsight
nav: Providers
network: true
overview: 'BlindInsight publishes 19 APIs on the [APIs.io](https://apis.io/) network, including accounts API, blindllm API, blindllm-queries API, and 16 more. Tagged areas include Company, Security, Encryption, Privacy, and Confidential Computing.


  The BlindInsight catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BlindInsight''s developer surface includes authentication, CLI, sandbox, documentation, API reference, getting-started guide, signup flow, and 18 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 61.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Machine-Learning
- Compliance
- Cryptography
website: https://blindinsight.io
---
