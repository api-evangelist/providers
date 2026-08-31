---
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Rhino Agentic Access
  operation_count: 12
  slug: rhino-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 1
apis:
- description: The Authentication API from Rhino — 1 operation(s) for authentication.
  name: Rhino Authentication API
  slug: rhino-authentication-api
- description: The PartnerApi::V2::Test::Resident API from Rhino — 1 operation(s) for partnerapi::v2::test::resident.
  name: Rhino Partner Api::V2::Test::Resident API
  slug: rhino-partnerapi-v2-test-resident-api
- description: The PartnerApi::V2::Test::SayrhinoUser API from Rhino — 1 operation(s) for partnerapi::v2::test::sayrhinouser.
  name: Rhino Partner Api::V2::Test::Sayrhino User API
  slug: rhino-partnerapi-v2-test-sayrhinouser-api
- description: The Prospects API from Rhino — 2 operation(s) for prospects.
  name: Rhino Prospects API
  slug: rhino-prospects-api
- description: The Webhooks API from Rhino — 5 operation(s) for webhooks.
  name: Rhino Webhooks API
  slug: rhino-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Rhino Webhooks
  slug: rhino-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SayRhino Partner Authentication API
  slug: open-rhino-authentication-api
- collection_type: open
  name: SayRhino Partner API
  slug: open-rhino-partner-api
- collection_type: open
  name: SayRhino Partner Partner Api::V2::Test::Resident API
  slug: open-rhino-partnerapi-v2-test-resident-api
- collection_type: open
  name: SayRhino Partner Partner Api::V2::Test::Sayrhino User API
  slug: open-rhino-partnerapi-v2-test-sayrhinouser-api
- collection_type: open
  name: SayRhino Partner Prospects API
  slug: open-rhino-prospects-api
- collection_type: open
  name: SayRhino Partner Webhooks API
  slug: open-rhino-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/rhino-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rhino-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhino-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhino-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sayrhino.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.prod.sayrhino.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.prod.sayrhino.com/docs
- group: operate
  title: ''
  type: Support
  url: https://support.sayrhino.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.sayrhino.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sayrhino
- group: start
  title: ''
  type: SignUp
  url: https://www.sayrhino.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://portal.sayrhino.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sayrhino.com/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sayrhino.com/privacy_policy
- group: company
  title: ''
  type: Careers
  url: https://careers.sayrhino.com
- group: commercial
  title: ''
  type: Licenses
  url: https://www.sayrhino.com/licenses
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/rhino_stock/
- group: design
  title: ''
  type: Conventions
  url: conventions/rhino-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rhino-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rhino-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rhino-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/rhino-examples.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rhino-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rhino-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rhino-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rhino-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rhino-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/rhino-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rhino-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhino-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rhino-partner-api-overlay.yaml
created: '2026-08-02'
description: Rhino (SayRhino) is a New York based insurtech that replaces the traditional cash security deposit with low-cost security deposit insurance, alongside cash deposit management, renters insurance and a renter guarantee product. Founded in 2017 and now operating alongside Jetty, Rhino sells through property owners and managers across the United States and integrates with the major property management systems including Yardi, RealPage, Entrata, Rent Manager, MRI and Salesforce. Its public machine-readable surface is the SayRhino Partner API (v2) — an OAuth 2.0 client-credentials REST API, documented with a live OpenAPI 3.0.3 definition and a Redoc reference, for creating and updating insurance prospects, reading eligibility offers and coverage, and managing webhook endpoints and deliveries across fifteen prospect, policy, policy-application and delinquency events.
image: https://www.sayrhino.com/assets/rhino_favicon_website_144x144-b7265da417b6731f322eeccf89a6313a3387099dd046a807b4cabe32db0d228e.png
layout: provider
mcp_servers:
- description: ''
  name: Rhino MCP Server
  slug: rhino-mcp-server
modified: '2026-08-02'
name: Rhino
nav: Providers
network: true
overview: 'Rhino publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Partner Api::V2::Test::Resident API, Partner Api::V2::Test::Sayrhino User API, and 2 more. Tagged areas include Insurance, Insurtech, Real-Estate, Property Management, and Rentals.


  The Rhino catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rhino''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, code examples, and 25 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rhino/refs/heads/main/screenshots/rhino-2026-08-17T081558.png
security:
- kind: authentication
  name: Rhino Authentication
  slug: rhino-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Rhino Domain Security
  slug: rhino-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rhino Vulnerability Disclosure
  slug: rhino-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: rhino
tags:
- Insurance
- Insurtech
- Real-Estate
- Property Management
- Rentals
- Security Deposits
- Renters Insurance
- Webhook
- Partner API
website: https://www.sayrhino.com/
---
