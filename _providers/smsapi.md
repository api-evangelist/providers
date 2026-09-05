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
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Smsapi Agentic Access
  operation_count: 31
  slug: smsapi-agentic-access
  summary_line: 31 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The 2FA API from SMSAPI — 2 operation(s) for 2fa.
  name: SMSAPI 2FA API
  slug: smsapi-2fa-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The Blacklist API from SMSAPI — 2 operation(s) for blacklist.
  name: SMSAPI Blacklist API
  slug: smsapi-blacklist-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The Contacts API from SMSAPI — 4 operation(s) for contacts.
  name: SMSAPI Contacts API
  slug: smsapi-contacts-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The HLR API from SMSAPI — 1 operation(s) for hlr.
  name: SMSAPI HLR API
  slug: smsapi-hlr-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The MMS API from SMSAPI — 1 operation(s) for mms.
  name: SMSAPI MMS API
  slug: smsapi-mms-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The Profile API from SMSAPI — 1 operation(s) for profile.
  name: SMSAPI Profile API
  slug: smsapi-profile-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The Sender Names API from SMSAPI — 3 operation(s) for sender names.
  name: SMSAPI Sender Names API
  slug: smsapi-sender-names-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The Short URLs API from SMSAPI — 1 operation(s) for short urls.
  name: SMSAPI Short URLs API
  slug: smsapi-short-urls-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The SMS API from SMSAPI — 1 operation(s) for sms.
  name: SMSAPI SMS API
  slug: smsapi-sms-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The Subusers API from SMSAPI — 2 operation(s) for subusers.
  name: SMSAPI Subusers API
  slug: smsapi-subusers-api
- baseURL: https://api.smsapi.com/sms.do
  baseurl_source: declared
  description: The VMS API from SMSAPI — 1 operation(s) for vms.
  name: SMSAPI VMS API
  slug: smsapi-vms-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SMSAPI REST 2FA API
  slug: open-smsapi-2fa-api
- collection_type: open
  name: SMSAPI REST 2FA Blacklist API
  slug: open-smsapi-blacklist-api
- collection_type: open
  name: SMSAPI REST 2FA Contacts API
  slug: open-smsapi-contacts-api
- collection_type: open
  name: SMSAPI REST 2FA HLR API
  slug: open-smsapi-hlr-api
- collection_type: open
  name: SMSAPI REST 2FA MMS API
  slug: open-smsapi-mms-api
- collection_type: open
  name: SMSAPI REST 2FA Profile API
  slug: open-smsapi-profile-api
- collection_type: open
  name: SMSAPI REST 2FA Sender Names API
  slug: open-smsapi-sender-names-api
- collection_type: open
  name: SMSAPI REST 2FA Short URLs API
  slug: open-smsapi-short-urls-api
- collection_type: open
  name: SMSAPI REST 2FA SMS API
  slug: open-smsapi-sms-api
- collection_type: open
  name: SMSAPI REST 2FA Subusers API
  slug: open-smsapi-subusers-api
- collection_type: open
  name: SMSAPI REST 2FA VMS API
  slug: open-smsapi-vms-api
- collection_type: open
  name: SMSAPI REST API
  slug: open-smsapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smsapi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smsapi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smsapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smsapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smsapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smsapi-com
- group: company
  title: ''
  type: Website
  url: https://www.smsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.smsapi.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/smsapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smsapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smsapi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.smsapi.com/blog/feed
created: '2026-07-01'
description: SMSAPI is a European bulk business-messaging provider headquartered in Poland and part of LINK Mobility. Its REST API delivers SMS, MMS, and voice (VMS) messaging, email marketing, two-factor authentication, contact and group management, sender field registration, subuser administration, and account/profile operations, authenticated with OAuth 2.0 bearer tokens over api.smsapi.com and api.smsapi.eu.
finops:
- name: Smsapi Finops
  service_category: Communications
  slug: smsapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smsapi.png
layout: provider
modified: '2026-07-01'
name: SMSAPI
nav: Providers
network: true
overview: 'SMSAPI publishes 11 APIs on the [APIs.io](https://apis.io/) network, including 2FA API, Blacklist API, Contacts API, and 8 more. Tagged areas include Messaging, SMS, MMS, Voice, and 2FA.


  SMSAPI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Smsapi Plans Pricing
  plan_count: 3
  slug: smsapi-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Smsapi Rate Limits
  slug: smsapi-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smsapi/refs/heads/main/screenshots/smsapi-2026-09-02T155955.png
security:
- kind: authentication
  name: Smsapi Authentication
  slug: smsapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smsapi Domain Security
  slug: smsapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Smsapi Trust Center
  slug: smsapi-trust-center
  summary_line: ISO 27001, GDPR
slug: smsapi
tags:
- Messaging
- SMS
- MMS
- Voice
- 2FA
- Bulk Messaging
- Communications
- CPaaS
website: https://www.smsapi.com/
---
