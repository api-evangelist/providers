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
artifact_total: 3
common:
- group: design
  title: ''
  type: Conformance
  url: conformance/happy-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/happy-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/happy-health-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/happy-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.happysleep.com/
- group: operate
  title: ''
  type: Support
  url: https://support.happysleep.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.happysleep.com/select-billing-method
- group: start
  title: ''
  type: SignUp
  url: https://www.happysleep.com/select-billing-method
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.happysleep.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.happysleep.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happy-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/happyhealthinc/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/happy-health_stock/
coverage:
  checked: '2026-08-22'
  detail: Happy Health's own technology page advertises "Cloud integration and SDK available" and SMART on FHIR data exchange, and the Happy Ring clinical microsite advertises eClinical/EDC and EHR integration, but there is no developer site to read — docs., developer. and portal. happysleep.com are wildcard catch-alls that 302 into the consumer checkout funnel, the api.happysleep.com origin returns 403 AccessDenied on every path, and the only route to the integration surface is a "Request a Demo" form.
  evidence:
  - status: 200
    url: https://www.happysleep.com/tech
  - status: 302
    url: https://developer.happysleep.com/docs
  - status: 403
    url: https://api.happysleep.com/openapi.json
  - status: 200
    url: https://happyring.fiftyseven.co/clinical-trials.html
  - status: 404
    url: https://www.happysleep.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-22'
description: Happy Health, Inc. is an Austin, Texas digital health company behind the Happy Ring — an FDA-cleared, clinical-grade smart ring — and Happy Sleep, its at-home sleep-testing and sleep-apnea care service. The ring passively measures brain and body biomarkers using four LEDs, four electrodes, a three-axis accelerometer and two temperature sensors, capturing electrodermal activity, blood oxygen, pulse rate, heart-rate variability, respiratory rate, peripheral skin temperature and movement, and streams them over Bluetooth to the Happy Sleep app for clinician and researcher review. The company markets the platform to clinical-trial sponsors, provider groups and researchers with claims of cloud integration, an available SDK, eClinical/EDC and EHR integration, and SMART on FHIR interoperability — but publishes no public developer portal, API reference, SDK package or machine-readable specification, so none of that integration surface is reachable or evaluable without a sales conversation.
image: https://cdn.prod.website-files.com/66e82d3d92a4258c329c7664/670e1e48919ef3c2db43f90d_256x256.png
layout: provider
modified: '2026-08-22'
name: Happy Health
nav: Providers
network: true
overview: 'Happy Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Wearables.


  Happy Health''s developer surface includes support, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Happy Health Plans Pricing
  plan_count: 0
  slug: happy-health-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Happy Health Rate Limits
  slug: happy-health-rate-limits
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Happy Health Domain Security
  slug: happy-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: happy-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Wearables
- Remote Patient Monitoring
- Sleep
- Medical Devices
- Clinical Trials
- Consumer Health
website: https://www.happysleep.com/
---
