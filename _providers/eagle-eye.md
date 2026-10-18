---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eagleeye.com/legal/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://eagleeye.com/legal/security-compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/authentication/eagle-eye-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eagle-eye-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/llms/eagle-eye-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eagle-eye-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/well-known/eagle-eye-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eagle-eye-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/hosts/eagle-eye-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eagle-eye-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/vendors/eagle-eye-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eagle-eye-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eagleeye.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/security/eagle-eye-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/eagle-eye-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eagle-eye/refs/heads/main/security/eagle-eye-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eagle-eye-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eagleeye.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.eagleeye.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eagleeye.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.eagleeye.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://eagleeye.com/air-platform
- group: operate
  title: ''
  type: Support
  url: https://eessupport.zendesk.com/
- group: company
  title: ''
  type: Blog
  url: https://eagleeye.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eagleeye.com/legal/privacy-policy
coverage:
  checked: '2026-10-14'
  detail: Documentation pages require JavaScript rendering and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developer.eagleeye.com/eagleeye-developer/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Eagle Eye provides an AI‑driven loyalty and promotions platform that helps retailers, brands and e‑commerce businesses deliver real‑time, omnichannel loyalty experiences. Their suite includes the AIR Platform, real‑time loyalty, omnichannel promotions, gifting & top‑up, EagleAI and PromoBase, all designed for scale and integration with partners. The company emphasizes data‑driven insights, seamless API integration, and a developer portal for building custom loyalty solutions.
image: https://eagleeye.com/hubfs/eagle-eye-main-page-featured.jpg
layout: provider
modified: '2026-10-13'
name: Eagle Eye
nav: Providers
network: true
overview: 'Eagle Eye is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, Personalization, Promotions, Retail, and Artificial Intelligence.


  Eagle Eye''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 55.4
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eagle Eye Authentication
  slug: eagle-eye-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Eagle Eye Domain Security
  slug: eagle-eye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Eagle Eye Trust Center
  slug: eagle-eye-trust-center
  summary_line: SOC 2, GDPR
slug: eagle-eye
tags:
- Loyalty
- Personalization
- Promotions
- Retail
- Artificial Intelligence
- Omnichannel
- Gift Cards
website: https://eagleeye.com
---
