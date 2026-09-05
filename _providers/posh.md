---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Posh's customer-facing HTTP API, served from the same gateway that backs the Posh Portal. Posh describes it on its portal page as a "powerful API" that "automates custom reporting" and connects the po
  name: Posh Platform API
  slug: posh-platform-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.posh.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.posh.ai/demo
- group: start
  title: ''
  type: Login
  url: https://app.poshdevelopment.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.posh.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.posh.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/61eb2514f01c7b377af34831/622bb1c684167fcca5a82a3d_posh-terms-of-use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.posh.ai/security-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://poshtechnologies.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.posh.ai/
- group: auth
  title: ''
  type: Security
  url: https://security.posh.ai/item/responsible-disclosure-policy
- group: auth
  title: ''
  type: Compliance
  url: conformance/posh-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/posh-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/posh-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/posh-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/posh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/posh-domain-security.yml
- group: design
  title: ''
  type: Components
  url: components/posh-components.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/posh_stock/
coverage:
  checked: '2026-08-26'
  detail: 'Posh runs a real, live API gateway at api.poshdevelopment.com whose reference surface at /api-docs returns HTTP 403 with the body "RBAC: access denied", so the contract is readable only to an authenticated tenant of the Posh Portal — there is no public developer portal, docs host or spec anywhere on posh.ai or poshdevelopment.com.'
  evidence:
  - status: 403
    url: https://api.poshdevelopment.com/api-docs
  - status: 404
    url: https://api.poshdevelopment.com/api/v1
  - status: 404
    url: https://www.posh.ai/openapi.json
  - status: 200
    url: https://www.posh.ai/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Posh (Posh AI, legally Posh Technologies) is a Boston-headquartered, remote-first conversational and agentic AI company founded in 2018 by Karan Kashyap and Matt McEachern out of MIT's AI lab. Posh builds AI purpose-built for regulated financial institutions — banks and credit unions — combining voice, digital, knowledge and outreach agents on a single governed platform driven by its proprietary REALM reasoning engine and "Operating Procedures" that pair LLM flexibility with code-level policy control. Its product line spans a Voice Assistant for phone banking, a Digital Assistant for web and mobile chat, a Knowledge Assistant for employee search, Posh Answers for website search, Posh Outreach for proactive campaigns, Posh Simulator for role-play training and Posh CoachQA for quality assurance, all managed from the no-code Posh Portal. Posh reports 125+ financial-institution clients and 300+ deployments, and integrates with core banking and contact-center platforms including
  Symitar, Fiserv, Corelation, Jack Henry, NICE CXone, Genesys Cloud, RingCentral and Five9. Posh operates a private, customer-facing HTTP API behind its portal for custom reporting and system integration; that API's reference is not published publicly.
image: https://cdn.prod.website-files.com/633d9e1c482aac9825b27b50/69656b01d26df273a9279698_webclip.png
layout: provider
modified: '2026-08-26'
name: Posh
nav: Providers
network: true
overview: 'Posh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Conversational AI, Agentic AI, Banking, and Credit Unions.


  Posh''s developer surface includes signup flow, engineering blog, support, and 15 more developer resources.'
plans:
- name: Posh Plans Pricing
  plan_count: 0
  slug: posh-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Posh Rate Limits
  slug: posh-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 29.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: UK
      standard: uk-gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 3
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/posh/refs/heads/main/screenshots/posh-2026-09-02T151830.png
security:
- kind: authentication
  name: Posh Authentication
  slug: posh-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Posh Domain Security
  slug: posh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Posh Vulnerability Disclosure
  slug: posh-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Posh Trust Center
  slug: posh-trust-center
  summary_line: SOC 2 Type II, SOC 3, CSA STAR, CSA AI Trustworthy Pledge
slug: posh
tags:
- Artificial Intelligence
- Conversational AI
- Agentic AI
- Banking
- Credit Unions
- Financial-Services
- Customer Service
- Contact Center
- Voice
- Chatbots
- Knowledge-Management
- RegTech
website: https://www.posh.ai/
---
