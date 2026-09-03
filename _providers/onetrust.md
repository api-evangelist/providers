---
access_model:
  confidence: high
  label: Enterprise · Public docs + public OpenAPI, tenant-gated keys
  onboarding: unknown
  pricing: enterprise
  public: true
  source:
  - plans
  - authentication
  - openapi
  trial: true
  try_now: false
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 389
  human_in_the_loop: 30
  name: Onetrust Agentic Access
  operation_count: 631
  slug: onetrust-agentic-access
  summary_line: 631 operations · 389 acting · 30 human-in-the-loop
api_count: 37
apis:
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The AI Governance APIs are used to integrate external systems and streamline the flow of data with A I Governance in the OneTrust Platform. (20 operations.)
  name: OneTrust AI Governance — AI Governance
  slug: ai-governance-ai-governance
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Platform - Global Activity API from OneTrust — 1 operation(s) documented on the OneTrust Develop er Portal.
  name: OneTrust Platform — Global Activity
  slug: platform-global-activity
- baseURL: https://consent-api.onetrust.com
  baseurl_source: declared
  description: The Consent Interfaces APIs are used to integrate external systems and streamline the flow of data w ith Consent & Preferences user interfaces. (1 operations.)
  name: OneTrust Consent & Preferences — Consent Interfaces
  slug: consent-and-preferences-consent-interfaces
- baseURL: https://mobile-data.onetrust.io
  baseurl_source: declared
  description: 'These are server-based APIs that will act as a medium between the OT hosted server that owns busines s logic and the client-side SDK, which will take the responsibility to render elements on UI based '
  name: OneTrust Consent & Preferences — Consent Management Platform (CMP)
  slug: consent-and-preferences-consent-management-platform-cmp
- baseURL: https://app.onetrust.com/request/v1
  baseurl_source: declared
  description: The Consent Receipts APIs are used to integrate external systems and streamline the flow of consent receipt data with the OneTrust Platform. (3 operations.)
  name: OneTrust Consent & Preferences — Consent Receipts
  slug: consent-and-preferences-consent-receipts
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Cookie Consent APIs are used to integrate external systems and streamline the flow of data with Cookie Consent in the OneTrust Platform. (44 operations.)
  name: OneTrust Consent & Preferences — Cookie Consent
  slug: consent-and-preferences-cookie-consent
- baseURL: https://customer.my.onetrust.com/api/cookiemanager
  baseurl_source: declared
  description: The Consent & Preferences - Cookie Consent (Swagger) API from OneTrust — 11 operation(s) documented on the OneTrust Developer Portal.
  name: OneTrust Consent & Preferences — Cookie Consent (Swagger)
  slug: consent-and-preferences-cookie-consent-swagger
- baseURL: https://cookies-data.onetrust.io/bannersdk
  baseurl_source: declared
  description: 'Use this API to retrieve all templates, consent model, and vendor list data for a specific Website D omain by a user’s geolocation. The API returns a single JSON formatted for custom UI development. #'
  name: OneTrust Consent & Preferences — Cookie Domain Data
  slug: consent-and-preferences-cookie-domain-data
- baseURL: https://consent-api.onetrust.com
  baseurl_source: declared
  description: The Consent & Preferences - Cross-Device Consent API from OneTrust — 1 operation(s) documented on th e OneTrust Developer Portal.
  name: OneTrust Consent & Preferences — Cross-Device Consent
  slug: consent-and-preferences-cross-device-consent
- baseURL: https://customer.my.onetrust.com/bannersdk/v2
  baseurl_source: declared
  description: Collection of APIs for the Mobile & OTT App Compliance SDKs. (1 operations.)
  name: OneTrust Consent & Preferences — Mobile App Consent
  slug: consent-and-preferences-mobile-app-consent
