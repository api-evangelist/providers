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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Calm Agentic Access
  operation_count: 3
  slug: calm-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://auth.calm.com
  baseurl_source: declared
  description: Obtain a JWT access token via OAuth 2.0 client credentials.
  name: Calm Authentication API
  slug: calm-authentication-api
- baseURL: https://auth.calm.com
  baseurl_source: declared
  description: Link and cancel partner-user Calm subscriptions.
  name: Calm Subscriptions API
  slug: calm-subscriptions-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Calm Partner Authentication API
  slug: open-calm-authentication-api
- collection_type: open
  name: Calm Partner API
  slug: open-calm-partner-api
- collection_type: open
  name: Calm Partner Authentication Subscriptions API
  slug: open-calm-subscriptions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/calm-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/calm-partner-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partner.calm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://partner.calm.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.calm.com/docs/api
- group: operate
  title: ''
  type: Support
  url: https://support.calm.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.calm.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calm.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://business.calm.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/calm-partner-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/calm-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/calm-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/calm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/calm-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/calm-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/calm-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/calm-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/calm-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/calm-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calm-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calm-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.calm.com
- group: start
  title: ''
  type: Portal
  url: https://www.calm.com
- group: start
  title: ''
  type: Signup
  url: https://www.calm.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.calm.com/subscribe
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/sso
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/sftp-instructions
- group: other
  title: ''
  type: Product
  url: https://business.calm.com
- group: other
  title: ''
  type: Product
  url: https://health.calm.com
- group: other
  title: ''
  type: Product
  url: https://app.calmhealth.com
- group: operate
  title: ''
  type: Support
  url: https://support.calm.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.calm.com/terms
- group: company
  title: ''
  type: Blog
  url: https://blog.calm.com
- group: company
  title: ''
  type: Press
  url: https://www.calm.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.calm.com/jobs
- group: operate
  title: ''
  type: Contact
  url: https://support.calm.com/hc/en-us/requests/new
- group: other
  title: ''
  type: AppStoreApple
  url: https://apps.apple.com/us/app/calm/id571800810
- group: other
  title: ''
  type: AppStoreGoogle
  url: https://play.google.com/store/apps/details?id=com.calm.android
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/calm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calm-com
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/calm
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/calm
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/calm.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/calm
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-domain-security.yml
- group: other
  title: ''
  type: CalmHealth
  url: https://health.calm.com
- group: commercial
  title: ''
  type: ForHealthPlans
  url: https://health.calm.com/health-plans
- group: other
  title: ''
  type: ForEmployers
  url: https://health.calm.com/employers
- group: other
  title: ''
  type: ForConsultants
  url: https://health.calm.com/consultants
- group: build
  title: ''
  type: ClinicalPrograms
  url: https://health.calm.com/clinical-programs
- group: other
  title: ''
  type: Gift
  url: https://www.calm.com/gift
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.calm.com
- group: company
  title: ''
  type: Blog
  url: https://www.calm.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.calm.com
- group: other
  title: ''
  type: Science
  url: https://www.calm.com/science
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calm.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://health.calm.com/trust
- group: company
  title: ''
  type: Careers
  url: https://www.calm.com/careers
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/calm/id571800810
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.calm.android
- group: company
  title: ''
  type: Twitter
  url: https://x.com/calm
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/calm
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/calm/
- group: operate
  title: ''
  type: Contact
  url: https://health.calm.com/contact
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calm-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-domain-security.yml
created: '2026-07-17'
description: 'Calm is a leading consumer mental-wellness company whose app offers guided meditations, Sleep Stories, breathing programs, mindfulness masterclasses, and soundscapes. Beyond the direct-to-consumer app, Calm sells two B2B products: Calm Business, which delivers the Calm experience to employers as an employee wellness benefit, and Calm Health, a clinical mental-health offering for health plans and large self-insured employers. Both are powered by the Calm Partner API, an OAuth 2.0 client-credentials REST surface that partner HR and benefits systems use to provision, link, and cancel Calm subscriptions for their members, alongside SAML 2.0 IdP-initiated SSO and SFTP eligibility-file uploads. Calm is a portfolio company of Lightspeed Venture Partners.'
examples:
- key_count: 2
  name: Calm Authorize Example
  slug: calm-authorize-example
- key_count: 2
  name: Calm Cancel User Example
  slug: calm-cancel-user-example
- key_count: 2
  name: Calm Link User Example
  slug: calm-link-user-example
features:
- Guided meditations across stress, anxiety, focus, and self-care libraries
- Sleep Stories — long-form bedtime audio narrated by well-known voices
- Daily Calm — a fresh 10-minute guided meditation every day
- Breathing exercises and breathwork programs
- Mindfulness and emotional-skill courses
- Calm Music — curated music for focus, relaxation, and sleep
- Calm Kids content library for children
- Soundscapes and nature audio
- Calm Business — employer-paid Calm benefit for employee wellness
- Calm Health — clinical mental health programs for health plans and self-insured employers
- Partner API with OAuth 2.0 client_credentials for subscription provisioning
- Partner SAML 2.0 IdP-initiated SSO with unique SubjectNameId
- SFTP eligibility file ingestion (CSV) at sftp.ws.calm.com:/inbound/eligibility/
- Partner Portal for administration, reporting, and segmentation
- iOS and Android apps plus a web experience at calm.com
- Available on Apple Watch, Apple TV, and Amazon Alexa
image: https://www.calm.com/favicon.ico
json_schemas:
- name: Calm Eligibility File Row
  property_count: 4
  slug: calm-eligibility-file
- name: Calm Partner User
  property_count: 9
  slug: calm-partner-user
jsonld:
- class_count: 16
  name: Calm Context
  property_count: 2
  slug: calm-context
layout: provider
mcp_servers:
- description: ''
  name: Calm MCP Server
  slug: calm-mcp-server
modified: '2026-07-18'
name: Calm
nav: Providers
network: true
overview: 'Calm publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Subscriptions API. Tagged areas include Company, Mental Health, Wellness, Meditation, and Mindfulness.


  The Calm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Calm''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, sandbox, and 68 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 5
  extends: []
  name: Calm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: calm-jsonschema-spectral-rules
scopes:
- name: Calm Scopes
  scope_count: 2
  slug: calm-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 66.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 14.4
    contract_quality: 61.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 14.4
    operational_transparency: 18.4
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calm/refs/heads/main/screenshots/calm-2026-07-25T204251.png
security:
- kind: authentication
  name: Calm Authentication
  slug: calm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Calm Domain Security
  slug: calm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calm
tags:
- Company
- Mental Health
- Wellness
- Meditation
- Mindfulness
- Sleep
- Employee Benefits
- Health
- B2B
- Subscription
website: https://www.calm.com
---
