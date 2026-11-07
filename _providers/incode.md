---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Incode Agentic Access
  operation_count: 14
  slug: incode-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Validation against government databases.
  name: Incode Government Validation API
  slug: incode-government-validation-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Create and complete onboarding sessions.
  name: Incode Onboarding API
  slug: incode-onboarding-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Following endpoints facilitate API key rotation, for security reasons - current key gets stolen, user access needs to be revoked, organization expires, etc. It is good practice to rotate them every on
  name: Incode API Keys API
  slug: incode-api-keys-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: Standalone API validations that are not related to any interview or onboarding process. This helps with various identity verifications specific to certain countries such as CURP and INE in Mexico or S
  name: Incode API validations API
  slug: incode-api-validations-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Authentications API from Incode — 2 operation(s) for authentications.
  name: Incode Authentications API
  slug: incode-authentications-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Curp validation API from Incode — 4 operation(s) for curp validation.
  name: Incode Curp validation API
  slug: incode-curp-validation-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Custom fields API from Incode — 2 operation(s) for custom fields.
  name: Incode Custom fields API
  slug: incode-custom-fields-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Custom watchlist API from Incode — 5 operation(s) for custom watchlist.
  name: Incode Custom watchlist API
  slug: incode-custom-watchlist-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Document capture API from Incode — 6 operation(s) for document capture.
  name: Incode Document capture API
  slug: incode-document-capture-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Ekyb API from Incode — 4 operation(s) for ekyb.
  name: Incode Ekyb API
  slug: incode-ekyb-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Ekyc API from Incode — 4 operation(s) for ekyc.
  name: Incode Ekyc API
  slug: incode-ekyc-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Electronic signature advanced API from Incode — 1 operation(s) for electronic signature advanced.
  name: Incode Electronic signature advanced API
  slug: incode-electronic-signature-advanced-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Electronic signature API from Incode — 4 operation(s) for electronic signature.
  name: Incode Electronic signature API
  slug: incode-electronic-signature-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Email input API from Incode — 2 operation(s) for email input.
  name: Incode Email input API
  slug: incode-email-input-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Face capture API from Incode — 3 operation(s) for face capture.
  name: Incode Face capture API
  slug: incode-face-capture-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Fiscal qr url API from Incode — 3 operation(s) for fiscal qr url.
  name: Incode Fiscal qr url API
  slug: incode-fiscal-qr-url-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Forms and data entry API from Incode — 1 operation(s) for forms and data entry.
  name: Incode Forms and data entry API
  slug: incode-forms-and-data-entry-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Frame analysis API from Incode — 2 operation(s) for frame analysis.
  name: Incode Frame analysis API
  slug: incode-frame-analysis-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Geolocation API from Incode — 1 operation(s) for geolocation.
  name: Incode Geolocation API
  slug: incode-geolocation-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Global watchlist API from Incode — 3 operation(s) for global watchlist.
  name: Incode Global watchlist API
  slug: incode-global-watchlist-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Id capture API from Incode — 17 operation(s) for id capture.
  name: Incode Id capture API
  slug: incode-id-capture-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Identities API from Incode — 1 operation(s) for identities.
  name: Incode Identities API
  slug: incode-identities-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Identity reuse API from Incode — 2 operation(s) for identity reuse.
  name: Incode Identity reuse API
  slug: incode-identity-reuse-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Interview API from Incode — 38 operation(s) for interview.
  name: Incode Interview API
  slug: incode-interview-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Login API from Incode — 5 operation(s) for login.
  name: Incode Login API
  slug: incode-login-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Nom151 API from Incode — 4 operation(s) for nom151.
  name: Incode Nom151 API
  slug: incode-nom151-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Omni API from Incode — 4 operation(s) for omni.
  name: Incode Omni API
  slug: incode-omni-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Onboarding authentication API from Incode — 4 operation(s) for onboarding authentication.
  name: Incode Onboarding authentication API
  slug: incode-onboarding-authentication-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Organization API from Incode — 4 operation(s) for organization.
  name: Incode Organization API
  slug: incode-organization-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Phone number input API from Incode — 3 operation(s) for phone number input.
  name: Incode Phone number input API
  slug: incode-phone-number-input-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Proof of address capture API from Incode — 3 operation(s) for proof of address capture.
  name: Incode Proof of address capture API
  slug: incode-proof-of-address-capture-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Shared consent API from Incode — 2 operation(s) for shared consent.
  name: Incode Shared consent API
  slug: incode-shared-consent-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Trust graph API from Incode — 5 operation(s) for trust graph.
  name: Incode Trust graph API
  slug: incode-trust-graph-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The User consent API from Incode — 2 operation(s) for user consent.
  name: Incode User consent API
  slug: incode-user-consent-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Video conference API from Incode — 25 operation(s) for video conference.
  name: Incode Video conference API
  slug: incode-video-conference-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The Videoselfie API from Incode — 5 operation(s) for videoselfie.
  name: Incode Videoselfie API
  slug: incode-videoselfie-api
