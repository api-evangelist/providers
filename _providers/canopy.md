---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Collect consent to skip the consent page in the SDK
  name: Canopy Connect Consent API
  phrasing_intents:
  - id: post-consent
    intent: Record a user's consent to the terms
    question: How do I record that a user agreed to the Canopy Connect privacy policy and terms?
  - id: get-tos
    intent: Get the current terms of service
    question: Which terms of service version is current right now?
  phrasing_ops: 2
  slug: canopy-consent-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Allows you to look up driver/household data
  name: Canopy Connect Enrichment API
  phrasing_intents:
  - id: get-property-data
    intent: Look up property data for an address
    question: How can I get property details for a home address?
  - id: get-enrichment-driverlicense
    intent: Look up a person's driver's license
    question: How do I find someone's driver's license number from their name, birth date and address?
  - id: get-enrichment-drivingrecordiq
    intent: Get a person's driving record
    question: How can I check a driver's history of violations and incidents before quoting auto insurance?
  - id: get-enrichment-household
    intent: Look up a person's household members and vehicles
    question: How do I find the other drivers living in a person's household?
  phrasing_ops: 4
  slug: canopy-enrichment-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Collection of miscellaneous API routes
  name: Canopy Connect Misc API
  phrasing_intents:
  - id: get-health
    intent: Check the service health
    question: Is the Canopy Connect service up right now?
  phrasing_ops: 1
  slug: canopy-misc-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Manage synced accounts
  name: Canopy Connect Monitorings API
  phrasing_intents:
  - id: get-monitorings
    intent: List monitorings on insurance accounts
    question: Which insurance accounts am I currently monitoring for refreshes?
  - id: post-monitoring
    intent: Start monitoring an insurance account
    question: How do I set up recurring refreshes of a connected insurance account?
  - id: patch-monitoring
    intent: Change a monitoring's schedule or status
    question: How do I change how often an existing monitoring refreshes?
  - id: delete-monitoring
    intent: Stop a monitoring
    question: How do I stop refreshing a monitored insurance account?
  - id: get-monitoring
    intent: Get a monitoring and its pulls
    question: How do I see the details of one monitored insurance account?
  - id: get-monitoring-reconnect-token
    intent: Generate a reconnect token for a monitoring
    question: How do I get a token to send a consumer back to reconnect a monitored account?
  - id: post-monitoring-refresh
    intent: Refresh a monitored account now
    question: Can I refresh a monitored insurance account right away instead of waiting for the schedule?
  - id: get-monitoring-events
    intent: Get changes between a monitoring's last two pulls
    question: What changed on a monitored policy between its two most recent refreshes?
  phrasing_ops: 8
  slug: canopy-monitorings-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Manage Policy Check team setting
  name: Canopy Connect Policy Check Team Setting API
  phrasing_intents:
  - id: get-policy-check-team-settings
    intent: View the team's Policy Check settings
    question: Which Policy Checks are configured on my account?
  - id: post-policy-check-team-settings
    intent: Configure the team's Policy Checks
    question: How do I change which Policy Checks run on every submission?
  phrasing_ops: 2
  slug: canopy-policy-check-team-setting-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Used to get policy form data
  name: Canopy Connect Policy Forms API
  phrasing_intents:
  - id: get-policy-form-by-id
    intent: Download a policy form PDF (deprecated)
    question: Is there an older endpoint that streams a policy form PDF directly by form ID alone?
  - id: download-policy-form-by-id
    intent: Download a policy form via signed URL
    question: How do I download a policy form for my team as a short-lived signed link?
  phrasing_ops: 2
  slug: canopy-policy-forms-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Search verified Auto ID Cards, Auto insurance policies and Home insurance policies from major insurance carriers without the need for login credentials.
  name: Canopy Connect Policy Search API
  phrasing_intents:
  - id: post-policy-search
    intent: Search for a policy without credentials
    question: Can I find someone's auto or home insurance policy without their carrier login?
  phrasing_ops: 1
  slug: canopy-policy-search-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get Pull data and download documents
  name: Canopy Connect Pulls API
  phrasing_intents:
  - id: get-pull-by-id
    intent: Get all data for a pull
    question: How do I fetch everything collected from a consumer's insurance connection?
  - id: patch-pull-by-id
    intent: Archive or unarchive a pull
    question: How do I archive a pull I no longer need to see?
  - id: get-pulls
    intent: List a team's pulls
    question: Which insurance pulls has my team received recently?
  - id: get-document-by-id
    intent: Download a pull document PDF (deprecated)
    question: Is there a legacy PDF route for downloading a document from a pull?
  - id: download-document-by-id
    intent: Download a document from a pull
    question: How do I download an insurance document like a declarations page from a pull?
  - id: download-file-by-id
    intent: Download a file the consumer uploaded
    question: How can I get a file a consumer uploaded in answer to a question?
  - id: post-pull-policy-check
    intent: Run a Policy Check on a pull
    question: How do I evaluate a Policy Check against one specific pull?
  - id: get-pull-policy-check-pdf
    intent: Download a pull's Policy Check PDF
    question: Can I get the Policy Check results for a pull as a PDF report?
  phrasing_ops: 8
  slug: canopy-pulls-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Manage servicing actions
  name: Canopy Connect Servicings API
  phrasing_intents:
  - id: get-servicings
    intent: List servicing actions
    question: Which servicing actions has my team requested on insurance accounts?
  - id: post-servicings
    intent: Create servicing actions on an existing pull
    question: How do I request changes to a policy reusing the login and consent from an earlier pull?
  - id: get-servicing
    intent: Get a servicing action
    question: How do I check the status of one servicing action?
  phrasing_ops: 3
  slug: canopy-servicings-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get, create, delete Teams
  name: Canopy Connect Teams API
  phrasing_intents:
  - id: get-team
    intent: Get team details
    question: How do I see information about my current team?
  - id: delete-team
    intent: Deprovision a team
    question: How do I deprovision a team I no longer need?
  - id: create-team
    intent: Provision a new team
    question: How do I provision a new team for a company?
  phrasing_ops: 3
  slug: canopy-teams-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get, create, update and delete Webhooks
  name: Canopy Connect Webhooks API
  phrasing_intents:
  - id: get-webhooks
    intent: List webhooks
    question: Which webhooks are set up on my team?
  - id: post-webhooks
    intent: Create a webhook
    question: How do I get notified at my own URL when pulls change?
  - id: patch-webhook
    intent: Update a webhook
    question: Can I turn a webhook off temporarily without deleting it?
  - id: delete-webhook
    intent: Delete a webhook
    question: How do I remove a webhook I no longer use?
  phrasing_ops: 4
  slug: canopy-webhooks-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Allows you to create a fully whitelabeled experience
  name: Canopy Connect Whitelabel API
  phrasing_intents:
  - id: get-tos
    intent: Get the current terms of service
    question: Which terms version should my white-label consent screen show?
  - id: post-consent-and-connect
    intent: Record consent, create a pull and log in to a carrier
    question: How do I start a pull with my own UI by submitting consent and the user's carrier login?
  - id: post-consent-and-documents
    intent: Record consent, create a pull and upload documents
    question: Can a consumer upload their insurance documents instead of logging in to their carrier?
  - id: post-connect
    intent: Reauthenticate a pull with new credentials
    question: What do I do when a pull says it's not authenticated?
  - id: get-carriers
    intent: List supported insurance carriers
    question: Which insurance carriers can consumers connect to?
  - id: get-carrier
    intent: Get one supported carrier
    question: How do I look up the details of a single insurance carrier?
  - id: post-idv
    intent: Submit an MFA code for a pull
    question: How do I pass along the verification code a carrier texted the consumer?
  - id: post-idvoptions
    intent: Choose how to receive an MFA code
    question: Can the consumer pick whether the carrier sends the code by text or email?
  phrasing_ops: 10
  slug: canopy-whitelabel-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get, create, update, and delete Widgets
  name: Canopy Connect Widgets API
  phrasing_intents:
  - id: get-widgets
    intent: List widgets
    question: Which consumer-facing widgets has my team set up?
  - id: post-widgets
    intent: Create a widget
    question: How do I create a new branded widget for consumers to connect insurance?
  - id: get-widgetId
    intent: Get a widget
    question: How do I see the settings of one widget?
  - id: patch-widgetId
    intent: Edit an existing widget
    question: How do I change the intro title or success message on an existing widget?
  - id: delete-widgetId
    intent: Delete a widget
    question: How do I delete a widget I no longer use?
  - id: put-widgetId-logo
    intent: Upload a widget logo
    question: How do I upload my company logo to a widget?
  - id: put-widgetId-icon
    intent: Upload a widget icon
    question: How do I upload a small icon for a widget?
  phrasing_ops: 7
  slug: canopy-widgets-api-api
