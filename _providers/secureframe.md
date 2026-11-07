---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://secureframe.com/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: First-party hosted (remote) Model Context Protocol server exposing the Secureframe compliance platform as 112 tools across 41 categories — 63 read, 49 write — mapped one-for-one onto the Public API op
  name: Secureframe MCP Server
  slug: mcp-server
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and updating Cloud Resources.
  name: Secureframe Cloud Resource API
  slug: secureframe-cloud-resource-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and creating Framework Asset Scopes. A Framework Asset Scope defines the scope of an asset (e.g., a Cloud Resource) within a Framework. Framework Asset Scop
  name: Secureframe Cloud Resource Framework Asset Scope API
  slug: secureframe-cloud-resource-framework-asset-scope-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting Comments.
  name: Secureframe Comment API
  slug: secureframe-comment-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Controls.
  name: Secureframe Control API
  slug: secureframe-control-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for publishing data to a custom integration.
  name: Secureframe Custom Integration API
  slug: secureframe-custom-integration-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Devices.
  name: Secureframe Device API
  slug: secureframe-device-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and creating Framework Asset Scopes. A Framework Asset Scope defines the scope of an asset (e.g., a Device) within a Framework. Framework Asset Scopes are i
  name: Secureframe Device Framework Asset Scope API
  slug: secureframe-device-framework-asset-scope-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Evidence.
  name: Secureframe Evidence API
  slug: secureframe-evidence-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for staging a direct-to-storage file upload.
  name: Secureframe File Upload API
  slug: secureframe-file-upload-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Frameworks.
  name: Secureframe Framework API
  slug: secureframe-framework-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Framework Requirements.
  name: Secureframe Framework Requirement API
  slug: secureframe-framework-requirement-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and archiving Integration Connections.
  name: Secureframe Integration Connection API
  slug: secureframe-integration-connection-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting Knowledge Base Answers.
  name: Secureframe Knowledge Base Answer API
  slug: secureframe-knowledge-base-answer-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting Knowledge Base Questions.
  name: Secureframe Knowledge Base Question API
  slug: secureframe-knowledge-base-question-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and discarding POA&M (Plan of Action & Milestones) items.
  name: Secureframe POA&M Item API
  slug: secureframe-poa-m-item-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Policies. Policies are returned in every status, including drafts and archived ones. Filter with `?q=status:published` to narrow. Note that `q` free-text se
  name: Secureframe Policy API
  slug: secureframe-policy-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and updating Repositories.
  name: Secureframe Repository API
  slug: secureframe-repository-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Framework Asset Scopes. A Framework Asset Scope defines the scope of an asset (e.g., a Repository) within a Framework. Framework Asset Scopes are immutable.
  name: Secureframe Repository Framework Asset Scope API
  slug: secureframe-repository-framework-asset-scope-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Risks.
  name: Secureframe Risk API
  slug: secureframe-risk-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for creating Security Questionnaires.
  name: Secureframe Security Questionnaire API
  slug: secureframe-security-questionnaire-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting SSP Duties.
  name: Secureframe SSP Duty API
  slug: secureframe-ssp-duty-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, and deleting SSP Duty Roles.
  name: Secureframe SSP Duty Role API
  slug: secureframe-ssp-duty-role-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting SSP Policies.
  name: Secureframe SSP Policy API
  slug: secureframe-ssp-policy-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and creating SSP Reports.
  name: Secureframe SSP Report API
  slug: secureframe-ssp-report-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and updating SSP Report Assessment Objectives.
  name: Secureframe SSP Report Assessment Objective API
  slug: secureframe-ssp-report-assessment-objective-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and updating SSP Report Sections.
  name: Secureframe SSP Report Section API
  slug: secureframe-ssp-report-section-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and updating SSP Report Section Blocks.
  name: Secureframe SSP Report Section Block API
  slug: secureframe-ssp-report-section-block-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting SSP Roles.
  name: Secureframe SSP Role API
  slug: secureframe-ssp-role-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, updating, and deleting SSP Vendors.
  name: Secureframe SSP Vendor API
  slug: secureframe-ssp-vendor-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading Tasks.
  name: Secureframe Task API
  slug: secureframe-task-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading, creating, and updating Tests.
  name: Secureframe Test API
  slug: secureframe-test-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for creating Evidence for a Test.
  name: Secureframe Test Evidence API
  slug: secureframe-test-evidence-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for creating a Test Export for a Test.
  name: Secureframe Test Export API
  slug: secureframe-test-export-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading a Test Export.
  name: Secureframe Test Export Reading API
  slug: secureframe-test-export-reading-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and archiving Vendors for companies using the Third Party Risk Management.
  name: Secureframe Third Party Risk Management Vendor API
  slug: secureframe-third-party-risk-management-vendor-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: 'This document describes the API for reading and updating Trust Center Requests.\ Note: In order to access this API, you need to have paid features enabled for Trust.'
  name: Secureframe Trust Center Request API
  slug: secureframe-trust-center-request-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and linking User Accounts.
  name: Secureframe User Account API
  slug: secureframe-user-account-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and updating Users.
  name: Secureframe User API
  slug: secureframe-user-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for creating Evidence for a User.
  name: Secureframe User Evidence API
  slug: secureframe-user-evidence-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for retrieving user security settings for the provided API key's company.
  name: Secureframe User Security Settings API
  slug: secureframe-user-security-settings-api
- baseURL: https://api.secureframe.com
  baseurl_source: declared
  description: This document describes the API for reading and archiving Vendors.
  name: Secureframe Vendor API
  slug: secureframe-vendor-api
