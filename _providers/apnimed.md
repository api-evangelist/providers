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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apnimed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apnimed.com/
- group: company
  title: ''
  type: About
  url: https://apnimed.com/about/
- group: company
  title: ''
  type: Blog
  url: https://apnimed.com/news/
- group: operate
  title: ''
  type: Support
  url: https://apnimed.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apnimed.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apnimed.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.apnimed.com/
- group: company
  title: ''
  type: Careers
  url: https://apnimed.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apnimed
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/apnimed_stock/
- group: company
  title: ''
  type: BlogFeeds
  url: https://apnimed.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://apnimed.com/news/
- group: other
  title: ''
  type: Research
  url: https://apnimed.com/publications/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apnimed-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Apnimed is a clinical-stage drug developer whose product is an oral pill (AD109) for obstructive sleep apnea, so there is no software surface to expose; apnimed.com is a WordPress marketing site whose full Yoast sitemap lists 24 pages and not one developer, API, or documentation page, and api./docs./developer.apnimed.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://apnimed.com/openapi.json
  - status: 404
    url: https://apnimed.com/llms.txt
  - status: 404
    url: https://apnimed.com/.well-known/agent-card.json
  - status: 404
    url: https://apnimed.com/.well-known/security.txt
  - status: 0
    url: https://api.apnimed.com/openapi.json
  - status: 404
    url: https://ir.apnimed.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Apnimed is a late-stage clinical-stage pharmaceutical company headquartered in Cambridge, Massachusetts, developing novel oral drug therapies for sleep-related breathing disorders. Its lead candidate AD109 (Oxnimbi) is a fixed-dose combination of an anti-muscarinic and a selective norepinephrine reuptake inhibitor, designed to improve upper-airway muscle activity and treat an underlying neuromuscular cause of obstructive sleep apnea (OSA) rather than manage it mechanically. The company was founded in 2017, partners with Shionogi through the Shionogi-Apnimed Sleep Science (SASS) joint venture, and had a New Drug Application for AD109 accepted by the FDA in 2026. Apnimed is a drug developer, not a software vendor: it publishes no developer portal, API documentation, or machine-readable API artifacts.'
image: https://apnimed.com/wp-content/themes/apnimed/favicon/android-icon-192x192.png
layout: provider
modified: '2026-08-06'
name: Apnimed
nav: Providers
network: true
overview: 'Apnimed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Healthcare, and Life Sciences.


  Apnimed''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 4
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apnimed/refs/heads/main/screenshots/apnimed-2026-08-07T161455.png
security:
- kind: domain-security
  name: Apnimed Domain Security
  slug: apnimed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apnimed
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Healthcare
- Life Sciences
- Sleep Medicine
- Clinical Trials
website: https://apnimed.com/
---
