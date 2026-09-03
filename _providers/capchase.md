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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
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
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Capchase Pay API
  slug: open-capchase-pay-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/capchase-mcp.yml
- group: other
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
  title: ''
  type: LLMsTxt
  url: llms/capchase-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/capchase-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/capchase-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/capchase-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capchase-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capchase-domain-security.yml
created: '2026-07-17'
description: 'Capchase provides embedded financing and B2B payment infrastructure for software and hardware vendors. Its Capchase Pay API lets vendors offer buyers flexible installment payment terms at checkout while the vendor is paid the full contract value upfront. Vendors create buyer companies, run automated KYB/underwriting qualification, create subscriptions that generate hosted payment links, list and retrieve subscription status, and pull instalment receipts. The v2 REST API is served from universe.capchase.com, uses HTTP Basic authentication (clientId / clientSecret), ships a Playground environment, and is documented on a ReadMe developer portal with an OpenAPI reference and an AI-agent llms.txt index. Sector: fintech; backed by QED Investors.'
image: https://cdn.prod.website-files.com/6146543ab50f167ae088b201/61701898ec2756274d6e8665_256px.png
layout: provider
modified: '2026-07-18'
name: Capchase
nav: Providers
network: true
overview: 'Capchase publishes 1 API on the [APIs.io](https://apis.io/) network: Pay API. Tagged areas include Company, Fintech, Payments, Embedded Finance, and Financing.


  Capchase''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, sandbox, and 15 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 6.6
  previous_composite: 41.7
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
    score: 45.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capchase/refs/heads/main/screenshots/capchase-2026-07-25T204424.png
security:
- kind: authentication
  name: Capchase Authentication
  slug: capchase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capchase Domain Security
  slug: capchase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capchase
tags:
- Company
- Fintech
- Payments
- Embedded Finance
- Financing
- B2B SaaS
- Revenue Financing
- BNPL
- KYB
- Underwriting
website: https://www.capchase.com/
---
