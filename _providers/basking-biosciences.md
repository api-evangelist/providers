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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basking-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.baskingbiosciences.com/
- group: company
  title: ''
  type: About
  url: https://www.baskingbiosciences.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.baskingbiosciences.com/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/basking-biosciences-inc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baskingbiosciences.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baskingbiosciences.com/legal/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/basking-biosciences-llms.txt
coverage:
  checked: '2026-08-10'
  detail: Basking Biosciences is a clinical-stage biopharmaceutical company developing the RNA-aptamer thrombolytic BB-031; its entire web presence is a 20-URL Webflow marketing site (science, programs, publications, news releases, legal) whose sitemap contains no developer, docs, or API path, and api.baskingbiosciences.com does not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.baskingbiosciences.com/sitemap.xml
  - status: 404
    url: https://www.baskingbiosciences.com/openapi.json
  - status: 404
    url: https://www.baskingbiosciences.com/developers
  - status: 404
    url: https://www.baskingbiosciences.com/.well-known/agent-card.json
  - status: 404
    url: https://pypi.org/pypi/basking-biosciences/json
  reason: not-a-software-company
  state: none
created: '2026-07-17'
description: Basking Biosciences is a clinical-stage biopharmaceutical company in Research Triangle, North Carolina (with operations in Mitchelton, Queensland, Australia) developing novel therapies for life-threatening blood clots. Its lead program BB-031 is an investigational RNA aptamer that targets von Willebrand Factor (vWF) to deliver a rapid-onset, targeted, and reversible thrombolytic for acute ischemic stroke, paired with BB-025, a direct-acting reversal agent designed to rapidly neutralize BB-031. The company is running the RAISE Phase 2 clinical trial and is backed by Insight Partners. Surfaced as a VC portfolio company and added to the API Evangelist network; the company publishes no public developer API, SDK, or documentation surface, so this profile carries company identity only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basking-biosciences.png
layout: provider
modified: '2026-08-10'
name: Basking Biosciences
nav: Providers
network: true
overview: 'Basking Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotech Therapeutics, Biopharmaceutical, Clinical Stage, and Stroke.


  Basking Biosciences'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basking-biosciences/refs/heads/main/screenshots/basking-biosciences-2026-07-25T202426.png
security:
- kind: domain-security
  name: Basking Biosciences Domain Security
  slug: basking-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basking-biosciences
tags:
- Company
- Biotech Therapeutics
- Biopharmaceutical
- Clinical Stage
- Stroke
- Thrombosis
- Drug Development
- Life Sciences
website: https://www.baskingbiosciences.com/
---
