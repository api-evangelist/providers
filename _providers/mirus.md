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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mirusmed.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mirusmed.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mirusmed.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.mirusmed.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mirusmed.com/wp-content/uploads/2021/10/MiRus-Privacy-Policy.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mirusmed.com/wp-content/uploads/2021/10/MiRus-Terms-of-Use-Policy.pdf
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/mirus_stock/
- group: design
  title: ''
  type: Conformance
  url: conformance/mirus-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mirus-llms.txt
coverage:
  checked: '2026-08-25'
  detail: 'Every route of the GALILEO / "Mirus Analytics" backend at rpm.mirusmed.com/api/ — including its FHIR endpoint and the /api/v1/fhir/metadata CapabilityStatement — answers 401 with WWW-Authenticate: Bearer to anonymous callers, and MiRus publishes no developer portal, reference, OpenAPI, SDK or .well-known document anywhere else on its public surface.'
  evidence:
  - status: 401
    url: https://rpm.mirusmed.com/api/v1/fhir
  - status: 401
    url: https://rpm.mirusmed.com/api/v1/fhir/metadata
  - status: 401
    url: https://rpm.mirusmed.com/api/openapi.json
  - status: 404
    url: https://www.mirusmed.com/.well-known/api-catalog
  - status: 404
    url: https://rpm.mirusmed.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-25'
description: 'MiRus is a Marietta, Georgia life sciences company founded in 2015 that develops and commercializes implants and procedural solutions built on MoRe, its proprietary molybdenum-rhenium superalloy, for spine, orthopaedic and structural heart disease. Its FDA-cleared portfolio spans the Europa pedicle screw system, CYGNUS MoRe anterior cervical plating, 3DR printed interbody and corpectomy systems, the Atlas foot-and-ankle plating line, and the Siegel transcatheter aortic valve, alongside GALILEO — a spine-focused surgical planning, intra-operative alignment measurement and remote physiologic monitoring platform delivered to clinicians as the "Mirus Analytics" web application at rpm.mirusmed.com. MiRus publishes no public developer program: the GALILEO backend, which includes a FHIR route, is bearer/Cognito authenticated and answers 401 on every path, and no OpenAPI, SDK, reference or developer portal is published anywhere on its public surface.'
image: https://www.mirusmed.com/wp-content/uploads/2021/07/MiRus_mixed_with-metal-clipping-mask.png
layout: provider
modified: '2026-08-25'
name: MiRus
nav: Providers
network: true
overview: 'MiRus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Life Sciences, and Spine.


  MiRus'' developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Mirus Plans Pricing
  plan_count: 0
  slug: mirus-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Mirus Rate Limits
  slug: mirus-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Mirus Authentication
  slug: mirus-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mirus Domain Security
  slug: mirus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mirus
tags:
- Company
- Medical Devices
- Healthcare
- Life Sciences
- Spine
- Orthopaedics
- Structural Heart
- Remote Patient Monitoring
- Medical Implants
- Surgical Planning
website: https://www.mirusmed.com/
---
