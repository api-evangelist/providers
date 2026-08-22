---
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
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/maple-health-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maple-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maple-health-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getmaple.ca/security/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/maple-health-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/maple-health-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maple-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.getmaple.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.getmaple.ca/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getmaple.ca/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.getmaple.ca/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getmaple
- group: operate
  title: ''
  type: Support
  url: https://www.getmaple.ca/contact/
- group: auth
  title: ''
  type: Security
  url: https://www.getmaple.ca/security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmaple.ca/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmaple.ca/privacy/
created: '2026-07-24'
description: Maple is a Canadian virtual-care company (getmaple.ca) headquartered in Toronto that connects patients across every Canadian province to Canadian-licensed doctors and nurse practitioners for on-demand and scheduled telehealth. Its consumer membership and B2B programs cover same-day acute care, paediatrics, mental health therapy and psychiatry, specialist consultations, chronic-condition management, prescriptions with pickup or delivery, lab requisitions, and medical notes, delivered through iOS, Android, and web apps. Maple sells to individuals and to employers, insurers, and health systems (clients include Air Canada, Blue Cross, Rogers, and Green Shield) via custom care programs rather than a self-serve technical platform. As of this review Maple publishes NO public developer portal, REST API, or HL7 FHIR endpoint; there is no documented CapabilityStatement or SMART-on-FHIR configuration. Its interoperability posture is enterprise/partner-gated, and its security program is
  SOC 2 Type II and ISO 27001 aligned with a responsible-disclosure channel at security@getmaple.ca.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Maple
nav: Providers
network: true
overview: 'Maple is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, Telehealth, Virtual Care, and Digital Health.


  Maple''s developer surface includes engineering blog, pricing, support, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 21.5
  delta: -1.2
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 22.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maple-health/refs/heads/main/screenshots/maple-health-2026-07-25T230125.png
security:
- kind: domain-security
  name: Maple Health Domain Security
  slug: maple-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maple Health Vulnerability Disclosure
  slug: maple-health-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Maple Health Trust Center
  slug: maple-health-trust-center
  summary_line: SOC 2, SOC 2 Type II, ISO 27001
slug: maple-health
tags:
- Healthcare
- Canada
- Telehealth
- Virtual Care
- Digital Health
- Mental Health
- e-Prescribing
- Remote Care
website: https://www.getmaple.ca/
---
