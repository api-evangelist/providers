---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: FHIR R4 (4.0.1) read-only Patient Access API from DentaQuest, the Sun Life U.S. dental company, published under the CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Third-party applica
  name: DentaQuest FHIR Patient Access API
  slug: sun-life-dentaquest-fhir-patient-access
- description: FHIR R4 (4.0.1) Provider Directory API from DentaQuest, the Sun Life U.S. dental company, conforming to the HL7 Da Vinci PDex Plan-Net Implementation Guide 1.1.0 and published under CMS-9115-F. Expose
  name: DentaQuest FHIR Provider Directory API
  slug: sun-life-dentaquest-fhir-provider-directory
- description: Anonymous FHIR R4 conformance endpoint for the DentaQuest (Sun Life U.S.) interoperability platform. A single GET /metadata operation returns the CapabilityStatement of the underlying Azure Healthcare
  name: DentaQuest FHIR Metadata API
  slug: sun-life-dentaquest-fhir-metadata
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sun-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sunlife.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.sunlife.com/en/about-us/
- group: other
  title: ''
  type: Canada
  url: https://www.sunlife.ca/
- group: other
  title: ''
  type: UnitedStates
  url: https://www.sunlife.com/us/en/
- group: other
  title: ''
  type: DigitalCapabilities
  url: https://www.sunlife.com/us/en/employers/products-and-services/digital-capabilities/
- group: build
  title: ''
  type: PartnerIntegrations
  url: https://www.sunlife.com/us/en/employers/products-and-services/digital-capabilities/sun-life-link/
- group: start
  title: ''
  type: EmployerPortal
  url: https://www.sunlife.com/us/en/employers/products-and-services/digital-capabilities/sun-life-connect/
- group: start
  title: ''
  type: MemberPortal
  url: https://www.sunlife.com/us/en/employers/products-and-services/digital-capabilities/member-portal/
- group: start
  title: ''
  type: Onboarding
  url: https://www.sunlife.com/us/en/employers/products-and-services/digital-capabilities/sun-life-onboard/
- group: other
  title: ''
  type: WhitePapers
  url: https://www.sunlife.com/us/en/employers/products-and-services/digital-capabilities/sun-life-link/navigating-connectivity-in-benefits-administration/
- group: other
  title: ''
  type: SignIn
  url: https://login.sunlifeconnect.com/commonlogin/
- group: operate
  title: ''
  type: AdvisorCommunity
  url: https://connect.sunlife.ca/s/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.sunlife.com/en/investors/
- group: company
  title: ''
  type: News
  url: https://www.sunlife.com/en/newsroom/
- group: company
  title: ''
  type: Careers
  url: https://www.sunlife.com/en/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sun-life-financial
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dentaquest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dentaquest.com/en/interoperability-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dentaquest.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dentaquest.com/en/interoperability-api
- group: start
  title: ''
  type: SignUp
  url: https://dentaquest.logicmanager.com/incidents/?t=1241&p=215&k=F0E3BD92F157F9B73EDE82834286E7CEA4044134B39D92AC3EE7E56392194241
- group: operate
  title: ''
  type: Support
  url: https://www.dentaquest.com/en/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dentaquest.com/en/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dentaquest.com/en/policies/internet-privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.dentaquest.com/en/policies/hipaa-privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/sun-life-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sun-life-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/sun-life-dentaquest-okta-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sun-life-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sun-life-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sun-life-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sun-life-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sun-life-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sun-life-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sun-life-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sun-life-llms.txt
created: '2026-07-25'
description: 'Sun Life Financial Inc. is a Canadian multinational life and health insurer and asset manager headquartered in Toronto, one of the "life trio" that dominates Canada''s insurance market alongside Manulife and Great-West Lifeco. Sun Life writes individual life insurance, individual and group health and dental coverage, group benefits, disability and absence management, annuities and retirement products, and runs a large wealth business through Sun Life Global Investments, SLC Management and MFS Investment Management, with operations across Canada, the United States, the United Kingdom, Ireland and Asia. In the United States it is a leading group benefits, stop-loss and dental carrier and owns DentaQuest. Sun Life publishes no developer portal under its own brand: its only named Sun Life API surface is Sun Life Link, a partner-gated benefits-connectivity program that exchanges evidence of insurability, plan setup, enrollment, billing and absence data with HR and benefits-administration
  platforms including Workday, ADP, UKG, PlanSource, Employee Navigator and bswift, negotiated per client rather than signed up for. The public, machine-readable APIs in the Sun Life group belong to DentaQuest, its U.S. dental subsidiary, which runs an Azure API Management developer portal at developers.dentaquest.com publishing three OpenAPI 3.0.1 definitions: a SMART-on-FHIR Patient Access API, a Da Vinci PDex Plan-Net Provider Directory API and an anonymous FHIR CapabilityStatement endpoint, all released under the CMS Interoperability and Patient Access Final Rule (CMS-9115-F) and served for both the DentaQuest and Delta Dental of Massachusetts brands. Canada''s supervisory split between OSFI and the provincial conduct regulators, and the exclusion of insurance from Consumer-Driven Banking, means no open-insurance mandate creates a forcing function for a public Sun Life API in its home market; the U.S. CMS mandate is what produced the only public one.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool list (derived, not provider-published)
  slug: candidate-mcp-tool-list-derived-not-provider-published
modified: '2026-07-25'
name: Sun Life
nav: Providers
network: true
overview: 'Sun Life publishes 3 APIs on the [APIs.io](https://apis.io/) network: DentaQuest FHIR Patient Access API, DentaQuest FHIR Provider Directory API, and DentaQuest FHIR Metadata API. Tagged areas include Insurance, Canada, Life Insurance, Health Insurance, and Employee Benefits.


  Sun Life''s developer surface includes product news, documentation, API reference, getting-started guide, signup flow, support, authentication, and 31 more developer resources.'
random_paper: 13
scopes:
- name: Sun Life Scopes
  scope_count: 5
  slug: sun-life-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 43.8
  delta: -4.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 32.3
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 47.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
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
    score: 71.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sun Life Authentication
  slug: sun-life-authentication
  summary_line: oauth2/openIdConnect/apiKey · 4 schemes
- kind: domain-security
  name: Sun Life Domain Security
  slug: sun-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sun-life
tags:
- Insurance
- Canada
- Life Insurance
- Health Insurance
- Employee Benefits
- Group Benefits
- Dental Insurance
- Disability
- Wealth Management
- Financial Services
- Carrier
- FHIR
- Patient Access
- Provider Directory
- Healthcare Interoperability
- CMS-9115-F
- DentaQuest
- SMART on FHIR
- Dental Benefits
website: https://www.sunlife.com/
---
