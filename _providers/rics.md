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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rics Agentic Access
  operation_count: 16
  slug: rics-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The AzureStorage API from RICS (Royal Institution of Chartered Surveyors) — 6 operation(s) for azurestorage.
  name: RICS (Royal Institution of Chartered Surveyors) Azure Storage API
  slug: rics-azurestorage-api
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The OlaMerchantPost API from RICS (Royal Institution of Chartered Surveyors) — 1 operation(s) for olamerchantpost.
  name: RICS (Royal Institution of Chartered Surveyors) Ola Merchant Post API
  slug: rics-olamerchantpost-api
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The Payment API from RICS (Royal Institution of Chartered Surveyors) — 3 operation(s) for payment.
  name: RICS (Royal Institution of Chartered Surveyors) Payment API
  slug: rics-payment-api
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The Profile API from RICS (Royal Institution of Chartered Surveyors) — 1 operation(s) for profile.
  name: RICS (Royal Institution of Chartered Surveyors) Profile API
  slug: rics-profile-api
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The Regulation API from RICS (Royal Institution of Chartered Surveyors) — 3 operation(s) for regulation.
  name: RICS (Royal Institution of Chartered Surveyors) Regulation API
  slug: rics-regulation-api
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The SurveyWriter API from RICS (Royal Institution of Chartered Surveyors) — 1 operation(s) for surveywriter.
  name: RICS (Royal Institution of Chartered Surveyors) Survey Writer API
  slug: rics-surveywriter-api
- baseURL: https://api.rics.org
  baseurl_source: declared
  description: The Token API from RICS (Royal Institution of Chartered Surveyors) — 1 operation(s) for token.
  name: RICS (Royal Institution of Chartered Surveyors) Token API
  slug: rics-token-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-rics-azure-ad-b2c-openid-configuration
- collection_type: open
  name: API Collection
  slug: open-rics-data-standard-3.3
- collection_type: open
  name: API Collection
  slug: open-rics-data-standard-3.3
- collection_type: open
  name: API Collection
  slug: open-rics-data-standard-3.3
- collection_type: open
  name: API Collection
  slug: open-rics-data-standard-3.3
- collection_type: open
  name: API Collection
  slug: open-rics-data-standard-3.3
- collection_type: open
  name: DigitalCommunity API
  slug: open-rics-digitalcommunity-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/RICS-Data-Standard/RDS/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/RICS-Data-Standard/RDS/releases
- group: other
  title: ''
  type: Overlay
  url: overlays/rics-digitalcommunity-api-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/RICS-Data-Standard/RDS/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rics-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rics-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rics-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rics-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.rics.org/
- group: company
  title: ''
  type: About
  url: https://www.rics.org/about-rics
- group: other
  title: ''
  type: Standards
  url: https://www.rics.org/profession-standards/rics-standards-and-guidance
- group: other
  title: ''
  type: Standards
  url: https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/valuation-standards/red-book
- group: other
  title: ''
  type: Standards
  url: https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/real-estate-standards/rics-property-measurement-2nd-edition
- group: other
  title: ''
  type: Standards
  url: https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/construction-standards/rics-data-standards
- group: docs
  title: ''
  type: JSONSchema
  url: openapi/rics-data-standard-3.3.3-schema.json
- group: docs
  title: ''
  type: XMLSchema
  url: openapi/rics-data-standard-3.3.3-schema.xsd
- group: design
  title: ''
  type: DataModel
  url: openapi/rics-data-standard-3.3.3-description.json
- group: build
  title: ''
  type: Examples
  url: openapi/rics-data-standard-3.3.3-example.json
- group: build
  title: ''
  type: Examples
  url: openapi/rics-data-standard-3.3.3-ipms-example.json
- group: build
  title: ''
  type: Examples
  url: openapi/rics-data-standard-3.3.3-icms-example.json
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/RICS-Data-Standard/RDS
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RICS-Data-Standard
- group: other
  title: ''
  type: OpenIDConnect
  url: openapi/rics-azure-ad-b2c-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: https://b2clogin.rics.org/ricsb2clive.onmicrosoft.com/B2C_1A_RICS_signup_signin/v2.0/.well-known/openid-configuration
- group: start
  title: ''
  type: Login
  url: https://services.rics.org/Rics.IntermediaryIdentityService/
