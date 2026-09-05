---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/menlo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.menlosecurity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.menlosecurity.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.menlosecurity.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://csportal.menlosecurity.com/hc/en-us
- group: auth
  title: ''
  type: TrustCenter
  url: security/menlo-trust-center.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.menlosecurity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.menlosecurity.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/menlo-llms.txt
created: '2026-07-17'
description: Menlo Security is a cybersecurity company that secures the enterprise browser, positioning the browser as the point of control for protecting both human users and AI agents. Its cloud-native Secure Enterprise Browser and Menlo Cloud Security Platform apply remote browser isolation to prevent zero-day phishing, ransomware, and malware from ever reaching the endpoint. The platform spans AI agent security and governance, AI Adaptive DLP (data loss prevention), file security for downloads and uploads, zero-trust remote access to private applications, and threat prevention. Menlo Security is headquartered in Mountain View, California and is backed by investors including General Catalyst, Vista Equity Partners, JPMorgan, American Express Ventures, and HSBC. Menlo does not publish a public developer API or OpenAPI surface; administration is handled through its cloud console and a customer support portal.
image: https://www.menlosecurity.com/hubfs/menlo-security-logo.svg
layout: provider
modified: '2026-07-20'
name: Menlo Security
nav: Providers
network: true
overview: 'Menlo Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Browser Security, and Enterprise Browser.


  Menlo Security''s developer surface includes engineering blog, pricing, support, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/menlo/refs/heads/main/screenshots/menlo-2026-08-07T172521.png
security:
- kind: domain-security
  name: Menlo Domain Security
  slug: menlo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Menlo Trust Center
  slug: menlo-trust-center
  summary_line: trust center published
slug: menlo
tags:
- Company
- Security
- Cybersecurity
- Browser Security
- Enterprise Browser
- Browser Isolation
- Zero Trust
- Data Loss Prevention
- AI Agent Security
- Threat Prevention
website: https://www.menlosecurity.com/
---
