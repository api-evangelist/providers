---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://x-tention.com/en
- group: other
  title: ''
  type: Products
  url: https://x-tention.com/en/products
- group: company
  title: ''
  type: Blog
  url: https://x-tention.com/en/newsroom
- group: company
  title: ''
  type: BlogRSS
  url: https://x-tention.com/en/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://x-tention.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://x-tention.com/en/tcs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x-tention.com/en/privacy-policy
- group: other
  title: ''
  type: Imprint
  url: https://x-tention.com/en/imprint
- group: other
  title: ''
  type: Customers
  url: https://x-tention.com/en/success-stories
- group: learn
  title: ''
  type: Training
  url: https://mach.health/academy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/x-tention
- group: auth
  title: ''
  type: Security
  url: https://x-tention.com/en/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://x-tention.com/en/information-security-policy-clients
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/x-tention-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/x-tention-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/x-tention-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/x-tention-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/x-tention-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/x-tention-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/x-tention-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/x-tention-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/x-tention-llms.txt
coverage:
  checked: '2026-09-02'
  detail: x-tention's only technical documentation lives inside the MACH Portal at portal.mach.health, an Angular application that returns the same 62,604-byte "Loading MACH Portal" login shell for every path including ones that cannot exist, so an anonymous visitor reaches no reference, no spec and no endpoint list — the public site markets HL7 v2, FHIR, openEHR, IHE and DICOM support across MACH and the Interoperability Platform but publishes no contract for any of it.
  evidence:
  - status: 200
    url: https://portal.mach.health/
  - status: 200
    url: https://portal.mach.health/.apievangelist-control-probe-does-not-exist-9f2a
  - status: 404
    url: https://x-tention.com/openapi.json
  - status: 404
    url: https://mach.health/openapi.json
  - status: 404
    url: https://x-tention.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: 'x-tention Informationstechnologie GmbH is an Austrian healthcare IT company headquartered in Wels, Upper Austria, that builds, integrates and operates information systems for hospitals, health insurers and social-care providers across Austria, Germany, Switzerland and the United Kingdom. Its products centre on healthcare interoperability: MACH (Medical Application Connection Hub), a hybrid on-premises and cloud integration platform built on the Orchestra health service bus it acquired with soffico GmbH, together with MACH Orchestra, MACH Portal, MACH Gateway, MACH MPI, DICOM Routing, a File Streaming Channel and HL7 FHIR Templates; an Interoperability Platform covering HL7 v2, IHE, FHIR and openEHR; a Clinical Data Platform for the DACH region; a gematik-approved TI-Messenger built with Famedly on the Matrix protocol; and cybersecurity services. x-tention publishes no public developer portal, API reference or machine-readable API contract: technical documentation lives inside
  the customer-authenticated MACH Portal, so its integration surfaces are described in marketing and product literature only.'
image: https://x-tention.com/themes/custom/xttheme/logo.svg
layout: provider
modified: '2026-09-02'
name: x-tention
nav: Providers
network: true
overview: 'x-tention is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Interoperability, and Integration.


  x-tention''s developer surface includes engineering blog, support, training material, and 19 more developer resources.'
plans:
- name: X Tention Plans Pricing
  plan_count: 0
  slug: x-tention-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: X Tention Rate Limits
  slug: x-tention-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: X Tention Domain Security
  slug: x-tention-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: X Tention Vulnerability Disclosure
  slug: x-tention-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: X Tention Trust Center
  slug: x-tention-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, ISO 9001
slug: x-tention
tags:
- Company
- Healthcare
- Health IT
- Interoperability
- Integration
- HL7
- FHIR
- openEHR
- DICOM
- IHE
- Hospital Information Systems
- Clinical Data
- Austria
- Cybersecurity
- Secure Messaging
website: https://x-tention.com/en
---
