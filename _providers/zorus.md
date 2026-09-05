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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zorus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zorustech.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.zorustech.com/
- group: start
  title: ''
  type: Login
  url: https://portal.zorustech.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.zorustech.com/blog/
- group: operate
  title: ''
  type: Support
  url: mailto:support@zorustech.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zorustech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zorustech.com/terms-of-service/
created: '2026-07-17'
description: Zorus is a cybersecurity company that provides DNS web protection and filtering built for managed service providers (MSPs), managed security service providers (MSSPs), and IT teams. Its Archon agent delivers DNS filtering without requiring per-router DNS changes, layered with CyberSight behavioral user analytics, geo-IP and network filtering, zero-trust device isolation, and SaaS inventory and usage visibility. Zorus is delivered as a multi-tenant SaaS platform administered through a partner portal (portal.zorustech.com), positioned as an alternative to Cisco Umbrella, WebRoot DNS, and WebTitan. Zorus does not currently publish a public developer API, OpenAPI specification, SDKs, or developer documentation; its API surface (api.zorustech.com) sits behind the authenticated product portal. This profile captures the company's public web properties and probed security posture.
image: https://www.zorustech.com/wp-content/uploads/2024/03/zoom-bg.png
layout: provider
modified: '2026-07-21'
name: Zorus
nav: Providers
network: true
overview: 'Zorus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, DNS Filtering, Web Protection, and MSP.


  Zorus'' developer surface includes developer portal, engineering blog, support, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zorus/refs/heads/main/screenshots/zorus-2026-09-02T171842.png
security:
- kind: domain-security
  name: Zorus Domain Security
  slug: zorus-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: zorus
tags:
- Company
- Cybersecurity
- DNS Filtering
- Web Protection
- MSP
- MSSP
- Network Security
- Zero Trust
- Analytics
website: https://www.zorustech.com/
---
