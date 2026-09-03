---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/latigo-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latigobio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://latigobio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latigobio.com/privacy-policy/
coverage:
  checked: '2026-08-23'
  detail: 'Latigo Biotherapeutics is a clinical-stage drug developer whose product is a molecule (oral NaV1.8 inhibitors LTG-001/LTG-321), not software — it runs no developer program: api., developer., docs., dev., portal., app. and data.latigobio.com are all NXDOMAIN, github.com/latigobio and /LatigoBiotherapeutics 404, and the corporate site itself sits behind a SiteGround robot challenge that answers HTTP 202 with an identical challenge shell to every path, including all eight /.well-known/* probes.'
  evidence:
  - status: 202
    url: https://latigobio.com/openapi.json
  - status: 202
    url: https://latigobio.com/.well-known/agent-card.json
  - status: 404
    url: https://github.com/latigobio
  - status: 404
    url: https://registry.npmjs.org/latigobio
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Latigo Biotherapeutics, Inc. ("Latigo Bio") is a clinical-stage biotechnology company headquartered in Thousand Oaks, California, developing novel non-opioid medicines for acute and chronic pain. Its lead candidates LTG-001 and LTG-321 are oral NaV1.8 sodium-channel inhibitors targeting pain at its peripheral source without the addiction risk of opioids; LTG-001 holds FDA Fast Track designation and reported positive Phase 2b results in post-abdominoplasty acute pain, published in the New England Journal of Medicine in July 2026. The company was founded on human-genetics-validated targets and uses in-house AI/ML and structure-based drug design to optimize potency and selectivity. It debuted in 2024 with a $135M Series A and closed a $150M Series B in March 2025, backed by Westlake Village BioPartners, 5AM Ventures, Foresite Capital and Corner Ventures. Latigo is a therapeutics developer, not a software vendor: it publishes no public API, developer portal, SDK or machine-readable
  specification.'
layout: provider
modified: '2026-08-23'
name: Latigo Bio
nav: Providers
network: true
overview: Latigo Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Discovery.
random_paper: 12
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/latigo-bio/refs/heads/main/screenshots/latigo-bio-2026-09-02T150217.png
security:
- kind: domain-security
  name: Latigo Bio Domain Security
  slug: latigo-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: latigo-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Clinical Trials
- Healthcare
- Pain Management
- Therapeutics
website: https://latigobio.com/
---
