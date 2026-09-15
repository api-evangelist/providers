---
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-09-14'
api_count: 5
apis:
- baseURL: https://api.finance.visma.net
  baseurl_source: declared
  description: REST API for Visma.net ERP (Visma Net Financials) covering general ledger, accounts receivable and payable, customers, suppliers, sales orders, purchase orders, inventory, projects and dimensions. 395
  name: Visma.net ERP API
  slug: visma-net-erp-api
- baseURL: https://eaccountingapi.vismaonline.com/v2/
  baseurl_source: declared
  description: 'REST API for Bookkeeping & Invoicing / eAccounting (Spiris, formerly Visma Spcs) covering customers, suppliers, articles, customer and supplier invoices, orders, quotes, vouchers, accounts, projects, '
  name: Visma Bookkeeping & Invoicing / eAccounting API
  slug: visma-eaccounting-api
- baseURL: https://vlsapi.vismaonline.com/
  baseurl_source: declared
  description: REST API for Spiris Lon / Visma Cloud Payroll covering employees, employments, salary transactions, absences, pay periods, payslips and accounting output. Published as OpenAPI 3.0.4 in two live versio
  name: Visma Cloud Payroll (Spiris Lon) API
  slug: visma-payroll-api
- description: 'GraphQL API for Business NXT, Visma''s ERP for mid-market Nordic customers. Two endpoints share one schema: /api/graphql for a Visma.net user context (authorization code with PKCE) and /api/graphql-ser'
  name: Visma Business NXT GraphQL API
  slug: visma-business-nxt-api
artifact_total: 13
asyncapis:
- description: ''
  name: Visma Net Erp Webhooks
  slug: visma-net-erp-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.visma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.visma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vismasoftware.no/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vismasoftware.no/vismanetapi/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vismasoftware.no/vismanetapi/introduction/getting-started-with-visma-net-api/
- group: start
  title: ''
  type: SignUp
  url: https://oauth.developers.visma.com/service-registry/
- group: operate
  title: ''
  type: Support
  url: https://docs.vismasoftware.no/vismanetapi/support/
- group: company
  title: ''
  type: Blog
  url: https://www.visma.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.visma.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visma.com/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.visma.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.vismasoftware.no/vismanetapi/end-of-life-notices/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/visma-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-trust-center.yml
  title: ''
  type: Compliance
  url: security/visma-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/llms/visma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/visma-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/mcp/visma-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/visma-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/well-known/visma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/visma-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/well-known/visma-connect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/visma-connect-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/packages/visma-packages.yml
  title: ''
  type: Packages
  url: packages/visma-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/components/visma-components.yml
  title: ''
  type: Components
  url: components/visma-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/authentication/visma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/visma-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/scopes/visma-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/visma-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/conventions/visma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/visma-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/conformance/visma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/visma-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/errors/visma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/visma-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/lifecycle/visma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/visma-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/changelog/visma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/visma-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/rate-limits/visma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/visma-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/plans/visma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/visma-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/sandbox/visma-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/visma-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/data-model/visma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/visma-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/asyncapi/visma-net-erp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/visma-net-erp-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/visma-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/visma-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/security/visma-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/visma-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/mcp/visma-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/visma-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Visma-Software-AS-Product
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-create-customer-and-sales-order.md
  title: ''
  type: AgentSkill
  url: skills/visma-create-customer-and-sales-order.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-invoice-and-reverse.md
  title: ''
  type: AgentSkill
  url: skills/visma-invoice-and-reverse.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-supplier-invoice-approval.md
  title: ''
  type: AgentSkill
  url: skills/visma-supplier-invoice-approval.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visma/refs/heads/main/skills/visma-business-nxt-mcp-session.md
  title: ''
  type: AgentSkill
  url: skills/visma-business-nxt-mcp-session.md
created: '2026-09-13'
description: 'Visma is a Nordic business-software group headquartered in Oslo, Norway, supplying cloud ERP, accounting, invoicing, payroll, HR and public-sector software to more than a million customers across Europe and Latin America. Its developer surface is federated across product lines rather than centralised: Visma.net ERP publishes a 511-operation OpenAPI 3.0 contract at api.finance.visma.net in service (client-credentials) and interactive (authorization-code) flavours; Bookkeeping & Invoicing/eAccounting and Cloud Payroll (Spiris, formerly Visma Spcs) publish OpenAPI 3.0 contracts at eaccountingapi.vismaonline.com and vlsapi.vismaonline.com; and Business NXT exposes a GraphQL API at business.visma.net. Identity is centralised on Visma Connect (connect.visma.com), an OpenID Connect provider advertising 129 scopes, with a second IdentityServer at identity.vismaonline.com for the Spiris product line. Visma ships two first-party remote MCP servers — Business NXT at mcp.business.visma.net
  and Spiris at mcp.spiris.se — both OAuth-protected and discoverable via RFC 9728.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Visma MCP Server
  slug: visma-mcp-server
modified: '2026-09-13'
name: Visma
nav: Providers
network: true
overview: 'Visma publishes 3 APIs on the [APIs.io](https://apis.io/) network: Visma.net ERP API, Bookkeeping & Invoicing / eAccounting API, and Cloud Payroll (Spiris Lon) API. Tagged areas include Accounting, Business Software, ERP, Enterprise, and Financial-Services.


  The Visma catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Visma''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 35 more developer resources.'
plans:
- name: Visma Plans Pricing
  plan_count: 1
  slug: visma-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Visma Rate Limits
  slug: visma-rate-limits
scopes:
- name: Visma Scopes
  scope_count: 5
  slug: visma-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 56.5
    discoverability: 81.5
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Visma Authentication
  slug: visma-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Visma Domain Security
  slug: visma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Visma Vulnerability Disclosure
  slug: visma-vulnerability-disclosure
  summary_line: Intigriti · contact published
- kind: trust-center
  name: Visma Trust Center
  slug: visma-trust-center
  summary_line: trust center published
slug: visma
tags:
- Accounting
- Business Software
- ERP
- Enterprise
- Financial-Services
- Human Resources
- Invoicing
- Nordic
- Payroll
- Software-as-a-Service
website: https://www.visma.com/
---
