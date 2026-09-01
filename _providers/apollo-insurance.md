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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Apollo Insurance Agentic Access
  operation_count: 8
  slug: apollo-insurance-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 3
apis:
- description: The Affiliates API from APOLLO Insurance — 2 operation(s) for affiliates.
  name: APOLLO Insurance Affiliates API
  slug: apollo-insurance-affiliates-api
- description: APOLLO public API
  name: APOLLO Insurance API
  slug: apollo-insurance-api-api
- description: The Compliance API from APOLLO Insurance — 3 operation(s) for compliance.
  name: APOLLO Insurance Compliance API
  slug: apollo-insurance-compliance-api
- description: The Quote API from APOLLO Insurance — 1 operation(s) for quote.
  name: APOLLO Insurance Quote API
  slug: apollo-insurance-quote-api
artifact_total: 13
asyncapis:
- description: ''
  name: Apollo Insurance Covertrack Webhooks
  slug: apollo-insurance-covertrack-webhooks
collections:
- collection_type: open
  name: Public API - Affiliates
  slug: open-apollo-insurance-affiliates-legacy
- collection_type: open
  name: Affiliates API
  slug: open-apollo-insurance-affiliates
- collection_type: open
  name: CoverTrack API's
  slug: open-apollo-insurance-covertrack
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/apollo-insurance-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/apollo-insurance-affiliates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/apollo-insurance-affiliates-legacy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/apollo-insurance-covertrack-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apollo-insurance-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apollo-insurance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/apollo-insurance-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apollo-insurance-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/apollo-insurance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apollo-insurance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apollo-insurance-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apollo-insurance-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apollo-insurance-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/apollo-insurance-examples.yml
- group: design
  title: ''
  type: Components
  url: components/apollo-insurance-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apollo-insurance-covertrack-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apollo-insurance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://apollocover.com/security
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://apollocover.com/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-insurance-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apollo-insurance-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-insurance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-insurance-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://apollocover.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apollocover.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apollocover.com/docs/public-affiliate-api/27500feeac1b7-introduction
- group: company
  title: ''
  type: Partners
  url: https://apollocover.com/partnerships
- group: operate
  title: ''
  type: SupportCenter
  url: https://help.apollocover.com/
- group: start
  title: ''
  type: CustomerPortal
  url: https://policy-portal.apollocover.com/
- group: company
  title: ''
  type: Blog
  url: https://apollocover.com/magazine
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apollocover.com/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apollocover.com/docs/public-affiliate-api/a8a7ea17b0889-affiliates-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apollocover.com/docs/public-affiliate-api/27500feeac1b7-introduction
- group: operate
  title: ''
  type: Support
  url: https://help.apollocover.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apollocover.com/terms-conditions/
- group: start
  title: ''
  type: Login
  url: https://policy-portal.apollocover.com/
- group: operate
  title: ''
  type: Contact
  url: https://apollocover.com/contact-us
- group: company
  title: ''
  type: About
  url: https://apollocover.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://apollocover.com/about-us/join-the-team
- group: company
  title: ''
  type: InvestorRelations
  url: https://apollocover.com/about-us/investor-relations
- group: company
  title: ''
  type: Press
  url: https://apollocover.com/about-us/in-the-news
- group: other
  title: ''
  type: Reviews
  url: https://apollocover.com/reviews
- group: other
  title: ''
  type: SiteMap
  url: https://apollocover.com/site-map
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apolloexchange
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/theapollomag
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/apolloinsurance
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/apolloinsurance
created: '2026-07-25'
description: 'APOLLO Insurance (APOLLO Insurance Agency Ltd., apollocover.com) is a Vancouver-founded Canadian digital insurance brokerage and MGA-style distribution platform that sells personal and small-commercial coverage entirely online — tenant and student tenant insurance in every province, homeowner, condo and townhouse, landlord and pet insurance on the personal side, and general liability, professional liability and directors and officers coverage on the business side. APOLLO does not underwrite; it distributes on a commission basis on behalf of A+ to A- rated Canadian carriers, and it sits in the thin digital-broker layer of a Big-Few Canadian market dominated by Intact, Definity, Co-operators and Desjardins. Its distinctive business is embedded tenant insurance for REITs and property managers: automated resident enrolment at lease signing, renewal handling, and real-time building-level compliance tracking, delivered through a Yardi Systems integration and its CoverTrack compliance
  product. Unusually for the Canadian insurance sector, APOLLO publishes a genuine, publicly readable developer portal at docs.apollocover.com — a Stoplight workspace with three public projects and downloadable OpenAPI definitions covering quote and application (pre-fill) for tenant insurance and compliance-status lookup for partner properties. The surface is real but partner-scoped: every call needs an affiliateId (a co-branded APOLLO subdomain) and an x-api-key token that APOLLO issues by hand to affiliates and property-manager partners, so there is no self-serve credential path and no consumer-facing API. Canada has no open-insurance mandate — OSFI supervises prudentially, the provinces (FSRA, AMF) supervise market conduct, and Consumer-Driven Banking excludes insurance entirely — so nothing forces this disclosure; APOLLO published it as a distribution strategy. No ACORD, AL3, IVANS or agency-management-system reference appears anywhere in its public site or documentation.'
image: https://platform-assets.apollocover.com/apollo.svg
layout: provider
mcp_servers:
- description: ''
  name: APOLLO Insurance MCP Server
  slug: apollo-insurance-mcp-server
modified: '2026-07-25'
name: APOLLO Insurance
nav: Providers
network: true
overview: 'APOLLO Insurance publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Affiliates API, Compliance API, and 2 more. Tagged areas include Insurance, Canada, Insurtech, Brokers, and Embedded Insurance.


  The APOLLO Insurance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  APOLLO Insurance''s developer surface includes sandbox, code examples, authentication, documentation, engineering blog, API reference, getting-started guide, and 41 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 63.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-insurance/refs/heads/main/screenshots/apollo-insurance-2026-07-25T200828.png
security:
- kind: authentication
  name: Apollo Insurance Authentication
  slug: apollo-insurance-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Apollo Insurance Domain Security
  slug: apollo-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apollo Insurance Trust Center
  slug: apollo-insurance-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: apollo-insurance
tags:
- Insurance
- Canada
- Insurtech
- Brokers
- Embedded Insurance
- Property and Casualty
- Tenant Insurance
- Quoting
- Distribution
- Compliance
website: https://apollocover.com/
---