- baseURL: https://demo-api.incodesmile.com
  baseurl_source: declared
  description: The anti Fraud API from Incode — 1 operation(s) for anti fraud.
  name: Incode anti Fraud API
  slug: incode-anti-fraud-api
artifact_total: 52
collections:
- collection_type: open
  name: Incode Omni Face and Liveness API
  slug: open-incode-face-and-liveness-api
- collection_type: open
  name: Incode Omni Face and Liveness Government Validation API
  slug: open-incode-government-validation-api
- collection_type: open
  name: Incode Omni Face and Liveness ID Verification API
  slug: open-incode-id-verification-api
- collection_type: open
  name: Incode Omni Face and Liveness Onboarding API
  slug: open-incode-onboarding-api
- collection_type: open
  name: Incode Omni Face and Liveness Results API
  slug: open-incode-results-api
- collection_type: open
  name: Incode Omni Face and Liveness Watchlist and AML API
  slug: open-incode-watchlist-and-aml-api
- collection_type: open
  name: Incode Omni API
  slug: open-incode
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://incode.com/rss.xml
- group: agent
  href: https://artifacts.apis.io/incode/agentic-access/incode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/incode-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/incode/security/incode-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/incode-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/incode/security/incode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/incode-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/incode/authentication/incode-authentication.yml
  title: ''
  type: Authentication
  url: authentication/incode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Incode-Technologies-Example-Repos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/incodetech
- group: company
  title: ''
  type: Website
  url: https://incode.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.incode.com/docs
- group: commercial
  href: https://artifacts.apis.io/incode/plans/incode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/incode-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/incode/rate-limits/incode-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/incode-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/incode/finops/incode-finops.yml
  title: ''
  type: FinOps
  url: finops/incode-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://incode.com/blog
created: '2026-06-25'
description: Incode is an AI-powered identity verification and biometric authentication platform. The Incode Omni API runs configurable onboarding sessions that capture and validate government IDs, perform face match and passive liveness, run government-database and watchlist/AML checks, and return scores, OCR data, and images via REST.
finops:
- has_sources: true
  method: generated
  name: Incode Finops
  primary_unit: ''
  service_category: Identity and Compliance
  slug: incode-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/incode.png
layout: provider
modified: '2026-10-06'
name: Incode
nav: Providers
network: true
overview: 'Incode publishes 37 API contracts indexed on the [APIs.io](https://apis.io/) network, including Government Validation API, Onboarding API, API Keys API, and 34 more. Tagged areas include Identity Verification, Biometrics, KYC, Liveness, and Onboarding.


  The Incode catalog on APIs.io includes 1 Spectral governance ruleset.


  Incode''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Incode Plans Pricing
  plan_count: 2
  slug: incode-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Incode Rate Limits
  slug: incode-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Incode API Rules
  rule_count: 68
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 19
  slug: incode-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 57.6
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 84.1
      total: 44
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/incode/incode-2026-07-25T222333.png
security:
- kind: authentication
  name: Incode Authentication
  slug: incode-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Incode Domain Security
  slug: incode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Incode Trust Center
  slug: incode-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP
slug: incode
tags:
- Identity Verification
- Biometrics
- KYC
- Liveness
- Onboarding
website: https://incode.com
---
