---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.refuel.ai/get-started
  - plans/refuel-ai-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Refuel Ai Agentic Access
  operation_count: 109
  slug: refuel-ai-agentic-access
  summary_line: 109 operations · 64 acting
api_count: 3
apis:
- description: Autolabel is the open-source Python library (pip install refuel-autolabel) to label, clean, and enrich text datasets with any LLM (OpenAI, Anthropic, Google, HuggingFace, vLLM, Refuel-hosted). It is a
  name: Refuel Autolabel (Open Source)
  slug: refuel-autolabel-oss
- baseURL: https://cloud-api.refuel.ai
  baseurl_source: declared
  description: The documented realtime application label surface — the endpoint Refuel's own catalog page publishes as `POST https://cloud-api.refuel.ai/applications/{applicationName}/label`, with the concrete reque
  name: Refuel Applications API
  slug: refuel-ai-applications-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Access API from Refuel — 4 operation(s) for access.
  name: Refuel Access API
  slug: refuel-ai-access-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Csp Reports API from Refuel — 1 operation(s) for csp reports.
  name: Refuel Csp Reports API
  slug: refuel-ai-csp-reports-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Datasets API from Refuel — 13 operation(s) for datasets.
  name: Refuel Datasets API
  slug: refuel-ai-datasets-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Finetuned Models API from Refuel — 1 operation(s) for finetuned models.
  name: Refuel Finetuned Models API
  slug: refuel-ai-finetuned-models-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Integrations API from Refuel — 2 operation(s) for integrations.
  name: Refuel Integrations API
  slug: refuel-ai-integrations-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Labs API from Refuel — 2 operation(s) for labs.
  name: Refuel Labs API
  slug: refuel-ai-labs-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Models API from Refuel — 1 operation(s) for models.
  name: Refuel Models API
  slug: refuel-ai-models-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Projects API from Refuel — 6 operation(s) for projects.
  name: Refuel Projects API
  slug: refuel-ai-projects-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Refuel Cloud API API from Refuel — 1 operation(s) for refuel cloud api.
  name: Refuel Refuel Cloud API
  slug: refuel-ai-refuel-cloud-api-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Schema API from Refuel — 1 operation(s) for schema.
  name: Refuel Schema API
  slug: refuel-ai-schema-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Tasks API from Refuel — 28 operation(s) for tasks.
  name: Refuel Tasks API
  slug: refuel-ai-tasks-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Team API from Refuel — 2 operation(s) for team.
  name: Refuel Team API
  slug: refuel-ai-team-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Teams API from Refuel — 1 operation(s) for teams.
  name: Refuel Teams API
  slug: refuel-ai-teams-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Usage API from Refuel — 1 operation(s) for usage.
  name: Refuel Usage API
  slug: refuel-ai-usage-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The User API from Refuel — 1 operation(s) for user.
  name: Refuel User API
  slug: refuel-ai-user-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Users API from Refuel — 3 operation(s) for users.
  name: Refuel Users API
  slug: refuel-ai-users-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Webhook API from Refuel — 1 operation(s) for webhook.
  name: Refuel Webhook API
  slug: refuel-ai-webhook-api
- baseURL: https://github.com/refuel-ai/autolabel
  baseurl_source: declared
  description: The Webhooks API from Refuel — 1 operation(s) for webhooks.
  name: Refuel Webhooks API
  slug: refuel-ai-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Refuel Ai Events
  slug: refuel-ai-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Refuel Cloud Applications API
  slug: open-refuel-ai-applications-api
- collection_type: open
  name: Refuel Cloud API
  slug: open-refuel-ai
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/refuel-ai-cloud-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/refuel-ai-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/refuel-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/refuel-ai-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/refuel-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/refuel-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/refuel-ai-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/refuel-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/refuel-ai-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/refuel-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/refuel-ai-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/refuel-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/refuel-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/refuel-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.refuel.ai/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/refuel-ai-sandbox.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/refuel-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/refuel-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.refuel.ai/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refuel-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/refuel-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/refuel-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refuel-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/refuelai
- group: company
  title: ''
  type: Website
  url: https://www.refuel.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.refuel.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.refuel.ai
- group: docs
  title: ''
  type: APIReference
  url: https://cloud-api.refuel.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.refuel.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/uEdr8nrMGm
- group: company
  title: ''
  type: Blog
  url: https://www.refuel.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.refuel.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://app.refuel.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.refuel.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.refuel.ai/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/refuel-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refuel-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/refuel-ai-finops.yml
created: '2026-06-21'
description: Refuel is an AI data-labeling and data-enrichment platform that uses large language models to label, clean, structure and enrich enterprise datasets. Refuel Cloud exposes a REST API at cloud-api.refuel.ai covering projects, datasets, tasks and task runs, taxonomies, seedsets and evalsets, confidence calibration, Refuel LLM-2 finetuning, and deployed applications whose realtime label endpoint transforms new rows on demand. The open-source autolabel library lets teams run the same LLM labeling workflows in their own environment against OpenAI, Anthropic, Google, HuggingFace, vLLM or Refuel-hosted models. Refuel.ai was acquired by Together AI in May 2025; the platform continues to operate and its API is still live.
finops:
- name: Refuel Ai Finops
  service_category: AI and Machine Learning
  slug: refuel-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refuel-ai.png
layout: provider
mcp_servers:
- description: 'Refuel serves a live, anonymous, remote MCP endpoint at https://docs.refuel.ai/mcp. It is a DOCUMENTATION server, not a Refuel Cloud API server: the three tools search and read the docs corpus and fil'
  name: Refuel.ai
  slug: refuelai
modified: '2026-08-14'
name: Refuel
nav: Providers
network: true
overview: 'Refuel publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Access API, Csp Reports API, and 16 more. Tagged areas include Artificial Intelligence, LLM, Data Labeling, Data Enrichment, and Autolabel.


  The Refuel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Refuel''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
plans:
- name: Refuel Ai Plans Pricing
  plan_count: 3
  slug: refuel-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Refuel Ai Rate Limits
  slug: refuel-ai-rate-limits
score:
  band: strong
  composite: 63.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 63.3
    developer_ergonomics: 74.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refuel-ai/refs/heads/main/screenshots/refuel-ai-2026-08-17T080415.png
security:
- kind: authentication
  name: Refuel Ai Authentication
  slug: refuel-ai-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Refuel Ai Domain Security
  slug: refuel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Refuel Ai Vulnerability Disclosure
  slug: refuel-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Refuel Ai Trust Center
  slug: refuel-ai-trust-center
  summary_line: SOC 2, GDPR
slug: refuel-ai
tags:
- Artificial Intelligence
- LLM
- Data Labeling
- Data Enrichment
- Autolabel
- Machine-Learning
- Data Quality
- Training Data
- Fine-Tuning
- Data Transformation
- Entity Resolution
- Content Moderation
website: https://www.refuel.ai
---
