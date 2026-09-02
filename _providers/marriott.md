---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Marriott Agentic Access
  operation_count: 13
  slug: marriott-agentic-access
  summary_line: 13 operations · 11 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Actuator API from Marriott International — 1 operation(s) for actuator.
  name: Marriott International Actuator API
  slug: marriott-actuator-api
- description: Authorization related endpoints.
  name: Marriott International Auth API
  slug: marriott-auth-api
- description: The Data API from Marriott International — 1 operation(s) for data.
  name: Marriott International Data API
  slug: marriott-data-api
- description: The Data Collection Event API from Marriott International — 1 operation(s) for data collection event.
  name: Marriott International Data Collection Event API
  slug: marriott-data-collection-event-api
- description: The FreedomPay Freeway Service API from Marriott International — 1 operation(s) for freedompay freeway service.
  name: Marriott International FreedomPay Freeway Service API
  slug: marriott-freedompay-freeway-service-api
- description: Validates a given RN/LN against a property in cloud PMS.
  name: Marriott International Guest Validation API
  slug: marriott-guest-validation-api
- description: Updates the user internet plan purchase in cloud PMS.
  name: Marriott International Internet Purchase Update API
  slug: marriott-internet-purchase-update-api
- description: Provides the landing page URL based on request inputs.
  name: Marriott International Landing Page API
  slug: marriott-landing-page-api
- description: The Loyalty API from Marriott International — 1 operation(s) for loyalty.
  name: Marriott International Loyalty API
  slug: marriott-loyalty-api
- description: The PostPreviewSubmit API from Marriott International — 1 operation(s) for postpreviewsubmit.
  name: Marriott International Post Preview Submit API
  slug: marriott-postpreviewsubmit-api
- description: The RetrieveConfigsMonitoredByConfigWatcher API from Marriott International — 1 operation(s) for retrieveconfigsmonitoredbyconfigwatcher.
  name: Marriott International Retrieve Configs Monitored By Config Watcher API
  slug: marriott-retrieveconfigsmonitoredbyconfigwatcher-api
- description: The Status API from Marriott International — 1 operation(s) for status.
  name: Marriott International Status API
  slug: marriott-status-api
artifact_total: 23
collections:
- collection_type: open
  name: commerce-payment-processor
  slug: open-marriott-commerce-payment-processor-api
- collection_type: open
  name: Data Collection API
  slug: open-marriott-data-collection-api
- collection_type: open
  name: Finance Status Notifier Application
  slug: open-marriott-finance-status-notifier-api
- collection_type: open
  name: Hotel Operations ARA - Preview Submit API
  slug: open-marriott-hotel-operations-ara-api
- collection_type: open
  name: Merge/Transfer Request API - new TIP MMF Spec for sending Account Merge request to SF CLM
  slug: open-marriott-loyalty-account-merge-api
- collection_type: open
  name: TIP Internet Portal
  slug: open-marriott-tip-internet-portal-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/marriott-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/marriott-tip-internet-portal-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marriott-loyalty-account-merge-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marriott-data-collection-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marriott-commerce-payment-processor-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marriott-finance-status-notifier-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/marriott-hotel-operations-ara-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marriott-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/marriott-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/marriott?type=team&view_policy=true
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marriott-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/marriott-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marriott-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marriott-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/marriott-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/marriott-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marriott-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marriott-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marriott-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marriott-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/marriott-packages.yml
- group: agent
  title: ''
  type: MCPAssessment
  url: mcp/marriott-mcp.yml
- group: other
  title: ''
  type: MockServer
  url: sandbox/marriott-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marriott-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.marriott.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportalprod.marriott.com/
- group: start
  title: ''
  type: TravelAgentPortal
  url: https://www.travelagents.marriott.com/
- group: build
  title: ''
  type: GDSChainCodes
  url: https://www.travelagents.marriott.com/travelagents/GDSResInfo.mi
- group: company
  title: ''
  type: ConnectivityPartners
  url: https://homes-and-villas.marriott.com/en/connectivity-partners
- group: start
  title: ''
  type: PartnerOnboarding
  url: https://partners.homes-and-villas.marriott.com/s/connectivity-partner-contact-us
- group: operate
  title: ''
  type: Support
  url: https://help.marriott.com/
- group: company
  title: ''
  type: Blog
  url: https://news.marriott.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.travelagents.marriott.com/travelagents/createAccount.mi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marriott.com/en-us/about/terms-of-use.mi
- group: commercial
  title: ''
  type: LoyaltyProgramTerms
  url: https://www.marriott.com/loyalty/terms/default.mi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marriott.com/about/us-consumer.mi
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.marriott.com/.well-known/security.txt
- group: auth
  title: ''
  type: BugBounty
  url: https://hackerone.com/marriott
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marriott-international
created: '2026-07-28'
description: 'Marriott International is the world''s largest hotel group by room count, headquartered in Bethesda, Maryland, United States, operating and franchising roughly thirty brands from The Ritz-Carlton, St. Regis and W through Marriott Hotels, Sheraton, Westin and Courtyard down to Fairfield, Moxy and StudioRes, plus the Homes & Villas by Marriott Bonvoy home-rental marketplace and the Marriott Bonvoy loyalty program. It sits on the supply side of the travel distribution chain: it publishes rates and availability into every major global distribution system — Marriott''s own travel-agent site states it "participates in the following GDS: Amadeus, Sabre, Travelport (Apollo/Galileo, and Worldspan)" — sells through the OTAs, connects short-term-rental supply through a channel-connectivity partner program, and spends heavily to pull demand back to direct booking on Marriott.com and the Bonvoy app. Its API posture is closed. A Broadcom Layer7 developer portal exists at devportalprod.marriott.com
  and returns HTTP 200, but its anonymous API catalog is literally empty and the portal''s own home content returns HTTP 401 — there is no self-serve signup, no public API reference, no published rates/availability/booking API, no sandbox, no SDK, no changelog and no exit path. The only Marriott OpenAPI documents that can be read without a contract are eight internal and partner-facing specifications left publicly readable on SwaggerHub under the "marriott-api" owner; six are mirrored here verbatim as evidence. Everything a developer would actually want is behind a partner relationship, a travel-agent registration, or a GDS or channel-manager contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marriott-international.png
layout: provider
modified: '2026-07-28'
name: Marriott International
nav: Providers
network: true
overview: 'Marriott International publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Actuator API, Auth API, Data API, and 9 more. Tagged areas include Travel, United States, Hospitality, Hotels, and Booking.


  Marriott International''s developer surface includes authentication, support, engineering blog, signup flow, and 36 more developer resources.'
random_paper: 0
scopes:
- name: Marriott Scopes
  scope_count: 2
  slug: marriott-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 35.1
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marriott/refs/heads/main/screenshots/marriott-2026-08-07T172102.png
security:
- kind: authentication
  name: Marriott Authentication
  slug: marriott-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Marriott Domain Security
  slug: marriott-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Marriott Vulnerability Disclosure
  slug: marriott-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: marriott
tags:
- Travel
- United States
- Hospitality
- Hotels
- Booking
- Distribution
- Loyalty
- Short-Term Rental
- Corporate Travel
website: https://www.marriott.com/
---
