---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/desjardins-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/desjardins-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.desjardins.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/desjardins
- group: company
  title: ''
  type: Blog
  url: https://blogues.desjardins.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.desjardins.com/ca/privacy/index.jsp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.desjardins.com/en/terms-use-legal-notes.html
- group: auth
  title: ''
  type: Security
  url: https://www.desjardins.com/en/security.html
- group: operate
  title: ''
  type: Support
  url: https://www.desjardins.com/en/contact-us.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/desjardins-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/desjardins-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/desjardins-llms.txt
created: '2026-07-23'
description: Desjardins Group (Mouvement Desjardins) is the largest cooperative financial group in North America, founded in 1900 in Lévis, Quebec by Alphonse Desjardins. It is a federation of caisses populaires (member-owned credit unions) rather than a share-capital chartered bank, comprising the Fédération des caisses Desjardins du Québec and its subsidiaries, the caisses in Quebec and the Caisse Desjardins Ontario Credit Union, regulated in Quebec by the Autorité des marchés financiers (AMF). It holds roughly CAD $470 billion in assets and serves more than 7.8 million members and clients with personal, business, wealth-management and insurance products. On open finance, Desjardins publishes no first-party public developer portal or downloadable API specification; developer.desjardins.com and other API-portal subdomains do not resolve, and consumer financial-data access is delivered today through third-party aggregators (Flinks, Plaid, Finicity, Tink) via screen-scraping/aggregator connectivity
  rather than a documented Desjardins API. Canada's Consumer-Driven Banking (open-banking) framework is legislated (Budget 2024/2025, overseen by the FCAC) but not yet operational; as a cooperative outside the Big Six, Desjardins may opt in to Phase 1 rather than being mandated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Desjardins Group
nav: Providers
network: true
overview: 'Desjardins Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Caisse Populaire.


  Desjardins Group''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 79
score:
  band: emerging
  composite: 15.5
  delta: -2.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/desjardins/refs/heads/main/screenshots/desjardins-2026-07-25T211754.png
security:
- kind: domain-security
  name: Desjardins Domain Security
  slug: desjardins-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Desjardins Vulnerability Disclosure
  slug: desjardins-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: desjardins
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Caisse Populaire
- Cooperative
- Consumer-Driven Banking
- Data Aggregation
- Quebec
website: https://www.desjardins.com/
---
