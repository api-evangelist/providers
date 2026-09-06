---
access_model:
  confidence: medium
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Signeasy Agentic Access
  operation_count: 12
  slug: signeasy-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.signeasy.com/v3
  baseurl_source: declared
  description: Embedded signing and sending flows for iframes and pop-ups.
  name: Signeasy Embedded API
  slug: signeasy-embedded-api
- baseURL: https://api.signeasy.com/v3
  baseurl_source: declared
  description: Signature requests composed of originals and templates.
  name: Signeasy Envelopes API
  slug: signeasy-envelopes-api
- baseURL: https://api.signeasy.com/v3
  baseurl_source: declared
  description: Master documents used to build signature requests.
  name: Signeasy Originals API
  slug: signeasy-originals-api
- baseURL: https://api.signeasy.com/v3
  baseurl_source: declared
  description: Reusable documents with predefined roles and merge fields.
  name: Signeasy Templates API
  slug: signeasy-templates-api
- baseURL: https://api.signeasy.com/v3
  baseurl_source: declared
  description: Authenticated account details and envelope credits.
  name: Signeasy Users API
  slug: signeasy-users-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Signeasy Embedded API
  slug: open-signeasy-embedded-api
- collection_type: open
  name: Signeasy Embedded Envelopes API
  slug: open-signeasy-envelopes-api
- collection_type: open
  name: Signeasy Embedded Originals API
  slug: open-signeasy-originals-api
- collection_type: open
  name: Signeasy Embedded Templates API
  slug: open-signeasy-templates-api
- collection_type: open
  name: Signeasy Embedded Users API
  slug: open-signeasy-users-api
- collection_type: open
  name: Signeasy API v3
  slug: open-signeasy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signeasy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signeasy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signeasy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signeasy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signeasy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signeasy
- group: company
  title: ''
  type: Website
  url: https://signeasy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signeasy.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/signeasy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signeasy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/signeasy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://signeasy.com/blog/
created: '2026-07-03'
description: Signeasy is an eSignature and intelligent contract management platform used by tens of thousands of businesses to sign, send, and manage documents. The Signeasy API (v3) is a RESTful eSignature API that lets developers send documents for signature (envelopes), embed signing and sending flows directly inside their own web and mobile apps via iframes, manage reusable templates with merge fields, upload original documents, and receive real-time signature lifecycle notifications through webhooks. All endpoints are served from https://api.signeasy.com/v3 and authenticated with OAuth 2.0 Bearer access tokens (sandbox and live).
finops:
- name: Signeasy Finops
  service_category: Business Applications and eSignature
  slug: signeasy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signeasy.png
layout: provider
modified: '2026-07-03'
name: Signeasy
nav: Providers
network: true
overview: 'Signeasy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Embedded API, Envelopes API, Originals API, and 2 more. Tagged areas include E-Signature, Electronic Signature, Documents, Contract Management, and Embedded Signing.


  Signeasy''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Signeasy Plans Pricing
  plan_count: 4
  slug: signeasy-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Signeasy Rate Limits
  slug: signeasy-rate-limits
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signeasy/refs/heads/main/screenshots/signeasy-2026-09-02T155433.png
security:
- kind: authentication
  name: Signeasy Authentication
  slug: signeasy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Signeasy Domain Security
  slug: signeasy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Signeasy Trust Center
  slug: signeasy-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: signeasy
tags:
- E-Signature
- Electronic Signature
- Documents
- Contract Management
- Embedded Signing
- Templates
- Webhook
website: https://signeasy.com/
---
