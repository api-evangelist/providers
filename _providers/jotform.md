---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Jotform Agentic Access
  operation_count: 45
  slug: jotform-agentic-access
  summary_line: 45 operations · 21 acting
api_count: 1
apis:
- description: EU-resident variant of the Jotform API for customers on EU plans / EU data residency.
  name: Jotform REST API (EU)
  slug: rest-eu
- description: HIPAA-compliant variant of the Jotform API for healthcare customers on Gold/Enterprise tiers.
  name: Jotform REST API (HIPAA)
  slug: rest-hipaa
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The Folder API from Jotform — 3 operation(s) for folder.
  name: Jotform Folder API
  slug: jotform-folder-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The Form API from Jotform — 10 operation(s) for form.
  name: Jotform Form API
  slug: jotform-form-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The Label API from Jotform — 4 operation(s) for label.
  name: Jotform Label API
  slug: jotform-label-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The Report API from Jotform — 3 operation(s) for report.
  name: Jotform Report API
  slug: jotform-report-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The Submission API from Jotform — 3 operation(s) for submission.
  name: Jotform Submission API
  slug: jotform-submission-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The System API from Jotform — 1 operation(s) for system.
  name: Jotform System API
  slug: jotform-system-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The User API from Jotform — 13 operation(s) for user.
  name: Jotform User API
  slug: jotform-user-api
- baseURL: https://api.jotform.com
  baseurl_source: declared
  description: The Webhook API from Jotform — 2 operation(s) for webhook.
  name: Jotform Webhook API
  slug: jotform-webhook-api
- description: Official remote Model Context Protocol server (Streamable HTTP, OAuth 2.0 authorization code with PKCE S256, dynamic client registration, scopes readOnly and full). Main server at https://mcp.jotform.
  name: Jotform MCP Server
  slug: mcp-server
artifact_total: 39
asyncapis:
- description: AsyncAPI definition for Jotform's webhook surface. Jotform delivers a POST request to a configured webhook URL each time a form receives a submission. The request body is sent as multipart/form-data a
  name: Jotform Webhooks AsyncAPI
  slug: jotform-asyncapi
- description: ''
  name: Jotform Webhooks
  slug: jotform-webhooks
collections:
- collection_type: open
  name: Jotform REST Folder API
  slug: open-jotform-folder-api
- collection_type: open
  name: Jotform REST Folder Form API
  slug: open-jotform-form-api
- collection_type: open
  name: Jotform REST Folder Label API
  slug: open-jotform-label-api
- collection_type: open
  name: Jotform REST Folder Report API
  slug: open-jotform-report-api
- collection_type: open
  name: Jotform REST Folder Submission API
  slug: open-jotform-submission-api
- collection_type: open
  name: Jotform REST Folder System API
  slug: open-jotform-system-api
- collection_type: open
  name: Jotform REST Folder User API
  slug: open-jotform-user-api
- collection_type: open
  name: Jotform REST Folder Webhook API
  slug: open-jotform-webhook-api
- collection_type: open
  name: Jotform REST API
  slug: open-jotform
common:
- group: other
  href: https://artifacts.apis.io/jotform/capabilities/jotform-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jotform-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/jotform/asyncapi/jotform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jotform-webhooks.yml
- group: design
  href: https://artifacts.apis.io/jotform/errors/jotform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jotform-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jotform/rules/jotform-rules.yml
  title: ''
  type: Spectral
  url: rules/jotform-rules.yml
- group: design
  href: https://artifacts.apis.io/jotform/rules/jotform-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/jotform-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/jotform/vocabulary/jotform-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jotform-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/jotform/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/jotform/components/jotform-components.yml
  title: ''
  type: Components
  url: components/jotform-components.yml
- group: design
  href: https://artifacts.apis.io/jotform/conventions/jotform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jotform-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.jotform.com/security/
- group: auth
  href: https://artifacts.apis.io/jotform/security/jotform-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jotform-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jotform.com/vulnerability-disclosure-program/#program-rules
- group: auth
  href: https://artifacts.apis.io/jotform/scopes/jotform-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/jotform-scopes.yml
- group: design
  href: https://artifacts.apis.io/jotform/lifecycle/jotform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jotform-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jotform/conformance/jotform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jotform-conformance.yml
- group: build
  href: https://artifacts.apis.io/jotform/mcp/jotform-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/jotform-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/jotform/mcp/jotform-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jotform-mcp.yml
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-ws-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-webservices-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-webservices-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-status-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-devportal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-devportal-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-apidocs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-apidocs-security.txt
- group: auth
  href: https://artifacts.apis.io/jotform/well-known/jotform-api-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jotform-api-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/jotform/well-known/jotform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jotform-well-known.yml
- group: other
  href: https://artifacts.apis.io/jotform/hosts/jotform-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jotform-hosts.yml
