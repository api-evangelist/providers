---
agent_readiness:
  band: human-only
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The REST API behind Sibel Health's ANNE cloud hubs. The base https://api.sibelhealth.com/jsn/alpha is referenced directly by the JavaScript bundle of the company's own datahub.sibelhealth.com single-p
  name: Sibel Health ANNE Cloud API
  slug: sibel-health-anne-cloud-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sibel-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sibel-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sibelhealth.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sibelhealth.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sibelhealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sibelhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sibelhealth.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://sibelhealth.com/request-demo/
- group: auth
  title: ''
  type: Security
  url: https://sibelhealth.com/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sibel-health-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sibel-health-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sibel-health-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sibel-health-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sibel-health-conformance.yml
- group: company
  title: ''
  type: Blog
  url: https://sibelhealth.com/news/
- group: other
  title: ''
  type: Publications
  url: https://sibelhealth.com/publications/
coverage:
  checked: '2026-08-27'
  detail: Sibel Health runs a live AWS API Gateway at api.sibelhealth.com/jsn/alpha — the base its own datahub.sibelhealth.com application calls — but every path, including /openapi.json and /.well-known/*, returns 403 to an anonymous caller, there is no developer portal (developer.sibelhealth.com has a valid certificate but never answers), and the SDK that two August 2024 FDA clearances were granted for is released only to strategic partners, so the contract is reachable only with an active tenant or signed agreement.
  evidence:
  - status: 403
    url: https://api.sibelhealth.com/jsn/alpha
  - status: 403
    url: https://api.sibelhealth.com/openapi.json
  - status: <no response>
    url: https://developer.sibelhealth.com/
  - status: 200
    url: https://sibelhealth.com/page-sitemap.xml
  reason: customer-only-docs
  state: gated
created: '2026-08-27'
description: 'Sibel Health, Inc. is a Chicago-based medical technology company, with an international office in Seoul, South Korea, that builds the FDA-cleared ANNE platform for continuous clinical-grade vital-sign monitoring. The platform pairs soft, flexible, rechargeable wearable sensors — ANNE Chest (worn at the suprasternal notch), ANNE Limb, and the ADAM sensor — with an ANNE Hub gateway, AI-enabled data analytics, and an integrated mobile plus cloud software platform. It is used across neonatal, pediatric, maternal, adult inpatient, hospital-at-home, remote patient monitoring, sleep diagnostic and decentralized clinical trial settings. Sibel operates a customer-facing cloud (per-tenant hubs such as datahub.sibelhealth.com and emory.hub.sibelhealth.com) backed by a live REST API at api.sibelhealth.com, and in August 2024 received two additional FDA clearances that let ANNE Chest and ANNE Limb interoperate with third-party software applications through a Sibel software development kit.
  Neither that API nor that SDK is publicly documented: there is no developer portal, no published OpenAPI or other machine-readable contract, no public SDK package on any registry, and access is arranged through the company sales and partnership process.'
image: https://sibelhealth.com/wp-content/uploads/2023/03/sibel.png
layout: provider
modified: '2026-08-27'
name: Sibel Health
nav: Providers
network: true
overview: 'Sibel Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical Devices, and Remote Patient Monitoring.


  Sibel Health''s developer surface includes support, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Sibel Health Plans Pricing
  plan_count: 0
  slug: sibel-health-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Sibel Health Rate Limits
  slug: sibel-health-rate-limits
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sibel Health Authentication
  slug: sibel-health-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Sibel Health Domain Security
  slug: sibel-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sibel Health Vulnerability Disclosure
  slug: sibel-health-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sibel-health
tags:
- Company
- Health
- Healthcare
- Medical Devices
- Remote Patient Monitoring
- Wearables
- Digital Health
- Vital Signs
- Clinical Trials
- Sensors
- Internet of Things
- Sleep
website: https://sibelhealth.com/
---
