---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.1
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Clearspeed Agentic Access
  operation_count: 4
  slug: clearspeed-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.us.clearspeed.com/questionnaire
  baseurl_source: declared
  description: The Default API from Clearspeed — 4 operation(s) for default.
  name: Clearspeed Default API
  slug: clearspeed-default-api
artifact_total: 10
asyncapis:
- description: ''
  name: Clearspeed Webhooks
  slug: clearspeed-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clearspeed Integration  API
  slug: open-clearspeed-default-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.clearspeed.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clearspeed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clearspeed.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clearspeed.com/apis/public/integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clearspeed.com/
- group: operate
  title: ''
  type: Support
  url: https://www.clearspeed.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.clearspeed.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.clearspeed.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearspeed.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearspeed.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.clearspeed.com/security-commitment
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/security/clearspeed-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clearspeed-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://compliance.clearspeed.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/security/clearspeed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearspeed-vulnerability-disclosure.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/openapi/_original/clearspeed-integration-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/clearspeed-integration-api-openapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/mcp/clearspeed-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clearspeed-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/mcp/clearspeed-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clearspeed-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/llms/clearspeed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearspeed-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/well-known/clearspeed-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearspeed-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/authentication/clearspeed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearspeed-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/conventions/clearspeed-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clearspeed-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/errors/clearspeed-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearspeed-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/data-model/clearspeed-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearspeed-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/examples/clearspeed-integration-api-examples.yml
  title: ''
  type: Examples
  url: examples/clearspeed-integration-api-examples.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/overlays/clearspeed-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clearspeed-integration-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/asyncapi/clearspeed-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/clearspeed-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/lifecycle/clearspeed-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clearspeed-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/conformance/clearspeed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearspeed-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/packages/clearspeed-packages.yml
  title: ''
  type: Packages
  url: packages/clearspeed-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/security/clearspeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearspeed-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/agentic-access/clearspeed-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clearspeed-agentic-access.yml
created: '2026-08-02'
description: Clearspeed is a voice-based risk assessment company whose AI analyzes involuntary vocal characteristics — tone, cadence, hesitation and stress — in a subject's spoken yes/no answers to produce an objective, language-independent risk indicator without requiring PII. Founded in 2016, it serves insurance claims and underwriting, government and defense vetting, financial services fraud and AML/KYC, plus hiring and vendor screening. Clearspeed exposes the Clearspeed Integration API, a REST contract on regional US and UK hosts that lets customers create participants against a questionnaire, track outcomes, and manage scoped API keys, with assessment results delivered back by webhook rather than polling.
image: https://www.clearspeed.com/opengraph.jpg
layout: provider
mcp_servers:
- description: ''
  name: Clearspeed Developer Portal MCP server
  slug: clearspeed-developer-portal-mcp-server
modified: '2026-08-04'
name: Clearspeed
nav: Providers
network: true
overview: 'Clearspeed publishes 1 API on the [APIs.io](https://apis.io/) network: Default API. Tagged areas include Company, Risk Assessment, Fraud Prevention, Voice Analytics, and Artificial Intelligence.


  The Clearspeed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clearspeed''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 64.5
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/clearspeed/refs/heads/main/screenshots/clearspeed-2026-08-07T163447.png
security:
- kind: authentication
  name: Clearspeed Authentication
  slug: clearspeed-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clearspeed Domain Security
  slug: clearspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearspeed Vulnerability Disclosure
  slug: clearspeed-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Clearspeed Trust Center
  slug: clearspeed-trust-center
  summary_line: SOC 2 Type 2, ISO 27001:2022, UK Cyber Essentials
slug: clearspeed
tags:
- Company
- Risk Assessment
- Fraud Prevention
- Voice Analytics
- Artificial Intelligence
- Insurance
- Identity Verification
- Screening
- Security
website: https://www.clearspeed.com/
---
