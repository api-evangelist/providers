---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Publicly served SOAP 1.1 / 1.2 web service behind the USADATA Leads Portal and Leads Module. The WSDL is served anonymously from the production API host and declares 24 operations covering the full li
  name: USADATA Leads Engine Service (SOAP)
  slug: leads-engine
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usadata-inc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usadata-inc-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/usadata-inc-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/usadata-inc-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/usadata-inc-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/usadata-inc-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/usadata-inc-plans-pricing.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/usadata-inc-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.sl360.com/signup
- group: docs
  title: ''
  type: APIReference
  url: https://leadsengine.usadata.com/service.asmx
- group: company
  title: ''
  type: Website
  url: https://www.usadata.com/
- group: other
  title: ''
  type: APIs
  url: https://www.usadata.com/products/apis
- group: company
  title: ''
  type: Blog
  url: https://www.usadata.com/resources/news
- group: operate
  title: ''
  type: Support
  url: https://www.usadata.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.usadata.com/resources/learning-lab
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usadata.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usadata.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.sl360.com/signin/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usadata
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usadata-inc-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/usadata-inc-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/usadata-inc-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/usadata-inc-sandbox.yml
created: '2026-07-17'
description: USADATA is a data and marketing intelligence company founded in 1998 and headquartered in New York City, backed by Insight Partners. It maintains a database of 260+ million US consumer records, 15+ million businesses, and 190 million households, updated monthly, and provides audience intelligence, data enrichment, hygiene, and omnichannel campaign activation. Products include the SL360 self-serve audience platform, Hailey AI conversational audience builder, a white-label Leads Portal with an embeddable Leads Module, and RESTful APIs for real-time and batch enrichment, audience building, hygiene (address standardization, NCOA, dedup, deceased suppression), and matchback attribution, with integrations into Salesforce, HubSpot, Marketo, and other CRM and marketing platforms. One machine-readable contract is published — the Leads Engine SOAP service at leadsengine.usadata.com serves a WSDL anonymously declaring 24 operations for counts, pricing, ordering, suppression, address lookup
  and geography. The REST APIs the marketing site advertises publish no spec, and API credentials are sales-gated with no developer portal, no reference documentation and no self-service sign-up.
image: https://static1.squarespace.com/static/69dd1686c455113b9719b22c/t/69dd16cec455113b9719c333/1723120623587/USD_logo_1C_NEBULON.png
layout: provider
mcp_servers:
- description: USADATA ships no MCP server. Searched the docs, npm, and the MCP registries on 2026-08-13 and found nothing first-party. What follows is a CANDIDATE tool set derived one-for-one from the 24 operations
  name: MCP Server (candidate, derived from the Leads Engine WSDL)
  slug: mcp-server-candidate-derived-from-the-leads-engine-wsdl
modified: '2026-08-13'
name: USADATA, Inc.
nav: Providers
network: true
overview: 'USADATA, Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Marketing, Data Enrichment, and Audience Targeting.


  USADATA, Inc.''s developer surface includes authentication, signup flow, API reference, engineering blog, support, sandbox, and 18 more developer resources.'
plans:
- name: Usadata Inc Plans Pricing
  plan_count: 0
  slug: usadata-inc-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Usadata Inc Rate Limits
  slug: usadata-inc-rate-limits
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 28.2
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 31.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Usadata Inc Authentication
  slug: usadata-inc-authentication
  summary_line: custom-soap-body-credential · 1 scheme
- kind: domain-security
  name: Usadata Inc Domain Security
  slug: usadata-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usadata-inc
tags:
- Company
- Data
- Marketing
- Data Enrichment
- Audience Targeting
- Data Hygiene
- Direct Mail
- Leads
- SOAP
- Mailing Lists
website: https://www.usadata.com/
---
