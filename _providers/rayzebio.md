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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rayzebio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rayzebio.com/
- group: company
  title: ''
  type: About
  url: https://rayzebio.com/about/about-overview/
- group: other
  title: ''
  type: Team
  url: https://rayzebio.com/about/team/
- group: operate
  title: ''
  type: Contact
  url: https://rayzebio.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://rayzebio.com/careers/
- group: company
  title: ''
  type: BlogRSS
  url: https://rayzebio.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rayzebio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rayzebio.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rayzebio/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.bms.com/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/rayzebio_stock/
coverage:
  checked: '2026-08-26'
  detail: 'RayzeBio is a clinical-stage radiopharmaceutical drug developer, now a Bristol Myers Squibb company, whose entire public surface is a 25-page WordPress marketing site — /openapi.json, /openapi.yaml, /swagger.json, /api-docs, /graphql, /llms.txt and every /.well-known/* path return a real 404, no GitHub org or npm/PyPI package exists under the name, and the only machine-readable endpoint on the host is the default WordPress /wp-json/ CMS route index (209 core/plugin routes: wp/v2, yoast, akismet, contact-form-7, wpe cache), which is WordPress plumbing and not a RayzeBio API product.'
  evidence:
  - status: 404
    url: https://rayzebio.com/openapi.json
  - status: 404
    url: https://rayzebio.com/graphql
  - status: 404
    url: https://rayzebio.com/.well-known/agent-card.json
  - status: 404
    url: https://rayzebio.com/llms.txt
  - status: 200
    url: https://rayzebio.com/wp-json/
  - status: 404
    url: https://api.github.com/orgs/rayzebio
  - status: 301
    url: https://rayzebio.com/media/news-new/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: RayzeBio is a clinical-stage radiopharmaceutical therapeutics company headquartered at 5505 Morehouse Drive, Suite 300, San Diego, California, and since 2024 a wholly owned Bristol Myers Squibb company. It develops targeted radiopharmaceutical therapies (RPTs) built on the alpha-emitting isotope actinium-225, led by RYZ101 (225Ac-DOTATATE) against somatostatin receptor 2 (SSTR2)-expressing tumors including gastroenteropancreatic neuroendocrine tumors, extensive-stage small cell lung cancer and hormone-receptor-positive breast cancer, alongside earlier programs targeting glypican-3 (GPC3) in hepatocellular carcinoma and ACP3, plus paired diagnostic imaging agents such as [68Ga]Ga-RAYZ-8009. Its public web presence is a WordPress corporate marketing site covering discovery capabilities, radioisotope manufacturing, the pipeline, posters and presentations, leadership and careers; the company operates no developer program and publishes no API, SDK, or machine-readable specification,
  and is profiled here for network completeness rather than for an API surface.
image: https://rayzebio.com/wp-content/uploads/2024/04/rayzebio_logo_grt_gry-300x122.png
layout: provider
modified: '2026-08-26'
name: RayzeBio
nav: Providers
network: true
overview: RayzeBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Radiopharmaceuticals.
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Rayzebio Domain Security
  slug: rayzebio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rayzebio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Radiopharmaceuticals
- Life Sciences
- Healthcare
- Clinical Trials
- Drug Discovery
website: https://rayzebio.com/
---
