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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eye-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eye.security/responsible-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eye-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eye.security/
- group: start
  title: ''
  type: Portal
  url: https://portal.eye.security/
- group: start
  title: ''
  type: Login
  url: https://portal.eye.security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eye.security/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.eye.security/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eye.security/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.eye.security/contact
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.eye.security/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eye-security-well-known.yml
created: '2026-07-17'
description: Eye Security is a European cybersecurity company providing managed detection and response (MDR) and managed XDR for mid-market organizations across logistics, manufacturing, healthcare, and professional services. It combines AI-driven threat detection with a 24/7 Security Operations Center (SOC), incident response and threat hunting, security awareness training, EU-native log retention, and integrated cyber insurance. Headquartered in Europe with an EU-focused stance on compliance and data residency, Eye positions itself as enterprise-grade security made for the mid-market. This API Evangelist profile tracks the company's public developer, security, and product surface.
image: https://www.eye.security/favicon.ico
layout: provider
modified: '2026-07-19'
name: Eye Security
nav: Providers
network: true
overview: 'Eye Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Managed Detection and Response, Managed XDR, and Security Operations Center.


  Eye Security''s developer surface includes developer portal, pricing, engineering blog, support, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eye-security/refs/heads/main/screenshots/eye-security-2026-07-25T214209.png
security:
- kind: domain-security
  name: Eye Security Domain Security
  slug: eye-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eye Security Vulnerability Disclosure
  slug: eye-security-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: eye-security
tags:
- Company
- Cybersecurity
- Managed Detection and Response
- Managed XDR
- Security Operations Center
- Incident Response
- Cyber Insurance
- Threat Hunting
- Europe
website: https://www.eye.security/
---
