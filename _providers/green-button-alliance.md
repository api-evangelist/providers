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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Green Button Alliance Agentic Access
  operation_count: 24
  slug: green-button-alliance-agentic-access
  summary_line: 24 operations · 8 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Green Button Connect My Data resource server API as specified by the Green Button Alliance against NAESB REQ.21 ESPI 4.0 — read access to ApplicationInformation, Authorization, UsagePoint and bulk
  name: Green Button Connect My Data (CMD) ESPI Resource Server API
  slug: green-button-connect-my-data-api
- description: The Third Party side of the OpenESPI reference implementation — ApplicationInformation, Authorization and RetailCustomer operations documented as legacy Swagger 1.2 resource listings served from GBA's
  name: Green Button Third Party (OpenESPI) API
  slug: green-button-third-party-api
- description: Green Button Alliance OpenESPI Authorization Server API from Green Button Alliance — 12 path(s) described in OpenAPI.
  name: Green Button Alliance OpenESPI Authorization Server API
  slug: green-button-alliance-authorization-server-openapi
artifact_total: 18
asyncapis:
- description: ''
  name: Green Button Alliance Webhooks
  slug: green-button-alliance-webhooks
collections:
- collection_type: open
  name: Green Button Resource Server ApplicationInformation API Documentation
  slug: open-green-button-alliance-application-information
- collection_type: open
  name: OpenESPI Authorization Server API
  slug: open-green-button-alliance-authorization-server
- collection_type: open
  name: Green Button API Documentation
  slug: open-green-button-alliance-green-button-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/GreenButtonAlliance/OpenAPI-Green-Button-Documentation/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/GreenButtonAlliance/OpenAPI-Green-Button-Documentation/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/green-button-alliance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/green-button-alliance-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/green-button-alliance-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/green-button-alliance-authentication.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/green-button-alliance-function-blocks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/green-button-alliance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/green-button-alliance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/green-button-alliance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/green-button-alliance-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/green-button-alliance-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/green-button-alliance-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/green-button-alliance-webhooks.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/green-button-alliance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/green-button-alliance-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/green-button-alliance-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/green-button-alliance-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/green-button-alliance-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/green-button-alliance-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/green-button-alliance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/GreenButtonAlliance/OpenESPI-GreenButton-Java/blob/main/openespi-common/SECURITY.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.greenbuttonalliance.org/developer-resources
- group: operate
  title: ''
  type: Support
  url: https://www.greenbuttonalliance.org/faqs-technical
- group: operate
  title: ''
  type: Support
  url: https://www.greenbuttonalliance.org/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.greenbuttonalliance.org/offerings/certification
- group: start
  title: ''
  type: SignUp
  url: https://www.greenbuttonalliance.org/register
- group: start
  title: ''
  type: Login
  url: https://www.greenbuttonalliance.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greenbuttonalliance.org/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greenbuttonalliance.org/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.greenbuttonalliance.org/
- group: company
  title: ''
  type: About
  url: https://www.greenbuttonalliance.org/about-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.greenbuttonalliance.org/developer-resources
- group: docs
  title: ''
  type: Documentation
  url: https://www.greenbuttonalliance.org/technical-info
- group: docs
  title: ''
  type: APIReference
  url: https://greenbuttonalliance.github.io/OpenESPI-GreenButton-API-Documentation/API/
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.greenbuttonalliance.org/.well-known/openid-configuration
- group: auth
  title: ''
  type: Certification
  url: https://www.greenbuttonalliance.org/testing
- group: auth
  title: ''
  type: Certification
  url: https://www.greenbuttonalliance.org/offerings/certification
- group: other
  title: ''
  type: Directory
  url: https://www.greenbuttonalliance.org/directory-services
- group: docs
  title: ''
  type: Specification
  url: https://www.greenbuttonalliance.org/purchase-the-standard
- group: docs
  title: ''
  type: Specification
  url: https://www.naesb.org/espi_standards.asp
- group: start
  title: ''
  type: Sandbox
  url: https://www.greenbuttonalliance.org/sandbox
- group: build
  title: ''
  type: Tools
  url: https://dmdvalidator.greenbuttonalliance.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GreenButtonAlliance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/green-button-alliance
- group: company
  title: ''
  type: Blog
  url: https://www.greenbuttonalliance.org/news
