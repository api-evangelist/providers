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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/quartet-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quartet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/quartet-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quartet-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.quartethealth.com/security/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quartet-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.quartethealth.com
- group: auth
  title: ''
  type: Security
  url: https://www.quartethealth.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quartethealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quartethealth.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://www.quartethealth.com/contact/
created: '2026-07-17'
description: Quartet Health is a value-based behavioral healthcare enablement and delivery platform that identifies, engages, and connects patients with mental health services across 39 states. It serves health plans, health systems, and community mental health centers with care coordination, patient-to-provider matching, and direct delivery of behavioral health care through its own medical group, focused on whole-person care for individuals with serious mental illness and other behavioral health needs. Quartet was acquired by NeuroFlow. Added to the API Evangelist network as a life-sciences company profile; the public site exposes no developer or API surface, but does publish a substantive security and compliance program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quartet.png
layout: provider
modified: '2026-07-20'
name: Quartet Health
nav: Providers
network: true
overview: 'Quartet Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Behavioral Health, Mental Health, and Healthcare.


  Quartet Health''s developer surface includes support and 10 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 19.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Quartet Domain Security
  slug: quartet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Quartet Vulnerability Disclosure
  slug: quartet-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Quartet Trust Center
  slug: quartet-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001, HIPAA/HITECH, PCI DSS, FedRAMP, HITRUST CSF
slug: quartet
tags:
- Company
- Life Sciences
- Behavioral Health
- Mental Health
- Healthcare
- Care Coordination
- Value-Based Care
- Digital Health
website: https://www.quartethealth.com
---
