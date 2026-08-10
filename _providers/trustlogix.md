---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for the TrustLogix platform — manage data source accounts, data access policies (create / impact-preview / review / publish), data-source tags and associations, monitoring policies (v1 and v2
  name: TrustLogix REST API
  slug: trustlogix-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.trustlogix.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trustlogix.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trustlogix.io/trustlogix-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trustlogix.io/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.trustlogix.io/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trustlogix.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.trustlogix.io/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustlogix.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustlogix.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.trustlogix.io/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.trustlogix.io/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trustlogix-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustlogix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trustlogix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trustlogix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trustlogix-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trustlogix-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trustlogix-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/trustlogix-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.trustlogix.io/security-pledge
- group: auth
  title: ''
  type: TrustCenter
  url: security/trustlogix-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustlogix-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TrustLogix is a data security and access governance platform that unifies data visibility, policy enforcement, and AI protection across cloud, on-premises, and hybrid data systems. It continuously detects inappropriate access, enforces least-privilege and attribute-based (ABAC) / role-based (RBAC) controls, and governs how users, service accounts, and AI agents reach sensitive data across platforms such as Snowflake, Databricks, Dremio, SQL Server, and Power BI. The platform includes Trust DSPM (data security posture management), Trust Access (data access governance with masking, row-access, and tag-based policies), and Trust AI — an agentic layer whose Guardian Agent and TrustAI MCP Server broker real-time policy decisions for registered AI agents. TrustLogix exposes a REST API for accounts, access policies, tags, monitoring policies, and users, plus SSO (Azure AD / Okta) with SCIM 2.0 provisioning.
image: https://cdn.prod.website-files.com/689aca9a00606d8ac05c62da/69004670671ad7cf11b7e5f3_TrustLogix-OpenGraph.jpg
layout: provider
mcp_servers:
- description: ''
  name: trustlogix-mcp.yml
  slug: trustlogix-mcpyml
modified: '2026-07-21'
name: Trustlogix
nav: Providers
network: true
overview: 'Trustlogix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Security, Data Access Governance, Data Security Posture Management, and Access Control.


  Trustlogix''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 16 more developer resources.'
random_paper: 81
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 53.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 34.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Trustlogix Authentication
  slug: trustlogix-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Trustlogix Domain Security
  slug: trustlogix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trustlogix Trust Center
  slug: trustlogix-trust-center
  summary_line: SOC 2
slug: trustlogix
tags:
- Company
- Data Security
- Data Access Governance
- Data Security Posture Management
- Access Control
- Snowflake
- Databricks
- AI Security
- MCP
- Authorization
- Compliance
website: https://www.trustlogix.io
---
