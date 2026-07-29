---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 264
  human_in_the_loop: 6
  name: Verifiable Agentic Access
  operation_count: 519
  slug: verifiable-agentic-access
  summary_line: 519 operations · 264 acting · 6 human-in-the-loop
api_count: 33
apis:
- description: Endpoints to list and dismiss active alerts. Alerts are triggered when an important event occurs that warrants user involvement. An alert can be considered dismissed if it has a dismissal timestamp an
  name: Verifiable Alerts API
  slug: verifiable-alerts-api
- description: Each API call that results in data being created, updated or deleted will result in one or more entries in the audit log. Using the endpoints provided in this section it is possible to list entries in
  name: Verifiable Audit API
  slug: verifiable-audit-api
- description: These endpoint allow you to create and manage access tokens to be used in API calls. Unlike most other endpoints, when creating an access token, these do not require an access token to be used. Instea
  name: Verifiable Authentication API
  slug: verifiable-authentication-api
- description: These endpoints allow you to add board certifications to a provider and perform certification lookups. Please note that a lookup may take some time depending on the load and performance of the externa
  name: Verifiable BoardCertifications API
  slug: verifiable-boardcertifications-api
- description: The CognitoFormsWebhook API from Verifiable — 1 operation(s) for cognitoformswebhook.
  name: Verifiable CognitoFormsWebhook API
  slug: verifiable-cognitoformswebhook-api
- description: The CreateOAuthCredentialsClientSecret API from Verifiable — 1 operation(s) for createoauthcredentialsclientsecret.
  name: Verifiable CreateOAuthCredentialsClientSecret API
  slug: verifiable-createoauthcredentialsclientsecret-api
- description: These endpoints allow you to create and get credentialing requests. A credentialing request is a workflow that supports the creation of a credentialing packet. You can create a request for Verifiable'
  name: Verifiable CredentialingRequests API
  slug: verifiable-credentialingrequests-api
- description: Endpoints related to scanning datasets and reading resulting matches. The supported datasets will grow over time and can be discovered via the [ListDatasets](/references/api/datasets/listdatasets) end
  name: Verifiable Datasets API
  slug: verifiable-datasets-api
- description: These endpoints allow you to add DEA registration numbers to a provider and perform DEA registration lookups. Unlike license verifications a DEA registration lookup is done immediately.
  name: Verifiable DEA API
  slug: verifiable-dea-api
- description: Definitions for static data
  name: Verifiable Definitions API
  slug: verifiable-definitions-api
- description: The DeleteOAuthCredentialsClientSecret API from Verifiable — 1 operation(s) for deleteoauthcredentialsclientsecret.
  name: Verifiable DeleteOAuthCredentialsClientSecret API
  slug: verifiable-deleteoauthcredentialsclientsecret-api
- description: Endpoints related to managing and retrieving Facility data. These APIs allow you to create, update, and retrieve facilities and their associated metadata. Each facility record includes key identifiers
  name: Verifiable Facilities API
  slug: verifiable-facilities-api
- description: Endpoints related to managing and retrieving detailed Facility Info. These APIs allow you to manage key information associated with a facility, including NPI numbers, DEA registrations, liability insu
  name: Verifiable FacilitiesInfo API
  slug: verifiable-facilitiesinfo-api
- description: 'Endpoints related to managing and retrieving Facility Specialties. These APIs allow you to associate specialties with a specific facility, retrieve a list of assigned specialties, view details for an '
  name: Verifiable FacilitiesSpecialties API
  slug: verifiable-facilitiesspecialties-api
- description: Endpoints for binary file access. When any of the other APIs return file paths, these file paths are referring to the `path` parameter in the following API's. File paths are unique per organization, b
  name: Verifiable Files API
  slug: verifiable-files-api
- description: Endpoints related to managing and listing groups. Providers and payers can be associated with groups.
  name: Verifiable Groups API
  slug: verifiable-groups-api
- description: These endpoints are used for our integrations with 3rd party services. They are not intended to be consumed directly by most clients. Please contact us for more information on our integration possibil
  name: Verifiable Integrations API
  slug: verifiable-integrations-api
- description: These endpoints allow you to add licenses to a provider and perform license lookups. Please note that a license lookup may take some time depending on the load and performance of the external data sou
  name: Verifiable Licenses API
  slug: verifiable-licenses-api
- description: The ListOAuthCredentials API from Verifiable — 1 operation(s) for listoauthcredentials.
  name: Verifiable ListOAuthCredentials API
  slug: verifiable-listoauthcredentials-api
- description: 'Endpoints to allow you to enable/disable monitoring or update monitoring settings for monitorable data. ## License Expiration Monitoring License Expiration Monitoring is a process that automatically p'
  name: Verifiable Monitoring API
  slug: verifiable-monitoring-api
- description: These endpoints allow you to create and manage provider notes.
  name: Verifiable Notes API
  slug: verifiable-notes-api