artifact_total: 56
common:
- group: other
  href: https://artifacts.apis.io/secureframe/capabilities/secureframe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/secureframe-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://secureframe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.secureframe.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.secureframe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.secureframe.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.secureframe.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://secureframe.com/pricing
- group: commercial
  href: https://artifacts.apis.io/secureframe/plans/secureframe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/secureframe-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/secureframe/rate-limits/secureframe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/secureframe-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://app.secureframe.com/login
- group: start
  title: ''
  type: SignUp
  url: https://secureframe.com/request-demo
- group: operate
  title: ''
  type: Support
  url: https://secureframe.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.secureframe.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secureframe.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://secureframe.com/product-updates
- group: operate
  href: https://artifacts.apis.io/secureframe/changelog/secureframe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/secureframe-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secureframe.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secureframe.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/secureframe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/secureframe
- group: company
  title: ''
  type: Blog
  url: https://secureframe.com/blog
- group: agent
  href: https://artifacts.apis.io/secureframe/mcp/secureframe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/secureframe-mcp.yml
- group: build
  href: https://artifacts.apis.io/secureframe/mcp/secureframe-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/secureframe-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/secureframe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/secureframe/llms/secureframe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secureframe-llms.txt
- group: agent
  href: https://artifacts.apis.io/secureframe/well-known/secureframe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/secureframe-well-known.yml
- group: design
  href: https://artifacts.apis.io/secureframe/conformance/secureframe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/secureframe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.secureframe.com/
- group: auth
  href: https://artifacts.apis.io/secureframe/security/secureframe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/secureframe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/secureframe/security/secureframe-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/secureframe-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/secureframe/security/secureframe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/secureframe-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/secureframe/security/secureframe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secureframe-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/secureframe/authentication/secureframe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/secureframe-authentication.yml
- group: auth
  href: https://artifacts.apis.io/secureframe/scopes/secureframe-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/secureframe-scopes.yml
- group: design
  href: https://artifacts.apis.io/secureframe/errors/secureframe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/secureframe-problem-types.yml
- group: design
  href: https://artifacts.apis.io/secureframe/conventions/secureframe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/secureframe-conventions.yml
- group: design
  href: https://artifacts.apis.io/secureframe/data-model/secureframe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/secureframe-data-model.yml
- group: design
  href: https://artifacts.apis.io/secureframe/lifecycle/secureframe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/secureframe-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/secureframe/lifecycle/secureframe-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/secureframe-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/secureframe/packages/secureframe-packages.yml
  title: ''
  type: Packages
  url: packages/secureframe-packages.yml
- group: other
  href: https://artifacts.apis.io/secureframe/overlays/secureframe-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/secureframe-public-api-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/secureframe/finops/secureframe-finops.yml
  title: ''
  type: FinOps
  url: finops/secureframe-finops.yml
created: '2026-05-08'
description: Secureframe automates security and privacy compliance for SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, CMMC, FedRAMP, NIST 800-171 and more. Its Public API is a 112-operation, JSON:API-shaped REST contract over the compliance record of truth — frameworks, requirements, controls, tests, evidence, policies, risks, personnel, devices, cloud resources, repositories, third-party vendors, trust center requests, and the System Security Plan and POA&M artifacts CMMC and FedRAMP assessments are conducted against. Secureframe also runs a first-party hosted MCP server that exposes all 112 operations as agent-callable tools over OAuth 2.1.
finops:
- has_sources: true
  method: derived
  name: Secureframe Finops
  primary_unit: subscription
  service_category: ''
  slug: secureframe-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/secureframe.png
layout: provider
mcp_servers:
- description: Secureframe publishes a first-party hosted (remote) MCP server that exposes its compliance platform — controls, tests, evidence, frameworks, risks, vendors, personnel, SSP and POA&M records — as 112 M
  name: Secureframe MCP Server
  slug: secureframe-mcp-server
modified: '2026-08-27'
name: Secureframe
nav: Providers
network: true
overview: 'Secureframe publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cloud Resource API, Cloud Resource Framework Asset Scope API, Comment API, and 39 more. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Risk Management.


  The Secureframe catalog on APIs.io includes 1 Spectral governance ruleset.


  Secureframe''s developer surface includes documentation, API reference, pricing, signup flow, support, changelog, engineering blog, and 35 more developer resources.'
plans:
- name: Secureframe Plans Pricing
  plan_count: 3
  slug: secureframe-plans-pricing
- name: Secureframe Price Estimates
  plan_count: 0
  slug: secureframe-price-estimates
random_paper: 18
rate_limits:
- limit_count: 1
  name: Secureframe Rate Limits
  slug: secureframe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Secureframe API Rules
  rule_count: 59
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 6
  slug: secureframe-rules
scopes:
- name: Secureframe Scopes
  scope_count: 1
  slug: secureframe-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 48.4
    developer_ergonomics: 37.5
    discoverability: 75.0
    operational_transparency: 73.7
  previous_composite: 59.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/secureframe/secureframe-2026-06-20T193625.png
security:
- kind: authentication
  name: Secureframe Authentication
  slug: secureframe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Secureframe Domain Security
  slug: secureframe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Secureframe Vulnerability Disclosure
  slug: secureframe-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Secureframe Trust Center
  slug: secureframe-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
skill_count: 3
skills:
- name: secureframe-asset-framework-scoping
  slug: secureframe-asset-framework-scoping
- name: secureframe-audit-evidence-collection
  slug: secureframe-audit-evidence-collection
- name: secureframe-poam-management
  slug: secureframe-poam-management
slug: secureframe
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Risk Management
- CMMC
- FedRAMP
- Security
- Audit
- Trust
website: https://secureframe.com/
---
