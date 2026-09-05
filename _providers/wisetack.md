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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Partner-gated REST API for embedding Wisetack pay-over-time financing into vertical SaaS and field service management platforms - create and monitor consumer financing applications with webhook report
  name: Wisetack Partner API
  slug: wisetack-partner-api
artifact_total: 4
asyncapis:
- description: ''
  name: Wisetack Webhooks
  slug: wisetack-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.wisetack.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wisetack-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wisetack-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wisetack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.wisetack.com/responsible-disclosure-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/wisetack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.wisetack.com/blog/announcing-wisetacks-soc-2-type-2-certification
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wisetack-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://support.wisetack.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.wisetack.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wisetack
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wisetack.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.wisetack.com/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wisetack.us/#/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wisetack.us/#/privacy
- group: operate
  title: ''
  type: ContactUs
  url: https://www.wisetack.com/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.wisetack.com/faqs
created: '2026-07-17'
description: Wisetack is an embedded consumer financing (pay-over-time) platform for real-world services. Home service, auto repair, dental, medical, and veterinary businesses offer customers monthly payment options delivered via text or link, with approval in minutes; financing is provided through Wisetack's lending partners. Wisetack embeds into 50+ vertical SaaS and field service management platforms (Housecall Pro, Jobber, JobNimbus, Thryv, Square) through a partner REST API with webhook reporting. Backed by Greylock and Insight Partners; SOC 2 Type 2 certified.
image: https://cdn.prod.website-files.com/5f194315e6b47c1697925302/67817164d9bfb1aad0c6aa30_wisetack-logo.png
layout: provider
modified: '2026-07-21'
name: Wisetack
nav: Providers
network: true
overview: 'Wisetack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Consumer Financing, and Embedded Finance.


  The Wisetack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wisetack''s developer surface includes support, engineering blog, getting-started guide, signup flow, FAQ, and 12 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 34.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wisetack/refs/heads/main/screenshots/wisetack-2026-09-02T170824.png
security:
- kind: domain-security
  name: Wisetack Domain Security
  slug: wisetack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wisetack Vulnerability Disclosure
  slug: wisetack-vulnerability-disclosure
  summary_line: contact published
slug: wisetack
tags:
- Company
- Fintech
- Lending
- Consumer Financing
- Embedded Finance
- Payments
- Home Services
website: https://www.wisetack.com/
---