artifact_total: 27
asyncapis:
- description: ''
  name: Canopy Webhooks
  slug: canopy-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/canopy/rate-limits/canopy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canopy-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/canopy/capabilities/canopy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/canopy-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/canopy/overlays/canopy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canopy-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/canopy/packages/canopy-packages.yml
  title: ''
  type: Packages
  url: packages/canopy-packages.yml
- group: build
  href: https://artifacts.apis.io/canopy/packages/canopy-packages.yml
  title: ''
  type: SDKs
  url: packages/canopy-packages.yml
- group: design
  href: https://artifacts.apis.io/canopy/components/canopy-components.yml
  title: ''
  type: Components
  url: components/canopy-components.yml
- group: start
  href: https://artifacts.apis.io/canopy/sandbox/canopy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/canopy-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/canopy/mcp/canopy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canopy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/canopy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/canopy/llms/canopy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canopy-llms.txt
- group: agent
  href: https://artifacts.apis.io/canopy/well-known/canopy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canopy-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.usecanopy.com/.well-known/api-catalog
- group: commercial
  href: https://artifacts.apis.io/canopy/plans/canopy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canopy-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/canopy/finops/canopy-finops.yml
  title: ''
  type: FinOps
  url: finops/canopy-finops.yml
- group: auth
  href: https://artifacts.apis.io/canopy/security/canopy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canopy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usecanopy.com/security
