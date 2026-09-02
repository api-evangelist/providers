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
  url: security/neurelis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neurelis.com/
- group: company
  title: ''
  type: About
  url: https://www.neurelis.com/about-neurelis/
- group: company
  title: ''
  type: Blog
  url: https://www.neurelis.com/neurelis-news/
- group: operate
  title: ''
  type: Support
  url: https://www.neurelis.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neurelis.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neurelis.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.neurelis.com/neurelis-news/signup/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurelis-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurelis-valtoco-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurelis-myneurelis-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Neurelis is a San Diego specialty pharmaceutical manufacturer whose product is a prescription nasal spray, not software — there is no developer subdomain in DNS (api., developer., docs. and portal.neurelis.com all fail to resolve), no GitHub organization, and every OpenAPI/Swagger/GraphQL/.well-known path probed across neurelis.com, valtoco.com, myneurelis.com and intravail.com returned 404.
  evidence:
  - status: 404
    url: https://www.neurelis.com/openapi.json
  - status: 404
    url: https://www.neurelis.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/neurelis
  - status: 200
    url: https://www.neurelis.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Neurelis, Inc. is a privately held San Diego neuroscience and specialty pharmaceutical company founded in 2007 that licenses, develops and commercializes therapies for epilepsy, psychiatry and other central nervous system disorders with high unmet need. Its lead commercial product is VALTOCO (diazepam nasal spray), an FDA-approved acute treatment for intermittent, stereotypic episodes of frequent seizure activity (seizure clusters) in adult and pediatric patients two years of age and older, built on Intravail transmucosal absorption-enhancement technology acquired with Aegis Therapeutics. Neurelis also holds the ProTek and Hydrogel drug-delivery platforms, licenses Intravail to partners such as ARS Pharmaceuticals and Dr. Reddy's/Upsher-Smith, and is advancing the NRL-1049 and NRL-1004 pipeline programs. Neurelis publishes no developer program, no public API and no machine-readable API contract; its only agent-facing machine-readable surface is a set of llms.txt documents served
  on its corporate, product and patient-support properties.
image: https://www.neurelis.com/wp-content/uploads/2024/11/Neurelis_Logo1-1.png
layout: provider
modified: '2026-08-26'
name: Neurelis
nav: Providers
network: true
overview: 'Neurelis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Healthcare, and Neuroscience.


  Neurelis'' developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Neurelis Domain Security
  slug: neurelis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: neurelis
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Healthcare
- Neuroscience
- Epilepsy
- Drug Delivery
- Specialty Pharma
- Biotechnology
website: https://www.neurelis.com/
---
