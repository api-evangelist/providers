---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The clients API from Tesseract — 3 operation(s) for clients.
  name: Tesseract Clients API
  slug: tesseract-clients-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The health API from Tesseract — 1 operation(s) for health.
  name: Tesseract Health API
  slug: tesseract-health-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The insights API from Tesseract — 5 operation(s) for insights.
  name: Tesseract Insights API
  slug: tesseract-insights-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The strategies API from Tesseract — 2 operation(s) for strategies.
  name: Tesseract Strategies API
  slug: tesseract-strategies-api
- baseURL: https://api.vault.tesseract.fi
  baseurl_source: declared
  description: The vaults API from Tesseract — 4 operation(s) for vaults.
  name: Tesseract Vaults API
  slug: tesseract-vaults-api
artifact_total: 18
collections:
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
- group: commercial
  href: https://artifacts.apis.io/tesseract/plans/tesseract-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tesseract-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://tesseract.fi/news/rss.xml
- group: auth
  href: https://artifacts.apis.io/tesseract/security/tesseract-domain-security.yml
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
  href: https://artifacts.apis.io/tesseract/authentication/tesseract-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tesseract-authentication.yml
- group: design
  href: https://artifacts.apis.io/tesseract/conventions/tesseract-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tesseract-conventions.yml
- group: design
  href: https://artifacts.apis.io/tesseract/conventions/tesseract-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tesseract-conventions.yml
- group: design
  href: https://artifacts.apis.io/tesseract/errors/tesseract-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tesseract-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tesseract/data-model/tesseract-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tesseract-data-model.yml
- group: design
  href: https://artifacts.apis.io/tesseract/conformance/tesseract-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tesseract-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.tesseract.fi/tesseract/security-and-compliance.md
- group: design
  href: https://artifacts.apis.io/tesseract/lifecycle/tesseract-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tesseract-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/tesseract/lifecycle/tesseract-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/tesseract-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/tesseract/mcp/tesseract-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tesseract-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tesseract/llms/tesseract-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tesseract-llms.txt
- group: start
  href: https://artifacts.apis.io/tesseract/sandbox/tesseract-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tesseract-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/tesseract/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/tesseract/overlays/tesseract-public-api-overlay.yaml
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
finops:
- has_sources: true
  method: derived
  name: Tesseract Finops
  primary_unit: aum
  service_category: ''
  slug: tesseract-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tesseract.png
layout: provider
modified: '2026-10-06'
name: Tesseract
nav: Providers
network: true
overview: 'Tesseract publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clients API, Health API, Insights API, and 2 more. Tagged areas include Company, Fintech, Cryptocurrency, DeFi, and Lending.


  The Tesseract catalog on APIs.io includes 1 Spectral governance ruleset.


  Tesseract''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 21 more developer resources.'
plans:
- name: Tesseract Plans Pricing
  plan_count: 4
  slug: tesseract-plans-pricing
- name: Tesseract Price Estimates
  plan_count: 0
  slug: tesseract-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Tesseract API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: tesseract-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 33.6
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 52.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tesseract/tesseract-2026-08-17T082323.png
security:
- kind: authentication
  name: Tesseract Authentication
  slug: tesseract-authentication
  summary_line: none/signature/oauth2 · 3 schemes
- kind: domain-security
  name: Tesseract Domain Security
  slug: tesseract-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Assign a yield strategy to a vault (EIP-712 signed)
  slug: tesseract-assign-vault-strategy
- name: Read a client's vault portfolio and performance
  slug: tesseract-read-vault-portfolio
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
