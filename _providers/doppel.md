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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The alerts API from Doppel — 3 operation(s) for alerts.
  name: Doppel alerts API
  slug: doppel-alerts-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The brands API from Doppel — 2 operation(s) for brands.
  name: Doppel brands API
  slug: doppel-brands-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The hrm API from Doppel — 3 operation(s) for hrm.
  name: Doppel hrm API
  slug: doppel-hrm-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The phishing-simulation API from Doppel — 1 operation(s) for phishing-simulation.
  name: Doppel phishing-simulation API
  slug: doppel-phishing-simulation-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The protected-assets API from Doppel — 3 operation(s) for protected-assets.
  name: Doppel protected-assets API
  slug: doppel-protected-assets-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The reports API from Doppel — 2 operation(s) for reports.
  name: Doppel reports API
  slug: doppel-reports-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The scan API from Doppel — 2 operation(s) for scan.
  name: Doppel scan API
  slug: doppel-scan-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The iocs API from Doppel — 0 operation(s) for iocs.
  name: Doppel Iocs API
  slug: doppel-iocs-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The reports (deprecated) API from Doppel — 0 operation(s) for reports (deprecated).
  name: Doppel reports (deprecated) API
  slug: doppel-reports-deprecated-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The sms_responses API from Doppel — 0 operation(s) for sms_responses.
  name: Doppel Sms Responses API
  slug: doppel-sms-responses-api
- baseURL: https://api.doppel.com/v1
  baseurl_source: declared
  description: The urls API from Doppel — 0 operation(s) for urls.
  name: Doppel URLS API
  slug: doppel-urls-api
artifact_total: 24
asyncapis:
- description: AsyncAPI derived from the Doppel V1 OpenAPI webhooks[] surface — the events Doppel POSTs to a subscriber endpoint for Brand Protection, IOC, and Human Risk Management activity. Payload schemas are the
  name: Doppel Webhooks
  slug: doppel-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Doppel alerts API
  slug: open-doppel-alerts-api
- collection_type: open
  name: Doppel alerts brands API
  slug: open-doppel-brands-api
- collection_type: open
  name: Doppel alerts hrm API
  slug: open-doppel-hrm-api
- collection_type: open
  name: Doppel alerts phishing-simulation API
  slug: open-doppel-phishing-simulation-api
- collection_type: open
  name: Doppel alerts protected-assets API
  slug: open-doppel-protected-assets-api
- collection_type: open
  name: Doppel alerts reports API
  slug: open-doppel-reports-api
- collection_type: open
  name: Doppel alerts scan API
  slug: open-doppel-scan-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.doppel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doppel.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://doppel.readme.io/docs/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://doppel.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://doppel.readme.io/docs/submit-alert
- group: auth
  title: ''
  type: Authentication
  url: authentication/doppel-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.doppel.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.doppel.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://doppel.instatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://doppel.readme.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/doppel-changelog.yml
- group: start
  title: ''
  type: Login
  url: https://vision.doppel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doppel.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doppel.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.doppel.com/security/responsible-disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/doppel-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.doppel.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doppel-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doppel-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doppel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/doppel-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doppel-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/doppel-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/doppel-openapi-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/doppel-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/doppel-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/doppel-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doppel-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doppel-vulnerability-disclosure.yml
created: '2026-07-17'
description: Doppel is an AI-native social engineering defense platform that protects brands, executives, and employees from AI-powered impersonation, phishing, fraud, and account takeover across domains, social media, ads, messaging apps, app stores, crypto surfaces, and the dark web. Its real-time Threat Graph correlates signals to detect and dismantle attacker infrastructure, unifying Digital Risk Protection, Human Risk Management, and Email Security. Doppel exposes a REST API (https://api.doppel.com/v1) for Brand Protection alerts, URL scanning, reports, protected assets, and phishing-simulation campaigns, plus webhooks for real-time events. Backed by a16z and Bessemer Venture Partners.
image: https://prod-cms.doppel.com/sites/default/files/2025-11/Open_Graph_Image_0.png
layout: provider
modified: '2026-07-18'
name: Doppel
nav: Providers
network: true
overview: 'Doppel publishes 11 APIs on the [APIs.io](https://apis.io/) network, including alerts API, brands API, hrm API, and 8 more. Tagged areas include Company, Security, Cybersecurity, Digital Risk Protection, and Social Engineering Defense.


  The Doppel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Doppel''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, changelog, and 23 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 43.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doppel/refs/heads/main/screenshots/doppel-2026-07-25T212309.png
security:
- kind: authentication
  name: Doppel Authentication
  slug: doppel-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Doppel Domain Security
  slug: doppel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doppel Vulnerability Disclosure
  slug: doppel-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Doppel Trust Center
  slug: doppel-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 42001:2023, ISO/IEC 27701, GDPR
slug: doppel
tags:
- Company
- Security
- Cybersecurity
- Digital Risk Protection
- Social Engineering Defense
- Brand Protection
- Anti-Phishing
- Threat Intelligence
- Human Risk Management
- Takedowns
website: https://www.doppel.com/
---
