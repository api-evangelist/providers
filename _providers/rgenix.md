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
  url: security/rgenix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inspirna.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inspirna.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inspirna.com/terms-of-use/
coverage:
  checked: '2026-08-26'
  detail: Rgenix is a clinical-stage oncology drug developer that renamed itself Inspirna in September 2021; rgenix.com now 301s to an unresponsive www.rgenix.com, and the live corporate site inspirna.com is a WordPress marketing site (company/science/pipeline/patients/careers/news) with no developer section, no GitHub organization, and a 404 on every contract-discovery path.
  evidence:
  - status: 404
    url: https://inspirna.com/openapi.json
  - status: 404
    url: https://inspirna.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/inspirna
  - status: 301
    url: http://rgenix.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Rgenix, Inc. is a clinical-stage biopharmaceutical company founded by scientists from The Rockefeller University to discover and develop first-in-class small molecules and biologics against previously undruggable drivers of cancer metastasis, using its proprietary RNA-DRIVEr target-discovery platform. Its programs include ompenaclid (RGX-202), an oral SLC6A8/creatine-transporter inhibitor in Phase 2 for RAS-mutant colorectal cancer, abequolixron (RGX-104), an oral LXR agonist in Phase 1b/2, and RGX-019-MMAE, a MERTK-targeting antibody-drug conjugate. The company changed its corporate name from Rgenix to Inspirna in September 2021 and operates from Long Island City, New York. It is a therapeutics developer with no public API, developer program, or machine-readable interface.
layout: provider
modified: '2026-08-26'
name: Rgenix
nav: Providers
network: true
overview: Rgenix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Drug Discovery.
random_paper: 2
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Rgenix Domain Security
  slug: rgenix-domain-security
  summary_line: TLSv1.3
slug: rgenix
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Drug Discovery
- Clinical Trials
- Life Sciences
website: https://inspirna.com/
---
