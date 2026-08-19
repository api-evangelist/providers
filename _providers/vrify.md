---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vrify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vrify.com/
- group: company
  title: ''
  type: About
  url: https://vrify.com/about
- group: other
  title: ''
  type: Product
  url: https://vrify.com/product
- group: docs
  title: ''
  type: Documentation
  url: https://help.vrify.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.vrify.com/en/articles/10452792-getting-started-with-vrify-present
- group: operate
  title: ''
  type: Support
  url: https://help.vrify.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.vrify.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://vrify.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://vrify.com/pricing
- group: start
  title: ''
  type: Login
  url: https://admin.vrify.com/
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/vrify-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vrify-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vrify-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vrify-authentication.yml
- group: design
  title: ''
  type: Components
  url: components/vrify-components.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vrify-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/vrify-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vrify-llms.txt
- group: auth
  title: ''
  type: SecurityPage
  url: https://vrify.com/legal/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vrify.com/legal/client-terms-of-service
- group: commercial
  title: ''
  type: UserTermsOfService
  url: https://vrify.com/legal/user-terms-of-service
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://vrify.com/legal/acceptable-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vrify.com/legal/privacy-policy
- group: other
  title: ''
  type: CookieNotice
  url: https://vrify.com/legal/cookie-notice
- group: commercial
  title: ''
  type: Legal
  url: https://vrify.com/legal
- group: company
  title: ''
  type: Blog
  url: https://vrify.com/resources
- group: other
  title: ''
  type: CaseStudies
  url: https://vrify.com/customer-stories
- group: company
  title: ''
  type: Press
  url: https://vrify.com/media
- group: company
  title: ''
  type: Careers
  url: https://vrify.com/careers
- group: learn
  title: ''
  type: Training
  url: https://academy.vrify.com/
- group: docs
  title: ''
  type: Guides
  url: https://guides.vrify.com/
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/vrify/id1235301790
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vrify/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/VRIFYTechnology
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/vrify-stock
coverage:
  checked: '2026-08-05'
  detail: 'VRIFY sells DORA/VRIFY Predict and VRIFY Present as a closed end-user SaaS — the marketing site, sitemap and 488-URL help centre never mention an API, and the only machine surface reachable without credentials is the app''s own Django backend at services.vrify.com/v2/, which answers 401 with WWW-Authenticate: Bearer realm="api" and whose /v2/docs endpoint 302s to a Django staff login.'
  evidence:
  - status: 401
    url: https://services.vrify.com/v2/
  - status: 302
    url: https://services.vrify.com/v2/docs
  - status: 404
    url: https://vrify.com/openapi.json
  - status: 404
    url: https://vrify.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'VRIFY Technology Inc. is a Vancouver, British Columbia software company that builds exploration intelligence software for the mining industry, with a team of geoscientists and AI engineers and a presence in Western Australia. Its platform pairs VRIFY Predict — the DORA AI-assisted mineral discovery product, which trains mineral-system-specific models on a large proprietary global exploration dataset to rank prospectivity targets, score them (VPS) and, since August 2026, quantify prediction uncertainty — with VRIFY Present, an interactive 3D and 360-degree presentation product mining companies use to communicate projects to investors, plus a Files upload/processing and VRIFY Explore data layer and an iOS app. Southern Cross Gold''s 2024 Sunday Creek discovery came from a target DORA identified independently. VRIFY raised a CAD$12.5M Series B in February 2025 led by LGVP with RCF Innovation and Beedie Capital, taking total funding past CAD$30M. VRIFY sells a closed end-user SaaS:
  as of August 2026 it publishes no public API, SDK, developer portal or machine-readable contract. The only machine surfaces a member of the public can reach are the app''s own backend at services.vrify.com/v2/ (401, WWW-Authenticate: Bearer realm="api", with its /v2/docs endpoint 302ing to a Django staff login) and a copy-paste 3D presentation embed customers place on their own company websites.'
image: https://cdn.prod.website-files.com/6787b60d6e8383c2fef24122/67ad320cea9bf38396f831b9_virfy-og-image.png
layout: provider
modified: '2026-08-05'
name: VRIFY
nav: Providers
network: true
overview: 'VRIFY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mining, Mineral Exploration, Geoscience, and Artificial Intelligence.


  VRIFY''s developer surface includes documentation, getting-started guide, support, pricing, changelog, authentication, legal docs, and 29 more developer resources.'
random_paper: 113
score:
  band: thin
  composite: 28.7
  delta: -0.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Vrify Authentication
  slug: vrify-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Vrify Domain Security
  slug: vrify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vrify Trust Center
  slug: vrify-trust-center
  summary_line: SOC 2 Type II
slug: vrify
tags:
- Company
- Mining
- Mineral Exploration
- Geoscience
- Artificial Intelligence
- Machine Learning
- 3D Visualization
- Data Visualization
- Investor Relations
- SaaS
- Canada
website: https://vrify.com/
---
