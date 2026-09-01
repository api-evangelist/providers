---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The RESO Web API is the ratified transport standard for real estate data, defined as a profile of OData 4.0/4.01 (Web API Core 2.0.0 and 2.1.0). Servers MUST expose an OData XML metadata document at /
  name: RESO Web API
  slug: reso-web-api
- description: The RESO Cloud MCP Server is the one production API endpoint RESO itself operates. It speaks the Model Context Protocol over Streamable HTTP at https://services.reso.org/mcp and exposes the RESO toolc
  name: RESO Cloud MCP Server
  slug: reso-cloud-mcp
artifact_total: 9
asyncapis:
- description: ''
  name: Reso Webhooks
  slug: reso-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-reso-dd-1
- collection_type: open
  name: API Collection
  slug: open-reso-dd-2
- collection_type: open
  name: API Collection
  slug: open-reso-dd-2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/RESOStandards/reso-tools/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/RESOStandards/reso-tools/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reso.org/
- group: company
  title: ''
  type: About
  url: https://www.reso.org/about-reso/
- group: docs
  title: ''
  type: Documentation
  url: https://transport.reso.org/
- group: docs
  title: ''
  type: Specification
  url: https://www.reso.org/specs/
- group: docs
  title: ''
  type: Specification
  url: https://github.com/RESOStandards/transport/blob/main/proposals/reso-common-format.md
- group: docs
  title: ''
  type: Specification
  url: https://github.com/RESOStandards/transport/blob/main/proposals/validation-expressions.md
- group: other
  title: ''
  type: DataDictionary
  url: https://www.reso.org/data-dictionary/
- group: other
  title: ''
  type: DataDictionary
  url: https://dd.reso.org/
- group: other
  title: ''
  type: Identifiers
  url: https://www.reso.org/universal-parcel-identifier/
- group: build
  title: ''
  type: Tooling
  url: https://upi.reso.org/builder/
- group: auth
  title: ''
  type: Certification
  url: https://www.reso.org/certification/
- group: auth
  title: ''
  type: Certification
  url: https://certification.reso.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reso.org/certification-fee-schedule/
- group: other
  title: ''
  type: Membership
  url: https://www.reso.org/membership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reso.org/eula/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RESOStandards
- group: company
  title: ''
  type: Blog
  url: https://www.reso.org/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.reso.org/feed/
- group: other
  title: ''
  type: Regulation
  url: https://www.nar.realtor/handbook-on-multiple-listing-policy/operational-issues-section-12-real-estate-transaction-standards-rets-policy-statement-790
- group: other
  title: ''
  type: Email
  url: mailto:dev@reso.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tools.reso.org/
- group: docs
  title: ''
  type: APIReference
  url: https://dd.reso.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.reso.org/developer-resources/
- group: operate
  title: ''
  type: Support
  url: https://www.reso.org/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.reso.org/developer-faqs/
- group: start
  title: ''
  type: SignUp
  url: https://www.reso.org/join/
- group: operate
  title: ''
  type: Roadmap
  url: https://transport.reso.org/
- group: operate
  title: ''
  type: ChangeLog
  url: https://tools.reso.org/releases/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/reso-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reso-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://transport.reso.org/versioning/
- group: design
  title: ''
  type: Conventions
  url: conventions/reso-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reso-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reso-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reso-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/reso-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reso-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/reso-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/reso-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/reso-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reso-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/reso-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/reso-query-a-certified-server.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/reso-replicate-with-entityevent.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/reso-certify-a-server.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reso-llms.txt
- group: auth
  title: ''
  type: SecurityAudit
  url: security/reso-security-audit.yml
- group: auth
  title: ''
  type: SecurityAudit
  url: https://tools.reso.org/security/
created: '2026-07-26'
description: 'RESO, the Real Estate Standards Organization, is the United States industry body that writes and certifies the machine-readable contract for residential real estate data. It publishes the RESO Data Dictionary (the field, enumeration and lookup vocabulary) and the RESO Web API (an OData 4.0/4.01 profile, Web API Core 2.0.0 ratified Jan 2021 and 2.1.0 ratified Dec 2023), plus the RESO Common Format, EntityEvent replication, Push Replication with Webhooks, Validation Expressions and the URN-based Universal Parcel Identifier (UPI). NAR Policy Statement 7.90 requires MLSs owned and operated by associations of REALTORS to implement the Data Dictionary and the Web API and to adopt new releases within one year of ratification, which makes this the only mandated machine-readable API contract in the API Evangelist sector study that is imposed by an industry body rather than a regulator. RESO itself operates no production API and holds no listing data: it certifies other people''s servers.
  Its specifications, reference OData EDMX metadata and Data Dictionary JSON are freely and anonymously downloadable from transport.reso.org and the RESOStandards GitHub organization (a EULA click-through wraps the reso.org copies), and the certification directory at reso.org/certificates and certification.reso.org is public without login. Reachability is the separate fact: a RESO-certified endpoint is run by a local MLS, and credentials for it are issued only after a data licence with that MLS is signed, so certification here means conformance, never public access.'
image: https://www.reso.org/wp-content/uploads/2021/04/RESO-Logo-Fullname_Horizontal_Blue.png
layout: provider
mcp_servers:
- description: ''
  name: RESO MCP server manifest (hosted cloud server + local stdio server)
  slug: reso-mcp-server-manifest-hosted-cloud-server-local-stdio-server
modified: '2026-07-26'
name: RESO (Real Estate Standards Organization)
nav: Providers
network: true
overview: 'RESO (Real Estate Standards Organization) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, United States, RESO, MLS, and Property Listings.


  The RESO (Real Estate Standards Organization) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RESO (Real Estate Standards Organization)''s developer surface includes documentation, pricing, engineering blog, API reference, getting-started guide, support, signup flow, and 45 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 80.4
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 31.6
  open_source:
    applies: true
    score: 25.0
  previous_composite: 43.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reso/refs/heads/main/screenshots/reso-2026-08-17T081530.png
security:
- kind: authentication
  name: Reso Authentication
  slug: reso-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Reso Domain Security
  slug: reso-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reso
tags:
- Real-Estate
- United States
- RESO
- MLS
- Property Listings
- Data Standards
- OData
- Industry Body
- IDX
- PropTech
website: https://www.reso.org/
---
