---
access_model:
  confidence: medium
  label: Enterprise, contact sales
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://www.validity.com/pricing/
  - https://developer.everest.validity.com/
  - '{''url'': ''https://www.returnpath.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.validity.com/capabilities/engage-inbox-placement-and-deliverability/ — a different registrable domain (returnpath.com -> validity.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-05'
api_count: 11
apis:
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Account Services API from Return Path — 13 operation(s) for account services.
  name: Return Path Account Services API
  slug: return-path-account-services-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Apps & Integrations API from Return Path — 12 operation(s) for apps & integrations.
  name: Return Path Apps & Integrations API
  slug: return-path-apps-integrations-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Certification API from Return Path — 2 operation(s) for certification.
  name: Return Path Certification API
  slug: return-path-certification-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Competitive Intel API from Return Path — 7 operation(s) for competitive intel.
  name: Return Path Competitive Intel API
  slug: return-path-competitive-intel-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Engagement API from Return Path — 35 operation(s) for engagement.
  name: Return Path Engagement API
  slug: return-path-engagement-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Inbox Placement API from Return Path — 17 operation(s) for inbox placement.
  name: Return Path Inbox Placement API
  slug: return-path-inbox-placement-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Infrastructure (DMARC) API from Return Path — 10 operation(s) for infrastructure (dmarc).
  name: Return Path Infrastructure (DMARC) API
  slug: return-path-infrastructure-dmarc-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Legacy API (1.0) API from Return Path — 6 operation(s) for legacy api (1.0).
  name: Return Path Legacy API (1.0) API
  slug: return-path-legacy-api-1-0-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The List Validation API from Return Path — 6 operation(s) for list validation.
  name: Return Path List Validation API
  slug: return-path-list-validation-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The Reputation API from Return Path — 18 operation(s) for reputation.
  name: Return Path Reputation API
  slug: return-path-reputation-api
- baseURL: https://api.everest.validity.com/api
  baseurl_source: declared
  description: The View Time Optimization API from Return Path — 4 operation(s) for view time optimization.
  name: Return Path View Time Optimization API
  slug: return-path-view-time-optimization-api
artifact_total: 18
asyncapis:
- description: ''
  name: Return Path Webhooks
  slug: return-path-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/return-path-everest-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.returnpath.com/
- group: other
  title: ''
  type: Product
  url: https://www.validity.com/capabilities/engage-inbox-placement-and-deliverability/
- group: company
  title: ''
  type: Blog
  url: https://www.validity.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.validity.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.validity.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://mycommunity.validity.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.validity.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.validity.com/legal/terms-of-service/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.everest.validity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.everest.validity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.everest.validity.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/two50okay/workspace/everest-by-validity-s-public-workspace/overview
- group: start
  title: ''
  type: Login
  url: https://everest.validity.com/login
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.validity.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.validity.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.validity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/return-path-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/return-path-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/return-path-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/return-path-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/return-path-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/return-path-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/return-path-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/return-path-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/return-path-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/return-path-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/return-path-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/return-path-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/return-path-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/return-path-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/return-path-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/return-path-llms.txt
created: '2026-07-17'
description: Return Path is an email-deliverability and inbox-intelligence brand that pioneered sender reputation, inbox-placement monitoring, and email fraud protection for marketers and email senders. Founded in 1999 and backed by Sapphire Ventures and Union Square Ventures, Return Path was acquired by Validity in 2019 and now ships as the Validity Everest email-success platform; returnpath.com 301-redirects to validity.com. The platform draws on signals from billions of global mailboxes to measure inbox placement, sender reputation, and deliverability across major mailbox providers. The Return Path product line's surviving API surface is the Everest API at api.everest.validity.com — 170 published operations across inbox placement, sender reputation and Sender Score, blocklist and spam-trap monitoring, DMARC infrastructure reporting, engagement analytics, list validation and certification. Validity publishes no OpenAPI, but it does publish a complete public Postman collection at developer.everest.validity.com,
  which is the machine-readable contract this profile is built from.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/return-path.png
layout: provider
modified: '2026-08-13'
name: Return Path
nav: Providers
network: true
overview: 'Return Path publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account Services API, Apps & Integrations API, Certification API, and 8 more. Tagged areas include Company, MarTech, Email, Email Deliverability, and Email Marketing.


  The Return Path catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Return Path''s developer surface includes engineering blog, support, documentation, API reference, authentication, and 29 more developer resources.'
plans:
- name: Return Path Plans Pricing
  plan_count: 0
  slug: return-path-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Return Path Rate Limits
  slug: return-path-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 25.5
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 40.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/return-path/refs/heads/main/screenshots/return-path-2026-08-17T081538.png
security:
- kind: authentication
  name: Return Path Authentication
  slug: return-path-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Return Path Domain Security
  slug: return-path-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Return Path Vulnerability Disclosure
  slug: return-path-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Return Path Trust Center
  slug: return-path-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, GDPR, CCPA, EU-US Data Privacy Framework, Microsoft SSPA, Standard Contractual Clauses
slug: return-path
tags:
- Company
- MarTech
- Email
- Email Deliverability
- Email Marketing
- Sender Reputation
- Inbox Placement
- Deliverability
- DMARC
- Email Authentication
- Email Validation
- Analytics
website: https://www.returnpath.com/
---
