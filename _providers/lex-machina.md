---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Lex Machina Agentic Access
  operation_count: 57
  slug: lex-machina-agentic-access
  summary_line: 57 operations · 5 acting
api_count: 21
apis:
- description: Alerts.
  name: Lex Machina Alerts API
  slug: lex-machina-alerts-api
- description: Analytics.
  name: Lex Machina Analytics API
  slug: lex-machina-analytics-api
- description: Attorney data.
  name: Lex Machina Attorneys API
  slug: lex-machina-attorneys-api
- description: Provides API authorization.
  name: Lex Machina Authorization API
  slug: lex-machina-authorization-api
- description: Bankruptcy court cases.
  name: Lex Machina Bankruptcy Cases API
  slug: lex-machina-bankruptcy-cases-api
- description: Provides a filter based way to find cases.
  name: Lex Machina Case Query API
  slug: lex-machina-case-query-api
- description: Docket data.
  name: Lex Machina Dockets API
  slug: lex-machina-dockets-api
- description: Entity data.
  name: Lex Machina Entities API
  slug: lex-machina-entities-api
- description: Federal court of appeals cases.
  name: Lex Machina Federal Appeals Cases API
  slug: lex-machina-federal-appeals-cases-api
- description: Federal district court cases.
  name: Lex Machina Federal District Cases API
  slug: lex-machina-federal-district-cases-api
- description: Find matches based on free text searches
  name: Lex Machina Find API
  slug: lex-machina-find-api
- description: ITC Investigations.
  name: Lex Machina ITC Investigations API
  slug: lex-machina-itc-investigations-api
- description: Judge data.
  name: Lex Machina Judges API
  slug: lex-machina-judges-api
- description: Law firm data.
  name: Lex Machina Law Firms API
  slug: lex-machina-law-firms-api
- description: Provides cannonical lists for specific fields.
  name: Lex Machina List API
  slug: lex-machina-list-api
- description: Party data.
  name: Lex Machina Parties API
  slug: lex-machina-parties-api
- description: US patent data.
  name: Lex Machina Patents API
  slug: lex-machina-patents-api
- description: PTAB Trials.
  name: Lex Machina PTAB Trials API
  slug: lex-machina-ptab-trials-api
- description: Finds entities.
  name: Lex Machina Search API
  slug: lex-machina-search-api
- description: State court cases.
  name: Lex Machina State Cases API
  slug: lex-machina-state-cases-api
- description: Provides API status.
  name: Lex Machina Status API
  slug: lex-machina-status-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lex Machina Alerts API
  slug: open-lex-machina-alerts-api
- collection_type: open
  name: Lex Machina Alerts Analytics API
  slug: open-lex-machina-analytics-api
- collection_type: open
  name: Lex Machina Alerts Attorneys API
  slug: open-lex-machina-attorneys-api
- collection_type: open
  name: Lex Machina Alerts Authorization API
  slug: open-lex-machina-authorization-api
- collection_type: open
  name: Lex Machina Alerts Bankruptcy Cases API
  slug: open-lex-machina-bankruptcy-cases-api
- collection_type: open
  name: Lex Machina Alerts Case Query API
  slug: open-lex-machina-case-query-api
- collection_type: open
  name: Lex Machina Alerts Dockets API
  slug: open-lex-machina-dockets-api
- collection_type: open
  name: Lex Machina Alerts Entities API
  slug: open-lex-machina-entities-api
- collection_type: open
  name: Lex Machina Alerts Federal Appeals Cases API
  slug: open-lex-machina-federal-appeals-cases-api
- collection_type: open
  name: Lex Machina Alerts Federal District Cases API
  slug: open-lex-machina-federal-district-cases-api
- collection_type: open
  name: Lex Machina Alerts Find API
  slug: open-lex-machina-find-api
- collection_type: open
  name: Lex Machina Alerts ITC Investigations API
  slug: open-lex-machina-itc-investigations-api
- collection_type: open
  name: Lex Machina Alerts Judges API
  slug: open-lex-machina-judges-api
- collection_type: open
  name: Lex Machina Alerts Law Firms API
  slug: open-lex-machina-law-firms-api
- collection_type: open
  name: Lex Machina Alerts List API
  slug: open-lex-machina-list-api
- collection_type: open
  name: Lex Machina Alerts Parties API
  slug: open-lex-machina-parties-api
- collection_type: open
  name: Lex Machina Alerts Patents API
  slug: open-lex-machina-patents-api
- collection_type: open
  name: Lex Machina Alerts PTAB Trials API
  slug: open-lex-machina-ptab-trials-api
- collection_type: open
  name: Lex Machina Alerts Search API
  slug: open-lex-machina-search-api
- collection_type: open
  name: Lex Machina Alerts State Cases API
  slug: open-lex-machina-state-cases-api
- collection_type: open
  name: Lex Machina Alerts Status API
  slug: open-lex-machina-status-api
- collection_type: open
  name: Lex Machina API
  slug: open-lex-machina
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lex-machina-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lex-machina-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lex-machina-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lex-machina-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lex-machina-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lexisnexis.com/en-us/products/lex-machina.page
- group: start
  title: ''
  type: Portal
  url: https://developer.lexmachina.com/
- group: start
  title: ''
  type: Login
  url: https://law.lexmachina.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lexmachina.com/gettingStarted
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lexmachina.com/support
- group: docs
  title: ''
  type: Documentation
  url: https://api.lexmachina.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.lexisnexis.com/community/insights/legal/lex-machina