- description: Endpoints related to managing and listing payer plans.
  name: Verifiable PayerPlans API
  slug: verifiable-payerplans-api
- description: Endpoints related to managing and listing payers. Each payer can have zero or more payer plans.
  name: Verifiable Payers API
  slug: verifiable-payers-api
- description: Endpoints related to managing and listing provider enrollments. Providers in a group can be associated to payer plans via provider enrollments.
  name: Verifiable ProviderEnrollments API
  slug: verifiable-providerenrollments-api
- description: 'These endpoints let you import a provider’s profile data from different sources (such as a provider’s National Provider Identifier (NPI) record). This allows you to build a more complete picture of a '
  name: Verifiable ProviderProfiles API
  slug: verifiable-providerprofiles-api
- description: Endpoints related to managing and listing providers. A provider must be created and associated with license numbers, NPI numbers or other identifiers that can be used to perform lookups to fetch assoc
  name: Verifiable Providers API
  slug: verifiable-providers-api
- description: 'Endpoints related to managing and listing providers'' info. Education, insurance, training and CAQH login info can be added to providers. Education, liability insurance, and training can have multiple '
  name: Verifiable ProvidersInfo API
  slug: verifiable-providersinfo-api
- description: The Reports API from Verifiable — 4 operation(s) for reports.
  name: Verifiable Reports API
  slug: verifiable-reports-api
- description: The SsoAdminPortal API from Verifiable — 1 operation(s) for ssoadminportal.
  name: Verifiable SsoAdminPortal API
  slug: verifiable-ssoadminportal-api
- description: The SsoAuth API from Verifiable — 1 operation(s) for ssoauth.
  name: Verifiable SsoAuth API
  slug: verifiable-ssoauth-api
- description: Endpoints related to managing and listing users.
  name: Verifiable Users API
  slug: verifiable-users-api
- description: Endpoints to allow you to create and manage webhooks that will be called when a special event occurs. On this special event Verifiable will attempt to make an HTTP POST to the URL specified in the web
  name: Verifiable Webhooks API
  slug: verifiable-webhooks-api
- description: The WorkOsWebhook API from Verifiable — 1 operation(s) for workoswebhook.
  name: Verifiable WorkOsWebhook API
  slug: verifiable-workoswebhook-api
artifact_total: 39
asyncapis:
- description: ''
  name: Verifiable Webhooks
  slug: verifiable-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://verifiable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.discovery.verifiable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.discovery.verifiable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.discovery.verifiable.com/references/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.discovery.verifiable.com/references/api/section/getting-started
- group: company
  title: ''
  type: Blog
  url: https://verifiable.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.verifiable.com
- group: operate
  title: ''
  type: Support
  url: https://verifiable.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verifiable.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verifiable.com/legal/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://verifiable.com/legal/security
- group: auth
  title: ''
  type: Security
  url: https://verifiable.com/legal/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/verifiable-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verifiable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verifiable-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/verifiable-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verifiable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verifiable-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verifiable-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/verifiable-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/verifiable-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verifiable-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verifiable-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/verifiable-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verifiable-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/verifiable-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verifiable-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verifiable-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/verifiable-openapi-overlay.yaml
created: '2026-07-17'
description: Verifiable is an API-first provider network management and credentialing platform for healthcare. Its RESTful API lets health plans, credentialing vendors, and digital health companies programmatically manage provider and facility records, run real-time primary-source verifications of licenses and credentials, continuously monitor providers for sanctions and exclusions, scan reference datasets, manage payers, payer plans, groups, and provider enrollments, drive credentialing requests, and receive events via webhooks. The platform is built API-first (Verifiable builds its own product on the same API) and is used as underlying credentialing infrastructure across healthcare. Backed by Craft Ventures.
image: https://cdn.prod.website-files.com/5f274600ac3de0cf25b08be9/699f3ecc7486361f3611e7f8_Homepage.jpg
layout: provider
mcp_servers:
- description: ''
  name: verifiable-mcp.yml
  slug: verifiable-mcpyml
modified: '2026-07-21'
name: Verifiable
nav: Providers
network: true
overview: 'Verifiable publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Audit API, Authentication API, and 30 more. Tagged areas include Company, Health, Healthcare, Credentialing, and Provider Data.


  The Verifiable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Verifiable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 23 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 51.4
  delta: -3.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.0
    developer_ergonomics: 69.0
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 57.9
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Verifiable Authentication
  slug: verifiable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Verifiable Domain Security
  slug: verifiable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Verifiable Vulnerability Disclosure
  slug: verifiable-vulnerability-disclosure
  summary_line: disclosure policy published
slug: verifiable
tags:
- Company
- Health
- Healthcare
- Credentialing
- Provider Data
- Primary Source Verification
- Compliance
- Monitoring
- API
website: https://verifiable.com
---
