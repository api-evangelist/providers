---
access_model:
  confidence: high
  label: Anonymous public read - no key, no registration, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.arlp.com/wp-json/
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The public, read-only WordPress REST API served by Alliance Resource Partners' corporate site at www.arlp.com. Anonymous - no key, no OAuth, no registration - and verified returning HTTP 200 on 2026-0
  name: Alliance Resource Partners Content API
  slug: alliance-resource-partners-content-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.arlp.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alliance-resource-partners-lp
- group: operate
  title: ''
  type: Support
  url: https://www.arlp.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arlp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arlp.com/privacy-statement/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.arlp.com/overview/default.aspx
- group: auth
  title: ''
  type: Authentication
  url: authentication/alliance-resource-partners-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alliance-resource-partners-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alliance-resource-partners-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alliance-resource-partners-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alliance-resource-partners-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alliance-resource-partners-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/alliance-resource-partners-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alliance-resource-partners-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alliance-resource-partners-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/alliance-resource-partners-content-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alliance-resource-partners-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/alliance-resource-partners-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alliance-resource-partners-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alliance-resource-partners-domain-security.yml
created: '2026-04-19'
description: 'Alliance Resource Partners, L.P. (NASDAQ: ARLP) is a diversified energy and natural-resource partnership headquartered in Tulsa, Oklahoma. It is the largest coal producer in the eastern United States, operating underground and surface mines across the Illinois Basin and Appalachia, and it holds an oil and gas mineral and royalty portfolio alongside a growth-investment arm covering other energy and infrastructure ventures. ARLP runs no developer program: it publishes no API documentation, no OpenAPI, no SDK, no API pricing and no developer portal, and the api.arlp.com and developer.arlp.com hosts once listed here do not resolve in DNS. The only machine-readable interface the company serves is the read-only WordPress REST API behind its corporate site at www.arlp.com, which returns ARLP''s own published corporate content - business segments, sustainability posture, careers, contact and legal pages, media, taxonomy and cross-content search - anonymously as JSON. Any operational
  data exchange with ARLP (customer contracts, rail and barge logistics, mine reporting, royalty statements) is a bilateral commercial agreement, not a published API product.'
examples:
- key_count: 13
  name: Alliance Resource Partners Content Types
  slug: alliance-resource-partners-content-types
- key_count: 11
  name: Alliance Resource Partners Oembed
  slug: alliance-resource-partners-oembed
- key_count: 2
  name: Alliance Resource Partners Statuses
  slug: alliance-resource-partners-statuses
- key_count: 5
  name: Alliance Resource Partners Taxonomies
  slug: alliance-resource-partners-taxonomies
finops:
- name: Alliance Resource Partners Finops
  service_category: Energy / Mining Data
  slug: alliance-resource-partners-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alliance-resource-partners.png
layout: provider
mcp_servers:
- description: ''
  name: Alliance Resource Partners MCP Server
  slug: alliance-resource-partners-mcp-server
modified: '2026-09-01'
name: Alliance Resource Partners
nav: Providers
network: true
overview: 'Alliance Resource Partners publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Coal, Mining, Energy, Royalties, and Natural Resources.


  Alliance Resource Partners'' developer surface includes support, authentication, code examples, and 19 more developer resources.'
plans:
- name: Alliance Resource Partners Plans Pricing
  plan_count: 0
  slug: alliance-resource-partners-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Alliance Resource Partners Rate Limits
  slug: alliance-resource-partners-rate-limits
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 13.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 15.6
    developer_ergonomics: 18.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 9.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/alliance-resource-partners/refs/heads/main/screenshots/alliance-resource-partners-2026-06-20T171531.png
security:
- kind: authentication
  name: Alliance Resource Partners Authentication
  slug: alliance-resource-partners-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Alliance Resource Partners Domain Security
  slug: alliance-resource-partners-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alliance-resource-partners
tags:
- Coal
- Mining
- Energy
- Royalties
- Natural Resources
- Content
- Corporate
website: https://www.arlp.com
---
