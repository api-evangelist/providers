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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodvest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goodvest.fr/
- group: company
  title: ''
  type: Blog
  url: https://www.goodvest.fr/blog
- group: operate
  title: ''
  type: Support
  url: https://community.goodvest.fr/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Goodvest
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goodvest.fr/tarifs
- group: commercial
  title: ''
  type: Plans
  url: plans/goodvest-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.goodvest.fr/pre-inscription
- group: start
  title: ''
  type: Login
  url: https://app.goodvest.fr/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodvest.fr/conditions-generales-dutilisation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodvest.fr/reglement-general-sur-la-protection-des-donnees
- group: design
  title: ''
  type: Conformance
  url: conformance/goodvest-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.goodvest.fr/informations-durabilite
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goodvest-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Goodvest ships only end-user web and mobile clients; its private gunicorn backend at api.goodvest.fr returns 404 at the root and on every OpenAPI, GraphQL, MCP and /.well-known/ path probed, and the 802-URL public sitemap contains no developer, reference or API page at all.
  evidence:
  - status: 404
    url: https://api.goodvest.fr/openapi.json
  - status: 404
    url: https://api.goodvest.fr/graphql
  - status: 404
    url: https://api.goodvest.fr/.well-known/agent-card.json
  - status: 200
    url: https://www.goodvest.fr/sitemap.xml
  - status: 0
    url: https://developer.goodvest.fr/
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Goodvest is a French mission-driven fintech (entreprise à mission) based in Paris that sells climate-aligned retail savings and investment products: an ISR assurance-vie (Goodvie, insured by Generali), a euro-fund assurance-vie (Goodlife, insured by Spirica), a Plan Épargne Retraite, a minors'' contract, a green Livret d''Épargne backed by CFCAL-Banque, and a Goodvest First private-management tier covering private equity, sustainable real estate, green infrastructure and structured products. Portfolios are screened against a published seven-filter methodology aligned with the Paris Agreement — fossil-fuel exclusion, carbon-footprint and biodiversity analysis — and every unit-linked support carries EU SFDR Article 8 or Article 9 sustainability disclosures. Goodvest SAS is registered with ORIAS (20007544) as an insurance broker and non-exclusive banking intermediary, is a member of ANACOFI-CIF, and is supervised by the ACPR and the AMF. It publishes a complete public fee schedule
  (0% entry, exit, arbitrage and performance fees) but no public API, SDK, webhook surface or developer portal of any kind.'
image: https://cdn.prod.website-files.com/6735d0b3c15a49054e06fe88/67c9766bfd3e213e868d8d80_Open%20graph.avif
layout: provider
modified: '2026-08-17'
name: Goodvest
nav: Providers
network: true
overview: 'Goodvest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Fintech, Financial-Services, and Investing.


  Goodvest''s developer surface includes engineering blog, support, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Goodvest Plans Pricing
  plan_count: 3
  slug: goodvest-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Goodvest Rate Limits
  slug: goodvest-rate-limits
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Goodvest Domain Security
  slug: goodvest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodvest
tags:
- Company
- Climate Tech
- Fintech
- Financial-Services
- Investing
- Wealth Management
- Sustainable Finance
- ESG
- Insurance
- Retirement
- France
website: https://www.goodvest.fr/
---