- group: build
  href: https://artifacts.apis.io/jotform/integrations/jotform-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/jotform-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/jotform/packages/jotform-packages.yml
  title: ''
  type: Packages
  url: packages/jotform-packages.yml
- group: agent
  href: https://artifacts.apis.io/jotform/agentic-access/jotform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jotform-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jotform/security/jotform-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jotform-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jotform/security/jotform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jotform-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jotform/authentication/jotform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jotform-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.jotform.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jotform
- group: company
  title: ''
  type: Website
  url: https://www.jotform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.jotform.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jotform.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jotform
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jotform.com/
- group: commercial
  href: https://artifacts.apis.io/jotform/plans/jotform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jotform-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/jotform/rate-limits/jotform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jotform-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jotform/finops/jotform-finops.yml
  title: ''
  type: FinOps
  url: finops/jotform-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.jotform.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://api.jotform.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.jotform.com/docs/#gettingstarted
- group: operate
  title: ''
  type: Support
  url: https://www.jotform.com/help/
- group: operate
  title: ''
  type: Community
  url: https://www.jotform.com/answers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jotform.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jotform.com/privacy/
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://www.jotform.com/accessibility/
- group: other
  title: ''
  type: Subprocessors
  url: https://www.jotform.com/subprocessors/
- group: other
  title: ''
  type: DataResidency
  url: https://www.jotform.com/enterprise/local-data-residency/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.jotform.com/privacy/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.jotform.com/.well-known/security.txt
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://www.jotform.com/developers/mcp/?tab=mcp
created: '2026-05-08'
description: Jotform is an online form builder with strong workflow, payments, e-signature and data collection capabilities. The Jotform REST API exposes forms, submissions, reports, folders, users, labels, files and webhooks across three regional/compliance hosts (api.jotform.com US standard, eu-api.jotform.com EU, hipaa-api.jotform.com HIPAA), authenticated with an API key sent as the APIKEY header or apiKey query parameter. Jotform also operates an official remote MCP server at https://mcp.jotform.com (OAuth 2.0 with PKCE, scopes readOnly and full) with product servers for Jotform Sign, Jotform Apps and a website Form Backend, and publishes the full tool reference as JSON.
finops:
- has_sources: true
  method: generated
  name: Jotform Finops
  primary_unit: plan-month
  service_category: Forms / Workflow
  slug: jotform-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jotform.png
layout: provider
mcp_servers:
- description: Jotform operates an official remote MCP server at https://mcp.jotform.com (Streamable HTTP, OAuth 2.0 authorization code with PKCE S256, dynamic client registration, scopes readOnly and full). One mai
  name: Jotform MCP Server
  slug: jotform
modified: '2026-11-05'
name: Jotform
nav: Providers
network: true
overview: 'Jotform publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Folder API, Form API, Label API, and 8 more. Tagged areas include Forms, Surveys, No-Code, Data Collection, and Workflows.


  The Jotform catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 2 Spectral governance rulesets.


  Jotform''s developer surface includes authentication, engineering blog, documentation, pricing, API reference, getting-started guide, support, and 49 more developer resources.'
plans:
- name: Jotform Plans Pricing
  plan_count: 5
  slug: jotform-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Jotform Rate Limits
  slug: jotform-rate-limits
rules:
- authorship: generated
  effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Jotform — asyncapi rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: jotform-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Jotform API Rules
  rule_count: 50
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 2
  slug: jotform-rules
scopes:
- name: Jotform Scopes
  scope_count: 2
  slug: jotform-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 70.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 69.8
    catalog_earned_first_party: 24.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.8
  facets:
    access_clarity: 86.8
    contract_governance: 35.6
    contract_quality: 53.0
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: ferpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jotform/jotform-2026-06-20T183806.png
security:
- kind: authentication
  name: Jotform Authentication
  slug: jotform-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Jotform Domain Security
  slug: jotform-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jotform Vulnerability Disclosure
  slug: jotform-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jotform Trust Center
  slug: jotform-trust-center
  summary_line: PCI DSS Service Provider Level 1, SOC 2 Type II (dedicated Enterprise environment), GDPR, CCPA, HIPAA (BAA), FERPA, HECVAT, StateRAMP Security Snapshot
skill_count: 5
skills:
- name: form-creator
  slug: jotform-form-creator
- name: jotform-list-forms-and-submissions
  slug: jotform-list-forms-and-submissions
- name: jotform-manage-submissions
  slug: jotform-manage-submissions
- name: jotform-register-webhook
  slug: jotform-register-webhook
- name: jotform-reports
  slug: jotform-reports
slug: jotform
tags:
- Forms
- Surveys
- No-Code
- Data Collection
- Workflows
- HIPAA
- EU
- MCP
- E-Signature
- Webhook
- Online Payments
website: https://www.jotform.com/
---