- group: other
  title: ''
  type: Membership
  url: https://www.greenbuttonalliance.org/membership-information
- group: operate
  title: ''
  type: ContactUs
  url: https://www.greenbuttonalliance.org/contact-us
- group: other
  title: ''
  type: Archive
  url: https://archive.greenbuttondata.org/
created: '2026-07-27'
description: 'The Green Button Alliance (GBA) is the non-profit that stewards, tests and certifies the Green Button standard — the NAESB REQ.21 Energy Services Provider Interface (ESPI) profile for utility customer electricity, natural gas and water usage data, in its Download My Data (DMD) and Connect My Data (CMD) forms. Incorporated in North Carolina and headquartered at PO Box 268, Jamison, Pennsylvania, it was formed after the 2012 White House / U.S. Department of Energy / NIST call to action and is the industry''s only source of Green Button certification (Data Custodian DMD $3,000, CMD $3,200, membership not required), alongside a free public Directory Services listing of utilities, third-party apps and platform providers. GBA sits in the standards-and-certification layer of the United States energy value chain, above the investor-owned utilities and the energy-data platforms (UtilityAPI, Con Edison and Enbridge Gas are sponsor members) that actually move consumer data. Its API posture
  is contracts without a service: three real OpenAPI 3.x definitions - the CMD ESPI resource server, the ApplicationInformation registration resource, and the OpenESPI OAuth 2.0 / OIDC authorization server - are published free under Apache 2.0 on GitHub, but the normative ESPI v4.0 standard itself must be purchased from NAESB, GBA operates no production consumer-data or market-data API of its own, and its ESPI sandbox at sandbox.greenbuttonalliance.org:8443 is offline pending a replacement platform expected 2026Q3. Green Button in the United States is voluntary — there is no federal mandate — with obligation arriving only through state action and, outside the US, Ontario''s O. Reg. 633/21.'
examples:
- key_count: 5
  name: Green Button Alliance Backchannel Subscription Request
  slug: green-button-alliance-backchannel-subscription-request
- key_count: 6
  name: Green Button Alliance Backchannel Subscription Response
  slug: green-button-alliance-backchannel-subscription-response
- key_count: 7
  name: Green Button Alliance Token Response Bulk
  slug: green-button-alliance-token-response-bulk
- key_count: 8
  name: Green Button Alliance Token Response Subscription
  slug: green-button-alliance-token-response-subscription
image: https://assets-002.noviams.com/novi-file-uploads/gba/structure/gba-logo-2023-tm-500-1.png
layout: provider
mcp_servers:
- description: Green Button Alliance operates no MCP server. This is an API Evangelist candidate tool set derived from the operations in GBA's own OpenAPI documents.
  name: Candidate MCP tool surface (derived, not published)
  slug: candidate-mcp-tool-surface-derived-not-published
modified: '2026-07-27'
name: Green Button Alliance
nav: Providers
network: true
overview: 'Green Button Alliance publishes 2 APIs on the [APIs.io](https://apis.io/) network: Green Button Connect My Data (CMD) ESPI Resource Server API and OpenESPI Authorization Server API. Tagged areas include Energy, United States, Utilities, Electricity, and Gas.


  The Green Button Alliance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Green Button Alliance''s developer surface includes authentication, code examples, sandbox, support, pricing, signup flow, documentation, and 44 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Green Button Alliance Rate Limits
  slug: green-button-alliance-rate-limits
scopes:
- name: Green Button Alliance Scopes
  scope_count: 0
  slug: green-button-alliance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.0
  delta: 8.4
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 45.5
    contract_quality: 61.1
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 45.5
    operational_transparency: 21.1
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 82.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/green-button-alliance/refs/heads/main/screenshots/green-button-alliance-2026-08-07T165838.png
security:
- kind: authentication
  name: Green Button Alliance Authentication
  slug: green-button-alliance-authentication
  summary_line: http/mutualTLS/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Green Button Alliance Domain Security
  slug: green-button-alliance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Green Button Alliance Vulnerability Disclosure
  slug: green-button-alliance-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: green-button-alliance
tags:
- Energy
- United States
- Utilities
- Electricity
- Gas
- Water
- Smart Metering
- Green Button
- ESPI
- Standards Body
- Certification
- Consumer Energy Data
website: https://www.greenbuttonalliance.org/
---