- group: auth
  href: https://artifacts.apis.io/canopy/security/canopy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canopy-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usecanopy.com/company/is-canopy-connect-safe
- group: auth
  href: https://artifacts.apis.io/canopy/security/canopy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usecanopy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.usecanopy.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usecanopy.com/reference/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usecanopy.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usecanopy.com/reference/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.usecanopy.com/api/developer-account
- group: start
  title: ''
  type: Login
  url: https://dashboard.usecanopy.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usecanopy.com/api/api-plans
- group: operate
  title: ''
  type: Support
  url: https://help.usecanopy.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usecanopy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canopy-connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usecanopy.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usecanopy.com/terms
- group: company
  title: ''
  type: Blog
  url: https://www.usecanopy.com/blog
- group: company
  title: ''
  type: About
  url: https://www.usecanopy.com/company/about
- group: company
  title: ''
  type: Careers
  url: https://www.usecanopy.com/company/careers
created: '2024-07-02'
description: Canopy Connect is an insurance infrastructure platform that lets consumers and businesses quickly and securely share property and casualty insurance information through integrations with 400+ carriers covering 95%+ of the U.S. auto and homeowners markets. The API returns structured policy, driver, vehicle, claims, and property data in seconds, replacing manual verification workflows used across mortgage lending, auto finance, insurance carriers, and embedded insurance products.
finops:
- has_sources: true
  method: derived
  name: Canopy Finops
  primary_unit: ''
  service_category: ''
  slug: canopy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canopy.png
layout: provider
mcp_servers:
- description: 'Canopy Connect runs a hosted, remote MCP server on its documentation host. The docs platform advertises it in its own configuration (`mcp_server_card: true`, `webmcp: true`) and the endpoint answers a'
  name: Canopy Connect Documentation MCP Server
  slug: canopy-connect-documentation-mcp-server
modified: '2026-09-05'
name: Canopy Connect
nav: Providers
network: true
overview: 'Canopy Connect publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Consent API, Enrichment API, Misc API, and 10 more. Tagged areas include Auto Insurance, Casualty, Financial Services, Home Insurance, and Insurance.


  The Canopy Connect catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Canopy Connect''s developer surface includes sandbox, documentation, API reference, getting-started guide, signup flow, pricing, support, and 28 more developer resources.'
plans:
- name: Canopy Plans Pricing
  plan_count: 3
  slug: canopy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Canopy Rate Limits
  slug: canopy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Canopy Connect API Rules
  rule_count: 69
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 15
  slug: canopy-rules
scopes:
- name: Canopy Scopes
  scope_count: 12
  slug: canopy-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 65.5
    developer_ergonomics: 73.2
    discoverability: 85.0
    operational_transparency: 21.1
  previous_composite: 67.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 50.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/canopy/canopy-2026-06-20T173925.png
security:
- kind: authentication
  name: Canopy Authentication
  slug: canopy-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canopy Domain Security
  slug: canopy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Canopy Vulnerability Disclosure
  slug: canopy-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Canopy Trust Center
  slug: canopy-trust-center
  summary_line: SOC 2 Type 2
skill_count: 3
skills:
- name: canopy-collect-insurance-data
  slug: canopy-collect-insurance-data
- name: canopy-monitor-policy-changes
  slug: canopy-monitor-policy-changes
- name: canopy-run-policy-checks
  slug: canopy-run-policy-checks
slug: canopy
tags:
- Auto Insurance
- Casualty
- Financial Services
- Home Insurance
- Insurance
- Insurance Verification
- Property
website: https://www.usecanopy.com/
---
