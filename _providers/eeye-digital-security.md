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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.eye.security/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.eye.security/
- group: company
  title: ''
  type: Blog
  url: https://www.eye.security/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eye.security/pricing
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
  url: well-known/eeye-digital-security-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eeye-digital-security-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eeye-digital-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eye.security/responsible-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eeye-digital-security-domain-security.yml
created: '2026-07-17'
description: Eye Security is a European (Netherlands-founded) cybersecurity company delivering enterprise-grade Managed Detection and Response (Managed XDR), 24/7 incident response, security awareness training, EU-native log retention (Eye Log), and bundled cyber insurance to the mid-market. Rather than building its own detection stack, Eye Security combines the human expertise of European security analysts with vetted EDR/ITDR technologies, integrating with a customer's existing tech stack. Backed by Bessemer Venture Partners. This API Evangelist profile was seeded as a VC-portfolio stub under the mis-expanded legacy name "eEye Digital Security"; the wired domain (eye.security), HackerOne program, and Bessemer backing identify the live company as Eye Security. Eye Security operates internal control-plane APIs (api.control.eye.security, portal, agent) but publishes no public developer API, OpenAPI, or developer portal, so this profile carries identity and security posture artifacts rather
  than API specifications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eeye-digital-security.png
layout: provider
modified: '2026-07-19'
name: Eye Security
nav: Providers
network: true
overview: 'Eye Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Managed Detection and Response, Managed XDR, and Incident Response.


  Eye Security''s developer surface includes documentation, engineering blog, pricing, support, and 7 more developer resources.'
random_paper: 50
score:
  band: minimal
  composite: 3.7
  delta: -11.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/eeye-digital-security/refs/heads/main/screenshots/eeye-digital-security-2026-07-25T213128.png
security:
- kind: domain-security
  name: Eeye Digital Security Domain Security
  slug: eeye-digital-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eeye Digital Security Vulnerability Disclosure
  slug: eeye-digital-security-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: eeye-digital-security
tags:
- Company
- Cybersecurity
- Managed Detection and Response
- Managed XDR
- Incident Response
- Cyber Insurance
- Security Awareness
- Endpoint Security
- Europe
website: https://www.eye.security/
---
