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
  url: security/expressable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.expressable.com/
- group: company
  title: ''
  type: About
  url: https://www.expressable.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.expressable.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.expressable.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.expressable.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.expressable.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.expressable.com/learning-center
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/expressable-llms.txt
- group: commercial
  title: ''
  type: NoticeOfPrivacyPractices
  url: https://www.expressable.com/notice-of-privacy-practices
- group: other
  title: ''
  type: Accessibility
  url: https://www.expressable.com/accessibility-statement
- group: commercial
  title: ''
  type: Plans
  url: plans/expressable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/expressable-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/expressable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.expressable.com/notice-of-privacy-practices
coverage:
  checked: '2026-08-12'
  detail: Expressable is a direct-to-consumer telehealth speech-therapy practice whose only software surface is a patient client portal at app.expressable.com — a Cloudflare Pages SPA whose bundle calls Stripe, Mixpanel and LaunchDarkly but no first-party API host; there is no api., docs. or developer. subdomain in DNS and every spec path on www.expressable.com 404s.
  evidence:
  - status: 404
    url: https://www.expressable.com/openapi.json
  - status: 404
    url: https://www.expressable.com/graphql
  - status: 404
    url: https://www.expressable.com/.well-known/agent-card.json
  - status: 200
    url: https://www.expressable.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Expressable is an online speech therapy platform based in Austin, Texas that connects children and adults with licensed speech-language pathologists for one-on-one virtual teletherapy sessions across the United States. Founded by speech-language pathologist Leanne Sherred, the company treats speech delays, stuttering, apraxia, aphasia, dysarthria, autism-related communication challenges, voice and swallowing disorders, accent modification and gender-affirming voice training through a client portal at app.expressable.com, and works with both insurance plans and private pay. Expressable is a direct-to-consumer and payer-facing healthcare services company: it publishes an llms.txt for AI agents but no public developer program, API reference, or machine-readable API contract.'
image: https://images.ctfassets.net/w45yni3hcp6l/66LZvHEALOCDaE9QComTUt/60f5f517a8b398af7262138c30e9ff93/home-preview-image.png
layout: provider
modified: '2026-08-12'
name: Expressable
nav: Providers
network: true
overview: 'Expressable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Speech Therapy.


  Expressable''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Expressable Plans Pricing
  plan_count: 0
  slug: expressable-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Expressable Rate Limits
  slug: expressable-rate-limits
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Expressable Domain Security
  slug: expressable-domain-security
  summary_line: TLSv1.3 · HSTS
slug: expressable
tags:
- Company
- Health
- Healthcare
- Telehealth
- Speech Therapy
- Teletherapy
- Digital Health
- Consumer Health
- Behavioral Health
website: https://www.expressable.com/
---
