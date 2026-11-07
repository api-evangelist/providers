---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Wallet Master Solana wallet research tools
  name: Wallet Master API
  slug: wallet-master-api
- baseURL: https://botapi.walletmaster.tools
  baseurl_source: declared
  description: 'Wallet Master API as documented publicly: 51 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Wallet Master API
  slug: walletmaster-tools-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/walletmaster-tools/plans/walletmaster-tools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/walletmaster-tools-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/walletmaster-tools/rules/walletmaster-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/walletmaster-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/walletmaster-tools/vocabulary/walletmaster-tools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/walletmaster-tools-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/walletmaster-tools/authentication/walletmaster-tools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/walletmaster-tools-authentication.yml
- group: design
  href: https://artifacts.apis.io/walletmaster-tools/conformance/walletmaster-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/walletmaster-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/walletmaster-tools/llms/walletmaster-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/walletmaster-tools-llms.txt
- group: other
  href: https://artifacts.apis.io/walletmaster-tools/hosts/walletmaster-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/walletmaster-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/walletmaster-tools/vendors/walletmaster-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/walletmaster-tools-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.walletmaster.tools/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.walletmaster.tools/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.walletmaster.tools/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.walletmaster.tools\\\
- group: auth
  href: https://artifacts.apis.io/walletmaster-tools/security/walletmaster-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/walletmaster-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.walletmaster.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.walletmaster.tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.walletmaster.tools/prices/
- group: company
  title: ''
  type: Blog
  url: https://www.walletmaster.tools/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.walletmaster.tools/contact/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found after exhaustive probing.
  evidence:
  - status: 404
    url: https://api.walletmaster.tools/openapi.json
  - status: 404
    url: https://api.walletmaster.tools/openapi.yaml
  - status: 404
    url: https://api.walletmaster.tools/swagger.json
  - status: 404
    url: https://api.walletmaster.tools/v1/openapi.json
  - status: 404
    url: https://api.walletmaster.tools/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Wallet Master offers an all‑in‑one Solana wallet finder and bulk analysis tools for copy traders. It provides high‑speed market trend monitoring, wallet discovery, and research utilities to help users track and analyze Solana wallets efficiently. The platform includes features such as bulk wallet lookup, real‑time alerts, and integration with popular Solana analytics services, aiming to streamline wallet research for traders and developers alike.
image: https://www.walletmaster.tools/wp-content/uploads/2025/08/server_banner_background.png
layout: provider
modified: '2026-11-04'
name: Wallet Master
nav: Providers
network: true
overview: 'Wallet Master is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solana, Wallets, Cryptocurrency, and Analytics.


  The Wallet Master catalog on APIs.io includes 1 Spectral governance ruleset.


  Wallet Master''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Walletmaster Tools Plans Pricing
  plan_count: 2
  slug: walletmaster-tools-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Wallet Master API Rules
  rule_count: 39
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 2
  slug: walletmaster-tools-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Walletmaster Tools Authentication
  slug: walletmaster-tools-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Walletmaster Tools Domain Security
  slug: walletmaster-tools-domain-security
  summary_line: TLSv1.3
slug: walletmaster-tools
tags:
- Company
- Solana
- Wallets
- Cryptocurrency
- Analytics
website: https://www.walletmaster.tools/
---
