---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 5
  name: Capchase Agentic Access
  operation_count: 9
  slug: capchase-agentic-access
  summary_line: 9 operations · 5 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://universe.capchase.com/api/v2
  baseurl_source: declared
  description: The Pay API from Capchase — 8 operation(s) for pay.
  name: Capchase Pay API
  slug: capchase-pay-api
arazzos:
- description: Create a buyer, confirm qualification, then create a financed subscription and read its status.
  name: Capchase Qualify a Buyer and Create a Financed Subscription
  slug: capchase-buyer-to-subscription
artifact_total: 8
collections:
- collection_type: open
  name: Capchase Pay API
  slug: open-capchase-pay-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.capchase.com/blog/rss.xml
- group: agent
  href: https://artifacts.apis.io/capchase/mcp/capchase-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/capchase-mcp.yml
- group: other
  href: https://artifacts.apis.io/capchase/overlays/capchase-pay-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/capchase-pay-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.capchase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://capchase.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://capchase.readme.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://capchase.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://capchase.readme.io/docs/get-started
- group: auth
  href: https://artifacts.apis.io/capchase/authentication/capchase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capchase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Capchase
- group: company
  title: ''
  type: Blog
  url: https://www.capchase.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.capchase.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.capchase.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.capchase.com/privacy-policy
- group: operate
  title: ''
  type: Deprecation
  url: https://capchase.readme.io/reference/migrating-from-v1
- group: auth
  title: ''
  type: Compliance
  url: https://www.capchase.com/
- group: agent
  href: https://artifacts.apis.io/capchase/llms/capchase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capchase-llms.txt
- group: start
  href: https://artifacts.apis.io/capchase/sandbox/capchase-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/capchase-sandbox.yml
- group: design
  href: https://artifacts.apis.io/capchase/conventions/capchase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/capchase-conventions.yml
- group: design
  href: https://artifacts.apis.io/capchase/lifecycle/capchase-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/capchase-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/capchase/conformance/capchase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capchase-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capchase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/capchase/security/capchase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capchase-domain-security.yml
created: '2026-07-17'
description: 'Capchase provides embedded financing and B2B payment infrastructure for software and hardware vendors. Its Capchase Pay API lets vendors offer buyers flexible installment payment terms at checkout while the vendor is paid the full contract value upfront. Vendors create buyer companies, run automated KYB/underwriting qualification, create subscriptions that generate hosted payment links, list and retrieve subscription status, and pull instalment receipts. The v2 REST API is served from universe.capchase.com, uses HTTP Basic authentication (clientId / clientSecret), ships a Playground environment, and is documented on a ReadMe developer portal with an OpenAPI reference and an AI-agent llms.txt index. Sector: fintech; backed by QED Investors.'
image: https://cdn.prod.website-files.com/6146543ab50f167ae088b201/61701898ec2756274d6e8665_256px.png
layout: provider
modified: '2026-10-06'
name: Capchase
nav: Providers
network: true
overview: 'Capchase publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Pay API. Tagged areas include Company, Fintech, Payments, Embedded Finance, and Financing.


  Capchase''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, sandbox, and 16 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 47.1
    developer_ergonomics: 61.3
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 26.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/capchase/capchase-2026-07-25T204424.png
security:
- kind: authentication
  name: Capchase Authentication
  slug: capchase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capchase Domain Security
  slug: capchase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Qualify a buyer and create a financed subscription
  slug: capchase-qualify-buyer-and-finance
- name: Reconcile subscriptions and pull instalment receipts
  slug: capchase-reconcile-subscriptions
slug: capchase
tags:
- Company
- Fintech
- Payments
- Embedded Finance
- Financing
- B2B SaaS
- Revenue Financing
- Buy Now Pay Later
- KYB
- Underwriting
website: https://www.capchase.com/
---
