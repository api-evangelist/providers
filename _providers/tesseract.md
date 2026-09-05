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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The clients API from Tesseract — 3 operation(s) for clients.
  name: Tesseract clients API
  slug: tesseract-clients-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The health API from Tesseract — 1 operation(s) for health.
  name: Tesseract health API
  slug: tesseract-health-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The insights API from Tesseract — 5 operation(s) for insights.
  name: Tesseract insights API
  slug: tesseract-insights-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The strategies API from Tesseract — 2 operation(s) for strategies.
  name: Tesseract strategies API
  slug: tesseract-strategies-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The vaults API from Tesseract — 4 operation(s) for vaults.
  name: Tesseract vaults API
  slug: tesseract-vaults-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tesseract Public clients API
  slug: open-tesseract-clients-api
- collection_type: open
  name: Tesseract Public clients health API
  slug: open-tesseract-health-api
- collection_type: open
  name: Tesseract Public clients insights API
  slug: open-tesseract-insights-api
- collection_type: open
  name: Tesseract Public clients strategies API
  slug: open-tesseract-strategies-api
- collection_type: open
  name: Tesseract Public clients vaults API
  slug: open-tesseract-vaults-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tesseract-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tesseract.fi/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tesseract.fi/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tesseract.fi/
- group: docs
  title: ''
  type: APIReference
  url: https://api.vault.tesseract.fi/public/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tesseract.fi/dedicated-client-vaults/integration-guide.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/tesseract-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tesseract-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tesseract-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tesseract-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tesseract-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tesseract-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.tesseract.fi/tesseract/security-and-compliance.md
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tesseract-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tesseract-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tesseract-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tesseract-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tesseract-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tesseract-public-api-overlay.yaml
- group: start
  title: ''
  type: Login
  url: https://app.tesseract.fi
- group: operate
  title: ''
  type: Support
  url: https://tesseract.fi/contact/
- group: company
  title: ''
  type: Blog
  url: https://tesseract.fi/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.tesseract.fi/dedicated-client-vaults/fees-and-commercial-model.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tesseract.fi/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tesseract.fi/privacy-notice/
created: '2026-07-17'
description: Tesseract is a Finnish digital-asset management and crypto-lending company. Tesseract Investment Oy is authorised as a Crypto-Asset Service Provider (CASP) under Regulation (EU) 2023/1114 (MiCA) and supervised by the Finnish Financial Supervisory Authority (FIN-FSA). It operates institutional-grade, per-client on-chain Dedicated Client Vaults (DCVs) on Ethereum mainnet, an Earn API that lets exchanges, neobanks and fintechs offer crypto yield to their users under their own brand, and Earn Direct for referred clients. Developers integrate via a public vault reporting API (unauthenticated reads, EIP-712 signed strategy assignment) and a partner Earn API using OAuth2 client-credentials with a daily net-settlement model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tesseract.png
layout: provider
modified: '2026-07-21'
name: Tesseract
nav: Providers
network: true
overview: 'Tesseract publishes 5 APIs on the [APIs.io](https://apis.io/) network, including clients API, health API, insights API, and 2 more. Tagged areas include Company, Fintech, Cryptocurrency, DeFi, and Lending.


  Tesseract''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 19 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 37.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 42.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tesseract/refs/heads/main/screenshots/tesseract-2026-08-17T082323.png
security:
- kind: authentication
  name: Tesseract Authentication
  slug: tesseract-authentication
  summary_line: none/signature/oauth2 · 3 schemes
- kind: domain-security
  name: Tesseract Domain Security
  slug: tesseract-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tesseract
tags:
- Company
- Fintech
- Cryptocurrency
- DeFi
- Lending
- Yield
- Digital Assets
- Ethereum
- MiCA
- Vault
- Institutional
website: https://tesseract.fi/
---
