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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
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
artifact_total: 28
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
- group: other
  href: https://artifacts.apis.io/kaleyra/capabilities/kaleyra-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kaleyra-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kaleyra/overview
- group: agent
  href: https://artifacts.apis.io/kaleyra/agentic-access/kaleyra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kaleyra-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kaleyra/security/kaleyra-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kaleyra-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kaleyra/security/kaleyra-trust-center.yml
  title: ''
  type: Compliance
  url: security/kaleyra-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kaleyra/security/kaleyra-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kaleyra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kaleyra.com/security/
- group: auth
  href: https://artifacts.apis.io/kaleyra/security/kaleyra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kaleyra-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kaleyra/authentication/kaleyra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kaleyra-authentication.yml
- group: design
  href: https://artifacts.apis.io/kaleyra/conformance/kaleyra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kaleyra-conformance.yml
- group: build
  href: https://artifacts.apis.io/kaleyra/packages/kaleyra-packages.yml
  title: ''
  type: Packages
  url: packages/kaleyra-packages.yml
- group: build
  href: https://artifacts.apis.io/kaleyra/packages/kaleyra-packages.yml
  title: ''
  type: SDKs
  url: packages/kaleyra-packages.yml
- group: agent
  href: https://artifacts.apis.io/kaleyra/well-known/kaleyra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kaleyra-well-known.yml
- group: agent
  href: https://artifacts.apis.io/kaleyra/mcp/kaleyra-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kaleyra-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kaleyra/llms/kaleyra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kaleyra-llms.txt
- group: other
  href: https://artifacts.apis.io/kaleyra/overlays/kaleyra-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kaleyra-overlay.yaml
- group: design
  href: https://artifacts.apis.io/kaleyra/errors/kaleyra-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/kaleyra-error-codes.yml
- group: design
  href: https://artifacts.apis.io/kaleyra/lifecycle/kaleyra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kaleyra-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kaleyra.io/
- group: design
  href: https://artifacts.apis.io/kaleyra/conventions/kaleyra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kaleyra-conventions.yml
- group: operate
  href: https://artifacts.apis.io/kaleyra/changelog/kaleyra-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kaleyra-changelog.yml
- group: design
  href: https://artifacts.apis.io/kaleyra/components/kaleyra-components.yml
  title: ''
  type: Components
  url: components/kaleyra-components.yml
- group: design
  href: https://artifacts.apis.io/kaleyra/data-model/kaleyra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kaleyra-data-model.yml
- group: design
  href: https://artifacts.apis.io/kaleyra/asyncapi/kaleyra-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/kaleyra-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/kaleyra/skills/_index.yml
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
  href: https://artifacts.apis.io/kaleyra/collections/kaleyra.postman_collection.json
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
  href: https://artifacts.apis.io/kaleyra/plans/kaleyra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kaleyra-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kaleyra/rate-limits/kaleyra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kaleyra-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kaleyra/finops/kaleyra-finops.yml
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
- has_sources: true
  method: generated
  name: Kaleyra Finops
  primary_unit: ''
  service_category: Communication and Messaging
  slug: kaleyra-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kaleyra.png
layout: provider
modified: '2026-07-17'
name: Kaleyra
nav: Providers
network: true
overview: 'Kaleyra publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Messages API, Verify API, Video API, and 3 more. Tagged areas include CPaaS, Messaging, SMS, WhatsApp, and Voice.


  The Kaleyra catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kaleyra''s developer surface includes authentication, changelog, getting-started guide, API reference, support, documentation, engineering blog, and 33 more developer resources.'
plans:
- name: Kaleyra Plans Pricing
  plan_count: 2
  slug: kaleyra-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Kaleyra Rate Limits
  slug: kaleyra-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Kaleyra API Rules
  rule_count: 66
  severity_counts:
    error: 63
    hint: 0
    info: 2
    warn: 1
  slug: kaleyra-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 56.7
    developer_ergonomics: 67.3
    discoverability: 73.2
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 45.0
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
    score: 23.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kaleyra/kaleyra-2026-07-25T223430.png
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
skill_count: 4
skills:
- name: Place a click-to-call bridged call
  slug: kaleyra-click-to-call
- name: Create a Kaleyra Video room
  slug: kaleyra-create-video-room
- name: Send an SMS and track delivery
  slug: kaleyra-send-sms
- name: Verify a user with an OTP
  slug: kaleyra-verify-otp
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
