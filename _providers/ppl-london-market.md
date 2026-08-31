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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Ppl London Market Agentic Access
  operation_count: 67
  slug: ppl-london-market-agentic-access
  summary_line: 67 operations · 29 acting
api_count: 5
apis:
- description: Enables the creation and management of Contract structured data.
  name: PPL Contract API
  slug: ppl-london-market-contract-api
- description: The document API from PPL — 6 operation(s) for document.
  name: PPL Document API
  slug: ppl-london-market-document-api
- description: The health API from PPL — 1 operation(s) for health.
  name: PPL Health API
  slug: ppl-london-market-health-api
- description: 'Enables the creation and management of the flow of negotiations from a Broker to an Underwriter. Negotiations shown will be those which (1) have been formally communicated to the Underwriter; and (2) '
  name: PPL Negotiation API
  slug: ppl-london-market-negotiation-api
- description: The notification API from PPL — 3 operation(s) for notification.
  name: PPL Notification API
  slug: ppl-london-market-notification-api
- description: The organisation API from PPL — 5 operation(s) for organisation.
  name: PPL Organisation API
  slug: ppl-london-market-organisation-api
- description: Enables the creation, management and processing of Open Market Underwriters and Facility Panel Underwriters that are willing to participate in the underwriting of an insured's asset or liability, repr
  name: PPL Participation API
  slug: ppl-london-market-participation-api
- description: Enables the creation and management of the Placement structure that comprises of Programmes and Contracts.
  name: PPL Placement API
  slug: ppl-london-market-placement-api
- description: Enables the creation and management of Programme structures within a Placement. This also includes the capability to add existing Contracts into a programme.
  name: PPL Programme API
  slug: ppl-london-market-programme-api
- description: Enables the creation and management of Contract sections, as structured data. Each Section represents of a specific partition of the overall risk to be insured. A section can be based upon the cover t
  name: PPL Section API
  slug: ppl-london-market-section-api
- description: Enables the retrieval of Submissions for Underwriters.
  name: PPL Submission API
  slug: ppl-london-market-submission-api
- description: The transaction API from PPL — 2 operation(s) for transaction.
  name: PPL Transaction API
  slug: ppl-london-market-transaction-api
- description: The version API from PPL — 1 operation(s) for version.
  name: PPL Version API
  slug: ppl-london-market-version-api
artifact_total: 23
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ppl-london-market-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ppl-london-market-placements-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ppl-london-market-submissions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ppl-london-market-organisations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ppl-london-market-documents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ppl-london-market-events-overlay.yaml
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
overview: 'PPL publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Contract API, Document API, Health API, and 10 more. Tagged areas include Insurance, United Kingdom, London Market, Lloyd''s of London, and Reinsurance.


  PPL''s developer surface includes authentication, sandbox, getting-started guide, documentation, API reference, signup flow, support, and 37 more developer resources.'
random_paper: 15
scopes:
- name: Ppl London Market Scopes
  scope_count: 1
  slug: ppl-london-market-scopes
  summary_line: 1 scope · authorizationCode/onBehalfOf/clientCredentials
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.6
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 48.8
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
    score: 71.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ppl-london-market/refs/heads/main/screenshots/ppl-london-market-2026-08-17T081327.png
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
- Brokers
- Underwriting
- Placement
- Market Infrastructure
- ACORD
- Electronic Placing
website: https://placingplatformlimited.com/
---
