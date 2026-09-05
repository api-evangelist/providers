---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Lynx FinHealth API for embedded health accounts, enrollment, contributions, payments and distributions, transactions, and card issuance/management. Reference is gated behind developer login; a hosted '
  name: Lynx API
  slug: lynx-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://lynx-fh.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lynx-fh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lynx-fh.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lynx-fh.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lynx-fh.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lynx-fh.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lynx-fh.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.lynx-fh.co/client-ui/
- group: start
  title: ''
  type: SignUp
  url: https://www.lynx-fh.com/request-lynx-api-access
- group: operate
  title: ''
  type: Support
  url: https://www.lynx-fh.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.lynx-fh.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lynx-fh.com/website-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lynx-fh.com/website-terms-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://www.lynx-fh.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/lynx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lynx-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lynx-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lynx-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lynx-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lynx-llms.txt
created: '2026-07-17'
description: Lynx (Lynx FinHealth) is a healthcare fintech platform that provides embedded banking, payments, benefits, and e-commerce infrastructure for health plans, providers, and digital health companies. Its API-first and white-label platform powers consumer-directed health accounts (HSA/FSA), ICHRA administration, directed and filtered spend accounts, instant physical and virtual card issuance with merchant and SKU-level controls, supplemental benefits, pharmacy access, rewards and incentive programs, and a qualified medical expense (QME) e-commerce marketplace with end-to-end fulfillment. Lynx is SOC 2 and HITRUST certified and exposes a developer hub, dated changelog, hosted sandbox, and Atlassian status page. Surfaced as a portfolio company of Obvious Ventures and enriched from the public Lynx surface (the full API reference, authentication model, and test data are gated behind developer login).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lynx.png
layout: provider
modified: '2026-07-20'
name: Lynx
nav: Providers
network: true
overview: 'Lynx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Fintech, Payments, and Benefits.


  Lynx''s developer surface includes documentation, API reference, getting-started guide, changelog, sandbox, signup flow, support, and 13 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 28.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/screenshots/lynx-2026-07-25T225752.png
security:
- kind: domain-security
  name: Lynx Domain Security
  slug: lynx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lynx
tags:
- Company
- Healthcare
- Fintech
- Payments
- Benefits
- Health Savings Accounts
- Embedded Finance
- Card Issuing
- Insurance
website: https://lynx-fh.com
---
