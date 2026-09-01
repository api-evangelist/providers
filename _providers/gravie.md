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
api_count: 1
apis:
- description: 'Public machine-readable files Gravie posts on behalf of its plan sponsors under the CMS Transparency in Coverage rule (45 CFR 147.211). Files cover in-network negotiated rates for the Cigna and Cigna '
  name: Gravie Transparency in Coverage Machine-Readable Files
  slug: transparency-in-coverage
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gravie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gravie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gravie.com/compliance/transparency-in-coverage/
- group: operate
  title: ''
  type: Support
  url: https://www.gravie.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.gravie.com/perspectives/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.gravie.com/feed/
- group: company
  title: ''
  type: NewsBlog
  url: https://www.gravie.com/news/
- group: other
  title: ''
  type: Podcast
  url: https://www.gravie.com/podcast/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gravieinc
- group: company
  title: ''
  type: Careers
  url: https://www.gravie.com/careers/
- group: start
  title: ''
  type: Login
  url: https://member.gravie.com/login
- group: start
  title: ''
  type: EmployerPortal
  url: https://employer.gravie.com/
- group: start
  title: ''
  type: ProviderPortal
  url: https://gravie-mesa.javelinaweb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gravie.com/compliance/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gravie.com/compliance/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.gravie.com/compliance/
- group: other
  title: ''
  type: TransparencyInCoverage
  url: https://www.gravie.com/compliance/transparency-in-coverage/
- group: other
  title: ''
  type: Glossary
  url: https://www.gravie.com/compliance/glossary/
- group: other
  title: ''
  type: Licensing
  url: https://www.gravie.com/compliance/gravie-licensing/
- group: commercial
  title: ''
  type: LegalNotices
  url: https://www.gravie.com/compliance/legal-notices/
- group: other
  title: ''
  type: ProviderDirectory
  url: https://www.gravie.com/find-providers/
- group: design
  title: ''
  type: Conformance
  url: conformance/gravie-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gravie-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gravie/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gogravie
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/gravie/id1626358793
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/gravie_stock/
created: '2026-08-01'
description: Gravie is a Minneapolis, Minnesota health benefits company founded in 2013 that designs and administers health plans for small and midsize employers. Its flagship product, Comfort, is a level-funded group health plan with zero deductibles and zero copays on most common healthcare services (preventive and primary care, specialist visits, labs and imaging, generic prescriptions and virtual care), paired with Gravie ICHRA (Individual Coverage Health Reimbursement Arrangement) administration, Gravie Pay for out-of-pocket cost financing, Gravie Care member navigation, and a pharmacy benefit. Gravie acts as a third-party administrator on top of partner provider networks (Aetna Signature Administrators, Cigna, Cigna OAP, HPS/Paymedix, and historically PreferredOne), settling claims under payer IDs GRV01 and 62308. Gravie publishes no public developer program or documented API; its machine-readable public surface is the CMS Transparency in Coverage in-network rate and allowed-amount
  files it posts on behalf of plan sponsors, alongside member, employer and provider portals and native iOS/Android member apps served from a private api.gravie.com backend.
image: https://www.gravie.com/wp-content/uploads/2023/03/gravie-logo-green.svg
layout: provider
modified: '2026-08-01'
name: Gravie
nav: Providers
network: true
overview: 'Gravie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Insurance, Health Benefits, Employee Benefits, and Third-Party Administrator.


  Gravie''s developer surface includes documentation, support, engineering blog, and 24 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gravie/refs/heads/main/screenshots/gravie-2026-08-07T165837.png
security:
- kind: domain-security
  name: Gravie Domain Security
  slug: gravie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gravie
tags:
- Company
- Health Insurance
- Health Benefits
- Employee Benefits
- Third-Party Administrator
- ICHRA
- Level Funded
- Transparency In Coverage
- Machine-Readable Files
- Healthcare
- Insurance
- Regulatory
website: https://www.gravie.com/
---
