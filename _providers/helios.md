---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.helios.do/
- group: company
  title: ''
  type: Blog
  url: https://blog.helios.do/
- group: operate
  title: ''
  type: HelpCenter
  url: https://intercom.help/heliosdo/fr/
- group: operate
  title: ''
  type: Support
  url: https://www.helios.do/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.helios.do/inscription/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.helios.do/documents/conditions_tarifaires.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.helios.do/documents/Conditions_Generales_Helios.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helios.do/documents/Politique_De_Confidentialite.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helios-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/helios-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/helios-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helios-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helios-domain-security.yml
coverage:
  checked: '2026-08-17'
  detail: helios is a consumer neobank that ships only an end-user mobile and web banking app — it publishes no developer portal, API reference, SDK or webhook surface, and as a payment services agent of OKALI (REGAFI 731225) it exposes no PSD2 dedicated interface of its own; /openapi.json, /graphql, /mcp, /api and every /.well-known/ path return a real 404 on www.helios.do (a nonsense control path also 404s, so these are not soft-404s), and certificate-transparency enumeration of *.helios.do lists app, backoffice, blog, email, go, help and meta but no api.* host of any kind.
  evidence:
  - status: 404
    url: https://www.helios.do/openapi.json
  - status: 404
    url: https://www.helios.do/.well-known/agent-card.json
  - status: 404
    url: https://www.helios.do/api
  - status: 200
    url: https://www.helios.do/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: helios is a French sustainable-banking company (HELIOS SAS, Paris) offering current, Premium, joint, youth, Liberté and independent/professional accounts, a green savings passbook, sustainable life insurance and wooden or recycled-plastic Visa cards through iOS, Android and web. It is a société à mission and a certified B Corp whose promise is that no customer euro finances fossil fuels or polluting industry, and it publishes the list of transition projects it funds. helios is registered in REGAFI under 731225 as a payment services agent of OKALI, the ACPR-approved electronic money institution that services the accounts. It publishes no public API, SDK, webhook or developer portal; the one machine-readable document it serves is an llms.txt AI-usage policy.
image: https://a.storyblok.com/f/279083/1200x630/38722f8a58/meta-image.png
layout: provider
modified: '2026-08-17'
name: helios
nav: Providers
network: true
overview: 'helios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Neobank, and Sustainable Finance.


  helios'' developer surface includes engineering blog, support, signup flow, pricing, and 9 more developer resources.'
plans:
- name: Helios Plans Pricing
  plan_count: 0
  slug: helios-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Helios Rate Limits
  slug: helios-rate-limits
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helios/refs/heads/main/screenshots/helios-2026-09-02T145716.png
security:
- kind: domain-security
  name: Helios Domain Security
  slug: helios-domain-security
  summary_line: TLSv1.3 · DMARC
slug: helios
tags:
- Company
- Banking
- Fintech
- Neobank
- Sustainable Finance
- Payments
- Climate Tech
- France
website: https://www.helios.do/
---
