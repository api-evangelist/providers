---
access_model:
  confidence: high
  label: Enterprise · Sales-assisted — no published pricing, access requires an AppOmni tenant
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 62
  human_in_the_loop: 4
  name: Appomni Agentic Access
  operation_count: 132
  slug: appomni-agentic-access
  summary_line: 132 operations · 62 acting · 4 human-in-the-loop
api_count: 6
apis:
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: Create, read, update and delete AppOmni security policies and the rules inside them, run and inspect policy assessments, and handle rule events — closing them, converting them to exceptions, or bulk d
  name: AppOmni Policies API
  slug: appomni-policies-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: Register and administer the SaaS services AppOmni monitors, inspect their data-sync state, rotate ingest tokens, and manage the tenant-wide custom fields, custom field values, tags and value lists att
  name: AppOmni Monitored Services API
  slug: appomni-monitored-services-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: 'Unified identities that stitch a person''s monitored-service accounts together by email, plus AppOmni platform users, limited users, groups, roles, permissions and the API authorization tokens used to '
  name: AppOmni Identity and Access API
  slug: appomni-identity-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: AppOmni AgentGuard runtime prompt security — DLP and prompt-firewall classification for AI agent traffic.
  name: AppOmni Agent Guard API
  slug: appomni-agentguard-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The AppOmni Developer Platform (AODP) enables the creation of custom service types allowing you to monitor the security posture of any application, including custom or proprietary apps that AppOmni do
  name: AppOmni AO Developer Platform API
  slug: appomni-ao-developer-platform-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Audit Logs API from AppOmni — 2 operation(s) for audit logs.
  name: AppOmni Audit Logs API
  slug: appomni-audit-logs-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Authorization Tokens API from AppOmni — 7 operation(s) for authorization tokens.
  name: AppOmni Authorization Tokens API
  slug: appomni-authorization-tokens-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: 'THIS FEATURE IS IN BETA - Please contact Customer Success to enable this early access API Provides a granular breakdown of policy assessments across monitored services, allowing you to identify areas '
  name: AppOmni [Beta] Policy Assessment Stats API
  slug: appomni-beta-policy-assessment-stats-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Custom Field Values API accesses the value of the custom field associated with a given monitored service.
  name: AppOmni Custom Field Values for a Monitored Service API
  slug: appomni-custom-field-values-for-a-monitored-service-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: 'The Custom Fields API controls the tenant-wide fields that can be custom-created and assigned to different monitored services. Note : Delete operations for custom fields is disabled in this API for al'
  name: AppOmni Custom Fields API
  slug: appomni-custom-fields-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Discovery API from AppOmni — 3 operation(s) for discovery.
  name: AppOmni Discovery API
  slug: appomni-discovery-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Insights API from AppOmni — 6 operation(s) for insights.
  name: AppOmni Insights API
  slug: appomni-insights-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: Marlin AI is an autonomous SaaS security AI that runs platform-wide deep analyses and correlations automatically across security observations in the AppOmni platform
  name: AppOmni Marlin AI API
  slug: appomni-marlin-ai-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: Posture Findings consolidates policy issues and Insights into a single view, allowing you to efficiently manage and resolve alerts. The Posture Findings API will exist concurrently with Insights and p
  name: AppOmni Posture Findings API
  slug: appomni-posture-findings-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Reports API from AppOmni — 6 operation(s) for reports.
  name: AppOmni Reports API
  slug: appomni-reports-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: 'Use SCIM to connect your identity provider to AppOmni, and utilize this API to: - Get all users in a company - Activate or deactivate users - Update a user’s name, password, user name, email address -'
  name: AppOmni SCIM User Management API
  slug: appomni-scim-user-management-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: The Users and Roles API from AppOmni — 7 operation(s) for users and roles.
  name: AppOmni Users and Roles API
  slug: appomni-users-and-roles-api
- baseURL: https://{instance}.appomni.com
  baseurl_source: declared
  description: ValueList and ValueListElement are used to manage lists of items used by Insights. ValueLists have a type designation and will be used by Insights on convention based on their type. Overview - ValueLi
  name: AppOmni Value List API
  slug: appomni-valuelist-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/overlays/appomni-security-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appomni-security-events-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/overlays/appomni-compliance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appomni-compliance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/overlays/appomni-scim-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appomni-scim-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/overlays/appomni-discovery-insights-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appomni-discovery-insights-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/overlays/appomni-developer-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appomni-developer-platform-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/overlays/appomni-ai-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appomni-ai-api-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/openapi/_original/appomni-security-events-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/appomni-security-events-api-openapi.yml