- baseURL: https://app.onetrust.com/api/privacynotice
  baseurl_source: declared
  description: The Policy & Notice Management APIs are used to list privacy notices, page through results, view ver sion history for a notice, and retrieve the version that was effective at a specific date and time.
  name: OneTrust Consent & Preferences — Policy & Notice Management
  slug: consent-and-preferences-policy-and-notice-management
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: 'The Universal Consent & Preference Management APIs are used to integrate external systems and stream line the flow of data with Universal Consent & Preference Management in the OneTrust Platform. (97 '
  name: OneTrust Consent & Preferences — Universal Consent & Preference Management (OAS)
  slug: consent-and-preferences-universal-consent-and-preference-management-oas
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Catalog APIs provide comprehensive functionality for managing data governance assets within Data Catalog, enabling users to create, retrieve, and organize business glossaries, terms, and tags
  name: OneTrust Data Use Governance — Data Catalog
  slug: data-use-governance-data-catalog
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Discovery API provides comprehensive REST endpoints for managing data discovery operations including data sources, scan profiles, credentials, and scan jobs with OAuth2 security and extensive
  name: OneTrust Data Use Governance — Data Discovery
  slug: data-use-governance-data-discovery
- baseURL: https://app.onetrust.com:8080/api/data-discovery-bridge
  baseurl_source: declared
  description: The Data Discovery Worker Node APIs enables secure communication with an on-premises Data Discovery worker node. It provides operations to retrieve, classify, and catalog data from connected data sour
  name: OneTrust Data Use Governance — Data Discovery Worker Node
  slug: data-use-governance-data-discovery-worker-node
- baseURL: https://app.onetrust.com/api/esg-management
  baseurl_source: declared
  description: The ESG Program Reporting & Disclosures API from OneTrust — 5 operation(s) documented on the OneTrus t Developer Portal.
  name: OneTrust ESG Program Reporting & Disclosures
  slug: esg-program-reporting-and-disclosures
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Access Management APIs enable you to programmatically control user access, manage organizational hierarchies, and monitor authentication activities across your OneTrust platform. (36 operations.)
  name: OneTrust Platform — Access Management
  slug: platform-access-management
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Bulk Export APIs are used to integrate external systems and extract specific data from Cookie Co nsent and Universal Consent & Preference Management in the OneTrust platform. (7 operations.)
  name: OneTrust Platform — Bulk Export
  slug: platform-bulk-export
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Documents API are used to integrate external systems and streamline the flow of data for documen ts in the OneTrust Platform. (3 operations.)
  name: OneTrust Platform — Documents
  slug: platform-documents
