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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seaport-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seaporttx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seaporttx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seaporttx.com/terms-of-use/
coverage:
  checked: '2026-08-26'
  detail: Seaport Therapeutics is a clinical-stage neuropsychiatric drug developer whose product is the Glyph oral-prodrug platform, not software; seaporttx.com is a corporate WordPress site that returns a real 404 on every OpenAPI, GraphQL, llms.txt and /.well-known/ path, and its only machine-readable document is the WordPress core /wp-json/ discovery index that ships with the CMS.
  evidence:
  - status: 404
    url: https://seaporttx.com/openapi.json
  - status: 404
    url: https://seaporttx.com/llms.txt
  - status: 404
    url: https://seaporttx.com/.well-known/agent-card.json
  - status: 200
    url: https://seaporttx.com/wp-json/
  - status: 0
    url: https://investors.seaporttx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Seaport Therapeutics is a Boston-based clinical-stage biopharmaceutical company developing new medicines for patients with depression, anxiety and other neuropsychiatric disorders. Its proprietary Glyph platform — licensed from the Porter Research Group at Monash University — applies lymphatic-targeting oral prodrug chemistry so that more medicine reaches the bloodstream and brain while bypassing first-pass liver metabolism and reducing side effects. The clinical pipeline includes GlyphAllo (SPT-300), an oral allopregnanolone prodrug in Phase 2 for major depressive disorder; GlyphAgo (SPT-320), an oral agomelatine prodrug in Phase 2 for generalized anxiety disorder; and Glyph2BLSD (SPT-348), a pre-clinical non-hallucinogenic 2-bromo-LSD neuroplastogen. Seaport publishes no public API, developer portal, SDK or machine-readable specification; its public web surface is a corporate WordPress site plus a hosted investor-relations subdomain.
image: https://seaporttx.com/wp-content/uploads/2023/11/seaport_logo.png
layout: provider
modified: '2026-08-26'
name: Seaport Therapeutics
nav: Providers
network: true
overview: Seaport Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seaport-therapeutics/refs/heads/main/screenshots/seaport-therapeutics-2026-09-02T154634.png
security:
- kind: domain-security
  name: Seaport Therapeutics Domain Security
  slug: seaport-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: seaport-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Neuroscience
- Drug Delivery
website: https://seaporttx.com/
---
