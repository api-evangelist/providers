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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cuein Agentic Access
  operation_count: 5
  slug: cuein-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: APIs for getting answers
  name: Cuein answers API
  slug: cuein-answers-api
- description: APIs for retrieving customer-support interaction insights
  name: Cuein conversations API
  slug: cuein-conversations-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cuein answers API
  slug: open-cuein-answers-api
- collection_type: open
  name: Cuein answers conversations API
  slug: open-cuein-conversations-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cuein-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cuein-answers-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuein-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cuein-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuein-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuein-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cuein-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cuein-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cuein-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cuein-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cuein-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cuein-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cuein-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cuein-insights-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cuein-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developer.cuein.ai/.well-known/api-catalog
- group: build
  title: ''
  type: Packages
  url: packages/cuein-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cuein-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cuein-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cuein.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://cuein-api.readme.io/reference
- group: docs
  title: ''
  type: APIReference
  url: https://cuein-api.readme.io/reference
- group: company
  title: ''
  type: Blog
  url: https://cuein.ai/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://cuein.ai/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cuein
- group: operate
  title: ''
  type: Support
  url: mailto:support@cuein.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuein.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuein.ai/privacy
created: '2026-07-17'
description: 'Cuein is an AI-native customer-experience platform ("co-pilot for customer experience teams") that unifies structured and unstructured customer-support data and applies generative AI to surface contact reasons, root causes, resolutions, and metrics such as Inferred CSAT and Resolution Rate. Its public developer surface exposes two REST APIs: an Insights API for retrieving per-conversation and bulk conversation insights over a date range, and an Answers API that generates answers grounded in a tenant''s knowledge articles and documents. Both APIs use x-api-key authentication and are documented on a ReadMe-hosted developer hub. Cuein was acquired by ServiceNow (announced Q1 2025); the standalone developer hub remains live. Backed by Lightspeed Venture Partners.'
image: https://files.readme.io/083b62d-Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Cuein MCP Server
  slug: cuein-mcp-server
modified: '2026-08-14'
name: Cuein
nav: Providers
network: true
overview: 'Cuein publishes 2 APIs on the [APIs.io](https://apis.io/) network: answers API and conversations API. Tagged areas include Company, Customer Experience, Customer-Support, Conversation Intelligence, and Generative AI.


  Cuein''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 24 more developer resources.'
plans:
- name: Cuein Plans Pricing
  plan_count: 0
  slug: cuein-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Cuein Rate Limits
  slug: cuein-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 46.6
    developer_ergonomics: 33.9
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cuein/refs/heads/main/screenshots/cuein-2026-07-25T210908.png
security:
- kind: authentication
  name: Cuein Authentication
  slug: cuein-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cuein Domain Security
  slug: cuein-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cuein Trust Center
  slug: cuein-trust-center
  summary_line: trust center published
slug: cuein
tags:
- Company
- Customer Experience
- Customer-Support
- Conversation Intelligence
- Generative AI
- Insights
- Knowledge Base
- Contact Center
website: https://developer.cuein.ai/
---
