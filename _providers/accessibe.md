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
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Accessibe Agentic Access
  operation_count: 7
  slug: accessibe-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: The accessFlow Model Context Protocol server connects AI clients such as GitHub Copilot and Cursor directly to accessFlow accessibility data. It exposes three tools — getMostUrgentIssues, getIssueReme
  name: accessFlow MCP Server
  slug: accessflow-mcp
- baseURL: https://dashboard.accessibe.com/api/v1/partners
  baseurl_source: declared
  description: The Accounts API from accessiBe — 5 operation(s) for accounts.
  name: accessiBe Accounts API
  slug: accessibe-accounts-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/accessibe/plans/accessibe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accessibe-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/accessibe/capabilities/accessibe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/accessibe-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/accessibe/agentic-access/accessibe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accessibe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/accessibe/security/accessibe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/accessibe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/accessibe/security/accessibe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accessibe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accessibe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.accessibe.com/api/v1/partners/docs
- group: docs
  title: ''
  type: Documentation
  url: https://accessibe.com/support
- group: docs
  title: ''
  type: APIReference
  url: https://dashboard.accessibe.com/api/v1/partners/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://accessibe.com/accessflow-integrate
- group: operate
  title: ''
  type: Support
  url: https://accessibe.com/support
- group: company
  title: ''
  type: Blog
  url: https://accessibe.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://accessibe.com/pricing/accesswidget
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.accessibe.com/app/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.accessibe.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accessibe.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accessibe.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accessibe.com
- group: auth
  title: ''
  type: Compliance
  url: https://accessibe.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.accessibe.com/hc/en-us/categories/15274937179922-Release-Notes
- group: operate
  href: https://artifacts.apis.io/accessibe/changelog/accessibe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/accessibe-changelog.yml
- group: agent
  href: https://artifacts.apis.io/accessibe/llms/accessibe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accessibe-llms.txt
- group: build
  href: https://artifacts.apis.io/accessibe/packages/accessibe-packages.yml
  title: ''
  type: Packages
  url: packages/accessibe-packages.yml
- group: build
  href: https://artifacts.apis.io/accessibe/packages/accessibe-packages.yml
  title: ''
  type: SDKs
  url: packages/accessibe-packages.yml
- group: agent
  href: https://artifacts.apis.io/accessibe/mcp/accessibe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accessibe-mcp.yml
- group: build
  href: https://artifacts.apis.io/accessibe/mcp/accessibe-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/accessibe-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/accessibe/authentication/accessibe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accessibe-authentication.yml
- group: design
  href: https://artifacts.apis.io/accessibe/conventions/accessibe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accessibe-conventions.yml
- group: design
  href: https://artifacts.apis.io/accessibe/conventions/accessibe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/accessibe-conventions.yml
- group: design
  href: https://artifacts.apis.io/accessibe/errors/accessibe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accessibe-problem-types.yml
- group: design
  href: https://artifacts.apis.io/accessibe/lifecycle/accessibe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accessibe-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/accessibe/conformance/accessibe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accessibe-conformance.yml
- group: design
  href: https://artifacts.apis.io/accessibe/data-model/accessibe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accessibe-data-model.yml
- group: design
  href: https://artifacts.apis.io/accessibe/components/accessibe-components.yml
  title: ''
  type: Components
  url: components/accessibe-components.yml
- group: agent
  href: https://artifacts.apis.io/accessibe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/accessibe/overlays/accessibe-partners-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/accessibe-partners-overlay.yaml
created: '2026-07-31'
description: accessiBe is a web accessibility technology company whose products help organizations make websites and web applications usable by people with disabilities and compliant with WCAG, the ADA, Section 508, AODA and the European Accessibility Act. Its portfolio spans accessWidget (an AI-driven remediation layer and end-user accessibility interface installed via an embed script), accessScan (a free single-URL compliance checker), accessFlow (a developer-first accessibility testing and monitoring platform with an SDK for Playwright, Cypress and Selenium plus CI/CD integrations), and accessServices (expert audits, user testing by people with disabilities, file and PDF remediation, and VPAT authoring). Developer surfaces include a documented Partners API for programmatic accessWidget license management and a first-party accessFlow MCP server that connects IDE AI assistants to accessibility audit findings and remediation guidance.
finops:
- has_sources: true
  method: derived
  name: Accessibe Finops
  primary_unit: website
  service_category: ''
  slug: accessibe-finops
  template: false
image: https://accessibe.com/wp-content/uploads/2026/01/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at flow-mcp.accessibe.com; 3 tools listed.
  name: accessiBe MCP Server
  slug: flow-mcp
modified: '2026-07-31'
name: accessiBe
nav: Providers
network: true
overview: 'accessiBe publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, and 1 more. Tagged areas include Company, Accessibility, Web Accessibility, WCAG, and ADA Compliance.


  accessiBe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Accessibe Plans Pricing
  plan_count: 7
  slug: accessibe-plans-pricing
- name: Accessibe Price Estimates
  plan_count: 0
  slug: accessibe-price-estimates
random_paper: 18
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 51.4
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/accessibe/accessibe-2026-08-07T160757.png
security:
- kind: authentication
  name: Accessibe Authentication
  slug: accessibe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Accessibe Domain Security
  slug: accessibe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accessibe Trust Center
  slug: accessibe-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: Triage and remediate accessibility issues with the accessFlow MCP server
  slug: accessibe-accessflow-remediation
- name: Bulk-create or bulk-update accessWidget licenses safely
  slug: accessibe-bulk-license-batch
- name: Provision an accessWidget license for a domain
  slug: accessibe-provision-accesswidget-license
slug: accessibe
tags:
- Company
- Accessibility
- Web Accessibility
- WCAG
- ADA Compliance
- Compliance
- Developer Tools
- Testing
- Quality Assurance
- Artificial Intelligence
website: https://accessibe.com
---
