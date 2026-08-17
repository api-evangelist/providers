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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scribe Agentic Access
  operation_count: 4
  slug: scribe-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: The Documents API from Scribe — 2 operation(s) for documents.
  name: Scribe Documents API
  slug: scribe-documents-api
- description: The Search API from Scribe — 1 operation(s) for search.
  name: Scribe Search API
  slug: scribe-search-api
- description: The Teams API from Scribe — 1 operation(s) for teams.
  name: Scribe Teams API
  slug: scribe-teams-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scribe Search & Retrieval Documents API
  slug: open-scribe-documents-api
- collection_type: open
  name: Scribe & Retrieval Documents Search API
  slug: open-scribe-search-api
- collection_type: open
  name: Scribe Search & Retrieval Documents Teams API
  slug: open-scribe-teams-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/scribe-search-retrieval-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://scribe.com
- group: docs
  title: ''
  type: Documentation
  url: https://public-api.scribehow.com/schema/redoc/
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.scribehow.com/schema/redoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://scribehow.com/settings?tab=developerAccess
- group: operate
  title: ''
  type: Support
  url: https://support.scribehow.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://scribe.com/library
- group: commercial
  title: ''
  type: Pricing
  url: https://scribe.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://scribehow.com/signup?plan=free
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scribe.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scribe.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scribe.com
- group: auth
  title: ''
  type: Compliance
  url: https://scribe.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/scribe-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scribe-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scribe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scribe-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scribe-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scribe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scribe-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scribe-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scribe-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scribe-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scribe-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scribe-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scribe-llms.txt
created: '2026-07-17'
description: Scribe (scribehow) is an AI workflow-documentation platform founded in 2019 that automatically turns any process or software walkthrough into a step-by-step guide. Its products — Scribe Capture, the knowledge base, and the newer Scribe Optimize workflow-mapping platform — are used by more than five million people across a large share of the Fortune 500. For developers, Scribe publishes a read-only Search & Retrieval API (OpenAPI 3.1) that searches, lists, and retrieves an organization's Scribe Documents and Knowledge Pages for integration into custom applications and AI agents. Public API access is an Enterprise-plan feature authenticated with a static API key sent in the X-API-Key header. The company is backed by Amplify Partners, Redpoint Ventures, Tiger Global, StepStone, Morado Ventures, and New York Life Ventures, and reached a $1.3B valuation with its 2025 Series C.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scribe.png
layout: provider
mcp_servers:
- description: ''
  name: scribe-mcp.yml
  slug: scribe-mcpyml
modified: '2026-07-21'
name: Scribe
nav: Providers
network: true
overview: 'Scribe publishes 3 APIs on the [APIs.io](https://apis.io/) network: Documents API, Search API, and Teams API. Tagged areas include Company, Ai Ml, Documentation, Knowledge Management, and Search.


  Scribe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 36
rate_limits:
- limit_count: 2
  name: Scribe Rate Limits
  slug: scribe-rate-limits
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.7
    developer_ergonomics: 47.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Scribe Authentication
  slug: scribe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scribe Domain Security
  slug: scribe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Scribe Trust Center
  slug: scribe-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, FERPA, GDPR, US State Privacy Laws
slug: scribe
tags:
- Company
- Ai Ml
- Documentation
- Knowledge Management
- Search
- Workflow
- Process Documentation
- Enterprise
website: https://scribe.com
---