- group: other
  title: ''
  type: Regulation
  url: https://www.rics.org/regulation
- group: other
  title: ''
  type: Directory
  url: https://www.ricsfirms.com/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.isurv.com/
- group: company
  title: ''
  type: Partners
  url: https://www.rics.org/get-involved/rics-tech-partner-programme
- group: company
  title: ''
  type: Blog
  url: https://www.rics.org/news-insights
- group: operate
  title: ''
  type: Support
  url: https://www.rics.org/footer/contact-us
- group: operate
  title: ''
  type: Community
  url: https://community.rics.org/home
- group: start
  title: ''
  type: SignUp
  url: https://www.rics.org/join-rics/apply-to-join-rics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rics.org/join-rics/join-fees
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rics.org/renew-my-membership/professional-fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rics.org/footer/rics-org-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rics.org/footer/rics-privacy-policy
- group: other
  title: ''
  type: Email
  url: mailto:datastandards@rics.org
- group: other
  title: ''
  type: Email
  url: mailto:join@rics.org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rics
created: '2026-07-26'
description: 'RICS, the Royal Institution of Chartered Surveyors, is the British royal-chartered professional body founded in London in 1868 that qualifies, regulates and sets standards for surveyors, valuers and built-environment professionals worldwide, with the United Kingdom as its home market. In the property value chain it sits on the professional and valuation side rather than the listings side: it writes the RICS Valuation - Global Standards (the Red Book, incorporating IVS), the RICS Home Survey Standard, RICS Property Measurement / IPMS, ICMS, ILMS and the Rules of Conduct, it regulates roughly 12,000 RICS-regulated firms, and it runs the consumer-facing Find a Surveyor directory at ricsfirms.com and the isurv knowledge platform. Because the United Kingdom has no MLS, there is no RESO here at all - no RESO Web API or Data Dictionary certification, no OData $metadata, no Universal Property Identifier - so the "certified but unreachable" pattern does not apply; there is simply no
  listing-data certification layer in this market. What RICS does publish is genuinely machine-readable: the RICS Data Standard (RDS) 3.3.3 is an MIT-licensed JSON Schema and XSD covering land, property and infrastructure assets and incorporating ICMS, ILMS, IPMS, IVS and IBOS, hosted openly on GitHub at RICS-Data-Standard/RDS and downloadable anonymously. RICS also operates one real production API - the DigitalCommunity API at api.rics.org, whose OpenAPI 3.0.1 contract is served publicly and anonymously from a live Swagger UI - but it is not a public data API: it exposes RICS firm regulation schemes, PII and redress records, subscriptions, payments, member profiles and survey-writer integration, and its own description states that credentials must first be issued by RICS. There is no developer portal, no self-serve signup, and no open dataset from RICS; the UK''s open property data layer belongs to HM Land Registry and Ordnance Survey, not to the professional body.'
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool list derived from the OpenAPI - RICS publishes no MCP server (api.rics.org/mcp returns 404)
  slug: candidate-mcp-tool-list-derived-from-the-openapi-rics-publishes-no-mcp-server-apiricsorgmcp-returns-404
modified: '2026-07-26'
name: RICS (Royal Institution of Chartered Surveyors)
nav: Providers
network: true
overview: 'RICS (Royal Institution of Chartered Surveyors) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Azure Storage API, Ola Merchant Post API, Payment API, and 4 more. Tagged areas include Real-Estate, United Kingdom, Industry Body, Valuation, and Standards.


  RICS (Royal Institution of Chartered Surveyors)''s developer surface includes authentication, changelog, code examples, engineering blog, support, signup flow, pricing, and 43 more developer resources.'
random_paper: 13
scopes:
- name: Rics Scopes
  scope_count: 1
  slug: rics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 40.3
    developer_ergonomics: 28.0
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rics/refs/heads/main/screenshots/rics-2026-09-02T153806.png
security:
- kind: authentication
  name: Rics Authentication
  slug: rics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rics Domain Security
  slug: rics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rics
tags:
- Real-Estate
- United Kingdom
- Industry Body
- Valuation
- Standards
- Surveying
- Property Measurement
- Regulations
- Construction
- PropTech
website: https://www.rics.org/
---
