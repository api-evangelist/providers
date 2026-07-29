---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: WestJet's IATA New Distribution Capability (NDC) direct-connect interface for travel sellers, offered in NDC schema versions 17.2 and 21.3/24.1 and delivered on Accelya's FLX/Farelogix platform. Publi
  name: WestJet Direct Connect API
  slug: westjet-direct-connect-api
artifact_total: 3
asyncapis:
- description: ''
  name: Westjet Ndc Notifications
  slug: westjet-ndc-notifications
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/westjet-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/westjet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/westjet-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://accelyastatus.statuspage.io/
- group: operate
  title: ''
  type: Roadmap
  url: https://westjetndc.com/capabilities/
- group: start
  title: ''
  type: GettingStarted
  url: https://westjetndc.com/connection-options/
- group: operate
  title: ''
  type: ChangeLog
  url: https://westjetndc.com/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/westjet-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/westjet-ndc-notifications.yml
- group: build
  title: ''
  type: Packages
  url: packages/westjet-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://westjetndc.com/news/
- group: company
  title: ''
  type: Website
  url: https://www.westjet.com/
- group: start
  title: ''
  type: Portal
  url: https://westjetndc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://westjetndc.com/capabilities/
- group: other
  title: ''
  type: TravelAgentResources
  url: https://westjettravelagents.com/
- group: build
  title: ''
  type: PolicyLibrary
  url: https://westjettravelagents.com/policy-library/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://westjettravelagents.com/policy-library/ticketing-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westjet.com/en-ca/legal/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westjet.com/en-ca/legal/privacy-policy
- group: other
  title: ''
  type: DataPortability
  url: https://www.westjet.com/en-ca/legal/privacy-policy/privacy-requests
- group: start
  title: ''
  type: Login
  url: https://westjetagentdirect.westjet.com/login-agent.html
- group: start
  title: ''
  type: SignUp
  url: https://westjetagentdirect.westjet.com/registeragency.html
- group: start
  title: ''
  type: Login
  url: https://agents.westjetvacations.com/
- group: other
  title: ''
  type: Cargo
  url: https://www.westjetcargo.com/en-ca
- group: other
  title: ''
  type: BusinessTravel
  url: https://westjetbusinesstravel.com/
- group: other
  title: ''
  type: Vacations
  url: https://www.westjetvacations.com/en/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.westjet.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/westjet-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/westjet
- group: company
  title: ''
  type: Newsroom
  url: https://www.westjet.com/en-ca/news
- group: company
  title: ''
  type: PressRoom
  url: https://westjet.mediaroom.com/
- group: operate
  title: ''
  type: Support
  url: https://www.westjet.com/en-ca/contact
created: '2026-07-28'
description: 'WestJet Airlines Ltd. is Canada''s second-largest air carrier, headquartered in Calgary, Alberta, operating scheduled passenger service to more than 100 destinations across Canada, the United States, Mexico, Central America, the Caribbean, Europe and Asia, alongside WestJet Encore, WestJet Vacations, WestJet Cargo and the Sunwing Vacations Group. In the distribution chain WestJet sits upstream of the agency channel: its inventory reaches travel sellers today through EDIFACT in the Amadeus, Sabre and Travelport GDSs, and it is standing up an IATA NDC surface (schema 17.2 and 21.3/24.1) built and hosted on Accelya''s FLX/Farelogix platform, with a stated Q4 2026 rollout. Its API posture is honest but closed: there is no public developer portal, no self-serve signup, no OpenAPI or WSDL and no consumer API. The WestJet Direct Connect API is documented only as a public capability matrix at westjetndc.com, and access requires an IATA or ARC accreditation number (TIDS is explicitly
  not supported), a business-type and sales-volume qualification form, and WestJet approval. Agency booking through WestJet Agent Direct likewise requires an IATA/TIDS/ARC number and a five-to-ten business day review. There is no bulk export for agency or booking data; guest data comes out only via a verbally authenticated PIPEDA-style "Guest information report" request.'
image: https://www.westjet.com/favicon.ico
layout: provider
modified: '2026-07-28'
name: WestJet
nav: Providers
network: true
overview: 'WestJet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Aviation, Airline, and Distribution.


  The WestJet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WestJet''s developer surface includes getting-started guide, changelog, engineering blog, developer portal, documentation, signup flow, support, and 25 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 40.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 34.8
    discoverability: 77.8
    governance: 3.1
    operational_transparency: 44.7
  provenance:
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: domain-security
  name: Westjet Domain Security
  slug: westjet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: westjet
tags:
- Travel
- Canada
- Aviation
- Airline
- Distribution
- NDC
- Booking
- Cargo
- Loyalty
website: https://www.westjet.com/
---