- baseURL: https://app.onetrust.com/api/integrationmanager
  baseurl_source: declared
  description: The Integrations APIs are used to configure, manage, and automate integrations. They provide functio nality to handle system credentials, import and export workflows, and manage integration details. (
  name: OneTrust Platform — Integrations
  slug: platform-integrations
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Inventory APIs are used to manage relationships and link data within the inventory. (13 operatio ns.)
  name: OneTrust Platform — Inventory
  slug: platform-inventory
- baseURL: https://app.onetrust.com/api/custom-entity
  baseurl_source: declared
  description: The Object Manager APIs are used to integrate external systems and streamline the flow of data for o bjects created via Object Manager in the OneTrust Platform. (38 operations.)
  name: OneTrust Platform — Object Manager
  slug: platform-object-manager
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Task Management APIs are used to integrate external systems and streamline the flow of data for tasks created across the OneTrust Platform. (3 operations.)
  name: OneTrust Platform — Task Management
  slug: platform-task-management
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: OneTrust supports cross-domain identity management through the SCIM 2.0 specification. System for Cr oss-Domain Identity Management (SCIM) is an open specification to help facilitate the automated man
  name: OneTrust Platform — User Provisioning
  slug: platform-user-provisioning
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: 'The Assessment Automation APIs provide functionality for managing assessment template lifecycle oper ations, including template export and import for cross-environment migration, retrieving published '
  name: OneTrust Privacy Automation — Assessment Automation
  slug: privacy-automation-assessment-automation
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Mapping Automation APIs are used to manage structured records (assets, vendors, processing activities, and legal entities), define schema attributes, traverse parent–child hierarchies, and cr
  name: OneTrust Privacy Automation — Data Mapping Automation
  slug: privacy-automation-data-mapping-automation
- baseURL: https://customer.my.onetrust.com/api
  baseurl_source: declared
  description: The Privacy Automation - Data Mapping Automation (Swagger) API from OneTrust — 4 operation(s) docume nted on the OneTrust Developer Portal.
  name: OneTrust Privacy Automation — Data Mapping Automation (Swagger)
  slug: privacy-automation-data-mapping-automation-swagger
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Privacy Rights Automation are used to manage, process, and fulfill data subject access requests (DSARs), including request creation, subtask management, resolution codes, verification methods, and
  name: OneTrust Privacy Automation — Data Subject Request (DSR) Automation
  slug: privacy-automation-data-subject-request-dsr-automation
- baseURL: https://app.onetrust.com/api
  baseurl_source: declared
  description: The Incident Management API allows you to efficiently manage and respond to incidents. (7 operations .)
  name: OneTrust Privacy Automation — Incident Management
  slug: privacy-automation-incident-management
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The The Trust Intelligence Platform - Document Gateway API from OneTrust — 1 operation(s) documented on the OneTrust Developer Portal.
  name: OneTrust The Trust Intelligence Platform — Document Gateway
  slug: the-trust-intelligence-platform-document-gateway
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Audit Management API provides comprehensive REST endpoints for managing enterprise audits, workp apers, and compliance assessments with OAuth2 security and advanced filtering capabilities. (11 ope
  name: OneTrust Tech Risk & Compliance — Audit Management
  slug: tech-risk-and-compliance-audit-management
- baseURL: https://app.onetrust.com/api/compliance-wr
  baseurl_source: declared
  description: The Compliance Automation APIs are used to integrate external systems and streamline the flow of dat a with Compliance Automation in the OneTrust Platform. (3 operations.)
  name: OneTrust Tech Risk & Compliance — Compliance Automation
  slug: tech-risk-and-compliance-compliance-automation
- baseURL: https://app.onetrust.com/api/enterprise-policy
  baseurl_source: declared
  description: The Enterprise Policy Management APIs are used to integrate external systems and streamline the flow of data with Enterprise Policy Management in the OneTrust platform. (6 operations.)
  name: OneTrust Tech Risk & Compliance — Enterprise Policy Management
  slug: tech-risk-and-compliance-enterprise-policy-management
- baseURL: https://app.onetrust.com/api/issue-management
  baseurl_source: declared
  description: The Issues Management APIs are used to integrate external systems and streamline the flow of data wi th Issues Management in the OneTrust platform. (9 operations.)
  name: OneTrust Tech Risk & Compliance — Issues Management
  slug: tech-risk-and-compliance-issues-management
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The IT Risk Management API provides comprehensive REST endpoints for managing enterprise security co ntrols, threats, vulnerabilities, and their implementations with OAuth2 security and extensive cust
  name: OneTrust Tech Risk & Compliance — IT Risk Management
  slug: tech-risk-and-compliance-it-risk-management
- baseURL: https://customer.my.onetrust.com/api/awareness-training
  baseurl_source: declared
  description: The Tech Risk & Compliance - Training API from OneTrust — 5 operation(s) documented on the OneTrust Developer Portal.
  name: OneTrust Tech Risk & Compliance — Training
  slug: tech-risk-and-compliance-training
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Third-Party Risk Management APIs provide comprehensive functionality for managing vendor relatio nships, engagements, and contracts within the GRC ecosystem, enabling organizations to assess, moni
  name: OneTrust Third-Party Management — Third-Party Risk Management
  slug: third-party-management-third-party-risk-management
artifact_total: 49
asyncapis:
- description: ''
  name: Onetrust Webhooks
  slug: onetrust-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://www.onetrust.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.onetrust.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onetrust.com/onetrust/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.onetrust.com/onetrust/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.onetrust.com/onetrust/reference/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://my.onetrust.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.onetrust.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onetrust-oss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onetrust.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.onetrust.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onetrust.com/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onetrust
- group: operate
  title: ''
  type: StatusPage
  url: https://my.onetrust.com/s/system-status
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/onetrust-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onetrust-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onetrust-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onetrust-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/onetrust-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onetrust-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onetrust-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onetrust-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onetrust-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/onetrust-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/onetrust-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/onetrust-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onetrust-packages.yml
- group: design
  title: ''
  type: Components
  url: components/onetrust-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/onetrust-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onetrust-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/onetrust-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onetrust-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onetrust-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/onetrust-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/onetrust-api-catalog.json
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/onetrust-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onetrust-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/onetrust-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/onetrust-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/onetrust-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onetrust-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onetrust-domain-security.yml
created: '2026-05-08'
description: OneTrust is an enterprise trust, privacy, and AI-governance platform. Its developer portal publishes 37 downloadable OpenAPI definitions covering roughly 631 operations across Universal Consent & Preference Management, Cookie Consent / CMP, Consent Receipts, Data Subject Request (DSR) Automation, Assessment Automation (PIA/DPIA), Data Mapping, Data Catalog and Data Discovery, Incident Management, IT & Security Risk Management, Audit Management, Issues Management, Enterprise Policy Management, Compliance Automation, Third-Party Risk Management, ESG Program Reporting, AI Governance, and the shared platform services (Access Management, SCIM 2.0 User Provisioning, Object Manager, Inventory, Bulk Export, Documents, Integrations, Task Management, Global Activity). Every API is authorized with OAuth 2.0 client credentials against a per-tenant environment host, and the portal also serves an RFC 9727 /.well-known/api-catalog, an llms.txt, and a public remote MCP server.
finops:
- name: Onetrust Finops
  service_category: Compliance & Governance
  slug: onetrust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onetrust.png
layout: provider
mcp_servers:
- description: OneTrust hosts a public remote MCP server on its developer portal. It is documented on a dedicated "MCP Server" page in the API reference, requires no authentication headers, and answered a live tools
  name: OneTrust Developer Portal MCP Server
  slug: onetrust-developer-portal-mcp-server
modified: '2026-08-27'
name: OneTrust
nav: Providers
network: true
overview: 'OneTrust publishes 37 APIs on the [APIs.io](https://apis.io/) network, including AI Governance — AI Governance, Platform — Global Activity, Consent & Preferences — Consent Interfaces, and 34 more. Tagged areas include Privacy, GRC, Compliance, Consent, and TPRM.


  The OneTrust catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OneTrust''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 35 more developer resources.'
plans:
- name: Onetrust Plans Pricing
  plan_count: 1
  slug: onetrust-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 12
  name: Onetrust Rate Limits
  slug: onetrust-rate-limits
scopes:
- name: Onetrust Scopes
  scope_count: 51
  slug: onetrust-scopes
  summary_line: 51 scopes · clientCredentials
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 26
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 67.8
    developer_ergonomics: 51.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 58.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/screenshots/onetrust-2026-06-20T190718.png
security:
- kind: authentication
  name: Onetrust Authentication
  slug: onetrust-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onetrust Domain Security
  slug: onetrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onetrust Vulnerability Disclosure
  slug: onetrust-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Onetrust Trust Center
  slug: onetrust-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: onetrust
tags:
- Privacy
- GRC
- Compliance
- Consent
- TPRM
- AI Governance
- Data Governance
- Risk Management
- Data Discovery
- ESG
- Security
- SCIM
website: https://www.onetrust.com/
---
