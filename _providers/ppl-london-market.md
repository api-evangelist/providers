---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Ppl London Market Agentic Access
  operation_count: 67
  slug: ppl-london-market-agentic-access
  summary_line: 67 operations · 29 acting
api_count: 5
apis:
- description: 'Manages the Placement structure in PPL Next Gen - Placements, Programmes, Contracts and the Sections within a Contract - together with carrier and underwriter participations, role assignment, and the '
  name: PPL Placements API
  slug: ppl-placements-api
- description: 'Enables underwriters to retrieve Submission requests supplied by a broker and to manage their negotiation of terms of cover, including reassignment of a negotiation and sending a response back to the '
  name: PPL Submissions API
  slug: ppl-submissions-api
- description: Retrieves the organisation reference data held in the platform that is a prerequisite for interacting with Placement and Firm Order resources - broker and carrier organisations, their team structures,
  name: PPL Organisations API
  slug: ppl-organisations-api
- description: Manages document files and document metadata across the Placement hierarchy, including the Market Reform Contract (MRC) itself and its supporting documents, with versioning, content retrieval, downloa
  name: PPL Documents API
  slug: ppl-documents-api
- description: Retrieves informative and actionable notifications about an interested party's involvement in the placement process, plus the business transaction log for contract-related engagements. Pull-based only
  name: PPL Events API
  slug: ppl-events-api
artifact_total: 15
collections:
- collection_type: open
  name: document
  slug: open-ppl-london-market-documents
- collection_type: open
  name: event
  slug: open-ppl-london-market-events
- collection_type: open
  name: organisation
  slug: open-ppl-london-market-organisations
- collection_type: open
  name: placement
  slug: open-ppl-london-market-placements
- collection_type: open
  name: submission
  slug: open-ppl-london-market-submissions
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/ppl-london-market-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ppl-london-market-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ppl-london-market-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ppl-london-market-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ppl-london-market-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ppl-london-market-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ppl-london-market-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ppl-london-market-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ppl-london-market-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ppl-london-market-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ppl-london-market-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ppl-london-market-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ppl-london-market-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/ppl-london-market-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pplnextgen.com/Get-Started
- group: build
  title: ''
  type: Postman
  url: https://developer.pplnextgen.com/Explore-Innovate
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ppl-london-market-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ppl-london-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://placingplatformlimited.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pplnextgen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pplnextgen.com/Get-Started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pplnextgen.com/Explore-Innovate
- group: auth
  title: ''
  type: Authentication
  url: https://developer.pplnextgen.com/Get-Started/Authentication-Information
- group: start
  title: ''
  type: SignUp
  url: https://developer.pplnextgen.com/Get-Started/Registration-Onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pplnextgen.com/Get-Started/Base-API-Standard
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pplnextgen.com/Get-Started/Reference-Architecture
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.pplnextgen.com/Get-Started/RoadMap
- group: operate
  title: ''
  type: Support
  url: https://developer.pplnextgen.com/Support
- group: docs
  title: ''
  type: Documentation
  url: https://placingplatformlimited.com/api-integrations/
- group: docs
  title: ''
  type: Documentation
  url: https://placingplatformlimited.com/the-core-placing-platform/
- group: start
  title: ''
  type: Login
  url: https://www.pplnextgen.com/PPL_Authentication/
- group: company
  title: ''
  type: Blog
  url: https://placingplatformlimited.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://placingplatformlimited.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ppl-placing-platform-limited/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.pplnextgen.com/Terms-And-Conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://placingplatformlimited.com/privacy-notice/
- group: operate
  title: ''
  type: Contact
  url: https://placingplatformlimited.com/contacts/
created: '2026-07-25'
description: 'PPL (Placing Platform Limited) is the London Market''s not-for-profit electronic placing platform, incorporated in England and Wales in 2013 and trading since the first risk was bound on the platform in July 2016. Owned collectively by the market it serves, PPL lets brokers and carriers quote, negotiate, bind and renew open-market (re)insurance risks electronically across almost all classes of business written in London, and is used by roughly 200 carriers and 200 broking firms. It is market infrastructure rather than a carrier or a broker - it writes no insurance and carries no risk - and it is one of the accredited placing platforms underpinning Lloyd''s Blueprint Two, generating the Core Data Record for bound business. Its API posture is unusual for insurance and genuinely good: the PPL Next Gen API Developer Portal at developer.pplnextgen.com is publicly readable and publishes a real API catalogue of five REST collections - Organisations, Placements, Submissions, Documents
  and Events - each with a downloadable OpenAPI 3.0 document and a Postman collection, built on REST standards and the ACORD GRLC (Global Reinsurance and Large Commercial) data model. Actually calling the APIs is market-gated rather than self-serve: consumers must be onboarded by PPL, subscribe to LIMOSS API Common Services, be guested into the Microsoft Entra ID (Azure AD) tenant of the LIMOSS API Gateway, and register an X.509 certificate per environment. The surface covers quote and bind (submission negotiation, contract negotiation, participations, firm order) and contract issuance via the Market Reform Contract document set; there is no claims or FNOL API, and no webhook or event-push surface - the Events API is pull-based.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Derived candidate MCP tool surface (no server published by PPL)
  slug: derived-candidate-mcp-tool-surface-no-server-published-by-ppl
modified: '2026-07-25'
name: PPL
nav: Providers
network: true
overview: 'PPL publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Placements API, Submissions API, Organisations API, and 2 more. Tagged areas include Insurance, United Kingdom, London Market, Lloyd''s of London, and Reinsurance.


  PPL''s developer surface includes authentication, sandbox, getting-started guide, documentation, API reference, signup flow, support, and 31 more developer resources.'
random_paper: 77
scopes:
- name: Ppl London Market Scopes
  scope_count: 1
  slug: ppl-london-market-scopes
  summary_line: 1 scope · authorizationCode/onBehalfOf/clientCredentials
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 49.5
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 45.9
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
    score: 63.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Ppl London Market Authentication
  slug: ppl-london-market-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Ppl London Market Domain Security
  slug: ppl-london-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ppl-london-market
tags:
- Insurance
- United Kingdom
- London Market
- Lloyd's of London
- Reinsurance
- Commercial Insurance
- Broker
- Underwriting
- Placement
- Market Infrastructure
- ACORD
- Electronic Placing
website: https://placingplatformlimited.com/
---