- group: build
  title: ''
  type: Postman
  url: https://api.appomni.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/collections/appomni-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/appomni-api.postman_collection.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/packages/appomni-packages.yml
  title: ''
  type: Packages
  url: packages/appomni-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/mcp/appomni-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/appomni-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/mcp/appomni-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/appomni-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/llms/appomni-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appomni-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/conformance/appomni-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appomni-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/conformance/appomni-conformance.yml
  title: ''
  type: Compliance
  url: conformance/appomni-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/errors/appomni-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appomni-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/lifecycle/appomni-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appomni-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appomni.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/conventions/appomni-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appomni-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/data-model/appomni-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appomni-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/authentication/appomni-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appomni-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/rate-limits/appomni-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appomni-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/plans/appomni-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appomni-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/agentic-access/appomni-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appomni-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/security/appomni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appomni-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/security/appomni-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appomni-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://appomni.com/ao-labs-vulnerability-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/security/appomni-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appomni-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.appomni.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appomni
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appomni
- group: company
  title: ''
  type: Website
  url: https://appomni.com/
- group: docs
  title: ''
  type: Documentation
  url: https://appomni.com/resources/
- group: docs
  title: ''
  type: APIReference
  url: https://api.appomni.com/
- group: operate
  title: ''
  type: Support
  url: https://appomni.com/support/
- group: company
  title: ''
  type: Blog
  url: https://appomni.com/article-type/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://appomni.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://appomni.com/demo-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appomni.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appomni.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://appomni.com/newsroom/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/json-schema/appomni-paginated-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/appomni-paginated-list-schema.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/examples/appomni-occurrence-example.json
  title: ''
  type: Examples
  url: examples/appomni-occurrence-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/json-ld/appomni-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appomni-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/vocabulary/appomni-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/appomni-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/rules/appomni-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/appomni-spectral-rules.yml
created: '2026-03-27'
description: AppOmni is a SaaS and AI security platform (SSPM) that gives security teams continuous visibility into the posture, identities, third-party connections and data exposure of the SaaS applications that run an enterprise — Salesforce, Microsoft 365, Google Workspace, Slack, ServiceNow, Okta, Workday, GitHub, Box, Zoom and custom applications built on its Developer Platform. It publishes a tenant-scoped REST API covering posture findings, policies, compliance reporting, monitored services, identity, discovery, insights, SCIM 2.0 provisioning and AI security, plus AskOmni (an MCP server) and AgentGuard runtime prompt protection for agentic AI.
examples:
- key_count: 12
  name: Appomni Occurrence Example
  slug: appomni-occurrence-example
finops:
- name: Appomni Finops
  service_category: API
  slug: appomni-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appomni.png
json_schemas:
- name: Finding
  property_count: 27
  slug: appomni-finding
- name: Occurrence
  property_count: 12
  slug: appomni-occurrence
- name: PaginatedList
  property_count: 4
  slug: appomni-paginated-list
json_structures:
- name: Appomni Occurrence Structure
  property_count: 0
  slug: appomni-occurrence-structure
jsonld:
- class_count: 25
  name: Appomni Context
  property_count: 5
  slug: appomni-context
layout: provider
mcp_servers:
- description: AskOmni is AppOmni's AI security assistant, and AppOmni publishes it as a Model Context Protocol server. Announced 2025-04-28 at RSA Conference as "the world's first MCP interface to SaaS security", i
  name: AskOmni MCP Server
  slug: askomni-mcp-server
modified: '2026-09-16'
name: AppOmni
nav: Providers
network: true
overview: 'AppOmni publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Policies API, Monitored Services API, Identity and Access API, and 15 more. Tagged areas include SaaS Security, SSPM, Compliance, Threat Detection, and CASB.


  The AppOmni catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AppOmni''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, code examples, and 40 more developer resources.'
plans:
- name: Appomni Plans Pricing
  plan_count: 0
  slug: appomni-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Appomni Rate Limits
  slug: appomni-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AppOmni API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appomni-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: AppOmni API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appomni-spectral-rules
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.0
    catalog_earned_first_party: 8.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    contract_governance: 45.5
    contract_quality: 68.1
    developer_ergonomics: 42.3
    discoverability: 77.5
    operational_transparency: 50.0
  previous_composite: 59.0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/screenshots/appomni-2026-06-20T172343.png
security:
- kind: authentication
  name: Appomni Authentication
  slug: appomni-authentication
  summary_line: http/apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Appomni Domain Security
  slug: appomni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appomni Vulnerability Disclosure
  slug: appomni-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Appomni Trust Center
  slug: appomni-trust-center
  summary_line: FedRAMP Moderate Authority to Operate, TX-RAMP, SOC 2 Type II, VPAT, NIST CSF, EU-US Data Privacy Framework, UK Extension to the EU-US Data Privacy Framework, Swiss-US Data Privacy Framework
slug: appomni
tags:
- SaaS Security
- SSPM
- Compliance
- Threat Detection
- CASB
- Zero Trust
- Identity
- SCIM
- AI Security
- Posture Management
website: https://appomni.com/
---
