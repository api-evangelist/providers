---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hyperscience Agentic Access
  operation_count: 20
  slug: hyperscience-agentic-access
  summary_line: 20 operations · 4 acting
api_count: 1
apis:
- description: REST API for the Hypercell platform — submit documents, retrieve extraction results, manage flows and human-review queues. Each tenant receives its own base URL.
  name: Hyperscience REST API
  slug: rest
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Audit Logs API from Hyperscience — 3 operation(s) for audit logs.
  name: Hyperscience Audit Logs API
  slug: hyperscience-audit-logs-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Cases API from Hyperscience — 2 operation(s) for cases.
  name: Hyperscience Cases API
  slug: hyperscience-cases-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Documents API from Hyperscience — 2 operation(s) for documents.
  name: Hyperscience Documents API
  slug: hyperscience-documents-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Flow Runs API from Hyperscience — 2 operation(s) for flow runs.
  name: Hyperscience Flow Runs API
  slug: hyperscience-flow-runs-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Flows API from Hyperscience — 2 operation(s) for flows.
  name: Hyperscience Flows API
  slug: hyperscience-flows-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Layouts API from Hyperscience — 2 operation(s) for layouts.
  name: Hyperscience Layouts API
  slug: hyperscience-layouts-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Pages API from Hyperscience — 2 operation(s) for pages.
  name: Hyperscience Pages API
  slug: hyperscience-pages-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Submissions API from Hyperscience — 2 operation(s) for submissions.
  name: Hyperscience Submissions API
  slug: hyperscience-submissions-api
- baseURL: https://<tenant>.hyperscience.net
  baseurl_source: declared
  description: The Version API from Hyperscience — 1 operation(s) for version.
  name: Hyperscience Version API
  slug: hyperscience-version-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hyperscience Audit Logs API
  slug: open-hyperscience-audit-logs-api
- collection_type: open
  name: Hyperscience Audit Logs Cases API
  slug: open-hyperscience-cases-api
- collection_type: open
  name: Hyperscience Audit Logs Documents API
  slug: open-hyperscience-documents-api
- collection_type: open
  name: Hyperscience Audit Logs Flow Runs API
  slug: open-hyperscience-flow-runs-api
- collection_type: open
  name: Hyperscience Audit Logs Flows API
  slug: open-hyperscience-flows-api
- collection_type: open
  name: Hyperscience Audit Logs Layouts API
  slug: open-hyperscience-layouts-api
- collection_type: open
  name: Hyperscience Audit Logs Pages API
  slug: open-hyperscience-pages-api
- collection_type: open
  name: Hyperscience Audit Logs Submissions API
  slug: open-hyperscience-submissions-api
- collection_type: open
  name: Hyperscience Audit Logs Version API
  slug: open-hyperscience-version-api
- collection_type: open
  name: Hyperscience API
  slug: open-hyperscience
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperscience-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hyperscience-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyperscience-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperscience-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperscience-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hyperscience-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyperscience
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperscience
- group: company
  title: ''
  type: Website
  url: https://www.hyperscience.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hyperscience.ai/contact/
- group: auth
  title: ''
  type: SecurityAndCompliance
  url: https://www.hyperscience.ai/security/
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperscience-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperscience-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperscience-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://hyperscience.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.hyperscience.ai/blog/
created: '2026-05-08'
description: Hyperscience provides enterprise-grade intelligent document processing (IDP) via the Hypercell platform. Capabilities include automated extraction, classification, GenAI processing, human-in-the-loop validation, and industry/use-case specific products (Hypercell for Freight Pay, GenAI, SNAP). Hyperscience exposes a REST API and a Flows SDK to its customers. FedRAMP High authorised; deployed in cloud and on-premises configurations.
finops:
- name: Hyperscience Finops
  service_category: Enterprise IDP
  slug: hyperscience-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperscience.png
layout: provider
modified: '2026-05-08'
name: Hyperscience
nav: Providers
network: true
overview: 'Hyperscience publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, Cases API, Documents API, and 6 more. Tagged areas include Artificial Intelligence, Document AI, IDP, Enterprise, and Automation.


  Hyperscience''s developer surface includes authentication, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Hyperscience Plans Pricing
  plan_count: 4
  slug: hyperscience-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Hyperscience Rate Limits
  slug: hyperscience-rate-limits
scopes:
- name: Hyperscience Scopes
  scope_count: 0
  slug: hyperscience-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 44.2
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperscience/refs/heads/main/screenshots/hyperscience-2026-06-20T183049.png
security:
- kind: authentication
  name: Hyperscience Authentication
  slug: hyperscience-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hyperscience Domain Security
  slug: hyperscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hyperscience Vulnerability Disclosure
  slug: hyperscience-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Hyperscience Trust Center
  slug: hyperscience-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
slug: hyperscience
tags:
- Artificial Intelligence
- Document AI
- IDP
- Enterprise
- Automation
- GenAI
- FedRAMP
website: https://www.hyperscience.ai/
---
