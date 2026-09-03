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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/francis-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.francismedical.com/
- group: company
  title: ''
  type: About
  url: https://www.francismedical.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.francismedical.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.francismedical.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.francismedical.com/faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.francismedical.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.francismedical.com/terms-and-conditions/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.francismedical.com/cookie-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.francismedical.com/product-security/
- group: company
  title: ''
  type: Careers
  url: https://www.francismedical.com/careers/
- group: other
  title: ''
  type: Leadership
  url: https://www.francismedical.com/leadership/
- group: other
  title: ''
  type: InstructionsForUse
  url: https://www.francismedical.com/emanual/
- group: other
  title: ''
  type: Locator
  url: https://www.francismedical.com/physician-locator/
- group: other
  title: ''
  type: Evidence
  url: https://www.francismedical.com/evidence/
- group: other
  title: ''
  type: Reimbursement
  url: https://www.francismedical.com/reimbursement/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/francis-medical
- group: other
  title: ''
  type: Product
  url: https://www.francismedical.com/vanquish/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/francis-medical-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/francis-medical-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Francis Medical's own Product Security page states that "our current product offerings do not include network-connected components" — the Vanquish Water Vapor Ablation System is a capital console and single-use catheter operated at the bedside, so there is no developer portal, no api./developer./docs./portal. hostname in DNS, and the only machine-readable JSON on the host is the marketing site's stock WordPress core REST API at /wp-json/.
  evidence:
  - status: 200
    url: https://www.francismedical.com/product-security/
  - status: 404
    url: https://www.francismedical.com/openapi.json
  - status: 404
    url: https://www.francismedical.com/swagger.json
  - status: 404
    url: https://www.francismedical.com/graphql
  - status: 404
    url: https://www.francismedical.com/llms.txt
  - status: 404
    url: https://www.francismedical.com/.well-known/agent-card.json
  - status: 404
    url: https://www.francismedical.com/.well-known/agent.json
  - status: 404
    url: https://www.francismedical.com/.well-known/security.txt
  - status: 200
    url: https://www.francismedical.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: Francis Medical is a privately held medical device company headquartered in Maple Grove, Minnesota, founded in 2018 by Michael Hoey and named for his father, who died of prostate cancer in 1991. It develops the Vanquish Water Vapor Ablation System, a transurethral outpatient platform that ablates targeted prostate tissue using the thermal energy stored in sterile water vapor delivered in short bursts through a catheter, with the aim of treating localized disease while avoiding the incontinence and sexual dysfunction associated with radical prostatectomy and radiation. The company received FDA Breakthrough Device Designation in 2023 and 510(k) clearance for prostate tissue ablation in December 2025, and it is running the VAPOR 1 and VAPOR 2 clinical studies alongside a long-term registry; it has signalled intent to extend the same water vapor platform to bladder and kidney cancer. Francis Medical has raised roughly $160 million to date, including an $80 million Series C in January
  2025 co-led by Solas BioVentures and Arboretum Ventures, with earlier participation from Coloplast. It is led by president and CEO Mike Kujak. Francis Medical publishes a physician locator, an electronic instructions-for-use (eIFU) library and a coordinated vulnerability disclosure policy for its devices and embedded software, but operates no public developer program, API documentation, or machine-readable API contract.
image: https://www.francismedical.com/wp-content/uploads/2025/08/Vanquish_Stacked_RGB-1.png
layout: provider
modified: '2026-08-16'
name: Francis Medical
nav: Providers
network: true
overview: 'Francis Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Oncology, and Urology.


  Francis Medical''s developer surface includes engineering blog, support, FAQ, and 18 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/francis-medical/refs/heads/main/screenshots/francis-medical-2026-09-02T145543.png
security:
- kind: domain-security
  name: Francis Medical Domain Security
  slug: francis-medical-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Francis Medical Vulnerability Disclosure
  slug: francis-medical-vulnerability-disclosure
  summary_line: disclosure policy published
slug: francis-medical
tags:
- Company
- Healthcare
- Medical Devices
- Oncology
- Urology
- Prostate Cancer
- Surgery
- Ablation
- Clinical Trials
- Minimally Invasive
website: https://www.francismedical.com/
---
