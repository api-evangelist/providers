---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: Vault Core is Thought Machine's cloud-native core banking engine. Its API surface spans a REST Core API for external integrations (channels, CRM, operator UI), a Posting API that manages financial mov
  name: Thought Machine Vault Core API
  slug: vault-core
- description: Vault Payments is Thought Machine's cloud-native payments processing platform, able to run card, instant, batch clearing and cross-border payment types across schemes and regions. Payments are nativel
  name: Thought Machine Vault Payments API
  slug: vault-payments
artifact_total: 6
asyncapis:
- description: ''
  name: Thought Machine Streaming Events
  slug: thought-machine-streaming-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.thoughtmachine.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thoughtmachine.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.thoughtmachine.net/
- group: company
  title: ''
  type: Blog
  url: https://www.thoughtmachine.net/blog
- group: operate
  title: ''
  type: Support
  url: https://www.thoughtmachine.net/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thought-machine
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thoughtmachine.net/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thoughtmachine.net/api-terms
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thought-machine-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thought-machine-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thought-machine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thought-machine-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thought-machine-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.thoughtmachine.net/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thought-machine-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thought-machine-lifecycle.yml
- group: other
  title: ''
  type: Events
  url: asyncapi/thought-machine-streaming-events.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thought-machine-llms.txt
created: '2026-08-02'
description: 'Thought Machine is a London-headquartered cloud-native core banking technology company founded in 2014 by Paul Taylor, with offices in New York and Singapore. It builds Vault Core, a universal product engine in which every banking product — mortgages, loans, deposits, credit cards, wallets and Islamic finance products — is expressed as a developer-written smart contract executed against a real-time ledger, and Vault Payments, a cloud-native payments processing platform that natively represents payments as ISO 20022 messages and runs card, instant (FedNow, UK New Payments Architecture, SEPA Instant), batch clearing and cross-border rails. Both products are API-first: Vault Core exposes a REST Core API, a Posting API for financial movements, a Kafka-based Streaming API that emits accounting, balance and customer events in real time, a Migration API for legacy core data, and a Contracts API for smart-contract functions. Deployment is SaaS or bank-hosted on AWS, Azure, GCP, IBM
  Cloud, OpenShift or hybrid. Clients include Lloyds Banking Group, Standard Chartered (Mox), JPMorgan Chase, SEB, ING Poland, Intesa Sanpaolo, Kiwibank, Lunar and Judo Bank. The developer documentation and API reference are published behind a partner login at docs.thoughtmachine.net; a separate TM Sandbox API programme is available by application.'
image: https://cdn.prod.website-files.com/6371f3e94a645913703e255a/6371f3e94a645953333e28d3_TM_Logo_Black%20.svg
layout: provider
modified: '2026-08-02'
name: Thought Machine
nav: Providers
network: true
overview: 'Thought Machine publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Core Banking, Financial Services, and Payments.


  The Thought Machine catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Thought Machine''s developer surface includes documentation, engineering blog, support, sandbox, authentication, and 13 more developer resources.'
random_paper: 51
scopes:
- name: Thought Machine Scopes
  scope_count: 5
  slug: thought-machine-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 41.3
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 40.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Thought Machine Authentication
  slug: thought-machine-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Thought Machine Domain Security
  slug: thought-machine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: thought-machine
tags:
- Company
- Banking
- Core Banking
- Financial Services
- Payments
- Cloud Native
- Smart Contracts
- ISO 20022
- Ledger
- Fintech
- United Kingdom
website: https://www.thoughtmachine.net/
---
