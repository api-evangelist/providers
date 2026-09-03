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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sof-a-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sofiasalud.com
- group: company
  title: ''
  type: Blog
  url: https://www.sofiasalud.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.sofiasalud.com/otros/preguntas-frecuentes-sofia
- group: start
  title: ''
  type: SignUp
  url: https://cotiza.sofiasalud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sofiasalud.com/otros/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sofiasalud.com/otros/aviso-de-privacidad
created: '2026-07-17'
description: Sofía is a 100% Mexican health insurance company (aseguradora) offering medical coverage for individuals, families, and businesses, delivered primarily through a mobile app with plans that carry no deductibles. Regulated in Mexico by the CNSF, Secretaría de Salud, and CONDUSEF, and backed by Index Ventures. This is a consumer/enterprise insurance provider surfaced as a portfolio-company lead; a live probe of the public surface found no developer program, API, or /.well-known/ discovery documents, so this profile remains identity-only pending any future API exposure.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sof-a.png
layout: provider
modified: '2026-07-21'
name: Sofía
nav: Providers
network: true
overview: 'Sofía is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Insurance, Insurance, and Mexico.


  Sofía''s developer surface includes engineering blog, support, signup flow, and 4 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sof-a/refs/heads/main/screenshots/sof-a-2026-09-02T160055.png
security:
- kind: domain-security
  name: Sof A Domain Security
  slug: sof-a-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sof-a
tags:
- Company
- Healthcare
- Health Insurance
- Insurance
- Mexico
- Insurtech
- Digital Health
website: https://www.sofiasalud.com
---