- group: company
  title: ''
  type: PressRoom
  url: https://www.lexisnexis.com/community/amp-pressroom/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.lexisnexis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LexMachinaInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lex-machina/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LexMachina
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@LexMachinaInc
- group: operate
  title: ''
  type: Support
  url: https://developer.lexmachina.com/support
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:support@lexmachina.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lexisnexis.com/en-us/terms/general/default.page
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lexisnexis.com/en-us/terms/privacy-policy/default.page
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.lexisnexis.com/en-us/about-us/social-responsibility/data-privacy.page
- group: build
  title: ''
  type: SDKs
  url: https://github.com/LexMachinaInc/python-lexmachina-sync-api-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/LexMachinaInc/node-lexmachina-api-client
- group: other
  title: ''
  type: Agent
  url: https://github.com/LexMachinaInc/lexmachina-agent
- group: build
  title: ''
  type: CodeSample
  url: https://github.com/LexMachinaInc/api-alerting-example
created: '2026-05-25'
description: Lex Machina is a legal analytics platform owned by LexisNexis that transforms raw court documents and dockets into structured datasets so litigators, corporate legal teams, insurers, and judges can make data-driven decisions about cases, courts, judges, lawyers, parties, and damages. The platform covers all 94 federal district courts, the 13 federal courts of appeals, the PTAB, the ITC, bankruptcy courts, and a growing list of state courts (with 18M+ additional state cases for party analytics), and tracks 8,000+ judges, 6,000+ expert witnesses, 146M+ counsel mentions, and 149M+ party mentions across 10M+ cases and 45M+ documents. Lex Machina exposes its Legal Analytics through a public Litigation Analytics API (OAuth 2.0, JWT bearer tokens) at api.lexmachina.com with synchronous Python and Node.js client libraries plus an A2A (Agent-to-Agent) agent for AI/agent integrations. Practice area coverage includes Antitrust, Bankruptcy, Commercial, Consumer Protection, Contracts, Copyright,
  Employment, ERISA, Insurance, Patent, Product Liability, Securities, Tax, Torts, and Trademark litigation. Lex Machina was founded in 2010 as a Stanford University Law School spin-out and was acquired by LexisNexis (RELX) in 2015.
features:
- Federal District court coverage across all 94 U.S. district courts
- Federal Appeals coverage across all 13 U.S. courts of appeals (since 2012)
- State court coverage with 18M+ additional cases used for party analytics
- Bankruptcy court case data and bankruptcy judge analytics
- PTAB trial data (Patent Trial and Appeal Board)
- ITC investigation data (International Trade Commission)
- 8,000+ federal and state judges tracked with behavior analytics
- 6,000+ expert witnesses tracked
- 146M+ counsel and 149M+ party mentions indexed across 10M+ cases
- Attorney, Law Firm, Party, Judge, Magistrate, and Patent entity lookups
- Substring search across attorneys, judges, law firms, and parties
- Case Query API with filtering by participants, dates, events, resolutions, findings, remedies, and damages
- District Case Analytics from either an ad-hoc query or a saved Alert
- Saved Alerts with daily run results retrievable by date
- Docket-entry retrieval for federal, state, and ITC dockets
- Reference lists for case resolutions, case tags, case types, courts, damages categories, events, judgment sources, appellate decisions, and appealability rulings
- OAuth 2.0 client-credentials authentication with JWT bearer tokens
- REST + JSON over HTTPS; OpenAPI 3.1.0 specification at /docs
- Official Python (sync) and Node.js client libraries on GitHub
- A2A (Agent-to-Agent) agent for AI/LLM integrations on port 10011
- Protege in Lex Machina — generative-AI analytics assistant in the UI
- 'Practice areas: Antitrust, Bankruptcy, Commercial, Consumer Protection, Contracts, Copyright, Employment, ERISA, Insurance, Patent, Product Liability, Securities, Tax, Torts, Trademark'
- Customer base across AmLaw 100/200 firms, corporate legal departments, insurers, government agencies, and law schools
- Apache-2.0 licensed client SDKs and example code on GitHub
- SOC 2 and ISO certifications via LexisNexis enterprise security program
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lex-machina.png
layout: provider
modified: '2026-05-25'
name: Lex Machina
nav: Providers
network: true
overview: 'Lex Machina publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Analytics API, Attorneys API, and 18 more. Tagged areas include Legal, Legal Analytics, Legal Technology, Litigation, and Litigation Analytics.


  Lex Machina''s developer surface includes authentication, developer portal, documentation, engineering blog, YouTube channel, support, and 21 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 34.6
  delta: -8.2
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 59.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 40.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lex-machina/refs/heads/main/screenshots/lex-machina-2026-06-20T184441.png
security:
- kind: authentication
  name: Lex Machina Authentication
  slug: lex-machina-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lex Machina Domain Security
  slug: lex-machina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lex Machina Vulnerability Disclosure
  slug: lex-machina-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lex Machina Trust Center
  slug: lex-machina-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: lex-machina
tags:
- Legal
- Legal Analytics
- Legal Technology
- Litigation
- Litigation Analytics
- Court Data
- Dockets
- Judges
- Law Firms
- Attorneys
- Patents
- PTAB
- ITC
- Bankruptcy
- Appeals
- State Courts
- Federal Courts
- LexisNexis
- Data
- Analytics
website: https://www.lexisnexis.com/en-us/products/lex-machina.page
---
