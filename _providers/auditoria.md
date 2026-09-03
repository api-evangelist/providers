---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/auditoria-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/auditoria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auditoria.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.auditoria.ai/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://www.auditoria.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://blog.auditoria.ai/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.auditoria.ai/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auditoria-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auditoriaai/
- group: start
  title: ''
  type: Login
  url: https://app.auditoria.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auditoria.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auditoria.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.auditoria.ai/trust/
- group: auth
  title: ''
  type: Security
  url: https://www.auditoria.ai/trust/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/auditoria-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.auditoria.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.auditoria.ai/hc/en-us/categories/360005816333-Auditoria-AI-Release-Notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/auditoria-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/auditoria-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/auditoria-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/auditoria-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/auditoria-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/auditoria-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/auditoria-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/auditoria-conformance.yml
coverage:
  checked: '2026-08-06'
  detail: Auditoria is an API consumer, not an API provider - the only documented ways to move AP/AR data in or out are a prebuilt ERP connector (Workday, NetSuite, Oracle Fusion, Sage Intacct, Coupa) or the Universal Connector's CSV/JSON templates dropped on SFTP or an S3 bucket, and a help-center search for "webhook" across all 44 integration articles returns zero results.
  evidence:
  - status: 200
    url: https://docs.auditoria.ai/hc/en-us/articles/60112878955289-Auditoria-Universal-Connector
  - status: 404
    url: https://www.auditoria.ai/openapi.json
  - status: 200
    url: https://docs.auditoria.ai/api/v2/help_center/articles/search.json?query=webhook
  - status: 404
    url: https://auth.auditoria.ai/.well-known/oauth-protected-resource
  - status: 404
    url: https://www.auditoria.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Auditoria.AI is a San Jose, California software company, founded in 2019, that builds agentic AI "SmartBots" for the corporate finance back office. Its SmartVendor line (AP Helpdesk, AP Invoices, AP Accruals) and SmartCustomer line (AR Helpdesk, AR Collections, AR Remittances), together with SmartResearch and the Guardian data-protection layer, automate vendor onboarding and management, invoice capture and validation, accruals, collections, remittance application and audit readiness on top of a customer's existing ERP. The platform runs a finance-domain small language model over structured ERP records and unstructured invoices, remittances, emails and supplier documents, and executes work as configurable SmartFlow Skills / Agent Co-workers with human-in-the-loop review. Auditoria integrates into Workday, Oracle NetSuite, Oracle Fusion Cloud Financials, SAP, Sage Intacct, Coupa and ServiceNow, with a template-driven Universal Connector over SFTP or Amazon S3 for ERPs that have
  no native connector. Auditoria is an API consumer rather than an API provider - it publishes no public developer API, SDK, webhook surface or developer portal.
image: https://www.auditoria.ai/wp-content/uploads/www.auditoria.ai-featured-scaled.png
layout: provider
modified: '2026-08-06'
name: Auditoria.AI
nav: Providers
network: true
overview: 'Auditoria.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Finance, Accounting, and Accounts Payable.


  Auditoria.AI''s developer surface includes documentation, support, engineering blog, changelog, authentication, and 20 more developer resources.'
random_paper: 17
scopes:
- name: Auditoria Scopes
  scope_count: 14
  slug: auditoria-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode/implicit/refreshToken
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 28.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/auditoria/refs/heads/main/screenshots/auditoria-2026-08-07T161929.png
security:
- kind: authentication
  name: Auditoria Authentication
  slug: auditoria-authentication
  summary_line: openIdConnect/oauth2/saml2 · 3 schemes
- kind: domain-security
  name: Auditoria Domain Security
  slug: auditoria-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Auditoria Vulnerability Disclosure
  slug: auditoria-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Auditoria Trust Center
  slug: auditoria-trust-center
  summary_line: SOC 2 Type II
slug: auditoria
tags:
- Company
- Artificial Intelligence
- Finance
- Accounting
- Accounts Payable
- Accounts Receivable
- Automation
- ERP
- Agents
- Software-as-a-Service
- Invoicing
- Procurement
website: https://www.auditoria.ai/
---
