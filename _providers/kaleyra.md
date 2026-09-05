---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.kaleyra.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.tatacommunications.com/kaleyra — a different registrable domain (kaleyra.com -> tatacommunications.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Kaleyra Agentic Access
  operation_count: 7
  slug: kaleyra-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- description: Send single and batch transactional email (Email API v2) with domain management, templates, webhooks, and delivery statistics.
  name: Kaleyra Email API
  slug: kaleyra-email-api
- description: Account-level platform operations - subaccount management, billing, numbers provisioning, callback profiles, consent, and blocklist management.
  name: Kaleyra Platform API
  slug: kaleyra-platform-api
- baseURL: https://api.kaleyra.io
  baseurl_source: declared
  description: Send SMS, WhatsApp, and RCS messages and read their status.
  name: Kaleyra Messages API
  slug: kaleyra-messages-api
- baseURL: https://api.kaleyra.io
  baseurl_source: declared
  description: Generate and validate one-time passwords (OTP).
  name: Kaleyra Verify API
  slug: kaleyra-verify-api
- baseURL: https://api.kaleyra.io
  baseurl_source: declared
  description: Kaleyra Video (WebRTC) room orchestration via REST.
  name: Kaleyra Video API
  slug: kaleyra-video-api
- baseURL: https://api.kaleyra.io
  baseurl_source: declared
  description: Click-to-call and outbound voice.
  name: Kaleyra Voice API
  slug: kaleyra-voice-api
artifact_total: 24
asyncapis:
- description: ''
  name: Kaleyra Webhooks
  slug: kaleyra-webhooks
collections:
- collection_type: postman
  name: Kaleyra CPaaS Messages API
  slug: postman-kaleyra-messages-api
- collection_type: postman
  name: Kaleyra CPaaS Messages Verify API
  slug: postman-kaleyra-verify-api
- collection_type: postman
  name: Kaleyra CPaaS Messages Video API
  slug: postman-kaleyra-video-api
- collection_type: postman
  name: Kaleyra CPaaS Messages Voice API
  slug: postman-kaleyra-voice-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kaleyra CPaaS Messages API
  slug: open-kaleyra-messages-api
- collection_type: open
  name: Kaleyra CPaaS Messages Verify API
  slug: open-kaleyra-verify-api
- collection_type: open
  name: Kaleyra CPaaS Messages Video API
  slug: open-kaleyra-video-api
- collection_type: open
  name: Kaleyra CPaaS Messages Voice API
  slug: open-kaleyra-voice-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kaleyra/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kaleyra-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kaleyra-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/kaleyra-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kaleyra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kaleyra.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaleyra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kaleyra-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kaleyra-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kaleyra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kaleyra-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kaleyra-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kaleyra-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kaleyra-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kaleyra-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kaleyra-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kaleyra-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kaleyra.io/
- group: design
  title: ''
  type: Conventions
  url: conventions/kaleyra-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kaleyra-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/kaleyra-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kaleyra-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kaleyra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kaleyra.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.kaleyra.io/docs/kcloud-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kaleyra.io/reference/api-reference-overview
- group: operate
  title: ''
  type: Support
  url: https://support.kaleyra.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kaleyra
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kaleyra.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kaleyra.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: collections/kaleyra.postman_collection.json
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kaleyra
- group: company
  title: ''
  type: Website
  url: https://www.kaleyra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kaleyra.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/kaleyra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kaleyra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kaleyra-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kaleyra.com/blog/
created: '2026-07-17'
description: Kaleyra is a global omnichannel CPaaS provider (a Tata Communications company since October 2023) offering SMS, WhatsApp, RCS, Voice, Email, Verify (OTP), and Video communication APIs. Its REST APIs authenticate with an api-key header, address accounts by SID in the path, and are served from region-specific hosts for India, APAC, and EU data residency.
finops:
- name: Kaleyra Finops
  service_category: Communication and Messaging
  slug: kaleyra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kaleyra.png
layout: provider
modified: '2026-07-17'
name: Kaleyra
nav: Providers
network: true
overview: 'Kaleyra publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Messages API, Verify API, Video API, and 1 more. Tagged areas include CPaaS, Messaging, SMS, WhatsApp, and Voice.


  The Kaleyra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kaleyra''s developer surface includes authentication, changelog, getting-started guide, API reference, support, documentation, engineering blog, and 32 more developer resources.'
plans:
- name: Kaleyra Plans Pricing
  plan_count: 2
  slug: kaleyra-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Kaleyra Rate Limits
  slug: kaleyra-rate-limits
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 62.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaleyra/refs/heads/main/screenshots/kaleyra-2026-07-25T223430.png
security:
- kind: authentication
  name: Kaleyra Authentication
  slug: kaleyra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kaleyra Domain Security
  slug: kaleyra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kaleyra Vulnerability Disclosure
  slug: kaleyra-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kaleyra Trust Center
  slug: kaleyra-trust-center
  summary_line: ISO 27001, SOC 2, GDPR, HIPAA, PCI DSS
slug: kaleyra
tags:
- CPaaS
- Messaging
- SMS
- WhatsApp
- Voice
- OTP
- India
website: https://www.kaleyra.com/
---
