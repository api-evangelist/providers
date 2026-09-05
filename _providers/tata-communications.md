---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tata Communications Agentic Access
  operation_count: 7
  slug: tata-communications-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 3
apis:
- description: Full-service API for the Tata Communications MOVE platform SIM Connect product, supporting management of a tenancy — its key entities, services, and the products the tenancy avails. Published on the s
  name: MOVE SIM Connect API
  slug: tata-communications-move-sim-connect-api
- description: Tata Communications MOVE platform IOT API, permitting management of a tenancy of the MOVE IOT Connect product including its key entities, services, and subscribed products. Published on the MOVE Azure
  name: MOVE IOT Connect API
  slug: tata-communications-move-iot-connect-api
- description: Issues an OAuth 2.0 bearer access token used to call the other Tata Communications MOVE APIs. Published on the MOVE Azure API Management developer portal; the reference is behind sign-in and no anonym
  name: MOVE Access Token API
  slug: tata-communications-move-access-token-api
- baseURL: https://move-external-apim-prod.azure-api.net
  baseurl_source: declared
  description: The CDR by Customer Message Id API from Tata Communications — 1 operation(s) for cdr by customer message id.
  name: Tata Communications CDR by Customer Message Id API
  slug: tata-communications-cdr-by-customer-message-id-api
- baseURL: https://move-external-apim-prod.azure-api.net
  baseurl_source: declared
  description: The Destination API from Tata Communications — 1 operation(s) for destination.
  name: Tata Communications Destination API
  slug: tata-communications-destination-api
- baseURL: https://move-external-apim-prod.azure-api.net
  baseurl_source: declared
  description: The Number Intelligence API from Tata Communications — 2 operation(s) for number intelligence.
  name: Tata Communications Number Intelligence API
  slug: tata-communications-number-intelligence-api
- baseURL: https://move-external-apim-prod.azure-api.net
  baseurl_source: declared
  description: The Report API from Tata Communications — 1 operation(s) for report.
  name: Tata Communications Report API
  slug: tata-communications-report-api
- baseURL: https://move-external-apim-prod.azure-api.net
  baseurl_source: declared
  description: The SenderId API from Tata Communications — 1 operation(s) for senderid.
  name: Tata Communications Sender ID API
  slug: tata-communications-senderid-api
- baseURL: https://move-external-apim-prod.azure-api.net
  baseurl_source: declared
  description: The TOP 25 CDR by account Id & Time Frame API from Tata Communications — 1 operation(s) for top 25 cdr by account id & time frame.
  name: Tata Communications TOP 25 CDR by account Id & Time Frame API
  slug: tata-communications-top-25-cdr-by-account-id-time-frame-api
artifact_total: 17
asyncapis:
- description: ''
  name: Tata Communications Webhooks
  slug: tata-communications-webhooks
collections:
- collection_type: open
  name: Mobile Messaging Exchange - Account Administration
  slug: open-tata-communications-mobile-messaging-exchange-account-administration
- collection_type: open
  name: Mobile Messaging Exchange - CDR Report API
  slug: open-tata-communications-mobile-messaging-exchange-cdr-report-api
- collection_type: open
  name: Number Intelligence API
  slug: open-tata-communications-number-intelligence-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tata-communications-number-intelligence-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tata-communications-mobile-messaging-exchange-account-administration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tata-communications-mobile-messaging-exchange-cdr-report-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tata-communications-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tata-communications-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tata-communications-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tata-communications-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tata-communications-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tata-communications-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/tata-communications-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tata-communications-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tata-communications-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tata-communications-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tatacommunications.com/cloud/cloud-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/tata-communications-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tata-communications-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/tata-communications-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tata-communications-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tata-communications-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tata-communications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tatacommunications.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tatacommunications.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tatacommunications.com/apis
- group: docs
  title: ''
  type: Documentation
  url: https://move-external-apim-prod.developer.azure-api.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tatacommunications.com/api-zone
- group: start
  title: ''
  type: SignUp
  url: https://move-external-apim-prod.developer.azure-api.net/signup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tata-communication
- group: company
  title: ''
  type: Blog
  url: https://www.tatacommunications.com/blog/
- group: start
  title: ''
  type: Portal
  url: https://www.developer.move.tatacommunications.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tatacommunications.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.tatacommunications.com/knowledge-base
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tatacommunications.com/cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tatacommunications.com/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tatacommunications.com/policies/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tatacommunications
- group: start
  title: ''
  type: Login
  url: https://developer.tatacommunications.com/login
created: '2026-07-25'
description: 'Tata Communications is the global wholesale carrier and digital-infrastructure arm of India''s Tata Group, headquartered in Mumbai. It owns one of the world''s largest subsea cable networks, carries a large share of global internet routes, and sells international voice and messaging wholesale, IZO network services, MOVE global IoT and eSIM connectivity, MVNE services, and — through its October 2023 acquisition of Kaleyra — a full CPaaS, UCaaS, and CCaaS stack. It sits in the supply layer of the telecom value chain: a carrier''s carrier whose customers are mostly other operators, enterprises, and aggregators rather than individual developers. Its API posture matches that position and is honestly partner-gated. Tata Communications runs a real first-party developer portal at developer.tatacommunications.com, built on Akana Community Manager, whose catalogue names 49 APIs — but only three are marked Public and return a downloadable Swagger 2.0 document to an anonymous caller; the
  other forty-six answer 401. MOVE IoT has a second, separate Azure API Management portal that lists three API products but gates the reference behind sign-in. The DIGO CPaaS documentation site is HTML-only, sales-gated behind a "we will get in touch" form, and was serving an expired TLS certificate at the time of review. No CAMARA network API and no GSMA Open Gateway participation could be evidenced anywhere on its properties. In practice most developers reach Tata Communications through the separately branded Kaleyra CPaaS portal rather than through Tata Communications itself.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Tata Communications
nav: Providers
network: true
overview: 'Tata Communications publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CDR by Customer Message Id API, Destination API, Number Intelligence API, and 3 more. Tagged areas include Telecommunications, India, Wholesale Carrier, CPaaS, and Messaging.


  The Tata Communications catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tata Communications'' developer surface includes authentication, code examples, sandbox, documentation, signup flow, engineering blog, developer portal, and 30 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 43.3
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tata-communications/refs/heads/main/screenshots/tata-communications-2026-08-17T082254.png
security:
- kind: authentication
  name: Tata Communications Authentication
  slug: tata-communications-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Tata Communications Domain Security
  slug: tata-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tata Communications Trust Center
  slug: tata-communications-trust-center
  summary_line: ISO/IEC 27001:2013, ISO/IEC 27017:2015, ISO/IEC 27018:2014, ISO/IEC 20000-1:2011, ISO/IEC 20000-9:2015, SOC1, SOC2, PCI DSS, HIPAA, GDPR, BDSG, CSA STAR, MTCS, MeitY, G-Cloud 10
slug: tata-communications
tags:
- Telecommunications
- India
- Wholesale Carrier
- CPaaS
- Messaging
- Voice
- IoT
- eSIM
- Number Intelligence
- Connectivity
- Subsea Cable
- Partner Gated
website: https://www.tatacommunications.com/
---
