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
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rics Agentic Access
  operation_count: 16
  slug: rics-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 1
apis:
- description: The RICS DigitalCommunity API is a live, RICS-operated REST API served from api.rics.org whose OpenAPI 3.0.1 contract is published anonymously and without credentials at https://api.rics.org/swagger/v
  name: RICS DigitalCommunity API
  slug: rics-digitalcommunity-api
artifact_total: 13
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool list derived from the OpenAPI - RICS publishes no MCP server (api.rics.org/mcp returns 404)
  slug: candidate-mcp-tool-list-derived-from-the-openapi-rics-publishes-no-mcp-server-apiricsorgmcp-returns-404
modified: '2026-07-26'
name: RICS (Royal Institution of Chartered Surveyors)
nav: Providers
network: true
overview: 'RICS (Royal Institution of Chartered Surveyors) publishes 1 API on the [APIs.io](https://apis.io/) network: RICS DigitalCommunity API. Tagged areas include Real Estate, United Kingdom, Industry Body, Valuation, and Standards.


  RICS (Royal Institution of Chartered Surveyors)''s developer surface includes authentication, changelog, code examples, engineering blog, support, signup flow, pricing, and 40 more developer resources.'
random_paper: 135
scopes:
- name: Rics Scopes
  scope_count: 1
  slug: rics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 40.3
    developer_ergonomics: 21.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- Real Estate
- United Kingdom
- Industry Body
- Valuation
- Standards
- Surveying
- Property Measurement
- Regulation
- Construction
- PropTech
website: https://www.rics.org/
---
