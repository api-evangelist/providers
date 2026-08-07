---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: REST API over the Tradeshift business commerce platform. 172 operations across accounts and branches, legal entities, taxes and validations, network connections and connection properties, document pro
  name: Tradeshift External API
  slug: tradeshift-external-api
- description: Production Model Context Protocol server that exposes Tradeshift platform capability to AI agents, described by Tradeshift as 95 tools across six domains (core services, supplier network, documents, c
  name: Tradeshift MCP Server
  slug: tradeshift-mcp-server
artifact_total: 18
asyncapis:
- description: ''
  name: Tradeshift Webhooks
  slug: tradeshift-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tradeshift-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tradeshift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradeshift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradeshift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tradeshift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tradeshift.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tradeshift.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tradeshift.com/docs/guides/get-started
- group: operate
  title: ''
  type: Support
  url: https://support.tradeshift.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.tradeshift.com/knowledgebase
- group: company
  title: ''
  type: Blog
  url: https://tradeshift.com/resources/
- group: company
  title: ''
  type: BlogRSS
  url: https://tradeshift.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tradeshift
- group: commercial
  title: ''
  type: Pricing
  url: https://tradeshift.com/seller-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://go.tradeshift.com/register
- group: start
  title: ''
  type: Login
  url: https://go.tradeshift.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tradeshift.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tradeshift.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tradeshift.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.tradeshift.com/docs/deprecation-process
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.tradeshift.com/announcements/
- group: auth
  title: ''
  type: Security
  url: https://tradeshift.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://tradeshift.com/security/
- group: design
  title: ''
  type: Idempotency
  url: conventions/tradeshift-conventions.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tradeshift-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/tradeshift-packages.yml
- group: design
  title: ''
  type: Components
  url: components/tradeshift-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tradeshift-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradeshift-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tradeshift-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradeshift-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tradeshift-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tradeshift-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tradeshift-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tradeshift-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tradeshift-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tradeshift-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tradeshift-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tradeshift-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tradeshift-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tradeshift-tool-crosswalk.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tradeshift-external-api-overlay.yaml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Tradeshift
created: '2026-08-02'
description: Tradeshift is a cloud-based business commerce network for accounts payable automation, e-invoicing compliance, procure-to-pay, supplier management, and B2B marketplace commerce, connecting buyers and sellers across more than 190 countries. The Tradeshift External API is a REST/JSON+XML interface over the same platform its own apps use, covering company accounts and branches, legal entities and tax identifiers, network connections and connection properties, business documents (invoices, orders, credit notes, quotes, requisitions, receipt advices) in the OASIS UBL / TSUBL format, document files and attachments, users and memberships, assignments and workflow, and document validation and clearance for country e-invoicing mandates. Authentication is OAuth (OAuth 1.0a two-legged for account-scoped integrations, OAuth 2.0 three-legged for apps acting on behalf of users), every call carries an X-Tradeshift-TenantId header, and apps can subscribe to platform webhooks for document, network,
  and user events. Tradeshift also runs a production MCP server exposing platform capability to AI agents under the same authentication, RBAC, and audit model as human sessions.
image: https://tradeshift.com/wp-content/uploads/2021/01/Logo-symbol-white-on-blue-bg-@10x.png
json_schemas:
- name: json-schema/maindoc/UBL-ApplicationResponse-2.1.json
  property_count: 5
  slug: tradeshift-ubl-applicationresponse-2.1
- name: json-schema/maindoc/UBL-CreditNote-2.1.json
  property_count: 5
  slug: tradeshift-ubl-creditnote-2.1
- name: json-schema/maindoc/UBL-DespatchAdvice-2.1.json
  property_count: 5
  slug: tradeshift-ubl-despatchadvice-2.1
- name: json-schema/maindoc/UBL-Invoice-2.1.json
  property_count: 5
  slug: tradeshift-ubl-invoice-2.1
- name: json-schema/maindoc/UBL-Order-2.1.json
  property_count: 5
  slug: tradeshift-ubl-order-2.1
- name: json-schema/maindoc/UBL-OrderResponse-2.1.json
  property_count: 5
  slug: tradeshift-ubl-orderresponse-2.1
- name: json-schema/maindoc/UBL-Quotation-2.1.json
  property_count: 5
  slug: tradeshift-ubl-quotation-2.1
- name: json-schema/maindoc/UBL-ReceiptAdvice-2.1.json
  property_count: 5
  slug: tradeshift-ubl-receiptadvice-2.1
- name: json-schema/maindoc/UBL-RequestForQuotation-2.1.json
  property_count: 5
  slug: tradeshift-ubl-requestforquotation-2.1
layout: provider
mcp_servers:
- description: ''
  name: tradeshift-mcp.yml
  slug: tradeshift-mcpyml
modified: '2026-08-02'
name: Tradeshift
nav: Providers
network: true
overview: 'Tradeshift publishes 2 APIs on the [APIs.io](https://apis.io/) network: External API and MCP Server. Tagged areas include e-invoicing, accounts-payable, ap-automation, procure-to-pay, and supply-chain.


  The Tradeshift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tradeshift''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 38 more developer resources.'
random_paper: 53
scopes:
- name: Tradeshift Scopes
  scope_count: 7
  slug: tradeshift-scopes
  summary_line: 7 scopes · clientCredentials/implicit
score:
  band: strong
  composite: 62.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.6
    developer_ergonomics: 75.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 62.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tradeshift Authentication
  slug: tradeshift-authentication
  summary_line: oauth1/oauth2/apiKey · 4 schemes
- kind: domain-security
  name: Tradeshift Domain Security
  slug: tradeshift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tradeshift Vulnerability Disclosure
  slug: tradeshift-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Tradeshift Trust Center
  slug: tradeshift-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISAE 3402 Type II, PCI DSS Level 1, ISO 27001
slug: tradeshift
tags:
- e-invoicing
- accounts-payable
- ap-automation
- procure-to-pay
- supply-chain
- b2b-commerce
- invoicing
- ubl
- peppol
- e-invoicing-compliance
- supplier-network
- business-documents
- fintech
- mcp
- agent-native
website: https://tradeshift.com/
---
