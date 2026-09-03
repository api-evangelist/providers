---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
    error_semantics: verified
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
  score: 26.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Boostup Agentic Access
  operation_count: 3
  slug: boostup-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://app.boostup.ai/export
  baseurl_source: declared
  description: The Export API from Boostup — 3 operation(s) for export.
  name: Boostup Export API
  slug: boostup-export-api
arazzos:
- description: Pull the first page of Opportunities, Accounts, and Forecast Submissions out of the Boostup / Terret Export API in one run, ready to page through with limit/skip.
  name: Export all Boostup revenue data
  slug: boostup-export-all-revenue-data
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Boostup Export API
  slug: open-boostup-export-api
common:
- group: design
  title: ''
  type: Arazzo
  url: arazzo/boostup-export-all-revenue-data.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/boostup-export-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boostup-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/boostup-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/boostup-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boostup-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boostup-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boostup-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/boostup-problem-types.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boostup-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/boostup-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boostup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boostup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boostup-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/boostup-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/boostup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boostup-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.terret.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.terret.ai/blogs
- group: docs
  title: ''
  type: Documentation
  url: https://app.boostup.ai/export/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://app.boostup.ai/export/docs/
- group: start
  title: ''
  type: SignUp
  url: https://app.boostup.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.boostup.ai/login
- group: operate
  title: ''
  type: Support
  url: https://support.boostup.ai/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.terret.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.terret.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.boostup.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://www.terret.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.terret.ai/security
- group: auth
  title: ''
  type: Security
  url: https://www.terret.ai/vulnerability-disclosure-policy/
created: '2026-07-17'
description: Boostup (now operating as Terret, terret.ai) is an AI-powered revenue intelligence platform that connects data across a company's revenue systems to analyze sales performance, forecast pipeline, and translate insights into real-time execution guidance for sales teams. Its products include Terret Nexus (an answer-to-action revenue engine that generates playbooks), Terret Forecast (pipeline forecasting), and Terret Conversation Intelligence (call analysis). For developers, Boostup exposes a public REST data-export API at app.boostup.ai/export that lets customers programmatically pull their Opportunities, Accounts, and Forecast Submissions out of the platform for in-house analysis and reporting. The API is authenticated with API keys passed in the Authorization header, returns JSON paginated in batches of up to 1000 records, and supports date-based filtering on close/create/update times. The company was surfaced as a portfolio company of Canaan Partners.
image: https://terret.ai/images/nexus-og-logo-only.jpg
layout: provider
modified: '2026-08-13'
name: Boostup
nav: Providers
network: true
overview: 'Boostup publishes 1 API on the [APIs.io](https://apis.io/) network: Export API. Tagged areas include Company, Revenue Intelligence, Sales, Forecasting, and Analytics.


  Boostup''s developer surface includes authentication, engineering blog, documentation, API reference, signup flow, support, and 25 more developer resources.'
plans:
- name: Boostup Plans Pricing
  plan_count: 0
  slug: boostup-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Boostup Rate Limits
  slug: boostup-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boostup/refs/heads/main/screenshots/boostup-2026-07-25T203626.png
security:
- kind: authentication
  name: Boostup Authentication
  slug: boostup-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Boostup Domain Security
  slug: boostup-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Boostup Vulnerability Disclosure
  slug: boostup-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Boostup Trust Center
  slug: boostup-trust-center
  summary_line: SOC 2, CSA STAR, FIPS 140
slug: boostup
tags:
- Company
- Revenue Intelligence
- Sales
- Forecasting
- Analytics
- Revenue Operations
- Conversation Intelligence
- Data Export
- CRM
website: https://www.terret.ai/
---
