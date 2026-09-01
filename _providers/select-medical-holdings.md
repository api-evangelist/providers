---
access_model:
  confidence: high
  label: No pricing — SMART-on-FHIR app registration and patient authorization required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Live HL7 FHIR R4 (4.0.1) patient-access API operated by Select Medical on its Epic platform (community et0948, Epic software version November 2025). The server's own CapabilityStatement self-identifie
  name: Select Medical FHIR R4 API
  slug: select-medical-holdings-fhir-r4
- description: 'Legacy HL7 FHIR DSTU2 (1.0.2) endpoint operated by Select Medical on the same Epic platform, registered as "Select Medical" in Epic''s public DSTU2 endpoint directory since 2020-06-01 and still listed '
  name: Select Medical FHIR DSTU2 API
  slug: select-medical-holdings-fhir-dstu2
artifact_total: 7
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/select-medical-holdings-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.selectmedical.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/select-medical-holdings
- group: start
  title: ''
  type: SignUp
  url: https://mychart.selectmedical.com/MyChart/signup
- group: start
  title: ''
  type: Login
  url: https://mychart.selectmedical.com/MyChart/Authentication/Login
- group: agent
  title: ''
  type: WellKnown
  url: well-known/select-medical-holdings-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/select-medical-holdings-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/select-medical-holdings-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/select-medical-holdings-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/select-medical-holdings-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/select-medical-holdings-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/select-medical-holdings-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/select-medical-holdings-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/select-medical-holdings-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/select-medical-holdings-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/select-medical-holdings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/select-medical-holdings-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/select-medical-holdings-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/select-medical-holdings-fhir-r4-overlay.yaml
- group: other
  title: ''
  type: FHIR
  url: fhir/select-medical-holdings-r4-capabilitystatement.json
created: '2026-03-24'
description: Select Medical Holdings Corporation is one of the largest operators of specialty hospitals and outpatient rehabilitation clinics in the United States, running critical illness recovery hospitals, inpatient rehabilitation hospitals, outpatient rehabilitation clinics and occupational health centers across the country. Select Medical is not a software vendor and publishes no commercial developer program, but as a covered healthcare provider running Epic it operates a live HL7 FHIR R4 patient-access API — registered under "Select Medical" in Epic's public endpoint directory — that exposes 59 FHIR resource types behind SMART-on-FHIR OAuth 2.0, together with an Epic MyChart patient portal. This profile documents that regulated interoperability surface rather than a commercial API product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/select-medical-holdings.png
layout: provider
modified: '2026-08-28'
name: Select Medical Holdings
nav: Providers
network: true
overview: 'Select Medical Holdings publishes 1 API on the [APIs.io](https://apis.io/) network: Select Medical FHIR R4 API. Tagged areas include Healthcare, Hospitals, Rehabilitation, Patient Access, and FHIR.


  Select Medical Holdings'' developer surface includes signup flow, authentication, and 19 more developer resources.'
plans:
- name: Select Medical Holdings Plans Pricing
  plan_count: 0
  slug: select-medical-holdings-plans-pricing
press:
- date: '2026-05-25'
  title: Select Medical Holdings Corporation (SEM) Q1 2026 ...
  url: https://seekingalpha.com/article/4897429-select-medical-holdings-corporation-sem-q1-2026-earnings-call-transcript
- date: '2026-05-25'
  title: SELECT MEDICAL HOLDINGS CORP SEC 10-K Report
  url: https://www.tradingview.com/news/tradingview:4c841f4ce399c:0-select-medical-holdings-corp-sec-10-k-report/
- date: '2026-05-25'
  title: Select Medical Holdings Corporation to be Acquired by ...
  url: https://www.prnewswire.com/news-releases/select-medical-holdings-corporation-to-be-acquired-by-consortium-led-by-robert-a-ortenzio-martin-f-jackson-and-wcas-302701686.html
- date: '2026-05-25'
  title: Select Medical Holdings Corporation to Announce Second ...
  url: https://www.biospace.com/select-medical-holdings-corporation-to-announce-second-quarter-2019-results-on-thursday-august-1
- date: '2026-05-25'
  title: Select Medical Holdings Corporation Announces ...
  url: https://www.prnewswire.com/news-releases/select-medical-holdings-corporation-announces-expiration-of-hart-scott-rodino-waiting-period-302756311.html
random_paper: 16
rate_limits:
- limit_count: 0
  name: Select Medical Holdings Rate Limits
  slug: select-medical-holdings-rate-limits
scopes:
- name: Select Medical Holdings Scopes
  scope_count: 5
  slug: select-medical-holdings-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 34.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Select Medical Holdings Authentication
  slug: select-medical-holdings-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Select Medical Holdings Domain Security
  slug: select-medical-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: select-medical-holdings
tags:
- Healthcare
- Hospitals
- Rehabilitation
- Patient Access
- FHIR
- Interoperability
- Electronic Health Records
- Fortune 1000
website: https://www.selectmedical.com
---
