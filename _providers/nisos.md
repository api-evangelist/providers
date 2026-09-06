---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Credential-gated HTTPS API behind the Nisos Ascend human risk management platform. Its existence and base URL are established from Nisos''s own production build: the Ascend console''s configuration modu'
  name: Nisos Ascend External API
  slug: nisos-ascend-external-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nisos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nisos.com/
- group: company
  title: ''
  type: Blog
  url: https://nisos.com/nisos-blog/
- group: operate
  title: ''
  type: Support
  url: https://nisos.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nisos.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nisos.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nisos.com/
- group: start
  title: ''
  type: Login
  url: https://ascend.nisos.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nisos-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nisos-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nisos-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nisos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nisos-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Nisos runs a live external API for its Ascend platform at https://api.ascend.nisos.com — named EXTERNAL_API_URL in the Ascend console's own production JavaScript — but it is reachable only with tenant credentials, answering every anonymous request including /openapi.json with HTTP 403 {"message":"Forbidden"}, and Nisos publishes no developer portal, API reference or specification anywhere on its 144-page public site.
  evidence:
  - status: 403
    url: https://api.ascend.nisos.com/openapi.json
  - status: 401
    url: https://platform.ascend.nisos.com/openapi.json
  - status: 404
    url: https://nisos.com/openapi.json
  - status: 200
    url: https://ascend.nisos.com/.well-known/zzz-control-probe-9182
  - status: 404
    url: https://nisos.com/developers/
  - status: 200
    url: https://nisos.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Nisos is a human risk intelligence company, founded in 2015 and headquartered in Alexandria, Virginia, that combines analyst-led investigative tradecraft with an AI-assisted platform to help enterprises detect, investigate and mitigate threats that originate with people. Its Managed Intelligence services cover executive protection and digital exposure, employment and hiring fraud, insider threat, third-party and supply-chain intelligence, threat landscape assessment, OSINT monitoring and adversary attribution investigations, drawing on surface, deep and dark web collection. Its Ascend platform productizes that tradecraft for client-led use, shipping Executive Shield and Insider Threat Intelligence modules with continuous monitoring, PII removal, risk analytics and dashboard reporting. Nisos sells enterprise-only through a demo request; it publishes no developer portal, no API reference and no machine-readable contract, though the Ascend console does call a live, credential-gated
  external API host of its own.
image: https://nisos.com/wp-content/uploads/2025/03/NISOS_logo_low_res_horiz-black-cropped.png
layout: provider
modified: '2026-08-26'
name: Nisos
nav: Providers
network: true
overview: 'Nisos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Threat Intelligence, Human Risk Management, Insider Threat, Executive Protection, and OSINT.


  Nisos'' developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Nisos Plans Pricing
  plan_count: 0
  slug: nisos-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Nisos Rate Limits
  slug: nisos-rate-limits
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 44.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nisos/refs/heads/main/screenshots/nisos-2026-09-02T150757.png
security:
- kind: domain-security
  name: Nisos Domain Security
  slug: nisos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nisos Trust Center
  slug: nisos-trust-center
  summary_line: trust center published
slug: nisos
tags:
- Threat Intelligence
- Human Risk Management
- Insider Threat
- Executive Protection
- OSINT
- Digital Investigations
- Cybersecurity
- Adversary Attribution
- Employment Fraud
- Third-Party Risk
- Trust and Safety
- Dark Web Monitoring
- Managed Service
- Federal
website: https://nisos.com/
---
